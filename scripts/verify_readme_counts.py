"""Verify hand-typed counts in README.md, AGENTS.md, and
.github/copilot-instructions.md match content-graph.json.

mkdocs-macros plugin renders {{ counts.* }} variables in docs/ files, but these
metadata files are rendered directly by GitHub and cannot use macros. This
script catches drift between the canonical content graph and the hand-typed
counts (including per-pillar totals) in these files.

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
# expected_count_key is either a top-level counts key ("controls",
# "playbooks_total", ...) or a per-pillar key of the form "by_pillar:N".
TARGETS = [
    (
        REPO_ROOT / "README.md",
        [
            (r"\*\*(\d+)\s+controls\*\*", "controls"),
            (r"\*\*(\d+)\s+playbooks\*\*", "playbooks_total"),
            (r"\|\s*\*\*Controls\*\*\s*\(Technical\)\s*\|[^|]*\|\s*(\d+)\s+controls\s+across", "controls"),
            (r"the\s+(\d+)-control\s+manifest", "controls"),
            # Pillar focus table: | **N. Name** | focus | COUNT | portals |
            (r"\|\s*\*\*1\.\s*Readiness[^|]*\|[^|]*\|\s*(\d+)\s*\|", "by_pillar:1"),
            (r"\|\s*\*\*2\.\s*Security[^|]*\|[^|]*\|\s*(\d+)\s*\|", "by_pillar:2"),
            (r"\|\s*\*\*3\.\s*Compliance[^|]*\|[^|]*\|\s*(\d+)\s*\|", "by_pillar:3"),
            (r"\|\s*\*\*4\.\s*Operations[^|]*\|[^|]*\|\s*(\d+)\s*\|", "by_pillar:4"),
            # Repo-tree comments: pillar-N-slug/  # COUNT controls
            (r"pillar-1-readiness/\s*#\s*(\d+)\s+controls", "by_pillar:1"),
            (r"pillar-2-security/\s*#\s*(\d+)\s+controls", "by_pillar:2"),
            (r"pillar-3-compliance/\s*#\s*(\d+)\s+controls", "by_pillar:3"),
            (r"pillar-4-operations/\s*#\s*(\d+)\s+controls", "by_pillar:4"),
            # Boundary comparison table (FSI-CopilotGov column = 2nd integer)
            (r"\|\s*\*\*Controls\*\*\s*\|\s*\d+\s*\|\s*(\d+)\s*\|", "controls"),
            (r"\|\s*\*\*Playbooks\*\*\s*\|\s*\d+\s*\|\s*(\d+)\s*\|", "playbooks_total"),
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
    (
        REPO_ROOT / ".github" / "copilot-instructions.md",
        [
            (r"in\s+`docs/`\s+\(framework,\s+(\d+)\s+controls\s+across", "controls"),
            (r"scores\s+collector\s+evidence\s+against\s+the\s+(\d+)-control\s+manifest", "controls"),
            (r"`docs/controls/pillar-\{1-4\}-\*/`\)\s+—\s+(\d+)\s+technical\s+controls", "controls"),
        ],
    ),
]


def _resolve_expected(counts: dict, count_key: str):
    """Resolve an expected value from the counts block. Supports top-level
    keys and per-pillar keys of the form ``by_pillar:N``."""
    if count_key.startswith("by_pillar:"):
        pillar = count_key.split(":", 1)[1]
        return (counts.get("by_pillar") or {}).get(pillar)
    return counts.get(count_key)


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
            expected = _resolve_expected(counts, count_key)
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
