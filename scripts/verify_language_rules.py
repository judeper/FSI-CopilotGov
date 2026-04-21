#!/usr/bin/env python3
"""Verify FSI language rules compliance across all documentation.

Checks that no prohibited phrases appear in documentation files,
as defined by the FSI regulatory language guidelines.

Smart exclusions (ported from FSI-AgentGov v1.3.5):
  - Quoted/code-fenced occurrences (`...`, "...", *...*)
  - Negation context (not, do not, cannot, never, instead of, rather than, etc.)
  - Teaching/reminder lines (do not say, avoid the phrase, ❌, etc.)
  - Lines that enumerate multiple banned phrases (clearly a teaching list)
  - Technical (non-regulatory) senses of 'guarantee' (delivery guarantee,
    durability, idempotency, atomicity, etc.)

File-level overrides (EXEMPT_FILES) remain for documents that are entirely
about prohibited language (e.g., FINRA 2210 detection examples).

Exit codes:
  0 — no violations found
  1 — one or more violations found
"""

import os
import re
import sys

# Fix Unicode encoding issues on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

DOCS_DIR = "docs"

# Compiled patterns for prohibited phrases (case-insensitive).
# Regex form lets us locate match positions for the smart exclusion check.
PROHIBITED_PATTERNS = [
    (re.compile(r"\bensur(?:es?|ing)\s+compliance\b", re.IGNORECASE), "ensures compliance"),
    (re.compile(r"\bguarantees?\b", re.IGNORECASE), "guarantees"),
    (re.compile(r"\bwill\s+prevent\b", re.IGNORECASE), "will prevent"),
    (re.compile(r"\beliminates?\s+(?:the\s+)?risk\b", re.IGNORECASE), "eliminates risk"),
    (re.compile(r"\beliminates?\s+the\s+need\s+for\b", re.IGNORECASE), "eliminates the need for"),
]

# Files that are allowed to contain prohibited phrases entirely
# (for documentation of the rules themselves).
EXEMPT_FILES = [
    os.path.join(".github", "instructions", "fsi-language-rules.instructions.md"),
    # Control 3.5 and its playbooks intentionally contain prohibited marketing
    # language as detection examples for FINRA 2210 Communication Compliance policies
    os.path.join("docs", "controls", "pillar-3-compliance", "3.5-finra-2210-compliance.md"),
    os.path.join("docs", "playbooks", "control-implementations", "3.5", "portal-walkthrough.md"),
    os.path.join("docs", "playbooks", "control-implementations", "3.5", "troubleshooting.md"),
    os.path.join("docs", "playbooks", "control-implementations", "3.5", "verification-testing.md"),
    # Examination-response guidance includes prohibited phrases as examples of
    # wording reviewers should avoid in regulator-facing responses.
    os.path.join("docs", "playbooks", "compliance-and-audit", "examination-response-guide.md"),
]


def _is_excused(line: str, match_start: int, match_end: int) -> bool:
    """Return True if the prohibited match should be excused.

    Excuses (per-occurrence, additive to file-level EXEMPT_FILES):
      - Quoted/code-fenced occurrences (single-line ` " * delimiters)
      - Negation context within ~80 chars before, or ~20 chars after, the match
      - Lines that are teaching about prohibited language
      - Lines enumerating multiple banned phrases together (teaching lists)
      - Technical (non-regulatory) senses of 'guarantee(s)'
    """
    matched = line[match_start:match_end]
    before = line[:match_start]

    # Inside backticks/quotes/asterisks (single-line)
    for delim in ("`", '"', "*"):
        if before.count(delim) % 2 == 1:
            return True

    # Negation in the preceding 80 chars (strip markdown emphasis first)
    window = before[-80:].lower()
    window_clean = (
        window.replace("**", "").replace("*", "").replace("__", "").replace("_", " ")
    )
    negations = (
        " not ", "cannot", "rather than", "instead of",
        "never ", "without ", "doesn't", "don't", "do not", "does not",
        "did not", "would not", "will not", "may not", "shall not",
        "stop", "tempted to", "no by itself", "not by itself",
        "no longer", "nothing", "constitutes legal", "constitutes a",
        "constitute a", "produce a legal", "or a guarantee",
        " no ", "avoid ",
    )
    if any(neg in window_clean for neg in negations):
        return True

    # Technical (non-regulatory) senses of 'guarantee(s)'
    if "guarantee" in matched.lower():
        tech_markers = (
            "transactional", "persistence", "durability", "hashing",
            "idempotenc", "atomicity", "delivery guarantee",
            "ordering guarantee", "consistency guarantee",
        )
        if any(t in line.lower() for t in tech_markers):
            return True

    # "not " near the match (within ~20 chars after)
    after = line[match_end:match_end + 40].lower()
    after_clean = after.replace("**", "").replace("*", "")
    if " not " in after_clean[:20] or after_clean.startswith(" not "):
        return True

    # Teaching/reminder lines
    line_lower = line.lower()
    teaching_markers = (
        "prohibited", "do not use", "do not say", "do not write",
        "avoid the phrase", "avoid using", "hedged language",
        "language reminder", "regulatory hedging", "reminder:",
        "use instead", "in place of", "❌", "implies a legal",
        "wrong:", "right:", "instead of",
    )
    if any(t in line_lower for t in teaching_markers):
        return True

    # Lines that enumerate multiple banned phrases (clearly a teaching list)
    banned_words = ("ensure", "guarantee", "prevent", "eliminate")
    if sum(1 for w in banned_words if w in line_lower) >= 3:
        return True

    return False


def check_file(filepath):
    """Check a single file for prohibited phrases. Returns list of violation strings."""
    violations = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (UnicodeDecodeError, OSError):
        return violations

    for line_num, line in enumerate(content.splitlines(), start=1):
        for pattern, label in PROHIBITED_PATTERNS:
            for m in pattern.finditer(line):
                if _is_excused(line, m.start(), m.end()):
                    continue
                violations.append(
                    f"  Line {line_num}: Found '{label}' in: {line.strip()[:100]}"
                )
                break  # one violation per pattern per line is enough
    return violations


def main():
    total_violations = 0
    files_checked = 0

    for root, dirs, files in os.walk(DOCS_DIR):
        for filename in sorted(files):
            if not filename.endswith(".md"):
                continue

            filepath = os.path.join(root, filename)

            if any(filepath.endswith(exempt) for exempt in EXEMPT_FILES):
                continue

            files_checked += 1
            violations = check_file(filepath)

            if violations:
                print(f"VIOLATIONS in {filepath}:")
                for v in violations:
                    print(v)
                total_violations += len(violations)

    print(f"\n--- Language Rules Verification Summary ---")
    print(f"Files checked: {files_checked}")
    print(f"Violations: {total_violations}")

    if total_violations > 0:
        print("\nFAILED: Fix prohibited language above before deploying.")
        sys.exit(1)
    else:
        print("\nPASSED: All files comply with FSI language rules.")
        sys.exit(0)


if __name__ == "__main__":
    main()
