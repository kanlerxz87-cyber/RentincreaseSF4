#!/usr/bin/env python3
"""Diagnostic HTTP sweep of the public source catalog (not a legal audit).

Run from a network with access to official sites, e.g. the manual GitHub Actions
workflow. 403/429, TLS failures and timeouts are inconclusive, not broken.
Do not silently equate HTTP 200 with factual support, current law or site safety.
"""
import argparse
import concurrent.futures
import datetime
import html
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADINGS = re.compile(r"<(?:title|h1)\b[^>]*>(.*?)</(?:title|h1)>", re.I | re.S)
NOT_FOUND = re.compile(r"\b(?:404|page not found|page cannot be found|invalid parameters)\b", re.I)


def classify(status, content_type="", prefix=b""):
    if status in (404, 410):
        return "broken"
    if status in (401, 403, 405, 429) or status >= 500:
        return "inconclusive"
    if not 200 <= status < 300:
        return "inconclusive"
    if "html" in content_type.lower():
        text = prefix.decode("utf-8", errors="replace")
        for match in HEADINGS.finditer(text):
            heading = html.unescape(re.sub(r"<[^>]+>", " ", match.group(1)))
            if NOT_FOUND.search(heading):
                return "broken"
        if re.search(r"\binvalid parameters\b", text[:4096], re.I):
            return "broken"
    return "reachable"


def check_url(url, timeout):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; SF-Rent-Research-LinkCheck/1.0)",
        "Accept": "text/html,application/pdf,*/*;q=0.8",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            status = response.status
            content_type = response.headers.get("Content-Type", "")
            prefix = response.read(65536) if "html" in content_type.lower() else b""
            return {"outcome": classify(status, content_type, prefix), "http_status": status}
    except urllib.error.HTTPError as exc:
        return {"outcome": classify(exc.code), "http_status": exc.code}
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
        # Record only exception type: URLs, response bodies and personal data are not logged.
        return {"outcome": "inconclusive", "http_status": None, "error_type": type(exc).__name__}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    sources = json.loads((ROOT / "data/sources.json").read_text(encoding="utf-8"))
    urls = sorted({s["url"] for s in sources})
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = dict(zip(urls, pool.map(lambda url: check_url(url, args.timeout), urls)))
    entries = [{"id": s["id"], **results[s["url"]]} for s in sources]
    counts = {k: sum(x["outcome"] == k for x in entries) for k in ("reachable", "broken", "inconclusive")}
    report = {
        "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_entries": len(entries),
        "unique_urls": len(urls),
        "counts": counts,
        "results": entries,
        "scope_limit": "HTTP/soft-404 diagnosis only. Reachable does not prove that a source supports a claim; inconclusive is not a broken link.",
    }
    for item in entries:
        print("{id}: {outcome} HTTP {http_status}".format(**item), flush=True)
    print("Summary:", json.dumps(counts), flush=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return 1 if counts["broken"] else 0


if __name__ == "__main__":
    sys.exit(main())
