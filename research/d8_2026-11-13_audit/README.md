# D8-01 — independent audit of the public dashboard

**Checked:** 2026-11-13 UTC<br>
**Audited baseline:** `main` at `1a5b82435cea8f171a97c246eee15592174dc2a2`<br>
**Browser-test archive:** this branch at `1f01a84`; its public site files match audited-baseline `main` `1a5b824`.<br>
**Scope:** user-facing decision workflow, rendered-table/source traceability, navigation/accessibility, build and live Pages. No legal-source or full-history privacy audit was repeated.

## Outcome

No broken build, broken internal link, blocking browser error or Axe finding was found. The live Pages build is successful. The decision pages provide an ordered route through the owner-facing questions, keep unresolved case values blank, and link those blanks to discovery steps. Three non-blocking follow-ups are recorded below: source-count/source-type wording, one landing-page table-header semantic detail, and a stale print/mobile suggestion. No shared site file or generator was changed in this audit.

## Prior work relied on

T58 independently re-checked the forefront official Rent Board materials and recorded the full-history privacy finding. D8 relies on that completed work instead of repeating it: [T58 record in `COORDINATION.md`](../../COORDINATION.md), [full-history scan](../privacy/FULL_HISTORY_SCAN_2026-11-13.md), [PR #59](https://github.com/kanlerxz87-cyber/RentincreaseSF4/pull/59), and [PR #60](https://github.com/kanlerxz87-cyber/RentincreaseSF4/pull/60). F44/F51/F56 remain owner-actionable; no identifiers were copied, and no history rewrite was attempted.

## Decision workflow and navigation

Live pages checked: [dashboard](https://kanlerxz87-cyber.github.io/RentincreaseSF4/), [Decision Readiness](https://kanlerxz87-cyber.github.io/RentincreaseSF4/pages/decision.html), [Suggestions](https://kanlerxz87-cyber.github.io/RentincreaseSF4/pages/suggestions.html), and [Sources](https://kanlerxz87-cyber.github.io/RentincreaseSF4/pages/sources.html).

- The landing page leads with the state-versus-local question, then the individual-owner license question, and links onward to the process, fee, rates, case, federal/market, Q&A, decision, suggestions, worksheet, sources and flagged pages. The category pages are in navigation.
- Decision Readiness has **five ordered gates**, **20 open questions**, **four decision paths**, and review criteria LR-01–LR-11. Its **eight** unconfirmed cells stay blank/flagged and name a discovery route. The paths distinguish ordinary, deferred, higher/petition-based, and no-increase outcomes without selecting one for the owner.
- The Suggestions page presents a review process (read, check evidence, choose, record, then implement). The validator found no pre-approved proposal; review checklists remain blank. Site-only suggestions are identified as project work rather than legal rules.
- Case and calculation pages preserve the supplied dates/amounts and use placeholders. The current validator checks blank/flagged unverified values and rejects raw initials/address patterns in the current public case files. This is a current-tree check, not a history scrub.

## Table and source traceability

Local gates: `scripts/build_site.py` completed (24 data JSON files, 22 category HTML pages, landing page, CSS, `.nojekyll`, and three Markdown deliverables). `scripts/validate_site.py` passed **162 checks, 0 errors**; the committed validation summary is [`data/validation_report.json`](../../data/validation_report.json). Its checks include source-ID resolution, nonempty row citations, rendered table-row links, blank/flagged unknowns, unique row IDs, and navigation targets.

I separately counted source types rather than treating the validator's domain allowlist as proof of government authority:

- The ledger has **93 sources total: 91 government/court/SEC sources plus two GitHub project records** (`S68` repository, `S69` Pages build API).
- The 499 JSON-backed rows all have resolved source IDs. **20 rows cite only project records** (REQ-02/13/14/19/20; Q-24; SUG-P4/P5, SUG-B4/B6, SUG-G1–G5; CL-G1–G5); these describe repository, deployment or site-work facts, not rent-law findings. Seven other rows combine a project record with government/SEC sources. The project rows link to the repository/build record rather than an irrelevant legal citation.
- The validator parses **614 rendered table rows** and requires an HTTPS link on an allowed domain. Its allowlist intentionally includes `github.com` and `api.github.com` for those project records, so “validation passed” does not mean every one of the 614 rows has a government/legal source.
- **Labeling mismatch:** the live dashboard calls all 93 “official government and SEC links,” and the Sources page says every table row links to government or SEC sources. Those phrases omit the two project records and the 20 project-only rows. The rows have traceable project records, but the public wording should distinguish legal authorities from project evidence. This is an editorial follow-up, not a rent-rule defect.

The 23 owner-supplied case rows are labelled as owner facts and carry contextual official links and flags; those links do not certify the owner facts. This follows the user’s rule not to fill unknown values by inference.

## Browser and accessibility QA

The read-only [N08 Playwright/Axe test](../n08_qa/browser_qa.mjs) ran against a `git archive` copy of public files at `1f01a84`; `.git` and private intake were not served. The machine-readable output is [`browser-qa.json`](browser-qa.json).

- **23 HTML pages × 2 viewports = 46 loads** (1440×1000 and 390×844); **55 internal targets**, **0 broken links**.
- **0 Axe WCAG 2 A/AA and 2.1 A/AA violation instances**, **0 review findings**, and **0 blocking errors**.
- **0** document overflows, duplicate IDs, or focus targets concealed behind navigation. All **59/59** horizontally scrolling table wrappers were keyboard-focusable.
- Minor semantics/usability observations: the landing-page quick-navigation table has **three `<th>` elements and none declares `scope="col"`** (Axe reported no violation); mobile navigation is about **324 px** tall at 390×844, but is non-sticky and does not cause document overflow.
- The CSS already contains print styling and a narrow-screen media query. Internal suggestion **SUG-G5** still proposes adding both, so its proposal text is stale. No stylesheet or suggestion was changed.

This was local browser automation, not a hosted-browser run. External URLs were not crawled by Playwright; source reachability/legal content is outside this browser report and is covered by the inherited source ledger/T58 where applicable.

## Live Pages and build

At the audited baseline, the Pages API reported `built`, legacy source `main` `/`, HTTPS enforced; baseline build commit was `1a5b82435cea8f171a97c246eee15592174dc2a2`, with no build error. After PR [#61](https://github.com/kanlerxz87-cyber/RentincreaseSF4/pull/61) merged at 2026-11-13T12:54:16Z as `a010361b829dfb1ea0a2d99ba7ad0051287afa4b`, CI `validate` passed and Pages reached `built` with no error for that merge commit (updated 12:54:40Z). The `fetch_page` tool re-read the live dashboard and Decision Readiness after that build; the live `data/validation_report.json` also reported `passed`. API and publication evidence is in [`live-pages.json`](live-pages.json). Sandbox `curl` to the `github.io` host was blocked by network policy, so live visual/browser metrics are not claimed; those metrics above are from the local public archive.

## Non-blocking follow-ups / scope boundary

1. In a separately logged integration scope, revise the dashboard/source-page count wording to distinguish **91 government/court/SEC sources** from **two project records**, and explicitly describe project-only rows as project records.
2. In a separately logged site-quality scope, consider adding `scope="col"` to the three landing-page headers.
3. In a separately logged suggestions-content scope, update SUG-G5 to reflect the print and narrow-screen CSS that already exists.

These are candidates, not changes made by D8-01. D8 was limited to `COORDINATION.md` claim/audit records and this audit directory; no shared generator, data, HTML, CSS, legal finding, or deployed site content was edited.
