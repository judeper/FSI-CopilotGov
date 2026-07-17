#!/usr/bin/env python3
"""Validate targeted regulatory citation integrity guards."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTROL_35_PATH = (
    REPO_ROOT
    / "docs"
    / "controls"
    / "pillar-3-compliance"
    / "3.5-finra-2210-compliance.md"
)
DERIVED_PATHS = (
    REPO_ROOT / "assessment" / "manifest" / "controls.json",
    REPO_ROOT / "assessment" / "manifest" / "content-graph.json",
)
RISK_ALERT_LINK_RE = re.compile(r"\[([^\]]*risk alert[^\]]*)\]\(([^)]+)\)", re.IGNORECASE)
GENERIC_SEC_DIVISION_PATHS = {
    "/about/divisions-offices/division-examinations",
    "/about/divisions-offices/division-enforcement",
}


def check_finra_partial_amendment_pairing(content: str) -> list[str]:
    errors: list[str] = []
    if "34-103492" in content:
        errors.append("stale SEC Release 34-103492 is present; use 34-105845.")
    if "2026-13713" in content and "34-105845" not in content:
        errors.append("FR document 2026-13713 appears without SEC Release 34-105845.")
    if "34-105845" in content and "SR-FINRA-2026-004" not in content:
        errors.append("SEC Release 34-105845 appears without SR-FINRA-2026-004.")
    return errors


def is_generic_sec_division_url(url: str) -> bool:
    parsed = urlparse(url.strip())
    if parsed.scheme not in {"http", "https"}:
        return False
    if not parsed.netloc.lower().endswith("sec.gov"):
        return False
    path = parsed.path.rstrip("/")
    return path in GENERIC_SEC_DIVISION_PATHS


def find_mislabeled_risk_alert_links(markdown: str) -> list[tuple[str, str]]:
    violations: list[tuple[str, str]] = []
    for label, url in RISK_ALERT_LINK_RE.findall(markdown):
        if is_generic_sec_division_url(url):
            violations.append((label.strip(), url.strip()))
    return violations


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    if not CONTROL_35_PATH.is_file():
        print(f"ERROR: missing expected file {CONTROL_35_PATH}", file=sys.stderr)
        return 2

    control_35 = _read_text(CONTROL_35_PATH)
    for err in check_finra_partial_amendment_pairing(control_35):
        errors.append(f"{CONTROL_35_PATH.relative_to(REPO_ROOT).as_posix()}: {err}")

    for path in DERIVED_PATHS:
        if not path.is_file():
            continue
        text = _read_text(path)
        if "34-103492" in text:
            errors.append(
                f"{path.relative_to(REPO_ROOT).as_posix()}: stale SEC Release 34-103492 is present."
            )

    for md in sorted((REPO_ROOT / "docs").rglob("*.md")):
        text = _read_text(md)
        for label, url in find_mislabeled_risk_alert_links(text):
            errors.append(
                f"{md.relative_to(REPO_ROOT).as_posix()}: '{label}' points to generic SEC division page ({url})."
            )

    if errors:
        print("Regulatory citation verification FAILED:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(
        "Regulatory citation verification passed "
        "(34-105845/2026-13713 pairing and Risk Alert link labeling)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
