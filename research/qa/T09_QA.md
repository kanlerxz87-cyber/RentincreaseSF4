# T09 — Independent second-pair-of-eyes QA after the D16 integration (session `arena-abb34cd1`, 2026-11-08)

## What happened (honest account of duplicate work)

This session claimed T09 at 2026-11-08 UTC after finding the D16-B/D16-C claims stale on `main` (`d63dee4`). It then independently built a Rent Board Fee integration of its own (sources S56–S62, flags F31–F38, a 26-row fee page, a `project record` row status, dynamic counts and a validator conflict-marker check).

**While that work was in review, a parallel session (`arena-18eafb4c`) landed the same integration on `main` through PR #15** — a fuller fee page (28 rows, including exemptions, deposit-interest and business-registration rows), sources S56–S69 and flags F31–F44, plus its own fixes for the same inherited defects (dynamic counts, the S43 mis-citation, the committed conflict markers).

**Resolution:** `origin/main` was merged into this branch and its implementation was kept as the single source of truth. This session's duplicate fee page, its S56–S62 numbering and its F31–F38 numbering were dropped rather than merged, so the site has one fee page, one numbering and no competing claims. Nothing from the parallel session was reverted or overwritten. What this session kept is the *independent verification* recorded below, because a second pass over the same official pages is exactly what the D16-B QA task was for.

## Independent verification performed on 2026-11-08 (fresh fetches, before the merge)

Every item was read directly from the official page or PDF; the published rows that depend on them are named.

| Official page | What was checked | Result against the published site |
| --- | --- | --- |
| [sf.gov/rent-board-fee](https://www.sf.gov/rent-board-fee) | $59.00 per dwelling unit / $29.50 per guest unit for 2026-2027; March 1 deadline; 5% per month to 15%; June 1 referral; December 14, 2026 exemption deadline; payment channels; $50 payment-failure fee; October/December/January/March-May-June-July timeline | Matches FEE-01/02/03/05/07/08/09/10/11 |
| [sf.gov recover-part-your-rent-board-fee-tenant](https://www.sf.gov/information--recover-part-your-rent-board-fee-tenant) | 50% cap excluding penalties; November 1 occupancy test; deposit-interest deduction vs direct bill; bill contents; banking; not a just cause for eviction; Small Claims | Matches FEE-16/17/18/19/21/22 |
| [Admin Code Ch. 37A (PDF)](https://www.sf.gov/sites/default/files/2022-09/901%20Rent%20Board%20Fee%20Ch.%2037A.pdf) | Sec. 37A.1 scope and (a)-(f) exclusions including the owner-occupied affidavit; Sec. 37A.4 March 1 + 5% at March 1/April 1/May 1 + June 1 referral; Sec. 37A.6 50% cap, methods, banking, (d) owner remains liable | Matches FEE-06/07/08/13/14/16/17/18/19 |
| [Form 573 (PDF)](https://www.sf.gov/documents/29484/573_Rent_Board_Fee_History_25-26_8.26.pdf) | Newest row 7/25-6/26 at $59.00 / $29.50; no 7/26-6/27 row; two oldest rows (7/01-6/02, 7/00-6/01) do not show a 50% tenant share | Matches FEE-03 and flag F40 |
| [2027 Informational Notice](https://www.sf.gov/notice-of-rent-board-fee-and-housing-inventory-requirement) | "No payment is required at this time"; annual exemption request; Monday, December 14, 2026 deadline; March 1, 2027 reporting; the two filings do not satisfy each other; "Some rent increases given without a license will be null and void." | Matches FEE-04/10 and flag F41 |
| [sf.gov/pay-your-rent-board-fee](https://www.sf.gov/pay-your-rent-board-fee) | Still carries "March 1, 2023" and "June 1, 2023" | Confirms flag F39 |
| [Treasurer — Register a Business](https://sftreasurer.org/business/register-business) and [lessor page](https://sftreasurer.org/information-lessors-residential-real-estate) | Fewer-than-four-units exemption, "by reason of that fact alone", per-building treatment, Tax Collector's authority to define a building | Matches FEE-23/24/25 |
| [Civil Code 1942.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV) | 180-day bar on increasing rent after a repair request/complaint; organizing barred under (d); remedies (h)(1)-(2) and attorney's fees (i) | Matches ST-13/ST-14/ST-15 and CHK-14 |
| [sf.gov security deposits](https://www.sf.gov/reports--security-deposits) | 4.2% for 3/1/26-2/28/27; annual interest on the tenant's annual due date; AB 12 one-month cap with the two-month exception for a natural person owning no more than 2 properties / 4 units | Matches FEE-20 |
| [Rent Ordinance Sec. 37.3](https://www.sf.gov/information--sec-373-rent-limitations) | 37.3(a)(1) 60% of CPI, never more than 7%; 37.3(a)(2) banking subject to 37.15 | Matches RATE-09 and PRC-02 |
| [AB 1482 page](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482) | 8.8% for 8/1/26-7/31/27; "This does NOT apply for units under the rent increase limitations of the San Francisco Rent Ordinance"; two-unit and single-family exemption conditions | Matches ST-01, ST-16, ST-17, F34 |
| [Sec. 37.15](https://www.sf.gov/information--sec-3715-reporting-obligations-licensing), [Housing Inventory](https://www.sf.gov/rent-board-housing-inventory), [Noncompliance](https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory), [banked increases](https://www.sf.gov/information--banked-rent-increases), [current rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit) | License condition, 1-9-unit March 1, 2023 start, no monetary penalty for late filing, 24-full-month banking, 1.6%/1.4%/1.7% and 4.2% rates, no 2027-28 row | Matches the license rows, RATE-01 to RATE-08, SUM-06 and flag F27 |

## Result of the merged build

`python3 scripts/build_site.py` then `python3 scripts/validate_site.py` on the merged tree: **108 checks, 0 errors**, 70 sources and 54 flags (F01-F44 plus T03-F01-F10), no broken internal links, no conflict markers, privacy scans passing.

## Limits

- Structural and wording verification only; not legal advice, and no attorney has approved any increase.
- The fee arithmetic is conditional on owner-supplied unit counts; the January 2027 Annual Notice does not exist yet (F43).
- No agent can verify the deploy status of the commit that contains this file, or remove the raw tokens from git history (F44).
