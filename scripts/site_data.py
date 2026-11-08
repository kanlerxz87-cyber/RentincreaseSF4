"""Aggregate canonical site data for build_site.py and validate_site.py."""

from site_sources import DATE, DISCLAIMER, SOURCES

OFFICIAL_SOURCES = {k: v for k, v in SOURCES.items() if v.get("kind", "official") == "official"}
PROJECT_SOURCES = {k: v for k, v in SOURCES.items() if v.get("kind") == "project"}
from site_flags import NAV, CARDS, FLAGS
from site_pages import COLUMNS, PAGES
from site_text import EXECUTIVE_SUMMARY_TEXT, FLAGGED_TEXT, README_TEXT, CSS_TEXT

__all__ = [
    "DATE", "DISCLAIMER", "SOURCES", "OFFICIAL_SOURCES", "PROJECT_SOURCES", "NAV", "CARDS", "FLAGS",
    "COLUMNS", "PAGES", "EXECUTIVE_SUMMARY_TEXT", "FLAGGED_TEXT",
    "README_TEXT", "CSS_TEXT",
]
