# Current source and repository audit — 2026-11-08 UTC

Session `arena-12d86074`, fixed branch `arena/12d86074-rentincreasesf4`. This audit preserves the inherited T08/D16 research, re-checks load-bearing official sources, and records the corrections applied before final integration. Structural validation is not legal verification; owner intake is not government-verified.

## Integration and stale-claim handling

- Only open PR at start: #14, T08 head `07eb1b42f4c6e132a56713620b5ff85dabb3c911`, last commit 2026-11-07T20:20:05Z, conflicting. The >60-minute/no-commit handoff rule was logged in `COORDINATION.md`.
- Shallow history initially prevented a merge. `git fetch --deepen=100 origin main` and `pull/14/head` found merge-base `cd51aee`; T08 was merged with only `COORDINATION.md` conflicting. Both records were preserved and marker lines removed.
- A plain `git pull --rebase` attempted to flatten the merge; it was aborted and repeated with `--rebase=merges`. Future integration pushes use merge-preserving rebase. No force-push or history rewrite was performed.
- T08 additions S56–S61, F31–F35, fee/retaliation/coverage rows and narrative renderer were retained. D16 fee research in `research/rent_board_fee/README.md` was reused rather than duplicated.

## Fresh official-source checks used for corrections

| Topic | Official source | Result / correction |
| --- | --- | --- |
| Current annual rate | https://media.api.sf.gov/documents/571_Allowable_Annual_Increases_26-27_1.pdf ; https://www.sf.gov/news--annual-rent-increase-3126-22827-announced | 1.6% for 3/1/26–2/28/27 confirmed; historical series confirmed. No petition for ordinary annual increase. |
| License / inventory | https://www.sf.gov/rent-board-housing-inventory ; https://www.sf.gov/information--sec-3715-reporting-obligations-licensing ; https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory | Individual/small-building owners are not exempt. Official condition is a current license before the effective date; no express separate pre-mailing Board filing for ordinary annual/banked increases was found. Safest sequence: report, verify license, check tenancy, serve notice. |
| Petitions / passthroughs | https://www.sf.gov/landlord-petitions-and-passthroughs ; capital, O&M, comparable, utility and tenant-occupancy pages | Petition-based increases require filing before notice; utility worksheets before notice; bond/water passthroughs use specific worksheet rules. Do not describe every passthrough as petition-based. |
| Roommates / 6.14 / Costa-Hawkins | https://www.sf.gov/roommates-and-subletting ; https://www.sf.gov/information--charging-additional-occupants-prohibited ; https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins | No extra rent merely for an added occupant. 6.14 and Costa-Hawkins have different conditions; continuing occupant facts do not establish a reset. |
| Banking | https://www.sf.gov/information--banked-rent-increases ; https://www.sf.gov/information--annual-rent-increase-multiple-years | SF.gov says 24 full months but examples describe 12-month skipped opportunities. Conflict retained as F03; no case banked total asserted. Earlier conditional Unit 2 banked illustration withdrawn. |
| Fixed-term leases | https://www4.courts.ca.gov/documents/California-Tenants-Guide.pdf | Printed p.22: rent generally cannot be raised during a fixed term unless the agreement expressly allows it. Lease type/clause unverified; F36 added. |
| Notice | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827&lawCode=CIV | 30/90-day rule and mailing +5 days confirmed. No proposed effective date supplied; notice-deadline cells blank (F37). |
| Retaliation | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV | 180-day provisions are conditional; broader lawful-rights/organizing protection; good-faith cause and other exceptions. Attorney-fee remedy is nuanced. Overbroad wording removed. |
| Fee / registration | https://www.sf.gov/sites/default/files/2022-09/901%20Rent%20Board%20Fee%20Ch.%2037A.pdf ; https://www.sf.gov/notice-of-rent-board-fee-and-housing-inventory-requirement ; https://sftreasurer.org/information-lessors-residential-real-estate ; https://sftreasurer.org/business/register-business | $59.00/unit fee separate from license; 50% recovery rules; fee exemption ≠ inventory. One residential structure under four units generally does not by itself require business registration; other business/payroll may. Case facts unverified (F42). |
| Security deposits | https://www.sf.gov/reports--security-deposits | 4.2% interest for 3/1/26–2/28/27; relevant to statutory fee-recovery method. |
| State cap / exemption | https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482 ; https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV | 8.8% state-only SF cap 8/1/26–7/31/27; not a substitute for SF rent-control cap. Two-unit owner-occupied/ADU/separate-parcel conditions remain fact-specific. |
| Federal discrimination | https://www.govinfo.gov/link/uscode/42/3604 ; https://www.ecfr.gov/current/title-24/subtitle-B/chapter-I/part-100/subpart-G/section-100.500 ; https://www.hud.gov/helping-americans/fair-housing-act-overview | eCFR current as of 11/05/2026 still states discriminatory-effect framework. HUD overview describes enforcement prioritization toward provable intentional discrimination. Tension flagged F39; policy page not treated as repealing the regulation. |
| Market context | https://www.huduser.gov/portal/datasets/fmr/fmr2027/FY2027_FMR_Schedule.pdf ; https://www.huduser.gov/portal/datasets/fmr/smallarea/index.html | FY2027 SF HMFA FMRs confirmed. SAFMR PDF parse stopped before California; xlsx failed. 94122 row remains blank (F13). FMR/SAFMR are voucher standards, not private rent caps. |
| Corporate / individual evidence | https://www.sec.gov/Archives/edgar/data/1466085/000143774926003792/ex_895776.htm ; https://www.sec.gov/Archives/edgar/data/1687229/000168722926000016/invh-20251231.htm ; https://www.sf.gov/file/workload-stats-june-2024pdf | IRT/INVH figures confirmed as portfolio-level, not SF-specific. June 2024 capital improvements 18/148; subtotal 19/149 includes one Costa-Hawkins; total landlord 23/154. No all-owner generalization. |
| Project platform | https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site ; https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository ; https://docs.github.com/en/pull-requests/reference/pull-requests ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches | Pages root/branch publishing, public-site warning, history-rewrite limits, PR/checks and branch protection documented. Requirements rows now cite project sources instead of unrelated HUD FMR sources. |

## Repository defects found and corrected

1. **Stale counts and badges.** Source header, dashboard cards, requirements and flagged markdown used hardcoded 52/55/38/40/30 counts. Counts are now derived from the canonical registry: 72 entries, 76 distinct URLs, 59 flags. Status badges distinguish `rule checked`, `project checked`, `owner supplied`, `analysis`, `needs review`, and `source listed`.
2. **Irrelevant citations.** Requirements rows cited HUD FMR sources for GitHub Pages/PR/flag-count tasks. They now cite GitHub Docs or the relevant legal rule; a validator check rejects market-source citations on requirements rows.
3. **Owner rows lacked official links.** Owner-supplied case rows now link governing rules and explicitly say the links are not proof of intake. Missing case facts remain blank and flagged.
4. **Overbroad legal wording.** License wording now separates effective-date condition from mailing notice; retaliation wording is conditional; banking conflict is visible; fixed-term lease authority is flagged; petition/worksheet wording no longer treats every passthrough as petition-based.
5. **Unsupported superlatives and invented case values.** Defect-frequency rankings removed. Withdrawn Unit 2 banked total and arbitrary notice/effective-date examples are blank. Fee arithmetic is labeled illustrative and separate from rent.
6. **Privacy.** Current tree uses placeholders and omits the address. Low-entropy SHA-256 fingerprints were moved out of the public validator into gitignored `internal/`; public scripts no longer contain them. Historical public Git/PR exposure is prominently disclosed as **not remediated** (F44). No raw identifier is reproduced.
7. **Conflict markers and merge preservation.** Inherited and merge marker lines were removed while preserving both records. Validator scans public files and scripts for markers. Merge-preserving rebase is required for future pushes.
8. **Static self-deploy limitation.** A page built before merge cannot truthfully certify its own final merge/deploy. Requirements link to the live site and coordination log; final evidence is appended after merge (F49).
9. **Navigation/readability.** Grouped navigation, descriptive source links, search, responsive tables, privacy strip and a clearer executive summary were added. Source aliases are retained for continuity but excluded from distinct-URL counts (F48).

## Remaining nonblocking flags

All 59 flags are published on `pages/flagged.html` and `FLAGGED_FOR_REVIEW.md`. The most consequential open items are: exact address/coverage/license unverified; lease type and effective date unknown; banking history unknown and SF.gov examples conflict; 94122 SAFMR row not obtained; no federal general private-rent cap; no attorney approval or both-units rule; HUD policy/eCFR tension; historical privacy exposure not remediated; fee/registration case facts unverified (F43); final merge/deploy recorded after merge (F49).

## Verification performed in this pass

- `python3 scripts/build_site.py`
- `python3 scripts/validate_site.py` — 111 structural/privacy/source-integrity/internal-link checks, 0 errors at the time of this audit.
- Generated outputs committed for legacy main/root Pages; CI rebuild/diff check remains the publication gate.
- No attorney review, no property-record lookup, no raw identifier publication, no history rewrite, and no claim that flagged items are verified.


## Current-main integration addendum

While I12 was in progress, `main` advanced through PRs #22–#24 (D16 fee page, B87 notice worksheet/service record kit, N08 QA records). The integration preserves those additions: the dedicated `fee` page and main flags F31–F44 remain; B87/N08 research files are retained. Current-session source additions were renumbered to S71–S77 and new flags to F45–F49 to avoid collisions with main's S62–S70 and F36–F44. Privacy history is main F44; case fee/registration facts are main F43. The in-law-unit wording follows main's corrected legal/illegal distinction (main F36). Final generated counts: 19 pages, 400 rows, 40 needs-review rows, 77 source entries / 76 distinct URLs, 59 flags, 111 structural checks, 0 errors.
