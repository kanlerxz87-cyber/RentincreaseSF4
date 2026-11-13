"""Suggestions contributed by session `arena-87a91aec` (T54), 2026-11-13.

A concurrent session (`arena-415e54ea`, PRs #51 and #53) independently published a
Suggestions review queue and a Decision Readiness page while this session was
working. Both are kept: the concurrent session's queue (`SUG-P*`, `SUG-A*`,
`SUG-B*`, `SUG-C*`) remains the first content on the page, and the proposals in
this module are appended as further groups (`SUG-D*` to `SUG-G*`) so nothing from
either session is lost and nothing is duplicated.

Rows use the same schema as the page: `label` is the suggestion, `value` is what
changes and why it helps, `notes` carries the official basis and any
cross-reference, `effort` is the build cost and `review_status` is the decision
state. Every row starts at "Review" - nothing here is pre-approved.

Rows that are purely proposals about how this site should work carry the exact
marker INTERNAL_MARKER in `notes` and no legal claim is made for them; the
validator enforces that a marked row carries the marker and an unmarked row does
not.
"""

INTERNAL_MARKER = "Internal site-design proposal"

REVIEW_STATUS_DEFAULT = "Review"

# The review-status values allowed on the page. "open for review" is the value
# used by the concurrent session's group A rows; "Review" is this session's.
REVIEW_STATUS_VALUES = ("open for review", "Review")


def sug(sid, title, value, source_ids, effort, notes="", review_status=REVIEW_STATUS_DEFAULT):
    """A suggestion row in the page's schema."""
    return {"id": sid, "label": title, "value": value, "status": "analysis",
            "source_ids": list(source_ids), "effort": effort, "review_status": review_status,
            "notes": notes, "flag_id": "", "source_note": ""}


def _row(sid, title, proposal, why, basis, source_ids, effort, impact, notes="", internal=False):
    """Build a row: what changes, why it helps, the official basis, effort and impact."""
    full_notes = basis
    if internal:
        full_notes = "{} - no official rule applies; proposal about this site. {}".format(INTERNAL_MARKER, full_notes)
    if notes:
        full_notes = "{} {}".format(full_notes, notes)
    value = "What changes: {} Why it helps the decision: {}".format(proposal, why)
    return sug(sid, title, value, source_ids,
               "{} build, {} impact".format(effort, impact),
               notes=full_notes)


# ------------------------------------------------------------------ group D
# Compliance gates: make the required order of operations impossible to miss.
D_GATES = [
    _row("SUG-D1", "License-status gate per unit",
         "Add a per-unit row on the Anonymized Case page and on the Notice Checklist: 'Rent Increase License status for this unit, confirmed on (date), portal reference (optional)'. Leave it blank and flag it until the owner fills in a real date.",
         "The license is the one precondition that can void an otherwise lawful increase, and Rule 13.14 tests the effective date of the increase, not the date the notice was served. A dated status field turns an invisible dependency into a visible gate.",
         "Rule 13.14: a rent increase purporting to be effective while the landlord is unlicensed renders the entire increase null and void, and the effective date - not the date of service - is the test. SF.gov: a landlord must have a current rent increase license on file before any annual or banked increase can go into effect.",
         ["S07", "S73", "S53", "S08"], "Low", "High",
         notes="Builds the site-side control behind SUG-A2, which obtains the fact itself."),
    _row("SUG-D2", "Housing Inventory filing tracker",
         "Add a per-unit filing row: 'Housing Inventory submitted for reporting year (YYYY) on (date)', with the recurring March 1 deadline and the rule that units in buildings with fewer than 10 residential units have reported since March 1, 2023.",
         "The rent increase license is generated from the Housing Inventory submission, so the filing is the upstream cause of every license gap. Tracking it removes the most common way a license goes missing.",
         "SF.gov: all owners of residential property are required to report into the Housing Inventory by March 1 every year; reporting began March 1, 2023 for condominiums and units in buildings with fewer than 10 residential units; the license is generated from the report.",
         ["S07", "S53", "S55"], "Low", "High",
         notes="Builds the site-side control behind SUG-A2."),
    _row("SUG-D3", "Rent Board Fee calendar with the tenant-recovery switch",
         "Add a fee timeline to the Rent Board Fee page (October informational notice, December exemption window, January invoice, March 1 due date, 5% monthly late penalties capped at 15%, June 1 referral) plus one yes/no field per unit: 'Was the tenant in occupancy on November 1 of the applicable tax year?'. That answer alone should decide whether the 50% recovery may be charged.",
         "The fee is a separate money decision from the rent increase, it has its own penalty ladder, and the right to recover half of it turns on a single November 1 occupancy test. Treating it as a calendar plus a switch removes a recurring source of error.",
         "SF.gov Rent Board Fee page: $59.00 per dwelling unit for 2026-2027, due March 1, 5% late penalty each month capped at 15%, referral to the Bureau of Delinquent Revenue after June 1, exemption request deadline December 14, 2026. 50% may be recovered only from tenants in occupancy on November 1 of the applicable tax year.",
         ["S56", "S62", "S65"], "Low", "Medium",
         notes="Site-side counterpart to SUG-A7."),
    _row("SUG-D4", "Effective-date rate engine",
         "Add a small calculator that takes the anniversary date and the intended effective date, then selects the published rate for the period that contains the effective date from the Current Rates ledger, instead of letting a reader pick a rate from a list.",
         "The rate in effect on the effective date controls, not the rate in effect when the notice is written, and the currently published 1.6% rate covers only March 1, 2026 through February 28, 2027. A date-driven selector prevents picking the wrong period.",
         "SF.gov: the percentage is the one in effect on the date the increase takes effect; 1.6% applies to increases effective March 1, 2026 through February 28, 2027, and Section 37.3 caps the increase at 7% of CPI.",
         ["S01", "S02", "S04", "S21"], "Medium", "High"),
    _row("SUG-D5", "Banked-increase ledger per unit",
         "Add a per-unit table that logs every increase the owner could have taken and did not take: the year, the anniversary date, the published percentage at that time, and whether 24 full months elapsed without any increase. Show the running banked total and the notice wording that must state the banked portion.",
         "Banking requires the 24-full-month test for each skipped year, forbids compounding and prorating, and never carries to a new tenant. It is the hardest part of the calculation to hold in memory and the easiest to misstate in a notice.",
         "SF.gov: a skipped increase is banked only if at least 24 full months pass without any increase; banked percentages are added, never compounded or prorated, and the notice must state the banked portion.",
         ["S05", "S54", "S77"], "Medium", "High",
         notes="Site-side counterpart to SUG-A3."),
    _row("SUG-D6", "Pending-legislation watch row",
         "Add a dated row to the Rates page that records the status of File 261020 and any successor, labelled 'proposed - not enacted', and never feeds it into a calculation. Re-check it at each review cycle.",
         "A notice about a proposed 10% cap was posted on the Rent Board's own rent-increase, Current Rates and Forms Center pages on November 9, 2026. Because it appears on live official pages, there is a real risk of reading it as current law.",
         "SF.gov notice posted November 9, 2026 on the rent-increase page, the Current Rates page and the Forms Center, and Board of Supervisors File 261020 in Legistar: the 10% combined banked and capital-improvement cap is proposed, not enacted, and subject to change.",
         ["S71", "S72", "S87"], "Low", "Medium"),
    _row("SUG-D7", "Retaliation-window screen",
         "Add a screening block that must be answered before any notice is dated: 'In the last 12 months, has any tenant complained to an agency or exercised a right under the tenant chapter?', with the answer and the date checked recorded next to it.",
         "A rent increase that follows a protected complaint or act can be challenged as retaliation within the statutory window, independently of whether the increase amount itself is permitted. The bar is time-based and easy to miss on a case with a repair or complaint history.",
         "California Civil Code 1942.5(a): a landlord may not retaliate against a lessee who has exercised rights under the chapter or complained to an agency within 12 months of the complaint; Section 37.10B separately prohibits bad-faith harassment.",
         ["S57", "S22"], "Low", "High",
         notes="Site-side counterpart to the 180-day history question on the Decision Readiness page (DR-14)."),
    _row("SUG-D8", "Uniform-criteria record for the one-unit-or-both decision",
         "Add a field that records the single neutral eligibility criterion applied to each unit (for example: the unit's anniversary date has passed), the date each anniversary passed, and the owner-entered reason if only one unit is raised.",
         "No official rule requires raising both units. What a reviewer would look for is a consistent, documented, non-pretextual reason applied the same way to both units, which is what the fair-housing rules ask when a neutral practice has a disparate effect.",
         "24 CFR 100.500: a practice with a disparate effect violates the Fair Housing Act unless it is supported by a substantial legitimate nondiscriminatory interest and no less discriminatory alternative is available. California Government Code 12955 and the California Civil Rights Department housing guidance add source-of-income and retaliation protections.",
         ["S42", "S41", "S38", "S39"], "Low", "High",
         notes="Overlaps SUG-C2; this adds the site field that records the reason."),
    _row("SUG-D9", "Roommate and 6.14 fact screen",
         "Add a structured, mostly blank questionnaire for each unit: who was the last original occupant, the date occupancy began, whether a 6.14 notice was ever served and when, and whether any occupant is a subtenant or a co-tenant.",
         "A market-rate reset on remaining occupants turns on the last original occupant, the date occupancy began and the 6.14 notice. Those are exactly the facts this case has not verified, and they decide whether an unlimited increase is even available.",
         "SF.gov on Section 6.14 and Costa-Hawkins: an unlimited increase on remaining occupants requires that the last original occupant has vacated and that a proper 6.14 notice was served within a reasonable time; a co-tenant is not subject to such an increase.",
         ["S16", "S01", "S37"], "Low", "High",
         notes="Site-side counterpart to SUG-A4."),
    _row("SUG-D10", "Coverage determination sheet per unit",
         "Add a per-unit coverage row recording: pre-1979 construction confirmed (date checked), not a single-family dwelling, no new-construction partial exemption, no single-family/condominium partial exemption, and the Property Information Map link with the date it was checked.",
         "If a unit is not covered by rent control the rent increase limitations do not apply to it and every other gate changes. This is the first gate and the one currently resting on an assumption rather than a record.",
         "SF.gov: many units built on or before June 13, 1979 that are not single-family dwellings have rent control, and partial exemptions exist for newly constructed units and for certain single-family homes and condominiums; the Property Information Map is the official lookup.",
         ["S06", "S32", "S59", "S60", "S08"], "Low", "High",
         notes="Site-side counterpart to SUG-A1."),
    _row("SUG-D11", "Notice assembly with required contents",
         "Extend the Notice Worksheet so the assembled notice shows, in the notice itself, the dollar amount, the percentage, the effective date and any banked portion, and carries a delivery-method row (personal delivery or mail, with the 5-day extension) and a proof-of-service row.",
         "Notice content and delivery method are the two steps most often defective, and both have fixed external requirements. Assembling the notice inside the tool means the checklist and the document cannot drift apart.",
         "California Civil Code 827: at least 30 days' notice where the increase is 10% or less and 90 days where it exceeds 10%, delivered personally or by mail, and the notice must state the amount of the increase and its effective date.",
         ["S35", "S78", "S01", "S26"], "Medium", "High",
         notes="Builds out SUG-B1."),
    _row("SUG-D12", "Petition routing table",
         "Add a table that names the petition or worksheet required before a notice for each increase type (capital improvement, operating and maintenance, utility, comparable rent, and the passthrough petitions) and marks them explicitly 'not required for a plain annual or banked increase'.",
         "Each petition category has its own pre-notice filing rule, and the filing for one type is not a substitute for another. A routing table stops the wrong petition from being filed, or none being filed when one is required.",
         "SF.gov: capital improvement, operating and maintenance, utility, comparable-rent and passthrough increases each have their own petition or worksheet rules that apply before the increase is noticed; no petition is required for a plain annual or banked increase.",
         ["S09", "S10", "S11", "S12", "S13", "S14", "S77"], "Low", "Medium"),
]

# ------------------------------------------------------------------ group E
# Evidence and defensibility: make the record reviewable.
E_EVIDENCE = [
    _row("SUG-E1", "Case-file completeness checklist",
         "Add a checklist of the documents an owner should be able to produce for each unit: the current lease, every prior increase notice, proof of service for each notice, the license status record, the Housing Inventory submission receipt, the Rent Board Fee payment receipt, the Property Information Map printout, and the rate sheet actually used for the calculation.",
         "An unlawful-increase petition is decided on a documentary record. Missing documents, not wrong amounts, are how an otherwise compliant increase fails review.",
         "California Civil Code 827 and Code of Civil Procedure 1013 govern notice and service by mail; the Housing Inventory submission, the portal license record, the fee payment and the Property Information Map are the official records the owner already has to create.",
         ["S35", "S78", "S07", "S55", "S56", "S32", "S02"], "Low", "Medium"),
    _row("SUG-E2", "Tenant-side challenge walkthrough",
         "Add a page that follows the exact path a tenant can take - search the Rent Board Portal for the landlord's license status, file the Tenant Petition and Form C at no charge and with no time limit, attend a hearing before an Administrative Law Judge - and lists what a reviewer would check at each step.",
         "The standard asked for is that an increase survives review by a San Francisco tenant-side lawyer. No official source offers pre-approval, so the closest available substitute is to run the challenge yourself before serving. The Rent Board states the process is designed so that no one needs an attorney.",
         "SF.gov: a tenant may file a Tenant Petition and Form C at no charge and with no time limit, and the matter is set for a hearing before a Rent Board Administrative Law Judge; the process is designed so that no one needs an attorney. A tenant may also search the portal for the landlord's license status.",
         ["S25", "S08", "S26", "S24"], "Medium", "High"),
    _row("SUG-E3", "Printable attorney-review handoff packet",
         "Add a one-page printable case summary, anonymized with dates and amounts unchanged, that can be handed to a tenant-side or defense attorney: the unit facts, the proposed increase, every rule relied on with its official link, and a list of every item still blank or flagged.",
         "Turning a dashboard into a document is what 'able to pass review' actually requires. Publishing the blanks in the packet rather than hiding them is what lets a reviewer judge the case rather than the presentation.",
         "SF.gov tenant and landlord resources, the free Rent Board counselor service, the unlawful-rent-increase petition, 42 USC 3604 and 24 CFR 100.500 are the rules a reviewer would apply.",
         ["S23", "S24", "S25", "S42", "S41"], "Low", "High",
         notes="Builds out SUG-A6 and SUG-B1."),
    _row("SUG-E4", "Neutral-language bank for the increase letter",
         "Add a short, sourced bank of neutral phrasings for the increase letter - stating the amount, percentage and effective date without characterising the tenants, their conduct, or their ability to pay - each tied to the rule it is designed to satisfy.",
         "Bad-faith conduct is a separate exposure from the arithmetic of the increase, and Section 37.10B carries its own civil remedies. Language control is a cheap control that a reviewer can check on the face of the letter.",
         "Section 37.10B prohibits bad-faith harassment of a tenant by a landlord and carries civil remedies; the published guidance is the official statement of the conduct that is prohibited.",
         ["S22", "S01"], "Medium", "Medium"),
    _row("SUG-E5", "Public-records disclosure note before filing",
         "Add a note to the Housing Inventory steps that the information entered in the submission is public and may include the owner's name and business, contact information, approximate square footage, bedrooms, bathrooms and vacancy/occupancy history, with a checkbox confirming the owner has read it before filing.",
         "The required filing publishes the owner's own identifying and business information. That is a real privacy consequence of the compliance step itself and belongs at the point of action, not buried on a research page.",
         "SF.gov: the information entered in the Housing Inventory submission is public and may include name and business, contact information, approximate square footage, number of bedrooms and bathrooms, and vacancy or occupancy history for the past 12 months.",
         ["S07", "S53"], "Low", "Medium"),
]

# ------------------------------------------------------------------ group F
# Discovering the missing information.
F_MISSING = [
    _row("SUG-F1", "Missing-information register",
         "Add one page that lists every open question in this case with five columns: what is missing, which official source would resolve it, how to obtain it, who must supply it, and which decision it blocks. Populate it from the existing needs-review rows so nothing stays only on the Flagged for Review page.",
         "Every unresolved item currently appears as a blank cell on several pages. A single register turns a scatter of blanks into an ordered work plan, and it is the direct answer to what information has to exist before a decision can reasonably be made.",
         "The official routes that would resolve the open items are the portal and Housing Inventory pages, the Property Information Map, the Section 6.14 guidance, the counsel line and the Tenant Petition process.",
         ["S25", "S24", "S16", "S55", "S32", "S07"], "Medium", "High",
         notes="Consolidates the Decision Readiness page (DR-* rows), which answers the same question for this case; this adds the reusable register."),
    _row("SUG-F2", "Facts only the owner can obtain",
         "Add a checklist of the case facts that no amount of outside research can supply: the last original occupant in each unit, the date occupancy began, whether a 6.14 notice was served, each unit's anniversary date, the full lease and notice history, square footage and bedroom/bathroom counts, whether either unit is an in-law unit, whether the owner occupies one unit, and whether each tenant was in occupancy on November 1 for the fee-recovery test.",
         "Several of the blanks on this site are the owner's own facts, not public records. Naming them explicitly prevents them from being mistaken for research gaps that more research would close.",
         "The Housing Inventory asks the owner for square footage, bedrooms, bathrooms, the date occupancy began and the base rent; the fee page turns on November 1 occupancy; the Section 6.14 page turns on the last original occupant and the date occupancy began. None of these are public records.",
         ["S07", "S53", "S16", "S56", "S60", "S59"], "Low", "High",
         notes="Overlaps SUG-A1 to SUG-A7; this is the explicit owner-only list."),
    _row("SUG-F3", "Counsel call script for the unanswered questions",
         "Add a printable call script containing only the specific open questions, with the Rent Board counselor's published phone number, office hours and the note that counseling is free, multilingual and cannot give legal advice.",
         "Rent Board counseling is free and multilingual but explicitly will not give legal advice, and the published guidance tells callers to have their questions written down in advance. A prepared script converts a five-minute call into a usable answer.",
         "SF.gov: counseling is free, available in Spanish, Cantonese and Mandarin with interpretation for other languages, is provided by phone Monday to Friday 9-12 and 1-4, and cannot give legal advice; the published guidance tells callers to have their questions written down first. Calls are generally limited to 5 minutes.",
         ["S24", "S07", "S55", "S16"], "Low", "High",
         notes="Builds out SUG-A5."),
    _row("SUG-F4", "Pre-decision gate sequence",
         "Add a single 'can I proceed?' checklist at the top of the process page that must be fully answered before any notice is dated: coverage confirmed, Housing Inventory filed, license current on the effective date, no retaliation window open, rate selected for the effective date, banked total confirmed, notice period and method chosen, petition routed, uniform criterion recorded.",
         "The rules are sequential and several of them are date-triggered. A single ordered gate list is what turns the site from a reference into something that can be worked through in order without missing a step.",
         "The sequence is fixed by the official rules: coverage, Housing Inventory report, current license on the effective date, no open retaliation window, the rate for the effective date, the banked total, the notice period and delivery method, petition routing, and one consistent criterion applied to both units.",
         ["S07", "S73", "S35", "S05", "S57", "S42", "S16", "S09"], "Low", "High",
         notes="Site-side ordering of the Decision Readiness gates (DR-G1 to DR-G5)."),
]

# ------------------------------------------------------------------ group G
# Internal site quality.
G_INTERNAL = [
    _row("SUG-G1", "Per-row verification date",
         "Add a visible 'last verified' date to every published row and every official source, so a reader can tell which findings were re-checked most recently and which are inherited from an earlier pass.",
         "Official pages change without notice - a proposed-cap notice appeared on three Rent Board pages in the same week. Showing the verification date makes the age of each figure visible instead of implied.",
         "The official pages themselves change, so the age of each figure has to be visible rather than implied.",
         ["S68"], "Low", "High", internal=True,
         notes="Extends SUG-B4 and SUG-B2."),
    _row("SUG-G2", "Link and content monitor for the source ledger",
         "Add a scheduled job that re-fetches every official URL in the ledger and reports any redirect, error or content change, and posts the result as a dated entry rather than editing a value silently.",
         "The ledger already records several official URLs that changed or returned errors, and official pages disagree with each other on examples. An automated check would surface the next change before a reader relies on it, and it preserves the rule that a value is never changed without a note.",
         "The repository and its GitHub Pages build API are the project records for how this site is maintained.",
         ["S68", "S69"], "Medium", "High", internal=True,
         notes="Same goal as SUG-B2; this one adds content-change detection, not just a link check."),
    _row("SUG-G3", "Unchanged-column consistency",
         "Keep the current table shape on every finding page and publish the Suggestions page and the missing-information register in the same shape, so a reviewer can read any page without relearning the layout.",
         "A single consistent shape is what makes the site scannable. Suggestions and the missing-information register are new pages, and matching the existing shape keeps the dashboard coherent instead of becoming a second, differently-organised document.",
         "The five-column shape already used on every finding page is the reference.",
         ["S68"], "Low", "Medium", internal=True),
    _row("SUG-G4", "Blank-means-unknown convention, stated once and repeated",
         "Keep the existing convention that an empty cell means 'not officially confirmed' and never means zero or 'not applicable', and repeat the legend at the top of every page rather than only on the landing page.",
         "A blank on this site is a deliberate statement that no official source confirms the value. If that is only explained on one page, a reader who lands on another page may read a blank as an answer.",
         "A blank means no official source confirms the value, which is different from a zero or from 'not applicable'.",
         ["S68"], "Low", "Medium", internal=True),
    _row("SUG-G5", "Print and mobile review mode",
         "Add a print stylesheet and a narrow-screen layout so the notice checklist, the worksheet and the case summary can be used on a phone at the property and printed for a file or for an attorney.",
         "The deciding moments - checking a license status, serving a notice, assembling a file - happen away from a desk. A desktop-only dashboard is usable for research but not for the moment of action.",
         "This is a proposal about how this research site is presented on small screens and on paper.",
         ["S68"], "Low", "Medium", internal=True),
    _row("SUG-G6", "Review-cycle date on the landing page",
         "Show one 'next review due' date on the landing page, set after each re-verification pass, together with the list of items that are most likely to have changed (the published rate period, the pending cap, the fee amount and the license rule).",
         "The published rate is period-limited and the pending legislation can be enacted at any time. A single visible review date makes it obvious when the dashboard needs re-checking rather than assuming it is current.",
         "The items most likely to change are the published rate period, the proposed cap in File 261020, the Rent Board Fee amount and the licensing rule - each of which has a published official source.",
         ["S02", "S71", "S56", "S07", "S68"], "Low", "Medium"),
]

T54_SECTIONS = [
    {"title": "D. Compliance gates - make the required order of operations impossible to miss",
     "intro": "Each proposal below adds a gate that must be answered before a notice is dated. Every one is grounded in a rule published by the San Francisco Rent Board, the Rent Ordinance, California statute or federal regulation. Contributed by the 2026-11-13 final review.",
     "rows": D_GATES},
    {"title": "E. Evidence and defensibility - make the record reviewable",
     "intro": "These proposals build the paper trail a tenant-side reviewer would look for, and make the case exportable as a document rather than only as a web page. Contributed by the 2026-11-13 final review.",
     "rows": E_EVIDENCE},
    {"title": "F. Discovering the missing information",
     "intro": "The owner's standard is that a decision should rest on what is already known and what is not yet known. These proposals turn the open blanks into an ordered discovery plan, and separate the facts that only the owner can supply from the ones a public record can answer. Contributed by the 2026-11-13 final review.",
     "rows": F_MISSING},
    {"title": "G. Internal site quality - proposals about this site",
     "intro": "These rows are about the research site itself rather than about the law. They carry no official legal basis and are labelled as internal site-design proposals; they are listed so the owner can accept, reject or defer them on their merits. Contributed by the 2026-11-13 final review.",
     "rows": G_INTERNAL},
]


def all_t54_rows():
    rows = []
    for sec in T54_SECTIONS:
        rows.extend(sec["rows"])
    return rows


def checklist_rows():
    """One blank decision row per T54 proposal, for the reviewer to complete.

    The checklist rows carry their own ``CL-`` identifiers so that a checklist
    row and the proposal it refers to are never confused, and so that every row
    ID on the site stays unique.
    """
    out = []
    for r in all_t54_rows():
        cid = "CL-" + r["id"].replace("SUG-", "")
        out.append({"id": cid, "label": r["label"], "value": "", "status": "analysis",
                    "source_ids": r["source_ids"], "notes": "", "flag_id": "",
                    "source_note": ""})
    return out
