"""Fail CI when hard-coded headline counts disagree with the content graph.

The repo has had recurring drift where docs / SPA / scripts state stale numbers
("58 controls", "243 playbooks") even after the underlying inventory grew. The
durable fix is the macros pipeline (``{{ counts.controls }}``); this verifier
is the back-stop that catches anything still hand-typed.

Scans markdown, JS/TS, Python and YAML source files for phrases of the form
``<N> controls``, ``<N> playbooks``, ``<N> solutions``, ``<N> pillars`` and
fails when the integer is not in the allowed set derived from
``assessment/manifest/content-graph.json``.

Intentional historical references (CHANGELOG, dated release notes, this file
itself, the verifier's own test) are exempted. Per-pillar control counts (16,
17, 15, 14) are allowed everywhere because they describe sub-totals that are
also derived from the graph.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GRAPH_PATH = REPO_ROOT / "assessment" / "manifest" / "content-graph.json"

PATTERNS: dict[str, re.Pattern[str]] = {
    "controls":  re.compile(r"\b(\d{2,3})\s+controls\b", re.IGNORECASE),
    "playbooks": re.compile(r"\b(\d{2,4})\s+playbooks\b", re.IGNORECASE),
    "solutions": re.compile(r"\b(\d{1,3})\s+(?:sister\s+)?solutions\b", re.IGNORECASE),
    "pillars":   re.compile(r"\b(\d)\s+pillars\b", re.IGNORECASE),
}

SCAN_GLOBS = (
    "README.md",
    "AGENTS.md",
    ".github/copilot-instructions.md",
    "docs/**/*.md",
    "docs/**/*.js",
    "docs/**/*.mjs",
    "assessment/**/*.py",
    "assessment/**/*.md",
    "scripts/**/*.py",
    "scripts/**/*.md",
    "tests/**/*.mjs",
    "tests/**/*.js",
    "tests/**/*.py",
)

EXEMPT_RELATIVE_PATHS = {
    # Historical release notes legitimately cite prior counts.
    "CHANGELOG.md",
    "docs/reference/release-notes-v1.4.md",
    # The verifier itself contains these patterns as code, not claims.
    "scripts/verify_count_consistency.py",
    # This script's smoke test references the patterns intentionally.
    "scripts/test_verify_count_consistency.py",
}

# Substrings that, when present on a matching line, indicate the count refers to
# something other than this framework's inventory and should be ignored:
# - The companion FSI-AgentGov repo's control count (currently 71).
# - Sarbanes-Oxley §§302/404 — the digit "404" is part of the citation, not a count.
EXEMPT_LINE_SUBSTRINGS = (
    "FSI-AgentGov",
    "FSI Agent Governance",
    "AgentGov",
    "Agent Governance",
    "Sarbanes-Oxley",
    "SOX 302",
    "SOX 404",
    "§§302/404",
    "302/404",
)


def _load_allowed() -> dict[str, set[int]]:
    if not GRAPH_PATH.is_file():
        raise SystemExit(
            f"content-graph.json not found at {GRAPH_PATH}; "
            "run 'python scripts/build_content_graph.py' first."
        )
    counts = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))["counts"]
    return {
        # Total controls plus the per-pillar sub-totals (also derived from graph).
        "controls":  {counts["controls"], 16, 17, 15, 14},
        # Total playbooks plus the control-implementation and cross-cutting sub-totals.
        "playbooks": {
            counts["playbooks_total"],
            counts["playbooks_control"],
            counts["playbooks_cross_cutting"],
        },
        "solutions": {counts["solutions"]},
        "pillars":   {counts["pillars"]},
    }


def _iter_files() -> list[Path]:
    seen: set[Path] = set()
    out: list[Path] = []
    for pattern in SCAN_GLOBS:
        for path in REPO_ROOT.glob(pattern):
            if not path.is_file():
                continue
            rel = path.relative_to(REPO_ROOT).as_posix()
            if rel in EXEMPT_RELATIVE_PATHS:
                continue
            if path in seen:
                continue
            seen.add(path)
            out.append(path)
    return out


def _scan_file(path: Path, allowed: dict[str, set[int]]) -> list[tuple[int, str, str]]:
    """Return list of (line_no, kind, snippet) violations."""
    violations: list[tuple[int, str, str]] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return violations
    for line_no, line in enumerate(text.splitlines(), start=1):
        if any(token in line for token in EXEMPT_LINE_SUBSTRINGS):
            continue
        for kind, pattern in PATTERNS.items():
            for match in pattern.finditer(line):
                value = int(match.group(1))
                if value not in allowed[kind]:
                    violations.append((line_no, kind, line.strip()))
    return violations


def main() -> int:
    # Ensure stdout can carry non-ASCII (some docs include box-drawing glyphs).
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    allowed = _load_allowed()
    files = _iter_files()
    failures: list[tuple[Path, int, str, str]] = []

    for path in files:
        for line_no, kind, snippet in _scan_file(path, allowed):
            failures.append((path, line_no, kind, snippet))

    print(f"verify_count_consistency: scanned {len(files)} files")
    print(f"  allowed: {{ {', '.join(f'{k}={sorted(v)}' for k, v in allowed.items())} }}")

    if not failures:
        print("PASSED: no count drift detected.")
        return 0

    print(f"FAILED: {len(failures)} count-drift line(s) detected.")
    for path, line_no, kind, snippet in failures:
        rel = path.relative_to(REPO_ROOT).as_posix()
        print(f"  {rel}:{line_no} [{kind}] {snippet}")
    print(
        "\nFix by replacing the hard-coded number with the macro form, e.g.:\n"
        "  - {{ counts.controls }} / {{ counts.playbooks_total }}\n"
        "  - or load from the manifest at runtime (SPA / scripts).\n"
        "If the value is intentional historical context, add the file to "
        "EXEMPT_RELATIVE_PATHS in scripts/verify_count_consistency.py."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
