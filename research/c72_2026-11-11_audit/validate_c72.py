#!/usr/bin/env python3
"""Standalone validator for C72 (research/c72_2026-11-11_audit/).

Enforces:
1. Official government / SEC URLs on all JSON sources and every README table row.
2. Exact Decimal arithmetic on Unit 1, Unit 2, Rent Board Fee, and 94122 SAFMRs.
3. Unverified case values remain null/blank (never inferred).
4. Zero raw personal identifiers AND zero stored hashes/digests of identifiers,
   using an explicit allowlist of known legal/technical 2-letter uppercase tokens.
"""

from __future__ import annotations

import json
import re
import sys
from decimal import Decimal
from pathlib import Path
from urllib.parse import urlparse

KIT_DIR = Path(__file__).resolve().parent
JSON_PATH = KIT_DIR / "c72_verified_addendum.json"
README_PATH = KIT_DIR / "README.md"

OFFICIAL_GOVERNMENT_HOSTS = {
    "www.sf.gov",
    "sf.gov",
    "media.api.sf.gov",
    "sfgov.legistar.com",
    "sfplanninggis.org",
    "sftreasurer.org",
    "leginfo.legislature.ca.gov",
    "calcivilrights.ca.gov",
    "www.hud.gov",
    "www.huduser.gov",
    "huduser.gov",
    "www.ecfr.gov",
    "www.govinfo.gov",
    "www.sec.gov",
}

ALLOWED_DEFECT_HOSTS = OFFICIAL_GOVERNMENT_HOSTS | {"github.com"}

# Explicit allowlist of standard legal/agency/geography/technical 2-letter acronyms.
# Stores ZERO tokens or digests derived from any private person's name or initials.
ALLOWED_TWO_UPPER_TOKENS = {
    "AB",  # Assembly Bill (AB 1482, AB 12, AB 832, AB 1620)
    "AK",  # Alaska (HUD chunk reference)
    "AL",  # Alabama (HUD chunk reference)
    "AN",  # Analysis row prefix (AN-29)
    "AZ",  # Arizona (HUD chunk reference)
    "BR",  # Bedroom (0-BR, 2BR)
    "CA",  # California
    "CH",  # Chapter
    "CI",  # Capital Improvement
    "EX",  # SEC Exhibit
    "FY",  # Fiscal Year
    "ID",  # Identifier / Legistar ID
    "LP",  # Limited Partnership (ERP Operating LP)
    "NO",  # Number / Notice emphasis
    "OR",  # Logical OR / Oregon
    "PR",  # Pull Request
    "QA",  # Quality Assurance
    "SF",  # San Francisco
    "ST",  # State row prefix
    "US",  # United States
}

FORBIDDEN_CLAIM_PHRASES = (
    "approved by a tenant lawyer",
    "certified lawful",
    "guaranteed no lawsuit",
)

STREET_ADDRESS_RE = re.compile(
    r"\b\d{2,5}\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?\s+"
    r"(?:Ave|Avenue|St|Street|Blvd|Boulevard|Way|Dr|Drive)\b"
)
URL_RE = re.compile(r"https://[^\s)>\]]+")
HEX64_RE = re.compile(r"\b[0-9a-f]{64}\b", re.IGNORECASE)
STANDALONE_TWO_UPPER_RE = re.compile(r"(?<![A-Za-z0-9_-])[A-Z]{2}(?![A-Za-z0-9_-])")


def main() -> int:
    checks = 0
    errors: list[str] = []

    def check(ok: bool, label: str, detail: str = "") -> None:
        nonlocal checks
        checks += 1
        if ok:
            suffix = f" - {detail}" if detail else ""
            print(f"PASS {label}{suffix}")
        else:
            msg = f"FAIL {label}" + (f" - {detail}" if detail else "")
            print(msg)
            errors.append(msg)

    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    readme = README_PATH.read_text(encoding="utf-8")

    sources = data.get("new_official_sources", [])
    defects = data.get("defect_ledger", [])
    check(
        len(sources) == 8 and len(defects) == 8,
        "JSON schema loaded",
        f"{len(sources)} new official sources, {len(defects)} audited defects",
    )

    src_ids = [s["id"] for s in sources]
    check(len(src_ids) == len(set(src_ids)), "source IDs unique")

    bad_src_urls = [
        s["url"]
        for s in sources
        if urlparse(s["url"]).hostname not in OFFICIAL_GOVERNMENT_HOSTS
    ]
    check(not bad_src_urls, "all new source URLs use official government/SEC hosts", str(bad_src_urls or "ok"))

    bad_defect_urls = [
        u
        for d in defects
        for u in d.get("official_proof_urls", [])
        if urlparse(u).hostname not in ALLOWED_DEFECT_HOSTS
    ]
    check(not bad_defect_urls, "all defect proof URLs use approved official/repo hosts")

    # Check every markdown table data row in README.md carries at least one official government/SEC link
    lines = readme.splitlines()
    table_data_rows = 0
    unlinked_rows: list[int] = []
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        # Skip header row if next line is separator
        if idx < len(lines):
            nxt = lines[idx].strip()
            if nxt.startswith("|") and all(
                re.fullmatch(r":?-{3,}:?", c.strip())
                for c in nxt.strip("|").split("|")
            ):
                continue
        table_data_rows += 1
        urls = URL_RE.findall(line)
        gov_urls = [u for u in urls if urlparse(u).hostname in OFFICIAL_GOVERNMENT_HOSTS]
        if not gov_urls:
            unlinked_rows.append(idx)

    check(
        table_data_rows >= 40 and not unlinked_rows,
        "every README markdown table row has at least one official government/SEC URL",
        f"{table_data_rows} rows checked" + (f"; missing at {unlinked_rows}" if unlinked_rows else ""),
    )

    # Decimal math verification
    calc = data["case_calculations"]
    rate = Decimal(calc["annual_rate_2026_2027_pct"]) / Decimal("100")
    u1_base = Decimal(calc["unit_1"]["current_base_rent"])
    u1_inc = (u1_base * rate).quantize(Decimal("0.01"))
    u1_new = u1_base + u1_inc
    check(
        u1_inc == Decimal("63.92")
        and u1_new == Decimal("4058.92")
        and Decimal(calc["unit_1"]["annual_increase_dollars"]) == u1_inc
        and Decimal(calc["unit_1"]["new_base_rent"]) == u1_new,
        "Unit 1 Decimal arithmetic exact",
        f"${u1_base} x 1.6% = ${u1_inc} -> ${u1_new}",
    )

    u2_base = Decimal(calc["unit_2"]["current_base_rent"])
    u2_inc = (u2_base * rate).quantize(Decimal("0.01"))
    u2_new = u2_base + u2_inc
    check(
        u2_inc == Decimal("50.40")
        and u2_new == Decimal("3200.40")
        and Decimal(calc["unit_2"]["annual_only_increase_dollars"]) == u2_inc
        and Decimal(calc["unit_2"]["annual_only_new_base_rent"]) == u2_new,
        "Unit 2 Decimal arithmetic exact",
        f"${u2_base} x 1.6% = ${u2_inc} -> ${u2_new}",
    )

    fee = calc["rent_board_fee_2026_2027"]
    check(
        Decimal(fee["per_dwelling_unit"]) * 2 == Decimal(fee["two_unit_total"])
        and Decimal(fee["per_dwelling_unit"]) / 2 == Decimal(fee["tenant_recoverable_50pct_per_unit"]),
        "Rent Board Fee arithmetic exact",
        "$59.00 x 2 = $118.00; 50% = $29.50",
    )

    # Unverified fields must remain null
    check(
        calc["unit_1"]["prior_increase_history"] is None
        and calc["unit_1"]["bedroom_count"] is None
        and calc["unit_2"]["prior_increase_history"] is None
        and calc["unit_2"]["verified_banked_amount"] is None
        and calc["unit_2"]["bedroom_count"] is None,
        "unverified case fields remain null/blank",
    )

    safmr = data["hud_94122_safmr_comparison"]
    check(
        safmr["fy2027"] == {"0br": 2370, "1br": 2770, "2br": 3410, "3br": 4460, "4br": 5020}
        and safmr["fy2026"] == {"0br": 2280, "1br": 2730, "2br": 3310, "3br": 4230, "4br": 4380},
        "HUD 94122 FY2027 and FY2026 SAFMR schedules verified",
    )

    # Privacy, digest-free, conflict-marker, and phrase checks across all files in KIT_DIR
    kit_files = sorted(p for p in KIT_DIR.iterdir() if p.is_file())
    unexpected_two_upper: list[tuple[str, str]] = []
    sha256_literals: list[str] = []
    conflict_hits: list[str] = []
    street_hits: list[str] = []
    forbidden_hits: list[str] = []

    for path in kit_files:
        text = path.read_text(encoding="utf-8")
        if re.search(r"^(?:<{7}|={7}|>{7})(?:\s|$)", text, flags=re.M):
            conflict_hits.append(path.name)
        if HEX64_RE.search(text):
            sha256_literals.append(path.name)
        if STREET_ADDRESS_RE.search(text):
            street_hits.append(path.name)
        if path.name != "validate_c72.py":
            low = text.lower()
            for phrase in FORBIDDEN_CLAIM_PHRASES:
                # Allow explicit disclaimer "not approved by a tenant lawyer"
                cleaned = low.replace("not approved by a tenant lawyer", "")
                if phrase in cleaned:
                    forbidden_hits.append(f"{path.name}:{phrase}")
            # Strip URLs before scanning standalone 2-letter uppercase tokens
            scrubbed = URL_RE.sub(" ", text)
            for tok in STANDALONE_TWO_UPPER_RE.findall(scrubbed):
                if tok not in ALLOWED_TWO_UPPER_TOKENS:
                    unexpected_two_upper.append((path.name, tok))

    check(not conflict_hits, "no merge-conflict markers")
    check(not sha256_literals, "zero embedded 64-hex SHA-256 digests stored in C72 kit")
    check(not street_hits, "no street address published")
    check(not forbidden_hits, "no forbidden attorney-approval or lawsuit-guarantee claims")
    check(
        not unexpected_two_upper,
        "allowlist-only 2-letter uppercase token privacy scan passed (zero personal initials)",
        str(unexpected_two_upper or "0 unallowlisted tokens"),
    )
    check(
        all(
            token in readme
            for token in (
                "February 1, 2025",
                "April 1, 2026",
                "June 1, 2019",
                "$3,995",
                "$3,150",
                "Tenant 1A",
                "Tenant 2A",
            )
        ),
        "exact anonymized dates, amounts, and placeholders preserved",
    )

    # Read-only crawl of published site HTML (index.html + pages/*.html) for broken links & anchors
    repo_root = KIT_DIR.parent.parent
    html_files = [repo_root / "index.html", *sorted((repo_root / "pages").glob("*.html"))]
    id_cache: dict[Path, set[str]] = {}
    for hf in html_files:
        if hf.exists():
            htxt = hf.read_text(encoding="utf-8")
            id_cache[hf.resolve()] = set(re.findall(r'\bid="([^"]+)"', htxt))

    broken_links: list[str] = []
    broken_anchors: list[str] = []
    malformed_external: list[str] = []
    total_hrefs = 0
    for hf in html_files:
        if not hf.exists():
            broken_links.append(str(hf.relative_to(repo_root)))
            continue
        htxt = hf.read_text(encoding="utf-8")
        for href in re.findall(r'\bhref="([^"]+)"', htxt):
            total_hrefs += 1
            if href.startswith(("mailto:", "tel:")):
                continue
            if href.startswith(("http://", "https://")):
                parsed = urlparse(href)
                if parsed.scheme != "https" or not parsed.hostname:
                    malformed_external.append(f"{hf.name}:{href}")
                continue
            path_part, _, frag = href.partition("#")
            target = (hf.parent / path_part).resolve() if path_part else hf.resolve()
            if not target.exists():
                broken_links.append(f"{hf.name}->{href}")
            elif frag and target in id_cache and frag not in id_cache[target]:
                broken_anchors.append(f"{hf.name}->{href}")

    # Page count grows as new category pages are added (T54/T55/T56 added two on
    # 2026-11-13), so assert a floor rather than a fixed count.
    check(
        len(html_files) >= 21 and not broken_links,
        "published site internal href targets resolve cleanly",
        f"{len(html_files)} HTML pages, {total_hrefs} hrefs scanned"
        + (f"; broken={broken_links}" if broken_links else ""),
    )
    check(not broken_anchors, "published site #fragment anchors resolve cleanly", str(broken_anchors or "0 broken anchors"))
    check(not malformed_external, "published site external https URLs well-formed", str(malformed_external or "ok"))

    if errors:
        print(f"\nC72 validation FAILED ({checks} checks, {len(errors)} errors).")
        return 1
    print(f"\nC72 validation PASSED ({checks} checks, 0 errors).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
