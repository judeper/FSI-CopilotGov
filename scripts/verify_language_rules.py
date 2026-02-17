#!/usr/bin/env python3
"""Verify FSI language rules compliance across all documentation.

Checks that no prohibited phrases appear in documentation files,
as defined by the FSI regulatory language guidelines.
"""

import os
import re
import sys

DOCS_DIR = "docs"

PROHIBITED_PHRASES = [
    "ensures compliance",
    "ensure compliance",
    "ensuring compliance",
    "guarantees",
    "will prevent",
    "eliminates risk",
    "eliminates the risk",
    "eliminate risk",
]

# Files that are allowed to contain prohibited phrases (for documentation of the rules themselves)
EXEMPT_FILES = [
    os.path.join(".github", "instructions", "fsi-language-rules.instructions.md"),
]


def check_file(filepath):
    """Check a single file for prohibited phrases. Returns list of violations."""
    violations = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line_lower = line.lower()
            for phrase in PROHIBITED_PHRASES:
                if phrase in line_lower:
                    violations.append(
                        f"  Line {line_num}: Found '{phrase}' in: {line.strip()[:100]}"
                    )
    return violations


def main():
    total_violations = 0
    files_checked = 0

    for root, dirs, files in os.walk(DOCS_DIR):
        for filename in sorted(files):
            if not filename.endswith(".md"):
                continue

            filepath = os.path.join(root, filename)

            # Skip exempt files
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
