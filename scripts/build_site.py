#!/usr/bin/env python3
"""Build the static GitHub Pages site, JSON exports and markdown deliverables.

Run: python3 scripts/build_site.py
The generated files are committed so legacy main/root GitHub Pages works without CI.
"""
import json
import re
from html import escape
from pathlib import Path

import site_data as D

ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "pages"
DATA_DIR = ROOT / "data"
ASSETS_DIR = ROOT / "assets"

BADGE = {
    "rule checked": ("verified", "rule checked"),
    "verified": ("verified", "rule checked"),
    "project checked": ("project", "project checked"),
    "owner supplied": ("owner", "owner supplied"),
    "analysis": ("analysis", "analysis"),
    "needs review": ("review", "needs review"),
    "source listed": ("listed", "source listed"),
}


def esc(value):
    return escape(str(value), quote=True)


def badge(status):
    cls, label = BADGE.get(status, ("listed", status))
    return f'<span class="badge {cls}">{esc(label)}</span>'


def source_links(source_ids, source_note=""):
    parts = []
    if source_note:
        parts.append(f'<span class="owner-src">{esc(source_note)}</span>')
    for sid in source_ids:
        src = D.SOURCES.get(sid)
        if not src:
            parts.append(f'<span class="src-id">{esc(sid)}</span>')
            continue
        parts.append(
            f'<a href="{esc(src["url"])}" target="_blank" rel="noopener" title="{esc(src["agency"])} — {esc(src["title"])}">'
            f'{esc(src["title"])} <span class="src-id">({esc(sid)})</span></a>'
        )
    return '<div class="src">' + "".join(parts) + "</div>"


def render_table(section):
    cols = section.get("columns", ["Item", "Value / finding", "Status", "Official source(s)", "Notes / flag"])
    head = "".join(f"<th>{esc(c)}</th>" for c in cols)
    body = []
    for r in section["rows"]:
        value = r.get("value", "")
        if r.get("status") == "needs review" and not value:
            value_cell = '<td class="blank">(blank — not confirmed)</td>'
        else:
            value_cell = f"<td>{esc(value)}</td>"
        notes = esc(r.get("notes", ""))
        if r.get("flag_id"):
            notes += f' <a class="flaglink" href="flagged.html#{esc(r["flag_id"])}">{esc(r["flag_id"])}</a>'
        body.append(
            "<tr>"
            f'<td><strong>{esc(r["label"])}</strong><div class="small">{esc(r["id"])}</div></td>'
            f"{value_cell}"
            f'<td>{badge(r.get("status", ""))}</td>'
            f'<td>{source_links(r.get("source_ids", []), r.get("source_note", ""))}</td>'
            f"<td>{notes}</td>"
            "</tr>"
        )
    return f'<div class="tablewrap"><table><thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


def render_flag_table():
    head = "".join(f"<th>{esc(c)}</th>" for c in ["Flag", "Issue", "Detail", "Status", "Official source(s)"])
    body = []
    for f in D.FLAGS:
        body.append(
            f'<tr id="{esc(f["id"])}"><td><strong>{esc(f["id"])}</strong></td>'
            f'<td>{esc(f["title"])}</td><td>{esc(f["detail"])}</td>'
            f'<td>{badge("needs review")}</td><td>{source_links(f["source_ids"])}</td></tr>'
        )
    return f'<div class="tablewrap"><table><thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


def nav_html(active=""):
    quick = ['<a href="../index.html">Home</a>']
    for slug, title in [("summary", "Summary"), ("process", "License steps"), ("flagged", "Flagged"), ("sources", "Sources")]:
        cls = ' class="active"' if active == slug else ""
        quick.append(f'<a href="{slug}.html"{cls}>{esc(title)}</a>')
    groups = []
    for title, items in D.NAV_GROUPS:
        links = []
        for slug, label in items:
            cls = ' class="active"' if active == slug else ""
            links.append(f'<a href="{slug}.html"{cls}>{esc(label)}</a>')
        links = "".join(links)
        groups.append(f'<div><h3>{esc(title)}</h3>{links}</div>')
    return (
        '<nav aria-label="Site navigation"><div class="wrap">'
        + "".join(quick)
        + '<details class="nav-groups"><summary>All categories</summary><div class="nav-panel">'
        + "".join(groups)
        + "</div></details></div></nav>"
    )


def privacy_strip():
    return (
        '<div class="privacy-strip"><div class="wrap"><strong>Privacy history warning:</strong> '
        'current placeholders do not erase earlier public Git/PR exposure. '
        '<a href="pages/flagged.html#F26">Read F26/F38</a> · '
        '<a href="research/privacy/HISTORY_EXPOSURE.md">remediation limits</a>.</div></div>'
    )


def page_shell(title, body, active="", root=False):
    prefix = "" if root else "../"
    nav = '<nav aria-label="Site navigation"><div class="wrap"><a href="index.html">Home</a></div></nav>' if root else nav_html(active)
    strip = privacy_strip() if root else privacy_strip().replace('href="pages/', 'href="').replace('href="research/', 'href="../research/')
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} · Rental increase SF</title><link rel="stylesheet" href="{prefix}assets/site.css"></head>
<body><a class="skip-link" href="#main">Skip to content</a>
<header><div class="wrap"><h1>{esc(title)}</h1><p>Rental increase SF · official-source-linked compliance research</p>
<p class="meta">Ledger date {esc(D.DATE)} UTC · {D.SOURCE_COUNT} distinct official URLs · {D.FLAG_COUNT} flagged items · not legal advice</p></div></header>
{strip}{nav}<main id="main" class="wrap">{body}</main>
<footer><div class="wrap">Informational research, not legal advice. No attorney approval or guarantee.
<a href="{prefix}pages/sources.html">Sources</a> · <a href="{prefix}SOURCES.md">SOURCES.md</a> ·
<a href="{prefix}data/validation_report.json">Validation report</a> · <a href="{prefix}COORDINATION.md">Coordination</a> ·
<a href="{prefix}research/privacy/HISTORY_EXPOSURE.md">Privacy history</a></div></footer>
<script src="{prefix}assets/site.js"></script></body></html>"""


def inline_md(raw):
    tokens = []

    def stash(html):
        token = f"\x00{len(tokens)}\x00"
        tokens.append(html)
        return token

    def md_link(m):
        label, url = m.group(1), m.group(2)
        return stash(f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(label)}</a>')

    def bare_link(m):
        url = m.group(0)
        trailing = ""
        while url and url[-1] in ".,;:)":
            trailing = url[-1] + trailing
            url = url[:-1]
        return stash(f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(url)}</a>') + trailing

    raw = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", md_link, raw)
    raw = re.sub(r"https?://[^\s<>]+", bare_link, raw)
    out = esc(raw)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    for i, html in enumerate(tokens):
        out = out.replace(f"\x00{i}\x00", html)
    return out


def render_summary_narrative():
    parts = ['<article class="narrative panel" aria-label="Executive summary narrative">']
    list_type = None

    def close_list():
        nonlocal list_type
        if list_type:
            parts.append(f"</{list_type}>")
            list_type = None

    for line in D.EXECUTIVE_SUMMARY_TEXT.splitlines():
        s = line.strip()
        if not s:
            close_list()
            continue
        if s.startswith("# ") and not s.startswith("## "):
            close_list()
            continue
        if s.startswith("## "):
            close_list()
            parts.append(f"<h2>{inline_md(s[3:])}</h2>")
        elif s.startswith("- "):
            if list_type != "ul":
                close_list()
                parts.append("<ul>")
                list_type = "ul"
            parts.append(f"<li>{inline_md(s[2:])}</li>")
        elif re.match(r"^\d+\.\s", s):
            if list_type != "ol":
                close_list()
                parts.append("<ol>")
                list_type = "ol"
            item = re.sub(r"^\d+\.\s", "", s)
            parts.append(f"<li>{inline_md(item)}</li>")
        else:
            close_list()
            parts.append(f"<p>{inline_md(s)}</p>")
    close_list()
    parts.append("</article>")
    return "\n".join(parts)


def search_bar():
    return (
        '<div class="searchbar"><label for="table-search">Search this page</label>'
        '<input id="table-search" type="search" data-table-search placeholder="Filter rows by keyword, source or flag">'
        '<span class="count" data-search-count aria-live="polite"></span></div>'
    )


def page_html(slug, page=None):
    page = page or D.PAGES[slug]
    parts = [f'<div class="hero"><h2>{esc(page["title"])}</h2><p>{esc(page.get("intro", "Official-source-linked tables for this category."))}</p>',
             f'<div class="disclaimer">{esc(D.DISCLAIMER)}</div></div>']
    if slug == "summary":
        parts.append(render_summary_narrative())
        parts.append("<h2>Evidence tables</h2>")
    elif slug == "flagged":
        parts.append('<div class="flagged-banner"><strong>Flagged for Review.</strong> These items do <strong>not</strong> block publication. Unverified case cells are blank; nonblocking does not mean verified.</div>')
    parts.append(search_bar())
    if slug == "flagged":
        parts.append(f"<section><h2>All {D.FLAG_COUNT} flags</h2>{render_flag_table()}</section>")
    elif slug == "sources":
        parts.append(f'<section><h2>Source registry</h2><p>{D.SOURCE_ENTRY_COUNT} entries, {D.SOURCE_COUNT} distinct URLs. Duplicate research aliases are retained for continuity but not counted as separate sources.</p>{render_table(page["sections"][0])}</section>')
    else:
        for sec in page["sections"]:
            parts.append(f'<section><h2>{esc(sec["title"])}</h2>{render_table(sec)}</section>')
    return page_shell(page["title"], "\n".join(parts), active=slug)


def card_value(raw):
    if raw == "auto:sources":
        return str(D.SOURCE_COUNT)
    if raw == "auto:flags":
        return str(D.FLAG_COUNT)
    return raw


def index_html():
    cards = []
    for title, value, slug, desc in D.CARDS:
        cards.append(
            f'<div class="card"><div class="k">{esc(title)}</div><div class="v">{esc(card_value(value))}</div>'
            f'<div class="d">{esc(desc)}</div><a href="pages/{slug}.html">Open {esc(title)}</a></div>'
        )
    groups = []
    for title, items in D.NAV_GROUPS:
        links = "".join(f'<li><a href="pages/{slug}.html">{esc(label)}</a></li>' for slug, label in items)
        groups.append(f'<div class="card"><div class="k">{esc(title)}</div><ul>{links}</ul></div>')
    body = f"""
<div class="hero"><h2>Direct answer: individual owners use the Housing Inventory and license process</h2>
<p>For a covered rent-controlled unit, an individual owner must report into the Housing Inventory and have a current Rent Increase License before an annual or banked increase takes effect. No individual-owner or small-building exemption was found on the official pages reviewed. The official condition is the effective date; the safest order is report, verify license, check the tenancy, then serve notice.</p>
<ol><li>Confirm coverage privately with the exact address/APN.</li><li>Report each unit at the Rent Board Portal.</li><li>Verify the license for the intended effective date.</li><li>Check lease type, anniversary, history, base rent and retaliation risk.</li><li>Calculate only supported amounts; serve and document a compliant notice.</li></ol>
<a class="cta" href="pages/process.html">Step-by-step license process</a><a class="cta secondary" href="pages/summary.html">Executive summary</a><a class="cta secondary" href="pages/flagged.html">Flagged for Review</a>
<div class="disclaimer">{esc(D.DISCLAIMER)}</div></div>
<div class="cards">{''.join(cards)}</div>
<section><h2>Two anonymized units — illustrations, not approvals</h2><div class="unit-grid">
<div class="unit"><h3>Unit 1</h3><p>Supplied rent $3,995 × 1.6% = $63.92</p><div class="amount">$4,058.92 illustration</div><p class="small">Coverage, license, lease, anniversary and history unverified.</p><a href="pages/calculations.html">Calculations</a></div>
<div class="unit"><h3>Unit 2</h3><p>Supplied last-lease rent $3,150 × 1.6% = $50.40</p><div class="amount">$3,200.40 illustration</div><p class="small">Current rent, banking and effective date unverified; banked cells blank.</p><a href="pages/case.html">Anonymized case</a></div>
</div></section>
<section><h2>How to read this dashboard</h2><div class="legend">{badge('rule checked')} official rule text fetched/checked · {badge('project checked')} repository/platform workflow checked · {badge('owner supplied')} anonymized intake, not government-verified · {badge('analysis')} derived, conditional · {badge('needs review')} blank/unconfirmed, flagged · {badge('source listed')} listed with fetch limitation.</div>
<p class="small">Every table row links to official rule or project-platform sources. Owner rows say explicitly that the links are governing rules, not proof of intake. Structural validation is not legal verification.</p></section>
<section><h2>Browse by category</h2><div class="cards">{''.join(groups)}</div></section>
"""
    return page_shell("Rental increase SF", body, root=True)


def sources_section():
    rows = []
    for sid, src in D.SOURCES.items():
        limited = src.get("checked") == "listed / fetch limitation" or src.get("alias_of")
        rows.append({
            "id": sid,
            "label": f'{src["agency"]} — {src["title"]}',
            "value": src["statement"],
            "status": "source listed" if limited else "rule checked",
            "source_ids": [sid],
            "notes": f'{src.get("category", "")} · checked {src.get("checked", D.DATE)}' + (f' · alias of {src["alias_of"]}' if src.get("alias_of") else ""),
            "flag_id": "F40" if src.get("alias_of") else "",
            "source_note": "",
        })
    return [{"title": "Official sources", "columns": ["Source", "What it supports", "Check status", "Official link", "Category / check date"], "rows": rows}]


def write_json(name, obj):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    PAGES_DIR.mkdir(exist_ok=True)
    DATA_DIR.mkdir(exist_ok=True)
    ASSETS_DIR.mkdir(exist_ok=True)
    pages = dict(D.PAGES)
    pages["sources"] = {"title": "Sources", "intro": "Official source registry with check dates and limitations.", "sections": sources_section()}
    pages["flagged"] = {"title": "Flagged for Review", "intro": "Open questions, source conflicts and project limitations.", "sections": []}
    write_json("pages.json", pages)
    for slug, page in pages.items():
        write_json(f"{slug}.json", page)
        if slug != "flagged":
            (PAGES_DIR / f"{slug}.html").write_text(page_html(slug, page), encoding="utf-8")
    (PAGES_DIR / "flagged.html").write_text(page_html("flagged", pages["flagged"]), encoding="utf-8")
    write_json("sources.json", [{"id": sid, **src} for sid, src in D.SOURCES.items()])
    write_json("flags.json", D.FLAGS)
    write_json("summary.json", {"date": D.DATE, "source_entries": D.SOURCE_ENTRY_COUNT, "distinct_source_urls": D.SOURCE_COUNT, "flags": D.FLAG_COUNT, "pages": len(pages)})
    (ROOT / "index.html").write_text(index_html(), encoding="utf-8")
    (ASSETS_DIR / "site.css").write_text(D.CSS_TEXT, encoding="utf-8")
    (ASSETS_DIR / "site.js").write_text(D.JS_TEXT, encoding="utf-8")
    (ROOT / "EXECUTIVE_SUMMARY.md").write_text(D.EXECUTIVE_SUMMARY_TEXT, encoding="utf-8")
    (ROOT / "FLAGGED_FOR_REVIEW.md").write_text(D.FLAGGED_TEXT, encoding="utf-8")
    (ROOT / "README.md").write_text(D.README_TEXT, encoding="utf-8")
    sources_md = ["# Sources", "", f"{D.SOURCE_ENTRY_COUNT} entries; {D.SOURCE_COUNT} distinct URLs. Checked 2026-11-08 unless a limitation is stated.", ""]
    for sid, src in D.SOURCES.items():
        sources_md.append(f'## {sid} — {src["agency"]} — {src["title"]}')
        sources_md.append(f'- URL: {src["url"]}')
        sources_md.append(f'- Category: {src.get("category", "")}; checked: {src.get("checked", D.DATE)}')
        sources_md.append(f'- Supports: {src["statement"]}')
        if src.get("alias_of"):
            sources_md.append(f'- Alias of {src["alias_of"]}; not a distinct URL.')
        sources_md.append("")
    (ROOT / "SOURCES.md").write_text("\n".join(sources_md), encoding="utf-8")
    print(f"Built {len(pages)} pages, {D.SOURCE_ENTRY_COUNT} source entries ({D.SOURCE_COUNT} distinct URLs), {D.FLAG_COUNT} flags.")


if __name__ == "__main__":
    main()
