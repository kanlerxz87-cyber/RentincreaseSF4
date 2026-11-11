"""Standalone markdown deliverables and stylesheet for the static site."""

EXECUTIVE_SUMMARY_TEXT = """# Executive Summary - Rental increase SF

Key official rate, licensing, fee, banking, proposed-legislation and HUD sources were targeted for recheck on 2026-11-11 UTC; other sources retain their individual verification dates. See research/t51_external_audit/README.md for scope and limitations. Informational research, not legal advice.

## FOREFRONT: Rent Board & Rent Increase License — yes, an individual owner must comply

**Question:** "I am just an individual property owner and not part of a corporation — do I still need to apply for the license and inform the Rent Board before notifying tenants of a rent increase?"

**Answer: Yes, an individual owner must report and have a license for a covered annual or banked increase. But it need not be in place before the notice is served: the legal test is the increase’s effective date.** Obtaining it before service is the safer recommended practice. Rent Board Rule 13.14 explicitly uses the effective date, not the date of service (https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-xiii-reporting-obligations-under-rent). SF.gov states: "A landlord must get a rent increase license before imposing annual allowable and/or banked rent increases on a tenant." No individual-owner exception is stated. The requirement has applied since July 1, 2022 — and since **March 1, 2023 for condominiums and buildings with 1-9 residential units** — so the requirement applies to covered units in small individual-owned buildings too; this property’s coverage remains unconfirmed. "Informing the Rent Board" and "getting the license" are the same process: you report into the **Rent Board Housing Inventory**, and the license is generated from that report.

**Step by step (do these in order, before any tenant notice takes effect):**

1. **Confirm the unit is covered** by the SF Rent Ordinance (check the property in the SF Planning Property Information Map; many units built on/before June 13, 1979 are covered — the owner-supplied "built in 1940" fact is unverified, see Flagged for Review).
2. **Report into the Rent Board Housing Inventory** via the Rent Board Portal (https://portal.sfrb.org/). SF.gov: "All owners of residential property are required to report." Reporting is free, online 24/7, due **March 1 every year**, and is submitted under penalty of perjury. The information entered is public.
3. **Receive the Rent Increase License.** Owners who report a unit as tenant-occupied receive a rent increase license; it is **automatically generated for non-owner-occupied units**. The license does **not** need to be included with your notice to tenants.
4. **Check the license is current and on file before the increase's effective date.** SF.gov: "A landlord must have a current rent increase license on file with the Rent Board before any annual or banked rent increase can go into effect," and a rent increase notice "will not be enforceable without having a rent increase license on the effective date of the notice." Tenants can search the Portal to check whether you are up to date; if you miss the deadline, the Rent Board may notify your tenants that you are not in compliance. (Exact consequence wording differs between SF.gov pages - see flag F25; the ordinance itself says the license is suspended and the tenant is not obligated to pay the increased rent during the suspension.)
5. **Late?** You can still report and receive a license after March 1; the Rent Board assesses **no monetary penalty** for late filing — but that does not make a notice enforceable for an effective date on which no license was on file.
6. **Recommended: after confirming the license, notify tenants**, in writing (Rule 13.14 tests the effective date rather than the service date): 30 days (90 days if the increase, alone or combined with another increase in the same year, exceeds 10%; +5 days if mailed within California; different mailing locations can require more), stating the dollar amount, percentage, and effective date, using the rate in effect on the increase date. Complying with the license rule does not replace any other local or state rent-increase law.

Official links for manual review: SF.gov "Learn about rent increases in San Francisco" (https://www.sf.gov/learn-about-rent-increases-san-francisco) and SF.gov "The Rent Board Housing Inventory" (https://www.sf.gov/rent-board-housing-inventory).

**What the Rent Ordinance itself says:**

- **Sec. 37.3(a)(1):** "A landlord who has reported the required information about their rental unit to the Rent Board as set forth in Section 37.15 shall have a license to impose annually a rent increase which does not exceed a tenant's base rent by more than 60% of said published increase. In no event, however, shall the allowable annual increase be greater than 7%." - https://www.sf.gov/information--sec-373-rent-limitations
- **Sec. 37.15(e):** a substantially compliant owner "shall receive a license to impose rent increases"; if not, "the license to impose rent increases shall be temporarily suspended ... but a tenant shall not be obligated to pay the increased rent for months during the period of suspension." Added by Ord. 265-20. - https://www.sf.gov/information--sec-3715-reporting-obligations-licensing
- **Form 571 (Rent Board):** the annual increase may be imposed "without filing a petition at the Rent Board." - https://media.api.sf.gov/documents/571_Allowable_Annual_Increases_26-27_1.pdf

**Two separate obligations - do not conflate them (flag F33).** The *Rent Increase License* is produced by Housing Inventory reporting and there is **no charge** for it. The *Rent Board Fee* is a **separate** per-unit annual payment: **$59.00 per dwelling unit for 2026-2027**, due **March 1, 2027**, with a 5% late penalty added after March 1, April 1 and May 1 (maximum 15%) and delinquency on June 1. The official fee page gives conflicting referral timing: its summary says unpaid fees are referred after June 1, but its timeline says a July notice allows 30 days before referral. Confirm the timing with the Rent Board (flag F38). The exemption window closes **Monday, December 14, 2026**, an exemption must be requested **every year**, and vacant units do not qualify. SF.gov states expressly that *"requesting a Rent Board Fee exemption does not satisfy Rent Board Housing Inventory reporting requirements"*, and the 2027 informational notice states the reverse - so you can pay the fee and still have no license, or be licensed and still owe the fee. If the fee is paid in full you may recover **50% ($29.50 per dwelling unit)** from tenants in occupancy on November 1, by deducting it from the annual security-deposit interest payment (4.2% for 3/1/26-2/28/27) or by a compliant direct bill - show it as a fee recovery, never as part of the rent increase. City business registration is a **third, separate** question: an individual whose only rental income is from one residential structure of fewer than four units is not required to register *by reason of that fact alone*. (https://www.sf.gov/rent-board-fee, https://www.sf.gov/information--recover-part-your-rent-board-fee-tenant, https://sftreasurer.org/information-lessors-residential-real-estate) The full fee tables, calendar and case arithmetic are on the **Rent Board Fee** page (`pages/fee.html`).

**Before you serve any notice, check the retaliation rules (state-law risk, see State Law rows ST-13 to ST-15).** Civil Code section 1942.5(a) restricts a rent increase or service reduction **when the landlord retaliates** within **180 days** of the latest applicable enumerated tenantability event (including a good-faith tenantability notice or oral repair complaint to the landlord, bed-bug notice, qualifying recorded agency complaint, related inspection/citation, proceeding or adverse decision), where the tenant is not in default in rent. That subdivision may not be invoked more than once in any 12-month period. Subdivision (d) separately bars retaliation for lawful tenant organizing or exercise of legal rights. Subdivision (g) preserves action for lawful cause where the notice or pleading states the good-faith ground, subject to proof if controverted. Remedies include actual damages; punitive damages of **$100-$2,000 per retaliatory act only where fraud, oppression or malice is shown**; and, in an action for damages for retaliatory eviction, reasonable attorney's fees to the prevailing party if requested upon initiation. This is a risk check, not a safe harbor to invent a reason. (https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1942.5.&lawCode=CIV)

**Your two-unit 1940 building - why coverage is likely but still unconfirmed.** SF.gov: many units built on or before June 13, 1979 have both rent control and eviction protection. A single-family dwelling with a **legal** in-law unit is a **two-unit building** and is **not** exempt; with an **illegal** in-law unit it is also a two-unit building and is not exempt **unless both units are rented together as a single tenancy**; and a single-family dwelling is not exempt if another residential structure is on the same lot. (This sentence was corrected on 2026-11-08 after a line-by-line comparison with the page - flag F36.) Conversely, AB 1482 exempts a two-unit structure only if the owner occupied one unit as a principal residence **at the beginning of the tenancy and continues in occupancy**, and neither unit is an ADU/JADU - a fact you did not supply, so no exemption is asserted (flags F34, F35). Two separately rented units in a pre-1979 building is the paradigm covered case, but confirm the lot and year in the Property Information Map before you rely on it. (https://www.sf.gov/learn-about-san-francisco-rental-laws, https://www.sf.gov/information--partial-exemption-certain-single-family-homes-and-condominiums-under-costa-hawkins, https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV)

**Scope limits:** SF.gov states the license rules apply ONLY to rent-controlled units, and that the license is not required for Section 6.14/Costa-Hawkins increases or for passthroughs allowed under the Rent Ordinance (https://www.sf.gov/notice-of-owner-noncompliance-with-housing-inventory, https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins). The Housing Inventory information you submit is **public**, including the owner's name and business contact information.

**Full step-by-step tables:** the site's Step-by-Step License page (`pages/process.html`) carries 12 numbered steps with an official link on every step, the ordinance text, and the case application for both units. For this case, Housing Inventory reporting and a current license for either unit are **unconfirmed** (blank, flagged T03-F05) — no increase should be treated as effective until that is confirmed.

**Before serving a notice, work through the Notice Worksheet** (`pages/worksheet.html`): pre-service gates (coverage, Housing Inventory, licence on the effective date, lease term, base rent, anniversary, rate, banking, petitions, subsidy, repairs/retaliation, occupant changes), the required notice contents, the service rules (personal delivery or mail under Civil Code 827 / CCP 1013, with five extra calendar days when both mailing and address are in California and potentially longer otherwise, plus proof of service) and a per-tenant service log. Every row links to its official source; the case cells stay blank and flagged until verified (flags B87-F01–B87-F08).


**Pending legislation — not current law:** As of November 11, 2026, Legistar showed File 261020 pending committee action and no enactment. Version 1 proposes a combined banked/capital-improvement limit of 10% of the lowest base rent in the preceding 12 months, through December 31, 2029 unless extended. It would apply to specified banked notices and capital-improvement petitions on or after September 15, 2026; excess could be imposed from January 1, 2030 as otherwise lawful. It may change. Recheck status before relying on a banked calculation; a 90-day notice alone does not establish legality. (https://sfgov.legistar.com/LegislationDetail.aspx?ID=8217304&GUID=7EDA4662-EBFB-4AF5-962F-C669B64AA770, https://sfgov.legistar.com/View.ashx?M=F&ID=15865646&GUID=0E2E6936-000B-4597-A4EE-FBB17C19636E)

**Effect on these units is unverified (F46/F47).** The proposed text addresses banked and capital-improvement increases, but its interaction with ordinary annual increases and any particular notice requires review. The proposal is not current law. The case history does not establish any banked amount for either unit. The stated applicability date equals the introduction date and precedes the later Rent Board notice; it is not earlier than introduction. The version 1 ordinance expressly supplies both the measurement and end date, so the earlier claims that they were unavailable or contradictory have been corrected.

**Practical check:** Before notice, open the official Rent Board guidance and Legistar record, check for amendments or enactment, and save a dated copy. Seek legal advice on any proposed banked or capital-improvement increase.


## Bottom line

For a unit covered by the San Francisco Rent Ordinance, the current ordinary annual allowable increase is **1.6% effective 3/1/26-2/28/27**, once every 12 months on the tenant's anniversary date. A current Rent Increase License must be on file before the increase takes effect; the increase is calculated on base rent only, is not rounded up, and requires written notice. California's state-only AB 1482 cap is **8.8% for San Francisco 8/1/26-7/31/27**, but SF.gov says it does **not** apply to units already under the SF Rent Ordinance's rent-increase limits. No official general federal private-rent cap was found; HUD FMR/SAFMR figures are gross-rent estimates used in several federal programs, not general private rent caps.

## Case handling

The owner-supplied case facts are anonymized. Dates and dollar amounts are preserved: Unit 1 last lease start February 1, 2025 at $3,995; Unit 1 continuing tenancy/current tenants April 1, 2026 at $3,995; Unit 2 last lease start June 1, 2019 at $3,150. Tenant identifiers are replaced with placeholders Tenant A-F. No exact street address, real name, initial, or contact detail is published. The case facts themselves are now published in full on the site as clearly labelled **owner-supplied (anonymized)** rows - ZIP 94122, 1940, two units, lease dates and rents, Tenant A-F - because you asked for the entries to be readable; they are explicitly not official findings. The separate official-verification rows stay blank and flagged: exact-address coverage, the official building-year record, license status, prior increases and notice history, whether the April 1, 2026 continuation restarted the anniversary date, and the legal status of the continuing occupants were not official-verified.

Arithmetic using the supplied historical amounts and official 1.6% rate: Unit 1 $3,995 x 1.6% = $63.92 -> $4,058.92; Unit 2 $3,150 x 1.6% = $50.40 -> $3,200.40. Unit 2’s $3,150 was its 2019 lease rent, not a confirmed current base rent. These figures are conditional illustrations, not approved notices, recommendations for an actual dollar amount or eligibility determinations. No banked increase is inferred.

Unit 1's roommate change does not by itself permit extra rent. SF.gov prohibits charging more rent merely because a new/additional roommate moved in. Section 6.14 / Costa-Hawkins market-rate reset rules require specific facts about the last original occupant and the continuing occupant's legal status; those facts are unverified. SF.gov and the Rent Board strongly encourage legal advice, and Jan. 13, 2026 minutes denied an appeal because the landlord did not prove the last original occupant no longer permanently resides. No market-rate reset is recommended.

## Notice checklist

Verify coverage in SF Planning PIM; report to the Housing Inventory and confirm a current Rent Increase License; verify each unit’s current lawful base rent, fixed-term lease permission, 12-month/anniversary eligibility and notice history; use the rate in effect on the increase date; provide the required written notice with the dollar amount, percentage, effective date and banked portion if any. Generally allow 30 days, or 90 days if the increase alone or combined over the preceding 12 months exceeds 10%. Add the applicable mail-service time: five calendar days when both mailing and address are in California, and longer in other circumstances. File any required petition or worksheet before notice. Keep neutral, consistent records. (https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827&lawCode=CIV, https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1013&lawCode=CCP)

## Discrimination and one-vs-both

The federal FHA, 24 CFR 100.500 disparate-impact rule, California FEHA and SF tenant-harassment rules apply. Intent is not required for a discriminatory-effect claim; a substantial legitimate nondiscriminatory interest and no less discriminatory alternative matter. No official source requires raising both units, but an identical written neutral policy applied to each eligible unit is the conservative approach. If only one unit is raised, document neutral eligibility/anniversary reasons, not tenant identity. Nothing here claims attorney approval or guarantees that no complaint, inquiry or lawsuit will occur.

## Corporate / individual evidence

SEC filings show IRT Q4 2025 same-store LIKE-TERM new -3.7%, renewal 2.9%, blended 0.8%; those figures cover leases with 9–14-month prior and current terms, approximately 81% of Q4 leases. Its all-lease Q4 figures were new -6.2%, renewal 3.0%, blended -1.0%. Invitation Homes 2025 total-portfolio renewal was +4.6%, new -0.8%. These are portfolio-level, not SF-specific and not legal benchmarks. SF Rent Board June 2024 workload stats show 23 landlord petitions/154 units (18 capital-improvement petitions covering 148 units) and 73 tenant petitions/73 units; this is narrow formal-petition evidence only, not proof of normal small-owner practice. (https://www.sec.gov/Archives/edgar/data/1466085/000143774926003792/ex_895776.htm, https://www.sec.gov/Archives/edgar/data/1687229/000168722926000016/invh-20251231.htm)

## Banked increases and the 10% notice threshold

SF.gov distinguishes a fully skipped increase, which is banked after 24 full months without any rent increase, from the unused portion of a partial increase, which may be imposed after at least 12 months or on a future anniversary. Add eligible percentages; do not compound or prorate; banking does not carry to a new tenant. Neither unit’s history is confirmed, so no banked amount is asserted. A previously published 13.1% Unit 2 illustration is conditional arithmetic only: it assumes the same tenancy, no increases since June 1, 2019, a current lawful $3,150 base, each skipped rate properly banked, an eligible date within the 1.6% rate period, and no other limitation. Those assumptions are unverified (F30); pending File 261020 could change the analysis. A 90-day notice for a qualifying increase over 10% does not itself establish legality. (https://www.sf.gov/information--banked-rent-increases, https://www.sf.gov/information--annual-rent-increase-multiple-years)

## Unit 1, Section 6.14 and privacy

Extra rent merely because of an additional occupant is unlawful; a roommate change alone is not a market-rate reset. Under the Rent Board’s Section 6.14 description, an unlimited increase may be available after the last original occupant vacates if a timely 6.14 notice was served on each remaining subsequent occupant; generally 60 days is reasonable. That notice can be served on a later co-tenant or subtenant. The Rent Board describes a separate Costa-Hawkins path for a qualifying lawful subtenant or assignee when the last original occupant no longer permanently resides; a co-tenant is not subject to that statutory increase. These paths have distinct requirements, and case-specific occupant status and notice history are unknown (F28). Do not assume either applies. The Housing Inventory filing is public by design. (https://www.sf.gov/information--rent-increases-under-section-614-and-costa-hawkins, https://www.sf.gov/rent-board-housing-inventory)

## Flagged for Review

All {{FLAGS}} irregularities and unverified items appear on the Flagged for Review page with source links. Important open items include case-specific coverage, current base rents, anniversary and notice history, the pending proposal, fee-referral wording and historical public privacy exposure (F44). Current-tree structural checks are not proof of anonymity and cannot remove history, PR diffs or copies. Flagged items do not block the site or merge.

## Sources

{{SOURCES}} official sources are catalogued in SOURCES.md and on the Sources page (the count is computed at build time, never typed by hand). Every published table row links to at least one official source. Unverified values are blank and flagged. No value is inferred or filled from a nonofficial snippet.
"""

FLAGGED_TEXT = """# Flagged for Review

This page is clearly labeled **Flagged for Review**. Status `needs review` means the item is published with official source links for manual review and does **not** block any task or the merge.

Full detail is in `research/sources/irregularities.md`, `research/sources/unverified.md`, `research/flags.md` and `pages/flagged.html`.

## Summary of flags

- {{FLAGS}} flagged items total; {{SOURCE_FLAGS}} source-quality, notice and process flags plus case flags.
- Case coverage, current rents, licensing, banking, notice history and bedroom counts remain unverified.
- File 261020 is proposed, not enacted; its case-specific application remains open (F46/F47).
- The current tree no longer publishes raw identifiers or recoverable short-identifier fingerprints, but historic git/PR exposure remains unresolved (F44).
- HUD ZIP benchmarks are now sourced directly; they do not establish asking rents or a private rent cap (T03-F07).

Every flag on the site includes official source links. Unverified value cells are blank.
"""

README_TEXT = """# RentincreaseSF4

Public GitHub Pages research site for "Rental increase SF": executive summary, official-source-linked tables, anonymized case dashboard, analysis, and a clearly labeled Flagged for Review page.

Live site: https://kanlerxz87-cyber.github.io/RentincreaseSF4/

- `index.html` - clean landing page / dashboard.
- `pages/` - category subpages with easy-read tables, including the Rent Board Fee page (`pages/fee.html`) and the Notice Worksheet page (`pages/worksheet.html`).
- `scripts/site_*.py` - canonical content; `data/` contains generated JSON with official source IDs.
- `SOURCES.md` / `VERIFICATION.md` / `research/` - official source ledger and dated verification records; recent audits are targeted, not exhaustive.
- `EXECUTIVE_SUMMARY.md` - standalone executive summary.
- `FLAGGED_FOR_REVIEW.md` / `pages/flagged.html` - flagged irregularities with links.
- `REPO_REVIEW.md` - line-by-line repository review.
- `COORDINATION.md` - shared task board, PR and merge record.
- `scripts/build_site.py` / `scripts/validate_site.py` - static site build and validation.

Privacy: personal information is anonymized with placeholders; raw identifiers are internal-only and excluded from git and the published site. Dates and dollar amounts are preserved. No exact address is published.

Not legal advice. No attorney approval or guarantee of no complaint/lawsuit is claimed. Any increase is framed as a conservative compliance checklist capable of tenant-lawyer review.
"""

CSS_TEXT = r"""
:root{--ink:#14213d;--muted:#5b6b84;--bg:#f5f7fb;--card:#fff;--line:#dce3ef;--accent:#0b6e4f;--accent2:#1f4e79;--warn:#9a6700;--warnbg:#fff8e1;--okbg:#eaf6ef;--flagbg:#fff1f1;--flag:#a12424;--owner:#5b4b8a;--ownerbg:#f1eefc}
*{box-sizing:border-box}
body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.55}
a{color:var(--accent2);text-decoration:underline;text-underline-offset:.15em}
a:hover{text-decoration:underline}
header{background:linear-gradient(135deg,#0b2545,#134e4a);color:#fff;padding:2.2rem 1rem}
header .wrap{max-width:1120px;margin:0 auto}
header h1{margin:0 0 .35rem;font-size:2rem;letter-spacing:-.02em}
header p{margin:.2rem 0;color:#dbeafe}
nav{background:#0b2545;position:sticky;top:0;z-index:10;border-bottom:1px solid rgba(255,255,255,.15)}
nav .wrap{max-width:1120px;margin:0 auto;display:flex;flex-wrap:wrap;gap:.15rem;padding:.45rem 1rem}
nav a{color:#e8eef8;font-size:.86rem;padding:.35rem .55rem;border-radius:6px;text-decoration:none}
nav a:hover,nav a.active{background:rgba(255,255,255,.14);text-decoration:none}
main{max-width:1120px;margin:0 auto;padding:1.5rem 1rem 3rem}
.hero{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:1.4rem;margin-bottom:1.4rem;box-shadow:0 2px 10px rgba(15,35,70,.05)}
.hero h2{margin-top:0;font-size:1.5rem}
.disclaimer{background:var(--warnbg);border-left:4px solid var(--warn);padding:.8rem 1rem;border-radius:6px;font-size:.92rem;margin:1rem 0}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem;margin:1.2rem 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:1rem;box-shadow:0 2px 10px rgba(15,35,70,.04)}
.card .k{font-size:.78rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.card .v{font-size:1.7rem;font-weight:700;margin:.2rem 0;color:var(--accent2)}
.card .d{font-size:.88rem;color:var(--muted)}
.card a{font-weight:600}
section{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:1rem;margin:1.2rem 0;overflow:hidden}
section>h2{margin:0 0 .8rem;font-size:1.2rem}
.tablewrap{overflow-x:auto}
.tablewrap:focus-visible{outline:3px solid var(--accent2);outline-offset:2px}
table{width:100%;border-collapse:collapse;font-size:.9rem}
th,td{text-align:left;vertical-align:top;padding:.65rem .6rem;border-bottom:1px solid var(--line)}
th{background:#eef3fa;color:#253b5b;font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;position:sticky;top:0}
tr:last-child td{border-bottom:0}
td.blank{color:var(--muted);font-style:italic}
.badge{display:inline-block;padding:.15rem .45rem;border-radius:999px;font-size:.72rem;font-weight:700;white-space:nowrap}
.badge.verified{background:var(--okbg);color:var(--accent)}
.badge.review{background:var(--warnbg);color:var(--warn)}
.badge.analysis{background:#e8eefc;color:var(--accent2)}
.badge.owner{background:var(--ownerbg);color:var(--owner)}
.owner-src{font-size:.78rem;color:var(--owner)}
td.blank{color:var(--warn);font-style:italic}
@media print{nav,.cta{display:none}section,.hero{box-shadow:none}}
.src a{display:inline-block;margin:0 .25rem .2rem 0;font-size:.78rem;background:#eef3fa;border:1px solid #d3ddef;padding:.1rem .35rem;border-radius:5px}
.flaglink{font-weight:700;color:var(--flag)}
.flagged-banner{background:var(--flagbg);border:1px solid #f0c2c2;border-left:5px solid var(--flag);padding:1rem;border-radius:10px;margin:1rem 0}
.flagitem{border:1px solid var(--line);border-radius:10px;padding:.8rem 1rem;margin:.7rem 0;background:#fff}
.flagitem h3{margin:0 0 .25rem;font-size:1rem}
.flagitem .id{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--flag);font-weight:700}
footer{border-top:1px solid var(--line);color:var(--muted);font-size:.85rem;padding:1.2rem;text-align:center}
footer .wrap{max-width:1120px;margin:0 auto}
.small{font-size:.82rem;color:var(--muted)}
ul{margin:.4rem 0 .4rem 1.2rem}
.narrative h2{margin:1.4rem 0 .5rem;font-size:1.18rem;color:var(--accent2);border-bottom:1px solid var(--line);padding-bottom:.35rem}
.narrative p{margin:.6rem 0}
.narrative ol,.narrative ul{margin:.5rem 0 .9rem 1.3rem;padding:0}
.narrative li{margin:.35rem 0}
.narrative a{word-break:break-word}
.narrative>h2:first-child{margin-top:0}
@media(max-width:700px){nav{position:static}header h1{font-size:1.55rem}nav .wrap{padding:.35rem .5rem}main{padding:1rem .6rem 2rem}th,td{padding:.5rem .45rem}}
"""
