# N08 — independent browser, accessibility and privacy QA

Session `arena-7152099a` · **2026-11-08 UTC**. This complementary QA task does not own or edit the shared site/generator. The tested baseline was a read-only copy of `main` at `d63dee438d5dd569d3b06edbfdd712674a043c75`, built with the repository's existing scripts in an isolated scratch directory. No shared generated file was changed.

## Results at the inherited baseline

| Check | Result | Evidence / official project source | Review status |
| --- | --- | --- | --- |
| Build and existing validator | Passed: 85 checks, 0 errors; 19 JSON files before validation report, 18 category pages plus landing page | [Builder at baseline](https://github.com/kanlerxz87-cyber/RentincreaseSF4/blob/d63dee438d5dd569d3b06edbfdd712674a043c75/scripts/build_site.py); [validator at baseline](https://github.com/kanlerxz87-cyber/RentincreaseSF4/blob/d63dee438d5dd569d3b06edbfdd712674a043c75/scripts/validate_site.py) | passed; structural checks are not legal verification |
| Real-browser page loads | 19 HTML files × 2 viewports (1440×1000 and 390×844) = 38 loads; all HTTP 200 | [Baseline browser JSON](baseline-browser-report.json); [reusable test](browser_qa.mjs) | passed |
| Whole-document horizontal overflow | 0 of 38 viewport checks; tables scroll inside their wrappers | [Baseline browser JSON](baseline-browser-report.json) | passed |
| Internal HTTP links and fragments | 37 distinct targets checked; 0 broken targets/fragments | [Baseline browser JSON](baseline-browser-report.json) | passed; external legal content checked separately |
| Automated accessibility | 40 violating node instances: 38 `link-in-text-block` (one footer link per page/viewport) and 2 `scrollable-region-focusable` on the mobile case page | [Baseline browser JSON](baseline-browser-report.json); [Axe rule help: links](https://dequeuniversity.com/rules/axe/4.14/link-in-text-block); [Axe rule help: scrollable regions](https://dequeuniversity.com/rules/axe/4.14/scrollable-region-focusable) | needs review — not a build/link failure |
| Mobile table keyboard access | 27 table wrappers require horizontal scrolling at 390px; none has its own tabindex. Most contain links and therefore do not trigger Axe's rule, but the two case tables without links do. | [Baseline browser JSON](baseline-browser-report.json); [table renderer at baseline](https://github.com/kanlerxz87-cyber/RentincreaseSF4/blob/d63dee438d5dd569d3b06edbfdd712674a043c75/scripts/build_site.py) | needs review |
| Mobile navigation usability | Sticky navigation is about 254px tall on a 844px viewport (about 30% of the screen); 18 category links plus Home wrap into many rows | [Baseline browser JSON](baseline-browser-report.json); [navigation at baseline](https://github.com/kanlerxz87-cyber/RentincreaseSF4/blob/d63dee438d5dd569d3b06edbfdd712674a043c75/scripts/build_site.py) | needs review — usability, not an automated WCAG failure |
| Current-tree privacy regression | 0 matching candidates in 76 tracked/new QA files; the known historical report still produces 6 matches when read into memory. No identifier values printed or written. | [Privacy result](privacy-result.json); [count-only test](privacy_check.py); [existing history audit](https://github.com/kanlerxz87-cyber/RentincreaseSF4/blob/main/research/privacy/HISTORY_EXPOSURE.md) | current tree clean; historical exposure unresolved |

The browser JSON's `errors` field includes accessibility review findings; it is not a count of broken links. The test exits nonzero for failed HTTP loads, document overflow or broken internal links, and reports accessibility findings separately for review. Automated Axe checks are not a complete accessibility conformance audit.

## Requests to the active integration owner

These are requests, not edits to another session's files:

1. **Underline inline links by default**, especially footer links, rather than distinguishing them only by color. Keep the hover state. The relevant baseline rule is `a{text-decoration:none}` in [site_text.py](https://github.com/kanlerxz87-cyber/RentincreaseSF4/blob/d63dee438d5dd569d3b06edbfdd712674a043c75/scripts/site_text.py).
2. **Make each horizontally scrollable table wrapper keyboard focusable** (`tabindex="0"`, an appropriate region role and a useful accessible name), with a visible focus outline. This fixes the two case-table violations and makes all 27 mobile scrolling tables consistently operable. See [render_table in build_site.py](https://github.com/kanlerxz87-cyber/RentincreaseSF4/blob/d63dee438d5dd569d3b06edbfdd712674a043c75/scripts/build_site.py).
3. **Add `scope="col"` to table headers** and consider a compact/mobile disclosure navigation or a non-sticky mobile nav. These are usability/semantics improvements, not claims that the baseline failed an automated rule.
4. **Keep the historical privacy exposure prominent.** The current-tree scan passing does not mean the old public report was erased from git history, PR diffs, old branches, caches or downloads. Do not label the repository fully confidential until that is independently remediated and verified.
5. **Re-run this QA against the final integrated tree and the deployed Pages URL**, not only the inherited baseline. The script is read-only and can target either a local public-only server or the live site.

## Reproduce

From this directory, run `npm ci`, then run `node browser_qa.mjs --site /path/to/public-site --url http://127.0.0.1:8000 --out /path/to/results`. Serve only public files; never serve the repository's `.git` directory or private intake. The included Chromium package supplies its browser binary and the small bundled NSS/NSPR library set, so no system package installation is needed. Run `python privacy_check.py` from the repository root or this directory for the count-only privacy check.

No raw tenant identifiers are included in the test fixtures, browser report, screenshots, scripts or findings. Screenshots were used for visual review in scratch space and are not required deliverables.


## Follow-up on integrated main and tested proposal

After PR #15/#17 landed, the same read-only test was run on `main` at `fcc7d6b`: 20 HTML files, 40 viewport loads, 40 internal targets, 0 broken links, 0 document overflow, but 84 Axe node instances (82 color-only links and 2 mobile case-table scroll regions). See [main browser report](main-fcc7d6b-browser-report.json). The shared owner had not yet adopted the N08 requests at that snapshot.

A proposed patch was then tested only in an isolated copy: [PATCH_PROOF.md](PATCH_PROOF.md), [patch](proposed_integration.patch), [after-browser report](proposed-fixes-browser-report.json). It reduced automated Axe violations to **0** while retaining 108 passing repository checks, 40 HTTP-200 loads, 40 internal targets and 0 broken links. The patch also tightens the retaliation and license-timing wording. It has **not** been applied to shared files by N08; the active integration owner must apply/reconcile, rebuild, merge and verify deployment.

A direct browser request from this sandbox to github.io was blocked by the outbound-network policy (`ERR_CONNECTION_CLOSED`). Live deployment was instead confirmed through the GitHub Pages API and successful `fetch_page` reads of the deployed index and executive summary; browser measurements above are explicitly local snapshots, not live-browser measurements.
