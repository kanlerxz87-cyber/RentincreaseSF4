# EA4-V — independent re-verification ledger, 2026-11-11 (UTC)

Session `arena-ea4a9203`. Every entry below is an official page that this session opened directly on 2026-11-11 (UTC) with the page-fetch tool, with the wording copied from the fetched text. Nothing here is taken from an earlier session's ledger. Where a page could not be opened, the entry says so and nothing is marked verified.

This file contains no tenant identifier and nothing derived from one. The published placeholders (Tenant A to Tenant F) are used where a tenant must be mentioned.

How to read it: **Quote** is the official wording. **Rows** lists the published row IDs that rely on it. **Result** is one of `holds` (site matches the official text), `holds, wording` (site matches but could be clearer), `correction` (site should change; listed again in `CORRECTIONS.md`), or `official-page defect` (the official page itself is inconsistent; published as a flag, never "fixed" by guessing).

## Part 1 — San Francisco Rent Board: rate, licence, banking, notice

### S01 — Learn about rent increases in San Francisco
<https://www.sf.gov/learn-about-rent-increases-san-francisco> — fetched 2026-11-11, both chunks (2 of 2).

| # | Quote (official wording) | Rows | Result |
| --- | --- | --- | --- |
| 1 | "The allowed rent increase percentage in San Francisco is 1.6%." "The percentage is effective March 1, 2026 through February 28, 2027." | SUM, RATE-01, CALC-01/02, REAS-01, AN-01, Q-01 | holds |
| 2 | "A landlord must get a rent increase license before imposing annual allowable and/or banked rent increases on a tenant." "To get a rent increase license, a landlord must first report into the Rent Board Housing Inventory." "This is effective July 1, 2022 (or March 1, 2023 for condominiums and buildings with 1-9 residential units)." | SUM, LIC rows, Q-11, AN-17, IND-01 | holds. No wording on the page limits this to corporate owners. |
| 3 | Base rent × .016; base rent includes housing services such as parking or storage; temporary passthroughs are excluded. "Rent increases cannot be rounded up to the nearest dollar." | CALC-06, CHK-06 | holds |
| 4 | First increase 12 months after the tenancy began; the date an increase takes effect becomes the anniversary date; a later increase sets a new anniversary date. | CHK-03, CASE-V4 | holds |
| 5 | "30-day written notice"; "90-day written notice if the increase (either by itself or combined with another increase in the same year) is more than 10%"; "If the notice is mailed, the landlord must give the tenant 5 more days." The notice "should include" the dollar amount, the percentage and the effective date. Use the percentage in effect on the date of the increase. | CHK-05/06/13, Q-04, CALC-10/11 | holds |
| 6 | Extra rent only because a new or additional roommate moved in is an unlawful increase, even if the lease allows it. | REAS-09, AN-07, Q-14 | holds |
| 7 | Multi-year example: move-in June 1, 2023 at $1,000; first increase June 1, 2026 = banked 3.1% (1.7% + 1.4%) + annual 1.6% = 4.7%, new rent $1,047.00. | CALC-07/08 (method) | holds |
| 8 | Change-of-anniversary example (chunk 2): first increase on May 1, 2026 after a June 1, 2023 move-in. The June 1, 2024 increase (1.7%) "has banked"; the June 1, 2025 increase (1.4%) is not banked "because a full 12 months has not elapsed between the date it first became available on June 1, 2025, and the date of the rent increase on May 1, 2026"; "The 1.4% rent increase is permanently lost due to the change in anniversary date". Result $1,033.00; "The new anniversary date is May 1"; "The next rent increase cannot be given until May 1, 2027". "Many owners give annual and banked rent increases on the same date each year to avoid possible issues." | CALC-08, CALC-09, CASE-V4 | holds. This is the official basis for the timing analysis in `CASE_TIMING_ANALYSIS.md`. |
| 9 | Notice box "Posted November 9, 2026": File No. 261020 "would temporarily limit the combined amount of banked rent increases and capital improvement rent increases … to 10% per year"; would apply to banked increases "noticed on or after September 15, 2026"; "This legislation has not been enacted and is subject to change." | RATE-12 to RATE-18, F46, F47 | holds |
| 10 | One-year example: move-in June 1, 2025, increase June 1, 2026, but the text reads "The annual allowable increase in effect on June 1, 2025 is 1.6%". The rate in effect on June 1, 2025 was 1.4% (S02); 1.6% is the rate in effect on June 1, 2026. | F01 | official-page defect (already published as F01; still present today) |
| 11 | Change-of-anniversary example: "12 full months have elapsed since the skipped rent increase first became available (June 1, 2023 – June 1, 2024)" — the increase first became available on June 1, 2024, so the 12 months run June 1, 2024 – June 1, 2025; and "the annual allowable increase in effect on June 1, 2026 (1.6%)" although the increase date in the example is May 1, 2026 (same 1.6% period, so the arithmetic is unaffected). | — | official-page defect, **new today** (see `CORRECTIONS.md` item N1) |

The page links Form 571 at <https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf>.

### S02 — Current Rates
<https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit> — fetched 2026-11-11, chunk 1 of 2.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "1.6% for March 1, 2026 – February 28, 2027"; table: March 1, 2025 – February 28, 2026 1.4%; March 1, 2024 – February 28, 2025 1.7%. | RATE rows, CALC-03/04/07 | holds |
| 2 | No row for March 1, 2027 – February 28, 2028 is published. | F27 | holds (the next rate is still unpublished) |
| 3 | "Security Deposit Interest: 4.2% for March 1, 2026 – February 28, 2027"; prior 5.0% and 5.2%. | FEE-20 | holds |
| 4 | "Rent Board Fees that can be banked": 2024-2025 (3/1/25) $29.50 tenant / $29.50 landlord; 2023-2024 (3/1/24) $29.50 / $29.50. | FEE-18 | holds |
| 5 | The link labelled "575 Cap. Imp. Labor Rates" points to the Form 574 PDF (`…/34916/574_Cap._Imp._Imputed_Interest_26-27_7.26.pdf`). | F45 | official-page defect (already F45; still present today) |
| 6 | Same November 9, 2026 File 261020 notice as S01. | F46, S72 | holds |

### S05 — Banked rent increases
<https://www.sf.gov/information--banked-rent-increases> — fetched 2026-11-11, whole page.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "A skipped increase is only banked if at least 24 full months pass without any rent increase. If less than 24 months pass, the skipped increase is lost and cannot be imposed at a later date." | CHK-04, REAS-02, CALC-05/09, CASE-V9 | holds |
| 2 | "Once an increase is properly banked, it does not expire." "A landlord may also combine a banked increase with a regular annual increase." | CALC-08 | holds |
| 3 | "A landlord does not have to impose the maximum allowed increase." "If only part of the allowable increase is used, the rest is banked. The remaining portion may be imposed at a later time, after at least 12 months have passed, or on a future anniversary date." | — | holds; **not yet used on the site** — it is the official basis for phasing a banked amount in over several years (see `CORRECTIONS.md` item A2) |
| 4 | "Banking has only been allowed since April 1, 1982"; "There is no limit on how much can be banked"; "Banked increases do not expire during a tenancy"; "New owners may use banked increases from prior owners"; "Banked increases do not carry over to a new tenant". | CALC-07 | holds |
| 5 | "Banked increases do not have to be approved by the Rent Board, but must be calculated correctly. They cannot be compounded or prorated." "add the percentage amounts for each year banked together. Then multiply the banked percentage amount by the tenant's current base rent." | CALC-07, Q-12 | holds |
| 6 | Notice: licence first; 30 days, 90 days if more than 10%, 5 more days if mailed; the notice should include the dollar amount, the percentage, the effective date and "Which part of the increase is banked". | CHK-05/06 | holds |
| 7 | Example: "the annual allowable rent increase in effect on August 1, 2024 (1.4%)" although the increase date in the example is August 1, 2025 (1.4% is the rate for March 1, 2025 – February 28, 2026). | F02 | official-page defect (already published as F02; still present today) |
| 8 | Same November 9, 2026 File 261020 notice. | F46 | holds |

### S54 — Annual rent increase for multiple years
<https://www.sf.gov/information--annual-rent-increase-multiple-years> — fetched 2026-11-11, whole page.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "Increases cannot be compounded"; "Landlords are not required to file a petition with the City to impose these types of rent increases"; "Landlords cannot "round up" to the nearest dollar". | AN-18, Q-12 | holds |
| 2 | "Landlords must give at least 30-days notice in writing before any increase goes into effect (or 35-days if sent by mail)". The page does not mention the 90-day rule for increases above 10%, although its own method can produce a total above 10%. | CHK-13 | official-page defect, **new today** (item N2): the 90-day rule is on S01 and S05 and in Civil Code 827, which control |
| 3 | The worked example links an out-of-date Form 571 ("571 Allowable Annual Increases 24-25 EN 11.17.23.pdf"). The percentages used (2.2% + 1.6% + 2.6% + 1.8% = 8.2%) match the current Form 571 series. | — | official-page defect, minor, **new today** (item N2) |
| 4 | Same November 9, 2026 File 261020 notice. | F46 | holds |

### S77 — Rent Board Rules and Regulations Part IV (Rules 4.10 and 4.12)
<https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-iv-rent-increases-not-requiring> — fetched 2026-11-11, chunks 1 and 2 of 4.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | Rule 4.10(a): the landlord "shall inform the tenant in writing on or before the date the notice is given" of "(1) Which portion of the rent increase reflects the annual increase, and/or banked amount, if any". | CHK-06, worksheet rows | holds |
| 2 | Rule 4.10(b): "Any rent increase which does not conform with the provisions of this Section shall render the entire rent increase null and void, unless the amount requested equals no more than the allowable annual and banked rent increase(s)"; good-faith tolerance of "one-half of one percent of the prior base rent". | worksheet rows | holds |
| 3 | Rule 4.12(a): "the rent may be increased only one time every twelve (12) months. This banked amount may only be given at the time of an annual increase." "A full 12 months must have elapsed from the date that an annual rent increase, or a portion thereof, could have been imposed before this banking section becomes applicable. Banked increases shall not be compounded and shall not be rounded up". | CHK-03/04, F03, B87-F03 | holds. In the Rent Board's own example (S01 item 8) the two descriptions give the same dates: the first increase can be imposed 12 months after move-in, and it is banked 12 months after that, which is 24 months with no increase. F03 and B87-F03 can say so; they stay published because the wording on the two pages still differs. |
| 4 | Rule 4.12(b): to impose a banked increase the landlord shall inform the tenant "which portion of the rent increase reflects banked amount, and (2) the dates upon which said banked amount is based; provided, however, that failure to include such information shall not render the increase null and void." | CHK-06 | holds, wording: the site should say the notice states the banked portion **and the dates it is based on** (item A3) |

### S76 — Rules and Regulations, complete PDF effective January 13, 2026 (Rules 1.11 and 1.12)
<https://media.api.sf.gov/documents/625_RR_Complete_1-13-26.pdf> — fetched 2026-11-11, chunk 2 of 9.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | Rule 1.11(a): "The anniversary date is the date on which the tenant's current rent became effective … The next allowable rent increase shall take effect no less than one year from the anniversary date, but when imposed after one year, shall set a new anniversary date for the imposition of future rent increases." | CHK-03, CASE-V4 | holds |
| 2 | Rule 1.12(a): the annual allowable increase "shall become effective each March 1, and shall be no more than 60% of the percentage increase in the Consumer Price Index (CPI) for All Urban Consumers in the San Francisco region … for the 12 month period ending October 31"; "because the CPI index for October 2025 was not published by the U.S. Department of Labor, the October 2025 CPI shall be approximated using the geometric mean of the CPI values published for August 2025 and December 2025"; "In no event, however, shall the allowable annual increase be greater than seven percent (7%). The Rent Board shall publish the annual allowable increase amount on or about January 1." | RATE rows, F27 | holds. The next rate (from March 1, 2027) is therefore expected around January 2027; no figure is published and none is estimated here. |

### S07 — The Rent Board Housing Inventory
<https://www.sf.gov/rent-board-housing-inventory> — fetched 2026-11-11, both chunks.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "All owners of residential property are required to report." "If you own residential property, you are required to report into the Housing Inventory online through the Rent Board Portal. Property owners who have tenants will receive a rent increase license after the submission." | SUM, LIC rows, Q-11, AN-17 | holds. "All owners": no exception for an individual owner. |
| 2 | "Reporting is free and can be done online 24/7." | LIC rows, Q-15 | holds |
| 3 | "If your unit is covered under rent control, you will need to comply with the Housing Inventory requirements before any annual or banked rent increase notice goes into effect." | LIC rows, CHK-02/11 | holds |
| 4 | "March 1 of every year. You can still make a Housing Inventory submission and receive a rent increase license after the deadline. However, your rent increase notice will not be enforceable without having a rent increase license on the effective date of the notice." "The Rent Board does not assess monetary penalties for filing after the deadline." | LIC rows, Q-17 | holds |
| 5 | "once you have reported into the Housing Inventory, a rent increase license will be automatically generated for non-owner occupied units. A landlord must have a current rent increase license on file with the Rent Board before any annual or banked rent increase can go into effect. The rent increase license does not need to be included with your rent increase notice." | Q-12, LIC rows | holds. There is no separate licence application. |
| 6 | "The information entered in the housing inventory submission is public." | CASE-V10, AN-19 | holds |
| 7 | "Any changes of a property owner's business contact information must be updated within 30 days." | Q-17 | holds |
| 8 | Non-owner-occupied unit fields: name and business contact information (or the property manager's), business registration number "if any", approximate square footage in 250-square-foot increments, bedrooms, bathrooms, date the current occupancy began, base rent "in $250.00 increments" and whether it includes utilities. "All information submitted is done under penalty of perjury." | process rows, FEE-24 | holds |
| 9 | "You will need to set up an account and use the PIN number on your Annual Notice to add property to your account. If you need to reset your pin number you can call 311 (415-701-2311 from outside San Francisco)." Paper filing is possible by email to the Rent Board inventory address or drop-off 9:00 AM to 4:00 PM. | process rows | holds |
| 10 | "Please note that reporting into the Rent Board Housing Inventory does not request an exemption of the Rent Board Fee." | FEE-04, Q-15 | holds |
| 11 | "If you are a tenant, you can search the Rent Board Portal to see if your landlord is up to date with their rent increase license." | CHK-02, AN-25 | holds |

The older FAQ address linked from S01 and S05 (`https://sf.gov/information/rent-board-housing-inventory-frequently-asked-questions-faq`) now redirects to this same page.

### S08 — Notice of Owner Noncompliance with Housing Inventory
<https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory> — fetched 2026-11-11, whole page.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "A rent increase notice that goes into effect while the unit is unlicensed may be null and void (this may apply for multiple years)". "If the unit is rent-controlled and you issued a rent increase that went into effect when no license was on record, your tenant may be entitled to a rent refund." | Q-13, AN-16, CHK-16 | holds |
| 2 | "Owners of condominiums and buildings with less than 10 residential units have been required to report since March 1, 2023, with updates due every following March". | Q-11, AN-17 | holds |
| 3 | "The Rent Increase License rules apply ONLY to units under San Francisco Rent Control." "A current Rent Increase License must be on file with the San Francisco Rent Board before any annual or banked rent increase goes into effect." | LIC rows | holds |
| 4 | "The Rent Increase License is not required in some situations where the original occupant(s) no longer live in the unit, or for passthroughs allowed under the Rent Ordinance". | FEE-22, LIC rows | holds |
| 5 | Tenant steps: check the Portal for a licence "on the effective date of your rent increase"; if none, file a Tenant Petition for Unlawful Rent Increase; if the increase has not yet taken effect, a Tenant Summary Petition, after which "a Rent Board staff person will send a letter to the landlord that explains they must obtain a Rent Increase License before the rent increase goes into effect." | Q-13, Q-21 | holds |
| 6 | Counselling phone 415-252-4600, Monday to Friday 9 am to 12 pm and 1 pm to 4 pm; office drop-in 9 am to 4 pm. | resource rows | holds |

### S53 — Administrative Code Sec. 37.15 (Rent Board copy)
<https://www.sf.gov/information--sec-3715-reporting-obligations-licensing> — fetched 2026-11-11, whole page.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | (a) "Owners of residential dwelling units subject to this Chapter 37 shall be required to report certain information about their units to the Rent Board … In the case of a unit owned by multiple owners, reporting by a single owner shall suffice." | Q-11, AN-17 | holds. The duty attaches to "owners"; the section does not distinguish individuals from companies. |
| 2 | (c) "For condominium units and units in buildings with fewer than 10 units, the information shall be reported commencing March 1, 2023 and updated annually by March 1 of each successive year. Unit information shall also be updated within 30 days of any change in the name or business contact information of the owner or designated property manager." | Q-17 | holds |
| 3 | (e) "If a landlord has substantially complied with the obligation to report information about a rental unit as required under this Section 37.15, the landlord shall receive a license to impose rent increases on tenants in that unit under Sections 37.3(a)(1)-(2). If the landlord has not substantially complied with the reporting obligation, then the license to impose rent increases shall be temporarily suspended during the period of the landlord's noncompliance. Upon receipt of the required information from the landlord, the suspension shall be terminated, and the license to impose rent increases shall be restored prospectively, but a tenant shall not be obligated to pay the increased rent for months during the period of suspension." | Q-13, CHK-16/17, AN-27 | holds |
| 4 | (d) "The Rent Board shall not use the information to operate a rental registry within the meaning of California Civil Code Sections 1947.7 – 1947.8." | — | holds (context) |
| 5 | (b)(2)(B) "the business registration number for the unit, if any". | FEE-24 | holds |

### S73 — Rules and Regulations Part XIII (Rule 13.14)
<https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-xiii-reporting-obligations-under-rent> — fetched 2026-11-11, whole page.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "Any rent increase under Ordinance Sections 37.3(a)(1)-(2) purporting to be effective while the landlord is unlicensed shall render the entire rent increase null and void; provided, however, that the effective date of the rent increase, not the date of service, shall be used to determine whether or not the increase conforms with the provisions of this section. Nothing in this Regulation shall affect a landlord's banking rights or the ability to accumulate otherwise lawful rent increases that were found to be null and void." | B87-F02, CHK-16, summary | holds. The legal test is the **effective date**; reporting before serving the notice is the cautious practice, not the legal deadline. |
| 2 | "with respect to condominium units and buildings with less than ten residential units, this section shall only apply to rent increases that are effective on or after March 1, 2023." | Q-11 | holds |
| 3 | Rule 13.13: an owner who reports "on information or belief", approximately, or as unknown where the information cannot be obtained "shall be deemed to have substantially complied". | process rows | holds |

## Part 2 — Pending legislation, File No. 261020

### S71 — Legistar record
<https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770> — fetched 2026-11-11.

| Field | Value at fetch |
| --- | --- |
| File # / Version | 261020 / 1 |
| Name | Administrative Code - Cap On Rent Increases for Rent-Controlled Units |
| Type / Status | Ordinance / **Pending Committee Action** |
| Introduced | 9/15/2026 |
| In control | Land Use and Transportation Committee |
| On agenda / Final action / Enactment date / Enactment # | all blank |
| History | 4 records: 9/15/2026 President, ASSIGNED UNDER 30 DAY RULE; 9/18/2026 and 9/30/2026 Clerk of the Board, REFERRED TO DEPARTMENT; 10/7/2026 Youth Commission, RESPONSE RECEIVED |
| Attachments | 6: Leg Ver1, Leg Dig Ver1, Referral FYI 091826, Referral YC 093026, YC Response 100726, Comment Ltrs |

Result: `holds` for RATE-12 to RATE-18, REQ-25, F46. **Not enacted.**

### Legislative Digest, Version 1 (official attachment 2 of the Legistar record)
<https://sfgov.legistar.com/View.ashx?M=F&ID=15865647&GUID=CC09B796-4675-4A7D-9960-85FE239F7FBB> — fetched 2026-11-11, whole document.

- Existing law: "The Rent Ordinance does not limit the amount of Banked Increases that a landlord can impose."
- Proposal: "a landlord could not impose Banked Increases and/or Capital Improvement Increases that caused a tenant's rent to increase by more than 10% of the lowest base rent that was in effect during the previous 12 months."
- Reach and duration: "The 10% cap would apply to Banked Increases based on rent increase notices that landlords provided to their tenants on or after September 15, 2026, and to Capital Improvement petitions that landlords filed with the Rent Board on or after that date, and would remain in effect until December 31, 2029."
- Carry-over: "A landlord would be able to accumulate Banked Increases and Capital Improvement Increases that exceeded 10% during the time when the 10% limit would remain in effect, and could impose those excess increases on or after January 1, 2030, as otherwise permitted by law."

### Ordinance text, Version 1 (official attachment 1)
<https://sfgov.legistar.com/View.ashx?M=F&ID=15865646&GUID=0E2E6936-000B-4597-A4EE-FBB17C19636E> — fetched 2026-11-11, chunks 1 and 3 of 3.

- Proposed Sec. 37.3(h): a landlord may not impose banked increases under Sec. 37.3(a)(2) and/or capital-improvement increases under Sec. 37.3(a)(3) "that cause a tenant's rent to increase by more than a total of 10% of the lowest base rent that was in effect at any time during the 12 months immediately preceding the date the increase takes effect"; the limit "shall apply to banked rent increases based on rent increase notices provided on or after September 15, 2026 … and shall remain in effect until December 31, 2029 unless extended by ordinance."
- The proposed limit names Sec. 37.3(a)(2) (banking) and (a)(3) (capital improvements). It does not name Sec. 37.3(a)(1), the ordinary annual increase.
- Proposed addition to Sec. 37.15(b)(2)(F): owners would also report "whether any banked rent increases were imposed under Section 37.3(a)(2) during the previous 12 months".
- Section 5: "This ordinance shall become effective on the 31st day after enactment."

Result: `correction` for flag F47, which says that "no page states how the 10% is measured" and treats the duration as unclear. The official digest and ordinance text attached to the same Legistar record state both (measure: 10% of the lowest base rent in the preceding 12 months; duration: until December 31, 2029; excess may be imposed from January 1, 2030). The proposal is still **not law** and may be amended. See `CORRECTIONS.md` item C1.

## Part 3 — Rent Board Fee and state rent cap

### S56 — The Rent Board Fee
<https://www.sf.gov/rent-board-fee> — fetched 2026-11-11, chunk 1 of 2.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "For the 2026-2027 tax year, the fee is: $59.00 per dwelling unit; $29.50 per guest unit". "you may be able to collect 50% of the fee from your tenants, which is $29.50 per dwelling unit or $14.75 per guest unit." | FEE-03, FEE-16, FEE-26/27, Q-15/16 | holds |
| 2 | "March 1 of each year for the Rent Board Fee. A 5% late penalty will be added to the amount of the fee every month following March 1 (for a maximum penalty of 15%)." | FEE-07, FEE-28 | holds |
| 3 | "Fees that have not been paid in full by June 1 will be referred to the Bureau of Delinquent Revenue" versus the timeline: July, Notice of Delinquent Payment, then "30 days from the mailing date to make a payment before the account is referred". | FEE-08, F38 | official-page defect (already F38; still present today) |
| 4 | "The deadline to submit a Request for Exemption for the 2027 Rent Board fee is December 14, 2026. Units without a valid and approved exemption will be billed for the Rent Board fee, due by March 1, 2027." | FEE-10/11 | holds |
| 5 | "Please note that requesting a Rent Board Fee exemption does not satisfy Rent Board Housing Inventory reporting requirements." | FEE-04, Q-15 | holds |
| 6 | "All residential property owners must pay a per-unit Rent Board fee unless the unit(s) have a current exemption. This includes single-family homes and condominiums, units built after 1979, vacant units, and units occupied by friends or family members." | FEE-01/02 | holds |
| 7 | Payment: online through the Portal (preferred); in person at the Treasurer and Tax Collector, City Hall Room 140; by mail to PO Box 7429, San Francisco, CA 94120-7429; "No payments are accepted at the Rent Board office"; $50.00 Payment Failure Fee. | FEE-05/09 | holds |
| 8 | "Once you have paid the Rent Board fee in full, you can recover 50 percent of the fee from the tenants in occupancy of each unit if the tenant has been living in the unit as of November 1 of the applicable tax year." "You may not recover any penalty fees you owed". | FEE-16, Q-16 | holds |
| 9 | Owner-occupied exemption: "occupied by an owner of record and is not rented at any time"; "Vacant units or units solely occupied by children or close relatives not on title as owner do not qualify". | FEE-13 | holds |

### S27 — California Tenant Protection Act of 2019 (AB 1482), Rent Board page
<https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482> — fetched 2026-11-11, chunk 1 of 2.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "The maximum rent increase for units under AB 1482 from August 1, 2026 to July 31, 2027 is 8.8% in San Francisco. This does NOT apply for units under the rent increase limitations of the San Francisco Rent Ordinance." | ST rows, AN-02, Q-01 | holds |
| 2 | "Limits annual rent increases to no more than 5% + local CPI (CPI = inflation rate), or 10% whichever is lower." "The current applicable CPI increase for San Francisco (that is, from August 1, 2026 to July 31, 2027), is 3.8%. Thus, the maximum annual increase for units subject to AB 1482 is currently 8.8% (5% + 3.8%)." | ST rows | holds |
| 3 | Rent-cap exemption: "Units that are already subject to a local rent control ordinance that restricts annual rent increases to an amount less than 5% + CPI." | AN-02, Q-19 | holds |
| 4 | "A two-unit property, provided the second unit was occupied by an owner of the property for the entire period of the tenancy." | Q-19 | holds |
| 5 | "the Rent Board does not provide legal advice and cannot enforce state law or conduct hearings on disputes about AB 1482. AB 1482 can only be enforced in state court." | ST rows | holds |

## Part 4 — Ordinance text, rate history, coverage, roommates

### S21 — Administrative Code Sec. 37.3 (Rent Board copy)
<https://www.sf.gov/information--sec-373-rent-limitations> — fetched 2026-11-11, chunks 1 and 3 of 5.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | (a)(1) "A landlord who has reported the required information about their rental unit to the Rent Board as set forth in Section 37.15 shall have a license to impose annually a rent increase which does not exceed a tenant's base rent by more than 60% of said published increase. In no event, however, shall the allowable annual increase be greater than 7%." | REQ-23, LIC rows, Q-11 | holds. The licence condition is in the ordinance itself and is written for "a landlord", with no carve-out by type of owner. |
| 2 | (a)(2) "A landlord who refrains from imposing an annual rent increase or any portion thereof may accumulate said increase and, subject to Section 37.15, impose that amount on the tenant's subsequent rent increase anniversary dates." | REAS-02, CALC-07 | holds |
| 3 | (a)(8) "A landlord who seeks to impose any rent increase which exceeds those permitted above shall petition for a rental arbitration hearing". | REAS-03 to REAS-08 | holds |
| 4 | (a)(11)(A) "a landlord may not impose increases solely because a tenant has added an additional occupant to an existing tenancy … The prohibition … shall apply notwithstanding a rental agreement or lease that specifically permits a rent increase for additional occupants." | REAS-09, Q-14, AN-07 | holds |
| 5 | (b) "On or before the date upon which a landlord gives a tenant legal notice of a rent increase, the landlord shall inform the tenant, in writing, of the following: (1) Which portion of the rent increase reflects the annual increase, and/or a banked amount, if any; …" "(5) Nonconforming Rent Increases. Any rent increase which does not conform with the provisions of this section shall be null and void." | CHK-06, B87-F04, worksheet rows | holds |

### S04 — Form 571, Allowable Annual Increases 26-27
<https://www.sf.gov/documents/34344/571_Allowable_Annual_Increases_26-27_1.pdf> (redirects to `https://media.api.sf.gov/documents/571_Allowable_Annual_Increases_26-27_1.pdf`, the address the site cites) — fetched 2026-11-11, whole document.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "Effective March 1, 2026 through February 28, 2027, the allowable annual increase amount is 1.6%." "$2,000.00 x .016 = $32.00". | RATE rows, CALC-01/02 | holds |
| 2 | 3/1/25 – 2/28/26 1.4%; 3/1/24 – 2/28/25 1.7%; 3/1/23 – 2/29/24 3.6%; 3/1/22 – 2/28/23 2.3%; 3/1/21 – 2/28/22 0.7%; 3/1/20 – 2/28/21 1.8%; 3/1/19 – 2/29/20 2.6%. | CALC-07, CALC-08 | holds. 1.8 + 0.7 + 2.3 + 3.6 + 1.7 + 1.4 = 11.5 (checked with exact decimal arithmetic in `checks.py`). |
| 3 | The document's title metadata reads "517: Allowable Annual Increases 26-27" although it is Form 571. | F04 | official-page defect (already F04; still present today) |

### S06 — Learn about San Francisco rental laws
<https://www.sf.gov/learn-about-san-francisco-rental-laws> — fetched 2026-11-11, whole page.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "Many residential units built on or before June 13, 1979 have both rent control and eviction protection." "You can search your address on the Property Information Map." "If your unit was built before June 14, 1979, and is not used as a single family dwelling, it may have both: Rent control; Eviction protection". | CHK-01, CASE-V1/V2, AN-28 | holds |
| 2 | Units with eviction protection only include "Most single-family homes and condos (if you moved in on or after Jan 1, 1996)". | Q-20, F35 | holds |
| 3 | "For example, the allowed rent increase percentage for 2024 to February 28, 2025 is 1.7%." | F24 | official-page defect (already F24; still present today) |
| 4 | "Rent Board counselor 415-252-4600 … Weekday free counseling hours (9 am to noon and 1 to 4pm)". | resource rows | holds |

### S16 — Rent increases under Section 6.14 and Costa-Hawkins
<https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins> — fetched 2026-11-11, whole page.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "The landlord may be entitled to increase the rent to market rate in certain roommate situations when the original tenants no longer live in the unit." "Since these provisions can be complicated, landlords and tenants should obtain legal advice". | Q-09, Q-14, CASE-V5 to V8 | holds |
| 2 | Section 6.14 "provides for an unlimited rent increase on remaining occupants when the last original occupant vacates the unit, as long as the landlord timely served all remaining occupants with a written "6.14 notice."" "Generally, sixty days is considered reasonable." | CASE-V8, F28 | holds |
| 3 | "a co-tenant, as opposed to a subtenant, is not subject to such a rent increase, regardless of when the co-tenant moved in. A co-tenant is someone who has an oral or written agreement with the landlord, or who has become a tenant by the conduct of the parties such as the landlord's acceptance of rent." | CASE-V5, Q-14 | holds |

On the owner-supplied facts one original Unit 1 tenant (Tenant A) still lives in the unit, so the condition "when the last original occupant vacates" is not met. That is a reading of supplied facts, not an official finding; the published rows already keep it blank and flagged.

## Part 5 — California statutes

### S35 — Civil Code section 827
<https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827&lawCode=CIV> — fetched 2026-11-11, both chunks. Last amended by Stats. 2024, Ch. 1015 (SB 1103), effective January 1, 2025.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | (b)(1) "In all leases of a residential dwelling … from week to week, month to month, or other period less than a month, the landlord may increase the rent provided in the lease or rental agreement, upon giving written notice to the tenant, as follows, by either of the following procedures: (A) By delivering a copy to the tenant personally. (B) By serving a copy by mail under the procedures prescribed in Section 1013 of the Code of Civil Procedure." | CHK-07, Q-04, worksheet rows | holds. The section is written for week-to-week and month-to-month tenancies; a fixed-term lease is a separate question (B87-F07). |
| 2 | (b)(2) "If the proposed rent increase for that tenant is 10 percent or less of the rental amount charged to that tenant at any time during the 12 months before the effective date of the increase, either in and of itself or when combined with any other rent increases for the 12 months before the effective date of the increase, the notice shall be delivered at least 30 days before the effective date of the increase, and subject to Section 1013 of the Code of Civil Procedure if served by mail." | CHK-05, CALC-10/11 | holds |
| 3 | (b)(3)(A) "greater than 10 percent … the notice shall be delivered at least 90 days before the effective date of the increase". | CHK-13, CALC-08 | holds |
| 4 | (c) "If a state or federal statute, state or federal regulation, recorded regulatory agreement, or contract provides for a longer period of notice regarding a rent increase than that provided in subdivision (a) or (b), the personal service or mailing of the notice shall be in accordance with the longer period." | CHK-05 | holds |

### S57 — Civil Code section 1942.5
<https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV> — fetched 2026-11-11, both chunks.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | (a) "If the lessor retaliates against the lessee because of the exercise by the lessee of the lessee's rights under this chapter or because of the lessee's complaint to an appropriate agency as to tenantability of a dwelling, and if the lessee of a dwelling is not in default as to the payment of rent, the lessor may not … increase the rent … within 180 days of any of the following" (five listed events). | ST-13, CHK-14, Q-18, F48 | holds |
| 2 | (b) "A lessee may not invoke subdivision (a) more than once in any 12-month period." | ST-13 | holds |
| 3 | (d) unlawful to increase rent "for the purpose of retaliating against the lessee because the lessee has lawfully organized or participated in a lessees' association … or has lawfully and peaceably exercised any rights under the law"; "the lessee shall bear the burden of producing evidence that the lessor's conduct was, in fact, retaliatory." | ST-13, Q-18 | holds |
| 4 | (f) "This section does not limit in any way the exercise by the lessor of the lessor's rights under any lease or agreement or any law pertaining to the hiring of property or the lessor's right to do any of the acts described in subdivision (a) or (d) for any lawful cause." | ST-13, CHK-14 | holds, wording: the site attributes "lawful cause" to subdivision (g); the words are in **(f)** (item C2) |
| 5 | (g) a lessor may do the acts "if the notice of termination, rent increase, or other act … states the ground upon which the lessor, in good faith, seeks to … increase rent … If the statement is controverted, the lessor shall establish its truth at the trial or other hearing." | ST-13, CHK-14 | holds, wording: (g) is the stated-ground rule. It is a reason to state the ground of the increase in the notice (item A4). |
| 6 | (h) actual damages and "Punitive damages in an amount of not less than one hundred dollars ($100) nor more than two thousand dollars ($2,000) for each retaliatory act where the lessor or agent has been guilty of fraud, oppression, or malice"; (i) attorney's fees "to the prevailing party if either party requests attorney's fees upon the initiation of the action". | Q-18 | holds |
| 7 | (j) "The remedies provided by this section shall be in addition to any other remedies provided by statutory or decisional law." | Q-18 | holds |

### S36 / S58 — Civil Code section 1947.12 (state rent cap, AB 1482)
<https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV> — fetched 2026-11-11, chunks 1 and 2 of 3.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | (a)(1) an owner "shall not, over the course of any 12-month period, increase the gross rental rate for a dwelling or a unit more than 5 percent plus the percentage change in the cost of living, or 10 percent, whichever is lower, of the lowest gross rental rate charged for that dwelling or unit at any time during the 12 months prior to the effective date of the increase." | ST rows, Q-01 | holds |
| 2 | (a)(2) "shall not be increased in more than two increments over that 12-month period". | ST rows | holds |
| 3 | (d)(3) the section does not apply to "Housing subject to rent or price control through a public entity's valid exercise of its police power … that restricts annual increases in the rental rate to an amount less than that provided in subdivision (a)." | AN-02, Q-01, Q-19 | holds. This is the statutory reason the 8.8% state figure is not the limit for a unit under the San Francisco Rent Ordinance. |
| 4 | (d)(6) "A property containing two separate dwelling units within a single structure in which the owner occupied one of the units as the owner's principal place of residence at the beginning of the tenancy, so long as the owner continues in occupancy, and neither unit is an accessory dwelling unit or a junior accessory dwelling unit." | Q-19, F34 | holds |
| 5 | (e) "An owner shall provide notice of any increase in the rental rate, pursuant to subdivision (a), to each tenant in accordance with Section 827." | ST rows | holds |

## Part 6 — Fair housing (the "one unit or both" question)

### S41 — 42 U.S.C. 3603 and 3604 (Fair Housing Act)
<https://www.govinfo.gov/link/uscode/42/3604> (resolves to the GovInfo PDF of the 2024 edition of the U.S. Code) — fetched 2026-11-11, chunk 1 of 3.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | Sec. 3604(b): unlawful "To discriminate against any person in the terms, conditions, or privileges of sale or rental of a dwelling, or in the provision of services or facilities in connection therewith, because of race, color, religion, sex, familial status, or national origin." Sec. 3604(f)(2): the same for "a handicap". | FED rows, AN-03, Q-08 | holds |
| 2 | Sec. 3603(b)(2) exempts "rooms or units in dwellings containing living quarters occupied or intended to be occupied by no more than four families living independently of each other, if the owner actually maintains and occupies one of such living quarters as his residence." | FED rows | holds. Whether the owner lives in the building was not supplied; no exemption is asserted, and California law (S38) has no such gap for these units. |

### S42 — 24 CFR 100.500 (discriminatory effect)
<https://www.ecfr.gov/current/title-24/subtitle-B/chapter-I/part-100/subpart-G/section-100.500> — fetched 2026-11-11, both chunks. The page displayed "up to date as of 11/09/2026. Title 24 was last amended 8/20/2026."

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "Liability may be established under the Fair Housing Act based on a practice's discriminatory effect … even if the practice was not motivated by a discriminatory intent. The practice may still be lawful if supported by a legally sufficient justification". | AN-04, FED rows, Q-08 | holds |
| 2 | (b)(1) a legally sufficient justification exists where the practice "(i) Is necessary to achieve one or more substantial, legitimate, nondiscriminatory interests … and (ii) Those interests could not be served by another practice that has a less discriminatory effect." (b)(2) it "must be supported by evidence and may not be hypothetical or speculative." | AN-04, AN-08, CHK-09 | holds |
| 3 | (d) such a justification "may not be used as a defense against a claim of intentional discrimination." | AN-04 | holds |
| 4 | Date wording on the site: AN-04 says "Current eCFR as of 11/04/2026". | AN-04 | correction, date only (item D1): the page now displays 11/09/2026; the text is unchanged |

### S38 — Government Code section 12955 (California FEHA, housing)
<https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=12955.&lawCode=GOV> — fetched 2026-11-11, chunk 1 of 2.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | (a) unlawful "For the owner of any housing accommodation to discriminate against or harass any person because of the race, color, religion, sex, gender, gender identity, gender expression, sexual orientation, marital status, national origin, ancestry, familial status, source of income, disability, veteran or military status, or genetic information of that person." | AN-05, ST rows, Q-08 | holds |
| 2 | (f) unlawful to "harass, evict, or otherwise discriminate against any person in the sale or rental of housing accommodations when the owner's dominant purpose is retaliation against a person who has opposed practices unlawful under this section". | AN-05 | holds |

None of these three texts says that a landlord must raise the rent of every unit, or of none. What they prohibit is different treatment because of a protected characteristic, and neutral practices with an unjustified discriminatory effect. Rows Q-08 and AN-08 say this and stay flagged (F22) because no official source gives a both-units rule either way.

## Part 7 — How large corporate landlords report rent changes (SEC filings)

### S48 — Independence Realty Trust, Exhibit 99.2 to Form 8-K (earnings release dated February 11, 2026)
<https://www.sec.gov/Archives/edgar/data/1466085/000143774926003792/ex_895776.htm> — fetched 2026-11-11, chunks 1 to 3 of 17.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | Same-Store Portfolio table, Q4 2025: Average Occupancy 95.4%; "Lease Over Lease Effective Rental Rate Growth": New Leases (3.7)%, Renewal Leases 2.9%, Blended 0.8%; Resident Retention Rate 61.4%. | CORP-01, SUM-09, Q-02 | holds |
| 2 | Same table, Q3 2025: Average Occupancy 95.3%; New Leases (3.5)%, Renewal Leases 2.6%, Blended 0.1%; Resident Retention Rate 60.4%. | CORP-02 | holds |
| 3 | "We completed renovations of 2,003 units during the year ended December 31, 2025, achieving a weighted average return on investment of 15.3%, with an average cost per unit renovated of $19,661, and an average monthly rent increase per unit of $251 over unrenovated comparable units." | CORP-03 | holds |
| 4 | Footnote (2): "Lease-over-lease effective rent growth represents the change in effective monthly rent, as adjusted for concessions, for each unit that had a prior lease and current lease that are for a term of 9-14 months." Footnote (4): "Q4 2025 new, renewal, and blended lease over lease rent growth for all leases was (6.2)%, 3.0% and (1.0)%, respectively." | CORP-01 | holds, wording: the published figures are the like-term (9 to 14 month) measure; the all-lease figures differ (item A5) |
| 5 | "Same-store portfolio includes 105 properties, which represent 30,502 units." IRT "owns and operates multifamily communities, across non-gateway U.S. markets." | CORP rows | holds: not San Francisco, not rent-controlled housing |

### S49 — Invitation Homes Inc., Form 10-K for the year ended December 31, 2025
<https://www.sec.gov/Archives/edgar/data/1687229/000168722926000016/invh-20251231.htm> — fetched 2026-11-11, chunks 43 and 44 of 81 (pages 65 to 69 of the filing).

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "Renewal lease net effective rental rate growth for the total portfolio averaged 4.6% and 4.9% for the years ended December 31, 2025 and 2024, respectively, and new lease net effective rental rate growth for the total portfolio averaged (0.8)% and 1.0% for the years ended December 31, 2025 and 2024, respectively." | CORP-04, CORP-05, SUM-09, Q-02 | holds |
| 2 | "We enter into leases directly with our residents, and the leases typically have a term of one to two years." | CORP rows | holds; **not yet used on the site** (item A5): it shows the corporate pattern is a rent change at each lease renewal |
| 3 | "we compare the monthly rent from an expiring lease to the monthly rent from the next lease for the same home … Leases are either renewal leases, where our current resident stays for a subsequent lease term, or new leases, where our previous resident moves out and a new resident signs a lease". | CORP rows | holds |
| 4 | "As of December 31, 2025 and 2024, we owned 86,192 and 85,138 single-family rental homes". | CORP rows | holds: portfolio-wide, not San Francisco specific |

Both filings were reachable and say what rows CORP-01 to CORP-05 and SUM-09 publish. See `UNMERGED_WORK_REVIEW.md` for the unmerged commits that would have blanked them.

### S03 — Rent Board announcement of the 2026-27 rate
<https://www.sf.gov/news--annual-rent-increase-3126-22827-announced> — fetched 2026-11-11, whole page.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "January 14, 2026": "For rent-controlled units, the annual allowable increase amount effective March 1, 2026 through February 28, 2027 is 1.6%." "$2,000.00 x .016 = $32.00". "The annual allowable increase amount effective March 1, 2025 through February 28, 2026 is 1.4%." | RATE rows | holds |
| 2 | The "complete list" link on this page still points to the 25-26 edition of Form 571. | F32 | official-page defect (already recorded; still present today) |

### S25 — Report an unlawful rent increase
<https://www.sf.gov/report-unlawful-rent-increase-or-request-review-your-rent-history> — fetched 2026-11-11, whole page.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "There is no charge for filing the petition"; "There is no time limit for filing a petition". | Q-21, Q-06 | holds |
| 2 | "Usually within a few months after the petition is filed, it will be scheduled for an arbitration hearing before a Rent Board Administrative Law Judge." "The hearing process is designed so that no one needs an attorney, although parties are entitled to have an attorney or other authorized representative assist them at the hearing." | Q-06, Q-13, Q-21 | holds |
| 3 | The "Eligibility" block appears twice on the page. | F16 | official-page defect (already F16; still present today) |

### S62 — Recover part of your Rent Board fee from the tenant
<https://www.sf.gov/information--recover-part-your-rent-board-fee-tenant> — fetched 2026-11-11, whole page.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "A landlord who has paid the Rent Board fee in full may be able to collect 50% of the Rent Board fee (excluding any late penalties that have been added to the fee) from the tenant(s) residing in the unit." | FEE-16, Q-16 | holds |
| 2 | "The landlord may only bill the tenant for the Rent Board fee if the tenant was residing in the unit on or before November 1 in the year before the fee became due." | FEE-16, FEE-27 | holds |
| 3 | Recover by "Deducting it from the tenant's security deposit interest due to the tenant each year" or "Billing the tenant directly (Only if there is no (or insufficient) security deposit held by the landlord, or if the landlord already pays the tenant's security deposit interest annually)." The bill should state "That the purpose of the fee is to fund the Rent Board" and "That the fee is due and payable within 30 days of the date of the bill". | FEE-17 | holds |
| 4 | "Banking only applies to fees assessed from November 1999 on." | FEE-18 | holds, wording: FEE-18 says "after July 25, 1999" from Chapter 37A; both are official and are shown side by side at integration (item A6) |
| 5 | "A tenant's failure to pay the Rent Board fee is not a just cause for eviction. The landlord must go to Small Claims Court in order to collect an unpaid fee." | FEE-19 | holds |

## Part 8 — Fee ordinance, petition statistics, single-family exemption

### S63 — Administrative Code Chapter 37A (official PDF, Rent Board document 901)
<https://www.sf.gov/sites/default/files/2022-09/901%20Rent%20Board%20Fee%20Ch.%2037A.pdf> — fetched 2026-11-11, both chunks.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | Sec. 37A.1: "This Chapter 37A is applicable to all residential units in the City and County of San Francisco, including residential units which are exempt from the rent increase limitation provisions (but not other provisions) of Chapter 37". Excluded: "(f) Any dwelling unit which is occupied by an owner of record on either a full-time or parttime basis and which is not rented at any time, provided that the owner file with the Rent Board an affidavit so stating". | FEE-01, FEE-13 | holds |
| 2 | Sec. 37A.4: "Fees shall be paid by March 1 of each year. The Rent Board shall add a 5% penalty to the amount of the fee if the fee has not been paid by March 1, an additional 5% if the fee has not been paid by April 1, and an additional 5% if the fee has not been paid by May 1. If the fee remains outstanding as of June 1, the Rent Board shall refer the matter to the Bureau of Delinquent" Revenue. | FEE-07, FEE-08, F38 | holds |
| 3 | Sec. 37A.6: "An owner who has paid the fee in full may seek recovery of the fee (exclusive of any penalties …) from the tenant(s) in occupancy of each residential unit on November 1, up to a maximum of 50% of the annual fee for each unit". | FEE-16 | holds |
| 4 | Sec. 37A.6(b): "Only those fees that become due after July 25, 1999 (the effective date of Ordinance No. 178-99) may be banked." | FEE-18 | holds |
| 5 | Sec. 37A.6(d): "The owner remains liable for full payment of the fee to the Rent Board whether or not the owner seeks any recovery". | FEE rows | holds |

### S29 — Rent Board Monthly Workload Statistics, June 2024
<https://www.sf.gov/file/workload-stats-june-2024pdf> — fetched 2026-11-11, whole document.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | Landlord Petitions Filed: "Capital Improvements 18 / 148"; "Operating and Maintenance 0 / 0"; "Comparable Rent 0 / 0"; "Costa-Hawkins &/or §6.14 1 / 1"; "SUBTOTAL: 19 / 149"; "TOTAL LL PETITIONS: 23 / 154". | IND-03, IND rows | holds for the row (18 / 148) |
| 2 | "TOTAL TT PETITIONS: 73 / 73"; "TOTAL Notices Received = 89". | IND rows | holds |
| 3 | The source list entry for S29 still reads "19 capital-improvement/148 units". | S29 statement | correction (item C3): the document says 18 petitions / 148 units; 19 is the subtotal that includes one Costa-Hawkins petition |

### S60 — Partial exemption for certain single-family homes and condominiums
<https://www.sf.gov/information--partial-exemption-certain-single-family-homes-and-condominiums-under-costa-hawkins> — fetched 2026-11-11, whole page.

| # | Quote | Rows | Result |
| --- | --- | --- | --- |
| 1 | "single-family homes and condominiums are generally exempt from the rent increase limitations (but not the just cause eviction provisions) of the Rent Ordinance, but ONLY IF the tenancy commenced on or after January 1, 1996." | Q-20, F35 | holds |
| 2 | "A single-family dwelling with a legal in-law unit constitutes a two-unit building and is not exempt from the Ordinance. A single-family dwelling with an illegal in-law unit also constitutes a two-unit building and is not exempt, unless both units are rented together as a single tenancy." | Q-20, F35, CHK-01 | holds |
| 3 | "Units exempted from rent control limitations by Costa-Hawkins are still subject to the Rent Ordinance for all other purposes, including the just-cause eviction regulations and payment of the annual Rent Board fee." | FEE-01 | holds |

## What this session did not open today

These published sources were **not** re-opened by this session on 2026-11-11, so this ledger says nothing about them and their rows keep the dates of the earlier checks: S09 to S15, S17 to S20, S22 to S24, S26, S28, S30 to S34, S37, S39, S40, S43 to S47, S50 to S52, S55 (the Portal needs an owner login), S59, S61, S64, S65, S66 to S70, S72 (same page as S01, whose notice was read), S74, S75, S78 to S82. Other sessions' records for today (`research/t49_audit/`, `research/t50_reverify/`, `research/t52_audit/`) cover some of them; those records are theirs, not this session's.

## Result count

`python3 research/ea4_2026-11-11/checks.py` recounts the table rows in this file by result and prints the totals; the totals are not typed by hand here.
