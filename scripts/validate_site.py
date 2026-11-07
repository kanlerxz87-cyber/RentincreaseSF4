"""Re-verify combined data line by line, validate source links, privacy and internal links.

Run: python3 scripts/validate_site.py
Writes data/validation_report.json. Exits nonzero on any error.
"""

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
    "hud.gov", "huduser.gov", "ecfr.gov", "govinfo.gov", "sec.gov", "api.github.com",
}

report = {"date": D.DATE, "status": "running", "checks": [], "errors": [], "warnings": []}

def check(name, ok, detail=""):
    entry = {"name": name, "ok": bool(ok), "detail": detail}
    report["checks"].append(entry)
    if not ok:
        report["errors"].append("{}: {}".format(name, detail))
    print(("PASS " if ok else "FAIL ") + name + ((" - " + detail) if detail else ""))

def warn(name, detail=""):
    message = name + ((": " + detail) if detail else "")
    report["warnings"].append(message)
    print("WARN " + message)

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
    # Placeholder so the footer's validation-report link resolves during the link check.
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "validation_report.json").write_text(json.dumps({"status": "running"}, indent=2) + "\n", encoding="utf-8")

    pages = json_load(DATA / "pages.json")
    sources_list = json_load(DATA / "sources.json")
    flags = json_load(DATA / "flags.json")
    flag_ids = {f["id"] for f in flags}
    source_map = {s["id"]: s for s in sources_list}

    check("canonical source map matches site data", len(source_map) == len(D.SOURCES) == 52, "52 official sources")
    check("flags count matches dashboard", len(flags) == 34, "34 flagged items")
    check("source URLs use official domains", all(official_domain(s["url"]) for s in sources_list), "all source URLs checked")
    check("every source has id, title, agency, category and statement",
          all(all(k in s for k in ("id", "title", "agency", "category", "statement", "url")) for s in sources_list))

    row_count = 0
    needs_review_count = 0
    row_errors = []
    for slug, page in pages.items():
        for sec in page["sections"]:
            for r in sec["rows"]:
                row_count += 1
                rid = r.get("id", "?")
                if not r.get("source_ids"):
                    row_errors.append("{} has no source_ids".format(rid))
                for sid in r["source_ids"]:
                    if sid not in source_map:
                        row_errors.append("{} references unknown source {}".format(rid, sid))
                    elif not official_domain(source_map[sid]["url"]):
                        row_errors.append("{} references nonofficial URL for {}".format(rid, sid))
                if r.get("status") not in ("verified", "needs review", "analysis"):
                    row_errors.append("{} has invalid status".format(rid))
                if r.get("status") == "needs review":
                    needs_review_count += 1
                    if r.get("value", "") != "":
                        row_errors.append("{} needs review but value is not blank".format(rid))
                    if not r.get("flag_id"):
                        row_errors.append("{} needs review but has no flag_id".format(rid))
                    elif r["flag_id"] not in flag_ids:
                        row_errors.append("{} flag_id {} not published".format(rid, r["flag_id"]))
                if r.get("flag_id") and r["flag_id"] not in flag_ids:
                    row_errors.append("{} flag_id {} not published".format(rid, r["flag_id"]))
    check("every table row has valid official source links", not row_errors, "{} rows checked; {}".format(row_count, "; ".join(row_errors[:5])))
    check("unverified rows are blank and flagged", needs_review_count > 0, "{} needs-review rows".format(needs_review_count))

    flag_errors = []
    for f in flags:
        if f.get("status") != "needs review":
            flag_errors.append("{} status is not needs review".format(f["id"]))
        if not f.get("source_ids"):
            flag_errors.append("{} has no source_ids".format(f["id"]))
        for sid in f["source_ids"]:
            if sid not in source_map:
                flag_errors.append("{} references unknown source {}".format(f["id"], sid))
            elif not official_domain(source_map[sid]["url"]):
                flag_errors.append("{} references nonofficial URL {}".format(f["id"], sid))
    check("every flag is published with official source links", not flag_errors, "; ".join(flag_errors[:5]))

    flagged_html = (PAGES / "flagged.html").read_text(encoding="utf-8")
    sources_html = (PAGES / "sources.html").read_text(encoding="utf-8")
    check("Flagged for Review page contains all flag IDs", all(f["id"] in flagged_html for f in flags))
    check("Flagged for Review page is clearly labeled", "Flagged for Review" in flagged_html and "does <strong>not</strong> block" in flagged_html)
    sources_html_unescaped = unescape(sources_html)
    check("Sources page contains all source IDs and URLs",
          all(s["id"] in sources_html_unescaped and s["url"] in sources_html_unescaped for s in sources_list))

    for slug in D.PAGES:
        check("data/{}.json exists".format(slug), (DATA / "{}.json".format(slug)).exists())
        check("pages/{}.html exists".format(slug), (PAGES / "{}.html".format(slug)).exists())
    for slug, _title in D.NAV:
        check("pages/{}.html in navigation exists".format(slug), (PAGES / "{}.html".format(slug)).exists())

    required_files = [
        ROOT / "index.html", ROOT / ".nojekyll", ROOT / "assets" / "site.css",
        ROOT / "README.md", ROOT / "EXECUTIVE_SUMMARY.md", ROOT / "FLAGGED_FOR_REVIEW.md",
        ROOT / "SOURCES.md", ROOT / "VERIFICATION.md", ROOT / "REPO_REVIEW.md", ROOT / "COORDINATION.md",
    ]
    check("site build files exist", all(p.exists() for p in required_files))

    index_html = (ROOT / "index.html").read_text(encoding="utf-8")
    check("index has clean landing / dashboard", "dashboard" in index_html.lower() and "Clean landing page / dashboard" in index_html)
    check("index links to Flagged for Review", 'pages/flagged.html' in index_html and "Flagged for Review" in index_html)
    check("index links to Executive Summary", 'pages/summary.html' in index_html and "Executive Summary" in index_html)

    public_md = sorted(ROOT.glob("*.md")) + sorted((ROOT / "research").rglob("*.md"))
    public_json = sorted(DATA.glob("*.json"))
    public_html = [ROOT / "index.html"] + sorted(PAGES.glob("*.html"))
    public_css = [ROOT / "assets" / "site.css"]
    public_files = [p for p in public_md + public_json + public_html + public_css if p.exists()]

    internal = ROOT / "internal" / "tenant-identifiers.local.md"
    raw_identifiers = []
    if internal.exists():
        for line in internal.read_text(encoding="utf-8").splitlines():
            if "raw identifiers, internal only" in line.lower():
                tail = line.split(":", 1)[-1]
                for token in re.findall(r"\b[A-Z](?:\s+[A-Z])*\b|\bJP\b", tail):
                    token = token.strip()
                    if len(token) >= 2 and token not in raw_identifiers:
                        raw_identifiers.append(token)
    check("private intake file is excluded from git", "internal/" in (ROOT / ".gitignore").read_text(encoding="utf-8"))
    if internal.exists() and raw_identifiers:
        check("raw identifiers parsed from private intake", len(raw_identifiers) >= 6, "{} identifiers loaded from gitignored local intake".format(len(raw_identifiers)))
        privacy_hits = []
        for p in public_files:
            text = p.read_text(encoding="utf-8")
            for token in raw_identifiers:
                if token in text:
                    privacy_hits.append("{} contains a private identifier".format(p.relative_to(ROOT)))
        check("no raw tenant identifiers in public files", not privacy_hits, "; ".join(privacy_hits[:5]))
    else:
        warn("identifier-specific privacy scan unavailable", "gitignored private intake is absent; it was not recreated or committed")

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
    expected_case = ["February 1, 2025", "$3,995", "April 1, 2026", "June 1, 2019", "$3,150"] + ["Tenant {}".format(c) for c in "ABCDEF"]
    check("dates, amounts and placeholder IDs preserved", all(s in case_text for s in expected_case))

    all_text = "\n".join(p.read_text(encoding="utf-8") for p in public_files if p.suffix in (".html", ".md", ".json", ".css"))
    check("conservative compliance checklist wording present",
          "conservative compliance checklist capable of tenant-lawyer review" in all_text.lower())
    check("no attorney approval or guarantee claimed",
          "No attorney approval or guarantee" in all_text or "No attorney has approved" in all_text)
    forbidden = ["approved by a tenant lawyer", "this increase is certified lawful", "guaranteed no lawsuit", "attorney approved this increase", "we certify this increase is lawful"]
    check("no forbidden certification language", not any(s in all_text.lower() for s in forbidden))

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
                broken.append("{} -> {}".format(html_file.relative_to(ROOT), link))
    check("no broken internal links", not broken, "; ".join(broken[:5]))

    report["status"] = "failed" if report["errors"] else ("passed_with_warnings" if report["warnings"] else "passed")
    report["summary"] = {
        "sources": len(source_map),
        "pages": len(list(PAGES.glob("*.html"))),
        "data_files": len(list(DATA.glob("*.json"))),
        "rows_verified": row_count,
        "needs_review_rows": needs_review_count,
        "flags": len(flags),
        "checks": len(report["checks"]),
        "errors": len(report["errors"]),
    }
    (DATA / "validation_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("\nValidation {} ({} checks, {} errors, {} warnings). Report: data/validation_report.json".format(
        report["status"].upper(), len(report["checks"]), len(report["errors"]), len(report["warnings"])
    ))
    if report["errors"]:
        for err in report["errors"]:
            print("ERROR: " + err)
        sys.exit(1)

if __name__ == "__main__":
    main()
