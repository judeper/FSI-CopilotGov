#!/usr/bin/env python3
"""Verify Copilot Tuning (Control 1.16) claims stay source-grounded.

Two narrowly scoped guards run only over the Control 1.16 file set (the
Copilot Tuning governance control and its playbooks). They exist to prevent
two specific regressions that were corrected once and must not silently
return:

  1. Fabricated data-volume thresholds. Microsoft does not publish a fixed
     "N indexable documents/items" tuning corpus minimum; the documented
     scenario minimums are small, per-recipe example sets (for example,
     "at least 20 example files"). A large document/item/corpus count
     presented as a tuning minimum (e.g. "100K+ indexable documents") is
     unsupported and must not reappear. The tenant *license* threshold
     (5,000 Microsoft 365 Copilot licenses) is legitimate and is excluded.

  2. Terminology drift. Copilot Tuning ships as an **early access preview**
     delivered via the Microsoft Frontier program, not a generic "public
     preview". The phrase "public preview" is disallowed within the tuning
     file set (other controls may legitimately reference other features'
     public previews, so this guard is deliberately scoped to 1.16 only).

Exit codes:
  0 — no violations found
  1 — one or more violations found
"""

from __future__ import annotations

import glob
import os
import re
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Scope: the Copilot Tuning control and its playbooks only.
TUNING_GLOBS = [
    os.path.join("docs", "controls", "pillar-1-readiness", "1.16-copilot-tuning-governance.md"),
    os.path.join("docs", "playbooks", "control-implementations", "1.16", "*.md"),
]

# Magnitude tokens: comma-grouped thousands (10,000 / 100,000) or K-suffixed (100K / 50K+).
_MAGNITUDE = re.compile(r"\b\d{1,3}(?:,\d{3})+\b|\b\d{1,3}K\+?\b", re.IGNORECASE)

# Data-volume nouns that turn a magnitude into a corpus/data claim.
_DATA_NOUNS = ("document", "item", "file", "record", "corpus", "indexable", "snapshot")

# Nouns that make a magnitude a legitimate, non-data-volume claim (license threshold).
_ALLOWED_NOUNS = ("license", "user", "seat")

_PUBLIC_PREVIEW = re.compile(r"public[\s\-]preview", re.IGNORECASE)


def find_quantitative_violations(text: str):
    """Return (line_no, snippet) for magnitude figures asserted as tuning data minimums.

    A magnitude token is flagged only when the same line references a
    data-volume noun (documents, items, files, ...) and does NOT reference an
    allowed noun (license, user, seat). This flags "100K+ indexable documents"
    while leaving "5,000 Microsoft 365 Copilot licenses" and "at least 20
    example files" untouched.
    """
    violations = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        if not _MAGNITUDE.search(line):
            continue
        lower = line.lower()
        if not any(noun in lower for noun in _DATA_NOUNS):
            continue
        if any(noun in lower for noun in _ALLOWED_NOUNS):
            continue
        violations.append((line_no, line.strip()[:140]))
    return violations


def find_terminology_violations(text: str):
    """Return (line_no, snippet) for "public preview" usage in the tuning file set."""
    violations = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        if _PUBLIC_PREVIEW.search(line):
            violations.append((line_no, line.strip()[:140]))
    return violations


def _iter_tuning_files():
    for pattern in TUNING_GLOBS:
        for path in sorted(glob.glob(os.path.join(REPO_ROOT, pattern))):
            yield path


def main() -> int:
    total = 0
    files_checked = 0
    for path in _iter_tuning_files():
        try:
            with open(path, "r", encoding="utf-8") as fh:
                text = fh.read()
        except (OSError, UnicodeDecodeError):
            continue
        files_checked += 1
        rel = os.path.relpath(path, REPO_ROOT)

        quant = find_quantitative_violations(text)
        term = find_terminology_violations(text)
        if quant or term:
            print(f"VIOLATIONS in {rel}:")
            for line_no, snippet in quant:
                print(f"  Line {line_no}: unsupported data-volume threshold: {snippet}")
            for line_no, snippet in term:
                print(f"  Line {line_no}: use 'early access preview' (Frontier), not 'public preview': {snippet}")
            total += len(quant) + len(term)

    print("\n--- Copilot Tuning Claims Verification Summary ---")
    print(f"Files checked: {files_checked}")
    print(f"Violations: {total}")

    if total:
        print("\nFAILED: Correct the Copilot Tuning claims above before deploying.")
        return 1
    print("\nPASSED: Copilot Tuning claims are source-grounded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
