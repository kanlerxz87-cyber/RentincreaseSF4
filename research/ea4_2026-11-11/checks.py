#!/usr/bin/env python3
"""EA4-V arithmetic and date checks (2026-11-11).

Exact decimal arithmetic only. The banking method below is the one shown in the
Rent Board's own worked examples on
https://www.sf.gov/learn-about-rent-increases-san-francisco
(quoted in VERIFICATION_LEDGER.md, S01 items 7 and 8). The script first
reproduces both official examples and stops if it cannot.

It reads no private data and writes nothing except its own printed output.
The case amounts and dates are the owner-supplied figures already published on
the site (rows CASE-08, CASE-09, CASE-14, CASE-15).
"""
from __future__ import annotations

import re
import sys
from datetime import date, timedelta
from decimal import Decimal as D, ROUND_HALF_UP
from pathlib import Path

# Form 571 (S04), fetched 2026-11-11: (first day, last day, percent)
RATES = [
    (date(2019, 3, 1), date(2020, 2, 29), D("2.6")),
    (date(2020, 3, 1), date(2021, 2, 28), D("1.8")),
    (date(2021, 3, 1), date(2022, 2, 28), D("0.7")),
    (date(2022, 3, 1), date(2023, 2, 28), D("2.3")),
    (date(2023, 3, 1), date(2024, 2, 29), D("3.6")),
    (date(2024, 3, 1), date(2025, 2, 28), D("1.7")),
    (date(2025, 3, 1), date(2026, 2, 28), D("1.4")),
    (date(2026, 3, 1), date(2027, 2, 28), D("1.6")),
]
FAILS: list[str] = []


def rate_on(day: date) -> D | None:
    for first, last, pct in RATES:
        if first <= day <= last:
            return pct
    return None  # not published (for example on or after 2027-03-01)


def add_years(day: date, years: int) -> date:
    return day.replace(year=day.year + years)


def allowable(start: date, increase: date) -> tuple[D, D | None, list[tuple[date, D]]]:
    """Return (banked %, annual % or None if unpublished, banked detail).

    Assumes no rent increase at all between `start` and `increase`.
    An increase that first became available on an anniversary A is banked only
    if a full 12 months have passed between A and the increase date.
    """
    if increase < add_years(start, 1):
        raise ValueError("no increase is allowed in the first 12 months")
    banked: list[tuple[date, D]] = []
    k = 1
    while add_years(start, k) <= increase:
        anniversary = add_years(start, k)
        if add_years(anniversary, 1) <= increase:
            pct = rate_on(anniversary)
            assert pct is not None
            banked.append((anniversary, pct))
        k += 1
    return sum((p for _, p in banked), D("0")), rate_on(increase), banked


def money(x: D) -> D:
    return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)


def check(label: str, got, want) -> None:
    ok = got == want
    print(f"{'PASS' if ok else 'FAIL'}  {label}: {got}" + ("" if ok else f"  (expected {want})"))
    if not ok:
        FAILS.append(label)


print("== 1. The method reproduces the Rent Board's own examples ==")
b, a, _ = allowable(date(2023, 6, 1), date(2026, 6, 1))
check("official example, move-in 2023-06-01, increase 2026-06-01: banked %", b, D("3.1"))
check("official example, same: annual %", a, D("1.6"))
check("official example, same: new rent on $1,000", money(D("1000") * (1 + (b + a) / 100)), D("1047.00"))
b, a, _ = allowable(date(2023, 6, 1), date(2026, 5, 1))
check("official example, increase moved to 2026-05-01: banked %", b, D("1.7"))
check("official example, same: annual %", a, D("1.6"))
check("official example, same: new rent on $1,000", money(D("1000") * (1 + (b + a) / 100)), D("1033.00"))

print("\n== 2. Published 1.6% figures ==")
U1, U2 = D("3995"), D("3150")
check("Unit 1 1.6% increase", money(U1 * D("0.016")), D("63.92"))
check("Unit 1 new base rent", money(U1 * D("1.016")), D("4058.92"))
check("Unit 2 1.6% increase", money(U2 * D("0.016")), D("50.40"))
check("Unit 2 new base rent", money(U2 * D("1.016")), D("3200.40"))

print("\n== 3. Unit 1, IF the 2025-02-01 tenancy continues and rent was never raised ==")
START1 = date(2025, 2, 1)
for day, want_b, want_a in [
    (date(2027, 1, 1), D("0"), D("1.6")),
    (date(2027, 1, 31), D("0"), D("1.6")),
    (date(2027, 2, 1), D("1.4"), D("1.6")),
    (date(2027, 2, 28), D("1.4"), D("1.6")),
    (date(2027, 3, 1), D("1.4"), None),
]:
    b, a, _ = allowable(START1, day)
    check(f"Unit 1 effective {day}: banked %", b, want_b)
    check(f"Unit 1 effective {day}: annual % (None = not yet published)", a, want_a)
check("Unit 1 3.0% increase", money(U1 * D("0.030")), D("119.85"))
check("Unit 1 new base rent at 3.0%", money(U1 * D("1.030")), D("4114.85"))
check("Unit 1 monthly amount of the 1.4% that is lost by an earlier date", money(U1 * D("0.014")), D("55.93"))

print("\n== 4. Unit 2, IF rent was never raised since 2019-06-01 ==")
START2 = date(2019, 6, 1)
b, a, detail = allowable(START2, date(2027, 2, 1))
check("Unit 2 effective 2027-02-01: banked %", b, D("11.5"))
check("Unit 2 effective 2027-02-01: annual %", a, D("1.6"))
check("Unit 2 banked years", [str(d) for d, _ in detail],
      ["2020-06-01", "2021-06-01", "2022-06-01", "2023-06-01", "2024-06-01", "2025-06-01"])
b2, a2, _ = allowable(START2, date(2027, 2, 28))
check("Unit 2 effective 2027-02-28: total %", b2 + a2, D("13.1"))
b3, a3, _ = allowable(START2, date(2027, 6, 1))
check("Unit 2 effective 2027-06-01: banked %", b3, D("13.1"))
check("Unit 2 effective 2027-06-01: annual % (None = not yet published)", a3, None)
check("Unit 2 13.1% increase", money(U2 * D("0.131")), D("412.65"))
check("Unit 2 new base rent at 13.1%", money(U2 * D("1.131")), D("3562.65"))
check("Unit 2 banked 11.5% alone", money(U2 * D("0.115")), D("362.25"))
check("Unit 2 10.0% increase", money(U2 * D("0.100")), D("315.00"))
check("Unit 2 new base rent at 10.0%", money(U2 * D("1.100")), D("3465.00"))
check("Unit 2 banked percent used in a 10.0% increase", D("10.0") - D("1.6"), D("8.4"))
check("Unit 2 banked percent left after a 10.0% increase", D("11.5") - D("8.4"), D("3.1"))

print("\n== 5. File 261020 as introduced (NOT law): banked part capped at 10% of the lowest base rent ==")
cap = money(U2 * D("0.10"))
check("Unit 2 cap on the banked part", cap, D("315.00"))
check("Unit 2 cap plus the 1.6% annual increase", cap + money(U2 * D("0.016")), D("365.40"))
check("Unit 2 new base rent under the proposed cap", U2 + cap + money(U2 * D("0.016")), D("3515.40"))
check("Unit 2 banked amount deferred under the proposed cap", money(U2 * D("0.115")) - cap, D("47.25"))
check("Unit 1 banked 1.4% is under a 10% cap", D("1.4") <= D("10"), True)

print("\n== 6. Latest notice dates by simple day count (serve earlier) ==")
for eff in (date(2027, 2, 1), date(2027, 2, 28)):
    for days, how in ((30, "30 days, handed over"), (35, "30 days + 5, mailed"),
                      (90, "90 days, handed over"), (95, "90 days + 5, mailed")):
        print(f"      effective {eff}: {how}: on or before {eff - timedelta(days=days)}")
check("30-day notice for 2027-02-01, handed over", date(2027, 2, 1) - timedelta(days=30), date(2027, 1, 2))
check("30-day notice for 2027-02-01, mailed", date(2027, 2, 1) - timedelta(days=35), date(2026, 12, 28))
check("90-day notice for 2027-02-28, handed over", date(2027, 2, 28) - timedelta(days=90), date(2026, 11, 30))
check("90-day notice for 2027-02-28, mailed", date(2027, 2, 28) - timedelta(days=95), date(2026, 11, 25))
check("90-day notice for 2027-02-01 would have been due (already past on 2026-11-11)",
      date(2027, 2, 1) - timedelta(days=90), date(2026, 11, 3))

print("\n== 7. Ledger rows by result ==")
ledger = Path(__file__).with_name("VERIFICATION_LEDGER.md").read_text(encoding="utf-8")
counts: dict[str, int] = {}
rows = 0
for line in ledger.splitlines():
    if not re.match(r"^\| \d+ \|", line):
        continue
    rows += 1
    last = line.rstrip().rstrip("|").split("|")[-1].strip().lower()
    if last.startswith("official-page defect"):
        key = "official-page defect"
    elif last.startswith("correction"):
        key = "correction"
    elif last.startswith("holds, wording"):
        key = "holds, wording"
    elif last.startswith("holds"):
        key = "holds"
    else:
        key = "other"
    counts[key] = counts.get(key, 0) + 1
print(f"      quoted rows: {rows}")
for key in sorted(counts):
    print(f"      {key}: {counts[key]}")
sources = len(re.findall(r"^### S\d+", ledger, flags=re.M))
print(f"      source sections: {sources}")
check("no ledger row has an unrecognised result", counts.get("other", 0), 0)

print()
if FAILS:
    print(f"FAILED: {len(FAILS)} check(s)")
    sys.exit(1)
print("ALL CHECKS PASSED")
