# T49 — Fresh 2026-11-11 line-by-line re-verification (session `arena-04258d5c`)

Focused re-verification of the load-bearing official pages on 2026-11-11 UTC via direct `fetch_page`. This is not a claim that every historical source was rechecked today; each source retains its individual verification date. No raw tenant identifier appears in this file.

## Pages opened directly 2026-11-11

| Site ID | Official URL | Fetch result | Published figure vs official text |
| --- | --- | --- | --- |
| S01 | https://www.sf.gov/learn-about-rent-increases-san-francisco | chunk 0 | 1.6% 3/1/26–2/28/27 confirmed; "A landlord must get a rent increase license before imposing annual allowable and/or banked rent increases"; July 1 2022 / March 1 2023 for 1–9 units; 30/90-day notice +5 mail; base rent only; no rounding up; File 261020 notice still present, "has not been enacted". **No change.** |
| S02 | https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit | chunk 0 | 1.6% / 1.4% / 1.7% confirmed; deposit interest 4.2% 3/1/26–2/28/27; File 261020 notice present; F45 defect still present (label "575 Cap. Imp. Labor Rates" → 574 PDF). **No change.** |
| S07 | https://www.sf.gov/rent-board-housing-inventory | chunk 0 | "All owners of residential property are required to report"; free, March 1, no monetary penalty, notice "not enforceable without having a rent increase license on the effective date"; license auto-generated; fee exemption ≠ inventory. **No change.** |
| S56 | https://www.sf.gov/rent-board-fee | chunk 0 | $59.00/dwelling, $29.50/guest, 50% recovery $29.50, March 1 deadline, 5% monthly max 15%, June 1 delinquent, exemption deadline December 14, 2026. **No change.** |
| S08 | https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory | chunk 0 | Unlicensed increase "may be null and void"; refund; license ONLY for rent-controlled units; not required for §6.14/passthrough; portal check; petitions. **No change.** |
| S05 | https://www.sf.gov/information--banked-rent-increases | chunk 0 | 24 full months; no compounding/prorating; add percentages; license; notice states banked portion; File 261020 notice present. **No change.** |
| S06 | https://www.sf.gov/learn-about-san-francisco-rental-laws | chunk 0 | June 13, 1979 cutoff; Property Information Map check. **No change.** |
| S53 | https://www.sf.gov/information--sec-3715-reporting-obligations-licensing | chunk 0 | §37.15(e): substantially compliant → license; otherwise suspended, tenant not obligated during suspension. **No change.** |
| S73 | https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-xiii-reporting-obligations-under-rent | chunk 0 | Rule 13.14: unlicensed effective increase "shall render the entire rent increase null and void"; effective-date test; July 1 2022 / March 1 2023. **No change.** |
| S27 | https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482 | chunk 0 | 8.8% 8/1/26–7/31/27; "does NOT apply for units under the rent increase limitations of the San Francisco Rent Ordinance". **No change.** |
| S71 | https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770 | chunk 0 | File 261020 Version 1, introduced 9/15/2026, status **Pending Committee Action**, enactment date/# blank, 4 history rows unchanged. **Minor non-legal change:** 6 attachments now listed (Comment Ltrs added since 2026-11-10). Still **NOT ENACTED**; F46 unchanged. |

## Gates run on the final tree (after DATE + statement updates)

- `python3 scripts/build_site.py` — regenerates data/, index, pages, summaries.
- `python3 scripts/validate_site.py` — expected 119 checks, 0 errors (82 sources, 65 flags, 347 rows).
- `python3 research/b87_notice_kit/validate_kit.py` — 19 checks, 0 errors.
- `python3 research/n08_qa/privacy_check.py` — 0 current-tree matches (historical exposure F44 unchanged).
- Independent HTMLParser broken-internal-link sweep — 0 broken.
- Arithmetic (`Decimal`): $3,995 × 1.6% = $63.92 → $4,058.92; $3,150 × 1.6% = $50.40 → $3,200.40; $59.00 ÷ 2 = $29.50. All match the published Calculations page.

## Irregularities found this session

1. **Legistar attachment count** (non-legal): S71 now lists 6 attachments vs 5 on 2026-11-10 (Comment Ltrs added). Status, history rows and enactment fields unchanged. Recorded in the S71 statement; no new flag needed.
2. **No new legal irregularity.** Every load-bearing figure held. Stale PRs #18/#19/#25 remain open (owner call, per T45/T47/T48). F44 (history exposure) remains owner-actionable and does not block.
