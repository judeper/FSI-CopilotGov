"""Select stale Regulatory Monitor PRs that are safe to close.

The workflow opens monitor PRs from branches named ``monitoring/regulatory-*``.
Open PRs are not cumulative unless their predecessors were merged into
``main`` first, so this selector only closes older PRs when the older PR body
proves it does not carry unique findings, or when the existing rolling
findings behavior applies.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

RESULT_FINDINGS = "findings"
RESULT_UNVERIFIED_CLEAN = "unverified-clean"
RESULT_UNVERIFIED_FINDINGS = "unverified-findings"
RESULT_DEGRADED = "degraded"

AUTO_CLOSE_RESULTS = {
    RESULT_FINDINGS,
    RESULT_UNVERIFIED_CLEAN,
    RESULT_UNVERIFIED_FINDINGS,
    RESULT_DEGRADED,
}


@dataclass(frozen=True)
class PriorPrSelection:
    """A prior PR selected for closure plus the reason for the audit comment."""

    number: int
    reason: str


def _label_names(pr: dict[str, Any]) -> set[str]:
    return {
        str(label.get("name", ""))
        for label in pr.get("labels", [])
        if isinstance(label, dict)
    }


def _body_new_items(body: str) -> int | None:
    match = re.search(r"- Monitor new items:\s*`(\d+)`", body)
    if not match:
        return None
    return int(match.group(1))


def classify_prior_pr(pr: dict[str, Any]) -> str:
    """Classify an older monitor PR from labels plus workflow body markers."""

    labels = _label_names(pr)
    new_items = _body_new_items(str(pr.get("body") or ""))

    if "monitor-degraded" in labels:
        if new_items == 0:
            return "degraded-clean"
        if new_items is not None and new_items > 0:
            return "degraded-findings"
        return "degraded-unknown"

    if "monitor-unverified" in labels:
        if new_items == 0:
            return "unverified-clean"
        if new_items is not None and new_items > 0:
            return "unverified-findings"
        return "unverified-unknown"

    return "findings"


def _is_owned_monitor_pr(pr: dict[str, Any], new_pr: int) -> bool:
    author = pr.get("author")
    author_login = author.get("login") if isinstance(author, dict) else None
    number = pr.get("number")
    if not isinstance(number, int):
        return False
    return (
        number < new_pr
        and str(pr.get("headRefName", "")).startswith("monitoring/regulatory-")
        and author_login == "app/fsi-monitor-bot"
        and str(pr.get("title", "")).startswith("Regulatory Monitor:")
    )


def should_close_prior_pr(new_result: str, prior_kind: str) -> bool:
    """Return whether ``new_result`` safely supersedes ``prior_kind``."""

    if prior_kind == "findings":
        return new_result == RESULT_FINDINGS

    if prior_kind == "unverified-clean":
        return new_result in AUTO_CLOSE_RESULTS

    if prior_kind == "degraded-clean":
        return new_result in {RESULT_FINDINGS, RESULT_DEGRADED}

    return False


def select_prior_prs(
    prs: Iterable[dict[str, Any]],
    *,
    new_pr: int,
    new_result: str,
) -> list[PriorPrSelection]:
    """Select older monitor PRs that the cleanup matrix permits closing."""

    if new_result not in AUTO_CLOSE_RESULTS:
        raise ValueError(f"Unknown new monitor result: {new_result!r}")

    selected: list[PriorPrSelection] = []
    for pr in prs:
        if not _is_owned_monitor_pr(pr, new_pr):
            continue
        prior_kind = classify_prior_pr(pr)
        if should_close_prior_pr(new_result, prior_kind):
            selected.append(
                PriorPrSelection(
                    number=pr["number"],
                    reason=f"{prior_kind} superseded by {new_result}",
                )
            )
    return selected


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Select stale Regulatory Monitor PR numbers to close.",
    )
    parser.add_argument("--new-pr", required=True, type=int)
    parser.add_argument(
        "--new-result",
        required=True,
        choices=sorted(AUTO_CLOSE_RESULTS),
    )
    args = parser.parse_args(argv)

    try:
        prs = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        parser.error(f"failed to parse PR JSON from stdin: {exc}")

    if not isinstance(prs, list):
        parser.error("expected gh pr list JSON array on stdin")

    for selection in select_prior_prs(
        prs,
        new_pr=args.new_pr,
        new_result=args.new_result,
    ):
        print(f"{selection.number}\t{selection.reason}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
