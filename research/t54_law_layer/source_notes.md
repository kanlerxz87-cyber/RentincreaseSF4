# T54 - State-vs-local classification of the "inform the Rent Board" duty

Session `arena-415e54ea`, 2026-11-13 UTC. Every statement below was read directly from the
primary official page on the date shown. No value is inferred.

## The question being answered

> "I read somewhere that I have to inform the rent board SF about rent increase for rent
> controlled units since the law passed in 2023. Is that a state or local law?"

## Findings

### 1. The Rent Increase License / Housing Inventory duty is LOCAL (San Francisco)

| Fact | Verified text | Source |
| --- | --- | --- |
| Enacted by | "Added by Ord. No. 265-20, effective January 18, 2021" | S53 |
| Operative date, 10+ unit buildings | "reported to the Rent Board by July 1, 2022" | S53 |
| Operative date, condominiums and buildings with fewer than 10 units | "shall be reported commencing March 1, 2023 and updated annually by March 1 of each successive year" | S53 |
| Rule restating the same dates | Rule 13.14: "shall apply to all rent increases that are effective on or after July 1, 2022, except that with respect to condominium units and buildings with less than ten residential units, this section shall only apply to rent increases that are effective on or after March 1, 2023." | S73 |
| The consequence | Rule 13.14: an increase "purporting to be effective while the landlord is unlicensed shall render the entire rent increase null and void; provided, however, that the effective date of the rent increase, not the date of service, shall be used" | S73 |
| Which government | Rent Board of the City and County of San Francisco; the provision sits in the San Francisco Administrative Code, Chapter 37 (the Rent Ordinance) | S21, S53, S74 |

**Conclusion:** the reporting + license requirement is a **San Francisco local ordinance**, not a
state statute. There is **no** state-law requirement that an owner report a rent increase to the
SF Rent Board.

### 2. Where the "2023" date comes from

`2023` is the year the **local** reporting/licensing duty became operative for **condominiums and
buildings with fewer than 10 residential units** (S53, S73, S07, S01). It is not the year a state
law passed. The ordinance itself was enacted in 2020 (Ord. 265-20), effective January 18, 2021;
large buildings began reporting July 1, 2022; small buildings began March 1, 2023.

A two-unit 1940 building such as this one falls in the **small-building** group, so its operative
date is **March 1, 2023** - which is almost certainly the "law passed in 2023" the owner read.

### 3. What the actual 2023 state law (SB 567) does - and does not - do

| Fact | Verified text | Source |
| --- | --- | --- |
| Bill | SB 567 (Durazo), Chapter 290, Statutes of 2023; approved and filed with the Secretary of State September 30, 2023 | S88 |
| Subject | "Termination of tenancy: no-fault just causes: gross rental rate increases"; amends, repeals and adds Civil Code sections 1946.2 and 1947.12 | S88 |
| Operative date | Section 1947.12(n): "This section shall become operative on April 1, 2024." Section 1946.2(m) likewise becomes operative April 1, 2024 | S88 |
| State rent cap formula | 5% plus the percentage change in the cost of living, or 10%, whichever is lower | S88, S36 |
| Does it require registration with a local rent board? | No such requirement appears in the bill text. The duties created are (a) just-cause eviction rules, (b) the statewide rent cap, (c) treble damages and AG/city-attorney enforcement, (d) notice requirements | S88, S36 |
| Enforcement | Section 1947.12(k): tenant civil action; Attorney General, city attorney or county counsel may enforce and seek injunctive relief | S88 |

**Conclusion:** the 2023 state law is a **just-cause and rent-cap** law. It does **not** create a
duty to inform the San Francisco Rent Board of a rent increase.

### 4. Why the state cap does not set this owner's number

Civil Code section 1947.12(d)(3) excludes: "Housing subject to rent or price control through a
public entity's valid exercise of its police power consistent with Chapter 2.7 (commencing with
Section 1954.50) that restricts annual increases in the rental rate to an amount less than that
provided in subdivision (a)." (S36, verified 2026-11-13, chunk 0.)

SF.gov states the same result from the local side: AB 1482 does **not** apply to units already
under the San Francisco Rent Ordinance's rent-increase limits (S27). The operative local number is
**1.6% for 3/1/26-2/28/27** (S01, S02, S04).

So for a *covered* San Francisco unit, the state 8.8% figure is **not** the ceiling; the local
1.6% is, and the local licensing, notice and anniversary rules apply on top.

### 5. The coverage question that comes before all of it

S06: "Many residential units built on or before June 13, 1979 have both rent control and eviction
protection," and the first step is to check the building year in the SF Planning Property
Information Map (S32). The owner supplies 1940 and two rented units, which is the paradigm covered
case, but the official record has **not** been checked - that stays blank and flagged (CASE-V1,
CASE-V2).

## What this adds to the site

- A **Law Layers** table on the Local Law page: for each layer (local / state / federal), whether
  it creates a duty to inform the Rent Board, with the official source.
- A **forefront block** on the Executive Summary and the landing page answering the state-vs-local
  question directly.
- New flag **F53** recording the attribution and the exact official basis for the correction.

## Verification performed

Direct `fetch_page` on 2026-11-13 (all returned the text quoted above):

1. <https://www.sf.gov/information--sec-3715-reporting-obligations-licensing> - "Added by Ord. No. 265-20, effective January 18, 2021"; subsection (c) dates.
2. <https://www.sf.gov/rent-board-housing-inventory> - "All owners of residential property are required to report"; March 1 deadline; license generated; fee exemption is separate.
3. <https://www.sf.gov/learn-about-rent-increases-san-francisco> - 1.6% 3/1/26-2/28/27; "must get a rent increase license before imposing"; operative dates "July 1, 2022 (or March 1, 2023 for condominiums and buildings with 1-9 residential units)".
4. <https://sf.gov/news/new-legislation-creates-housing-inventory-and-requires-owners-obtain-license-imposing> - "Ordinance No. 265-20, which became effective on January 18, 2021".
5. <https://www.sf.gov/reports--december-2022--rent-board-rules-and-regulations-part-xiii-reporting-obligations-under-rent> - Rule 13.14 full text.
6. <https://www.sf.gov/information--sec-373-rent-limitations> - Section 37.3(a)(1) license condition and 60%-of-CPI / 7% ceiling.
7. <https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB567> - SB 567 chaptered text, digest, Section 1947.12(n) operative date.
8. <https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV> - current Section 1947.12, including subdivision (d)(3) exclusion.
9. <https://www.sf.gov/learn-about-san-francisco-rental-laws> - June 13, 1979 cutoff and exemption list.

No secondary source was used for any legal statement. Search results were used **only** to locate
the primary pages, never as the authority for a row.

## Irregularities / limits

- The site's earlier pages asserted the licence dates correctly but never said **which layer of
  government** imposed them, and `grep -i "state or local"` over the generator returned nothing.
  That is the gap this task closes; it is not an error in any prior value.
- SB 567 contains no rent-board reporting duty, but this is a **negative finding** (absence of a
  requirement in the text). It is stated as "no such requirement appears in the bill text", not as
  "the law forbids it".
- Whether the subject units are covered is still unverified (CASE-V1, CASE-V2). Nothing in this
  document asserts coverage.
- Not legal advice. No attorney has reviewed this analysis.
