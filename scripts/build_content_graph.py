"""Build the canonical content graph for FSI-CopilotGov.

Walks the documentation tree (controls, playbooks) and the solutions lock,
emitting `assessment/manifest/content-graph.json` as a single source of
truth for downstream tooling (manifest generation, drift checks, site
build verification).

Stdlib only -- no external dependencies.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS = REPO_ROOT / "docs"
CONTROLS_DIR = DOCS / "controls"
PLAYBOOKS_DIR = DOCS / "playbooks"
CONTROL_IMPL_DIR = PLAYBOOKS_DIR / "control-implementations"
SOLUTIONS_LOCK = REPO_ROOT / "assessment" / "data" / "solutions-lock.json"
OUTPUT_PATH = REPO_ROOT / "assessment" / "manifest" / "content-graph.json"

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

SCHEMA_VERSION = "1.0.0"

CONTROL_ID_RE = re.compile(r"\*\*Control ID:\*\*\s*([0-9A-Za-z.\-]+)")
PILLAR_RE = re.compile(r"\*\*Pillar:\*\*\s*(.+)")
LAST_VERIFIED_RE = re.compile(r"\*\*Last Verified:\*\*\s*([0-9]{4}-[0-9]{2}-[0-9]{2})")
REG_REF_RE = re.compile(r"\*\*Regulatory Reference:\*\*\s*(.+)")
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


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


def collect_controls() -> list[dict]:
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
            title_match = TITLE_RE.search(head)
            last_match = LAST_VERIFIED_RE.search(head)
            reg_match = REG_REF_RE.search(head)
            controls.append(
                {
                    "id": cid_match.group(1).strip(),
                    "pillar": pillar_num,
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


def build_graph() -> dict:
    controls = collect_controls()
    known_ids = {c["id"] for c in controls}
    playbooks = collect_playbooks(known_ids)
    solutions = collect_solutions()

    pillars = sorted({c["pillar"] for c in controls})
    pb_ctrl = sum(1 for p in playbooks if p["type"] == "control-implementation")
    pb_cross = sum(1 for p in playbooks if p["type"] == "cross-cutting")

    return {
        "schemaVersion": SCHEMA_VERSION,
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "counts": {
            "controls": len(controls),
            "pillars": len(pillars),
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
    graph = build_graph()
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
