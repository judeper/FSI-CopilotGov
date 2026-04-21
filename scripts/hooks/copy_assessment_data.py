"""MkDocs hook — copy assessment data assets into the built site.

Runs during ``mkdocs build`` / ``mkdocs serve``. Copies:

* ``assessment/manifest/controls.json`` →
  ``site/assessment/data/controls.json``
* ``assessment/data/solutions-lock.json`` (when present, Phase C) →
  ``site/assessment/data/solutions-lock.json``

This is the v1.4 plumbing that lets the SPA fetch the manifest at
runtime as a static asset (``/assessment/data/controls.json``), keeping
the engine, the validator, and the SPA bound to a single source of
truth.

Wire-up in ``mkdocs.yml``::

    hooks:
      - scripts/hooks/copy_assessment_data.py
"""
from __future__ import annotations

import logging
import shutil
from pathlib import Path

log = logging.getLogger("mkdocs.copy_assessment_data")

REPO_ROOT = Path(__file__).resolve().parents[2]

# (source path, dest path under site/, required?)
SOURCES = (
    (REPO_ROOT / "assessment" / "manifest" / "controls.json",
     "assessment/data/controls.json", True),
    (REPO_ROOT / "assessment" / "data" / "solutions-lock.json",
     "assessment/data/solutions-lock.json", False),
)

# Directory trees to mirror into the built site. Each entry is
# (source dir, dest dir under site/, glob, required?).
# Phase G (Excel templates) publishes downloadable assets here so
# links in docs/getting-started/checklist.md and homework pages
# resolve at the published URLs.
SOURCE_DIRS = (
    (REPO_ROOT / "assessment" / "templates",
     "assessment/templates", "*.xlsx", False),
)


def on_post_build(config, **_kwargs):
    """Copy assessment data assets into the built site."""
    site_dir = Path(config["site_dir"])
    copied = 0
    for src, rel, required in SOURCES:
        if not src.exists():
            level = log.warning if required else log.info
            level("copy_assessment_data: %s missing: %s",
                  "REQUIRED source" if required else "optional source", src)
            continue
        dest = site_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
        copied += 1
    for src_dir, rel, pattern, required in SOURCE_DIRS:
        if not src_dir.exists():
            level = log.warning if required else log.info
            level("copy_assessment_data: %s dir missing: %s",
                  "REQUIRED" if required else "optional", src_dir)
            continue
        dest_dir = site_dir / rel
        dest_dir.mkdir(parents=True, exist_ok=True)
        for src_file in src_dir.glob(pattern):
            if not src_file.is_file():
                continue
            shutil.copyfile(src_file, dest_dir / src_file.name)
            copied += 1
    log.info("copy_assessment_data: copied %d asset(s)", copied)
