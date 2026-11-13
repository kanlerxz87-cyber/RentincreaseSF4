# T54 - Fresh 2026-11-13 verification + Suggestions section

Session: `arena/1e813501-rentincreasesf4` (claimed 2026-11-13 UTC).
Base commit: `f810ee58e77a52f7ca51f03764d26a45dc36fa6d` (main tip, PR #50 merged).
Exclusive file scope: `scripts/site_sources.py`, `scripts/site_pages.py`, `scripts/site_flags.py`,
`scripts/build_site.py`, `scripts/validate_site.py`, `scripts/site_text.py`, regenerated `data/`,
`pages/`, `index.html`, `assets/`, root generated summaries, `research/t54_final_verification/`,
`SOURCES.md`, `VERIFICATION.md`, `COORDINATION.md`.

No other session held a live claim. The inherited `in progress` rows in the board are stale
(2026-11-07/08/10/11) and their work is already on `main`.

## What this session changed

1. **Explicit state-vs-local-law answer.** Added summary row `LIC-11` and an executive-summary
   sentence answering the owner's question directly: the Rent Increase License and the Housing
   Inventory reporting duty are a **local San Francisco** obligation (SF Admin. Code Sec. 37.15,
   added by Ord. 265-20) that applies only to rent-controlled units. The statewide California
   Tenant Protection Act (AB 1482) is a separate state cap that requires no Rent Board license and
   does not apply where the SF Rent Ordinance already limits rent increases. The "March 1, 2023"
   date is the local date the reporting duty became operative for condominiums and buildings with
   1-9 units, not a state law.
2. **New "Suggestions & Decisions" section** (`pages/suggestions.html`, nav entry, dashboard card).
   Twelve review-only proposals: six site/decision-making improvements and six information-
   discovery steps that close specific flagged gaps before any decision. Each row is a proposal,
   not a finding, and carries a proposed review decision plus official source links.
3. **New "proposed" status** (badge, CSS, validator allowance) so unimplemented suggestions stay
   visually distinct from verified findings.
4. **Ledger date updated to 2026-11-13** and re-verification notes appended to the load-bearing
   source statements.

## Fresh official-source verification (direct `fetch_page`, 2026-11-13 UTC)

| Source | URL | Confirmed on 2026-11-13 |
| --- | --- | --- |
| S01 | https://www.sf.gov/learn-about-rent-increases-san-francisco | 1.6% effective 3/1/26-2/28/27; license required before annual/banked increases; effective 7/1/2022 or 3/1/2023 for condominiums and 1-9 unit buildings; 30/90-day notice, +5 mailed; File 261020 notice still present, not enacted. |
| S02 | https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit | 1.6% / 1.4% / 1.7% schedules; 4.2% deposit interest 3/1/26-2/28/27; same File 261020 notice. |
| S07 | https://www.sf.gov/rent-board-housing-inventory | All owners report; license auto-generated for tenant-occupied/non-owner-occupied units; March 1 deadline; no monetary late penalty; notice not enforceable without a license on the effective date; inventory information public; fee exemption does not satisfy reporting. |
| S27 | https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482 | SF state-only cap 8.8% 8/1/26-7/31/27; does NOT apply to units under SF Rent Ordinance limits; statewide law effective 1/1/2020, expires 1/1/2030; two-unit owner-occupied exemption. |
| S53 | https://www.sf.gov/information--sec-3715-reporting-obligations-licensing | Full Sec. 37.15 text; added by Ord. 265-20, effective January 18, 2021; buildings with 10+ units report by 7/1/2022, condos and <10-unit buildings from 3/1/2023; subsection (e) license/suspension and no tenant obligation during suspension. |
| S56 | https://www.sf.gov/rent-board-fee | $59.00 per dwelling unit, $29.50 per guest unit, 2026-2027; 5% monthly late penalty to 15% max; exemption deadline December 14, 2026; 50% recovery ($29.50) from tenants in occupancy on November 1. Referral-timing wording still differs inside the page (F38). |
| S57 | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV | Civil Code 1942.5(a) 180-day retaliation window; (b) once per 12 months; (c)/(d) immigration-reporting and organizing provisions; (f) waiver void. |
| S71 | https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770 | File 261020 Version 1, Pending Committee Action, introduced 9/15/2026, Land Use and Transportation Committee; enactment date and number blank; six attachments. NOT ENACTED. |
| S83 | https://www.huduser.gov/datasets/fmr/fmr2027/zip-calc?year=2027&zip=94122&cbsasub=METRO41860MM7360 | FY2027 SAFMR 94122: $2,370 / $2,770 / $3,410 / $4,460 / $5,020 (efficiency/1/2/3/4 BR); voucher benchmark, not a cap (F52). |

Every figure held from the inherited ledger. No value was inferred or filled from a nonofficial snippet.

## Gates at build time

- `python scripts/build_site.py` -> 23 data files, 21 page HTML files, index.html, assets/site.css, .nojekyll, 3 markdown deliverables.
- `python scripts/validate_site.py` -> **133 checks, 0 errors** (87 sources, 70 flags, 363 rows, 12 suggestion rows).
- `research/b87_notice_kit/validate_kit.py` -> 19 checks, 0 errors.
- Re-running the build leaves `git diff` clean (generated outputs are committed).

## Irregularities / flags (unchanged, published for review)

- F38: the official fee page states referral timing differently inside one page (summary says after June 1; timeline says a July notice allows 30 days before referral).
- F44 / F51: raw tenant identifiers and recoverable short-identifier hashes remain in this public repository's git history and pull-request diffs; only the owner can remediate. No git-history rewrite was attempted.
- F47 / F46: File 261020 is not enacted and its wording is internally inconsistent; re-check before any banked notice.
- No new irregularities were found in this session.
