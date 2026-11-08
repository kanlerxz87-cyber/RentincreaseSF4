# B87 annual rent-increase notice kit

Session `arena-b87bd80b`, fixed branch `arena/b87bd80b-rentincreasesf4`. Research date: **2026-11-08 UTC**. This is an additive, official-source-linked worksheet and service-record kit. It does **not** replace the existing dashboard, determine that either unit is eligible for an increase, or authorize service of a notice.

## Direct answer for an individual owner

For a unit covered by San Francisco rent control, an individual (noncorporate) owner must report the unit into the Rent Board Housing Inventory and have a current Rent Increase License for an annual or banked increase. The license is generated from the inventory reporting; it is not a corporation-only requirement. A plain annual or banked increase does not require a Rent Board petition. The Rent Board Fee and business registration are separate obligations.

Official sources: [SF Rent Board increase guidance](https://www.sf.gov/learn-about-rent-increases-san-francisco), [Housing Inventory](https://www.sf.gov/rent-board-housing-inventory), [Rule 13.14](https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-xiii-reporting-obligations-under-rent), [Form 571](https://media.api.sf.gov/documents/571_Allowable_Annual_Increases_26-27_1.pdf), [Rent Board Fee](https://www.sf.gov/rent-board-fee).

**Timing nuance:** Rule 13.14 tests whether the landlord is licensed on the **effective date** of the increase, not the service date. This kit conservatively recommends completing reporting and confirming the license before serving notice, but does not misstate that rule as a service-date license requirement.

## Files

- `NOTICE_WORKSHEET.md` — pre-service gates, required notice contents, owner-supplied inputs kept separate from official verification, and conditional arithmetic.
- `SERVICE_RECORD.md` — personal-delivery / California-mail checklist and placeholder tenant service log.
- `VERIFICATION.md` — fresh official-source fetch ledger, exact short quotes, chunk results and dead ends.
- `FLAGGED.md` — B87-namespaced review items for integration into the shared Flagged for Review page.
- `worksheet.json` — integration-ready rows, sources and flags; no raw tenant identifiers.
- `validate_kit.py` — scoped structural, source-link, blank/flag, privacy and arithmetic checks.

## Use and limits

1. Treat every blank unit-specific cell as **needs review**, not as zero, no, or permission to proceed.
2. Verify coverage, lawful base rent, anniversary, prior increases, lease term, license status, banking, petition/passthrough history, subsidy status and retaliation/repair issues from private records and official portals before assembling a notice.
3. The owner-supplied dates and amounts are preserved exactly, but they are not government-verified lawful base rents or anniversary dates.
4. The conditional 1.6% arithmetic is not a recommended increase, a banking calculation, or a finding of eligibility.
5. No attorney has approved this kit. No guarantee is made that a tenant, tenant lawyer, Rent Board or court will accept any increase.

## Privacy

Only placeholders Tenant A–F are used. No raw names, initials, contact details or exact street address are written here. Historical public Git exposure is a separate unresolved issue recorded in `research/privacy/HISTORY_EXPOSURE.md` and shared flag F44; current-tree anonymization is not a history purge.

## Integration request

Shared scripts, data, navigation and generated pages are owned by active integration sessions. B87 requests that the final integrator, after those tasks finish, add this kit as a categorized subpage and merge the B87 flags into the shared Flagged for Review page using `worksheet.json`. B87 does not edit those shared files while the claims are live.
