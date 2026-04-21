#!/usr/bin/env python3
"""Harvest the v1.4 SPA-extension fields into the manifest.

Reads ``assessment/manifest/controls.json`` (engine-facing, produced by
``assessment/manifest/generate_manifest.py``) and adds the SPA-facing
extension fields:

* ``name`` — derived from title (strip "Control X.Y: " prefix)
* ``zonesApplicable`` — derived from checks; empty -> [1,2,3]
* ``roles`` — from ROLE_CONTROLS in ``scripts/extract_assessment_data.py``
* ``regulatory`` — parsed from ``**Regulatory Reference:**`` line
* ``priority`` — TODO (author judgment)
* ``yesBar`` / ``partialBar`` / ``noBar`` — TODO (author judgment)
* ``verifyIn`` — empty list (per-control authoring)
* ``verifyPowerShell`` — empty string
* ``evidenceExpected`` — empty list
* ``controlDocUrl`` — derived from ``source_file`` slug
* ``portalPlaybookUrl`` — from extract_assessment_data.json playbooks,
  else conventional path
* ``collectorField`` — empty (engine-aware authoring)
* ``sectorYesBar`` — TODO map for the 8 canonical FSI sectors
* ``facilitatorNotes`` — TODO ask/followUp + 5-minute default budget
* ``solutions`` — empty list (Phase C0/C2 will populate from sister repo)

The harvest is **additive**: existing values are never overwritten.
Re-running this script after authoring is safe.

Run from the repo root::

    python scripts/harvest_manifest_extension.py
"""
from __future__ import annotations

import io
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "assessment" / "manifest" / "controls.json"
ASSESSMENT_DATA = ROOT / "docs" / "javascripts" / "assessment-data.json"

# Regulatory tokens to look for in the **Regulatory Reference:** line.
# Order matters: longer / more-specific phrases first to avoid partial
# overlap (e.g., "OCC Bulletin 2011-12" before "OCC").
REG_TOKENS: list[tuple[str, str]] = [
    # Federal Reserve / OCC interagency (longer first)
    ("SR 11-7 / OCC Bulletin 2011-12", "SR-11-7"),
    ("OCC Bulletin 2011-12", "OCC-2011-12"),
    ("OCC Bulletin 2023-17", "OCC-2023-17"),
    ("SR 11-7", "SR-11-7"),
    ("12 CFR part 30, appendix D", "OCC-Heightened-Standards"),
    ("OCC Heightened Standards", "OCC-Heightened-Standards"),
    # FFIEC (longest first to avoid double-matching with bare "FFIEC")
    ("FFIEC IT Examination Handbook", "FFIEC-IT-Handbook"),
    ("FFIEC IT Handbook", "FFIEC-IT-Handbook"),
    ("FFIEC Cybersecurity Assessment Tool", "FFIEC-Cybersecurity"),
    ("FFIEC Cybersecurity", "FFIEC-Cybersecurity"),
    ("FFIEC Business Continuity Management Handbook", "FFIEC-BCM"),
    ("FFIEC Business Continuity", "FFIEC-BCM"),
    ("FFIEC", "FFIEC"),
    # SOX
    ("Sarbanes-Oxley §§302/404", "SOX-302-404"),
    ("Sarbanes-Oxley", "SOX"),
    ("SOX §§302/404", "SOX-302-404"),
    ("SOX", "SOX"),
    # GLBA
    ("GLBA §501(b)", "GLBA-501b"),
    ("GLBA Safeguards Rule", "GLBA-Safeguards"),
    ("GLBA", "GLBA"),
    # FINRA — both "Rule N" and bare "N" forms
    ("FINRA Rule 4511", "FINRA-4511"),
    ("FINRA Rule 4530", "FINRA-4530"),
    ("FINRA Rule 4370", "FINRA-4370"),
    ("FINRA Rule 3110", "FINRA-3110"),
    ("FINRA Rule 3120", "FINRA-3120"),
    ("FINRA Rule 2210", "FINRA-2210"),
    ("FINRA Rule 5280", "FINRA-5280"),
    ("FINRA 4511", "FINRA-4511"),
    ("FINRA 4530", "FINRA-4530"),
    ("FINRA 4370", "FINRA-4370"),
    ("FINRA 3110", "FINRA-3110"),
    ("FINRA 3120", "FINRA-3120"),
    ("FINRA 2210", "FINRA-2210"),
    ("FINRA 5280", "FINRA-5280"),
    ("FINRA Regulatory Notice 24-09", "FINRA-24-09"),
    ("FINRA Notice 24-09", "FINRA-24-09"),
    ("FINRA Regulatory Notice 25-07", "FINRA-25-07"),
    ("FINRA Notice 25-07", "FINRA-25-07"),
    # SEC
    ("SEC Marketing Rule (Rule 206(4)-1)", "SEC-206-4-1"),
    ("SEC Marketing Rule", "SEC-206-4-1"),
    ("Rule 206(4)-1", "SEC-206-4-1"),
    ("Investment Advisers Act Section 206", "IAA-206"),
    ("Investment Advisers Act", "IAA"),
    ("SEC Regulation Best Interest (Reg BI)", "SEC-Reg-BI"),
    ("SEC Regulation Best Interest", "SEC-Reg-BI"),
    ("Reg BI", "SEC-Reg-BI"),
    ("SEC Risk Alerts on AI Marketing Claims", "SEC-AI-Marketing-Risk-Alert"),
    ("SEC Rule 17a-4", "SEC-17a-4"),
    ("SEC Rule 17a-3", "SEC-17a-3"),
    ("SEC Rule 10b-5", "SEC-10b-5"),
    ("17a-4", "SEC-17a-4"),
    ("17a-3", "SEC-17a-3"),
    ("10b-5", "SEC-10b-5"),
    ("Reg S-P", "Reg-S-P"),
    ("Regulation S-P", "Reg-S-P"),
    # Other
    ("Chinese Wall Requirements", "Chinese-Wall"),
    ("State AI Disclosure Laws", "State-AI-Disclosure"),
    ("CFTC 1.31", "CFTC-1.31"),
    ("NIST AI RMF", "NIST-AI-RMF"),
    ("NYDFS Part 500", "NYDFS-500"),
    ("NYDFS", "NYDFS-500"),
    ("HIPAA", "HIPAA"),
    ("PCI DSS", "PCI-DSS"),
    ("PCI", "PCI-DSS"),
    ("NCUA", "NCUA"),
    ("CFPB", "CFPB"),
    ("EU AI Act", "EU-AI-Act"),
]

# Canonical FSI sectors used in sectorYesBar.
SECTORS = (
    "bank",
    "broker-dealer",
    "investment-adviser",
    "insurance-carrier",
    "insurance-wholesale",
    "credit-union",
    "holding-company",
    "other",
)


def slug_from_source_file(source_file: str) -> str:
    return Path(source_file).stem if source_file else ""


def control_doc_url(source_file: str) -> str:
    """Derive site-root URL for the control doc (kebab-case slug)."""
    if not source_file:
        return "/"
    parts = source_file.split("/")
    # docs/controls/<pillar>/<file>.md -> /controls/<pillar>/<slug>/
    if len(parts) >= 4 and parts[0] == "docs" and parts[1] == "controls":
        return f"/controls/{parts[2]}/{Path(parts[-1]).stem}/"
    return f"/controls/{Path(source_file).stem}/"


def parse_regulatory(doc_text: str) -> list[str]:
    m = re.search(
        r"^\*\*Regulatory Reference:\*\*\s*(.+?)$",
        doc_text,
        re.MULTILINE,
    )
    if not m:
        return []
    line = m.group(1)
    # Match-and-consume so a longer token (e.g. "FFIEC IT Handbook") prevents
    # a shorter alias (e.g. bare "FFIEC") from double-matching the same span.
    working = line
    found: list[str] = []
    for token, tag in REG_TOKENS:
        idx = working.lower().find(token.lower())
        if idx >= 0:
            if tag not in found:
                found.append(tag)
            # Blank out the matched span (preserve length to keep indices stable).
            working = working[:idx] + (" " * len(token)) + working[idx + len(token):]
    return found


def derive_zones(checks: list[dict]) -> list[int]:
    zones: set[int] = set()
    for c in checks or []:
        for z in c.get("zone_required", []) or []:
            if isinstance(z, int) and z in (1, 2, 3):
                zones.add(z)
    return sorted(zones) if zones else [1, 2, 3]


def name_from_title(title: str, control_id: str) -> str:
    m = re.match(rf"^Control\s+{re.escape(control_id)}\s*:\s*(.+)$", title)
    return m.group(1).strip() if m else (title or "")


def load_assessment_data() -> dict[str, dict]:
    """Return id -> assessment-data.json control entry (empty if missing)."""
    if not ASSESSMENT_DATA.exists():
        return {}
    try:
        with io.open(ASSESSMENT_DATA, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}
    out: dict[str, dict] = {}
    for c in data.get("controls", []) or []:
        cid = c.get("id")
        if cid:
            out[cid] = c
    return out


def harvest_one(control: dict[str, Any], adata_entry: dict[str, Any]) -> dict[str, Any]:
    """Return only the fields to ADD (not present in `control` already)."""
    cid = control["id"]
    src = control.get("source_file", "")
    doc_text = ""
    doc_path = ROOT / src if src else None
    if doc_path and doc_path.exists():
        try:
            doc_text = doc_path.read_text(encoding="utf-8")
        except OSError:
            doc_text = ""

    extension: dict[str, Any] = {}

    # name (deterministic)
    if "name" not in control:
        extension["name"] = name_from_title(control.get("title", ""), cid)

    # zonesApplicable (derived from checks)
    if "zonesApplicable" not in control:
        extension["zonesApplicable"] = derive_zones(control.get("checks", []))

    # roles (from extract_assessment_data ROLE_CONTROLS map)
    if "roles" not in control:
        roles = list(adata_entry.get("assignedRoles") or [])
        extension["roles"] = roles or ["TODO: assign per ROLE_CONTROLS"]

    # regulatory (parsed from MD)
    if "regulatory" not in control:
        extension["regulatory"] = parse_regulatory(doc_text)

    # priority — author judgment
    if "priority" not in control:
        extension["priority"] = "TODO: critical|high|medium|low"

    # rating bars — author judgment
    for key, hint in (
        ("yesBar", "concise pass criteria"),
        ("partialBar", "partial coverage criteria"),
        ("noBar", "fail criteria"),
    ):
        if key not in control:
            extension[key] = f"TODO: {hint}"

    # verifyIn — empty list (per-control authoring)
    if "verifyIn" not in control:
        extension["verifyIn"] = []

    # verifyPowerShell — empty default
    if "verifyPowerShell" not in control:
        extension["verifyPowerShell"] = ""

    # evidenceExpected — empty default
    if "evidenceExpected" not in control:
        extension["evidenceExpected"] = []

    # controlDocUrl
    if "controlDocUrl" not in control:
        extension["controlDocUrl"] = control_doc_url(src)

    # portalPlaybookUrl — prefer the URL from extract_assessment_data
    if "portalPlaybookUrl" not in control:
        playbooks = adata_entry.get("playbooks") or {}
        url = playbooks.get("portalWalkthrough")
        if url and not url.startswith("/"):
            url = "/" + url.lstrip("/")
        extension["portalPlaybookUrl"] = url or f"/playbooks/control-implementations/{cid}/portal-walkthrough/"

    # collectorField — engine-aware authoring
    if "collectorField" not in control:
        extension["collectorField"] = ""

    # sectorYesBar — 8 canonical FSI sectors, all TODO
    if "sectorYesBar" not in control:
        extension["sectorYesBar"] = {
            sector: "TODO: sector-specific yes-bar" for sector in SECTORS
        }

    # facilitatorNotes
    if "facilitatorNotes" not in control:
        extension["facilitatorNotes"] = {
            "ask": "TODO: facilitator question",
            "followUp": "TODO: follow-up hint",
            "timeBudgetMinutes": 5,
        }

    # solutions — kebab-case folder ids, populated by Phase C
    if "solutions" not in control:
        extension["solutions"] = []

    return extension


def main() -> int:
    if not MANIFEST.exists():
        print(f"ERROR: manifest not found at {MANIFEST}", file=sys.stderr)
        return 2
    controls = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if not isinstance(controls, list):
        print("ERROR: manifest is not a JSON list", file=sys.stderr)
        return 2

    adata = load_assessment_data()
    if not adata:
        print(
            "WARN: assessment-data.json missing or empty; roles/playbooks "
            "will be TODO. Run scripts/extract_assessment_data.py first.",
            file=sys.stderr,
        )

    enriched_count = 0
    fields_added = 0
    for ctrl in controls:
        before_keys = set(ctrl.keys())
        ext = harvest_one(ctrl, adata.get(ctrl.get("id"), {}))
        added = {k: v for k, v in ext.items() if k not in before_keys}
        if added:
            ctrl.update(added)
            enriched_count += 1
            fields_added += len(added)

    MANIFEST.write_text(
        json.dumps(controls, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"Enriched {enriched_count} of {len(controls)} controls "
        f"({fields_added} fields added)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
