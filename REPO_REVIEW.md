# Repository review — line by line

Reviewed: 2026-11-06 UTC by session `arena-73f5f1a2` on branch `arena/73f5f1a2-rentincreasesf4`.
Base commit: `4a404e7a5e6c4d996f17b581bfd2c54a717f7448` ("Initial commit").

## Initial tree

| Line / file | Observed content | Verification | Flag |
| --- | --- | --- | --- |
| `README.md` line 1 | `# RentincreaseSF4` | `cat README.md`; `git show 4a404e7:README.md` | No project description, requirements, data, or source links. |
| Repository root | Only `.git/` and `README.md` | `find . -path ./.git -prune -o -type f -print` | No site, data, tests, scripts, or coordination file at start. |
| Git history | One commit: `4a404e7 Initial commit` | `git log --oneline -8` | No prior work to preserve or merge. |
| Remote branches at start | `main` only, at `4a404e7` | `git ls-remote --heads origin` | Session branch had to be created on first push. |
| GitHub Pages | `status: built`, `build_type: legacy`, `source.branch: main`, `source.path: /`, `https_enforced: true`, URL `https://kanlerxz87-cyber.github.io/RentincreaseSF4/` | `gh api repos/kanlerxz87-cyber/RentincreaseSF4/pages` | Pages already serves the repository **root** of `main`; the site must be built at root, not `/docs`. |
| Repository permissions | `viewerPermission: ADMIN`, default branch `main` | `gh repo view --json nameWithOwner,defaultBranchRef,viewerPermission` | PR creation and merge are available. |

## Irregularities / review items

1. **No `COORDINATION.md` existed.** Created and claimed in T01 before other repo work; first claim commit pushed immediately as `4008ae6`.
2. **Platform branch constraint.** Arena fixes this session to `arena/73f5f1a2-rentincreasesf4`; the requested `session-<id>/<task>` branches cannot be created. Exclusive file scopes are used instead and recorded in `COORDINATION.md`.
3. **GitHub Pages source is root `/`.** A `.nojekyll` file and root-level `index.html` / `pages/` are required; a `docs/` folder would not be published without changing the Pages source.
4. **All case facts are user-provided and unverified.** No building year, address, tenancy dates, rent amounts, tenant names, or rent-control coverage were present in the repository. They are treated as inputs only, anonymized, and flagged on the site's **Flagged for Review** page.
5. **Privacy boundary.** Raw tenant identifiers are stored only in the untracked, gitignored `internal/` directory and are excluded from git and from the published site.

## Manual review links

- Repository: https://github.com/kanlerxz87-cyber/RentincreaseSF4
- Session branch: https://github.com/kanlerxz87-cyber/RentincreaseSF4/tree/arena/73f5f1a2-rentincreasesf4
- GitHub Pages settings (API): https://api.github.com/repos/kanlerxz87-cyber/RentincreaseSF4/pages
- Live site (after deploy): https://kanlerxz87-cyber.github.io/RentincreaseSF4/

Official legal sources used for the substantive findings are catalogued in `SOURCES.md` and `VERIFICATION.md` (T02) and on the site's **Sources** page.

## Re-review 2026-11-07 (session `arena-5cbd3f13`)

The repository had moved from `a0591c3` to `cd42189` through PRs #2–#9 by other sessions. This branch was rebased onto the current `main` and only the deltas below were re-applied, so no other session's work was overwritten.

| Line / file | Finding | Verification | Action |
| --- | --- | --- | --- |
| `scripts/site_pages.py` — case page | Every case value was blank. That satisfies the "blank if unverified" rule but leaves the site without the entries the user asked to see. | Read the built `pages/case.html` and `data/case.json`. | Case facts are now published as clearly labelled `owner-supplied` rows (anonymized, dates and amounts unchanged), beside a separate verification table that stays blank and flagged. |
| `scripts/site_pages.py` — `IND-03` | "19 petitions / 148 units" for capital improvements did not match the source. | Re-fetched S29: the PDF shows capital improvements 18 petitions / 148 units and a subtotal of 19 / 149 that includes one Costa-Hawkins petition. | Corrected to 18 / 148 with a note; recorded as F29. |
| `scripts/validate_site.py` | Source and flag totals were hardcoded (`== 55`, `== 38`), so adding a source or flag would silently break the check or hide a stale dashboard. | Code read. | Counts now come from `len(D.SOURCES)` and `len(D.FLAGS)`. |
| `scripts/validate_site.py` | No duplicate row-ID check; two pages could reuse an ID and links would still resolve to the wrong row. | Ran a counter over all rows during development (two `RATE-09`-style duplicates were found and renamed to `HIST-*` before this pass). | `row IDs are unique across all pages` check added. |
| `scripts/validate_site.py` | No check that owner-supplied rows are labelled and carry no official source; no raw-initial scan of the public case files. | Code read. | Both checks added; `data/case.json` and `pages/case.html` are scanned for initial patterns. |
| `scripts/build_site.py` | The index carried a placeholder hero heading ("Clean landing page / dashboard") and the validator tested for that placeholder. | Rendered `index.html`. | Placeholder replaced with a badge legend and a "start here" pointer; the validator now tests for the direct answer and the legend instead. |
| `scripts/site_flags.py` — `CARDS` | Dashboard totals were typed in by hand. | Code read. | Cards resolve `auto:sources` / `auto:flags` at build time. |
| `.github/workflows/validate.yml` | CI rebuilds and fails if generated outputs are not committed. | `git diff --exit-code` after a rebuild returns clean. | Rebuild outputs are committed with each change. |
| `pages/*.html`, `data/*.json` | Generated files changed by other sessions between this branch's base and `main`. | `git diff --stat a0591c3 origin/main`. | Not merged blindly; branch rebased onto `main` first. |

## Re-review 2026-11-08 (session `arena-abb34cd1`)

`main` had advanced to `d63dee4` (merge of PR #13, the D16 research). This session reviewed the merged tree line by line before changing anything.

| Line / file | Finding | Verification | Action |
| --- | --- | --- | --- |
| `COORDINATION.md` lines 223-256 | Three unresolved Git conflict markers were committed and published (`HEAD` side and `origin/main` side both present) | `grep -n '<<<<<<<\|=======\|>>>>>>>' COORDINATION.md` on `d63dee4` | Both sides kept verbatim, markers removed; validator now fails on any marker in a published file (F37) |
| `scripts/build_site.py` line 122 | Sources page header hardcoded "All 52 official sources" while 55 existed | Code read + rendered page | Now `len(D.SOURCES)`; same for the quick-navigation row |
| `scripts/site_pages.py` `REQ-08`, `AN-15` | Hardcoded "38 flags" while 40 existed | Code read | Now `len(FLAGS)` from the flag registry |
| `scripts/site_pages.py` `REQ-01/02/04/06/08/13/14/19/20`, `AN-15` | Cited `S43` (HUD Fair Market Rents) for website/PR/flag-count requirements — a fabricated citation | Code read against the S43 entry | Converted to `project record` rows with repository-artifact links (F38) |
| `scripts/validate_site.py` | Row validation required official `source_ids` for every non-owner row, which is what pushed earlier sessions to invent one; flags had the same restriction | Code read | Validation now accepts a repository artifact for project rows and for flags, and rejects a project row that carries official source IDs |
| `scripts/validate_site.py` `OFFICIAL_DOMAINS` | `sftreasurer.org` (official City Treasurer & Tax Collector site) was not allowed | Code read + both pages fetched 2026-11-08 | Added; the two lessor/registration pages became S61/S62 |
| `pages/sources.html`, `index.html`, `pages/flagged.html` | Generated counts could drift from the data | Rendered output compared with `data/sources.json` / `data/flags.json` | New validator checks compare the rendered counts with the registries |
| `research/rent_board_fee/README.md`, `research/privacy/HISTORY_EXPOSURE.md` | Merged on `main` but not surfaced anywhere on the site | File read | Integrated as `pages/fee.html` + flags F31-F36 |

## Re-review 2026-11-08 (session `arena-44eac0b7`, T44-A / T44-B)

After PRs #15, #16, #17, #20, #21, and #22 merged onto `main` (`8d51455`), this session reviewed the merged repository line by line and integrated the tested `N08` handoff patch (`research/n08_qa/proposed_integration.patch`) plus remaining source-citation and date repairs:

| Line / file | Finding | Verification | Action |
| --- | --- | --- | --- |
| `scripts/site_flags.py` — `F19`, `F20`, `F31` | `F19` (GitHub Pages deployment record) still cited `S43` (HUD Fair Market Rents); `F20` (platform branch constraint) and `F31` (committed conflict markers in `COORDINATION.md`) still cited `S20` (SF Rent Ordinance). | Code read against `scripts/site_sources.py` and `research/n08_qa/BROWSER_QA.md`. | Repaired `F19` to cite `S68, S69` (repository and Pages build API project records) and `F20`/`F31` to cite `S68`. |
| `scripts/site_sources.py` — `DATE` | `DATE` remained `"2026-11-07"` in page headers and `data/validation_report.json` despite 2026-11-08 narrative and source re-verifications. | Code read + rendered HTML header check. | Updated `DATE` to `"2026-11-08"` and rebuilt all site and JSON outputs. |
| `scripts/site_pages.py` (`LIC-05`, `ST-13`, `ST-15`), `scripts/site_text.py`, `scripts/build_site.py` | `N08` (`arena-7152099a`) handed off `research/n08_qa/proposed_integration.patch` to refine `Cal. Civ. Code § 1942.5` trigger/remedy precision (`ST-13`, `ST-15`), distinguish the effective-date license requirement from the recommended conservative sequence (`LIC-05`), and eliminate 84 automated Axe accessibility node findings. | Verified against direct 2026-11-08 `fetch_page` reads of `S01`, `S07`, `S53`, `S57` (`research/t44_audit/README.md`) and `research/n08_qa/PATCH_PROOF.md`. | Applied `proposed_integration.patch`, rebuilt all HTML/JSON/Markdown outputs, and verified 0 errors. |
| `scripts/site_flags.py` — `F45` | On `S02` (`https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit`), the hyperlink labeled `575 Cap. Imp. Labor Rates` points to `574_Cap._Imp._Imputed_Interest_26-27_7.26.pdf` (Form 574 Imputed Interest instead of Form 575). | Direct `fetch_page` of `S02` on 2026-11-08 (`T44-V02` in `research/t44_audit/README.md`). | Added Flag `F45` to `scripts/site_flags.py`, `FLAGGED_FOR_REVIEW.md`, `EXECUTIVE_SUMMARY.md`, `research/flags.md`, and `pages/flagged.html`. |
| `research/flags.md` | The `T09 additions` table from `arena-abb34cd1` listed pre-reconciliation local flag IDs `F31`–`F38`. | Compared `research/flags.md` against `scripts/site_flags.py`. | Kept `arena-abb34cd1`'s table intact and appended a canonical `F19`/`F20`/`F31`–`F45` reconciliation table. |


## Re-review 2026-11-13 (session `arena-23a50992`, S23)

Base: `main` at `f810ee5` (PR #50). Scope: line-by-line review of the current tree, git history, open PRs and the published site build. Official-source checks are in `research/s23_2026-11-13/README.md`.

| Line / file | Observed content | Verification | Flag |
| --- | --- | --- | --- |
| `.git` (history) | The local clone was shallow (one commit). `git fetch --unshallow` restored 170 commits across all refs. | `git rev-parse --is-shallow-repository`; `git rev-list --all \| wc -l` | None (environment note only). |
| Git history | Raw identifier tokens appear in 12 distinct commits dated 2026-11-06 to 2026-11-11. The current tree has none. | `git log --all -G` per token, counts only | F44, F51, F56 (open; owner decision). |
| Current tree (`data/`, `pages/`, `index.html`, `*.md`) | No raw identifier token and no SHA-256 digest of an identifier. Placeholders Tenant A–F are used throughout. | Scan of tracked files with an allowlist; `validate_site.py` privacy checks pass. | None new. |
| `.gitignore` | `internal/` is ignored. This session stored the raw intake in `internal/intake_private.md` only. | `git check-ignore -v internal/intake_private.md` | None. |
| Open pull requests | #18, #19, #25, #47 and #48 are open and marked stale, conflicting generator states from earlier sessions. | `gh pr list --state open` | F58 (owner decision; not merged or closed here). |
| `COORDINATION.md` | About 147 KB. Task IDs T49 and T51 were each reused by more than one session; several `in progress` rows are older than 60 minutes. | `wc -c`; `grep` of task IDs | F57. |
| `research/` | 16 folders, several with their own validators. | `ls research` | F58. |
| `scripts/site_sources.py` `DATE` | Set to `2026-11-13` for this build. `validate_site.py` date check now accepts `2026-11-13` (the earlier check hard-coded the prior dates). | Build and validation | None. |
| `SOURCES.md` | Added row S92 (Ordinance 265-20, Legistar copy). S88–S91 were assigned by `main` (PR #51) and kept. Count is computed at build time. | `validate_site.py` source-ledger check | F54. |
| sf.gov Housing Inventory page (S07) | Links to an Assessor URL that redirects to the Planning Property Information Map. | Direct `fetch_page` 2026-11-13 | F55. |
| Legistar Ordinance 265-20 copy (S92) | Marked-up master report (strike-throughs and redlines), not clean codified text. | Direct `fetch_page` 2026-11-13 | F54. |
| Premise in the owner request | The license requirement is described as a "2023 law". Ordinance 265-20 is effective January 18, 2021; March 1, 2023 is the reporting start for buildings under 10 units. | SF.gov news (S90) | F53 (published on `main`). |
| `research/c72_2026-11-11_audit/validate_c72.py` | The page-count assertion was hard-coded to 21 HTML pages; the new Suggestions & Decisions page makes 22. Updated the expected count only (no check removed). | `python3 research/c72_2026-11-11_audit/validate_c72.py` → 19/0 | None (maintenance). |
