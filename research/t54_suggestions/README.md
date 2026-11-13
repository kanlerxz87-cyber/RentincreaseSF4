# T54 — 2026-11-13 verification record (session `arena-6f65a2f5`)

Two deliverables in the owner's brief were not satisfied by the published site, and one
load-bearing question was answered only implicitly:

1. *"create a section dedicated for suggestions so someone can review suggestions and choose
   the best path before implementing any changes"* → no Suggestions page, no NAV entry, no card,
   no requirements row existed (grep of `pages/`, `data/`, `scripts/` for "suggest" returned only
   `TENANT_ASSISTANCE_RESEARCH.md`).
2. *"I read somewhere that I have to inform the rent board SF about rent increase for rent
   controlled units since the law passed in 2023. Is that a state or local law?"* → the site
   stated the March 1, 2023 phase-in date and cited Sec. 37.15, but never named the level of
   government, never cited the enacting ordinance's own text, and never addressed the 2023
   **state** law a reader is most likely to have encountered.

Everything below was read directly with `fetch_page` on **2026-11-13** (no search snippet was
used as authority). Verbatim quotes are reproduced so a human can re-check each claim against
the same official page.

## 1. The duty is local — primary text

**SF Administrative Code Sec. 37.15 (Rent Board's own copy, S53)** — closing note of the
section, verbatim:

> \[Added by Ord. No. 265-20, effective January 18, 2021\]

and Sec. 37.15(c):

> For units (other than condominium units) in buildings with 10 units or more, the information
> described in subsection (b) shall be reported to the Rent Board by July 1, 2022, and updated by
> March 1, 2023 and annually by March 1 of each successive year. For condominium units and units
> in buildings with fewer than 10 units, the information shall be reported commencing March 1,
> 2023 and updated annually by March 1 of each successive year.

and Sec. 37.15(d):

> The Rent Board shall not use the information to operate a rental registry within the meaning of
> California Civil Code Sections 1947.7 – 1947.8.

and Sec. 37.15(e):

> If a landlord has substantially complied with the obligation to report information about a rental
> unit as required under this Section 37.15, the landlord shall receive a license to impose rent
> increases on tenants in that unit under Sections 37.3(a)(1)-(2). If the landlord has not
> substantially complied ... the license to impose rent increases shall be temporarily suspended
> during the period of the landlord's noncompliance ... but a tenant shall not be obligated to pay
> the increased rent for months during the period of suspension.

**SF.gov news item, Jan. 22, 2021 (new source S88)** —
<https://www.sf.gov/news/new-legislation-creates-housing-inventory-and-requires-owners-obtain-license-imposing>:

> Ordinance No. 265-20, which became effective on January 18, 2021, requires owners of residential
> housing units in San Francisco to begin reporting certain information about their units to the
> Rent Board.

> For condominium units and units in buildings with less than 10 residential units, reporting will
> begin on March 1, 2023 with updates due every March 1 thereafter.

> In addition, the legislation requires owners to obtain a license from the Rent Board before
> imposing any annual and/or banked rent increases upon tenants. The license will only be issued by
> the Rent Board if the owner is in substantial compliance with the housing inventory's reporting
> requirements.

**Ordinance No. 265-20 file attachment (new source S89)** —
<https://sfgov.legistar.com/View.ashx?M=F&ID=9024120&GUID=79C40690-896E-43CD-9855-77B3AC909AEF>:

> Ordinance amending the Administrative Code to require owners of residential dwelling units to
> report certain information to the Rent Board; to authorize the Rent Board to issue a license to
> owners who report the information; and to require that an owner have a license to impose certain
> types of rent increases ...
> Be it ordained by the People of the City and County of San Francisco:
> Section 1. Purpose and Findings. ... in directing the Rent Board to create a housing inventory,
> the Board of Supervisors does not intend that the Rent Board should set rents through a rent
> registry ...
> Section 2. The Administrative Code is hereby amended by revising Section 37.3; adding new
> Section 37.15; and renumbering existing Section 37.15 as Section 37.16 ...

*Recorded limitation:* the attachment renders as the Board's redline/Master Report (amendment
markup visible in the text). The enacted wording was therefore read from the codified section
(S53) and used only for the ordinance's title, purpose and the fact that a **City** enactment
created the duty. This is stated on source S89 and on row LOC-26.

**Rent Board Rules Part XIII, Rule 13.14 (S73), adopted July 12, 2022** — verbatim:

> Any rent increase under Ordinance Sections 37.3(a)(1)-(2) purporting to be effective while the
> landlord is unlicensed shall render the entire rent increase null and void; provided, however,
> that the effective date of the rent increase, not the date of service, shall be used to determine
> whether or not the increase conforms with the provisions of this section. Nothing in this
> Regulation shall affect a landlord's banking rights or the ability to accumulate otherwise lawful
> rent increases that were found to be null and void.
> This section shall apply to all rent increases that are effective on or after July 1, 2022,
> except that with respect to condominium units and buildings with less than ten residential units,
> this section shall only apply to rent increases that are effective on or after March 1, 2023.

**Sec. 37.3(a)(1) (S21)** — verbatim:

> A landlord who has reported the required information about their rental unit to the Rent Board as
> set forth in Section 37.15 shall have a license to impose annually a rent increase which does not
> exceed a tenant's base rent by more than 60% of said published increase. In no event, however,
> shall the allowable annual increase be greater than 7%.

## 2. The 2023 state law is a different subject

**Civil Code Sec. 1947.12 (S36), current text and its own history note** — verbatim:

> (a)(1) ... shall not, over the course of any 12-month period, increase the gross rental rate for a
> dwelling or a unit more than 5 percent plus the percentage change in the cost of living, or 10
> percent, whichever is lower ...
> (d)(3) Housing subject to rent or price control through a public entity's valid exercise of its
> police power consistent with Chapter 2.7 (commencing with Section 1954.50) that restricts annual
> increases in the rental rate to an amount less than that provided in subdivision (a).
> (e) An owner shall provide notice of any increase in the rental rate, pursuant to subdivision (a),
> to each tenant in accordance with Section 827.
> _(Repealed (in Sec. 3) and added by Stats. 2023, Ch. 290, Sec. 4. (SB 567) Effective January 1,
> 2024. Operative April 1, 2024. Repealed as of January 1, 2030, by its own provisions.)_

**Civil Code Sec. 1946.2 (new source S90)**, read in full (chunks 1–3): subdivision (d)(4)
> An owner's failure to strictly comply with this subdivision shall render the notice of termination
> void.

(e)(6) two-unit owner-occupied exemption, (f) the 12-point-type notice, (i)(1)–(2) the local
just-cause displacement rule; history note
> _(Amended by Stats. 2025, Ch. 203, Sec. 1. (AB 1529) Effective January 1, 2026. Repealed as of
> January 1, 2030, by its own provisions.)_

**Neither section, as read, contains any duty to notify a rent board before a rent increase.** That
is recorded as an absence finding limited to the sections read (S35 §827, S36 §1947.12, S57 §1942.5,
S90 §1946.2, S91 §1947.7) — flag **F55** — not as a certified exhaustive search of the Codes.

**SF.gov AB 1482 page (S27)** confirms the state amendment and its inapplicability to these units:

> The maximum rent increase for units under AB 1482 from August 1, 2026 to July 31, 2027 is 8.8% in
> San Francisco.
> This does NOT apply for units under the rent increase limitations of the San Francisco Rent
> Ordinance.
> ... It is amended by SB 567.
> The current applicable CPI increase for San Francisco (that is, from August 1, 2026 to July 31,
> 2027), is 3.8%.

**Civil Code Sec. 1947.7 (new source S91)** — the state backstop an owner might hope for, and why it
is uncertain here — verbatim:

> it is the intent of the Legislature to limit the imposition of penalties and sanctions against an
> owner of residential rental units where that person has attempted in good faith to fully comply
> with the regulatory processes of those programs.
> (b) An owner of a residential rental unit who is in substantial compliance with an ordinance or
> charter that controls or establishes a system of controls on the price at which residential rental
> units may be offered for rent or lease and which requires the registration of rents ... shall not
> be assessed a penalty or any other sanction for noncompliance ...
> (c) ... all annual rent adjustments which may have been denied during the period of the owner's
> noncompliance shall be restored prospectively once the owner is in compliance ...

Because Sec. 37.15(d) says the Rent Board shall **not** operate a rental registry "within the
meaning of California Civil Code Sections 1947.7 – 1947.8", no answer is given on the site; the
question is published blank as **Q-24** with flag **F56**.

## 3. Load-bearing case values re-checked (all held)

| Checked 2026-11-13 | Official page | Result |
| --- | --- | --- |
| 1.6% for 3/1/26–2/28/27; 1.4% 3/1/25–2/28/26; 1.7% 3/1/24–2/28/25 | S01, S02 | Unchanged; no 2027–28 rate published → **F27 stays open** |
| "A landlord must get a rent increase license before imposing annual allowable and/or banked rent increases"; effective 7/1/2022, or 3/1/2023 for condos and 1–9 unit buildings | S01 | Unchanged |
| 30-day notice; 90-day if >10% alone or combined in the same year; +5 days if mailed; contents (dollar amount, percentage, effective date, banked portion); use the rate in effect on the increase date; base rent only; no rounding up | S01, S05 | Unchanged |
| All owners report; free; March 1; licence auto-generated; "will not be enforceable without having a rent increase license on the effective date"; no monetary penalty for late filing; inventory data public | S07 | Unchanged |
| "may be null and void (this may apply for multiple years)"; "ONLY to units under San Francisco Rent Control"; not required for §6.14/Costa-Hawkins or passthroughs; ALJ hearing route | S08 | Unchanged; the softer wording versus Rule 13.14 is why **F25** was updated rather than closed |
| 24 full months before a skipped increase banks; no compounding or proration; add percentages | S05 | Unchanged |
| Security-deposit interest 4.2% for 3/1/26–2/28/27; bankable Rent Board fee rows 2023-24 and 2024-25 at $29.50 tenant / $29.50 landlord | S02 | Unchanged |
| File 261020 notice posted November 9, 2026; "This legislation has not been enacted and is subject to change" | S02, S01, S05 | Unchanged → **F46/F47 stay open** |
| Link labeled "575 Cap. Imp. Labor Rates" still points to the Form 574 Imputed Interest PDF | S02 | Defect still live → **F45 stays open** |
| SF.gov example wording defects: "annual allowable increase in effect on June 1, 2025 is 1.6%" (that is the 6/1/2026 rate); banked example's sentence "annual allowable rent increase in effect on August 1, 2024 (1.4%)" (the example's effective date is August 1, 2025; the page itself labels 8/1/2024 as 1.7%) | S01, S05 | **F01/F02 narrowed to what the pages actually say today**, not deleted |

## 4. A link that was tested instead of assumed

The owner-noncompliance page (S08) links "Housing Inventory" to
`https://www.sf.gov/rent-board-housing-inventory-link/`. It was fetched directly and **resolves**
to the same official Housing Inventory page, so no defect flag was raised. Recorded here so a
later session does not re-propose it as a broken link.

## 5. Site gates run for this pass

| Gate | Result |
| --- | --- |
| `python3 scripts/build_site.py` | 23 data files, 21 page HTML files (index + 21 pages), assets, 3 markdown deliverables |
| `python3 scripts/validate_site.py` | **140 checks, 0 errors** (91 sources, 74 flags, 410 rows, 75 needs-review rows, 0 broken internal links) |
| `python3 research/b87_notice_kit/validate_kit.py` | 19 checks, 0 errors |
| `python3 research/c72_2026-11-11_audit/validate_c72.py` | 19 checks, 0 errors (22 HTML pages, 2,129 hrefs, 0 broken links, 0 broken anchors) |
| `python3 research/n08_qa/privacy_check.py` | no matching initials pattern in the anonymized case files |
| Reproducibility | rebuild produced byte-identical `index.html`, `pages/`, `data/`, `assets/` (46 files, sha-256 compared) |

**Cross-scope edit recorded:** `research/c72_2026-11-11_audit/validate_c72.py` asserted
`len(html_files) == 21`, a hard-coded page count that failed the moment the Suggestions page was
added, even though its broken-link list was empty. The assertion is now `>= 21` with the actual
count printed in the detail line. The owner session for that file finished and merged on
2026-11-11; the change preserves the check's meaning and is logged in `COORDINATION.md`.

## 6. What the Suggestions page deliberately does not do

Every `SG-*` row has status `analysis` (a reasoned proposal), never `verified`; the eight `DEC-*`
rows are blank with flag `F54` so the site takes no position on the owner's choices; no suggestion
changes a rate, date, dollar amount or legal conclusion; and row `SG-54` records the suggestions
that were rejected by design (computing a banked total from missing history, asserting a
vacancy-based reset, quoting an unpublished 2027–28 rate, or describing an increase as
approved/certified/challenge-proof). Flag `F53` states that nothing on the page has been
implemented.
