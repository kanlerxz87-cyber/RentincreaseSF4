"""Structural, privacy, source-integrity and internal-link validation.

Run: python3 scripts/validate_site.py
Writes data/validation_report.json. Exits nonzero on any error.
This is not legal verification and does not confirm owner property records.
"""

import collections
import hashlib
import json
import re
import sys
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

import site_data as D

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PAGES = ROOT / "pages"

OFFICIAL_DOMAINS = {
    "sf.gov", "media.api.sf.gov", "sfplanninggis.org", "default.sfplanning.org",
    "commissions.sfplanning.org", "leginfo.legislature.ca.gov", "calcivilrights.ca.gov",
    "courts.ca.gov", "hud.gov", "huduser.gov", "ecfr.gov", "govinfo.gov", "sec.gov",
    "api.github.com", "docs.github.com", "github.com", "sfrb.org", "sftreasurer.org", "codelibrary.amlegal.com",
}
VALID_ROW_STATUSES = {"rule checked", "project checked", "owner supplied", "analysis", "needs review", "source listed"}
MARKET_SOURCE_IDS = {"S43", "S44", "S45", "S46", "S47", "S50", "S51", "S52"}

report = {"date": D.DATE, "status": "running", "checks": [], "errors": []}


def check(name, ok, detail=""):
    entry = {"name": name, "ok": bool(ok), "detail": detail}
    report["checks"].append(entry)
    if not ok:
        report["errors"].append(f"{name}: {detail}")
    print(("PASS " if ok else "FAIL ") + name + ((" - " + detail) if detail else ""))


def official_domain(url):
    host = urlparse(url).netloc.lower()
    return any(host == d or host.endswith("." + d) for d in OFFICIAL_DOMAINS)


def json_load(path):
    return json.loads(path.read_text(encoding="utf-8"))


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("href", "src") and value:
                self.links.append(value)


def main():
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "validation_report.json").write_text(json.dumps({"status": "running"}, indent=2) + "\n", encoding="utf-8")

    pages = json_load(DATA / "pages.json")
    sources_list = json_load(DATA / "sources.json")
    flags = json_load(DATA / "flags.json")
    summary_meta = json_load(DATA / "summary.json")
    flag_ids = {f["id"] for f in flags}
    source_map = {s["id"]: s for s in sources_list}
    distinct_urls = {s["url"] for s in sources_list}

    check("canonical source map matches site data", len(source_map) == len(D.SOURCES), f"{len(D.SOURCES)} source entries")
    check("distinct source URL count is dynamic and excludes aliases", len(distinct_urls) == D.SOURCE_COUNT == summary_meta["distinct_source_urls"], f"{D.SOURCE_COUNT} distinct URLs")
    check("flags count matches canonical registry", len(flags) == len(D.FLAGS) == summary_meta["flags"], f"{len(flags)} flagged items")
    check("source URLs use official or official-publisher domains", all(official_domain(s["url"]) for s in sources_list))
    check("every source has id, title, agency, category, statement, url and check date",
          all(all(k in s for k in ("id", "title", "agency", "category", "statement", "url", "checked")) for s in sources_list))

    row_count = 0
    needs_review_count = 0
    owner_rows = []
    row_errors = []
    all_rows = []
    for slug, page in pages.items():
        for sec in page.get("sections", []):
            for r in sec["rows"]:
                all_rows.append((slug, r))
                row_count += 1
                rid = r.get("id", "?")
                status = r.get("status")
                if status not in VALID_ROW_STATUSES:
                    row_errors.append(f"{rid} has invalid status {status}")
                if status == "owner supplied":
                    owner_rows.append(rid)
                    if not r.get("source_ids"):
                        row_errors.append(f"{rid} owner-supplied row has no governing-rule links")
                    if "not government-verified" not in r.get("source_note", "") and "Owner intake" not in r.get("source_note", ""):
                        row_errors.append(f"{rid} owner-supplied row lacks intake disclaimer")
                    if not r.get("value"):
                        row_errors.append(f"{rid} owner-supplied row has no value")
                elif not r.get("source_ids"):
                    row_errors.append(f"{rid} has no source_ids")
                for sid in r.get("source_ids", []):
                    if sid not in source_map:
                        row_errors.append(f"{rid} references unknown source {sid}")
                    elif not official_domain(source_map[sid]["url"]):
                        row_errors.append(f"{rid} references nonofficial URL for {sid}")
                if status == "needs review":
                    needs_review_count += 1
                    if r.get("value", "") != "":
                        row_errors.append(f"{rid} needs review but value is not blank")
                    if not r.get("flag_id"):
                        row_errors.append(f"{rid} needs review but has no flag_id")
                    elif r["flag_id"] not in flag_ids:
                        row_errors.append(f"{rid} flag_id {r['flag_id']} not published")
                if r.get("flag_id") and r["flag_id"] not in flag_ids:
                    row_errors.append(f"{rid} flag_id {r['flag_id']} not published")
                if slug == "requirements" and set(r.get("source_ids", [])) & MARKET_SOURCE_IDS:
                    row_errors.append(f"{rid} requirements row cites unrelated market source")

    dupes = [i for i, n in collections.Counter(r["id"] for _, r in all_rows).items() if n > 1]
    check("row IDs are unique across generated pages", not dupes, ", ".join(dupes[:5]))
    check("owner-supplied case rows are labelled and linked to governing rules", len(owner_rows) >= 10, f"{len(owner_rows)} owner-supplied rows")
    check("every table row has valid status and official source links", not row_errors, f"{row_count} rows checked; " + "; ".join(row_errors[:5]))
    check("unverified rows are blank and flagged", needs_review_count > 0, f"{needs_review_count} needs-review rows")

    flag_errors = []
    for f in flags:
        if f.get("status") != "needs review":
            flag_errors.append(f"{f['id']} status is not needs review")
        if not f.get("source_ids"):
            flag_errors.append(f"{f['id']} has no source_ids")
        for sid in f["source_ids"]:
            if sid not in source_map:
                flag_errors.append(f"{f['id']} references unknown source {sid}")
            elif not official_domain(source_map[sid]["url"]):
                flag_errors.append(f"{f['id']} references nonofficial URL {sid}")
    check("every flag is published with official source links", not flag_errors, "; ".join(flag_errors[:5]))

    flagged_html = (PAGES / "flagged.html").read_text(encoding="utf-8")
    sources_html = (PAGES / "sources.html").read_text(encoding="utf-8")
    check("Flagged for Review page contains all flag IDs", all(f["id"] in flagged_html for f in flags))
    check("Flagged for Review page is clearly labeled nonblocking", "Flagged for Review" in flagged_html and "<strong>not</strong> block" in flagged_html)
    sources_html_unescaped = unescape(sources_html)
    check("Sources page contains all source IDs and URLs", all(s["id"] in sources_html_unescaped and s["url"] in sources_html_unescaped for s in sources_list))
    check("Sources page states distinct URL count", f"{D.SOURCE_COUNT} distinct" in sources_html)

    for slug in pages:
        check(f"data/{slug}.json exists", (DATA / f"{slug}.json").exists())
        check(f"pages/{slug}.html exists", (PAGES / f"{slug}.html").exists())
    for slug, _title in D.NAV:
        check(f"navigation target pages/{slug}.html exists", (PAGES / f"{slug}.html").exists())

    required_files = [
        ROOT / "index.html", ROOT / ".nojekyll", ROOT / "assets" / "site.css", ROOT / "assets" / "site.js",
        ROOT / "README.md", ROOT / "EXECUTIVE_SUMMARY.md", ROOT / "FLAGGED_FOR_REVIEW.md",
        ROOT / "SOURCES.md", ROOT / "VERIFICATION.md", ROOT / "REPO_REVIEW.md", ROOT / "COORDINATION.md",
        ROOT / "research" / "privacy" / "HISTORY_EXPOSURE.md",
    ]
    check("site build and disclosure files exist", all(p.exists() for p in required_files))

    index_html = (ROOT / "index.html").read_text(encoding="utf-8")
    check("fee page is generated and linked", (PAGES / "fee.html").exists() and "pages/fee.html" in index_html)
    check("index explains badges and leads with direct answer", "How to read this dashboard" in index_html and "Direct answer" in index_html)
    check("index links to Flagged for Review", "pages/flagged.html" in index_html and "Flagged for Review" in index_html)
    check("index links to Executive Summary", "pages/summary.html" in index_html and "Executive Summary" in index_html or "Executive summary" in index_html)
    summary_html = (PAGES / "summary.html").read_text(encoding="utf-8")
    check("executive summary forefront covers individual-owner license", "FOREFRONT" in summary_html and "individual" in summary_html.lower() and "Rent Increase License" in summary_html)

    public_md = sorted(ROOT.glob("*.md")) + sorted((ROOT / "research").rglob("*.md"))
    public_json = sorted(DATA.glob("*.json"))
    public_html = [ROOT / "index.html"] + sorted(PAGES.glob("*.html"))
    public_assets = [ROOT / "assets" / "site.css", ROOT / "assets" / "site.js"]
    public_research = sorted((ROOT / "research").rglob("*.json")) + sorted((ROOT / "research").rglob("*.py")) + sorted((ROOT / "research").rglob("*.mjs")) + sorted((ROOT / "research").rglob("*.log")) + sorted((ROOT / "research").rglob("*.patch"))
    public_files = [p for p in public_md + public_json + public_html + public_assets + public_research if p.exists()]

    # Optional internal-only regression baseline. Low-entropy fingerprints are not
    # published; if absent in CI, placeholder/pattern checks still run.
    baseline_path = ROOT / "internal" / "privacy_fingerprints.json"
    private_fingerprints = []
    if baseline_path.exists():
        private_fingerprints = json_load(baseline_path).get("sha256_normalized_initials", [])
    check("privacy regression baseline is internal-only", "internal/" in (ROOT / ".gitignore").read_text(encoding="utf-8"),
          "internal baseline optional and gitignored; public placeholder/pattern scans run in every checkout")
    privacy_hits = []
    for p in public_files:
        text = p.read_text(encoding="utf-8")
        candidates = re.findall(r"(?<![A-Za-z])[A-Z]\s+[A-Z](?![A-Za-z])|(?<![A-Za-z])[A-Z]{2}(?![A-Za-z])", text)
        for candidate in candidates:
            normalized = " ".join(candidate.split())
            if private_fingerprints and hashlib.sha256(normalized.encode()).hexdigest() in private_fingerprints:
                privacy_hits.append(str(p.relative_to(ROOT)))
    check("no raw tenant identifiers in public files", not privacy_hits, "; ".join(privacy_hits[:5]))
    fingerprint_hits = [str(p.relative_to(ROOT)) for p in public_files + sorted((ROOT / "scripts").glob("*.py"))
                        if re.search(r"\b[0-9a-f]{64}\b", p.read_text(encoding="utf-8"))]
    check("no low-entropy privacy fingerprints in public files or scripts", not fingerprint_hits, "; ".join(fingerprint_hits[:5]))

    address_patterns = [
        r"\b\d{3,5}\s+\d{1,2}(?:st|nd|rd|th)\s+(?:Ave|Avenue|Street|St)\b",
        r"\b\d{3,5}\s+[A-Za-z]+\s+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd)\b",
    ]
    address_hits = []
    for p in public_files:
        text = p.read_text(encoding="utf-8")
        for pat in address_patterns:
            if re.search(pat, text, re.IGNORECASE):
                address_hits.append(str(p.relative_to(ROOT)))
                break
    check("no exact street address published", not address_hits, "; ".join(address_hits[:5]))

    case_text = (DATA / "case.json").read_text(encoding="utf-8")
    expected_case = ["February 1, 2025", "$3,995", "April 1, 2026", "June 1, 2019", "$3,150"] + [f"Tenant {c}" for c in "ABCDEF"]
    check("dates, amounts and placeholder IDs preserved", all(s in case_text for s in expected_case))
    initial_hits = [str(x.relative_to(ROOT)) for x in (DATA / "case.json", PAGES / "case.html")
                    if re.search(r"\b[A-Z]{1,2}\s[A-Z]{1,2}\b", x.read_text(encoding="utf-8"))]
    check("no raw initials in anonymized case files", not initial_hits, "; ".join(initial_hits[:3]))

    content_files = [p for p in public_files if p.suffix not in {".py", ".mjs", ".patch", ".log"}]
    all_text = "\n".join(p.read_text(encoding="utf-8") for p in content_files)
    check("conservative compliance checklist wording present", "conservative compliance checklist capable of tenant-lawyer review" in all_text.lower())
    check("no attorney approval or guarantee claimed", "No attorney approval or guarantee" in all_text or "No attorney has approved" in all_text)
    forbidden = ["approved by a tenant lawyer", "this increase is certified lawful", "guaranteed no lawsuit", "attorney approved this increase", "we certify this increase is lawful"]
    check("no forbidden certification language", not any(s in all_text.lower() for s in forbidden))
    unsupported_rankings = ["most likely cause", "second-most-common", "second most common"]
    check("no unsupported defect-frequency rankings", not any(s in all_text.lower() for s in unsupported_rankings))

    process_html = (PAGES / "process.html").read_text(encoding="utf-8")
    process_plain = unescape(process_html)
    check("step-by-step license page exists in navigation", "pages/process.html" in index_html)
    check("step-by-step license page has all 12 numbered steps", all(f"Step {n}" in process_plain for n in range(1, 13)))
    check("step-by-step page links Sec. 37.15, Sec. 37.3 and Housing Inventory", "sec-3715" in process_plain and "sec-373" in process_plain and "rent-board-housing-inventory" in process_plain)
    check("step-by-step page answers individual-owner question", "individual property owner" in process_plain.lower() and "yes." in process_plain.lower())

    exec_md = (ROOT / "EXECUTIVE_SUMMARY.md").read_text(encoding="utf-8")
    check("executive summary puts license answer first", exec_md.index("Rent Increase License") < exec_md.index("## Bottom line"))
    check("executive summary cites ordinance license condition", "37.3(a)(1)" in exec_md and "37.15" in exec_md)
    check("executive summary links official license pages",
          "https://www.sf.gov/learn-about-rent-increases-san-francisco" in exec_md
          and "https://www.sf.gov/rent-board-housing-inventory" in exec_md
          and "https://www.sf.gov/information--sec-3715-reporting-obligations-licensing" in exec_md)
    check("executive summary states no individual-owner exemption", "no individual-owner" in exec_md.lower() and "exemption" in exec_md.lower())
    check("executive summary publishes dynamic flag count", f"All {D.FLAG_COUNT} flags" in exec_md)

    calc_rows = {r["id"]: r for sec in pages["calculations"]["sections"] for r in sec["rows"]}
    check("withdrawn banked total and invented notice dates remain blank", all(calc_rows[rid]["value"] == "" and calc_rows[rid]["status"] == "needs review" for rid in ("CALC-08", "CALC-10", "CALC-11")))
    check("fixed-term lease gap is flagged and answered", "F45" in flag_ids and any(r["id"] == "Q-22" for _, r in all_rows) and any(r["id"] == "CHK-18" for _, r in all_rows))

    broken = []
    for html_file in [ROOT / "index.html"] + sorted(PAGES.glob("*.html")):
        parser = LinkParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        for link in parser.links:
            if link.startswith(("http://", "https://", "mailto:", "tel:")) or link.startswith("#"):
                continue
            path_part = link.split("#", 1)[0].split("?", 1)[0]
            if not path_part:
                continue
            target = (html_file.parent / path_part).resolve()
            if not target.exists():
                broken.append(f"{html_file.relative_to(ROOT)} -> {link}")
    check("no broken internal links", not broken, "; ".join(broken[:5]))

    marker_hits = []
    for p_ in sorted(ROOT.glob("*.md")) + sorted(PAGES.glob("*.html")) + sorted(DATA.glob("*.json")) + sorted((ROOT / "scripts").glob("*.py")):
        text = p_.read_text(encoding="utf-8")
        if re.search(r"^(<<<<<<<|=======|>>>>>>>)", text, re.MULTILINE):
            marker_hits.append(str(p_.relative_to(ROOT)))
    check("no committed merge-conflict markers in public files or scripts", not marker_hits, "; ".join(marker_hits[:5]))

    numeric = [f["id"] for f in flags if re.fullmatch(r"F\d\d", f["id"])]
    expected_numeric = [f"F{i:02d}" for i in range(1, 50)]
    check("numeric flag IDs are unique and contiguous F01-F49", numeric == expected_numeric, f"{len(numeric)} numeric flags")

    stale_refs = []
    for p_ in [ROOT / "SOURCES.md", ROOT / "VERIFICATION.md", ROOT / "EXECUTIVE_SUMMARY.md", ROOT / "FLAGGED_FOR_REVIEW.md"]:
        text = p_.read_text(encoding="utf-8")
        for num in re.findall(r"flagged (F\d\d)", text):
            if num not in flag_ids:
                stale_refs.append(f"{p_.name} references unpublished {num}")
    check("no references to unpublished flag IDs", not stale_refs, "; ".join(stale_refs[:5]))

    all_site_text = "\n".join(p_.read_text(encoding="utf-8") for p_ in [ROOT / "index.html"] + sorted(PAGES.glob("*.html")))
    check("Rent Board Fee is distinguished from license", "$59.00" in all_site_text and "separate" in all_site_text.lower())
    check("retaliation 180-day rule is published", ("180 days" in all_site_text or "180-day" in all_site_text) and "1942.5" in all_site_text)
    check("AB 1482 two-unit owner-occupied exemption is published", "ADU" in all_site_text and "principal residence" in all_site_text)
    check("in-law-unit coverage rule is published", "in-law unit" in all_site_text.lower() and "legal in-law" in all_site_text.lower() and "illegal in-law" in all_site_text.lower())
    check("historical privacy exposure is disclosed, not claimed remediated", ("not remediated" in all_site_text.lower() or "do not erase earlier public" in all_site_text.lower()) and "F44" in all_site_text)
    check("summary page renders narrative, not just tables", summary_html.count("<h2>") >= 8 and "<ol>" in summary_html and "<h2>FOREFRONT" in summary_html, f"{summary_html.count('<h2>')} headings")
    check("summary page has no unrendered markdown", not re.search(r"<p>\s*#|\*\*|\]\(", summary_html))
    check("summary states fee/license distinction, retaliation and in-law coverage", "$59.00" in summary_html and "1942.5" in summary_html and "legal in-law" in summary_html.lower())
    check("responsive tables and search enhancement exist", "@media" in (ROOT / "assets" / "site.css").read_text(encoding="utf-8") and "data-table-search" in (ROOT / "assets" / "site.js").read_text(encoding="utf-8"))

    report["status"] = "passed" if not report["errors"] else "failed"
    report["summary"] = {
        "source_entries": len(source_map),
        "distinct_source_urls": len(distinct_urls),
        "pages": len(list(PAGES.glob("*.html"))),
        "data_files": len(list(DATA.glob("*.json"))),
        "rows_checked": row_count,
        "needs_review_rows": needs_review_count,
        "flags": len(flags),
        "checks": len(report["checks"]),
        "errors": len(report["errors"]),
        "legal_verification": False,
    }
    (DATA / "validation_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nValidation {report['status'].upper()} ({len(report['checks'])} checks, {len(report['errors'])} errors). Report: data/validation_report.json")
    if report["errors"]:
        for err in report["errors"]:
            print("ERROR: " + err)
        sys.exit(1)


if __name__ == "__main__":
    main()
