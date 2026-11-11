# EA4-V — corrections and additions found on 2026-11-11

Session `arena-ea4a9203`. Each item comes from an official page this session opened on 2026-11-11; the quotes are in `VERIFICATION_LEDGER.md`. Items are applied to the site only through the generator (`scripts/site_*.py`) during the integration task EA4-I. Nothing in `pages/` or `data/` is edited by hand.

Status of each item is given in the last column: `to apply` (will be changed at integration), `flag only` (published as a review flag, because the official page itself is inconsistent), `record` (kept in this file only).

## C — the site says something the official text does not support

| ID | Where | Site now | Official text read today | Action |
| --- | --- | --- | --- | --- |
| C1 | Flag F47; rows RATE-15, RATE-16, RATE-18 | "No official page states … how the 10% is measured". "Nothing official says how a notice served between 9/15/2026 and enactment would be treated." The words "temporarily" and "for the next three years" are recorded as an inconsistency. | The Legislative Digest and the ordinance text attached to the same Legistar record give all three. Measure: "10% of the lowest base rent that was in effect during the previous 12 months". Reach: banked increases "based on rent increase notices that landlords provided to their tenants on or after September 15, 2026". Duration: "until December 31, 2029"; the excess may be imposed "on or after January 1, 2030". The cap names banked and capital-improvement increases, not the ordinary annual increase. | to apply. Fill the three rows from the digest, add the digest and the ordinance text as sources, and keep "not law; may be amended" in every row. |
| C2 | Row CHK-14 note; row ST-13 note | "subsection (g) addresses lawful cause" | Civil Code 1942.5 **(f)** keeps the landlord's right to act "for any lawful cause". **(g)** is a different rule: the act is allowed if the notice "states the ground upon which the lessor, in good faith, seeks to … increase rent", and the landlord must prove it if challenged. | to apply. Name (f) and (g) correctly. |
| C3 | Source list entry S29 | "19 capital-improvement/148 units" | "Capital Improvements 18 / 148"; the "19 / 149" line is the subtotal that includes one Costa-Hawkins petition. Row IND-03 already says 18 / 148. | to apply. Correct the source statement. |
| C4 | Rows REQ-19, REQ-20, REQ-24 | "PRs #1 through #13 merged"; "Read from the GitHub Pages build API on 2026-11-08"; "Done 2026-11-08" | The repository now has merged pull requests up to #42 and the checks were repeated today. | to apply. Replace fixed counts and dates with wording that stays true, and point to `COORDINATION.md`. |

## D — only a date is out of date

| ID | Where | Site now | Read today | Action |
| --- | --- | --- | --- | --- |
| D1 | Row AN-04; source S42 | "Current eCFR as of 11/04/2026" | The eCFR page displayed "up to date as of 11/09/2026"; the rule text is the same. | to apply |
| D2 | Row LIC-01 | "official pages re-fetched 2026-11-07" | Same wording found today on S01 and S07. | to apply |
| D3 | Rates page description; rows RATE-14, RATE-17 | "2026-11-10" | Legistar record and both rate pages read again today; nothing changed. | to apply |
| D4 | Rows MKT-01, MKT-06, FED-05 | "2026-11-06" | The HUD pages were **not** opened by this session today. | record. The dates stay as they are, because they are the dates of the last real check. |

## A — official content that helps the owner and is not on the site yet

| ID | Official text | Why it matters | Action |
| --- | --- | --- | --- |
| A1 | The Rent Board's change-of-anniversary example (S01) and Rule 4.12(a) (S77). | On the supplied dates, Unit 1's skipped 1.4% becomes a banked increase on February 1, 2027. An increase taking effect earlier is 1.6% only and loses the 1.4% for good. See `CASE_TIMING_ANALYSIS.md`. | to apply, as `analysis` rows with a new review flag. Never as a verified fact about the case. |
| A2 | "A landlord does not have to impose the maximum allowed increase." "If only part of the allowable increase is used, the rest is banked. The remaining portion may be imposed at a later time, after at least 12 months have passed, or on a future anniversary date." (S05) | A banked amount can be taken in steps. Taking only the annual 1.6% now does not give up a properly banked amount. | to apply |
| A3 | Rule 4.12(b): the landlord states "which portion of the rent increase reflects banked amount, and (2) the dates upon which said banked amount is based". | The notice checklist says to state the banked part. It should also say to state the dates. | to apply |
| A4 | Civil Code 1942.5(g) (quoted in C2). | A reason to write the ground of the increase on the notice ("annual allowable increase under the San Francisco Rent Ordinance"). | to apply, as a cautious practice, not as a legal requirement. |
| A5 | IRT: the published percentages are for leases "for a term of 9-14 months"; for all leases the Q4 2025 figures were (6.2)%, 3.0% and (1.0)%. Invitation Homes: "the leases typically have a term of one to two years"; rent is compared "from an expiring lease to the monthly rent from the next lease". | Explains in one line how large landlords raise rent: at each lease renewal, not during the lease. Also states which measure the published numbers are. | to apply |
| A6 | The Rent Board page says "Banking only applies to fees assessed from November 1999 on"; Chapter 37A says "Only those fees that become due after July 25, 1999 … may be banked." | Row FEE-18 gives only the ordinance date. Both wordings are official. | to apply. Show both. |
| A7 | Rule 4.12(a) "A full 12 months must have elapsed from the date that an annual rent increase … could have been imposed" and S05 "at least 24 full months pass without any rent increase". | Flags F03 and B87-F03 call "12 months" against "24 months" an inconsistency. In the Rent Board's example they give the same date: the increase can first be imposed 12 months after move-in and is banked 12 months after that. | to apply. Keep both flags and add this explanation. |
| A8 | "Section 6.14 provides for an unlimited rent increase on remaining occupants when the last original occupant vacates the unit" (S16). | On the supplied facts one original Unit 1 tenant still lives there, so this condition is not met. | to apply, as a note on the existing flagged rows. |

## N — the official page itself is inconsistent (new today)

These are published as review flags. The site does not "fix" an official page by guessing.

| ID | Page | What is inconsistent | Effect on the site |
| --- | --- | --- | --- |
| N1 | S01, change-of-anniversary example | The text says 12 full months elapsed "since the skipped rent increase first became available (June 1, 2023 – June 1, 2024)". In the example the increase first became available on June 1, 2024. The text also says "the annual allowable increase in effect on June 1, 2026 (1.6%)" although the increase in the example is on May 1, 2026. | None on the arithmetic: both dates fall in the same 1.6% period and the result ($1,033.00) is consistent. flag only. |
| N2 | S54, annual increase for multiple years | The page gives only "30-days notice … (or 35-days if sent by mail)" and never mentions the 90-day rule, although its own method can produce a total above 10%. It also links the 24-25 edition of Form 571. | The 90-day rule is on S01, S05 and in Civil Code 827(b)(3), which control. flag only. |

Official-page defects already published and still present today: F01, F02, F04, F16, F24, F32, F38, F45.

Not published: a link on the Housing Inventory page (S07) that this session noted as possibly mislabelled. It was seen once and not checked a second time, so it is recorded here only.

## P — privacy

| ID | Finding | Action |
| --- | --- | --- |
| P1 | The public file `scripts/validate_site.py` contains values from which the tenants' real initials can be worked out in well under a second. See `PRIVACY_FINDING.md`. | to apply. Remove the values, replace the check, and tell the owner what only the owner can do about the history. |

## R — repository records

| ID | Finding | Action |
| --- | --- | --- |
| R1 | `COORDINATION.md` has no merge record for pull request #34 (merged 2026-11-10T01:15:25Z, merge commit `89c7bb9930350565babf986007740bd8046b8ee4`). | to apply |
| R2 | The results of pull requests #29 and #32 are not recorded on `main`. | to apply |
| R3 | The header of `COORDINATION.md` is out of date, and the file has a damaged passage near line 276 and repeated sections. | record. Rewriting other sessions' entries is outside this session's scope; a short dated note is added instead. |
| R4 | Three old pull requests (#18, #19, #25) are still open and cannot be merged cleanly. | See `UNMERGED_WORK_REVIEW.md`. |
