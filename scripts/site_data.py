"""Aggregate canonical site data for build_site.py and validate_site.py."""

from site_sources import DATE, DISCLAIMER, SOURCES
from site_flags import NAV, CARDS, FLAGS
from site_pages import COLUMNS, PAGES
from site_text import EXECUTIVE_SUMMARY_TEXT, FLAGGED_TEXT, README_TEXT, CSS_TEXT
from site_suggestions import (
    DECISION_DEFAULT,
    INTERNAL_MARKER,
    REVIEW_COLUMNS,
    REVIEW_CHECKLIST_TEXT,
    REVIEW_TEXT,
    SUGGESTION_COLUMNS,
    SUGGESTION_SECTIONS,
    all_suggestions,
    review_checklist,
)

__all__ = [
    "DATE", "DISCLAIMER", "SOURCES", "NAV", "CARDS", "FLAGS",
    "COLUMNS", "PAGES", "EXECUTIVE_SUMMARY_TEXT", "FLAGGED_TEXT",
    "README_TEXT", "CSS_TEXT",
    "DECISION_DEFAULT", "INTERNAL_MARKER", "REVIEW_COLUMNS",
    "REVIEW_CHECKLIST_TEXT", "REVIEW_TEXT", "SUGGESTION_COLUMNS",
    "SUGGESTION_SECTIONS", "all_suggestions", "review_checklist",
]
