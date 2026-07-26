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

# Target files that MUST exist for the verifier to be meaningful.  A missing
# file is an actionable failure — it likely means the control was renamed or
# moved without updating this guard.
REQUIRED_FILES = [
    os.path.join(
        "docs", "controls", "pillar-1-readiness", "1.16-copilot-tuning-governance.md"
    ),
]

# Magnitude tokens:
#   - comma-grouped thousands: 10,000 / 100,000
#   - K or M suffix:           100K / 50K+ / 1M / 2M+
#   - bare large integers:     100000 (≥ 5 digits catches ≥ 10 000 without comma grouping)
_MAGNITUDE = re.compile(
    r"\b\d{1,3}(?:,\d{3})+\b"  # comma-grouped thousands: 10,000 / 100,000
    r"|\b\d{1,3}[KM]\+?\b"     # K/M suffix: 100K, 100K+, 1M, 2M+
    r"|\b\d{5,}\b",            # bare integers ≥ 5 digits: 100000
    re.IGNORECASE,
)

# Data-volume nouns that turn a magnitude into a corpus/data claim.
_DATA_NOUNS = ("document", "item", "file", "record", "corpus", "indexable", "snapshot")

# Nouns that make a magnitude a legitimate, non-data-volume claim (license threshold).
_ALLOWED_NOUNS = ("license", "user", "seat")

# How many words around a magnitude token to search for an allowed noun.
# Narrow enough that "5,000 licenses" on a different clause does NOT exempt
# "100K+ indexable documents" earlier on the same line (closing the
# line-global suppression bypass).
_ALLOWED_PROXIMITY_WORDS = 5

_PUBLIC_PREVIEW = re.compile(r"public[\s\-]preview", re.IGNORECASE)

# Strip URL content before magnitude scanning to prevent false positives from
# path-segment numbers in hyperlinks (e.g. /2023-12247/ in a federalregister URL).
_MD_LINK_URL = re.compile(r"\(https?://[^\s)]*\)", re.IGNORECASE)
_BARE_URL = re.compile(r"https?://\S+", re.IGNORECASE)


def _strip_urls(line: str) -> str:
    """Remove URL substrings so path-segment numbers are not mistaken for corpus claims."""
    line = _MD_LINK_URL.sub("", line)
    line = _BARE_URL.sub("", line)
    return line


def _magnitude_near_allowed_noun(scannable: str, match: re.Match) -> bool:
    """Return True if an allowed noun appears within _ALLOWED_PROXIMITY_WORDS words
    of the matched magnitude token.

    Per-magnitude proximity replaces the previous line-global allowed-noun
    check, which could be bypassed by appending any allowed noun anywhere on
    the same line as a fabricated corpus figure.

    ``scannable`` is the URL-stripped copy of the line; both the match and
    this proximity window operate on the same string.
    """
    words = scannable.split()
    # Locate which word index contains the start of the magnitude match.
    pos = 0
    mag_idx = len(words) - 1
    for i, word in enumerate(words):
        if pos + len(word) > match.start():
            mag_idx = i
            break
        pos += len(word) + 1  # +1 for the space separator
    lo = max(0, mag_idx - _ALLOWED_PROXIMITY_WORDS)
    hi = min(len(words), mag_idx + _ALLOWED_PROXIMITY_WORDS + 1)
    window = " ".join(words[lo:hi]).lower()
    return any(noun in window for noun in _ALLOWED_NOUNS)


def find_quantitative_violations(text: str):
    """Return (line_no, snippet) for magnitude figures asserted as tuning data minimums.

    A magnitude token is flagged when:
      1. The URL-stripped line contains a data-volume noun (document, item, file, …), AND
      2. The magnitude is NOT within _ALLOWED_PROXIMITY_WORDS words of an allowed
         noun (license, user, seat).

    URL content is stripped before scanning to prevent false positives from
    path-segment numbers embedded in hyperlinks (e.g. /2023-12247/).

    This flags "100K+ indexable documents" and "1M files" while leaving
    "5,000 Microsoft 365 Copilot licenses" and "at least 20 example files"
    untouched.  Each magnitude match is checked independently, closing the
    line-global suppression bypass where any allowed noun on the line would
    previously exempt the entire line.
    """
    violations = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        scannable = _strip_urls(line)
        lower = scannable.lower()
        if not any(noun in lower for noun in _DATA_NOUNS):
            continue
        line_flagged = False
        for match in _MAGNITUDE.finditer(scannable):
            if _magnitude_near_allowed_noun(scannable, match):
                continue
            if not line_flagged:
                violations.append((line_no, line.strip()[:140]))
                line_flagged = True
    return violations


def find_terminology_violations(text: str):
    """Return (line_no, snippet) for "public preview" usage in the tuning file set."""
    violations = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        if _PUBLIC_PREVIEW.search(line):
            violations.append((line_no, line.strip()[:140]))
    return violations


def check_required_files(root: str | None = None) -> list[str]:
    """Return relative paths of required target files that are absent.

    Accepts an optional ``root`` override so unit tests can probe an
    arbitrary directory without touching the live repository tree.
    """
    r = root if root is not None else REPO_ROOT
    return [rel for rel in REQUIRED_FILES if not os.path.isfile(os.path.join(r, rel))]


def _iter_tuning_files():
    for pattern in TUNING_GLOBS:
        for path in sorted(glob.glob(os.path.join(REPO_ROOT, pattern))):
            yield path


def main() -> int:
    missing = check_required_files()
    if missing:
        for rel in missing:
            print(f"ERROR: Required target file not found: {rel}")
        print(
            "\nFAILED: Expected Copilot Tuning target files are missing."
            " Rename or restore the files, then re-run this check."
        )
        return 1

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
