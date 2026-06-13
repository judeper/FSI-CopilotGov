#!/usr/bin/env python3
"""Verify framework version stamps across canonical surface files.

Ported from FSI-AgentGov (``scripts/verify_version_stamps.py``) and adapted to
FSI-CopilotGov's single footer format. This is the *version* half of the
count/version drift gate; the *count* half lives in
``scripts/verify_count_consistency.py`` and ``scripts/verify_readme_counts.py``.

Scope:
    Catch drift in *footer / metadata stamps* -- NOT body text. Historical
    narrative such as "As of v1.4.0, the repository..." in README/AGENTS is
    intentional and must never trip this check, because the footer regex is
    anchored to a whole line of the exact stamp shape.

Canonical version source:
    Repo-root ``VERSION`` file (single line, e.g. ``1.7.1``). The MkDocs build
    hook (``scripts/hooks/version_json.py``) also reads this file and embeds the
    value into ``version.json`` at build time, so the deployed site exposes the
    canonical version alongside the build SHA.

What this script enforces:
    Every page that carries the canonical site footer stamp::

        *FSI Copilot Governance Framework vX.Y.Z - <Month Year>*

    must state a version literal equal to the canonical ``VERSION``. Pages
    without the footer (NO-MATCH) are skipped silently -- this scanner only
    enforces files that *do* stamp a version in the canonical footer format.

Modes:
    default     Scan and print a report. Exit 0 regardless of drift.
    --check     Same scan; exit 1 if any non-allowlisted file is drifted.

Allowlist:
    ``_KNOWN_DRIFT_ALLOWLIST`` grandfathers files that are intentionally
    pinned to a prior version. It is intentionally empty -- any future drift
    becomes a blocking CI failure. Add an entry only with an inline comment
    explaining why the drift is permanent. The script reports any allowlisted
    file that is no longer drifted so stale entries are removed.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = REPO_ROOT / "VERSION"

# Anchored to a whole line so body prose (e.g. "As of v1.4.0, ...") never
# matches -- only the canonical footer stamp does. The capture group is the
# version literal.
FOOTER_RE = re.compile(
    r"^\*FSI Copilot Governance Framework v(\d+\.\d+(?:\.\d+)?)\b.*\*\s*$",
    re.M,
)

# Files scanned for the footer stamp. README is an explicit entry; the docs
# tree is globbed (every rendered page carries the footer).
EXPLICIT_FILES = ("README.md",)
DOCS_GLOB = "docs/**/*.md"

# Files intentionally pinned to a prior version. Intentionally empty.
_KNOWN_DRIFT_ALLOWLIST: set[str] = set()


def read_canonical_version() -> str:
    if not VERSION_FILE.exists():
        sys.stderr.write(
            f"ERROR: canonical VERSION file not found at {VERSION_FILE}\n"
        )
        sys.exit(2)
    raw = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+(\.\d+)?", raw):
        sys.stderr.write(
            f"ERROR: VERSION file content {raw!r} is not a valid semver-ish "
            "literal (expected e.g. 1.7.1)\n"
        )
        sys.exit(2)
    return raw


class Result:
    def __init__(self, path: str, found: str | None, expected: str):
        self.path = path
        self.found = found
        self.expected = expected

    @property
    def status(self) -> str:
        if self.found is None:
            return "NO-MATCH"
        return "OK" if self.found == self.expected else "DRIFT"


def scan_file(path: Path) -> str | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    matches = FOOTER_RE.findall(text)
    if not matches:
        return None
    first = matches[0]
    return first if isinstance(first, str) else first[0]


def _iter_scan_paths() -> list[Path]:
    seen: set[Path] = set()
    out: list[Path] = []
    for rel in EXPLICIT_FILES:
        p = REPO_ROOT / rel
        if p not in seen:
            seen.add(p)
            out.append(p)
    for p in sorted(REPO_ROOT.glob(DOCS_GLOB)):
        if p.is_file() and p not in seen:
            seen.add(p)
            out.append(p)
    return out


def collect_results(canonical: str) -> list[Result]:
    results: list[Result] = []
    for path in _iter_scan_paths():
        found = scan_file(path)
        rel = path.relative_to(REPO_ROOT).as_posix()
        results.append(Result(rel, found, canonical))
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 on non-allowlisted drift (CI mode). Default reports only.",
    )
    args = parser.parse_args()

    canonical = read_canonical_version()
    results = collect_results(canonical)

    drifted = [r for r in results if r.status == "DRIFT"]
    no_match = [r for r in results if r.status == "NO-MATCH"]
    ok = [r for r in results if r.status == "OK"]

    print(f"Canonical version (from VERSION): {canonical}")
    print(f"Files scanned: {len(results)}")
    print(f"  OK (footer matches):      {len(ok)}")
    print(f"  DRIFT:                    {len(drifted)}")
    print(f"  NO-MATCH (footer absent): {len(no_match)}")
    print()

    if drifted:
        print("DRIFT detected (file -> found / expected):")
        for r in drifted:
            tag = (
                "  [allowlisted]"
                if r.path in _KNOWN_DRIFT_ALLOWLIST
                else "  [BLOCKING] "
            )
            print(f"{tag} {r.path:60s} {r.found} -> {r.expected}")
        print()

    drifted_paths = {r.path for r in drifted}
    stale_entries = sorted(
        p for p in _KNOWN_DRIFT_ALLOWLIST if p not in drifted_paths
    )
    if stale_entries:
        print(
            "STALE allowlist entries (file is no longer drifted; remove from "
            "_KNOWN_DRIFT_ALLOWLIST):"
        )
        for p in stale_entries:
            print(f"  - {p}")
        print()

    blocking = [r for r in drifted if r.path not in _KNOWN_DRIFT_ALLOWLIST]

    if args.check:
        if blocking:
            print(
                f"FAIL: {len(blocking)} file(s) drifted from canonical version "
                f"{canonical} and are not allowlisted.\n"
                "Fix: bump the footer stamp to match the repo-root VERSION file "
                "(the single source of truth)."
            )
            return 1
        if stale_entries:
            print(
                f"FAIL: {len(stale_entries)} stale allowlist entr(y/ies) must "
                "be removed from _KNOWN_DRIFT_ALLOWLIST."
            )
            return 1
        print("PASS: no non-allowlisted version-stamp drift detected.")
        return 0

    print("(report-only mode; pass --check for CI gating)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
