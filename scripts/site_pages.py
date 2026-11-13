"""Page definitions: every row has source_ids, status, value, notes and optional flag_id."""

import json
from pathlib import Path

COLUMNS = ["Item", "Value / finding", "Status", "Official source(s)", "Notes / flag"]
OWNER_COLUMNS = ["Item", "Owner-supplied value", "Status", "Source", "Notes / flag"]

def row(id, label, value, status, source_ids, notes="", flag_id="", source_note=""):
    return {"id": id, "label": label, "value": value, "status": status, "source_ids": source_ids,
            "notes": notes, "flag_id": flag_id, "source_note": source_note}

def owned(id, label, value, notes=""):
    """Owner-supplied case fact: published, anonymized, and explicitly not an official source."""
    return {"id": id, "label": label, "value": value, "status": "owner supplied", "source_ids": ["S06", "S01"],
            "notes": notes, "flag_id": "F49", "source_note": "Owner intake (anonymized and unverified); official links provide general context only, not verification of this fact."}

PAGES = {
    "summary": {
        "title": "Executive Summary",
        "description": "Bottom line for Rental increase SF, with every finding linked to an official source.",
        "sections": [
            {"title": "FOREFRONT - Is the \"inform the Rent Board\" law state or local? (local)", "columns": COLUMNS, "rows": [
                row("SL-01", "The direct answer", "LOCAL. The duty to report a rent-controlled unit to the SF Rent Board and hold a Rent Increase License comes from the San Francisco Administrative Code (Chapter 37, Sec. 37.15), added by Ordinance No. 265-20 effective January 18, 2021. It is not a California state statute and not a federal rule.", "verified", ["S53", "S90", "S21"], "This is the answer to the state-vs-local question, placed first. Full layer-by-layer table on the Local Law page (LAW-01 to LAW-08)."),
                row("SL-02", "Where the '2023' date comes from", "2023 is the year the LOCAL duty became operative for condominiums and buildings with 1-9 residential units (March 1, 2023). It is not the year a state law passed. Buildings with 10 or more units began reporting July 1, 2022; the ordinance itself dates from January 18, 2021. A two-unit building is in the 1-9 unit group.", "verified", ["S53", "S73", "S01"], "Rent Board Rule 13.14 states the same two dates and tests the increase's effective date, not the date of service."),
                row("SL-03", "What the real 2023 state law was", "SB 567 (Chapter 290, Statutes of 2023) amended the statewide Tenant Protection Act - just-cause eviction rules and enforcement of the state 5%-plus-CPI / 10% rent cap - and became operative April 1, 2024. It creates no rent-board reporting duty.", "verified", ["S88", "S89"], "Negative finding from the chaptered bill text."),
                row("SL-04", "Why the state cap is not this owner's ceiling", "Civil Code 1947.12(d)(3) excludes housing under a stricter local rent control ordinance, and SF.gov states AB 1482 does not apply to units under the SF Rent Ordinance limits. The local 1.6% for 3/1/26-2/28/27 governs covered SF units.", "verified", ["S36", "S27", "S01"], "State 8.8% is not an alternative the owner may elect."),
                row("SL-05", "So what must the owner actually do?", "Report into the Rent Board Housing Inventory through the Rent Board Portal (free, due March 1 each year), which generates the Rent Increase License; confirm the license is on file on the increase's effective date; then serve the compliant written notice. There is no separate licence application form.", "verified", ["S07", "S01", "S53"], "Step-by-step page: PRC-01 to PRC-12. The Rent Board Fee is a separate obligation (FEE page)."),
            ]},
            {"title": "FOREFRONT - Rent Board & Rent Increase License: individual owner", "columns": COLUMNS, "rows": [
                row("LIC-01", "Does an individual (non-corporate) owner still need the license?", "Yes - SF.gov states 'a landlord must get a rent increase license before imposing annual allowable and/or banked rent increases'; no individual-owner exception is stated on the official pages re-fetched 2026-11-07", "verified", ["S01", "S07"], "Ownership form (individual vs corporation) is not listed as an exemption. Do not rely on being a small/individual owner."),
                row("LIC-02", "Small buildings (1-9 units) timing", "Requirement effective July 1, 2022; March 1, 2023 for condominiums and buildings with 1-9 residential units", "verified", ["S01", "S07"], "A small individual-owned building is therefore covered now (2026)."),
                row("LIC-03", "Step 1 - Report to the Rent Board (Housing Inventory)", "All owners of residential property are required to report through the Rent Board Portal; reporting is free, online 24/7, due March 1 every year", "verified", ["S07"], "This reporting is how you 'inform the Rent Board'. Information submitted is public; submit under penalty of perjury."),
                row("LIC-04", "Step 2 - License is generated", "Property owners who report a unit as tenant-occupied receive a rent increase license; it is automatically generated for non-owner-occupied units", "verified", ["S07"], "The license does not need to be included with the rent increase notice to tenants."),
                row("LIC-05", "Step 3 - License must be current BEFORE the increase takes effect", "A landlord must have a current rent increase license on file with the Rent Board before any annual or banked rent increase can go into effect; a notice is not enforceable without a license on the effective date", "verified", ["S07", "S01"], "Legal test: the license must be current on the effective date. Recommended conservative order: report -> confirm license -> serve notice -> effective date. See flag F25 on consequence wording."),
                row("LIC-06", "Late reporting", "You can still submit and receive a license after the March 1 deadline; the Rent Board does not assess monetary penalties for late filing - but the increase notice is not enforceable without a license on the effective date", "verified", ["S07"], "Late filing does not cure a notice whose effective date passed without a license; get legal advice on any already-served notice."),
                row("LIC-07", "Step 4 - Only then notify tenants", "30-day written notice (90-day if >10% alone/combined in same year; +5 days if mailed) stating dollar amount, percentage and effective date, using the rate in effect on the increase date", "verified", ["S01", "S05", "S35"], "License first, tenant notice second. License alone does not satisfy state/local notice law; you must still comply with all other rent increase laws."),
                row("LIC-08", "Can tenants check?", "Tenants can search the Rent Board Portal to see if their landlord is up to date with their rent increase license; if you miss the deadline the Rent Board may notify tenants you are not in compliance", "verified", ["S07", "S08"], "Assume tenants and free tenant-side legal services can and will check this before paying an increase."),
                row("LIC-09", "This case: license / Housing Inventory status", "", "needs review", ["S07", "S01"], "Owner-supplied intake does not confirm Housing Inventory reporting or a current license for either unit; blank and flagged. No increase should be treated as effective until this is confirmed.", "T03-F05"),
                row("LIC-10", "Full step-by-step page", "12 numbered steps from coverage check to notice delivery, each with its official source link, plus the ordinance text and the case-specific application", "verified", ["S01", "S07", "S53", "S21", "S35"], "Published on the Step-by-Step License page (pages/process.html)."),
            ]},
            {"title": "Executive findings", "columns": COLUMNS, "rows": [
                row("SUM-01", "Current SF annual allowable increase", "1.6% effective 3/1/26-2/28/27", "verified", ["S01", "S02", "S03", "S04"], "For covered rent-controlled units, once every 12 months."),
                row("SUM-02", "State-only AB 1482 SF cap", "8.8% for 8/1/26-7/31/27", "verified", ["S27"], "Does NOT apply to units under SF Rent Ordinance rent-increase limits."),
                row("SUM-03", "Federal general private-rent cap", "", "needs review", ["S43", "S40", "S41", "S42"], "No official source found; blank and flagged.", "F22"),
                row("SUM-04", "Rent Increase License", "Current license required before annual/banked increase takes effect", "verified", ["S01", "S07", "S08"], "Unlicensed increase may be null/void."),
                row("SUM-05", "Notice", "30-day written; 90-day if >10%; +5 days if mailed; dollar amount, percentage, effective date", "verified", ["S01", "S05", "S35"], "Use rate in effect on increase date."),
                row("SUM-06", "Banked increases", "Only if >=24 full months without any increase; add percentages, do not compound/prorate", "verified", ["S05"], "No banked amount inferred for this case."),
                row("SUM-07", "Roommate / additional occupant", "Cannot charge extra rent merely because a new/additional roommate moved in", "verified", ["S01", "S17", "S18", "S19"], "No market-rate reset inferred."),
                row("SUM-08", "Unit 1 vacancy-decontrol issue", "", "needs review", ["S15", "S16", "S28", "S37"], "Continuing occupant legal status and last-original-occupant facts unverified.", "T03-F04"),
                row("SUM-09", "Corporate practice", "IRT Q4 2025 same-store renewal 2.9%, new -3.7%, blended 0.8%; Invitation Homes 2025 renewal 4.6%, new -0.8%", "verified", ["S48", "S49"], "Portfolio-level, not SF-specific and not a legal benchmark."),
                row("SUM-10", "Individual practice", "June 2024: 23 landlord petitions/154 units; 73 tenant petitions; 89 eviction notices", "verified", ["S29"], "Narrow formal-petition evidence only."),
                row("SUM-11", "Conservative approach", "Identical, neutral, license-and-notice-compliant <=1.6% policy on each eligible unit; or less", "analysis", ["S01", "S07", "S35", "S42"], "Compliance checklist capable of tenant-lawyer review; no approval or guarantee."),
                row("SUM-12", "One unit or both", "", "needs review", ["S41", "S42", "S38"], "No official source requires both; document neutral eligibility reasons if only one is raised.", "F22"),
                row("SUM-14", "Pending banked-increase legislation", "File 261020 is proposed, not enacted; it could limit combined banked and capital-improvement increases to 10% per year.", "verified", ["S05", "S71"], "If enacted as proposed, it would apply to banked notices and capital-improvement petitions from September 15, 2026; check status before relying on a banked calculation. F46.", "F46"),
                row("SUM-13", "94122 Small Area FMR", "", "needs review", ["S44", "S46", "S50", "S51", "S52"], "Official ZIP row not obtained; blank.", "T03-F07"),
            ]},
        ],
    },
    "process": {
        "title": "Step-by-Step: Rent Board License and Notice",
        "description": "The direct answer to the licensing question, the ordinance text, the 12-step process, and how it applies to the two anonymized units.",
        "sections": [
            {"title": "Direct answer and ordinance text", "columns": COLUMNS, "rows": [
                row("PRC-01", "Must an individual property owner (not a corporation) get a Rent Increase License before raising rent?", "Yes. A landlord must have a current Rent Increase License on file before any annual or banked increase can take effect. The requirement follows the unit's rent-controlled status, not the owner's size or corporate form.", "verified", ["S01", "S07", "S08", "S53"], "No owner-type, individual-owner or small-portfolio exemption appears on the official pages."),
                row("PRC-02", "What does the Rent Ordinance itself say?", "Section 37.3(a)(1): a landlord who has reported the required information under Section 37.15 shall have a license to impose an annual increase not exceeding 60% of the published CPI increase, never more than 7%. Section 37.15(e): a substantially compliant owner receives the license; otherwise it is suspended and the tenant is not obligated to pay the increased rent for the months of the suspension.", "verified", ["S21", "S53"], "The license condition is written into the ordinance, not only the SF.gov summaries."),
                row("PRC-20", "Is there a separate licence application form I have to file?", "No. The Rent Board describes the licence as generated by the Housing Inventory report: 'once you have reported into the Housing Inventory, a rent increase license will be automatically generated for non-owner occupied units.' SF.gov's increase page states the same route: 'To get a rent increase license, a landlord must first report into the Rent Board Housing Inventory.' There is no separate licence application and no separate licence fee - SF.gov states that reporting into the Housing Inventory 'is free and can be done online 24/7' (the annual Rent Board Fee is a different obligation).", "verified", ["S07", "S01"], "The Rent Board Fee (S56) IS a separate annual payment and has its own exemption request window - do not confuse the two (flag F33)."),
                row("PRC-21", "So \"informing the Rent Board\" and \"applying for the licence\" are the same step?", "Yes - both refer to the Housing Inventory report. Reporting is done through the Rent Board Portal, is free, is available 24/7 online, is due March 1 every year, and is submitted under penalty of perjury.", "verified", ["S07", "S55", "S53"], "The report is the licence-generating act; the licence itself does not need to be attached to the tenant notice."),
                row("PRC-22", "Is this a state requirement, a local requirement, or both?", "Local only. It is San Francisco Administrative Code Sec. 37.15 (added by Ord. 265-20, effective January 18, 2021). No California statute requires reporting a rent increase to a rent board; the 2023 state law (SB 567) addressed just cause and the state rent cap and became operative April 1, 2024.", "verified", ["S53", "S90", "S88", "S73"], "Full layer table on the Local Law page: LAW-01 to LAW-08, summarized on the Executive Summary at SL-01 to SL-05. Flag F53."),
                row("PRC-03", "Is there a small-owner or fewer-than-10-unit exemption?", "No exemption found. Condominiums and units in buildings with fewer than 10 residential units have been required to report since March 1, 2023, with updates every March 1.", "verified", ["S07", "S08", "S53"], "Applies to this two-unit building if the units are rent-controlled."),
                row("PRC-04", "Must the owner report into the Housing Inventory first?", "Yes. All owners of residential property are required to report; a rent increase license is generated for units reported as tenant-occupied.", "verified", ["S07", "S53"], "Free; annual deadline March 1; no monetary penalty for late filing."),
                row("PRC-05", "Does informing the Rent Board mean filing each increase notice?", "The official pages describe the license as arising from the annual Housing Inventory report. No separate filing of an individual increase notice is described, and the license does not need to be included with the notice.", "verified", ["S07", "S53", "S01"], "Read as absence of a stated requirement; confirm with a Rent Board counselor."),
                row("PRC-06", "What happens if a notice goes into effect without a current license?", "The notice may be null and void (possibly for multiple years) or unenforceable, depending on the SF.gov page; the tenant may be entitled to a refund and may file a Tenant Petition for Unlawful Rent Increase for an Administrative Law Judge hearing.", "verified", ["S08", "S53", "S25", "S26"], "Wording differs between SF.gov pages - see flag F25."),
                row("PRC-07", "Does the license requirement cover every kind of increase?", "It covers annual allowable and banked increases on rent-controlled units. SF.gov states it is not required for Section 6.14/Costa-Hawkins increases or for passthroughs allowed under the Rent Ordinance.", "verified", ["S08", "S16", "S09"], "Those increases have their own notice and petition rules."),
                row("PRC-08", "Is the Housing Inventory information public?", "Yes. SF.gov states the information entered in the Housing Inventory submission is public, and may include name and business, contact information, approximate square footage, bedrooms, bathrooms and vacancy/occupancy history.", "verified", ["S07", "S53"], "Privacy note: the required filing publishes the owner's name and business contact information."),
                row("PRC-09", "Does the license requirement apply if the unit is not rent-controlled?", "No. SF.gov states the Rent Increase License rules apply only to units under San Francisco rent control.", "verified", ["S08", "S06"], "Coverage of the specific address is unverified in this case."),
            ]},
            {"title": "Step-by-step process (with official links)", "columns": COLUMNS, "rows": [
                row("STP-01", "Step 1 - Confirm the unit is under the Rent Ordinance", "Many units built on or before June 13, 1979 that are not single-family dwellings have rent control; check the address in the SF Planning Property Information Map. Partial exemptions exist.", "verified", ["S06", "S32", "S08"], "Exact address not supplied in this case."),
                row("STP-02", "Step 2 - Create a Rent Board Portal account", "Owners create an account in the Rent Board Portal to reach the Housing Inventory and the license record; paper filings can be emailed to the Rent Board or dropped off at its office.", "verified", ["S55", "S07", "S08"], "Office open 9-4 weekdays; counseling 415-252-4600."),
                row("STP-03", "Step 3 - Report each unit into the Housing Inventory", "Report by March 1 each year (buildings under 10 units since March 1, 2023) under penalty of perjury: owner or manager contact, square footage, bedrooms, bathrooms, occupancy date and base rent in $250 increments.", "verified", ["S07", "S53"], "Reporting is free; no monetary penalty is assessed for late filing."),
                row("STP-04", "Step 4 - Confirm a current license for each unit", "The license is generated for tenant-occupied units after reporting and must be current on the effective date of the increase, not merely later.", "verified", ["S07", "S08", "S55"], "Check status by address or APN in the portal."),
                row("STP-05", "Step 5 - Fix the anniversary date", "The first annual increase may be imposed 12 months after the lease began; after an increase, the increase date becomes the anniversary date and the next increase needs at least 12 more months.", "verified", ["S01"], "A later increase date becomes the new anniversary date."),
                row("STP-06", "Step 6 - Use the rate in effect on the effective date", "1.6% for increases effective March 1, 2026 through February 28, 2027; the rate is 60% of the Bay Area CPI-U increase and Section 37.3 caps it at 7%.", "verified", ["S01", "S02", "S04", "S21"], "No rate published yet for increases on or after 3/1/27 - flag F27."),
                row("STP-07", "Step 7 - Decide whether a banked increase applies", "A skipped increase is only banked if at least 24 full months pass without any rent increase; banked percentages are added together, never compounded or prorated, never carry to a new tenant, and need no Rent Board petition.", "verified", ["S05", "S54"], "SF.gov examples describe elapsed time differently - flag F03."),
                row("STP-08", "Step 8 - Calculate on base rent only and do not round up", "Multiply base rent (including parking or storage charges) by the total percentage; temporary passthroughs and fluctuating charges are excluded, and the result is not rounded up.", "verified", ["S01", "S03", "S54"], "See the Calculations page for the illustrative arithmetic."),
                row("STP-09", "Step 9 - File any petition or worksheet before the notice", "Capital improvement, operating and maintenance, utility, comparable-rent and bond/water passthrough increases each have their own petition or worksheet rules that apply before the increase is noticed.", "verified", ["S09", "S10", "S11", "S12", "S13", "S14"], "Not needed for a plain annual or banked increase."),
                row("STP-10", "Step 10 - Serve written notice with the required contents", "At least 30 days' written notice, or 90 days if the increase by itself or combined with another increase in the same year is more than 10%; add 5 days if mailed. State the dollar amount, the percentage, the effective date and any banked portion.", "verified", ["S01", "S05", "S35"], "Civil Code 827 requires longer notice in some cases."),
                row("STP-11", "Step 11 - Deliver it properly and keep proof", "Personal delivery or mail under Civil Code 827 and Code of Civil Procedure 1013; keep the notice, proof of service and the license record with the unit file.", "verified", ["S35", "S08", "S55"], "The license need not be attached to the notice."),
                row("STP-12", "Step 12 - Expect tenant-side review and apply the same rule to each unit", "Tenant petitions are free and have no filing deadline for an unlawful increase; a tenant may search the portal for license status. Apply the same written, neutral, dated process to every eligible unit.", "verified", ["S25", "S26", "S08", "S42"], "No rule requires raising both units - see Analysis."),
            ]},
            {"title": "How this applies to the two anonymized units", "columns": COLUMNS, "rows": [
                row("APP-01", "Unit 1 - earliest annual increase under the stated lease date", "With a February 1, 2025 lease start, the first annual increase could have been given on February 1, 2026; any later increase date uses the rate in effect on that date.", "analysis", ["S01", "S02"], "Derived from the official timing rule plus the owner-supplied date; no increase history was supplied."),
                row("APP-02", "Unit 1 - effect of the April 1, 2026 continuing tenancy at $3,995", "Adding an occupant while keeping the same rent does not by itself create a new tenancy or a market-rate reset, and extra rent for an additional occupant is unlawful.", "verified", ["S01", "S17", "S18"], "Whether the April 1, 2026 document restarted the lease or anniversary date is unverified - see Anonymized Case."),
                row("APP-03", "Unit 2 - earliest annual increase under the stated lease date", "With a June 1, 2019 lease start, annual increases were available from June 1, 2020; an increase effective now uses the 1.6% rate plus any properly banked increases.", "analysis", ["S01", "S05", "S02"], "Prior increases since 2019 were not supplied, so no banked amount is computed."),
                row("APP-04", "Banked totals can push one notice above 10%", "If a correctly banked total plus the current annual rate exceeds 10%, the notice must be 90 days rather than 30 days.", "verified", ["S01", "S05", "S35"], "No banked percentage is asserted for either unit. Proposed File 261020 could limit banked increases; see F46 before relying on this timing rule.", "F46"),
                row("APP-05", "An increase effective on or after March 1, 2027", "", "needs review", ["S02"], "The next allowable rate has not been published; blank rather than estimated.", "F27"),
                row("APP-06", "License status for either unit", "", "needs review", ["S07", "S08", "S53"], "Owner has not stated whether each unit is reported and licensed; check the portal.", "T03-F05"),
            ]},
        ],
    },
    "fee": {
        "title": "Rent Board Fee & Other Registrations",
        "description": "The second, separate Rent Board obligation: the annual per-unit fee, its March 1 deadline, penalties, exemptions, the 50% tenant recovery, and City business registration.",
        "sections": [
            {"title": "Fee basics - a separate obligation from the Rent Increase License", "columns": COLUMNS, "rows": [
                row("FEE-01", "Who must pay the Rent Board Fee", "An owner of a residential dwelling unit or guest unit must pay a Rent Board Fee each year unless there is a current exemption on file with the Rent Board or a Homeowners' Exemption on file with the Assessor-Recorder. No individual-owner or small-building exception is stated.", "verified", ["S56"], "This is a fee obligation, not a licence application."),
                row("FEE-02", "What the fee is charged on", "All residential property owners must pay a per-unit fee unless the unit has a current exemption. This includes single-family homes and condominiums, units built after 1979, vacant units, and units occupied by friends or family members.", "verified", ["S56"], "Rent-control coverage is not the test for the fee; exemption is."),
                row("FEE-03", "Amount for the 2026-2027 tax year", "$59.00 per dwelling unit; $29.50 per guest unit (single room occupancy or SRO/residential hotel room). The 50% tenant share is $29.50 per dwelling unit or $14.75 per guest unit.", "verified", ["S56", "S64"], "Form 573 confirms $59.00 per unit for 7/21-6/22 through 7/25-6/26 (flag F40 on the form's title metadata)."),
                row("FEE-04", "Paying the fee does not make you licensed", "SF.gov states that requesting a Rent Board Fee exemption does not satisfy Housing Inventory reporting requirements, and the 2027 informational notice states the reverse: Housing Inventory reporting does not satisfy a fee exemption. The licence arises only from the Housing Inventory report.", "verified", ["S56", "S65", "S53"], "Two separate obligations; no official page found conditions the licence on fee payment (flag F41)."),
                row("FEE-05", "How and where to pay", "Preferred: credit card or electronic check (ACH) online through the Rent Board Portal. In person: Office of the Treasurer and Tax Collector, City Hall Room 140. By mail: San Francisco Rent Board, PO Box 7429, San Francisco, CA 94120-7429. No payments are accepted at the Rent Board office.", "verified", ["S56"], "A dishonoured check or eCheck adds a $50.00 payment failure fee."),
                row("FEE-06", "Statutory scope of Chapter 37A", "Chapter 37A applies to all residential units in San Francisco, including units exempt from the Chapter 37 rent-increase limitations under the Costa-Hawkins Act or Section 37.3(d), with listed exclusions (nonprofit co-ops, licensed care facilities and dormitories, government-regulated rents such as Section 8, tourist-use guest rooms, and units with a current homeowners' exemption).", "verified", ["S63"], "Ordinance text, not just the SF.gov summary."),
            ]},
            {"title": "Deadlines, penalties and the 2026-27 compliance calendar", "columns": COLUMNS, "rows": [
                row("FEE-07", "Due date and late penalties", "The fee is due March 1 each year. A 5% late penalty is added if unpaid by March 1, a further 5% if unpaid by April 1, and a further 5% if unpaid by May 1 - a maximum penalty of 15%.", "verified", ["S56", "S63"], "SF.gov and Section 37A.4 agree on the March/April/May sequence."),
                row("FEE-08", "Delinquency and referral to the Bureau of Delinquent Revenue", "SF.gov states that fees not paid in full by June 1 will be referred to the Bureau of Delinquent Revenue with additional costs added to the principal charges; its timeline instead says a Notice of Delinquent Payment is mailed in July, after which the owner has 30 days before referral. Section 37A.4 says the matter is referred if the fee remains outstanding as of June 1.", "verified", ["S56", "S63"], "The official page is internally inconsistent - see flag F38. Manual confirmation with 311 is advised."),
                row("FEE-09", "Payment failure fee", "If a check or eCheck payment is not honoured by the bank, the payment is null and void and a $50.00 payment failure fee is charged in addition to any late payment penalties.", "verified", ["S56"], "Not recoverable from a tenant."),
                row("FEE-10", "Exemption request window and annual refiling", "Requests for exemption are submitted through the Rent Board Portal between October and early December, and an exemption request must be submitted every year. For the 2027 fee the deadline is Monday, December 14, 2026; units without a valid approved exemption are billed for the fee due March 1, 2027.", "verified", ["S56", "S65"], "Homeowners' Exemption holders do not refile yearly with the Rent Board."),
                row("FEE-11", "2026-27 calendar as published", "October: informational notices mailed, exemption window opens. December 14, 2026: exemption request deadline. January 2027: annual notices (fee invoices) mailed. March 1, 2027: fee due with no penalty; first 5% penalty from March 2. April 1 and May 1: second and third 5% penalties. May 31, 11:59 pm: last day to pay with all penalties. June 1: outstanding bills delinquent. July: notice of delinquent payment mailed.", "verified", ["S56", "S65"], "Housing Inventory reporting is also due March 1, 2027 - see the Step-by-Step License page."),
                row("FEE-12", "This case: fee amount billed and exemption status for the two units", "", "needs review", ["S56", "S64"], "No official billing record or exemption record was supplied; the January 2027 annual notice does not exist yet. Left blank (flag F43).", "F43"),
            ]},
            {"title": "Exemptions are narrow - a rented unit is not exempt", "columns": COLUMNS, "rows": [
                row("FEE-13", "Owner-occupied exemption", "A single-family home, condominium, co-op or apartment unit occupied by an owner of record and not rented at any time may qualify. Vacant units, and units occupied solely by children or close relatives who are not on title as owner, do not qualify. Section 37A.1(f) requires the owner to file an affidavit with the Rent Board.", "verified", ["S56", "S63"], "Both units here are rented, so this exemption would not apply on the owner-supplied facts."),
                row("FEE-14", "Other exemption categories", "Government-controlled or regulated rents (for example Section 8, with documentation), hotel guest rooms designed for tourist use under the Residential Hotel Ordinance, housing in hospitals, monasteries, extended-care facilities and licensed homes for the elderly, dormitories owned by educational institutions, and nonprofit cooperatives owned, occupied and controlled by a majority of residents.", "verified", ["S56", "S63"], "Documentation is required for each category."),
                row("FEE-15", "Homeowners' Exemption route", "An owner whose unit is the primary residence and who already has a Homeowners' Exemption through the Assessor-Recorder should not be assessed the Rent Board fee and may email proof to the Rent Board. The Homeowners' Exemption applies only to the current fee cycle and cannot be applied retroactively unless it appeared on earlier property tax statements.", "verified", ["S56"], "The Rent Board does not process Homeowners' Exemption applications."),
            ]},
            {"title": "Recovering 50% of the fee from tenants - not a rent increase", "columns": COLUMNS, "rows": [
                row("FEE-16", "Maximum recovery and who can be charged", "An owner who has paid the fee in full may recover up to 50% of the annual fee (exclusive of any penalties) from the tenant(s) in occupancy of each unit on November 1 of the applicable tax year. For 2026-2027 that is $29.50 per dwelling unit.", "verified", ["S56", "S62", "S63"], "Only tenants in occupancy on or before November 1 can be billed."),
                row("FEE-17", "How the recovery may be made", "By deducting the amount from the next security-deposit interest payment owed to the tenant, or by billing the tenant directly - but direct billing is allowed only where there is no or insufficient security deposit held, or where the owner already pays the deposit interest annually. The bill must state the amount for that unit, that the purpose is to fund the Rent Board and related administrative costs, and that the amount is due and payable within 30 days of the bill.", "verified", ["S62", "S63"], "Do not net it into the rent figure on a rent-increase notice."),
                row("FEE-18", "Banking an unrecovered fee", "A fee not recovered in the year the owner was first entitled to it may be banked and collected from that tenant in a future year. Only fees that became due after July 25, 1999 may be banked, and the billing statement must show the fee owed for each year and any interest due for each year.", "verified", ["S62", "S63"], "Banking is by deposit-interest deduction except where no or insufficient interest exists."),
                row("FEE-19", "If the tenant does not pay", "A tenant's failure to pay the Rent Board fee is not a just cause for eviction; the landlord must go to Small Claims Court to collect an unpaid fee.", "verified", ["S62"], "The owner remains liable to the Rent Board either way (Section 37A.6(d))."),
                row("FEE-20", "Security-deposit interest rate used for a deduction", "The interest rate owed on deposits for March 1, 2026 through February 28, 2027 is 4.2%. Interest is paid annually on the tenant's annual due date for deposits held over one year and may not be compounded. AB 12 caps a deposit at one month's rent (two months for a qualifying small natural-person owner), for deposits collected on or after July 1, 2024.", "verified", ["S67"], "This is the amount a fee recovery is deducted from."),
                row("FEE-21", "How a 50% recovery is divided among several co-tenants", "", "needs review", ["S62", "S63"], "No official page states how the 50% is allocated among multiple co-tenants of one unit. Left blank rather than inferred (flag F42).", "F42"),
                row("FEE-22", "Recovery is not part of the rent increase", "The fee recovery is a separate statutory billing mechanism tied to the security-deposit interest cycle; it is not an annual or banked rent increase, does not change the base rent, and is not covered by the Rent Increase License precondition for annual/banked increases.", "analysis", ["S62", "S63", "S01"], "Keep the two documents and the two amounts visibly separate."),
            ]},
            {"title": "Other registration question - City business registration", "columns": COLUMNS, "rows": [
                row("FEE-23", "Does an individual small owner need a City business registration certificate?", "A person receiving rental income from one residential structure consisting of fewer than four units, or from one residential condominium, is not - by reason of that fact alone - required to obtain a business registration certificate. Other business activity or payroll expense may require one. A lessor is treated as a separate person for each individual building, the Tax Collector decides what a separate building is and how many units it has, and a return must be filed unless the lessor leases fewer than 4 units in any individual building.", "verified", ["S66"], "Rule only. For this owner it depends on facts not supplied - see the next row."),
                row("FEE-24", "What the Housing Inventory asks for", "Section 37.15(b)(2)(B) requires the business registration number for the unit, if any - so reporting does not assume that every owner has one.", "verified", ["S53"], "Absence of a business registration number is not, by itself, a reporting failure."),
                row("FEE-25", "This case: whether a business registration is required", "", "needs review", ["S66"], "Whether both units are in one structure, whether the owner has other business activity or payroll, and any existing registration were not supplied. Left blank (flag F43).", "F43"),
            ]},
            {"title": "Case arithmetic using the official fee (owner-supplied unit count)", "columns": COLUMNS, "rows": [
                row("FEE-26", "Fee for both rented units, 2026-2027", "2 units x $59.00 = $118.00, due March 1, 2027", "analysis", ["S56", "S64"], "Illustrative only: the unit count is owner-supplied and the official billing record has not been issued. Not a finding."),
                row("FEE-27", "Maximum recoverable from the tenants", "50% x $118.00 = $59.00 in total, $29.50 per unit", "analysis", ["S56", "S62"], "Only after paying in full, only from tenants in occupancy on November 1, 2026, and never any penalty. Whether each tenant qualifies is unverified."),
                row("FEE-28", "Illustration of the maximum statutory penalty", "15% x $118.00 = $17.70, added if the fee is still unpaid after May 1", "analysis", ["S56", "S63"], "Penalties cannot be recovered from tenants. Illustration, not a projection."),
            ]},
        ],
    },
    "requirements": {
        "title": "Full Requirements List",
        "description": "Every active requirement, status and official source link.",
        "sections": [
            {"title": "Requirements", "columns": COLUMNS, "rows": [
                row("REQ-01", "Executive summary", "Published", "verified", ["S01", "S27", "S68"], "Executive Summary page, EXECUTIVE_SUMMARY.md and its source-linked summary rows. Project record only - no government source governs this internal deliverable (flag F37)."),
                row("REQ-02", "Public GitHub Pages site", "Built at repository root", "verified", ["S68", "S69"], "Legacy Pages source main /; deployment status read from the GitHub Pages build API."),
                row("REQ-03", "Collect / organize / analyze full requirements list", "Published", "verified", ["S20"], "This page."),
                row("REQ-04", "Answer all user questions", "Published", "verified", ["S01", "S27", "S68"], "Questions & Answers page, with the substantive answers sourced to S01/S27."),
                row("REQ-05", "Review repo line by line", "Done", "verified", ["S20"], "REPO_REVIEW.md."),
                row("REQ-06", "Verify every row against official sources", "Done; validation script re-checks", "verified", ["S68", "S01"], "SOURCES.md, VERIFICATION.md, data/validation_report.json (project record)."),
                row("REQ-07", "Provide links for manual review", "Every row has official links", "verified", ["S01"], "Official source(s) column."),
                row("REQ-08", "Flag irregularities", "All flagged items published with official source links", "verified", ["S68", "S01"], "Flagged for Review page; the live count is shown on the dashboard and is not hard-coded here (flag F37)."),
                row("REQ-09", "No hallucinations / no inferred values", "Blank cells for unverified values", "verified", ["S01"], "Validation enforces blank + flag."),
                row("REQ-10", "Personal information top priority", "Placeholders only; raw identifiers internal-only", "verified", ["S23"], "Privacy scan in validation."),
                row("REQ-11", "Anonymize all personal information", "Tenant A-F placeholders", "verified", ["S23"], "No real names, initials, contact details or exact address."),
                row("REQ-12", "Keep dates and amounts same", "Preserved", "verified", ["S01"], "February 1, 2025; $3,995; April 1, 2026; June 1, 2019; $3,150."),
                row("REQ-13", "Clean landing page + category subpages", "Published", "verified", ["S68"], "index.html and pages/."),
                row("REQ-14", "Simple dashboard UI", "Published", "verified", ["S68"], "Cards and status badges."),
                row("REQ-15", "All entries/findings in easy-read tables", "Published", "verified", ["S01"], "Tables on every subpage."),
                row("REQ-16", "Analysis / findings", "Published", "verified", ["S42"], "Analysis & Findings page."),
                row("REQ-17", "Clearly labeled Flagged for Review page with source links", "Published", "verified", ["S01"], "pages/flagged.html."),
                row("REQ-18", "Verified source-linked tables", "Published", "verified", ["S01"], "Sources page."),
                row("REQ-19", "PR from integration branch to main", "Done - PRs #1 through #13 merged; each merge result and merge commit is recorded in COORDINATION.md", "verified", ["S68"], "Verified with gh pr view / git log on 2026-11-08; the current session's PR link and merge result are recorded in COORDINATION.md after the merge (flag F19).", "F19"),
                row("REQ-20", "Merged PR + successful Pages deployment", "Done - GitHub Pages API reports status built with legacy source main /; the latest deployment commit is recorded in COORDINATION.md", "verified", ["S69", "S68"], "Read from the GitHub Pages build API on 2026-11-08 (flag F19).", "F19"),
                row("REQ-22", "Step-by-step licensing and notice process", "Published - pages/process.html with 12 numbered steps", "verified", ["S53", "S01", "S35"], "Every step carries official links."),
                row("REQ-23", "Ordinance-level license citations", "Published - Sec. 37.3(a)(1), Sec. 37.15 and Form 571", "verified", ["S21", "S53", "S04"], "Licensing condition is in the ordinance itself."),
                row("REQ-24", "Independent re-verification of the combined data", "Done 2026-11-08 - official pages for the fee, retaliation, exemption and coverage rules re-fetched, sources expanded, validator re-run", "verified", ["S01", "S07", "S53", "S02", "S56", "S57", "S60"], "Recorded in VERIFICATION.md and COORDINATION.md; the source count is computed, not hard-coded."),
                row("REQ-21", "Conservative compliance checklist capable of tenant-lawyer review", "Published", "analysis", ["S01", "S07", "S35", "S42"], "No attorney approval or guarantee."),
                row("REQ-26", "State-vs-local classification of the \"inform the Rent Board\" duty, with ordinance provenance and the source of the 2023 date", "Answered - LOCAL San Francisco ordinance (Administrative Code Sec. 37.15, Ord. 265-20 effective January 18, 2021); 2023 is the local operative date for 1-9 unit buildings (March 1, 2023); SB 567 (2023) is the state law, operative April 1, 2024, with no rent-board reporting duty", "verified", ["S53", "S73", "S90", "S88"], "Published on the Executive Summary (SL-01 to SL-05) and Local Law (LAW-01 to LAW-08); flagged F53."),
                row("REQ-27", "A dedicated Suggestions section so a reviewer can choose the best path before anything is implemented", "Published - 24 reviewable proposals in three groups, each with effort and review status, plus a 5-step review process", "verified", ["S01", "S07", "S35"], "pages/suggestions.html, first-class item in the navigation and dashboard."),
                row("REQ-28", "A clear list of questions, information and answers that must be settled before a reasonable decision, with suggestions for discovering missing information", "Published - 5 ordered gates, 20 open questions, and 4 decision paths; every unverified cell stays blank and names its discovery route", "verified", ["S01", "S07", "S32", "S55"], "pages/decision.html; gaps reuse the existing CASE-V and T03-F flags."),
                row("REQ-25", "Re-check the committee status of File 261020 before serving any banked or capital improvement notice", "Checked 2026-11-10 - 'Pending Committee Action' in the Land Use and Transportation Committee; not law, no enactment", "verified", ["S71", "S72"], "Published on the Rates page as RATE-12 to RATE-18 and flagged F46/F47. Re-check the Legistar record before relying on this status."),
            ]},
        ],
    },
    "rates": {
        "title": "Official Allowable Increase Rates",
        "description": "SF Rent Board rates effective on 2026-11-10 and historical context.",
        "sections": [
            {"title": "Current and recent rates", "columns": COLUMNS, "rows": [
                row("RATE-01", "3/1/26 - 2/28/27", "1.6%", "verified", ["S01", "S02", "S03", "S04"], "Current local rate."),
                row("RATE-02", "3/1/25 - 2/28/26", "1.4%", "verified", ["S02", "S04"], "Historical."),
                row("RATE-03", "3/1/24 - 2/28/25", "1.7%", "verified", ["S02", "S04"], "Historical."),
                row("RATE-04", "3/1/23 - 2/29/24", "3.6%", "verified", ["S04"], "Historical."),
                row("RATE-05", "3/1/22 - 2/28/23", "2.3%", "verified", ["S04"], "Historical."),
                row("RATE-06", "3/1/21 - 2/28/22", "0.7%", "verified", ["S04"], "Historical."),
                row("RATE-07", "3/1/20 - 2/28/21", "1.8%", "verified", ["S04"], "Historical."),
                row("RATE-08", "3/1/19 - 2/29/20", "2.6%", "verified", ["S04"], "Relevant to Unit 2 lease start; no banked amount inferred."),
            ]},
            {"title": "Rate basis", "columns": COLUMNS, "rows": [
                row("RATE-09", "Local formula", "60% of Bay Area CPI-U increase; max 7%", "verified", ["S01", "S21"], "SF Admin Code 37.3."),
                row("RATE-10", "Temporary CPI methodology", "", "needs review", ["S28", "S01"], "Jan. 13, 2026 minutes adopted Version 1 temporary methodology.", "F06"),
                row("RATE-11", "Calculation", "Base rent x rate; no rounding up", "verified", ["S01", "S03", "S04"], "Temporary passthroughs excluded."),
                row("RATE-12", "Proposed banked and capital-improvement cap, File 261020", "Not enacted as of November 10, 2026; proposal would temporarily limit combined banked and capital-improvement increases to 10% per year.", "verified", ["S05", "S71"], "If enacted as currently proposed, applicability would include banked notices and capital-improvement petitions from September 15, 2026. Check current status; see F46.", "F46"),
                row("RATE-13", "Effect of proposed cap on either unit", "", "needs review", ["S05", "S71"], "Not enacted and case-specific histories are unverified; do not treat the proposal as current law.", "F46"),
                row("RATE-14", "Exact Legistar record at fetch (2026-11-10)", "Version 1; introduced 9/15/2026; in control: Land Use and Transportation Committee; STATUS 'Pending Committee Action'; final action, enactment date and enactment number all blank", "verified", ["S71"], "History rows are procedural only: 9/15/2026 assigned under 30-day rule; 9/18/2026 and 9/30/2026 referred to department; 10/7/2026 Youth Commission response received.", "F47"),
                row("RATE-15", "Proposed applicability date vs posting date", "Notice posted November 9, 2026 says the proposal would apply to banked increases noticed on or after September 15, 2026 and to capital improvement petitions filed on or after September 15, 2026", "verified", ["S72", "S71"], "The applicability date precedes both the posting date and the 9/15/2026 introduction. Nothing official says how a notice served between 9/15/2026 and enactment would be treated.", "F47"),
                row("RATE-16", "Duration wording disagrees", "Notice: 'temporarily limit'. Legistar title: 'for the next three years'", "verified", ["S72", "S71"], "Recorded as an inconsistency; neither wording is preferred here.", "F47"),
                row("RATE-17", "Next-year rate (3/1/27 - 2/28/28)", "", "needs review", ["S02", "S01"], "Still not published on either official page when re-checked 2026-11-10; blank rather than estimated.", "F27"),
                row("RATE-18", "How the proposed 10% is measured", "", "needs review", ["S71", "S72"], "No official page states whether the 10% includes or excludes the separate annual allowable increase, or how it treats a banked increase already imposed; blank, not inferred.", "F47"),
            ]},
        ],
    },
    "local": {
        "title": "Local Law - San Francisco",
        "description": "Which layer of government requires the Rent Board report and license (local, not state), then the SF Rent Ordinance, Rent Board rules, licensing, banking and petitions.",
        "sections": [
            {"title": "State, local or federal? Which layer imposes the duty to inform the Rent Board", "columns": COLUMNS, "rows": [
                row("LAW-01", "Is the \"inform the Rent Board before raising rent\" duty a state law or a local law?", "LOCAL - it is a San Francisco ordinance (Administrative Code Chapter 37, added by Ordinance No. 265-20, effective January 18, 2021). No state statute requires an owner to report a rent increase to the SF Rent Board.", "verified", ["S53", "S90", "S21", "S74"], "This is the direct answer to the state-vs-local question. Section 37.15 sits in the local Administrative Code, enforced by the SF Rent Board."),
                row("LAW-02", "Then where does the \"2023 law\" come from?", "THE LOCAL OPERATIVE DATE, not a state statute. Ordinance 265-20 took effect January 18, 2021. Reporting began July 1, 2022 for buildings with 10 or more units, and March 1, 2023 for condominiums and buildings with 1-9 residential units. Rent Board Rule 13.14 applies to increases effective on or after July 1, 2022, and for condominiums and buildings with fewer than 10 units only to increases effective on or after March 1, 2023.", "verified", ["S53", "S73", "S90", "S01"], "A two-unit 1940 building is in the 1-9 unit group, so its date is March 1, 2023. The site does not assert that any specific date was 'passed' in 2023 - only that the small-building duty became operative then."),
                row("LAW-03", "What did the actual 2023 California state law do?", "SB 567 (Chapter 290, Statutes of 2023) amended the statewide Tenant Protection Act: it changed the no-fault just-cause eviction rules and enforcement for the state rent cap (5% plus CPI, or 10%, whichever is lower), and it became operative April 1, 2024. It did not create a duty to report a rent increase to a local rent board.", "verified", ["S88", "S89", "S36"], "Stated as a negative finding from the bill text, not as a prohibition."),
                row("LAW-04", "Does the state rent cap set the number for a covered SF unit?", "NO - by statute and by SF.gov. Civil Code 1947.12(d)(3) excludes housing subject to a local rent control ordinance that restricts annual increases to less than the state formula. SF.gov states AB 1482 does not apply to units already under the SF Rent Ordinance rent-increase limits. The local 1.6% (3/1/26-2/28/27) therefore governs, not the state figure.", "verified", ["S36", "S27", "S01", "S02"], "The state cap only governs units that are NOT under a stricter local ordinance."),
                row("LAW-05", "Does any federal law require informing the Rent Board or cap this rent?", "NO federal requirement found. HUD FMRs and SAFMRs are voucher payment standards for the Housing Choice Voucher programme, not limits on private-market rent, and no federal rent-registration duty was located.", "verified", ["S91", "S43", "S44"], "Federal cap cell remains blank and flagged (F22) because no official general federal private-rent cap exists to cite."),
                row("LAW-06", "Which obligations still apply on top of the local duty?", "Three independent layers apply at once: LOCAL - Housing Inventory report, Rent Increase License, 1.6% annual limit, anniversary date, banked increases, 30/90-day notice, Rent Board Fee. STATE - Civil Code 827 notice rules and Civil Code 1942.5 retaliation limits; the AB 1482 cap applies only to units outside local rent control. FEDERAL - fair housing (FHA, 24 CFR 100.500 disparate impact) applies to how tenants are treated, not to the rent amount.", "verified", ["S01", "S07", "S35", "S57", "S42"], "Local, state and federal duties are cumulative. Complying with one does not satisfy another."),
                row("LAW-07", "Is the license application a separate form from the Housing Inventory report?", "NO - they are the same act. Reporting into the Housing Inventory through the Rent Board Portal generates the license automatically for tenant-occupied units; there is no separate licence application and no charge for it.", "verified", ["S07", "S01", "S53"], "The Rent Board Fee is a different, separate payment (FEE page)."),
                row("LAW-08", "What is the legal consequence of the duty being local rather than state?", "The remedy lives in the local ordinance and Rent Board Rules: under Rule 13.14 an increase purporting to be effective while the landlord is unlicensed renders the entire increase null and void, tested as of the effective date, not the date of service; a tenant may petition the Rent Board at no charge.", "verified", ["S73", "S53", "S25"], "State courts enforce state law; the Rent Board enforces the local ordinance. Different forum, different remedy."),
            ]},
            {"title": "Local rules", "columns": COLUMNS, "rows": [
                row("LOC-01", "Coverage cutoff", "Many units built on/before June 13, 1979 have rent control and eviction protection", "verified", ["S06"], "Verify exact address in PIM; partial exemptions exist."),
                row("LOC-02", "Annual increase", "1.6% once every 12 months on anniversary date", "verified", ["S01", "S02"], "Current rate."),
                row("LOC-03", "Ordinance cap", "60% CPI, max 7%", "verified", ["S21"], "SF Admin Code 37.3."),
                row("LOC-04", "Initial rent", "No limit on first rent for vacant covered unit", "verified", ["S01", "S27"], "Not a reset for an existing tenancy."),
                row("LOC-05", "License", "Current Rent Increase License required before annual/banked increase", "verified", ["S01", "S07", "S08"], "Unlicensed increase may be null/void."),
                row("LOC-06", "Housing Inventory", "Annual report by March 1; license auto-generated for non-owner-occupied units", "verified", ["S07"], "No monetary penalty, but notice unenforceable without license."),
                row("LOC-07", "Banking", "24 full months; add percentages; no compounding/prorating; license", "verified", ["S05"], "Notice must state banked portion."),
                row("LOC-08", "Additional occupants", "No extra rent merely because new/additional roommate moved in", "verified", ["S01", "S17", "S18"], "Even if lease says otherwise."),
                row("LOC-25", "Pending legislation (proposed, not law)", "File 261020 would cap combined banked plus capital improvement increases at 10% per year; version 1, 'Pending Committee Action' on 2026-11-10", "verified", ["S71", "S72"], "Proposed only - creates no current limit. See Rates page RATE-12 to RATE-18 and flags F46/F47.", "F46"),
                row("LOC-09", "Petition grounds", "Capital improvement, O&M, comparable rents, Proposition I, utility, 1.21, bond/water passthroughs", "verified", ["S09"], "Petition/worksheet before notice."),
                row("LOC-10", "Section 6.14", "Unlimited increase only when last original occupant vacates plus timely 6.14 notice", "verified", ["S15", "S16"], "60 days generally reasonable."),
                row("LOC-11", "Costa-Hawkins local view", "Co-tenants not subject; qualifying post-1995 subtenant/assignee only", "verified", ["S15", "S16"], "Legal advice strongly encouraged."),
                row("LOC-12", "Tenant harassment", "Bad-faith coercion/discrimination/privacy interference prohibited", "verified", ["S22"], "Larson footnote conflict flagged."),
                row("LOC-13", "Tenant petition", "No charge, no time limit, ALJ hearing", "verified", ["S25", "S26"], "516C and 518 forms."),
                row("LOC-14", "Ordinance text 37.15", "Owners report under penalty of perjury; condominiums and units in buildings under 10 units report from March 1, 2023 and annually by March 1; compliant owners receive a license to impose rent increases; otherwise the license is suspended and the tenant is not obligated to pay the increased rent for months during the suspension", "verified", ["S53", "S20"], "Added by Ord. 265-20; not a rental registry under Civil Code 1947.7-1947.8."),
                row("LOC-20", "Rent Board Fee is separate from the license", "Every residential dwelling unit owner pays a per-unit fee unless exempt: 2026-2027 is $59.00 per dwelling unit, due March 1, 5% late penalty per month to a 15% maximum; a fee exemption does not satisfy Housing Inventory reporting", "verified", ["S56"], "Two separate obligations; see flag F33."),
                row("LOC-21", "Recovering half the fee", "If the fee is paid in full, 50% ($29.50 per dwelling unit for 2026-2027) may be recovered from tenants in occupancy as of November 1 of the tax year; penalties may not be recovered", "verified", ["S56"], "Not a rent increase; identify it separately on any statement."),
                row("LOC-22", "Units built after June 13, 1979", "Exempt from the rent increase limitations only, if the first Certificate of Occupancy issued after June 13, 1979 and there was no prior residential use; just-cause eviction protection and the Rent Board fee still apply", "verified", ["S59"], "The owner-supplied 1940 year would fall before the cutoff if confirmed."),
                row("LOC-23", "In-law unit or second structure on the lot", "A single-family dwelling with a LEGAL in-law unit is a two-unit building and is not exempt. With an ILLEGAL in-law unit it is also a two-unit building and is not exempt UNLESS both units are rented together as a single tenancy. A single-family dwelling is not exempt if another residential structure is on the same lot", "verified", ["S60"], "Wording corrected 2026-11-08 against the page; two rented units is consistent with coverage (flags F35, F36)."),
                row("LOC-24", "30-day update duty", "A change in the owner or designated manager name or business contact information must be reported within 30 days", "verified", ["S53"], "Separate from the annual March 1 update."),
                row("LOC-15", "License scope", "License rules apply only to rent-controlled units; SF.gov says the license is not required for 6.14/Costa-Hawkins increases or petition-based passthroughs", "verified", ["S08", "S16", "S09"], "Those increases have separate rules and remedies."),
                row("LOC-16", "Housing Inventory data is public", "Submission information is public, including name and business contact details", "verified", ["S07", "S53"], "Privacy consideration before filing."),
                row("LOC-17", "Multiple-year increases", "Landlords are not required to file a petition to impose multi-year banked increases; add the allowable percentages; no compounding; no rounding up", "verified", ["S54"], "30-day notice (35 if mailed)."),
                row("LOC-18", "Where to file and check", "Rent Board Portal account; report inventory; look up license status by address or APN; paper filings by email or office drop-off", "verified", ["S55", "S08"], "Office open 9-4 weekdays; counseling 415-252-4600."),
            ]},
        ],
    },
    "state": {
        "title": "State Law - California",
        "description": "AB 1482, Civil Code 827, 1947.12, 1954.53 and FEHA.",
        "sections": [
            {"title": "State rules", "columns": COLUMNS, "rows": [
                row("ST-01", "AB 1482 SF state-only cap", "8.8% for 8/1/26-7/31/27 (5% + 3.8% CPI)", "verified", ["S27"], "Does NOT apply to units under SF Rent Ordinance limits."),
                row("ST-02", "State cap formula", "5% + CPI or 10% lower; max two increases/12 months", "verified", ["S27", "S36"], "CPI-U April-over-April, rounded nearest 0.1%, Aug. 1 cutoff."),
                row("ST-03", "More-restrictive local exemption", "Units already subject to more restrictive local rent control are exempt from state cap", "verified", ["S27", "S36"], "Local protections remain."),
                row("ST-04", "Just cause", "Required after 12/24 months; lease expiration alone is not just cause", "verified", ["S27"], "Relocation assistance for no-fault evictions."),
                row("ST-05", "Notice", "30 days <=10%; 90 days >10%; 827(c) longer notice controls", "verified", ["S35"], "Personal delivery/mail rules."),
                row("ST-06", "Costa-Hawkins initial rent", "No limit on initial rent for vacant unit", "verified", ["S27", "S37"], "Not a reset for existing tenancy."),
                row("ST-07", "Costa-Hawkins d(2)", "Unlimited increase only to qualifying post-1995 lawful sublessee/assignee after original occupants no longer permanently reside", "verified", ["S37"], "Co-tenants excluded."),
                row("ST-08", "Costa-Hawkins d(3)", "Partial occupancy changes protected when original occupant or qualifying pre-1996 lawful sublessee/assignee remains", "verified", ["S37"], "Critical unresolved Unit 1 issue."),
                row("ST-09", "FEHA classes", "Race, color, religion, sex, gender, gender identity/expression, sexual orientation, marital status, national origin, ancestry, familial status, source of income, disability, veteran/military status, genetic information", "verified", ["S38", "S39"], "Includes perception/association."),
                row("ST-10", "FEHA retaliation", "Dominant-purpose retaliation/harassment/eviction barred", "verified", ["S38"], "Source-of-income and aggregate-income rules."),
                row("ST-11", "Exemption notices", "Required written notice for single-family/condo exemption; REIT/corporate/LLC limits", "verified", ["S27"], "AB 1482 notice language."),
                row("ST-12", "Damages", "Injunctive relief, excess rent, attorney fees, up to treble for willful/oppressive/fraud/malice", "verified", ["S27", "S36"], "State court enforcement; Rent Board cannot enforce state law."),
                row("ST-13", "Retaliation - 180-day bar", "If the landlord retaliates and the tenant is not in default in rent, rent/service changes are restricted within 180 days of the latest applicable enumerated tenantability event: good-faith notice/oral complaint to the landlord, bed-bug notice, qualifying recorded agency complaint, related inspection/citation, proceeding or adverse decision", "verified", ["S57"], "Subdivision (a) may not be invoked more than once in 12 months. Subdivision (d) separately bars retaliation for organizing/lawful rights; (g) preserves lawful cause stated in good faith in the notice/pleading, subject to proof. Case timing is unverified."),
                row("ST-14", "Retaliation - organizing and lawful rights", "Increasing rent to retaliate because a tenant organized or participated in a tenants' association, or lawfully exercised rights, is unlawful", "verified", ["S57"], "The tenant bears the burden of producing evidence under this subdivision."),
                row("ST-15", "Retaliation remedies", "Actual damages; $100-$2,000 punitive damages per retaliatory act only where fraud, oppression or malice is shown; in an action for damages for retaliatory eviction, reasonable attorney's fees to the prevailing party if requested upon initiation", "verified", ["S57"], "Civil Code 1942.5(h)-(j); other statutory/decisional remedies are preserved. Not an automatic fee award for every rent-increase dispute."),
                row("ST-16", "AB 1482 two-unit owner-occupied exemption", "Exempt only for a two-unit structure in a single building where the owner occupied one unit as a principal residence at the beginning of the tenancy and continues in occupancy, and neither unit is an ADU/JADU", "verified", ["S58", "S27"], "Owner occupancy of a unit here was not supplied; no exemption asserted (F34)."),
                row("ST-17", "AB 1482 separate-parcel exemption conditions", "Requires written tenant notice in the statutory form AND that the owner is not a REIT, a corporation, or an LLC with at least one corporate member", "verified", ["S58", "S27"], "An individual owner can meet the owner test, but the notice is still required."),
            ]},
        ],
    },
    "federal": {
        "title": "Federal Law",
        "description": "Fair Housing Act, disparate impact, HUD FMR/SAFMR context and the no-cap finding.",
        "sections": [
            {"title": "Federal rules and context", "columns": COLUMNS, "rows": [
                row("FED-01", "FHA 3604", "Discrimination in rental/terms/services because of race, color, religion, sex, familial status, national origin; disability provisions", "verified", ["S41", "S40"], "Official U.S. Code PDF."),
                row("FED-02", "Disparate impact", "Liability can exist without intent; substantial legitimate nondiscriminatory interest and no less discriminatory alternative", "verified", ["S42"], "Current as of 11/04/2026."),
                row("FED-03", "General federal private-rent cap", "", "needs review", ["S43", "S40", "S41", "S42"], "No official source found; blank and flagged.", "F22"),
                row("FED-04", "HUD FMR definition", "40th-percentile gross rents for standard-quality units", "verified", ["S43", "S44"], "Used for voucher payment standards, not a rent-increase cap."),
                row("FED-05", "FMR effective date", "Federal fiscal-year start, generally October 1", "verified", ["S43"], "FY2027 is current on 2026-11-06."),
                row("FED-06", "SAFMR definition", "ZIP-code FMRs; designated/optional areas; exception payment standards up to 110%", "verified", ["S44"], "Not a private rent cap."),
                row("FED-07", "94122 SAFMR (FY2027 and FY2026)", "$2,370 / $2,770 / $3,410 / $4,460 / $5,020 (FY2027); $2,280 / $2,730 / $3,310 / $4,230 / $4,380 (FY2026)", "verified", ["S83", "S84", "S44"], "Official HUD ZIP calculation pages, re-verified 2026-11-11. Order is efficiency / 1BR / 2BR / 3BR / 4BR. These are 40th-percentile gross-rent voucher benchmarks, not caps or opinions of market rent."),
            ]},
        ],
    },
    "case": {
        "title": "Anonymized Case Facts",
        "description": "Owner-supplied facts published with placeholder tenants and unchanged dates and amounts, separated from what still has to be verified officially.",
        "sections": [
            {"title": "Owner-supplied case facts (anonymized) - not official findings", "columns": OWNER_COLUMNS, "rows": [
                owned("CASE-01", "Location", "Outer Sunset, San Francisco, CA 94122", "ZIP and neighbourhood only; no street address is published."),
                owned("CASE-02", "Exact street address", "Withheld - not published", "Privacy rule: no exact address appears anywhere on this site or in the repository."),
                owned("CASE-03", "Building year", "1940", "Before the June 13, 1979 coverage cutoff; a property-specific check is still required."),
                owned("CASE-04", "Residential units in the building", "2", "Owner describes Unit 1 and Unit 2."),
                owned("CASE-05", "Rent-controlled status", "Owner states both units are rent controlled", "Owner statement, not an official determination."),
                owned("CASE-06", "Rent Increase License / Housing Inventory status", "Not supplied", "Confirm in the Rent Board Portal before serving any notice."),
                owned("CASE-07", "Prior increases, notices, petitions", "Not supplied", "No banked amount is inferred."),
                owned("CASE-08", "Unit 1 - last lease start", "February 1, 2025", "Date preserved exactly."),
                owned("CASE-09", "Unit 1 - rent at last lease start", "$3,995 per month", "Amount preserved exactly."),
                owned("CASE-10", "Unit 1 - initial lease tenants", "Tenant A, Tenant B, Tenant C", "Placeholders replace all three original initials."),
                owned("CASE-11", "Unit 1 - continuing tenancy / current tenants", "Tenant A and Tenant D", "Placeholders; no inference about legal status."),
                owned("CASE-12", "Unit 1 - current tenancy date", "April 1, 2026", "Date preserved exactly."),
                owned("CASE-13", "Unit 1 - rent on April 1, 2026", "$3,995 per month", "Unchanged from the last lease start."),
                owned("CASE-14", "Unit 2 - last lease start", "June 1, 2019", "Date preserved exactly."),
                owned("CASE-15", "Unit 2 - rent at last lease start", "$3,150 per month", "Amount preserved exactly."),
                owned("CASE-16", "Unit 2 - tenants", "Tenant E and Tenant F", "Placeholders replace both initials."),
                owned("CASE-17", "Unit 2 - current rent", "Not supplied", "No current figure is assumed."),
            ]},
            {"title": "Anonymization map (published; no raw initials anywhere)", "columns": OWNER_COLUMNS, "rows": [
                owned("MAP-1", "Tenant A", "Original Unit 1 tenant, still listed on the continuing tenancy", "Role only."),
                owned("MAP-2", "Tenant B", "Original Unit 1 tenant, not on the continuing tenancy", "Role only."),
                owned("MAP-3", "Tenant C", "Original Unit 1 tenant, not on the continuing tenancy", "Role only."),
                owned("MAP-4", "Tenant D", "Unit 1 tenant on the April 1, 2026 tenancy", "Role only."),
                owned("MAP-5", "Tenant E", "Unit 2 tenant since June 1, 2019", "Role only."),
                owned("MAP-6", "Tenant F", "Unit 2 tenant since June 1, 2019", "Role only."),
            ]},
            {"title": "What still has to be verified from an official source", "columns": COLUMNS, "rows": [
                row("CASE-V1", "Coverage of the exact address", "", "needs review", ["S06", "S32"], "Check the address in the Planning Property Information Map; no exact address is published here.", "T03-F03"),
                row("CASE-V2", "Official building-year record", "", "needs review", ["S32", "S06"], "Owner says 1940; the official record was not obtained in this session.", "T03-F03"),
                row("CASE-V3", "Current Rent Increase License status", "", "needs review", ["S07", "S08", "S53"], "Not supplied; confirm in the Rent Board Portal for the effective date of any increase.", "T03-F05"),
                row("CASE-V4", "Anniversary dates and prior increase history", "", "needs review", ["S01", "S05"], "Not supplied; see F28 for the Section 6.14 and anniversary-date question.", "T03-F05"),
                row("CASE-V5", "Unit 1 continuing occupant legal status (co-tenant, subtenant, assignee)", "", "needs review", ["S15", "S16", "S37"], "Not supplied; no market-rate reset is recommended.", "T03-F04"),
                row("CASE-V6", "Whether a new tenancy actually began on April 1, 2026", "", "needs review", ["S16", "S01"], "Not supplied; affects the anniversary date and any Costa-Hawkins analysis.", "T03-F04"),
                row("CASE-V7", "Whether the last original Unit 1 tenant still permanently resides there", "", "needs review", ["S16", "S28"], "Not supplied; Section 6.14 requires the last original occupant to have vacated.", "T03-F04"),
                row("CASE-V8", "Section 6.14 notice served on the occupant added April 1, 2026", "", "needs review", ["S16", "S15"], "Not supplied; a written 6.14 notice within a reasonable time (generally 60 days) is required for a later unlimited increase.", "F28"),
                row("CASE-V9", "Banked increase eligibility for either unit", "", "needs review", ["S05"], "Needs 24 full months without any increase; history unknown.", "T03-F05"),
                row("CASE-V10", "Privacy of the Housing Inventory filing", "Inventory submission information is public, including owner name and business contact information", "verified", ["S07", "S53"], "Relevant before filing, but the filing is required to obtain the license."),
            ]},
        ],
    },
    "calculations": {
        "title": "Illustrative Calculations",
        "description": "Owner-supplied amounts multiplied by official rates only; arithmetic, not a recommendation.",
        "sections": [
            {"title": "Current 1.6% rate", "columns": COLUMNS, "rows": [
                row("CALC-01", "Unit 1 $3,995 x 1.6%", "$63.92 increase; $4,058.92 illustrative new base rent", "analysis", ["S01", "S02", "S03", "S04"], "Eligibility, license, notice and anniversary unverified."),
                row("CALC-02", "Unit 2 $3,150 x 1.6%", "$50.40 increase; $3,200.40 illustrative new base rent", "analysis", ["S01", "S02", "S03", "S04"], "Eligibility, license, notice and anniversary unverified."),
            ]},
            {"title": "Historical 1.4% rate", "columns": COLUMNS, "rows": [
                row("CALC-03", "Unit 1 $3,995 x 1.4%", "$55.93 increase; $4,050.93 illustrative new base rent", "analysis", ["S02", "S04"], "Historical comparison only."),
                row("CALC-04", "Unit 2 $3,150 x 1.4%", "$44.10 increase; $3,194.10 illustrative new base rent", "analysis", ["S02", "S04"], "Historical comparison only."),
            ]},
            {"title": "Banked increases", "columns": COLUMNS, "rows": [
                row("CALC-05", "Banked total for either unit", "", "needs review", ["S05", "S04"], "Prior increases and anniversary dates not supplied; blank.", "T03-F05"),
                row("CALC-06", "Rounding", "No rounding up; base rent only", "verified", ["S01"], "Temporary passthroughs excluded."),
                row("CALC-07", "Official rate series behind any banked amount", "1.8% (3/1/20-2/28/21), 0.7% (3/1/21-2/28/22), 2.3% (3/1/22-2/28/23), 3.6% (3/1/23-2/29/24), 1.7% (3/1/24-2/28/25), 1.4% (3/1/25-2/28/26), 1.6% (3/1/26-2/28/27)", "verified", ["S04", "S02"], "Banked percentages are added, then applied to current base rent; they are never compounded or prorated."),
                row("CALC-08", "Unit 2 - conditional illustration if nothing was ever raised", "11.5% of skipped years (1.8 + 0.7 + 2.3 + 3.6 + 1.7 + 1.4) plus 1.6% = 13.1%; $3,150 x 13.1% = $412.65, or $3,562.65", "analysis", ["S05", "S04", "S02"], "Conditional arithmetic only: it assumes no increase since June 1, 2019, which the owner has not confirmed. A combined increase above 10% also requires 90 days' written notice, and the effective date must fall on or before 2/28/2027 for the 1.6% component to be the published rate. Pending File 261020 could affect this illustrative calculation; a 90-day notice alone does not establish legality. See F46.", "F30"),
                row("CALC-09", "Unit 1 - banked amount", "", "needs review", ["S05", "S01"], "The lease began February 1, 2025 and no notice history was supplied, so nothing can yet satisfy the 24-full-month banking rule.", "T03-F05"),
            ]},
            {"title": "Notice deadlines if the increase is 1.6%", "columns": COLUMNS, "rows": [
                row("CALC-10", "Effective February 1, 2027, served in person", "Notice delivered by January 2, 2027", "analysis", ["S01", "S35"], "30 days before the effective date; the 1.6% rate is in effect through 2/28/2027."),
                row("CALC-11", "Effective February 1, 2027, served by mail", "Notice mailed by December 28, 2026", "analysis", ["S01", "S35"], "Mailed notice gets 5 extra days and Civil Code 1013 extension rules apply."),
            ]},
        ],
    },
    "compliance": {
        "title": "Correct Tenant-Notice Method",
        "description": "Conservative compliance checklist capable of tenant-lawyer review; not attorney approval.",
        "sections": [
            {"title": "Before any increase", "columns": COLUMNS, "rows": [
                row("CHK-01", "Verify coverage", "Check exact address in SF Planning PIM; confirm exemptions", "verified", ["S06", "S32"], "Exact address not supplied in this case."),
                row("CHK-02", "Verify license", "Current Rent Increase License on effective date", "verified", ["S01", "S07", "S08"], "Tenant portal lookup."),
                row("CHK-03", "Verify 12 months / anniversary", "At least 12 months since last increase", "verified", ["S01"], "Use rate in effect on increase date."),
                row("CHK-04", "Verify banked amounts", "Only if >=24 full months without any increase; add percentages; no compounding/prorating", "verified", ["S05"], "Not inferred here."),
                row("CHK-05", "Written notice timing", "30 days; 90 days if >10% alone/combined in same year; +5 days if mailed", "verified", ["S01", "S05", "S35"], "827(c) longer notice controls."),
                row("CHK-06", "Notice contents", "Dollar amount, percentage, effective date; banked portion if any", "verified", ["S01", "S05"], "No rounding up."),
                row("CHK-07", "Delivery", "Personal delivery or mail under Civil Code 827 / CCP 1013", "verified", ["S35"], "Keep proof of service."),
                row("CHK-08", "Petition grounds", "Petition/worksheet before notice when required", "verified", ["S09", "S10", "S11", "S12", "S13", "S14"], "Otherwise notice may be void."),
                row("CHK-09", "Neutral policy", "Identical written neutral policy, dates, calculations and recordkeeping for each eligible unit", "analysis", ["S42", "S38"], "Document neutral eligibility reasons if only one unit is raised."),
                row("CHK-10", "Legal review", "Capable of tenant-lawyer review; no approval claimed", "analysis", ["S23", "S24", "S25"], "Free counseling is not legal advice; TRC covers eviction proceedings."),
                row("CHK-11", "License before notice", "Report into the Housing Inventory and confirm a current license for each unit and each effective date", "verified", ["S53", "S07", "S55"], "Unlicensed notices may be void or unenforceable."),
                row("CHK-12", "Keep the license record", "File the license record and a dated portal lookup with the notice and proof of service", "analysis", ["S08", "S55"], "Evidence if the increase is challenged."),
                row("CHK-13", "90-day notice if the total exceeds 10%", "90 days when the increase alone or combined with another increase in the same year is more than 10%", "verified", ["S01", "S05", "S35"], "The 90-day notice rule is not permission to impose an increase: pending File 261020 could affect banked increases (F46).", "F46"),
                row("CHK-14", "Check the retaliation clock", "Before serving notice, review tenantability complaints and other qualifying events within the prior 180 days and consult counsel about retaliation risks", "verified", ["S57", "S22"], "Section 1942.5(a) addresses retaliatory increases with conditions; subsection (g) addresses lawful cause. Other retaliation rules may also apply."),
                row("CHK-15", "Keep the fee separate", "Pay or confirm the Rent Board Fee ($59.00 per dwelling unit for 2026-2027, due March 1) and, if recovering 50%, show it as a separate fee recovery rather than folding it into the rent increase", "verified", ["S56"], "The fee is not part of base rent."),
                row("CHK-16", "Match each notice to a license on its effective date", "Check the portal license status for the specific effective date of each notice, for each unit, including any prior year", "verified", ["S53", "S08", "S55"], "A license now does not cure a notice effective before it existed."),
                row("CHK-17", "Re-serve rather than backdate", "If a notice went out unlicensed, report, confirm the license, and serve a new notice with a compliant effective date", "analysis", ["S08", "S53", "S35"], "Do not treat an unenforceable notice as effective."),
                row("CHK-18", "Work through the Notice Worksheet", "The Notice Worksheet page lists the pre-service gates, required notice contents, service rules and a per-tenant service log, each row linked to its official source", "verified", ["S01", "S35", "S78"], "Published from the B87 official-source kit (research/b87_notice_kit); case cells stay blank until verified."),
            ]},
        ],
    },
    "reasons": {
        "title": "Reasonable Reasons for an Increase",
        "description": "Official grounds that can support an increase; mere below-market rent is not enough.",
        "sections": [
            {"title": "Supported grounds", "columns": COLUMNS, "rows": [
                row("REAS-01", "Annual CPI-based allowable increase", "1.6% effective 3/1/26-2/28/27", "verified", ["S01", "S02", "S04"], "Once every 12 months; license and notice."),
                row("REAS-02", "Properly banked skipped/partial increases", "24 full months; add percentages", "verified", ["S05"], "No banked amount inferred here."),
                row("REAS-03", "Capital improvement petition", "Petition before notice; not base rent; discontinue after amortization", "verified", ["S09", "S12"], "Hardship application available."),
                row("REAS-04", "Operating & maintenance petition", "Up to 7% additional base rent; two-year comparison", "verified", ["S09", "S11"], "Petition before notice."),
                row("REAS-05", "Comparable-rent special circumstances", "Extraordinary circumstances; mere long-standing below-market rent is NOT enough", "verified", ["S09", "S10"], "One-time tenancy reset; petition before notice."),
                row("REAS-06", "Utility passthrough", "Dollar-for-dollar; petition/worksheet before notice; 12 months", "verified", ["S09", "S13"], "Not base rent."),
                row("REAS-07", "Section 1.21 no tenant in occupancy", "Petition before notice; otherwise void", "verified", ["S09", "S14"], "Not applicable if any qualifying tenant resides."),
                row("REAS-08", "Proposition I rent history / bond / water revenue bond passthroughs", "Rent Board petition/worksheet grounds", "verified", ["S09"], "Follow specific form instructions."),
                row("REAS-09", "New or additional roommate", "", "needs review", ["S01", "S17", "S18"], "Not a lawful reason; blank and flagged.", "T03-F04"),
                row("REAS-10", "Assumed vacancy decontrol / market-rate reset", "", "needs review", ["S15", "S16", "S37", "S28"], "Not recommended without official eligibility and legal review.", "T03-F04"),
            ]},
        ],
    },
    "corporate": {
        "title": "How Large Real Estate Corporations Handle Increases",
        "description": "Official SEC EDGAR figures; portfolio-level evidence only, not SF-specific or a legal benchmark.",
        "sections": [
            {"title": "SEC filing evidence", "columns": COLUMNS, "rows": [
                row("CORP-01", "Independence Realty Trust Q4 2025", "Same-store new leases -3.7%; renewal 2.9%; blended 0.8%; occupancy 95.4%; retention 61.4%", "verified", ["S48"], "Multifamily REIT; not SF-specific."),
                row("CORP-02", "Independence Realty Trust Q3 2025", "Same-store new leases -3.5%; renewal 2.6%; blended 0.1%", "verified", ["S48"], "Not SF-specific."),
                row("CORP-03", "IRT 2025 value-add", "2,003 renovations; average $251/month increase over unrenovated comparables", "verified", ["S48"], "Not SF-specific."),
                row("CORP-04", "Invitation Homes 2025 total portfolio", "Renewal +4.6%; new -0.8%", "verified", ["S49"], "Single-family rental REIT; not SF-specific."),
                row("CORP-05", "Invitation Homes 2024 total portfolio", "Renewal +4.9%; new +1.0%", "verified", ["S49"], "Not SF-specific."),
                row("CORP-06", "All large corporations generalization", "", "needs review", ["S48", "S49"], "No official source proves what all large corporations do.", "F23"),
                row("CORP-07", "Essex Property Trust - San Francisco County, Q4 2025", "Average monthly rental rate $2,966 vs $2,897 in Q4 2024 (+2.4%); 1,356 apartment homes; financial occupancy 95.5%; gross revenues +2.0%", "verified", ["S85"], "Official Form 8-K Exhibit 99.1, page S-9, re-verified 2026-11-11. County-level same-property data; the filing does not say how individual rents were set or whether any unit is rent-controlled."),
                row("CORP-08", "Essex Property Trust - blended rate growth, FY2025", "Blended same-property net effective rate growth +2.5% for FY2025, portfolio-wide", "verified", ["S85"], "Taken from footnote 7 of the same filing, which defines the measure; portfolio-wide and not San Francisco-specific. Quarterly tradeout columns are not published here because their column labels were not captured unambiguously."),
                row("CORP-09", "Equity Residential - FY2025 Form 10-K", "", "needs review", ["S86"], "Filing confirmed retrievable 2026-11-11; no San Francisco-specific figure extracted, so none is published. See F15.", "F15"),
            ]},
        ],
    },
    "individual": {
        "title": "How Individual SF Property Owners Handle Increases",
        "description": "Official local rules and narrow Rent Board workload evidence; no generalization claimed.",
        "sections": [
            {"title": "Official evidence", "columns": COLUMNS, "rows": [
                row("IND-01", "Ordinary path", "Annual allowable increase, license, 12-month anniversary, written notice", "verified", ["S01", "S07", "S35"], "Same local rules apply to individual owners."),
                row("IND-02", "Formal petitions June 2024", "23 landlord petitions / 154 units", "verified", ["S29"], "Narrow descriptive count."),
                row("IND-03", "Capital improvement petitions June 2024", "18 petitions / 148 units", "verified", ["S29"], "Corrected 2026-11-07 against the source PDF: 18 capital-improvement petitions / 148 units; the 19 / 149 subtotal includes 1 Costa-Hawkins petition (F29)."),
                row("IND-04", "Tenant petitions / eviction notices June 2024", "73 tenant petitions / 73 units; 89 eviction notices", "verified", ["S29"], "Not proof of typical practice."),
                row("IND-05", "All individual SF owners generalization", "", "needs review", ["S29"], "No official source proves what all individual owners do.", "F23"),
            ]},
        ],
    },
    "market": {
        "title": "Market Context - HUD FMR / SAFMR",
        "description": "HUD figures are voucher standards, not rent caps or legal bases for an increase.",
        "sections": [
            {"title": "FY2027 current federal fiscal year", "columns": COLUMNS, "rows": [
                row("MKT-01", "San Francisco, CA HMFA 0 BR", "$2,574", "verified", ["S47", "S43"], "FY2027 FMR; current federal FY on 2026-11-06."),
                row("MKT-02", "San Francisco, CA HMFA 1 BR", "$3,003", "verified", ["S47", "S43"], "FY2027 FMR."),
                row("MKT-03", "San Francisco, CA HMFA 2 BR", "$3,697", "verified", ["S47", "S43"], "FY2027 FMR."),
                row("MKT-04", "San Francisco, CA HMFA 3 BR", "$4,832", "verified", ["S47", "S43"], "FY2027 FMR."),
                row("MKT-05", "San Francisco, CA HMFA 4 BR", "$5,439", "verified", ["S47", "S43"], "FY2027 FMR."),
                row("MKT-08", "94122 FY2027 Small Area FMR", "$2,370 / $2,770 / $3,410 / $4,460 / $5,020", "verified", ["S83", "S44"], "Official HUD ZIP calculation page, re-verified 2026-11-11. Efficiency / 1BR / 2BR / 3BR / 4BR; 40th-percentile gross-rent benchmark, not a cap."),
            ]},
            {"title": "FY2026 historical", "columns": COLUMNS, "rows": [
                row("MKT-06", "San Francisco, CA HMFA 0-4 BR", "$2,485 / $2,977 / $3,604 / $4,604 / $4,772", "verified", ["S45", "S43"], "FY2026 revised effective May 21, 2026; historical as of 2026-11-06."),
                row("MKT-07", "94122 FY2026 Small Area FMR", "$2,280 / $2,730 / $3,310 / $4,230 / $4,380", "verified", ["S84", "S44"], "Official HUD ZIP calculation page, re-verified 2026-11-11. Efficiency / 1BR / 2BR / 3BR / 4BR; historical benchmark, not a cap."),
                row("MKT-09", "FMR/SAFMR as rent cap", "No - voucher payment standards only", "verified", ["S43", "S44"], "Not a legal basis for a private rent increase."),
                row("MKT-10", "Use of the 94122 SAFMR for these units", "", "needs review", ["S83", "S84", "S43"], "Comparing a SAFMR with a contract rent would need each unit's bedroom count and utility treatment, which are not published; no comparison, percentage or 'market rent' figure is asserted.", "F52"),
            ]},
        ],
    },
    "questions": {
        "title": "All User Questions Answered",
        "description": "Direct answers with official source links; blanks where official confirmation is absent.",
        "sections": [
            {"title": "Questions and answers", "columns": ["Question", "Answer", "Status", "Official source(s)", "Notes / flag"], "rows": [
                row("Q-01", "What are reasonable/normal rental increases under local, state and federal law?", "Local 1.6% for covered units; state-only AB 1482 8.8% does not replace SF limits; no official general federal private-rent cap found. HUD FMR is not a cap.", "verified", ["S01", "S27", "S43", "S44"], "Federal cap blank and flagged."),
                row("Q-02", "How do big real estate corporations handle increases?", "Public REITs disclose lease-over-lease rates in SEC filings: IRT Q4 2025 renewal 2.9%, new -3.7%, blended 0.8%; Invitation Homes 2025 renewal 4.6%, new -0.8%.", "verified", ["S48", "S49"], "Portfolio-level, not SF-specific; no generalization."),
                row("Q-03", "How do individual SF property owners handle increases?", "Official rules require the annual allowable increase, license, 12-month timing and notice; June 2024 Rent Board workload shows 23 landlord petitions/154 units.", "verified", ["S01", "S07", "S29"], "Narrow formal-petition evidence only."),
                row("Q-04", "What is the correct tenant-notice method?", "Written 30-day notice; 90-day if >10% alone/combined in same year; +5 days if mailed; dollar amount, percentage, effective date; banked portion if any; license first; 827 delivery rules.", "verified", ["S01", "S05", "S35", "S07"], "Conservative checklist capable of lawyer review."),
                row("Q-05", "What are reasonable reasons for increases?", "Annual CPI-based allowable increase, properly banked skipped/partial increases, and Rent Board-approved petition/worksheet passthroughs; not extra rent merely because a roommate moved in.", "verified", ["S01", "S05", "S09", "S10", "S18"], "Mere long tenure below market is not extraordinary."),
                row("Q-06", "What tenant-friendly advocate/lawyer scrutiny exists?", "Free Rent Board counseling (not legal advice), tenant counselors, eviction-court free legal help, Tenant Right to Counsel for eviction proceedings, and tenant petitions before an ALJ.", "verified", ["S23", "S24", "S25", "S30", "S31"], "No official general rent-increase attorney approval service found."),
                row("Q-07", "Can increases pass a SF tenant lawyer's review as reasonable, normal business practice, nondiscriminatory and lawful?", "", "needs review", ["S23", "S24", "S25", "S42"], "No official source can certify approval; only a conservative checklist capable of review.", "T03-F08"),
                row("Q-08", "Should one unit or both be raised to avoid discrimination lawsuits/inquiries?", "", "needs review", ["S41", "S42", "S38"], "No official rule requires both; use identical neutral criteria and document eligibility reasons if only one is raised.", "F22"),
                row("Q-09", "Is a market-rate reset available after Unit 1's roommate change?", "", "needs review", ["S15", "S16", "S37", "S28"], "Continuing occupant legal status and last-original-occupant facts unverified; no reset recommended.", "T03-F04"),
                row("Q-11", "Do individual owners (not corporations) need to apply for the Rent Board license and inform the Rent Board before notifying tenants?", "Yes. A current Rent Increase License must be on file before an annual or banked increase takes effect, and all owners must report into the Housing Inventory first; no individual-owner or small-building exemption was found (buildings under 10 units report from March 1, 2023).", "verified", ["S01", "S07", "S08", "S53"], "See the Step-by-Step License page."),
                row("Q-12", "Is there a separate form to tell the Rent Board about each individual increase?", "The official pages describe only the annual Housing Inventory report as the route to the license; no separate filing of the increase notice is described, and the license need not be included with the notice.", "verified", ["S07", "S53", "S01"], "Absence of a stated requirement; counselor confirmation suggested."),
                row("Q-13", "What happens if a notice goes out without a current license?", "The increase may be null and void, the tenant may be entitled to a refund and may petition the Rent Board, which can schedule an Administrative Law Judge hearing.", "verified", ["S08", "S53", "S25", "S26"], "A tenant summary petition also prompts a letter to the landlord."),
                row("Q-14", "Does the added roommate allow a market-rate reset?", "No, not by itself: extra rent for an additional occupant is unlawful, and a 6.14/Costa-Hawkins increase requires specific facts plus a timely written 6.14 notice. Those facts are unverified here.", "verified", ["S01", "S18", "S16", "S37"], "No reset recommended; see flag F28."),
                row("Q-15", "Is the Rent Board Fee the same thing as the Rent Increase License?", "No. They are separate obligations. The license comes from Housing Inventory reporting and there is no charge for that reporting; the fee is a separate per-unit annual payment (2026-2027: $59.00 per dwelling unit, due March 1, with a 5% monthly late penalty to a 15% maximum). SF.gov states expressly that requesting a fee exemption does not satisfy Housing Inventory reporting.", "verified", ["S56", "S07", "S53"], "Paying the fee is not a substitute for the license; see flag F33."),
                row("Q-16", "Can part of the Rent Board Fee be charged to the tenants?", "Yes, if the fee is paid in full: 50% of the fee, i.e. $29.50 per dwelling unit for 2026-2027, may be recovered from tenants in occupancy as of November 1 of the applicable tax year. Penalties may not be recovered.", "verified", ["S56"], "This is a fee recovery, not a rent increase; keep it separately identified."),
                row("Q-17", "How long do I have to report a Housing Inventory change, and what if I already served a notice?", "Unit information is updated annually by March 1, and a change in the owner or manager name or business contact information must be updated within 30 days. If a notice already went out with no license on file, report first, then re-serve the notice so the effective date falls after the license is on file: a notice is unenforceable for an effective date on which no license was on file, and an unlicensed increase may be null and void.", "verified", ["S53", "S07", "S08"], "Whether any notice has already been served here is unverified."),
                row("Q-18", "Can an increase during a repair dispute or after a complaint be retaliatory?", "Yes, that is a separate state-law risk. Section 1942.5(a) restricts retaliatory increases within 180 days of specified tenantability events when the tenant is not in rent default, subject to the statute’s conditions and lawful-cause provision. Retaliation for tenant organizing or exercising lawful rights is separately barred. Remedies have additional conditions, including fraud, oppression or malice for punitive damages.", "verified", ["S57", "S22", "S42"], "Timing versus any open habitability complaint is unverified; this is not a legal opinion."),
                row("Q-19", "Are these two units exempt from AB 1482 because the owner lives in one?", "Only if the owner occupied one unit as a principal residence when the tenancy began and continues in occupancy, and neither unit is an ADU/JADU. That fact was not supplied, so no exemption is asserted. Independently, AB 1482's rent cap does not apply where the unit is already under the SF Rent Ordinance limits, which are stricter.", "verified", ["S58", "S60", "S27"], "Conditional; see flags F34 and F35."),
                row("Q-20", "Does an in-law unit or a second structure change whether these units are covered?", "It can. SF.gov states that a single-family dwelling with a legal in-law unit is a two-unit building and is not exempt, that with an illegal in-law unit it is also a two-unit building and is not exempt unless both units are rented together as a single tenancy, and that a single-family dwelling is not exempt if another residential structure is on the same lot. Two rented units is consistent with Rent Ordinance coverage, but the official lot and building record was not supplied.", "verified", ["S60", "S59", "S06"], "Verify the lot in the Property Information Map; see flags F35 and F36."),
                row("Q-21", "Do the tenants have to keep accepting increases, or can they challenge each one?", "They can challenge. A tenant may file an unlawful-rent-increase petition with no filing fee and no time limit, and the matter can go to an Administrative Law Judge. Tenant-side free legal help is documented for eviction proceedings (Eviction Defense Collaborative line and Tenant Right to Counsel), not as a general pre-approval service for rent increases.", "verified", ["S25", "S61", "S30"], "No official source offers approval of an increase before it is served."),
                row("Q-10", "Is any increase guaranteed lawful or lawsuit-proof?", "No. No attorney approval or guarantee of no complaint/inquiry/lawsuit is claimed.", "analysis", ["S23", "S24", "S42"], "Conservative compliance checklist only."),
            ]},
            {"title": "What is still missing, and how to find it", "columns": COLUMNS, "rows": [
                row("Q-22", "Which open questions can an official record answer, and which only you can answer?", "The Suggestions & Review page publishes a missing-information register (SUG-18) that names, for every open item, what is missing, which official source would resolve it, how to obtain it, who must supply it and which decision it blocks, plus a separate list of the facts only the owner can supply (SUG-19): the last original occupant in each unit, the date occupancy began, whether a 6.14 notice was served, each unit's anniversary date, the full lease and notice history, square footage and bedroom and bathroom counts, whether either unit is an in-law unit, whether the owner occupies one unit, and whether each tenant was in occupancy on November 1 for the fee-recovery test.", "verified", ["S07", "S16", "S56", "S24", "S55", "S32"], "Published as proposals for review, not as a determination about either unit."),
                row("Q-23", "How do I put the open questions to the Rent Board efficiently?", "Counseling is free, available in Spanish, Cantonese and Mandarin with interpretation for other languages, and cannot give legal advice, so the questions have to be written down first; calls are generally limited to 5 minutes. The Suggestions & Review page publishes a printable call script (SUG-20) containing only the open questions, with the counselor's published phone number and office hours, and a pre-decision gate sequence (SUG-21) listing the questions to answer before any notice is dated.", "verified", ["S24", "S07", "S55", "S16"], "The Rent Board states it will tell you when a question is one that should be answered by a lawyer."),
                row("Q-24", "Where do the proposed improvements to this site live?", "On the Suggestions & Review page (`pages/suggestions.html`): 27 proposals in four groups - compliance gates, evidence and defensibility, discovering the missing information, and internal site quality. Every row carries the official rule that motivates it, an effort and impact estimate, and a Decision cell starting at Review, with a blank review checklist for recording Accept, Reject or Defer before anything is implemented.", "verified", ["S68"], "Project-record source: the proposals are about this site, and no legal finding rests on them."),
            ]},
        ],
    },
    "analysis": {
        "title": "Analysis & Findings",
        "description": "Source-linked analysis, including discrimination, one-vs-both, and conservative checklist.",
        "sections": [
            {"title": "Findings", "columns": COLUMNS, "rows": [
                row("AN-01", "Normal local increase", "1.6% or less on each eligible unit", "verified", ["S01", "S02"], "Once every 12 months; license; notice."),
                row("AN-02", "State cap is not a substitute", "AB 1482 8.8% does not apply to SF Rent Ordinance rent-controlled units", "verified", ["S27", "S36"], "Local protections remain."),
                row("AN-03", "No federal rent cap found", "", "needs review", ["S43", "S40", "S41", "S42"], "HUD FMR/SAFMR are voucher standards.", "F22"),
                row("AN-04", "Disparate-impact risk", "Liability can exist without intent; neutral criteria and no less discriminatory alternative matter", "verified", ["S42"], "Current eCFR as of 11/04/2026."),
                row("AN-05", "FEHA broader classes", "Source of income, retaliation, perception/association and aggregate-income rules apply", "verified", ["S38", "S39"], "State overlay."),
                row("AN-06", "Local harassment overlay", "Bad-faith coercion/discrimination prohibited", "verified", ["S22"], "Larson footnote flagged."),
                row("AN-07", "Unit 1 roommate change", "Not a basis for extra rent; vacancy-decontrol eligibility unverified", "verified", ["S01", "S17", "S18", "S15", "S16", "S37"], "No market-rate reset recommended."),
                row("AN-08", "One vs both", "Raising both is not officially required; identical neutral policy reduces disparate-treatment optics", "analysis", ["S41", "S42", "S38"], "Document neutral eligibility/anniversary reasons; no guarantee."),
                row("AN-09", "Unit 2 long tenure", "Mere below-market rent is not extraordinary circumstances", "verified", ["S10"], "Special Circumstances petition required for comparable-rent reset."),
                row("AN-10", "Banked increases", "Cannot be inferred because rent history is unverified", "verified", ["S05"], "Blank and flagged."),
                row("AN-11", "Corporate figures", "Portfolio-level disclosures are evidence of practice, not legal benchmarks", "verified", ["S48", "S49"], "Not SF-specific."),
                row("AN-12", "Individual figures", "June 2024 workload is narrow formal-petition evidence", "verified", ["S29"], "No generalization."),
                row("AN-13", "Tenant-lawyer review", "Checklist capable of review; no approval claimed", "analysis", ["S23", "S24", "S25", "S30", "S31"], "TRC is eviction-focused."),
                row("AN-14", "Conservative compliance checklist", "At most ordinary 1.6% annual allowable increase (or less) on each eligible unit, identical written neutral policy, license, notice, dates, calculations, recordkeeping", "analysis", ["S01", "S07", "S35", "S42"], "No guarantee of no complaint/lawsuit."),
                row("AN-15", "Flagged items do not block", "All flagged items published with official source links", "verified", ["S01", "S68"], "Needs review does not block the merge; the live count is shown on the dashboard (flag F37)."),
                row("AN-25", "What a tenant-side reviewer would test", "1) current license on the effective date, 2) correct rate for that date, 3) 12 months since the last increase, 4) base rent only and no rounding up, 5) notice contents, lead time and delivery, 6) no extra charge for an added roommate, 7) no retaliation or bad-faith harassment", "analysis", ["S01", "S05", "S07", "S35", "S17", "S22"], "Each item is checkable against the official pages linked here; passing them is not a certification of lawfulness."),
                row("AN-16", "The license is a precondition, not paperwork", "An increase noticed while the unit is unlicensed may be null and void or unenforceable with refund exposure, and the Rent Board issues noncompliance notices; its January 2026 minutes record more than 23,000 licenses", "verified", ["S08", "S53", "S28"], "Checks should look at the effective date, not today's status."),
                row("AN-17", "Individual owners are not exempt", "The requirement follows rent-controlled status; there is no owner-size exemption, and buildings under 10 units have reported since March 1, 2023", "verified", ["S07", "S53", "S08"], "Direct answer to the owner's question."),
                row("AN-18", "A banked total can exceed 10%", "Adding a correctly banked percentage to the current annual increase can push one notice above 10%, which then needs 90-day notice", "verified", ["S01", "S05", "S54"], "No banked amount is asserted for either unit; pending File 261020 could affect banked increases (F46).", "F46"),
                row("AN-19", "The filing itself is public", "Housing Inventory information is public, so reporting publishes the owner's name and business contact information", "verified", ["S07", "S53"], "Privacy consideration; the filing is still required for a license."),
                row("AN-26", "Two distinct registrations with the Rent Board", "Housing Inventory reporting produces the license at no charge; the Rent Board Fee is a separate $59.00-per-unit annual payment. Paying the fee does not replace reporting.", "verified", ["S53", "S56", "S07"], "Both are due around March 1 but are not interchangeable (F33)."),
                row("AN-27", "License timing and retaliation risk", "A license that exists today does not validate a notice whose effective date preceded it. California Civil Code section 1942.5 separately limits rent increases after qualifying tenantability events, subject to its conditions and exceptions.", "verified", ["S53", "S08", "S57"], "Check the effective date and the statutory conditions; no ranking of defects is established."),
                row("AN-28", "This building is very likely covered", "Two rented units in a pre-1979 building is the paradigm Rent Ordinance case; the in-law-unit rule and the 1979 cutoff both point toward coverage rather than exemption", "analysis", ["S06", "S59", "S60"], "Owner-supplied facts only; confirm in the Property Information Map."),
                row("AN-29", "Conservative approach", "Ordinary annual increase at or under 1.6%, license on file first, 30-day written notice, no additional-occupant charge, and an identical written standard applied to both units", "analysis", ["S01", "S07", "S35", "S42"], "Still not a guarantee against a petition."),
            ]},
        ],
    },
}

# ---------------------------------------------------------------------------
# Notice Worksheet page (B87-I integration, 2026-11-10).
# Loaded from the verified B87 kit JSON so the kit stays the single source of
# truth; B87 source IDs are mapped to the site's canonical source IDs.

_WORKSHEET_JSON = Path(__file__).resolve().parent.parent / "research" / "b87_notice_kit" / "worksheet.json"

B87_SOURCE_MAP = {
    "B87-S01": "S01", "B87-S02": "S07", "B87-S03": "S73", "B87-S04": "S74",
    "B87-S05": "S53", "B87-S06": "S75", "B87-S07": "S76", "B87-S08": "S77",
    "B87-S09": "S35", "B87-S10": "S78", "B87-S11": "S79", "B87-S12": "S80",
    "B87-S13": "S04", "B87-S14": "S02", "B87-S15": "S05", "B87-S16": "S54",
    "B87-S17": "S09", "B87-S18": "S12", "B87-S19": "S81", "B87-S20": "S10",
    "B87-S21": "S13", "B87-S22": "S16", "B87-S23": "S57", "B87-S24": "S82",
    "B87-S25": "S25", "B87-S26": "S24", "B87-S27": "S26", "B87-S28": "S06",
    "B87-S29": "S56", "B87-S30": "S08",
}

def _worksheet_row(r):
    """Map one B87 kit row onto the site row schema without changing meaning."""
    status = "verified" if r["status"] == "verified rule" else r["status"]
    flags = r.get("flag_ids") or []
    flag_id = flags[0] if flags else ""
    notes_parts = []
    if status == "needs review":
        value = ""  # validator: unverified cells stay blank
        if r.get("rule"):
            notes_parts.append(r["rule"])
    else:
        value = r.get("value") or r.get("rule") or ""
    if r.get("notes"):
        notes_parts.append(r["notes"])
    if len(flags) > 1:
        notes_parts.append("See also " + ", ".join(flags[1:]) + ".")
    source_ids = [B87_SOURCE_MAP[s] for s in r["source_ids"]]
    return row(r["id"], r["label"], value, status, source_ids, " ".join(notes_parts), flag_id)

def _worksheet_page():
    kit = json.loads(_WORKSHEET_JSON.read_text(encoding="utf-8"))
    groups = [
        ("Owner inputs (case facts - not official findings)", ("B87-IN-",)),
        ("Pre-service gates - every cell blank until verified", ("B87-G",)),
        ("Required notice contents", ("B87-N",)),
        ("Conditional arithmetic (illustrative only)", ("B87-C",)),
        ("Service record rules", ("B87-SV",)),
        ("Tenant service log (blank until a notice is served)", ("B87-LOG",)),
    ]
    sections = []
    for title, prefixes in groups:
        rows = [_worksheet_row(r) for r in kit["rows"] if r["id"].startswith(prefixes)]
        sections.append({"title": title, "columns": COLUMNS, "rows": rows})
    return {
        "title": "Notice Worksheet",
        "description": "Pre-service worksheet and per-tenant service record for an annual rent-increase notice, from the B87 official-source kit. Case cells stay blank until verified.",
        "sections": sections,
    }

PAGES["worksheet"] = _worksheet_page()

# ---------------------------------------------------------------------------
# T55 (2026-11-13): Suggestions page. Every proposal is reviewable, carries the
# official source that motivates it, states its cost/effort, and can be accepted
# or declined BEFORE anything is implemented. Nothing here changes a rule.
# ---------------------------------------------------------------------------

SUG_COLUMNS = ["ID", "Suggestion", "Why it helps the decision", "Evidence / official source", "Effort", "Review status"]

def sug(id, title, why, source_ids, effort, status="open for review", notes=""):
    return {"id": id, "label": title, "value": why, "status": "analysis", "source_ids": source_ids,
            "effort": effort, "review_status": status, "notes": notes,
            "flag_id": "", "source_note": ""}

SUGGESTIONS = {
    "title": "Suggestions - review before implementing",
    "description": "A dedicated review queue of proposed improvements to this site and to the rent-increase decision process. Each suggestion states what it changes, why it helps, the official basis, the effort, and its review status so a reviewer can choose the best path before anything is implemented.",
    "sections": [
        {"title": "How to use this page (the review process)", "columns": ["Step", "What happens", "Owner of the decision", "Record kept"], "rows": [
            {"id": "SUG-P1", "label": "1. Read the proposal", "value": "Each suggestion below states the exact change, the decision it improves, and the official source that motivates it. Nothing is implemented by being listed here.", "status": "analysis", "source_ids": ["S01"], "notes": "Honest label: this is a proposal queue, not a change log.", "flag_id": ""},
            {"id": "SUG-P2", "label": "2. Check the evidence", "value": "Open the linked official page and confirm the quoted rule, dollar figure or date still says what the row says. If it does not, the suggestion is stale - say so before accepting it.", "status": "analysis", "source_ids": ["S01", "S07"], "notes": "Every row on this site is linked for exactly this reason.", "flag_id": ""},
            {"id": "SUG-P3", "label": "3. Choose a path", "value": "Accept, defer or decline. Accepting a suggestion is a decision by the owner (or by the next build session for site-only changes). No suggestion here changes a legal obligation on its own.", "status": "analysis", "source_ids": ["S53"], "notes": "Nothing auto-applies.", "flag_id": ""},
            {"id": "SUG-P4", "label": "4. Record the outcome", "value": "Write the decision, the date and the reviewer in the review-status column (or in COORDINATION.md), so the next session does not re-litigate a closed item.", "status": "analysis", "source_ids": ["S68"], "notes": "COORDINATION.md is the shared task board for this repository.", "flag_id": ""},
            {"id": "SUG-P5", "label": "5. Only then implement", "value": "Implementation means editing scripts/site_*.py and rebuilding, not hand-editing pages. The validator re-runs every check after a build.", "status": "analysis", "source_ids": ["S68"], "notes": "Generated files are reproducible; CI re-runs the build and fails on drift.", "flag_id": ""},
        ]},
        {"title": "A. Suggestions to close information gaps before deciding", "columns": ["ID", "Suggestion", "Why it helps the decision", "Evidence / official source", "Effort", "Review status"], "rows": [
            sug("SUG-A1", "Pull the Property Information Map record for both units and record the official build year, unit count and any in-law designation", "The owner-stated 1940 year and two-unit count are the entire basis for assuming coverage. If the official record shows a post-1979 certificate of occupancy or a single-family designation, the whole licensing analysis changes. This is the single highest-value open item.", ["S32", "S06", "S59"], "15 minutes, free, no account", notes="Maps to CASE-V1 / CASE-V2. Owner action; the agent cannot log in."),
            sug("SUG-A2", "Log in to the Rent Board Portal and screenshot the Housing Inventory status and licence status for each unit", "Licence status is the one unverified fact that can void an entire increase under Rule 13.14. Everything downstream depends on it.", ["S55", "S07", "S73"], "10 minutes, free", notes="Maps to CASE-V3 / T03-F05."),
            sug("SUG-A3", "Reconstruct the actual rent history for each unit from leases, bank statements and any prior notices", "Banked increases are the only lawful route above 1.6%, and they can only be computed from a real payment history. Without it, every banked figure on this site stays blank - correctly.", ["S05", "S54", "S01"], "1-2 hours, owner records only", notes="Maps to CASE-V4 / CASE-V9, flag F30."),
            sug("SUG-A4", "Identify, in writing, the legal status of the occupant added to Unit 1 on April 1, 2026 (co-tenant, subtenant or assignee) and whether a written Section 6.14 notice was served", "Co-tenant status means no market reset at all; subtenant/assignee status could allow one only with specific facts and a timely written notice. The difference is large and it is a fact question, not a research question.", ["S16", "S37", "S15"], "30 minutes + possibly legal advice", notes="Maps to CASE-V5 to CASE-V8, flag F28."),
            sug("SUG-A5", "Ask the Rent Board directly (311 or 415-252-4600) whether the April 1, 2026 continuation restarted the Annex A / anniversary clock", "The anniversary date determines the earliest lawful effective date. A wrong assumption here makes an otherwise compliant notice premature.", ["S24", "S01", "S73"], "One phone call", notes="Maps to CASE-V6. Free counselling; not legal advice."),
            sug("SUG-A6", "Get one paid hour with a tenant-side or landlord-tenant attorney to review the completed Notice Worksheet", "Every page here says the same thing: this is a compliance checklist capable of review, not an approval. A single review converts an open question into a documented position.", ["S23", "S24", "S30"], "1 hour, paid", notes="Maps to F47 / REQ-21. The site never claims attorney approval."),
            sug("SUG-A7", "Confirm the Rent Board Fee exemption status and billing record for both units", "The fee is a separate obligation with penalties up to 15%; whether it has been paid or exempted is unverified and is independently enforceable.", ["S56", "S63", "S65"], "10 minutes, Portal", notes="Maps to FEE-12 / F43."),
        ]},
        {"title": "B. Suggestions to improve this site so it supports a decision", "columns": ["ID", "Suggestion", "Why it helps the decision", "Evidence / official source", "Effort", "Review status"], "rows": [
            sug("SUG-B1", "Add a printable one-page decision sheet that lists only the eight gate questions and the owner-stated answers", "The full site is comprehensive but too long to use at the moment of deciding. A one-pager is what a reviewer actually holds while checking a draft notice.", ["S01", "S07", "S35"], "Build change, low risk", notes="New file; does not alter any verified value."),
            sug("SUG-B2", "Add an automated 'stale source' check that re-fetches every official URL on a schedule and flags any page whose quoted figure changed", "The 1.6% rate, the $59.00 fee and File 261020 all move. A dated diff is the cheapest defence against relying on an out-of-date page.", ["S02", "S56", "S71"], "Build change, medium", notes="Would require a scheduled workflow; currently sources are re-checked manually per session."),
            sug("SUG-B3", "Link each flag directly from the table cell that raised it, in both directions", "Reviewers currently read a row, then hunt the flag. Bidirectional links cut review time and reduce the chance a flagged row is acted on as if it were verified.", ["S01"], "Build change, low risk", notes="Improves navigation only; no content change."),
            sug("SUG-B4", "Publish a diff-style change log of every figure that changed between builds", "Re-verification is only meaningful if a reader can see what moved. A visible changelog makes an auditor's job possible without reading git history.", ["S68"], "Build change, medium", notes="Git history already contains the data; this only surfaces it."),
            sug("SUG-B5", "Add a plain-language glossary (base rent, anniversary date, banked increase, passthrough, license, Housing Inventory)", "Several terms look interchangeable to a first-time owner but carry different legal consequences - notably license vs fee, and banked increase vs passthrough.", ["S01", "S05", "S56"], "Content change, low risk", notes="Definitions must be quoted from the official pages, not paraphrased freely."),
            sug("SUG-B6", "Keep the site free of any owner name, address or tenant identifier, and re-run the privacy check on every build", "Privacy is the owner's stated top priority, and the F44/F51 history flags show how easily identifiers leak into a public repository.", ["S68"], "Already implemented; keep enforced", notes="F44 and F51 remain owner-actionable for historical commits; this site cannot rewrite published history."),
        ]},
        {"title": "C. Suggestions on how to approach the increase itself (decision paths, not legal advice)", "columns": ["ID", "Suggestion", "Why it helps the decision", "Evidence / official source", "Effort", "Review status"], "rows": [
            sug("SUG-C1", "Adopt one written, neutral rule - 'on each unit's anniversary date, impose the published annual allowable increase if the licence is current' - and apply it identically to both units", "An identical rule applied by anniversary date is the cleanest answer to the one-vs-both discrimination question, because the selection criterion is the calendar, not the tenant.", ["S42", "S38", "S01"], "One page of policy text", notes="Analysis recommendation. It is not a guarantee against a complaint or a petition."),
            sug("SUG-C2", "Document the neutral reason for any unit that is NOT increased at the same time (for example: anniversary not reached, or licence not current)", "If the two units are treated differently, the file should show a reason that does not depend on who the tenant is. This is the practical defence in a disparate-treatment inquiry.", ["S42", "S38", "S22"], "10 minutes per decision", notes="Contingent recommendation; depends on SUG-A2 and SUG-A5."),
            sug("SUG-C3", "Do not raise rent merely because a roommate was added to Unit 1", "SF.gov states additional-occupant charges are an unlawful rent increase even where the lease provides for one. This is the sharpest available trap in this case.", ["S01", "S18", "S17"], "No action needed - avoidance", notes="Directly answers Q-14 and AN-07."),
            sug("SUG-C4", "Set the effective date no earlier than the later of (a) the anniversary date and (b) the date the licence is confirmed on file", "Rule 13.14 tests the effective date, not the service date. Sequencing the dates this way removes the nullity risk without needing to guess.", ["S73", "S07", "S01"], "Scheduling discipline", notes="Conservative sequencing; the rule states the legal test, the sequence is the recommendation."),
            sug("SUG-C5", "Serve the notice with proof of service and keep a dated copy of the official pages relied on", "A dated record is the cheapest way to answer a later question about which rate and which rules were in force when the notice was served.", ["S35", "S78", "S01"], "10 minutes per notice", notes="Matches the existing Notice Worksheet (pages/worksheet.html)."),
            sug("SUG-C6", "Re-check File 261020's committee status immediately before serving any banked or capital-improvement notice", "The pending ordinance targets exactly the stacked multi-year increase that Unit 2's long tenure could theoretically support. It is not law today, but that can change.", ["S71", "S72", "S05"], "5 minutes", notes="Maps to F46 / REQ-25."),
        ]},
    ],
}

PAGES["suggestions"] = SUGGESTIONS

# ---------------------------------------------------------------------------
# T54 (2026-11-13): additional suggestion groups contributed by session
# `arena-87a91aec`, appended to the Suggestions review queue published by
# session `arena-415e54ea` (PRs #51 and #53). Nothing from either session is
# discarded: the concurrent session's SUG-P*, SUG-A*, SUG-B* and SUG-C* rows
# stay first on the page, and the groups below are added after them. Where the
# two overlap, the row's notes name the related row instead of repeating it.
from site_suggestions import T54_SECTIONS, checklist_rows  # noqa: E402

_T54_COLUMNS = ["ID", "Suggestion", "Why it helps the decision", "Evidence / official source", "Effort", "Review status"]
for _sec in T54_SECTIONS:
    SUGGESTIONS["sections"].append({
        "title": _sec["title"],
        "intro": _sec["intro"],
        "columns": list(_T54_COLUMNS),
        "rows": _sec["rows"],
    })

# The review checklist: one blank decision row per T54 proposal, so a reviewer
# can record Accept / Reject / Defer before anything is implemented.
SUGGESTIONS["sections"].append({
    "title": "H. Review checklist for the D-G proposals (reviewer to complete)",
    "intro": "One row per proposal above. The Decision, Reviewer, Date and Review note cells are intentionally blank - they are the reviewer's to complete. A blank cell here means 'not yet decided', which is different from a blank cell on a finding page, where a blank means 'no official source confirms the value'.",
    "columns": ["ID", "Suggestion", "Decision", "Reviewer", "Date", "Review note"],
    "rows": checklist_rows(),
})


# ---------------------------------------------------------------------------
# T56 (2026-11-13): Decision Readiness register. One row per question that must
# be answered before a rent-increase decision is reasonable. "Information known
# now" holds only what an official source states OR what the owner supplied
# (labelled as such). Unverified fact cells stay BLANK and are flagged.
# ---------------------------------------------------------------------------

GATE_COLUMNS = ["Question that must be answered", "Information known now", "Status", "Official source(s)", "What is missing, why it matters, and how to discover it"]

DECISION = {
    "title": "Decision Readiness - what must be known first",
    "description": "Every question, piece of information and answer that has to be settled before a rent-increase decision on these two units is reasonable. Unknown items stay blank and flagged, with the discovery route named for each.",
    "sections": [
        {"title": "The decision, broken into five gates that must close in order", "columns": ["Gate", "What must be true before moving on", "Status", "Official source(s)", "Why the order matters"], "rows": [
            row("DR-G1", "Gate 1 - Coverage: the unit is actually subject to the SF Rent Ordinance", "Both units are two rented units in a 1940 building, which SF.gov describes as the paradigm covered case (many units built on or before June 13, 1979 have rent control). Owner-supplied facts; the official record is unchecked.", "analysis", ["S06", "S32", "S59"], "If the unit is exempt, the 1.6% limit, the license and the Rent Board notice rules do not apply at all - a different decision entirely."),
            row("DR-G2", "Gate 2 - Standing: the owner is entitled to impose an increase at all", "A landlord must have a current Rent Increase License on file before an annual or banked increase takes effect; the license follows the unit's rent-controlled status, not the owner's corporate form.", "verified", ["S01", "S07", "S53", "S73"], "Rule 13.14 makes an unlicensed increase null and void as of its effective date - so this gate can void a fully correct notice."),
            row("DR-G3", "Gate 3 - Amount: the correct base rent, rate and elapsed time", "The rate is 1.6% for 3/1/26-2/28/27 and an increase may be imposed once every 12 months on the anniversary date, on base rent only, not rounded up.", "verified", ["S01", "S02", "S05"], "A rate that is right but applied to the wrong base rent or too early is still an unlawful increase."),
            row("DR-G4", "Gate 4 - Process: the notice and delivery meet both local and state rules", "30-day written notice (90-day if more than 10% alone or combined in the same year), plus 5 days if mailed within California; the notice must state the dollar amount, the percentage and the effective date, using the rate in effect on the increase date.", "verified", ["S01", "S35", "S78"], "A correct amount in a defective notice can still be unenforceable. Civil Code 827 content and service rules are cumulative with the local rules."),
            row("DR-G5", "Gate 5 - Fair treatment: the choice between the two units is defensible", "Federal and state fair-housing law reach discriminatory effect without intent; a substantial legitimate non-discriminatory interest and the absence of a less discriminatory alternative are the test. No official source requires raising both units.", "verified", ["S42", "S38", "S41"], "This is the gate that answers the one-unit-or-both question, and it is decided by the reason for the choice, not the size of the increase."),
        ]},
        {"title": "Gate 1 - Coverage: open questions and the discovery route", "columns": GATE_COLUMNS, "rows": [
            row("DR-01", "What is the official build year and unit count on record for this property?", "SF.gov states that many units built on or before June 13, 1979 have rent control and eviction protection, and that the first step is to look up the address in the SF Planning Property Information Map.", "verified", ["S06", "S32"], "The 1940 year is owner-supplied only. Open the Property Information Map and record the official year, the unit count and any in-law designation. Free, no account, about 15 minutes. Flagged as T03-F04."),
            row("DR-02", "Does the property fall into a partial exemption (single-family or condominium, new construction, substantial rehabilitation, subsidized)?", "SF.gov lists partial exemptions for units built after June 13, 1979, most single-family homes and condominiums, substantial rehabilitation, and government-regulated rents; a legal or illegal in-law unit does not by itself create an exemption and can keep a two-unit building covered.", "verified", ["S06", "S59", "S60"], "Exemption status is unverified for this address. The Property Information Map record and the certificate of occupancy answer it; if it is ambiguous the official route is a Rent Board counselor or a Section 6.14/Costa-Hawkins petition for a formal determination (S15)."),
            row("DR-03", "Is either unit an ADU or JADU, and were both units ever rented under one tenancy?", "Civil Code 1947.12(d)(6) exempts a two-unit structure only where the owner occupied one unit as a principal residence at the beginning of the tenancy and continues in occupancy, and neither unit is an ADU or JADU. The in-law rule also turns on whether both units are rented together as a single tenancy.", "verified", ["S36", "S60", "S58"], "Owner-supplied facts do not state whether the owner ever occupied a unit, nor the ADU status. That fact decides whether the state exemption could even be argued (it does not remove the local ordinance). Flags F34, F35."),
        ]},
        {"title": "Gate 2 - Standing: license, fee and registration questions", "columns": GATE_COLUMNS, "rows": [
            row("DR-04", "Has each unit been reported into the Rent Board Housing Inventory, and is a Rent Increase License on file?", "", "needs review", ["S55", "S07", "S73"], "Owner-supplied intake does not confirm reporting or licence status. Discover it by logging into the Rent Board Portal and viewing the unit record; tenants can see the same status, so a tenant-side reviewer will check it. Everything in Gate 3 and Gate 4 is wasted work until this closes. Flag T03-F05.", "T03-F05"),
            row("DR-05", "Will the licence be current on the intended effective date (not just on the day the notice is served)?", "", "needs review", ["S73", "S07", "S08"], "Rule 13.14 tests the effective date. Once DR-04 is known, schedule the effective date after the licence is confirmed. If a notice has already been served with an earlier effective date, that is a legal question for counsel, not something to assume away. Flag F25.", "F25"),
            row("DR-06", "Is the annual Rent Board Fee paid or exempt for each unit for the current cycle?", "", "needs review", ["S56", "S63", "S65"], "The fee is a separate obligation with 5%-per-stage penalties to a 15% maximum and delinquency referral. Discover it from the Portal and the Treasurer's records. Paying it does not create a licence, and a licence does not pay it. Flag F43.", "F43"),
            row("DR-07", "Does the owner need a City business registration for this rental?", "A person receiving rental income from 'one residential structure consisting of fewer than four units' is not, 'by reason of that fact alone', required to obtain a business registration certificate. Other business activity or payroll expense can still require one.", "verified", ["S66"], "The owner-supplied fact is a two-unit building, which is fewer than four units; whether the owner has other business activity or payroll expense was not supplied. Confirm against the Treasurer page before filing anything. Flag F39 covers the narrow wording of this rule."),
        ]},
        {"title": "Gate 3 - Amount: base rent, anniversary date and banking", "columns": GATE_COLUMNS, "rows": [
            row("DR-08", "What is the current base rent for Unit 1, and what is the current rent for Unit 2?", "Owner-supplied: Unit 1 was $3,995 at the February 1, 2025 lease start and $3,995 on the April 1, 2026 continuing tenancy. Unit 2 was $3,150 at the June 1, 2019 lease start.", "analysis", ["S01", "S56"], "Unit 2's CURRENT rent was never supplied - only the 2019 figure. The 1.6% must be calculated on the base rent actually in effect, so the Unit 2 calculation on this site is illustrative only. Discover it from the current lease and recent payment records. Flag T03-F06."),
            row("DR-09", "What is each unit's anniversary date?", "A landlord can impose the first annual increase 12 months after the lease began, and each increase sets a new anniversary date at least 12 months out.", "verified", ["S01", "S76"], "Unit 1's April 1, 2026 continuation may or may not have restarted the clock; that is a fact question about whether it was a new tenancy or a continuing one. Unit 2's 2019 date is old enough that any 12-month bar has long passed. Flag T03-F04 / CASE-V6."),
            row("DR-10", "Has every increase been correctly banked, and is any banked amount actually available?", "", "needs review", ["S05", "S54", "S03"], "Banking requires at least 24 full months without any increase, percentages are added (never compounded or prorated), and the notice must state the banked portion. The full increase history was never supplied, so no banked figure is asserted anywhere on this site. Discover it from leases, notices and cancelled cheques. Flags F30, CASE-V9.", "F30"),
            row("DR-11", "If a banked increase were claimed, would the notice cross the 10% threshold and need 90 days?", "If a correctly banked total plus the current annual rate exceeds 10%, the notice must be 90 days rather than 30 days.", "verified", ["S01", "S05"], "Conditional only - it becomes live only after DR-10 is answered. The site's 13.1% illustration is arithmetic, not a finding, and is flagged as F30."),
            row("DR-12", "Does pending File 261020 change the permissible amount?", "Proposed, not enacted: it would temporarily limit combined banked plus capital-improvement increases to 10% per year if enacted as drafted. A plain 1.6% annual increase is not described as being affected.", "verified", ["S71", "S72", "S87"], "Status must be re-checked immediately before serving any banked or capital-improvement notice. As of the last check the Legistar record was Pending Committee Action. Flags F46, F47."),
        ]},
        {"title": "Gate 4 - Process and risk: notice, timing and retaliation", "columns": GATE_COLUMNS, "rows": [
            row("DR-13", "Is each notice complete and correctly served?", "The notice must be written; state the dollar amount, the percentage and the effective date; give 30 days (90 if more than 10%), plus 5 days if mailed within California; and follow Civil Code 827 delivery rules.", "verified", ["S01", "S35", "S78"], "The Notice Worksheet page tracks each required element and the per-tenant service record. Proof of service is the evidence if the date is later disputed."),
            row("DR-14", "Is there an outstanding repair complaint or other tenantability event within 180 days?", "", "needs review", ["S57", "S61", "S82"], "Civil Code 1942.5(a) applies where the lessor retaliates: if the tenant is not in default in rent, the lessor may not increase the rent within 180 days of the latest applicable enumerated tenantability event (a good-faith repair notice or oral complaint to the landlord, a bed-bug notice, a recorded agency complaint, a resulting inspection or citation, a proceeding, or an adverse decision), and subdivision (b) limits invocation to once in 12 months. Separately, a tenant may petition the Rent Board to defer an increase for unrepaired conditions. This history was never supplied. Discover it from the correspondence file and any Rent Board or DBI records before serving. Flag T03-F02.", "T03-F02"),
            row("DR-15", "Has a Notice of Violation, citation or permit issue been recorded for either unit?", "", "needs review", ["S61", "S32"], "An open violation is both a retaliation risk and, for an O&M or capital-improvement petition, a bar to recovery. Discover it from DBI records and the Property Information Map before relying on any petition-based increase. Owner records not supplied.", "T03-F02"),
            row("DR-16", "Is the household's rent subsidized (for example a Section 8 voucher)?", "", "needs review", ["S60", "S10"], "Subsidized units can be partially exempt from the local rent limitations, and the voucher payment standard interacts with the rent. Never supplied. Discover it from the lease and any HAP contract. No exemption is assumed on this site.", "T03-F04"),
        ]},
        {"title": "Gate 5 - Fair treatment across the two units (the one-unit-or-both question)", "columns": GATE_COLUMNS, "rows": [
            row("DR-17", "Does any official source require raising both units together?", "No. No official source located requires an owner to raise rent on every unit, and no official source prohibits raising one.", "verified", ["S42", "S41", "S38"], "This is a negative finding. The absence of a requirement is not a green light - Gate 5 is about how the choice is made and documented, not whether it is permitted."),
            row("DR-18", "What legal standard would a fair-housing inquiry actually apply?", "Disparate-impact liability can exist without intent; a policy is defensible where it serves a substantial legitimate non-discriminatory interest and there is no less discriminatory alternative. California FEHA separately reaches source of income, retaliation, perception and association.", "verified", ["S42", "S38", "S39"], "Practical consequence: select units by a rule that does not reference the tenant (anniversary date, licence status, coverage), and write the rule down before applying it."),
            row("DR-19", "Is there a neutral, documented reason for any difference in treatment between the two units?", "", "needs review", ["S42", "S22", "S01"], "Not supplied. This is the single document a tenant-side reviewer would ask for. Discover it by writing the policy before the first notice: 'each unit is increased on its own anniversary date if the licence is current'. Recommendation only - it is not a guarantee against a complaint. Flags F22, T03-F09.", "F22"),
            row("DR-20", "Does the increase size itself create disparate impact?", "The compliant amount is at most the published annual allowable increase on base rent, applied once every 12 months, so the local ceiling is small and uniform.", "verified", ["S01", "S02"], "A uniform, small, rule-based increase reduces (but does not eliminate) exposure. Nothing here claims that no complaint can occur."),
        ]},
        {"title": "What would change the answer - the four decision paths", "columns": ["Path", "When it is the right path", "Status", "Official source(s)", "What it requires first"], "rows": [
            row("DR-P1", "Path A - ordinary annual increase at or under 1.6% on each unit's anniversary date, licence current", "The default conservative path: both units covered, licence confirmed, anniversary reached, no retaliation event, no banked claim.", "analysis", ["S01", "S07", "S35"], "Gates 1, 2 and 4 closed; Gate 3 answered for base rent and anniversary. No petition needed."),
            row("DR-P2", "Path B - postpone one unit to preserve a uniform anniversary policy", "When one unit's anniversary has not been reached or its licence is not current. Deferring is lawful; increasing early is not.", "analysis", ["S01", "S73", "S05"], "A written note of the neutral reason. Deferring does not waive the increase - banking preserves it (DR-10)."),
            row("DR-P3", "Path C - add a banked or petition-based amount above 1.6%", "Only where a real rent history supports banking, or a Rent Board petition is granted, or a certified passthrough applies.", "analysis", ["S05", "S09", "S12"], "DR-10 must be answered from records; a petition must be FILED BEFORE the notice is served, or the notice is void. Higher scrutiny and 90-day notice likely."),
            row("DR-P4", "Path D - no increase this cycle", "Where coverage, licence or the Unit 1 occupant question cannot be closed, or where a repair dispute is open.", "analysis", ["S01", "S57", "S73"], "Nothing to file. Banking rights continue to accrue if 24 months elapse without an increase (DR-10)."),
        ]},
    ],
}

PAGES["decision"] = DECISION


