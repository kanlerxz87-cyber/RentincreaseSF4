# Follow-up audit — November 7, 2026

## Verification scope and limitations

The inherited source ledger is dated November 6, 2026. Its historical verification notes are preserved, not represented as fresh checks of every external source today. This follow-up checked every generated table row for source-ID integrity, official-domain links, blank/flag conventions and local link resolution. These are structural checks, not proof that each linked page supports every interpretation. No claim of attorney approval is made. External links beyond the sources listed below have not all been freshly fetched in this follow-up; their current availability and legal currency remain for review.

## Fresh official-source checks

- [SF Rent Board: Learn about rent increases](https://www.sf.gov/learn-about-rent-increases-san-francisco), both returned chunks: confirms 1.6% March 1, 2026–February 28, 2027; license requirement; base-rent calculation; no rounding up; first increase after 12 months and subsequent anniversary rules; 30/90-day notice guidance and five extra days for mail; no surcharge merely for a roommate change. Its example incorrectly labels June 1, 2025 as 1.6%; existing flag F01 is retained. Follow the operative rate schedule, not that erroneous example.
- [SF Rent Board: Current Rates](https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit): independently confirms the 1.6%, 1.4%, and 1.7% annual schedules shown on the site.
- [SF Rent Board: AB 1482](https://www.sf.gov/reports--california-tenant-protection-act-2019-ab-1482), first returned chunk: confirms 8.8% August 1, 2026–July 31, 2027 for state-covered SF units, explicitly not a substitute for local rent-control limitations. The alternative information-- URL returns a not-found page; the site's reports-- source URL works.

## Case conclusion — conditional, not a notice to tenants

Using the owner's unverified base rents and the official 1.6% rate, the illustrative totals remain $4,058.92 for Unit 1 and $3,200.40 for Unit 2. These are arithmetic, not verified lawful rent determinations. The address, 1940 construction claim, coverage, license status, actual lawful base rent, prior increases and notice records are not independently confirmed. No banked total or effective increase date is inferred. An occupant change alone does not authorize a market reset.

A neutral annual policy is a conservative analytical recommendation, not an official finding of what is universally normal or fair. Raising both units does not itself eliminate discrimination or retaliation risk. An increase for either unit requires its own eligibility and service review. No free lawyer consultation or favorable tenant-lawyer review has been obtained. The evidence for corporate practices is portfolio-specific, not representative of Outer Sunset owners.

## Repository corrections

- Removed the privacy validator's dependency on an ignored intake file absent in clean checkouts. A one-way fingerprint regression test checks supplied identifiers without printing or storing the raw identifiers in public test output. This is a limited exact-pattern test, not a comprehensive anonymization certification.
- Replaced a blanket “Verified” date in page headers with “Research ledger dated.” Added this audit to every page footer.
- Corrected stale deployment flag F19: prior PR #1 already merged and its Pages build succeeded.
- All prior case-specific unknowns remain blank and flagged. Official rule links on those rows explain the governing rule; they do not authenticate private case facts.

## Publication evidence

Repository: https://github.com/kanlerxz87-cyber/RentincreaseSF4

Existing PR #1: https://github.com/kanlerxz87-cyber/RentincreaseSF4/pull/1

GitHub Pages API reported build 1346488563 as built for a0591c3 before this follow-up. The follow-up PR and resulting deployment are recorded in COORDINATION.md. The live site is https://kanlerxz87-cyber.github.io/RentincreaseSF4/ .
