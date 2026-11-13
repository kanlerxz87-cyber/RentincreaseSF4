# T54 (session `arena-6f65a2f5`) — verification record and integration log

Branch `arena/6f65a2f5-rentincreasesf4`, 2026-11-13 UTC.

**Why this file is not `README.md` in this folder:** two parallel sessions both claimed task `T54` on the shared board and
both wrote a record at `research/t54_suggestions/README.md`. Session `arena-87a91aec`'s record is the one merged to `main`
and it stays at that path untouched; this session's record is preserved here as a sibling so neither is lost. Read
`README.md` in this folder first for that session's Suggestions & Review page and its own 2026-11-13 re-verification;
this file documents this session's line-by-line re-read of the licensing, ordinance-provenance and Civil Code sources,
the state-backstop layer that was missing from the site, and the two merge rounds that integrated the overlapping work.

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

## 6. Integration with a colliding parallel session (2026-11-13)

While this session's work was uncommitted, another session (`arena-23a50992`, PRs #51/#52/#55, merged to `main` as
`038f2e6`) implemented the **same two brief items**: a Suggestions page and the state-vs-local answer. This was a
coordination failure, not a content dispute — the board row for `T54` was claimed by both sessions.

**Resolution strategy: main became the shared base; nothing from either session was discarded.**

1. `git merge --no-commit origin/main`, then every generated or shared file (`scripts/`, `pages/`, `data/`, root `.md`,
   `assets/`, `.github/`, `research/c72_.../validate_c72.py`) was reset to **main's version** (`git checkout origin/main -- ...`),
   so the merge commit carries no interleaved half-adopted state. This session's own verification record was the only file kept
   as-is from the pre-merge tree.
2. Overlapping content that main already published was **not re-added**: the state-vs-local answer (main's `SL-01`–`SL-05`,
   `LAW-01`–`LAW-08`, `REQ-26`–`REQ-28`, flag `F53`), the ordinance provenance sources (main's `S90` = the SF.gov news item,
   `S92` = the Ord. 265-20 attachment, `S89` = Civ. Code 1946.2), the licence-scope rows (`PRC-07`, `LOC-15`), and the
   suggestion groups with effort and review status (`SUG-A1`–`A7`, `SUG-B1`–`B6`, `SUG-C1`–`C6`).
   Source IDs were **not** reused or renumbered: this session's four new sources became main's `S90`/`S92`/`S89` plus one new row.

**What this session then added on top (all verifiable, none duplicative):**

| Added | Where | Why it was still missing |
| --- | --- | --- |
| **S93** Civil Code §1947.7 read directly | `SOURCES.md`, Sources page | Main cited only §37.15(d)'s non-registry disclaimer (in `LOC-14`); the state penalty shield an owner would look for was not in the ledger |
| **LAW-09** the statute-versus-scope distinction | Local Law page | Main answered *where* the duty lives, not whether the state shield softens it |
| **ST-18 / ST-19** §1947.7 as read, and what it does not do | State Law page | No state-side row quoted the section |
| **Q-22** applicability, blank + **F59** | Questions page | Unresolved on the official record — deliberately not answered by inference |
| **LIC-11 / LIC-12** Rule 13.14 verbatim; the individual owner's actual exposure | Executive Summary | Main *paraphrased* the rule; the verbatim text is the strongest wording in the record and narrows `F25` |
| **AN-30** do not substitute a state statute for the free report | Analysis | Turns the §1947.7 finding into an action, without advising |
| **SUG-P6 + section D (`SUG-D1`–`SUG-D8`)** owner decision record, 8 blank rows + **F60** | Suggestions page | Main's board listed options and effort but had nowhere to record a choice, which is what the brief asked for |
| **F01 / F02 / F25** narrowed with today's page text; **F46** + `RATE-12/14/17` + `S71`/`S73` re-dated | Flags page, Rates page, ledger | Main's versions still carried the 2026-11-10 wording and left the File 261020 status undated |
| 11 new validator checks (156 total) | `scripts/validate_site.py` | Locks the decision grid (8 blank rows, all flagged), the verbatim quotations, the re-check dates and the ledger total |

**One defect found in main and corrected here rather than left:** the 2026-11-13 addendum in `SOURCES.md` said
"91 catalogued sources: 89 official" while its own ledger already held 92 rows (`S88`–`S92`) — a stale hand-typed total that
the validator missed because it only tests that the current count string appears *somewhere* in the file. The prose now reads
"93 catalogued sources: 91 official ... plus two project records", and a new check (`"{n} catalogued sources" in SOURCES.md`)
makes that total exact so it cannot drift again.

**Gates after the merge:** `validate_site.py` 156 checks / 0 errors · b87 kit 19 / 0 · c72 19 / 0 · privacy scan 0 matches ·
two consecutive builds byte-identical over 57 published files.

## 7. Second integration round (2026-11-13, same day)

After the first merge was pushed, three more branches merged to `main` (PRs #54, #56, #57) and PR #58 could not be merged
because `main` had moved again — with a conflict. The same procedure was used a second time, and it is recorded here
because it changed what this session published:

1. `git merge --no-commit origin/main`, then **every** generated and shared path (`scripts/`, `data/`, `pages/`,
   `assets/`, `research/`, `.github/`, root `*.md`, `index.html`) was reset to main's version with
   `git checkout origin/main -- ...`, so no interleaved auto-merge survived. An earlier attempt that relied on
   `git checkout --theirs` left a duplicated `LIC-11` row in the tree — caught by the validator's unique-row-ID check,
   which is why the reset-the-whole-tree form is the one to use. The merge commit is otherwise empty of content.
2. Everything main had published in the meantime was **not** re-added. Dropped from this session's plan as duplicative:
   - the owner decision grid (`SUG-D1`–`SUG-D8` with a blank decision cell and a "blank by design" flag) — main already
     generates `CL-*` blank reviewer rows for every T54 proposal in `scripts/site_suggestions.py`, so a second grid would
     have been noise. The flag that would have covered it was not added either.
   - the "state-vs-local" rows, the ordinance-provenance sources and the suggestions how-to groups, all already on main.
3. What was still genuinely missing and therefore re-applied, with ids moved to free slots (main had taken `LIC-11`,
   `LIC-12`, `Q-22`, `Q-23`, `Q-24` in the meantime):

| Re-applied | New id | Was |
| --- | --- | --- |
| Civil Code 1947.7 read directly, catalogued as an official source | `S93` | (new) |
| the statute-versus-scope question on the Local Law page | `LAW-09` | (new) |
| section 1947.7 as read, and what it does not do | `ST-18`, `ST-19` | (new) |
| applicability question, blank with a discovery route | `Q-25` | was `Q-22` |
| Rule 13.14 verbatim in the forefront summary; the individual owner's real exposure | `LIC-13`, `LIC-14` | were `LIC-11`, `LIC-12` |
| do-not-substitute-a-statute recommendation | `AN-30` | (new) |
| `F59` (1947.7 unresolved); `F01`/`F02` narrowed to today's page text; `F25` amended with the rule text, not closed; `F46` re-dated | flags | — |
| `RATE-12`/`RATE-14`/`RATE-17` currency stamps; `S71`/`S73` re-verification dates | rows/sources | — |
| executive summary: Rule 13.14 verbatim in step 4, the state-backstop paragraph, the dated recheck scope, flagged-item prose through `F59` | `EXECUTIVE_SUMMARY.md` | — |
| `SOURCES.md`: the `S93` ledger row, the addendum, and the stale total corrected (main's prose said "91 catalogued sources: 89 official" against a 92-row ledger) + a check that pins the exact phrase | ledger | — |

**Gate results after the second round:** `scripts/validate_site.py` 153 checks / 0 errors on main's baseline, and after the
residual checks are added the published figure is in `data/validation_report.json` · `research/b87_notice_kit/validate_kit.py`
19 / 0 · `research/c72_2026-11-11_audit/validate_c72.py` 19 / 0 · `research/n08_qa/privacy_check.py` 0 matches · two
consecutive builds byte-identical.

**Process lesson for the board (worth repeating to other sessions):** claiming `T54` twice is how two sessions produced
the same page. The board works when the task line, not just the title, is unique — and when a session pulls `main`
*immediately* before opening its PR, because a merged `main` is the only reliable claim on shared files.
