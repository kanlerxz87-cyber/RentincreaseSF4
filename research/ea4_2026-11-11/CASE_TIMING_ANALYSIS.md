# EA4-V — what the effective date does to each unit (2026-11-11)

**This is conditional arithmetic, not an official finding and not legal advice.** It applies the Rent Board's own published examples to the owner-supplied dates and rents. Every line depends on facts the owner has not supplied (see "What has to be confirmed first"). On the site it is published only with the status `analysis` and a review flag.

The arithmetic is checked by `python3 research/ea4_2026-11-11/checks.py`, which first reproduces both official Rent Board examples and then applies the same method here.

## The official rule

All quotes were read on the official pages on 2026-11-11 (see `VERIFICATION_LEDGER.md`, sources S01, S05 and S77).

- The first increase can be given 12 months after the tenancy began. The date an increase takes effect becomes the anniversary date.
- "A skipped increase is only banked if at least 24 full months pass without any rent increase. If less than 24 months pass, the skipped increase is lost and cannot be imposed at a later date." (S05)
- Rule 4.12(a): "A full 12 months must have elapsed from the date that an annual rent increase, or a portion thereof, could have been imposed before this banking section becomes applicable." (S77)
- The Rent Board's example (S01): a tenant moved in on June 1, 2023. The landlord gives the first increase on May 1, 2026 instead of June 1, 2026. The 1.4% that first became available on June 1, 2025 is not banked "because a full 12 months has not elapsed between the date it first became available on June 1, 2025, and the date of the rent increase on May 1, 2026". "The 1.4% rent increase is permanently lost due to the change in anniversary date".
- "Once an increase is properly banked, it does not expire." "If only part of the allowable increase is used, the rest is banked." (S05)
- "Many owners give annual and banked rent increases on the same date each year to avoid possible issues." (S01)

## Unit 1 — $3,995, lease start February 1, 2025

The first increase became available on February 1, 2026. The rate in effect on that day was 1.4%. It was not used, on the supplied facts. It becomes a banked increase only if no increase takes effect before February 1, 2027.

| If the increase takes effect | Allowed by the official method | Monthly increase | New base rent | What happens to the skipped 1.4% |
| --- | --- | --- | --- | --- |
| Before February 1, 2027 | 1.6% | $63.92 | $4,058.92 | Lost for good ($55.93 a month). The anniversary date moves to the new date. |
| February 1 to February 28, 2027 | 1.4% banked + 1.6% annual = 3.0% | $119.85 | $4,114.85 | Used. |
| March 1, 2027 or later | 1.4% banked + the 2027-28 rate | not yet known | not yet known | Used. The 2027-28 rate is not published yet. |

This table is right only if **both** of these are true:

1. The tenancy that began on February 1, 2025 is still the same tenancy. The owner also gave April 1, 2026 as a "current tenancy date" with one original tenant (Tenant A) and one new person (Tenant D). If April 1, 2026 started a **new** tenancy, no increase is allowed before April 1, 2027, nothing is banked, and an increase in February 2027 would be too early.
2. The rent has not been raised since February 1, 2025.

No official page opened today says whether a new lease signed with a continuing original tenant restarts the 12 months. That is the first question to ask a Rent Board counselor (415-252-4600) before choosing a date for Unit 1.

## Unit 2 — $3,150, lease start June 1, 2019

If the rent has never been raised, six yearly increases are banked (those that first became available each June 1 from 2020 to 2025): 1.8 + 0.7 + 2.3 + 3.6 + 1.7 + 1.4 = 11.5%. Properly banked increases do not expire. The owner does not have to use all of it.

For an increase taking effect on or before February 28, 2027 (while 1.6% is the annual rate):

| Choice | Percent | Monthly increase | New base rent | Notice | Banked percent left |
| --- | --- | --- | --- | --- | --- |
| Annual increase only | 1.6% | $50.40 | $3,200.40 | 30 days | 11.5% |
| Annual plus part of the banked amount, 10.0% in total | 10.0% | $315.00 | $3,465.00 | 30 days (the increase is "10 percent or less") | 3.1% |
| Annual plus all of the banked amount | 13.1% | $412.65 | $3,562.65 | 90 days (more than 10%) | 0% |

Two points about the dates for Unit 2:

- The anniversary date on the supplied facts is June 1. An increase taking effect on any other date moves the anniversary date to that date. It also means the increase that first became available on June 1, 2026 (1.6%) is not banked; it is replaced by the annual rate in effect on the new date. Through February 28, 2027 that rate is the same 1.6%, so the total is 13.1% either way.
- Waiting until June 1, 2027 keeps the June 1 anniversary. The banked total would then be 13.1%, plus the 2027-28 annual rate, which is not published yet.

## Latest notice dates

These are simple day counts back from the effective date. They are the last possible days, not target days. Serve earlier. A mailed notice needs 5 more days.

| Increase takes effect | Notice needed | Handed to the tenant by | Mailed by |
| --- | --- | --- | --- |
| February 1, 2027 | 30 days (10% or less) | January 2, 2027 | December 28, 2026 |
| February 28, 2027 | 30 days (10% or less) | January 29, 2027 | January 24, 2027 |
| February 1, 2027 | 90 days (more than 10%) | November 3, 2026 — already past | October 29, 2026 — already past |
| February 28, 2027 | 90 days (more than 10%) | November 30, 2026 | November 25, 2026 |

So an increase of more than 10% can no longer take effect on February 1, 2027. With a notice handed over today or later, the earliest effective date for an increase above 10% is 90 days after delivery.

The Rent Increase License must be on file on the day the increase takes effect (Rule 13.14, source S73). Reporting both units in the Housing Inventory before serving any notice is the cautious order.

## What the pending File No. 261020 would change

File No. 261020 is **not law**. On 2026-11-11 its status was "Pending Committee Action" (source S71). As introduced it would:

- cap banked and capital-improvement increases at "10% of the lowest base rent that was in effect during the previous 12 months";
- apply to banked increases "based on rent increase notices that landlords provided to their tenants on or after September 15, 2026";
- stay in effect until December 31, 2029, with the excess imposable "on or after January 1, 2030".

The proposed cap names banked increases and capital-improvement increases. It does not name the ordinary annual increase.

If it passed exactly as introduced:

| Unit | Effect |
| --- | --- |
| Unit 1 | None on the figures above. The banked part is 1.4%. |
| Unit 2, annual only (1.6%) | None. |
| Unit 2, 10.0% in total | None. The banked part is 8.4%, which is under 10%. |
| Unit 2, 13.1% in total | The banked part (11.5%, $362.25) would be cut to $315.00. The most allowed would be $315.00 + $50.40 = $365.40, for a base rent of $3,515.40. The other $47.25 could not be charged before January 1, 2030. |

Because the proposal reaches back to notices given on or after September 15, 2026, a notice served now for the full 13.1% could be cut back later if the proposal is enacted as written. The text can still change.

## What has to be confirmed first

1. Both units are reported in the Housing Inventory and a Rent Increase License is on file for the effective date (rows CASE-06, CASE-V3).
2. Whether Unit 1's tenancy dates from February 1, 2025 or April 1, 2026 (rows CASE-12, CASE-V6).
3. Whether any rent increase was ever given to either unit, and Unit 2's current rent (rows CASE-07, CASE-17, CASE-V4, CASE-V9).
4. That each lease is month-to-month or otherwise allows an increase on the chosen date (flag B87-F07).
5. That the building is covered by the Rent Ordinance (rows CASE-V1, CASE-V2).

## What this file does not say

It does not say which choice the owner should make. It does not say an increase would survive a tenant petition. It does not predict the 2027-28 rate or the fate of File No. 261020.
