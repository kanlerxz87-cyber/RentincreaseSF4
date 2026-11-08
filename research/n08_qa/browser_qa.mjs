#!/usr/bin/env node
/**
 * Independent, read-only QA. Never edits the site or its validation report.
 * Usage: node browser_qa.mjs --site /path/to/public-site --url http://127.0.0.1:8000 --out /path/to/results
 * The server must serve only public files, never .git or private intake.
 * Checks WCAG A/AA automated rules, two viewport sizes, keyboard focus,
 * document overflow, table scrolling, internal HTTP links and fragments.
 * Automated accessibility checks are not a complete accessibility audit.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import {chromium as playwright} from 'playwright';
import AxeBuilder from '@axe-core/playwright';
import chromium, {inflate, setupLambdaEnvironment} from '@sparticuz/chromium';
import {fileURLToPath} from 'node:url';

function arg(name, fallback) {
  const i = process.argv.indexOf(name);
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}
const site = path.resolve(arg('--site', '.'));
const base = arg('--url', 'http://127.0.0.1:8000').replace(/\/$/, '');
const out = path.resolve(arg('--out', '.arena/n08-qa/results'));
await fs.mkdir(out, {recursive: true});
const files = ['index.html'];
for (const name of (await fs.readdir(path.join(site, 'pages'))).sort()) {
  if (name.endsWith('.html')) files.push(`pages/${name}`);
}
const report = {checkedAt: new Date().toISOString(), site: null, base, files: [], internalLinks: [], errors: [], notes: [
  'Read-only test; no site files changed.',
  'Axe automated WCAG 2 A/AA and 2.1 A/AA rules only; not a complete accessibility conformance assessment.',
  'External source content is verified separately against official sources; this test checks links, not legal truth.',
  'No raw identifier values are recorded.'
]};
// The npm distribution also bundles the few NSS/NSPR libraries absent on a
// minimal Debian sandbox. Extract them locally; no system package install.
const bin = path.resolve(path.dirname(fileURLToPath(import.meta.resolve('@sparticuz/chromium'))), '../bin');
await inflate(path.join(bin, 'al2023.tar.br'));
setupLambdaEnvironment('/tmp/al2023/lib');
const executablePath = await chromium.executablePath();
const safeArgs = chromium.args.filter(a => !['--disable-web-security', '--allow-running-insecure-content', '--disable-site-isolation-trials'].includes(a));
const browser = await playwright.launch({executablePath, args: safeArgs, headless: true});
const context = await browser.newContext();
const page = await context.newPage();
const internal = new Map();
const external = new Set();
function classify(href, file) {
  if (!href || href.startsWith(('mailto:')) || href.startsWith('tel:') || href.startsWith('javascript:')) return;
  const u = new URL(href, `${base}/${file}`);
  if (u.origin !== base) { external.add(u.href); return; }
  const rel = decodeURIComponent(u.pathname.replace(/^\//, '')) || 'index.html';
  const key = `${rel}${u.hash}`;
  if (!internal.has(key)) internal.set(key, {file: rel, fragment: u.hash.slice(1), from: []});
  internal.get(key).from.push(file);
}
try {
  for (const file of files) {
    const url = `${base}/${file}`;
    const entry = {file, viewports: []};
    for (const viewport of [{width: 1440, height: 1000}, {width: 390, height: 844}]) {
      await page.setViewportSize(viewport);
      const response = await page.goto(url, {waitUntil: 'networkidle'});
      const metrics = await page.evaluate(() => {
        const nav = document.querySelector('nav');
        const wrappers = [...document.querySelectorAll('.tablewrap')];
        return {
          title: document.title,
          h1Count: document.querySelectorAll('h1').length,
          mainCount: document.querySelectorAll('main').length,
          lang: document.documentElement.lang,
          viewportMeta: !!document.querySelector('meta[name="viewport"]'),
          documentWidth: document.documentElement.scrollWidth,
          viewportWidth: innerWidth,
          navHeight: nav?.getBoundingClientRect().height || 0,
          tableCount: document.querySelectorAll('table').length,
          scopedHeaders: document.querySelectorAll('th[scope]').length,
          headerCount: document.querySelectorAll('th').length,
          scrollingTables: wrappers.filter(el => el.scrollWidth > el.clientWidth + 1).length,
          focusableScrollingTables: wrappers.filter(el => el.scrollWidth > el.clientWidth + 1 && el.tabIndex >= 0).length,
          links: [...document.querySelectorAll('a[href]')].map(el => el.getAttribute('href')),
          ids: [...document.querySelectorAll('[id]')].map(el => el.id),
          duplicateIds: [...document.querySelectorAll('[id]')].map(el => el.id).filter((id, i, a) => a.indexOf(id) !== i)
        };
      });
      for (const href of metrics.links) classify(href, file);
      delete metrics.links;
      const ids = new Set(metrics.ids);
      delete metrics.ids;
      const axe = await new AxeBuilder({page}).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
      const violations = axe.violations.map(v => ({id: v.id, impact: v.impact, help: v.help, helpUrl: v.helpUrl, nodes: v.nodes.map(n => ({target: n.target, summary: n.failureSummary}))}));
      const result = {width: viewport.width, height: viewport.height, httpStatus: response?.status(), ...metrics, documentOverflow: metrics.documentWidth > metrics.viewportWidth + 1, violations};
      entry.viewports.push(result);
      if (result.httpStatus !== 200) report.errors.push(`${file}: HTTP ${result.httpStatus}`);
      if (result.documentOverflow) report.errors.push(`${file}: document overflows at ${viewport.width}px`);
      if (result.h1Count !== 1 || result.mainCount !== 1 || result.lang !== 'en') report.errors.push(`${file}: landmark/language defect`);
      if (result.duplicateIds.length) report.errors.push(`${file}: duplicate fragment IDs`);
      if (violations.length) report.errors.push(`${file}: ${violations.length} ${axeRuleIds(violations)}`);
      if (viewport.width === 390 && ['index.html', 'pages/summary.html', 'pages/case.html'].includes(file)) {
        await page.screenshot({path: path.join(out, file.replaceAll('/', '-').replace('.html', '-mobile.png')), fullPage: false});
      }
    }
    // Keyboard smoke test: focus must be visible and not concealed by sticky nav.
    await page.setViewportSize({width: 390, height: 844});
    await page.goto(url, {waitUntil: 'networkidle'});
    const concealed = [];
    for (let i = 0; i < 30; i++) {
      await page.keyboard.press('Tab');
      const focus = await page.evaluate(() => {
        const el = document.activeElement;
        if (!el || el === document.body) return null;
        const r = el.getBoundingClientRect();
        const nav = document.querySelector('nav');
        const nr = nav?.getBoundingClientRect();
        const style = getComputedStyle(el);
        return {tag: el.tagName, text: (el.textContent || '').trim().slice(0, 70), top: r.top, bottom: r.bottom,
          navBottom: nr?.bottom || 0, inNav: !!nav?.contains(el), display: style.display, visibility: style.visibility};
      });
      if (focus && !focus.inNav && focus.display !== 'none' && focus.visibility !== 'hidden' && focus.top < focus.navBottom && focus.bottom > 0) concealed.push(focus);
    }
    entry.keyboard = {tabs: 30, concealedByStickyNav: concealed};
    report.files.push(entry);
    console.log(`${file}: ${entry.viewports.map(v => `${v.width}px=${v.violations.length} axe rules`).join(', ')}`);
  }
  for (const [key, link] of internal) {
    const url = `${base}/${encodeURI(link.file)}`;
    let status = null;
    let fragmentFound = null;
    try {
      const response = await context.request.get(url);
      status = response.status();
      if (status === 200 && link.fragment) {
        const html = await response.text();
        // Generated pages use simple quoted IDs; parse in a browser if needed.
        const p = await context.newPage();
        await p.setContent(html);
        fragmentFound = await p.evaluate(id => !!document.getElementById(id), link.fragment);
        await p.close();
      }
    } catch (err) { report.errors.push(`Internal request failed: ${link.file}`); }
    const ok = status === 200 && (!link.fragment || fragmentFound === true);
    report.internalLinks.push({...link, from: [...new Set(link.from)], status, fragmentFound, ok});
    if (!ok) report.errors.push(`Broken internal link: ${key}`);
  }
  report.externalLinkCount = external.size;
  report.summary = {
    htmlFiles: report.files.length,
    viewportChecks: report.files.reduce((n, f) => n + f.viewports.length, 0),
    internalLinkTargets: report.internalLinks.length,
    brokenInternalLinks: report.internalLinks.filter(l => !l.ok).length,
    axeViolationInstances: report.files.reduce((n, f) => n + f.viewports.reduce((m, v) => m + v.violations.reduce((k, v) => k + v.nodes.length, 0), 0), 0),
    errors: report.errors.length
  };
} finally {
  await browser.close();
  await fs.writeFile(path.join(out, 'browser-report.json'), JSON.stringify(report, null, 2) + '\n');
}
function axeRuleIds(violations) { return `axe rules [${violations.map(v => v.id).join(', ')}]`; }
console.log(JSON.stringify(report.summary, null, 2));
// Accessibility findings are review findings, not a broken-link/build failure.
process.exitCode = report.internalLinks.some(l => !l.ok) || report.files.some(f => f.viewports.some(v => v.httpStatus !== 200 || v.documentOverflow)) ? 1 : 0;
