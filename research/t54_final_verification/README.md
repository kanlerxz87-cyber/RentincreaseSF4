# Independent 2026-11-13 verification and integration record

Session: `arena/1e813501-rentincreasesf4`. Base commit: `f810ee58e77a52f7ca51f03764d26a45dc36fa6d`.
Claimed 2026-11-13 UTC. This directory is the independent verification record for this session; it is
kept alongside (not instead of) `research/s23_2026-11-13/` and `research/t54_law_layer/`, which are
the other 2026-11-13 records already on `main`.

## Independent official-source verification (direct `fetch_page`, 2026-11-13 UTC)

| Source | URL | Confirmed on 2026-11-13 |
| --- | --- | --- |
| S01 | https://www.sf.gov/learn-about-rent-increases-san-francisco | 1.6% effective 3/1/26-2/28/27; license required before annual/banked increases; effective 7/1/2022 or 3/1/2023 for condominiums and 1-9 unit buildings; 30/90-day notice, +5 mailed; File 261020 notice present, not enacted. |
| S02 | https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit | 1.6% / 1.4% / 1.7% schedules; 4.2% deposit interest 3/1/26-2/28/27; same File 261020 notice. |
| S07 | https://www.sf.gov/rent-board-housing-inventory | All owners report; license auto-generated for tenant-occupied/non-owner-occupied units; March 1 deadline; no monetary late penalty; notice not enforceable without a license on the effective date; inventory information public; fee exemption does not satisfy reporting. |
| S27 | https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482 | SF state-only cap 8.8% 8/1/26-7/31/27; does NOT apply to units under SF Rent Ordinance limits; statewide law effective 1/1/2020, expires 1/1/2030; two-unit owner-occupied exemption. |
| S53 | https://www.sf.gov/information--sec-3715-reporting-obligations-licensing | Full Sec. 37.15 text; added by Ord. 265-20, effective January 18, 2021; buildings with 10+ units report by 7/1/2022, condos and <10-unit buildings from 3/1/2023; subsection (e) license/suspension and no tenant obligation during suspension. |
| S56 | https://www.sf.gov/rent-board-fee | $59.00 per dwelling unit, $29.50 per guest unit, 2026-2027; 5% monthly late penalty to 15% max; exemption deadline December 14, 2026; 50% recovery ($29.50) from tenants in occupancy on November 1. Referral-timing wording still differs inside the page (F38). |
| S57 | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV | Civil Code 1942.5(a) 180-day retaliation window; (b) once per 12 months; (c)/(d) immigration-reporting and organizing provisions; (f) waiver void. |
| S71 | https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770 | File 261020 Version 1, Pending Committee Action, introduced 9/15/2026, Land Use and Transportation Committee; enactment date and number blank; six attachments. NOT ENACTED. |
| S83 | https://www.huduser.gov/datasets/fmr/fmr2027/zip-calc?year=2027&zip=94122&cbsasub=METRO41860MM7360 | FY2027 SAFMR 94122: $2,370 / $2,770 / $3,410 / $4,460 / $5,020 (efficiency/1/2/3/4 BR); voucher benchmark, not a cap (F52). |

Every figure held from the inherited ledger. No value was inferred or filled from a nonofficial snippet.

## Integration outcome

While this session was working, `origin/main` advanced to `038f2e6` (PR #55, session
`arena/23a50992`). That session had already delivered a more complete version of the two gaps this
session targeted - an explicit state-vs-local law section (including the SB 567 (2023) analysis), the
Suggestions review queue (`pages/suggestions.html`), the Decision Readiness register
(`pages/decision.html`), lawyer-review criteria LR-01–LR-11, flags F53–F58 and sources S88–S92, and
the 2026-11-13 ledger date.

To avoid duplicating or discarding that work, this session merged `origin/main` into its branch and
resolved every conflict by taking `main`'s side for the conflicted generators and generated outputs,
preserving only this independent verification record. The final tree therefore contains `main`'s
Suggestions and Decision Readiness pages, not a second suggestions page.

## Gates on the integrated tree

- `python scripts/build_site.py` -> 24 data files, 22 page HTML files, index.html, assets/site.css, .nojekyll, 3 markdown deliverables.
- `python scripts/validate_site.py` -> **145 checks, 0 errors** (92 sources, 76 flags).
- `research/b87_notice_kit/validate_kit.py` -> 19 checks, 0 errors.
- `research/c72_2026-11-11_audit/validate_c72.py` -> 19 checks, 0 errors.
- Re-running the build leaves `git diff` clean.

## Irregularities (unchanged, published for review)

- F38: the official fee page states referral timing differently inside one page.
- F44 / F51 / F56: raw tenant identifiers, recoverable short-identifier hashes and the public-repo
  history exposure remain in this public repository's git history; only the owner can remediate. No
  git-history rewrite was attempted.
- F47 / F46: File 261020 is not enacted and its wording is internally inconsistent; re-check before
  any banked notice.
- No new irregularity was found in this session.
