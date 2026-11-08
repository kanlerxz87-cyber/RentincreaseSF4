"""Aggregate canonical site data for build_site.py and validate_site.py."""

from site_sources import DATE, DISCLAIMER, SOURCES
from site_flags import NAV, NAV_GROUPS, CARDS, FLAGS
from site_pages import COLUMNS, PAGES
from site_text import EXECUTIVE_SUMMARY_TEXT, FLAGGED_TEXT, README_TEXT, CSS_TEXT, JS_TEXT, SOURCE_COUNT, SOURCE_ENTRY_COUNT, FLAG_COUNT

__all__ = [
    "DATE", "DISCLAIMER", "SOURCES", "NAV", "NAV_GROUPS", "CARDS", "FLAGS",
    "COLUMNS", "PAGES", "EXECUTIVE_SUMMARY_TEXT", "FLAGGED_TEXT",
    "README_TEXT", "CSS_TEXT", "JS_TEXT", "SOURCE_COUNT", "SOURCE_ENTRY_COUNT", "FLAG_COUNT",
]
