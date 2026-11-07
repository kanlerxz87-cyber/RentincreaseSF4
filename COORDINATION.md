# COORDINATION.md — shared task board

Session ID: `arena-fce57ebb-rentincreasesf4`
Branch: `arena/fce57ebb-rentincreasesf4`
Last updated: 2026-11-07 UTC

## Status legend

- `unclaimed` — no session has claimed the task.
- `in progress` — claimed; only the owning session edits the listed file scope.
- `done` — sources, verification and irregularities recorded below.
- `needs review` — item is published on the site's **Flagged for Review** page; it does **not** block other work or the merge.

## Platform / branch note

Arena fixes this session to the single branch `arena/fce57ebb-rentincreasesf4` and does not permit creating, switching to, or pushing additional branches. The requested `session-<id>/<task>` branches are therefore replaced by **exclusive, non-overlapping file scopes on the one permitted branch**.

GitHub Pages is already enabled on this repository with legacy source `main` / `/` at `https://kanlerxz87-cyber.github.io/RentincreaseSF4/`. The published site is therefore built at the repository root, not in a `docs/` folder. `.nojekyll` has been added so static HTML is served as-is.

Push procedure: the first push created the remote branch; every subsequent push is preceded by `git pull --rebase origin arena/fce57ebb-rentincreasesf4`. Merge conflicts are logged in the \"Conflict / handoff log\" section below and resolved without discarding another session's work.

## Task board

| ID | Task | Status | Owner | File scope (exclusive) | Sources / verification performed | Irregularities / flags |
| --- | --- | --- | --- | --- | --- | --- |
| T01 | Coordination, repo review, privacy boundary | `done` | `arena-73f5f1a2` | `COORDINATION.md`, `.gitignore`, `REPO_REVIEW.md`, `internal/` (untracked/private only) | `git status`, `git log`, `git ls-remote`, `cat README.md`, `find`, `gh repo view`, `gh api .../pages`; line-by-line review recorded in `REPO_REVIEW.md`. | Branch constraint; Pages source is root `/`; no code/data/site at start; all case facts user-provided/unverified; raw identifiers confined to gitignored `internal/`. |
| T02 | Official-source research and line-by-line verification ledger | `done` | `arena-73f5f1a2` | `SOURCES.md`, `VERIFICATION.md`, `research/sources/`, `research/verification/` | 52 official sources catalogued with links; direct `fetch_page` including remaining code/PDF chunks; 68-row root ledger; 80-line exact-claim crosswalk; rate/cap/decontrol/FMR/SEC figures cross-checked. | 24 source-quality flags F01–F24; 19 blank/unverified fields; 94122 SAFMR row blank; unit facts blank; no official federal private-rent cap, attorney approval, or both-units requirement found. |
| T03 | Anonymized case facts, calculations, flags (research copies) | `done` | `arena-73f5f1a2` | `research/case_facts.md`, `research/calculations.md`, `research/flags.md` | Owner-supplied intake kept internal-only; official governing rules from T02 linked; Python `Decimal` arithmetic and raw-identifier privacy scan; dates/amounts and placeholder mapping verified. | 10 T03 flags plus F01–F24; all case-specific official-source cells blank; no banked total computed; no new tenancy, vacancy-decontrol eligibility, attorney approval, or no-lawsuit guarantee inferred. |
| T04 | Final integration: shared table data, site generation, index/navigation, build + broken-link validation | `done` | `arena-73f5f1a2` | `data/`, `scripts/`, `index.html`, `pages/`, `assets/`, `.nojekyll`, `EXECUTIVE_SUMMARY.md`, `FLAGGED_FOR_REVIEW.md`, `README.md` | Merged T02/T03 research into 18 shared JSON files; built root `index.html`, 17 subpages, `assets/site.css`, `.nojekyll` and 3 standalone markdown deliverables; `scripts/validate_site.py` re-verified 167 table rows, 39 needs-review rows, 34 flags, 52 official sources, privacy, dates/amounts/placeholders, no exact address, no forbidden certification language, no broken internal links. `data/validation_report.json`: 70 checks, 0 errors. | 34 flags published on `pages/flagged.html` with official source links; F19/F20 remain `needs review` until T05 records PR/merge/Pages result. Flagged items do not block the merge. |
| T05 | Pull request, merge, GitHub Pages deploy confirmation, record PR/merge result | `done` | `arena-73f5f1a2` | `COORDINATION.md` (final update only) | PR #1 merged 2026-11-06T14:11:04Z, merge commit `a0591c3`; GitHub Pages API: `status: built`, legacy source `main` / `/` (re-verified 2026-11-07 by session `arena-6f344b80` via `gh pr view 1` and `gh api .../pages`). | F19/F20 remain published as `needs review` process flags; they do not block. |
| T06 | Forefront Rent Board / Rent Increase License answer for individual owners (step-by-step), stale REQ-19/20 + F19 update, privacy-leak fix in validation report, re-verification 2026-11-07, PR + merge + Pages confirmation | `done` | `arena-6f344b80` (claimed 2026-11-07 UTC) | `COORDINATION.md`, `scripts/site_text.py`, `scripts/site_pages.py`, `scripts/site_flags.py`, `scripts/site_sources.py` (DATE only), `scripts/validate_site.py`, regenerated `data/`, `index.html`, `pages/`, `EXECUTIVE_SUMMARY.md`, `FLAGGED_FOR_REVIEW.md`, `README.md` (build outputs only) | Re-fetched SF.gov S01 + S07 on 2026-11-07 (see log below). | New flags F25–F26 (see below); flagged items do not block. |
| D16-A | Rent Board Fee (SF Admin Code Ch. 37A; sf.gov/rent-board-fee; Form 573) and its 50% tenant pass-through, separate from Housing Inventory/license: official-source verification of who pays, amount, due date, penalties, exemptions, recovery rules, and how it interacts with a rent-increase notice | `in progress` | `arena-d16cbfc8` (claimed 2026-11-07 UTC) | `research/rent_board_fee/` (new directory only) + this file | Pages to fetch: sf.gov/rent-board-fee, sf.gov/pay-your-rent-board-fee, Form 573 (25-26), Admin Code 37A text. Not covered by any other claim (grep of main and all session branches for `37A` / `Rent Board fee` returned nothing on 2026-11-07 20:10 UTC). | — |
| D16-P | Privacy audit of git history, PR diffs and published files for the raw tenant-identifier tokens (public repo) + owner remediation guidance; no raw token is ever written to the repo | `in progress` | `arena-d16cbfc8` (claimed 2026-11-07 UTC) | `research/privacy/` (new directory only) + this file | Scan of every commit reachable from every remote branch (shallow clone, depth 50) with in-shell patterns only. Finding so far: the 2026-11-06 `data/validation_report.json` (commit `0ede010` through `a0591c3`) printed the six raw tokens in one check detail; repo is public, 0 forks. F26 on the site does not yet say the exposure persists in git history/PR #1 diff. | History rewrite / force-push / GitHub Support purge cannot be done by agents (branch rules) -> owner action, to be published on Flagged for Review. |
| D16-B | Independent second-pair-of-eyes QA of the integrated site after the other open claims land (re-fetch official pages for the new rows; check F25 against Rent Ordinance §37.15; check REQ-row source integrity; link check) | `unclaimed until other claims are `done`` | `arena-d16cbfc8` (planned) | `research/qa/` (new directory only); fixes only through D16-C | — | — |
| D16-C | Final integration of D16 outputs into shared `data/`, `scripts/`, generated pages + PR to `main`, merge, Pages confirmation, record result | `unclaimed until D16-A/P/B are `done` and other sessions' claims are `done` or stale (>60 min)` | `arena-d16cbfc8` (planned) | `data/`, `scripts/`, `pages/`, `index.html`, `EXECUTIVE_SUMMARY.md`, `FLAGGED_FOR_REVIEW.md`, `SOURCES.md`, `VERIFICATION.md` — only after other owners finish; otherwise requests are logged here | — | — |

## Final integration session

T01–T03 were `done`; then T04 (this session, since no other sessions were detected) claimed final integration, merged the research into the shared `data/` files, re-verified every row line by line, confirmed the site builds with no broken internal links, and published. T05 now opens the PR to `main`, merges it, confirms the Pages deployment, and records the PR link and merge result here. Flagged and unverified items are published on the clearly labeled **Flagged for Review** page and do not block the merge.

> Conflict log (2026-11-07): merging `origin/main` (PR #3, session `arena-fce57ebb`, a T05 claim-only merge) into this branch conflicted in this file only. Resolved by keeping the completed T05 record above (PR #1 merged, Pages built — independently re-verified this session) and this session's T06 row; the other session's T05 claim is noted here so its work is not discarded: T05 was also claimed by `arena-fce57ebb` on 2026-11-07 and its claim was merged via PR #3. No other files conflicted.

## Conflict / handoff log

- 2026-11-06 UTC: no conflicts at start; remote contained only `main` at `4a404e7`. First push (`4008ae6`) created `arena/73f5f1a2-rentincreasesf4` on origin.
- 2026-11-06 UTC: T02 scope narrowed before writing research files so T03 case-fact files would not overlap. All T02 pushes completed after `git pull --rebase` with no conflicts. No other sessions, handoffs, or conflicting claims.
- 2026-11-06 UTC: T03 claim, files and done status pushed after `git pull --rebase` with no conflicts. Privacy scan found no raw identifiers in T03 research files.
- 2026-11-06 UTC: T04 claim, data/site/scripts/docs and validation fixes pushed after `git pull --rebase` with no conflicts. Validation initially found 3 issues (HTML-escaped source URL check, false-positive certification wording, reversed Home link); all were fixed and revalidated: 70 checks, 0 errors.
- 2026-11-07 UTC: T05 claim (current session `arena-fce57ebb-rentincreasesf4`) — pull request, merge, GitHub Pages deploy confirmation, and record PR/merge result in this file.

## Requests to other sessions

- None. No files outside this session's claimed scopes will be edited. `COORDINATION.md` is the shared task board: each task owner may make status/log edits to it, while substantive files remain in the listed exclusive scopes.

- **T06 — in progress (2026-11-07, session `arena-6f344b80`).** Forefront answer added to `EXECUTIVE_SUMMARY.md` and `pages/summary.html` (new LIC-01–LIC-09 table): an individual owner must still report into the Rent Board Housing Inventory and have a current Rent Increase License on file before an annual/banked increase takes effect; no individual exception; 1–9-unit buildings covered since 2023-03-01. Sources re-fetched 2026-11-07: S01 SF.gov "Learn about rent increases" ("A landlord must get a rent increase license before imposing annual allowable and/or banked rent increases"; 1.6% 3/1/26–2/28/27 re-confirmed) and S07 SF.gov "Rent Board Housing Inventory" ("All owners of residential property are required to report"; license auto-generated for non-owner-occupied units; notice "not enforceable" without a license on the effective date; Mar 1 deadline; no monetary penalty for late filing). Other rows carried from T02 verification (not re-fetched this session). Irregularities found this session: **F25** SF.gov consequence wording differs ("may be null/void" vs "not enforceable"); **F26 PRIVACY** — `data/validation_report.json` (2026-11-06) published the raw tenant identifier tokens in a check detail; fixed in `scripts/validate_site.py` (count only, values withheld), report regenerated, independent scan of all public files found no identifier tokens. Also updated: stale REQ-19/REQ-20 (PR #1 merged 2026-11-06, merge commit `a0591c3`, verified `gh pr view 1`; Pages API `status: built`, re-checked 2026-11-07). Validation after rebuild: **71 checks, 0 errors; 176 rows; 36 flags** (`data/validation_report.json`). Local preview served HTTP 200 for index/summary/flagged.

## Sources / verification / irregularities by task

- **T01 — done.** Sources: local git/gh inspection and GitHub Pages API response (2026-11-06 UTC). Verification: initial tree contained `README.md` only (line 1: `# RentincreaseSF4`); one commit; remote `main` only; Pages `status: built`, `build_type: legacy`, `source.branch: main`, `source.path: /`; repository `viewerPermission: ADMIN`. Irregularities: platform branch constraint; Pages root source; no project data; all case facts unverified; privacy boundary created with `.gitignore` and untracked `internal/tenant-identifiers.local.md`. Full detail: `REPO_REVIEW.md`.
- **T02 — done.** Sources: 52 official sources in `SOURCES.md` (SF.gov, SF Rent Board PDFs, SF Planning, CA Legislative Information, CA CRD, HUD USER, eCFR, GovInfo, SEC EDGAR, MOHCD, GitHub Pages API). Official links appear in every row. Verification: direct `fetch_page` to each official page; long HTML/PDF/SEC files read in chunks; remaining §1947.12, §12955, §37.10B, GovInfo §3604, Rent Board minutes, AB 1482 and SF.gov \"Learn about rent increases\" chunks fetched; rate figures cross-checked across S01–S04; state cap across S27/S36; §6.14/Costa-Hawkins across S15/S16/S28/S37; FY2026/FY2027 FMR schedules cross-checked; SEC IRT/INVH figures read from official EDGAR text. Exact quotes and chunk numbers: `research/sources/official_sources.md`. Line-by-line claims: `VERIFICATION.md` and `research/verification/line_by_line.md`. Irregularities: 24 flags in `research/sources/irregularities.md` (F01–F24) and 19 blank/unverified fields in `research/sources/unverified.md`; all published on the **Flagged for Review** page. No value was inferred or substituted from a nonofficial snippet.
- **T03 — done.** Sources: owner-supplied intake stored only in untracked `internal/tenant-identifiers.local.md`; official governing rules and rates from T02 (`SOURCES.md`). Verification: `research/case_facts.md` preserves dates and dollar amounts while replacing all tenant identifiers with placeholders `Tenant A`–`Tenant F`; Python `Decimal` confirmed $3,995 × 1.6% = $63.92 → $4,058.92, $3,995 × 1.4% = $55.93 → $4,050.93, $3,150 × 1.6% = $50.40 → $3,200.40, $3,150 × 1.4% = $44.10 → $3,194.10; raw-identifier scan returned no hits; all required dates, amounts and placeholders verified present. Irregularities: 10 T03 flags in `research/flags.md` plus F01–F24; case-specific source cells blank; no banked total computed; no new tenancy, vacancy-decontrol eligibility, attorney approval, or no-lawsuit guarantee inferred.
- **T04 — done.** Sources: T02 official-source ledger and T03 anonymized research copies; `SOURCES.md`, `VERIFICATION.md`, `research/`. Verification: `scripts/build_site.py` generated 18 `data/*.json` files, root `index.html`, 17 `pages/*.html` files, `assets/site.css`, `.nojekyll`, `README.md`, `EXECUTIVE_SUMMARY.md` and `FLAGGED_FOR_REVIEW.md`. `scripts/validate_site.py` re-read every combined data row line by line: 167 rows with official source links, 39 `needs review` rows with blank values and published flag IDs, 34 flags with official links, 52 official sources, correct dates/amounts/placeholders, no raw tenant identifiers, no exact street address, no forbidden certification language, no broken internal links, and all required site files. Result: `data/validation_report.json` — 70 checks, 0 errors. Irregularities: 34 flags published on `pages/flagged.html` and `FLAGGED_FOR_REVIEW.md`; F19/F20 remain `needs review` until T05 records PR/merge/Pages results. No other conflicts or handoffs.
- **T05 — not started.**

## Parallel session 2026-11-07 — tenant-assistance research

Session `arena-05ec645c`, fixed branch `arena/05ec645c-rentincreasesf4`: the active `arena-2e273eee` session has claimed follow-up audit/integration, so this session will not edit its claimed site, data, scripts, or audit files. New independent task: official tenant legal-assistance resources and review safeguards, scoped exclusively to `TENANT_ASSISTANCE_RESEARCH.md` (plus coordination entries). Status: **in progress**. Integration request: please consider incorporating any actionable verified findings from this separately scoped research into the site if appropriate. Existing PR #1 has already merged and the Pages API reports its build succeeded. Branch naming is fixed by Arena, overriding the requested session branch scheme.

- **Independent tenant-assistance research — done (arena-05ec645c).** Deliverable: `TENANT_ASSISTANCE_RESEARCH.md`. Directly read official [MOHCD resources](https://www.sf.gov/tenant-and-landlord-resources), [Rent Board petition instructions](https://www.sf.gov/report-unlawful-rent-increase-or-request-review-your-rent-history), [license noncompliance](https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory), [Rent Board scope](https://www.sf.gov/departments--rent-board--about), and [eviction guidance](https://www.sf.gov/evictions-san-francisco). Each table row links to the official source supporting the claim. Flag: free eviction legal help is documented; universal free attorney representation for an ordinary rent-increase dispute is not established. No attorney has reviewed or approved the case; case-specific records remain unverified. Integration request to `arena-2e273eee`: incorporate the note's findings if appropriate, including the limited scope of the free legal-help claim, and preserve the work of this session. No other active session's claimed files were edited.
## Follow-up session 2026-11-07

Session `arena-2e273eee` on fixed branch `arena/2e273eee-rentincreasesf4` takes over stale T05 and claims follow-up audit/integration scope: coordination, audit report, site generator/data corrections if necessary, validation artifacts. Previous T01–T04 are completed; no live competing claim found. Prior PR #1 is already merged (merge a0591c3); Pages API reports built. The old T05 status above was stale. This session will validate the inherited deliverable, distinguish structural checks from fresh source verification, and record deployment evidence. No new branches will be created due to platform branch constraints.

| Task | Status | Owner | Scope |
| --- | --- | --- | --- |
| F01 follow-up audit and final publication | in progress | arena-2e273eee | COORDINATION.md, FOLLOWUP_AUDIT.md, scripts/, generated site/data as needed |

### Follow-up audit completion

- 2026-11-07: First branch-specific pull failed because the remote branch did not yet exist. Pulled/rebased origin main before initial push; no conflict and no work discarded.
- F01 audit/integration done: fresh fetches of S01 (both chunks), S02, S27 (first chunk) confirm operative local/state rates and core notice/roommate guidance. Other historical source checks are inherited, not claimed as fresh verification. Limits and the incorrect alternative AB1482 URL are documented in FOLLOWUP_AUDIT.md, linked on every page.
- Fixed clean-checkout privacy validation without publishing identifiers; removed blanket fresh-verification header wording; updated stale F19 deployment flag. Added GitHub Actions build/structural validation on pushes and PRs (scope extended to `.github/workflows/validate.yml`).
- Built and validated all 167 source-linked rows, 39 blank/flagged rows, 34 flags, 52 source links; 70 checks passed, zero errors, no broken internal links. These are structural checks, not legal certification. Remaining legal/private-record unknowns remain published for review.
- Follow-up publication in progress; prior PR #1 merge and successful Pages build confirmed using gh API. Current session uses only arena/2e273eee-rentincreasesf4 as required.

### Concurrent session record retained

- **T04 — done.** Sources: T02 official-source ledger and T03 anonymized research copies; `SOURCES.md`, `VERIFICATION.md`, `research/`. Verification: `scripts/build_site.py` generated 18 `data/*.json` files, root `index.html`, 17 subpages, `assets/site.css`, `.nojekyll`, `README.md`, `EXECUTIVE_SUMMARY.md` and `FLAGGED_FOR_REVIEW.md`. `scripts/validate_site.py` re-read every combined data row line by line: 167 rows with official source links, 39 `needs review` rows with blank values and published flag IDs, 34 flags with official links, 52 official sources, correct dates/amounts/placeholders, no raw tenant identifiers, no exact street address, no forbidden certification language, no broken internal links, and all required site files. Result: `data/validation_report.json` — 70 checks, 0 errors. Irregularities: 34 flags published on `pages/flagged.html` and `FLAGGED_FOR_REVIEW.md`; F19/F20 remain `needs review` until T05 records PR/merge/Pages result. No other conflicts or handoffs.
- **T05 — in progress.** Claimed by current session `arena-fce57ebb-rentincreasesf4` on 2026-11-07 UTC. Will open PR from `arena/fce57ebb-rentincreasesf4` to `main`, merge it, confirm GitHub Pages deployment, and record the PR link and merge result here.

## Requests to other sessions

- None.

## Sources / verification / irregularities by task

- **T01 — done.** (see above)
- **T02 — done.** (see above)
- **T03 — done.** (see above)
- **T04 — done.** (see above)
- **T05 — in progress.** (see above)

### Concurrent merge reconciliation

2026-11-07: PR #2 initially could not merge because concurrent session PR #3 changed COORDINATION.md on main. Stopped merge, fetched main, and preserved both session records while resolving the coordination-only conflict. The attempted rebase was aborted before using a normal merge so no published branch history was rewritten. Concurrent session T05 ownership is preserved; this session owns the follow-up audit F01, not its work. Request to other session: keep this F01 record and audit corrections intact.

> Conflict log (2026-11-07, session `arena-6f344b80`): merging `origin/main` after PR #2 (session `arena-2e273eee`, follow-up audit incl. fingerprint-based privacy validation, `FOLLOWUP_AUDIT.md`, `.github/workflows/validate.yml`) conflicted in generated files, `scripts/site_flags.py` and `scripts/validate_site.py` only. Resolution: took PR #2's versions of those scripts (keeping their fingerprint privacy checks, F19 text and card wording), then re-applied only this session's deltas (flag count 36, new flags F25–F26, forefront-summary validation check); regenerated all site/data files with `build_site.py`. Their audit findings and files were not discarded. Re-validation after reconciliation: 71 checks, 0 errors. PR for this session: #4.

## T06 final record (2026-11-07, session `arena-6f344b80`)

- PR: https://github.com/kanlerxz87-cyber/RentincreaseSF4/pull/4 — **MERGED** 2026-11-07T20:02:56Z, merge commit `48fdf99`.
- GitHub Pages: API `status: built`, latest build commit `48fdf99`, error none (legacy source `main` / `/`). Live site: https://kanlerxz87-cyber.github.io/RentincreaseSF4/ — Executive Summary page carries the FOREFRONT Rent Board / license section (LIC-01–LIC-09).
- Validation at merge: 71 checks, 0 errors; 176 rows; 36 flags on the Flagged for Review page (do not block). Conflicts with PR #3 and PR #2 were resolved without discarding those sessions' work (see conflict logs above).
- This record was landed on `main` by a follow-up docs-only PR from the same session branch; its number/merge is reported in the session's final message (a record cannot cite its own merge commit).
### Parallel research reconciliation

2026-11-07, arena-05ec645c: main advanced during independent research. Rebasing onto main conflicted in COORDINATION.md; aborted the rebase to preserve the already-pushed branch history, merged main and retained both sides of the coordination-only conflict. No other session’s work discarded.

### Tenant-assistance research publication

- PR [#6](https://github.com/kanlerxz87-cyber/RentincreaseSF4/pull/6) merged on 2026-11-07 UTC as `f792bf1b47e9bcc990e21aeb9fee0d7e0de69de6`. Its GitHub Actions validation completed successfully. Pages [build and deployment run](https://github.com/kanlerxz87-cyber/RentincreaseSF4/actions/runs/42409257423) succeeded, and the Pages API reported `built` for that commit. The research is available at `TENANT_ASSISTANCE_RESEARCH.md`; it supplements the existing site rather than changing another session's claimed site files.
- The current report was corrected after F26: identifiers previously appeared in a published validation report. Prior public Git history may still contain that report; the historical exposure is not remedied merely by removing it from the latest site. Do not claim complete confidentiality or rewrite repository history without appropriate authorization.

## Session `arena-d16cbfc8` (branch `arena/d16cbfc8-rentincreasesf4`) — claims and log, 2026-11-07 UTC

Read `COORDINATION.md`, `git ls-remote` and every `origin/arena/*` branch before claiming. Other live claims seen at claim time: `arena-c007d556` (integration: Rent Ordinance §37.15, S53–S55, process page — not yet merged), `arena-f8681e80` (T07 summary clarification; PR #5 closed unmerged), `arena-05ec645c` (tenant-assistance research; merged), `arena-6f344b80` (T06 forefront answer; merged), `arena-2e273eee` (follow-up audit; merged), `arena-fce57ebb` (T05; merged). Task IDs here carry a `D16-` prefix because `T06`/`T07` were each used by more than one session. This session does **not** edit any file in another session's claimed scope; it writes only new directories under `research/` until D16-C.

- **Why D16-A:** the Rent Board *fee* is a second, separate Rent Board obligation for every owner of a residential unit (not the same as the Housing Inventory report / Rent Increase License). It is not mentioned in any current page, row or branch and bears on the user's lead question ("what do I owe the Rent Board before a rent increase?"). Official pages found: https://www.sf.gov/rent-board-fee and the Form 573 fee history.
- **Why D16-P:** the user's top priority is privacy. A scan on 2026-11-07 shows the raw identifier tokens were published in `data/validation_report.json` from `0ede010` (2026-11-06) onward; they are removed from the current `main` tip but remain in public git history, PR #1's diff and any cached copy of the earlier Pages deployment. The existing flag F26 says the report was regenerated but not that history still contains the tokens.

