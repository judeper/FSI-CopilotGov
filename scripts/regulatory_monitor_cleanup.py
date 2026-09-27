"""Select stale Regulatory Monitor PRs that are safe to close.

The workflow opens monitor PRs from branches named ``monitoring/regulatory-*``.
Open PRs are not cumulative unless their predecessors were merged into
``main`` first, so this selector only closes older PRs when the older PR body
contains a workflow-written marker proving cleanup is safe.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

RESULT_FINDINGS = "findings"
RESULT_UNVERIFIED_CLEAN = "unverified-clean"
RESULT_UNVERIFIED_FINDINGS = "unverified-findings"
RESULT_DEGRADED = "degraded"
RESULT_VERIFIED_CLEAN = "verified-clean"

AUTO_CLOSE_RESULTS = {
    RESULT_FINDINGS,
    RESULT_UNVERIFIED_CLEAN,
    RESULT_UNVERIFIED_FINDINGS,
    RESULT_DEGRADED,
    RESULT_VERIFIED_CLEAN,
}

ITEM_KEY_CAP = 1000
MARKER_BEGIN = "<!-- regulatory-monitor-cleanup:v1"
MARKER_END = "-->"
MARKER_BLOCK_RE = re.compile(
    rf"(?s)(?:^|\n){re.escape(MARKER_BEGIN)}\n(.*?)\n{re.escape(MARKER_END)}\s*\Z"
)
REPORT_LINK_RE = re.compile(
    r"^(?:### \d+\. \[[^\]]+\]\(([^)\s]+)\)|- \[[^\]]+\]\(([^)\s]+)\))"
)


@dataclass(frozen=True)
class PriorPrSelection:
    """A prior PR selected for closure plus the reason for the audit comment."""

    number: int
    reason: str


@dataclass(frozen=True)
class CleanupMarker:
    """Parsed workflow-owned cleanup marker from a monitor PR body."""

    result: str
    new_items: int
    item_keys_count: int
    item_keys_status: str
    item_keys_sha256: str
    item_keys: frozenset[str]

    @property
    def has_complete_keys(self) -> bool:
        return (
            self.item_keys_status == "complete"
            and len(self.item_keys) == self.item_keys_count
            and self.item_keys_count == self.new_items
        )


@dataclass(frozen=True)
class PriorPrInfo:
    """Safety-relevant classification for a prior monitor PR."""

    kind: str
    marker: CleanupMarker | None

    @property
    def complete_item_keys(self) -> frozenset[str] | None:
        if self.marker and self.marker.has_complete_keys:
            return self.marker.item_keys
        return None


def _label_names(pr: dict[str, Any]) -> set[str]:
    return {
        str(label.get("name", ""))
        for label in pr.get("labels", [])
        if isinstance(label, dict)
    }


def _hash_keys(keys: Sequence[str]) -> str:
    return hashlib.sha256("\n".join(keys).encode("utf-8")).hexdigest()


def extract_item_keys_from_report(report_text: str) -> list[str]:
    """Extract stable item keys from the generated markdown report."""

    keys: set[str] = set()
    for line in report_text.splitlines():
        match = REPORT_LINK_RE.match(line)
        if not match:
            continue
        key = match.group(1) or match.group(2)
        if key:
            keys.add(key)
    return sorted(keys)


def build_cleanup_marker(
    *,
    result: str,
    new_items: int,
    item_keys: Sequence[str],
    cap: int = ITEM_KEY_CAP,
) -> str:
    """Build the hidden workflow-owned PR body marker."""

    if result not in AUTO_CLOSE_RESULTS - {RESULT_VERIFIED_CLEAN}:
        raise ValueError(f"reportable PR result cannot be {result!r}")
    if new_items < 0:
        raise ValueError("new_items must be non-negative")

    sorted_keys = sorted(set(item_keys))
    if len(sorted_keys) != new_items:
        status = "parse-mismatch"
    elif len(sorted_keys) > cap:
        status = "truncated"
    else:
        status = "complete"

    emitted_keys = sorted_keys[:cap]
    lines = [
        MARKER_BEGIN,
        f"result={result}",
        f"new_items={new_items}",
        f"item_keys_count={len(sorted_keys)}",
        f"item_keys_status={status}",
        f"item_keys_sha256={_hash_keys(sorted_keys)}",
        "item_keys:",
        *emitted_keys,
        MARKER_END,
    ]
    return "\n".join(lines)


def _parse_cleanup_marker(body: str) -> CleanupMarker | None:
    matches = MARKER_BLOCK_RE.findall(body)
    if len(matches) != 1:
        return None

    field_lines: list[str] = []
    key_lines: list[str] = []
    in_keys = False
    for line in matches[0].splitlines():
        if line == "item_keys:":
            if in_keys:
                return None
            in_keys = True
            continue
        if in_keys:
            key_lines.append(line)
        else:
            field_lines.append(line)

    if not in_keys:
        return None

    fields: dict[str, str] = {}
    for line in field_lines:
        if "=" not in line:
            return None
        key, value = line.split("=", 1)
        if key in fields:
            return None
        fields[key] = value

    if set(fields) != {
        "result",
        "new_items",
        "item_keys_count",
        "item_keys_status",
        "item_keys_sha256",
    }:
        return None

    result = fields["result"]
    if result not in AUTO_CLOSE_RESULTS - {RESULT_VERIFIED_CLEAN}:
        return None
    if fields["item_keys_status"] not in {
        "complete",
        "truncated",
        "parse-mismatch",
    }:
        return None

    try:
        new_items = int(fields["new_items"])
        item_keys_count = int(fields["item_keys_count"])
    except ValueError:
        return None
    if new_items < 0 or item_keys_count < 0:
        return None
    if any(not key for key in key_lines):
        return None

    unique_keys = sorted(set(key_lines))
    if len(unique_keys) != len(key_lines):
        return None
    if len(key_lines) > item_keys_count:
        return None
    if fields["item_keys_status"] == "complete":
        if len(key_lines) != item_keys_count:
            return None
        if item_keys_count != new_items:
            return None
        if fields["item_keys_sha256"] != _hash_keys(unique_keys):
            return None

    return CleanupMarker(
        result=result,
        new_items=new_items,
        item_keys_count=item_keys_count,
        item_keys_status=fields["item_keys_status"],
        item_keys_sha256=fields["item_keys_sha256"],
        item_keys=frozenset(unique_keys),
    )


def _classify_from_marker_and_labels(
    marker: CleanupMarker | None,
    labels: set[str],
) -> PriorPrInfo:
    has_degraded = "monitor-degraded" in labels
    has_unverified = "monitor-unverified" in labels

    if has_degraded and has_unverified:
        return PriorPrInfo("unknown", marker)
    if marker is None:
        return PriorPrInfo("unknown", None)

    if has_degraded:
        if marker.result != RESULT_DEGRADED:
            return PriorPrInfo("unknown", marker)
        return PriorPrInfo(
            "degraded-clean" if marker.new_items == 0 else "degraded-findings",
            marker,
        )

    if has_unverified:
        if marker.result == RESULT_UNVERIFIED_CLEAN and marker.new_items == 0:
            return PriorPrInfo("unverified-clean", marker)
        if marker.result == RESULT_UNVERIFIED_FINDINGS and marker.new_items > 0:
            return PriorPrInfo("unverified-findings", marker)
        return PriorPrInfo("unknown", marker)

    if marker.result == RESULT_FINDINGS and marker.new_items > 0:
        return PriorPrInfo("findings", marker)

    return PriorPrInfo("unknown", marker)


def classify_prior_pr(pr: dict[str, Any]) -> PriorPrInfo:
    """Classify an older monitor PR from a workflow marker plus labels."""

    marker = _parse_cleanup_marker(str(pr.get("body") or ""))
    return _classify_from_marker_and_labels(marker, _label_names(pr))


def _is_owned_monitor_pr(pr: dict[str, Any], new_pr: int | None) -> bool:
    author = pr.get("author")
    author_login = author.get("login") if isinstance(author, dict) else None
    number = pr.get("number")
    if not isinstance(number, int):
        return False
    return (
        (new_pr is None or number < new_pr)
        and str(pr.get("headRefName", "")).startswith("monitoring/regulatory-")
        and author_login == "app/fsi-monitor-bot"
        and str(pr.get("title", "")).startswith("Regulatory Monitor:")
    )


def should_close_prior_pr(
    new_result: str,
    prior_info: PriorPrInfo,
    *,
    new_item_keys: frozenset[str] | None = None,
) -> bool:
    """Return whether ``new_result`` safely supersedes ``prior_info``."""

    if prior_info.kind == "findings":
        old_item_keys = prior_info.complete_item_keys
        return (
            new_result == RESULT_FINDINGS
            and old_item_keys is not None
            and new_item_keys is not None
            and old_item_keys.issubset(new_item_keys)
        )

    if prior_info.kind == "unverified-clean":
        return new_result in AUTO_CLOSE_RESULTS

    if prior_info.kind == "degraded-clean":
        return new_result in {
            RESULT_FINDINGS,
            RESULT_DEGRADED,
            RESULT_VERIFIED_CLEAN,
        }

    return False


def _load_complete_keys_from_report(report_file: str | None) -> frozenset[str] | None:
    if not report_file:
        return None
    report_text = Path(report_file).read_text(encoding="utf-8")
    keys = extract_item_keys_from_report(report_text)
    new_items_matches = re.findall(r"(?m)^\*\*New Items:\*\* (\d+)$", report_text)
    if len(new_items_matches) != 1:
        return None
    new_items = int(new_items_matches[0])
    if len(keys) != new_items or len(keys) > ITEM_KEY_CAP:
        return None
    return frozenset(keys)


def select_prior_prs(
    prs: Iterable[dict[str, Any]],
    *,
    new_pr: int | None,
    new_result: str,
    new_item_keys: frozenset[str] | None = None,
) -> list[PriorPrSelection]:
    """Select older monitor PRs that the cleanup matrix permits closing."""

    if new_result not in AUTO_CLOSE_RESULTS:
        raise ValueError(f"Unknown new monitor result: {new_result!r}")

    selected: list[PriorPrSelection] = []
    for pr in prs:
        if not _is_owned_monitor_pr(pr, new_pr):
            continue
        prior_info = classify_prior_pr(pr)
        if should_close_prior_pr(
            new_result,
            prior_info,
            new_item_keys=new_item_keys,
        ):
            selected.append(
                PriorPrSelection(
                    number=pr["number"],
                    reason=f"{prior_info.kind} superseded by {new_result}",
                )
            )
    return selected


def _emit_marker(args: argparse.Namespace) -> int:
    try:
        new_items = int(args.new_items)
    except ValueError:
        print("new_items must be an integer", file=sys.stderr)
        return 2

    report_text = Path(args.report_file).read_text(encoding="utf-8")
    marker = build_cleanup_marker(
        result=args.result,
        new_items=new_items,
        item_keys=extract_item_keys_from_report(report_text),
    )
    print(f"{args.output_name}<<EOF")
    print(marker)
    print("EOF")
    return 0


def _select(args: argparse.Namespace) -> int:
    try:
        prs = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(f"failed to parse PR JSON from stdin: {exc}", file=sys.stderr)
        return 2

    if not isinstance(prs, list):
        print("expected gh pr list JSON array on stdin", file=sys.stderr)
        return 2

    new_item_keys = _load_complete_keys_from_report(args.new_report_file)
    for selection in select_prior_prs(
        prs,
        new_pr=args.new_pr,
        new_result=args.new_result,
        new_item_keys=new_item_keys,
    ):
        print(f"{selection.number}\t{selection.reason}")

    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Select stale Regulatory Monitor PR numbers to close.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    marker_parser = subparsers.add_parser(
        "emit-marker",
        help="Emit a workflow-owned PR body marker as a GitHub output.",
    )
    marker_parser.add_argument("--report-file", required=True)
    marker_parser.add_argument(
        "--result",
        required=True,
        choices=sorted(AUTO_CLOSE_RESULTS - {RESULT_VERIFIED_CLEAN}),
    )
    marker_parser.add_argument("--new-items", required=True)
    marker_parser.add_argument("--output-name", default="cleanup_marker")
    marker_parser.set_defaults(func=_emit_marker)

    select_parser = subparsers.add_parser(
        "select",
        help="Read gh pr list JSON from stdin and print PR numbers to close.",
    )
    select_parser.add_argument("--new-pr", type=int)
    select_parser.add_argument(
        "--new-result",
        required=True,
        choices=sorted(AUTO_CLOSE_RESULTS),
    )
    select_parser.add_argument("--new-report-file")
    select_parser.set_defaults(func=_select)

    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
