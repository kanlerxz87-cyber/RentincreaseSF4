"""Integration adapter for the independently verified B87 notice worksheet kit.

The kit lives in research/b87_notice_kit/worksheet.json. This module maps its
namespaced source IDs to the canonical official-source registry, publishes its
flags, and builds a categorized subpage. It does not infer case facts: blank
case-value cells stay blank and flagged, and every row keeps official links.
"""

import json
from pathlib import Path

from site_sources import SOURCES

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "research" / "b87_notice_kit" / "worksheet.json"

# Each B87 URL was opened by session arena-b87bd80b on 2026-11-08 and the seven
# newly added canonical sources were re-opened directly on 2026-11-10. The map
# deliberately uses only canonical source IDs that the site validator knows.
B87_SOURCE_MAP = {
    "B87-S01": "S01",
    "B87-S02": "S07",
    "B87-S03": "S72",
    "B87-S04": "S73",
    "B87-S07": "S74",
    "B87-S09": "S35",
    "B87-S10": "S75",
    "B87-S11": "S76",
    "B87-S12": "S77",
    "B87-S13": "S04",
    "B87-S14": "S02",
    "B87-S15": "S05",
    "B87-S16": "S54",
    "B87-S17": "S09",
    "B87-S22": "S16",
    "B87-S23": "S57",
    "B87-S24": "S78",
    "B87-S25": "S25",
    "B87-S27": "S26",
    "B87-S28": "S06",
}


def canonical_sources(ids):
    out = []
    for sid in ids:
        if sid not in B87_SOURCE_MAP:
            raise ValueError("Unmapped B87 source ID: " + sid)
        mapped = B87_SOURCE_MAP[sid]
        if mapped not in SOURCES:
            raise ValueError("Unknown canonical source ID: " + mapped)
        if mapped not in out:
            out.append(mapped)
    return out


def _load_kit():
    return json.loads(KIT.read_text(encoding="utf-8"))


def _flag_row(flag):
    return {
        "id": flag["id"],
        "title": flag["title"],
        "detail": flag["detail"],
        "source_ids": canonical_sources(flag["source_ids"]),
        "status": "needs review",
    }


KIT_DATA = _load_kit()
B87_FLAGS = [_flag_row(f) for f in KIT_DATA["flags"]]

WORKSHEET_COLUMNS = [
    "Item / gate",
    "Rule or owner input (source-linked)",
    "Case value",
    "Status",
    "Official source(s)",
    "Notes / flags",
]

SECTIONS = [
    ("IN", "Owner-supplied inputs (anonymized; not official findings)"),
    ("G", "Pre-service eligibility gates"),
    ("N", "Required notice contents"),
    ("C", "Conditional arithmetic - not a finding or recommendation"),
    ("SV", "Service, effective-date and tenant-challenge record"),
    ("LOG", "Placeholder service log - blank until actual service"),
]


def _row(raw):
    raw_status = raw["status"]
    value = raw.get("value", "")
    # The kit uses "verified rule" for source-linked rules whose case value is
    # blank. On this dashboard the status describes the case-value cell, so a
    # blank value is always published as needs review with a published flag.
    if raw_status in ("verified rule",) or (raw_status == "analysis" and value == ""):
        status = "needs review"
    elif raw_status in ("needs review", "analysis"):
        status = raw_status
    else:
        raise ValueError("Unhandled B87 row status: " + raw_status)
    flag_ids = list(raw.get("flag_ids", []))
    if status == "needs review" and not flag_ids:
        flag_ids = ["B87-F01"]
    notes = raw.get("notes", "")
    if raw_status == "verified rule":
        notes = (notes + " | The official rule is source-linked; the case value is blank and needs review.").strip(" |")
    return {
        "id": raw["id"],
        "label": raw["label"],
        "rule": ("Owner-supplied intake (anonymized; not an official finding): " + raw.get("rule", ""))
                if raw["id"].startswith("B87-IN-") else raw.get("rule", ""),
        "value": value,
        "status": status,
        "source_ids": canonical_sources(raw["source_ids"]),
        "notes": notes,
        "flag_id": flag_ids[0] if flag_ids else "",
        "flag_ids": flag_ids,
        "source_note": "",
    }


def build_worksheet_page():
    rows = [_row(r) for r in KIT_DATA["rows"]]
    sections = []
    for prefix, title in SECTIONS:
        group = [r for r in rows if r["id"].startswith("B87-" + prefix)]
        if group:
            sections.append({
                "title": title,
                "columns": WORKSHEET_COLUMNS,
                "kind": "worksheet",
                "rows": group,
            })
    used = {r["id"] for s in sections for r in s["rows"]}
    leftover = [r for r in rows if r["id"] not in used]
    if leftover:
        raise ValueError("Uncategorized B87 worksheet rows: " + ", ".join(r["id"] for r in leftover))
    return {
        "title": "Notice Worksheet",
        "description": (
            "Source-linked annual/banked rent-increase gates, required notice contents, "
            "service record and conditional arithmetic. The second column states either a "
            "source-linked rule or explicitly labeled owner-supplied intake; the Case value "
            "column is blank unless officially confirmed. Status refers to the case value. "
            "This is a worksheet, not a filed notice, an eligibility determination or "
            "attorney approval."
        ),
        "sections": sections,
    }


__all__ = ["B87_FLAGS", "B87_SOURCE_MAP", "WORKSHEET_COLUMNS", "build_worksheet_page"]
