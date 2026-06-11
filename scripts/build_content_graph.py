"""Build the canonical content graph for FSI-CopilotGov.

Walks the documentation tree (controls, playbooks) and the solutions lock,
emitting `assessment/manifest/content-graph.json` as a single source of
truth for downstream tooling (manifest generation, drift checks, site
build verification).

Stdlib only -- no external dependencies.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS = REPO_ROOT / "docs"
CONTROLS_DIR = DOCS / "controls"
PLAYBOOKS_DIR = DOCS / "playbooks"
CONTROL_IMPL_DIR = PLAYBOOKS_DIR / "control-implementations"
SOLUTIONS_LOCK = REPO_ROOT / "assessment" / "data" / "solutions-lock.json"
OUTPUT_PATH = REPO_ROOT / "assessment" / "manifest" / "content-graph.json"
CHECKLIST_PATH = DOCS / "getting-started" / "checklist.md"

CROSS_CUTTING_CATEGORIES = (
    "compliance-and-audit",
    "getting-started",
    "governance-operations",
    "incident-and-risk",
    "regulatory-modules",
)

PILLAR_DIRS = {
    "pillar-1-readiness": 1,
    "pillar-2-security": 2,
    "pillar-3-compliance": 3,
    "pillar-4-operations": 4,
}

# 1.1.0 adds per-control ``tier`` plus ``counts.by_tier`` / ``counts.by_pillar_tier``.
SCHEMA_VERSION = "1.1.0"

# Per-control governance tier (the control's "entry tier") is authored as the
# single-letter Level code in the per-control tables of
# docs/getting-started/checklist.md. That column is the canonical source for
# each control's headline tier; the tier subtotals rendered in the checklist
# summary are derived from it via the content graph (never hand-typed).
TIER_ORDER = ("Baseline", "Recommended", "Regulated")
TIER_BY_CODE = {"B": "Baseline", "R": "Recommended", "Reg": "Regulated"}

CONTROL_ID_RE = re.compile(r"\*\*Control ID:\*\*\s*([0-9A-Za-z.\-]+)")
PILLAR_RE = re.compile(r"\*\*Pillar:\*\*\s*(.+)")
LAST_VERIFIED_RE = re.compile(r"\*\*Last Verified:\*\*\s*([0-9]{4}-[0-9]{2}-[0-9]{2})")
REG_REF_RE = re.compile(r"\*\*Regulatory Reference:\*\*\s*(.+)")
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
# Per-control checklist row: "| [ ] | <id> | <title> | <Level> | ... |".
# The ID cell must be a control number, which skips the "—" sub-item rows,
# the legend table, and the Summary-by-Governance-Level table.
CHECKLIST_ROW_RE = re.compile(
    r"^\|\s*\[\s*[xX]?\s*\]\s*\|\s*([0-9]+\.[0-9]+[a-z]?)\s*\|[^|]*\|\s*([A-Za-z]+)\s*\|",
    re.MULTILINE,
)


def _rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def _read_head(path: Path, limit: int = 4000) -> str:
    return path.read_text(encoding="utf-8", errors="replace")[:limit]


def _split_reg_refs(raw: str) -> list[str]:
    # Regulatory reference is a comma-separated list with parenthetical
    # qualifiers; split only on top-level commas.
    out: list[str] = []
    depth = 0
    buf: list[str] = []
    for ch in raw.strip():
        if ch == "(":
            depth += 1
            buf.append(ch)
        elif ch == ")":
            depth = max(0, depth - 1)
            buf.append(ch)
        elif ch == "," and depth == 0:
            piece = "".join(buf).strip()
            if piece:
                out.append(piece)
            buf = []
        else:
            buf.append(ch)
    tail = "".join(buf).strip()
    if tail:
        out.append(tail)
    return out


def collect_control_tiers() -> dict[str, str]:
    """Map control id -> governance tier from the checklist Level column.

    ``docs/getting-started/checklist.md`` is the canonical, human-authored
    home of each control's headline (entry) tier. Its per-control rows look
    like ``| [ ] | 1.1 | Title | B | ... |``; the single-letter Level code is
    translated to a full tier name. Rows that are not real controls (the
    ``—`` sub-item rows, the legend table, and the summary table) do not match
    ``CHECKLIST_ROW_RE`` and are ignored.
    """
    tiers: dict[str, str] = {}
    if not CHECKLIST_PATH.is_file():
        return tiers
    text = CHECKLIST_PATH.read_text(encoding="utf-8", errors="replace")
    for cid, code in CHECKLIST_ROW_RE.findall(text):
        tier = TIER_BY_CODE.get(code)
        if tier is None:
            raise ValueError(
                f"checklist.md: control {cid} has unrecognised Level code "
                f"{code!r} (expected one of {sorted(TIER_BY_CODE)})"
            )
        tiers[cid] = tier
    return tiers


def collect_controls(tiers: dict[str, str]) -> list[dict]:
    controls: list[dict] = []
    for pillar_dir_name, pillar_num in PILLAR_DIRS.items():
        pillar_dir = CONTROLS_DIR / pillar_dir_name
        if not pillar_dir.is_dir():
            continue
        for md in sorted(pillar_dir.glob("*.md")):
            if md.name == "index.md":
                continue
            head = _read_head(md)
            cid_match = CONTROL_ID_RE.search(head)
            if not cid_match:
                # Skip files that aren't control specs.
                continue
            cid = cid_match.group(1).strip()
            title_match = TITLE_RE.search(head)
            last_match = LAST_VERIFIED_RE.search(head)
            reg_match = REG_REF_RE.search(head)
            controls.append(
                {
                    "id": cid,
                    "pillar": pillar_num,
                    "tier": tiers.get(cid),
                    "title": title_match.group(1).strip() if title_match else "",
                    "path": _rel(md),
                    "last_verified": last_match.group(1) if last_match else None,
                    "regulatory_references": _split_reg_refs(reg_match.group(1)) if reg_match else [],
                }
            )
    controls.sort(key=lambda c: (c["pillar"], _natural_key(c["id"])))
    return controls


def _natural_key(cid: str) -> tuple:
    parts = re.split(r"[.\-]", cid)
    out = []
    for p in parts:
        out.append((0, int(p)) if p.isdigit() else (1, p))
    return tuple(out)


def collect_playbooks(known_control_ids: set[str]) -> list[dict]:
    playbooks: list[dict] = []

    # Control-implementation playbooks: control_refs derived from parent folder.
    if CONTROL_IMPL_DIR.is_dir():
        for md in sorted(CONTROL_IMPL_DIR.rglob("*.md")):
            rel_parts = md.relative_to(CONTROL_IMPL_DIR).parts
            control_refs: list[str] = []
            if len(rel_parts) >= 2:
                folder = rel_parts[0]
                if folder in known_control_ids:
                    control_refs = [folder]
            playbooks.append(
                {
                    "path": _rel(md),
                    "type": "control-implementation",
                    "control_refs": control_refs,
                }
            )

    # Cross-cutting category playbooks.
    for category in CROSS_CUTTING_CATEGORIES:
        cat_dir = PLAYBOOKS_DIR / category
        if not cat_dir.is_dir():
            continue
        for md in sorted(cat_dir.rglob("*.md")):
            playbooks.append(
                {
                    "path": _rel(md),
                    "type": "cross-cutting",
                    "category": category,
                }
            )

    # Top-level playbooks index page (cross-cutting overview).
    root_index = PLAYBOOKS_DIR / "index.md"
    if root_index.is_file():
        playbooks.append(
            {
                "path": _rel(root_index),
                "type": "cross-cutting",
                "category": "overview",
            }
        )

    playbooks.sort(key=lambda p: p["path"])
    return playbooks


def collect_solutions() -> list[dict]:
    if not SOLUTIONS_LOCK.is_file():
        return []
    data = json.loads(SOLUTIONS_LOCK.read_text(encoding="utf-8"))
    out: list[dict] = []
    for sol in data.get("solutions", []):
        coverage = sol.get("controlCoverage") or sol.get("control_coverage") or []
        out.append(
            {
                "id": sol.get("id", ""),
                "version": sol.get("version", ""),
                "control_coverage": list(coverage),
            }
        )
    out.sort(key=lambda s: s["id"])
    return out


def _tier_breakdowns(controls: list[dict]) -> tuple[dict, dict]:
    """Return ``(by_tier, by_pillar_tier)`` rolled up from per-control tiers.

    Both structures always carry every tier key (zero-filled) so the emitted
    shape is stable regardless of which tiers happen to be populated.
    """
    by_tier = {t: 0 for t in TIER_ORDER}
    by_pillar_tier: dict[str, dict[str, int]] = {}
    for c in controls:
        tier = c["tier"]
        by_tier[tier] += 1
        pk = str(c["pillar"])
        bucket = by_pillar_tier.setdefault(pk, {t: 0 for t in TIER_ORDER})
        bucket[tier] += 1
    by_pillar_tier = {k: by_pillar_tier[k] for k in sorted(by_pillar_tier, key=int)}
    return by_tier, by_pillar_tier


def build_graph() -> dict:
    tiers = collect_control_tiers()
    controls = collect_controls(tiers)

    missing_tier = [c["id"] for c in controls if c["tier"] is None]
    if missing_tier:
        raise ValueError(
            "controls missing a governance tier: "
            f"{missing_tier}. Every control must appear in a per-control table "
            "in docs/getting-started/checklist.md with a B/R/Reg Level code."
        )

    known_ids = {c["id"] for c in controls}
    playbooks = collect_playbooks(known_ids)
    solutions = collect_solutions()

    pillars = sorted({c["pillar"] for c in controls})
    pb_ctrl = sum(1 for p in playbooks if p["type"] == "control-implementation")
    pb_cross = sum(1 for p in playbooks if p["type"] == "cross-cutting")

    by_pillar: dict[str, int] = {}
    for c in controls:
        key = str(c["pillar"])
        by_pillar[key] = by_pillar.get(key, 0) + 1
    by_pillar = {k: by_pillar[k] for k in sorted(by_pillar, key=int)}

    by_tier, by_pillar_tier = _tier_breakdowns(controls)

    return {
        "schemaVersion": SCHEMA_VERSION,
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "counts": {
            "controls": len(controls),
            "pillars": len(pillars),
            "by_pillar": by_pillar,
            "by_tier": by_tier,
            "by_pillar_tier": by_pillar_tier,
            "playbooks_total": len(playbooks),
            "playbooks_control": pb_ctrl,
            "playbooks_cross_cutting": pb_cross,
            "solutions": len(solutions),
        },
        "controls": controls,
        "playbooks": playbooks,
        "solutions": solutions,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify the committed content-graph.json is up to date "
        "(ignoring generatedAt) without rewriting it. Exit 1 if stale.",
    )
    args = parser.parse_args()

    graph = build_graph()

    if args.check:
        if not OUTPUT_PATH.is_file():
            print(
                f"ERROR: {OUTPUT_PATH.relative_to(REPO_ROOT).as_posix()} is missing; "
                "run: python scripts/build_content_graph.py",
                file=sys.stderr,
            )
            return 1
        committed = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        fresh = dict(graph)
        committed_cmp = dict(committed)
        # generatedAt is intentionally non-deterministic; exclude from compare.
        fresh.pop("generatedAt", None)
        committed_cmp.pop("generatedAt", None)
        if fresh != committed_cmp:
            print(
                "Content graph is STALE -- committed content-graph.json does not "
                "match the documentation tree.\n"
                "Fix: python scripts/build_content_graph.py  (then commit the result)",
                file=sys.stderr,
            )
            return 1
        print("Content graph is up to date.")
        return 0

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(graph, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    counts = graph["counts"]
    print(f"Wrote {OUTPUT_PATH.relative_to(REPO_ROOT).as_posix()}")
    print(
        "  controls={controls} pillars={pillars} "
        "playbooks_total={playbooks_total} "
        "(control={playbooks_control}, cross_cutting={playbooks_cross_cutting}) "
        "solutions={solutions}".format(**counts)
    )
    bt = counts["by_tier"]
    print(
        "  by_tier: Baseline={Baseline} Recommended={Recommended} "
        "Regulated={Regulated}".format(**bt)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
