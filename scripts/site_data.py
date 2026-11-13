"""Aggregate canonical site data for build_site.py and validate_site.py."""

from site_sources import DATE, DISCLAIMER, SOURCES
from site_flags import NAV, CARDS, FLAGS
from site_pages import COLUMNS, PAGES
from site_text import EXECUTIVE_SUMMARY_TEXT, FLAGGED_TEXT, README_TEXT, CSS_TEXT
from site_suggestions import (
    INTERNAL_MARKER,
    REVIEW_STATUS_DEFAULT,
    REVIEW_STATUS_VALUES,
    T54_SECTIONS,
    all_t54_rows,
    checklist_rows,
)

__all__ = [
    "DATE", "DISCLAIMER", "SOURCES", "NAV", "CARDS", "FLAGS",
    "COLUMNS", "PAGES", "EXECUTIVE_SUMMARY_TEXT", "FLAGGED_TEXT",
    "README_TEXT", "CSS_TEXT",
    "INTERNAL_MARKER", "REVIEW_STATUS_DEFAULT", "REVIEW_STATUS_VALUES",
    "T54_SECTIONS", "all_t54_rows", "checklist_rows",
]
