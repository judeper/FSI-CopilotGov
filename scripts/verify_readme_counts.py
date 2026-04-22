"""Verify hand-typed counts in README.md and AGENTS.md match content-graph.json.

mkdocs-macros plugin renders {{ counts.* }} variables in docs/ files, but README and
AGENTS are rendered directly by GitHub and cannot use macros. This script catches
drift between the canonical content graph and these hand-typed metadata files.

Run as part of CI gate alongside verify_controls and verify_language_rules.
Exit 0 = clean, exit 1 = drift detected.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GRAPH_PATH = REPO_ROOT / "assessment" / "manifest" / "content-graph.json"

# Files that must reflect the canonical counts.
# Each entry: (path, list of (regex_pattern, expected_count_key) tuples).
# The regex must capture the integer in group 1.
TARGETS = [
    (
        REPO_ROOT / "README.md",
        [
            (r"\*\*(\d+)\s+controls\*\*", "controls"),
            (r"\*\*(\d+)\s+playbooks\*\*", "playbooks_total"),
            (r"\|\s*\*\*Controls\*\*\s*\(Technical\)\s*\|[^|]*\|\s*(\d+)\s+controls\s+across", "controls"),
            (r"the\s+(\d+)-control\s+manifest", "controls"),
        ],
    ),
    (
        REPO_ROOT / "AGENTS.md",
        [
            (r"in\s+`docs/`\s+\(framework,\s+(\d+)\s+controls\s+across", "controls"),
            (r"scores\s+collector\s+evidence\s+against\s+the\s+(\d+)-control\s+manifest", "controls"),
            (r"`docs/controls/pillar-\{1-4\}-\*/`\)\s+—\s+(\d+)\s+technical\s+controls", "controls"),
        ],
    ),
]


def load_graph() -> dict:
    if not GRAPH_PATH.exists():
        print(f"ERROR: content-graph.json not found at {GRAPH_PATH}", file=sys.stderr)
        print("       Run: python scripts/build_content_graph.py", file=sys.stderr)
        sys.exit(1)
    return json.loads(GRAPH_PATH.read_text(encoding="utf-8"))


def main() -> int:
    graph = load_graph()
    counts = graph["counts"]
    failures: list[str] = []
    checks_run = 0

    for file_path, patterns in TARGETS:
        if not file_path.exists():
            failures.append(f"{file_path}: file not found")
            continue
        text = file_path.read_text(encoding="utf-8")
        for pattern, count_key in patterns:
            expected = counts.get(count_key)
            if expected is None:
                failures.append(f"{file_path}: counts['{count_key}'] missing from graph")
                continue
            matches = re.findall(pattern, text)
            if not matches:
                failures.append(
                    f"{file_path}: pattern not found (drift may have already happened — re-anchor): {pattern!r}"
                )
                continue
            for actual_str in matches:
                checks_run += 1
                actual = int(actual_str)
                if actual != expected:
                    failures.append(
                        f"{file_path}: pattern {pattern!r} matched {actual} but graph counts['{count_key}'] = {expected}"
                    )

    if failures:
        print("--- README/AGENTS Counts Verification: FAILED ---", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        print(
            "\nFix: update the file to match content-graph.json, or update this script's "
            "regex anchors if the surrounding prose has changed.",
            file=sys.stderr,
        )
        return 1

    print(f"--- README/AGENTS Counts Verification: PASSED ({checks_run} checks) ---")
    return 0


if __name__ == "__main__":
    sys.exit(main())
