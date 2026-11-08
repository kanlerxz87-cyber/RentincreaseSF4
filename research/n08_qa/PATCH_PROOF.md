# N08 — tested integration proposal (not applied to shared files)

Session `arena-7152099a` · 2026-11-08 UTC. The active integration owners hold the shared generator/site scope. To avoid a concurrent edit, this proposal was prepared and tested **only in an isolated scratch copy** of `main` at `fcc7d6b` (the generator files are unchanged in `a613996`). It is delivered as [proposed_integration.patch](proposed_integration.patch) for the owner to apply, rebuild and verify. N08 has not edited the shared files or claimed another session's merge.

## What the patch changes

- `scripts/build_site.py`: each table wrapper gets `tabindex="0"`, `role="region"` and an accessible name; column headers get `scope="col"`.
- `scripts/site_text.py`: inline links are underlined by default (navigation keeps its own styling), scroll regions get a visible focus outline, and mobile navigation is not sticky. The executive-summary retaliation paragraph states the statutory conditions and remedy limits.
- `scripts/site_pages.py`: ST-13/ST-15 state the tenantability/good-faith/rent-default/latest-event/once-per-12-month conditions, the lawful-cause provision, the fraud/oppression/malice condition for punitive damages, and the limited retaliatory-eviction fee provision. LIC-05 distinguishes the legal effective-date test from the recommended report/license-before-service workflow.

## Measured result

| Test | Before patch (main `fcc7d6b`) | After patch in isolated copy | Evidence |
| --- | --- | --- | --- |
| Existing repository validator | 108 checks, 0 errors | 108 checks, 0 errors | [Before validator log](main-fcc7d6b-validation.log); [after validator log](proposed-fixes-validation.log). [Builder](https://github.com/kanlerxz87-cyber/RentincreaseSF4/blob/fcc7d6b4a36357e2a8bb943f4389c920aee111f3/scripts/build_site.py) / [validator](https://github.com/kanlerxz87-cyber/RentincreaseSF4/blob/fcc7d6b4a36357e2a8bb943f4389c920aee111f3/scripts/validate_site.py) |
| HTML files / viewport checks | 20 / 40 | 20 / 40 | [Before browser JSON](main-fcc7d6b-browser-report.json); [after browser JSON](proposed-fixes-browser-report.json) |
| HTTP 200 / document overflow | 40 loads / 0 overflow | 40 loads / 0 overflow | Same browser JSON files |
| Internal link targets / broken | 40 / 0 | 40 / 0 | Same browser JSON files |
| Axe violating node instances | 84 (82 color-only link nodes; 2 mobile case-table scroll regions) | **0** | Same browser JSON files; [Axe link rule](https://dequeuniversity.com/rules/axe/4.14/link-in-text-block); [Axe scroll-region rule](https://dequeuniversity.com/rules/axe/4.14/scrollable-region-focusable) |
| Blocking browser errors | 0 | 0 | Same browser JSON files |
| Current-tree privacy fingerprint matches | 0 | 0 in the N08 tracked/new-file scan; historical fixture still detects 6 in memory | [Privacy result](privacy-result.json); [count-only test](privacy_check.py) |

Zero automated Axe violations is **not** a claim of complete accessibility conformance or legal approval. The legal wording is based on the official [Civil Code §1942.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV), [SF Housing Inventory](https://www.sf.gov/rent-board-housing-inventory), [SF noncompliance guidance](https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory) and [SF Admin Code §37.15](https://www.sf.gov/information--sec-3715-reporting-obligations-licensing), reopened directly on 2026-11-08.

## Integration instructions for the owning session

From the repository root, after reconciling any newer shared-file changes: `git apply --check research/n08_qa/proposed_integration.patch`, then `git apply research/n08_qa/proposed_integration.patch`, `python scripts/build_site.py`, `python scripts/validate_site.py`, and the read-only browser test in this directory. If the patch no longer applies cleanly, use the exact changes above rather than overwriting another session's work. Re-verify the final deployed Pages URL and record the actual result. Do not mark the N08 proposal adopted until it is present in the merged tree.
