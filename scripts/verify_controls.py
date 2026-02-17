#!/usr/bin/env python3
"""Verify control file structure for FSI-CopilotGov.

Validates that each control markdown file contains the required sections
and metadata fields as defined by the framework's 10-section format.
"""

import os
import re
import sys

CONTROLS_DIR = os.path.join("docs", "controls")

PILLAR_DIRS = [
    "pillar-1-readiness",
    "pillar-2-security",
    "pillar-3-compliance",
    "pillar-4-operations",
]

REQUIRED_METADATA = [
    "Control ID:",
    "Pillar:",
    "Last Verified:",
]

REQUIRED_SECTIONS = [
    "## Objective",
    "## Why This Matters for FSI",
    "## Control Description",
    "## Verification Criteria",
    "## Additional Resources",
]

RECOMMENDED_SECTIONS = [
    "## Copilot Surface Coverage",
    "## Governance Levels",
    "## Setup & Configuration",
    "## Financial Sector Considerations",
]


def verify_control(filepath):
    """Verify a single control file. Returns list of errors."""
    errors = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check required metadata
    for meta in REQUIRED_METADATA:
        if meta not in content:
            errors.append(f"  Missing metadata: {meta}")

    # Check required sections
    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"  Missing required section: {section}")

    # Check recommended sections (warn only)
    warnings = []
    for section in RECOMMENDED_SECTIONS:
        if section not in content:
            warnings.append(f"  Missing recommended section: {section}")

    return errors, warnings


def main():
    total_errors = 0
    total_warnings = 0
    total_controls = 0

    for pillar_dir in PILLAR_DIRS:
        pillar_path = os.path.join(CONTROLS_DIR, pillar_dir)
        if not os.path.isdir(pillar_path):
            print(f"WARNING: Pillar directory not found: {pillar_path}")
            continue

        for filename in sorted(os.listdir(pillar_path)):
            if filename == "index.md" or not filename.endswith(".md"):
                continue

            filepath = os.path.join(pillar_path, filename)
            total_controls += 1
            errors, warnings = verify_control(filepath)

            if errors:
                print(f"ERRORS in {filepath}:")
                for e in errors:
                    print(e)
                total_errors += len(errors)

            if warnings:
                total_warnings += len(warnings)

    print(f"\n--- Control Verification Summary ---")
    print(f"Controls checked: {total_controls}")
    print(f"Errors: {total_errors}")
    print(f"Warnings: {total_warnings}")

    if total_errors > 0:
        print("\nFAILED: Fix errors above before deploying.")
        sys.exit(1)
    else:
        print("\nPASSED: All controls meet required structure.")
        sys.exit(0)


if __name__ == "__main__":
    main()
