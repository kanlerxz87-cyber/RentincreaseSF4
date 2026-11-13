"""Suggestions and review catalogue.

Every entry is a *proposal* about how this research site could be improved to
support better decision making. Nothing here is a legal finding and nothing
here is applied automatically: each row carries a Decision cell that starts at
"Review" so a reviewer can accept, reject or defer before any change is built.

Rows whose proposal is grounded in an official rule carry that rule's official
source link(s). Rows that are purely internal site-design proposals carry the
explicit marker INTERNAL_MARKER instead, so no official source is ever
invented merely to satisfy a "every row has a link" rule.
"""

INTERNAL_MARKER = "Internal site-design proposal"

DECISION_DEFAULT = "Review"

SUGGESTION_COLUMNS = [
    "ID / suggestion",
    "What changes",
    "Effort",
    "Impact",
    "Official basis",
    "Decision",
]

# ---------------------------------------------------------------- category 1
# Compliance gates - make the legally required order of operations impossible
# to miss in the dashboard.
GATES = [
    {
        "id": "SUG-01",
        "title": "License-status gate per unit",
        "proposal": "Add a per-unit row on the Anonymized Case page and on the Notice Checklist: 'Rent Increase License status for this unit, confirmed on (date), portal reference (optional)'. Leave it blank and flag it until the owner fills in a real date.",
        "why": "The license is the one precondition that can void an otherwise lawful increase, and the rule tests the *effective date* of the increase, not the date the notice was served. A dated status field turns an invisible dependency into a visible gate.",
        "basis": 'Rule 13.14: a rent increase purporting to be effective while the landlord is unlicensed renders the entire increase null and void, and the effective date - not the date of service - is the test. SF.gov: a landlord must have a current rent increase license on file before any annual or banked increase can go into effect.',
        "effort": "Low",
        "impact": "High",
        "source_ids": ["S07", "S73", "S53", "S08"],
    },
    {
        "id": "SUG-02",
        "title": "Housing Inventory filing tracker",
        "proposal": "Add a per-unit filing row: 'Housing Inventory submitted for reporting year (YYYY) on (date)'. Show the recurring March 1 deadline and the rule that units in buildings with fewer than 10 residential units have reported since March 1, 2023.",
        "why": "The rent increase license is generated from the Housing Inventory submission, so the filing is the upstream cause of every license gap. Tracking it removes the most common way a license goes missing.",
        "basis": 'SF.gov: all owners of residential property are required to report into the Housing Inventory by March 1 every year; reporting began March 1, 2023 for condominiums and units in buildings with fewer than 10 residential units; the license is generated from the report.',
        "effort": "Low",
        "impact": "High",
        "source_ids": ["S07", "S53", "S55"],
    },
    {
        "id": "SUG-03",
        "title": "Rent Board Fee calendar with the tenant-recovery switch",
        "proposal": "Add a fee timeline to the Rent Board Fee page (October informational notice, December exemption window, January invoice, March 1 due date, 5% monthly late penalties capped at 15%, June 1 referral) plus one yes/no field per unit: 'Was the tenant in occupancy on November 1 of the applicable tax year?' That answer alone should decide whether the 50% recovery may be charged.",
        "why": "The fee is a separate money decision from the rent increase, it has its own penalty ladder, and the right to recover half of it turns on a single November 1 occupancy test. Treating it as a calendar plus a switch removes a recurring source of error.",
        "basis": 'SF.gov Rent Board Fee page: $59.00 per dwelling unit for 2026-2027, due March 1, 5% late penalty each month capped at 15%, referral to the Bureau of Delinquent Revenue after June 1, exemption request deadline December 14, 2026. 50% may be recovered only from tenants in occupancy on November 1 of the applicable tax year.',
        "effort": "Low",
        "impact": "Medium",
        "source_ids": ["S56", "S62", "S65"],
    },
    {
        "id": "SUG-04",
        "title": "Effective-date rate engine",
        "proposal": "Add a small calculator that takes the anniversary date and the intended effective date, then selects the published rate for the period that contains the effective date from the Current Rates ledger instead of letting a reader pick a rate from a list.",
        "why": "The rate in effect on the effective date controls, not the rate in effect when the notice is written, and the currently published 1.6% rate covers only March 1, 2026 through February 28, 2027. A date-driven selector prevents picking the wrong period.",
        "basis": 'SF.gov: the percentage is the one in effect on the date the increase takes effect; 1.6% applies to increases effective March 1, 2026 through February 28, 2027, and Section 37.3 caps the increase at 7% of CPI.',
        "effort": "Medium",
        "impact": "High",
        "source_ids": ["S01", "S02", "S04", "S21"],
    },
    {
        "id": "SUG-05",
        "title": "Banked-increase ledger per unit",
        "proposal": "Add a per-unit table that logs every increase the owner could have taken and did not take: the year, the anniversary date, the published percentage at that time, and whether 24 full months elapsed without any increase. Show the running banked total and the notice wording that must state the banked portion.",
        "why": "Banking requires the 24-full-month test for each skipped year, forbids compounding and prorating, and never carries to a new tenant. It is the hardest part of the calculation to hold in memory and the easiest to misstate in a notice.",
        "basis": 'SF.gov: a skipped increase is banked only if at least 24 full months pass without any increase; banked percentages are added, never compounded or prorated, and the notice must state the banked portion.',
        "effort": "Medium",
        "impact": "High",
        "source_ids": ["S05", "S54", "S77"],
    },
    {
        "id": "SUG-06",
        "title": "Pending-legislation watch row",
        "proposal": "Add a dated row to the Rates page that records the status of File 261020 and any successor, labelled 'proposed - not enacted', and never feeds it into a calculation. Re-check it at each review cycle.",
        "why": "A notice about a proposed 10% cap was posted on the Rent Board's own rent-increase and Current Rates pages on November 9, 2026. Because it appears on live official pages, there is a real risk of reading it as current law.",
        "basis": 'SF.gov notice posted November 9, 2026 on the rent-increase page and the Current Rates page, and Board of Supervisors File 261020 in Legistar: the 10% combined banked and capital-improvement cap is proposed, not enacted, and subject to change.',
        "effort": "Low",
        "impact": "Medium",
        "source_ids": ["S71", "S72", "S87"],
    },
    {
        "id": "SUG-07",
        "title": "Retaliation-window screen",
        "proposal": "Add a short screening block that must be answered before any notice is dated: 'In the last 12 months, has any tenant complained to an agency or exercised a right under the tenant chapter?', with a note of the answer and the date checked.",
        "why": "A rent increase that follows a protected complaint or act can be challenged as retaliation within the statutory window, independently of whether the increase amount itself is permitted. The bar is time-based and easy to miss on a case that has had a repair or complaint history.",
        "basis": 'California Civil Code 1942.5(a): a landlord may not retaliate against a lessee who has exercised rights under the chapter or complained to an agency within 12 months of the complaint; Section 37.10B separately prohibits bad-faith harassment.',
        "effort": "Low",
        "impact": "High",
        "source_ids": ["S57", "S22"],
    },
    {
        "id": "SUG-08",
        "title": "Uniform-criteria record for the one-unit-or-both decision",
        "proposal": "Add a field that records the single neutral eligibility criterion applied to each unit (for example: the unit's anniversary date has passed), the date each anniversary passed, and the owner-entered reason if only one unit is raised.",
        "why": "No official rule requires raising both units. What a reviewer would look for is a consistent, documented, non-pretextual reason applied the same way to both units, which is what the fair-housing rules ask when a neutral practice has a disparate effect.",
        "basis": '24 CFR 100.500: a practice with a disparate effect violates the Fair Housing Act unless it is supported by a substantial legitimate nondiscriminatory interest and no less discriminatory alternative is available. California Government Code 12955 and the California Civil Rights Department housing guidance add source-of-income and retaliation protections.',
        "effort": "Low",
        "impact": "High",
        "source_ids": ["S42", "S41", "S38", "S39"],
    },
    {
        "id": "SUG-09",
        "title": "Roommate and 6.14 fact screen",
        "proposal": "Add a structured, mostly blank questionnaire for each unit: who was the last original occupant, the date occupancy began, whether a 6.14 notice was ever served and when, and whether any occupant is a subtenant or a co-tenant.",
        "why": "A market-rate reset on remaining occupants turns on the last original occupant, the date occupancy began and the 6.14 notice. Those are exactly the facts this case has not verified, and they decide whether an unlimited increase is even available.",
        "basis": 'SF.gov on Section 6.14 and Costa-Hawkins: an unlimited increase on remaining occupants requires that the last original occupant has vacated and that a proper 6.14 notice was served within a reasonable time; a co-tenant is not subject to such an increase.',
        "effort": "Low",
        "impact": "High",
        "source_ids": ["S16", "S01", "S37"],
    },
    {
        "id": "SUG-10",
        "title": "Coverage determination sheet per unit",
        "proposal": "Add a per-unit coverage row recording: pre-1979 construction confirmed (date checked), not a single-family dwelling, no new-construction partial exemption, no single-family/condominium partial exemption, and the Property Information Map link with the date it was checked.",
        "why": "If a unit is not covered by rent control the rent increase limitations do not apply to it and every other gate changes. This is the first gate and the one currently resting on an assumption rather than a record.",
        "basis": 'SF.gov: many units built on or before June 13, 1979 that are not single-family dwellings have rent control, and partial exemptions exist for newly constructed units and for certain single-family homes and condominiums; the Property Information Map is the official lookup.',
        "effort": "Low",
        "impact": "High",
        "source_ids": ["S06", "S32", "S59", "S60", "S08"],
    },
    {
        "id": "SUG-11",
        "title": "Notice assembly with required contents",
        "proposal": "Extend the Notice Worksheet so the assembled notice shows, in the notice itself, the dollar amount, the percentage, the effective date and any banked portion, and carries a delivery-method row (personal delivery or mail, with the 5-day extension) and a proof-of-service row.",
        "why": "Notice content and delivery method are the two steps most often defective, and both have fixed external requirements. Assembling the notice inside the tool means the checklist and the document cannot drift apart.",
        "basis": "California Civil Code 827: at least 30 days' notice where the increase is 10% or less and 90 days where it exceeds 10%, delivered personally or by mail, and the notice must state the amount of the increase and its effective date.",
        "effort": "Medium",
        "impact": "High",
        "source_ids": ["S35", "S78", "S01", "S26"],
    },
    {
        "id": "SUG-12",
        "title": "Petition routing table",
        "proposal": "Add a table that names the petition or worksheet required *before* a notice for each increase type (capital improvement, operating and maintenance, utility, comparable rent, and the passthrough petitions) and marks them explicitly 'not required for a plain annual or banked increase'.",
        "why": "Each petition category has its own pre-notice filing rule, and the filing for one type is not a substitute for another. A routing table stops the wrong petition from being filed, or none being filed when one is required.",
        "basis": 'SF.gov: capital improvement, operating and maintenance, utility, comparable-rent and passthrough increases each have their own petition or worksheet rules that apply before the increase is noticed; no petition is required for a plain annual or banked increase.',
        "effort": "Low",
        "impact": "Medium",
        "source_ids": ["S09", "S10", "S11", "S12", "S13", "S14", "S77"],
    },
]

# ---------------------------------------------------------------- category 2
# Evidence, defensibility and disclosure - make the record reviewable.
EVIDENCE = [
    {
        "id": "SUG-13",
        "title": "Case-file completeness checklist",
        "proposal": "Add a checklist of the documents an owner should be able to produce for each unit: the current lease, every prior increase notice, proof of service for each notice, the license status record, the Housing Inventory submission receipt, the Rent Board Fee payment receipt, the Property Information Map printout, and the rate sheet actually used for the calculation.",
        "why": "An unlawful-increase petition is decided on a documentary record. Missing documents, not wrong amounts, are how an otherwise compliant increase fails review.",
        "basis": 'California Civil Code 827 and Code of Civil Procedure 1013 govern notice and service by mail; the Housing Inventory submission, the portal license record, the fee payment and the Property Information Map are the official records the owner already has to create.',
        "effort": "Low",
        "impact": "Medium",
        "source_ids": ["S35", "S78", "S07", "S55", "S56", "S32", "S02"],
    },
    {
        "id": "SUG-14",
        "title": "Tenant-side challenge walkthrough",
        "proposal": "Add a page that follows the exact path a tenant can take - search the Rent Board Portal for the landlord's license status, file the Tenant Petition and Form C at no charge and with no time limit, attend a hearing before an Administrative Law Judge - and lists what a reviewer would check at each step.",
        "why": "The standard asked for is that an increase survives review by a San Francisco tenant-side lawyer. No official source offers pre-approval, so the closest available substitute is to run the challenge yourself before serving. The Rent Board states the process is designed so that no one needs an attorney.",
        "basis": "SF.gov: a tenant may file a Tenant Petition and Form C at no charge and with no time limit, and the matter is set for a hearing before a Rent Board Administrative Law Judge; the process is designed so that no one needs an attorney. A tenant may also search the portal for the landlord's license status.",
        "effort": "Medium",
        "impact": "High",
        "source_ids": ["S25", "S08", "S26", "S24"],
    },
    {
        "id": "SUG-15",
        "title": "Printable attorney-review handoff packet",
        "proposal": "Add a one-page printable case summary, anonymized with dates and amounts unchanged, that can be handed to a tenant-side or defense attorney: the unit facts, the proposed increase, every rule relied on with its official link, and a list of every item still blank or flagged.",
        "why": "Turning a dashboard into a document is what 'able to pass review' actually requires. Publishing the blanks in the packet rather than hiding them is what lets a reviewer judge the case rather than the presentation.",
        "basis": 'SF.gov tenant and landlord resources, the free Rent Board counselor service, the unlawful-rent-increase petition, 42 USC 3604 and 24 CFR 100.500 are the rules a reviewer would apply.',
        "effort": "Low",
        "impact": "High",
        "source_ids": ["S23", "S24", "S25", "S42", "S41"],
    },
    {
        "id": "SUG-16",
        "title": "Neutral-language bank for the increase letter",
        "proposal": "Add a short, sourced bank of neutral phrasings for the increase letter - stating the amount, percentage and effective date without characterising the tenants, their conduct, or their ability to pay - each tied to the rule it is designed to satisfy.",
        "why": "Bad-faith conduct is a separate exposure from the arithmetic of the increase, and Section 37.10B carries its own civil remedies. Language control is a cheap control that a reviewer can check on the face of the letter.",
        "basis": 'Section 37.10B prohibits bad-faith harassment of a tenant by a landlord and carries civil remedies; the published guidance is the official statement of the conduct that is prohibited.',
        "effort": "Medium",
        "impact": "Medium",
        "source_ids": ["S22", "S01"],
    },
    {
        "id": "SUG-17",
        "title": "Public-records disclosure note before filing",
        "proposal": "Add a note to the Housing Inventory steps that the information entered in the submission is public and may include the owner's name and business, contact information, approximate square footage, bedrooms, bathrooms and vacancy/occupancy history, with a checkbox confirming the owner has read it before filing.",
        "why": "The required filing publishes the owner's own identifying and business information. That is a real privacy consequence of the compliance step itself and belongs at the point of action, not buried on a research page.",
        "basis": 'SF.gov: the information entered in the Housing Inventory submission is public and may include name and business, contact information, approximate square footage, number of bedrooms and bathrooms, and vacancy or occupancy history for the past 12 months.',
        "effort": "Low",
        "impact": "Medium",
        "source_ids": ["S07", "S53"],
    },
]

# ---------------------------------------------------------------- category 3
# Missing information - what has to be discovered before a decision is sound.
MISSING = [
    {
        "id": "SUG-18",
        "title": "Missing-information register",
        "proposal": "Add one page that lists every open question in this case with five columns: what is missing, which official source would resolve it, how to obtain it, who must supply it, and which decision it blocks. Populate it from the existing needs-review rows so nothing stays only on the Flagged for Review page.",
        "why": "Every unresolved item currently appears as a blank cell on several pages. A single register turns a scatter of blanks into an ordered work plan, and it is the direct answer to what information has to exist before a decision can reasonably be made.",
        "basis": 'The official routes that would resolve the open items are the portal and Housing Inventory pages, the Property Information Map, the Section 6.14 guidance, the counsel line and the Tenant Petition process.',
        "effort": "Medium",
        "impact": "High",
        "source_ids": ["S25", "S24", "S16", "S55", "S32", "S07"],
    },
    {
        "id": "SUG-19",
        "title": "Facts only the owner can obtain",
        "proposal": "Add a checklist of the case facts that no amount of outside research can supply: the last original occupant in each unit, the date occupancy began, whether a 6.14 notice was served, each unit's anniversary date, the full lease and notice history, square footage and bedroom/bathroom counts, whether either unit is an in-law unit, whether the owner occupies one unit, and whether each tenant was in occupancy on November 1 for the fee-recovery test.",
        "why": "Several of the blanks on this site are the owner's own facts, not public records. Naming them explicitly prevents them from being mistaken for research gaps that more research would close.",
        "basis": 'The Housing Inventory asks the owner for square footage, bedrooms, bathrooms, the date occupancy began and the base rent; the fee page turns on November 1 occupancy; the Section 6.14 page turns on the last original occupant and the date occupancy began. None of these are public records.',
        "effort": "Low",
        "impact": "High",
        "source_ids": ["S07", "S53", "S16", "S56", "S60", "S59"],
    },
    {
        "id": "SUG-20",
        "title": "Counsel call script for the unanswered questions",
        "proposal": "Add a printable call script containing only the specific open questions, with the Rent Board counselor's published phone number, office hours and the note that counseling is free, multilingual and cannot give legal advice.",
        "why": "Rent Board counseling is free and multilingual but explicitly will not give legal advice, and the published guidance tells callers to have their questions written down in advance. A prepared script converts a five-minute call into a usable answer.",
        "basis": 'SF.gov: counseling is free, available in Spanish, Cantonese and Mandarin with interpretation for other languages, is provided by phone Monday to Friday 9-12 and 1-4, and cannot give legal advice; the published guidance tells callers to have their questions written down first. Calls are generally limited to 5 minutes.',
        "effort": "Low",
        "impact": "High",
        "source_ids": ["S24", "S07", "S55", "S16"],
    },
    {
        "id": "SUG-21",
        "title": "Pre-decision gate sequence",
        "proposal": "Add a single 'can I proceed?' checklist at the top of the process page that must be fully answered before any notice is dated: coverage confirmed, Housing Inventory filed, license current on the effective date, no retaliation window open, rate selected for the effective date, banked total confirmed, notice period and method chosen, petition routed, uniform criterion recorded.",
        "why": "The rules are sequential and several of them are date-triggered. A single ordered gate list is what turns the site from a reference into something that can be worked through in order without missing a step.",
        "basis": 'The sequence is fixed by the official rules: coverage, Housing Inventory report, current license on the effective date, no open retaliation window, the rate for the effective date, the banked total, the notice period and delivery method, petition routing, and one consistent criterion applied to both units.',
        "effort": "Low",
        "impact": "High",
        "source_ids": ["S07", "S73", "S35", "S05", "S57", "S42", "S16", "S09"],
    },
]

# ---------------------------------------------------------------- category 4
# Internal site quality - proposals about this site, not about the law.
INTERNAL = [
    {
        "id": "SUG-22",
        "title": "Per-row verification date",
        "proposal": "Add a visible 'last verified' date to every published row and every official source, so a reader can tell which findings were re-checked most recently and which are inherited from an earlier pass.",
        "why": "Official pages change without notice - a proposed-cap notice appeared on two Rent Board pages on the same day. Showing the verification date makes the age of each figure visible instead of implied.",
        "basis": 'Internal site-design proposal about how this research site is maintained. The official pages themselves change - a proposed-cap notice was posted on two Rent Board pages on November 9, 2026 - so the age of each figure has to be visible rather than implied.',
        "effort": "Low",
        "impact": "High",
        "source_ids": ["S68"],
        "internal": True,
    },
    {
        "id": "SUG-23",
        "title": "Link and content monitor for the source ledger",
        "proposal": "Add a scheduled job that re-fetches every official URL in the ledger and reports any redirect, error or content change, and posts the result as a dated entry rather than editing a value silently.",
        "why": "The ledger already records several official URLs that changed or returned errors, and official pages disagree with each other on examples. An automated check would surface the next change before a reader relies on it, and it preserves the rule that a value is never changed without a note.",
        "basis": 'Internal site-design proposal about how this research site is maintained, using the repository and its GitHub Pages build API as the record. The ledger already records official URLs that changed or returned errors, so the next change should surface before a reader relies on it.',
        "effort": "Medium",
        "impact": "High",
        "source_ids": ["S68", "S69"],
        "internal": True,
    },
    {
        "id": "SUG-24",
        "title": "Unchanged-column consistency",
        "proposal": "Keep the current five-column table shape on every finding page and publish the Suggestions page and the missing-information register in the same shape, so a reviewer can read any page without relearning the layout.",
        "why": "A single consistent shape is what makes the site scannable. Suggestions and the missing-information register are new pages, and matching the existing shape keeps the dashboard coherent instead of becoming a second, differently-organised document.",
        "basis": 'Internal site-design proposal about how this research site is presented; the five-column shape already used on every finding page is the reference.',
        "effort": "Low",
        "impact": "Medium",
        "source_ids": ["S68"],
        "internal": True,
    },
    {
        "id": "SUG-25",
        "title": "Blank-means-unknown convention, stated once and repeated",
        "proposal": "Keep the existing convention that an empty cell means 'not officially confirmed' and never means zero or 'not applicable', and repeat the legend at the top of every page rather than only on the landing page.",
        "why": "A blank on this site is a deliberate statement that no official source confirms the value. If that is only explained on one page, a reader who lands on another page may read a blank as an answer.",
        "basis": "Internal site-design proposal about how this research site is presented. A blank on this site means no official source confirms the value, which is different from a zero or from 'not applicable'.",
        "effort": "Low",
        "impact": "Medium",
        "source_ids": ["S68"],
        "internal": True,
    },
    {
        "id": "SUG-26",
        "title": "Print and mobile review mode",
        "proposal": "Add a print stylesheet and a narrow-screen layout so the notice checklist, the worksheet and the case summary can be used on a phone at the property and printed for a file or for an attorney.",
        "why": "The deciding moments - checking a license status, serving a notice, assembling a file - happen away from a desk. A desktop-only dashboard is usable for research but not for the moment of action.",
        "basis": 'Internal site-design proposal about how this research site is presented on small screens and on paper.',
        "effort": "Low",
        "impact": "Medium",
        "source_ids": ["S68"],
        "internal": True,
    },
    {
        "id": "SUG-27",
        "title": "Review-cycle date on the landing page",
        "proposal": "Show one 'next review due' date on the landing page, set after each re-verification pass, together with the list of items that are most likely to have changed (the published rate period, the pending cap, the fee amount and the license rule).",
        "why": "The published rate is period-limited and the pending legislation can be enacted at any time. A single visible review date makes it obvious when the dashboard needs re-checking rather than assuming it is current.",
        "basis": 'The items most likely to change are the published rate period, the proposed cap in File 261020, the Rent Board Fee amount and the licensing rule - each of which has a published official source.',
        "effort": "Low",
        "impact": "Medium",
        "source_ids": ["S02", "S71", "S56", "S07", "S68"],
    },
]

SUGGESTION_SECTIONS = [
    {
        "title": "1. Compliance gates - make the required order of operations impossible to miss",
        "intro": "Each proposal below adds a gate that must be answered before a notice is dated. Every one is grounded in a rule published by the San Francisco Rent Board, the Rent Ordinance, California statute or federal regulation.",
        "rows": GATES,
    },
    {
        "title": "2. Evidence and defensibility - make the record reviewable",
        "intro": "These proposals build the paper trail a tenant-side reviewer would look for, and make the case exportable as a document rather than only as a web page.",
        "rows": EVIDENCE,
    },
    {
        "title": "3. Discovering the missing information",
        "intro": "The owner's standard is that a decision should rest on what is already known and what is not yet known. These proposals turn the open blanks into an ordered discovery plan, and separate the facts that only the owner can supply from the ones that a public record can answer.",
        "rows": MISSING,
    },
    {
        "title": "4. Internal site quality - proposals about this site",
        "intro": "These rows are about the research site itself rather than about the law. They carry no official legal basis and are labelled as internal site-design proposals; they are listed so the owner can accept, reject or defer them on their merits.",
        "rows": INTERNAL,
    },
]


def all_suggestions():
    rows = []
    for section in SUGGESTION_SECTIONS:
        rows.extend(section["rows"])
    return rows


def review_checklist():
    """One blank decision row per suggestion, for the reviewer to complete."""
    out = []
    for s in all_suggestions():
        out.append({
            "id": s["id"],
            "title": s["title"],
            "decision": "",
            "reviewer": "",
            "date": "",
            "note": "",
            "source_ids": s["source_ids"],
        })
    return out


REVIEW_COLUMNS = ["ID / suggestion", "Decision", "Reviewer", "Date", "Review note"]

REVIEW_TEXT = """## How to use this page

This page is a **catalogue of proposals**, not a set of changes. Nothing here has been
implemented, and every row starts at the decision value **Review**. Read the rows, then
fill in the **Review checklist** at the bottom of this page with Accept, Reject or Defer
for each item. Only the items marked Accept are candidates for implementation.

**How each row is sourced.** A row that improves the site because an official rule
requires something carries that rule's official source link. A row that is purely a
proposal about how this site should work carries the marker **Internal site-design
proposal** and no legal claim is made for it. No official source is cited merely to fill
a cell.

**What this page does not do.** It does not state that any rent increase is lawful,
approved or safe from challenge. It does not give legal advice. It does not decide
anything about the two units in this case; it proposes changes to the research site so
that the decision is better supported.

**Priority convention used below.** Effort is the build cost (Low / Medium / High).
Impact is the expected effect on the quality of the decision (High / Medium / Low).
Both are estimates about site work, not statements about law.
"""

REVIEW_CHECKLIST_TEXT = """One row per suggestion. The Decision, Reviewer, Date and Review note cells are
intentionally blank - they are the reviewer's to complete. A blank cell in this table
means "not yet decided", which is different from the blank cells on the finding pages,
where a blank means "no official source confirms the value".

Accept only the items you want built. Items marked Reject or Defer stay in the
catalogue with the decision recorded, so the reasoning survives.
"""
