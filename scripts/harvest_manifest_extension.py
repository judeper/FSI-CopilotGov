#!/usr/bin/env python3
"""Harvest the v1.4 SPA-extension fields into the manifest.

Reads ``assessment/manifest/controls.json`` (engine-facing, produced by
``assessment/manifest/generate_manifest.py``) and adds the SPA-facing
extension fields:

* ``name`` — derived from title (strip "Control X.Y: " prefix)
* ``zonesApplicable`` — derived from checks; empty -> [1,2,3]
* ``roles`` — from ROLE_CONTROLS in ``scripts/extract_assessment_data.py``
* ``regulatory`` — parsed from ``**Regulatory Reference:**`` line
  (always re-derived; see ``REDERIVED_FIELDS``)
* ``priority`` — TODO (author judgment)
* ``yesBar`` / ``partialBar`` / ``noBar`` — TODO (author judgment)
* ``verifyIn`` — empty list (per-control authoring)
* ``verifyPowerShell`` — empty string
* ``evidenceExpected`` — empty list
* ``controlDocUrl`` — derived from ``source_file`` slug
* ``portalPlaybookUrl`` — from extract_assessment_data.json playbooks,
  else conventional path
* ``collectorField`` — derived from ``assessment/data/evidence-contract.json``
  (always re-derived; see ``REDERIVED_FIELDS``)
* ``sectorYesBar`` — TODO map for the 6 canonical FSI sectors
* ``facilitatorNotes`` — TODO ask/followUp + 5-minute default budget
* ``solutions`` — empty list (Phase C0/C2 will populate from sister repo)

The harvest is **additive** for author-judgment fields: existing values are
never overwritten. The doc-derived fields listed in ``REDERIVED_FIELDS`` are
the exception — they are refreshed on every run so a corrected control doc
cannot leave stale metadata frozen in the manifest.
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
EVIDENCE_CONTRACT = ROOT / "assessment" / "data" / "evidence-contract.json"

# Regulatory tokens to look for in the **Regulatory Reference:** line.
# Order matters: longer / more-specific phrases first to avoid partial
# overlap (e.g., "OCC Bulletin 2011-12" before "OCC").
REG_TOKENS: list[tuple[str, str]] = [
    # Federal Reserve / OCC interagency.
    #
    # Each bulletin/SR number is matched as its own token so a compound
    # citation such as "SR 26-2 / OCC Bulletin 2026-13" yields BOTH tags.
    # A single compound token would consume the counterpart's span and
    # silently drop it (the pre-#257 behaviour, which lost OCC-2011-12
    # wherever the doc wrote "SR 11-7 / OCC Bulletin 2011-12").
    #
    # SR 26-2 / OCC Bulletin 2026-13 (April 2026) supersede SR 11-7 /
    # OCC Bulletin 2011-12 for traditional models but explicitly exclude
    # generative and agentic AI. Controls that cite both therefore carry
    # both tags: the superseding guidance and the interim principles the
    # control actually applies.
    ("OCC Bulletin 2026-13", "OCC-2026-13"),
    ("OCC Bulletin 2025-26", "OCC-2025-26"),
    ("OCC Bulletin 2023-17", "OCC-2023-17"),
    ("OCC Bulletin 2011-12", "OCC-2011-12"),
    ("SR 26-2", "SR-26-2"),
    ("SR 21-14", "SR-21-14"),
    ("SR 11-7", "SR-11-7"),
    ("12 CFR part 30, appendix D", "OCC-Heightened-Standards"),
    ("OCC Heightened Standards", "OCC-Heightened-Standards"),
    # Interagency guidance (distinct from the OCC/Fed bulletins above)
    ("Interagency Guidance on Third-Party Relationships", "Interagency-TPRM-2023"),
    ("Interagency RFI on AI", "Interagency-AI-RFI-2023"),
    ("Interagency AI Guidance", "Interagency-AI-2023"),
    # FFIEC (longest first to avoid double-matching with bare "FFIEC")
    ("FFIEC IT Examination Handbook", "FFIEC-IT-Handbook"),
    ("FFIEC IT Handbook", "FFIEC-IT-Handbook"),
    ("FFIEC Cybersecurity Assessment Tool", "FFIEC-Cybersecurity"),
    ("FFIEC Cybersecurity", "FFIEC-Cybersecurity"),
    ("FFIEC Business Continuity Management Handbook", "FFIEC-BCM"),
    ("FFIEC Business Continuity", "FFIEC-BCM"),
    ("FFIEC", "FFIEC"),
    # SOX (most specific section first; bare "SOX" is the last resort)
    ("Sarbanes-Oxley §§302/404", "SOX-302-404"),
    ("SOX §§302/404", "SOX-302-404"),
    ("Sarbanes-Oxley 802", "SOX-802"),
    ("SOX 802", "SOX-802"),
    ("Sarbanes-Oxley", "SOX"),
    ("SOX", "SOX"),
    # GLBA
    ("GLBA §501(b)", "GLBA-501b"),
    ("GLBA Safeguards Rule", "GLBA-Safeguards"),
    ("GLBA Title V", "GLBA-Title-V"),
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
    ("FINRA Regulatory Notice 26-14", "FINRA-26-14"),
    ("FINRA Notice 26-14", "FINRA-26-14"),
    # SEC
    ("SEC Release No. 34-105845 / SR-FINRA-2026-004 Partial Amendment No. 1", "SEC-34-105845-SR-FINRA-2026-004"),
    ("SEC Marketing Rule (Rule 206(4)-1)", "SEC-206-4-1"),
    ("SEC Marketing Rule", "SEC-206-4-1"),
    ("Rule 206(4)-1", "SEC-206-4-1"),
    ("Investment Advisers Act Section 206", "IAA-206"),
    ("Investment Advisers Act", "IAA"),
    ("SEC Regulation Best Interest (Reg BI)", "SEC-Reg-BI"),
    ("SEC Regulation Best Interest", "SEC-Reg-BI"),
    ("Reg BI", "SEC-Reg-BI"),
    ("SEC Press Release 2024-36 (Delphia and Global Predictions AI washing enforcement actions)", "SEC-2024-36-AI-Washing"),
    ("SEC Press Release 2024-36", "SEC-2024-36-AI-Washing"),
    ("SEC Rule 17a-4", "SEC-17a-4"),
    ("SEC Rule 17a-3", "SEC-17a-3"),
    ("SEC Rule 10b-5", "SEC-10b-5"),
    ("17a-4", "SEC-17a-4"),
    ("17a-3", "SEC-17a-3"),
    ("10b-5", "SEC-10b-5"),
    ("Reg S-P", "Reg-S-P"),
    ("Regulation S-P", "Reg-S-P"),
    ("SEC Regulation S-ID", "SEC-Reg-S-ID"),
    ("Regulation S-ID", "SEC-Reg-S-ID"),
    # Other
    ("Chinese Wall Requirements", "Chinese-Wall"),
    ("State AI Disclosure Laws", "State-AI-Disclosure"),
    ("CFTC 1.31", "CFTC-1.31"),
    ("NIST AI RMF", "NIST-AI-RMF"),
    ("NIST SP 800-53", "NIST-800-53"),
    ("ISO/IEC 42001", "ISO-42001"),
    ("PCAOB Auditing Standards", "PCAOB-AS-2201"),
    ("AS 2201", "PCAOB-AS-2201"),
    ("Federal Rules of Civil Procedure", "FRCP"),
    ("Equal Credit Opportunity Act", "ECOA"),
    ("ECOA", "ECOA"),
    ("Fair Housing Act", "Fair-Housing-Act"),
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
    "credit-union",
    "other",
)

# Fields that are wholly derived from the control doc or from the evidence
# contract and therefore refreshed on every harvest instead of being preserved
# once written. Everything else in the manifest may carry author judgment and
# is only filled when absent.
REDERIVED_FIELDS = ("regulatory", "collectorField")


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


def load_collector_fields() -> dict[str, str]:
    """Return control id -> collectorField from the evidence contract.

    ``assessment/data/evidence-contract.json`` is the only place that records
    which collector output actually supplies evidence for a control, so it is
    the source of truth for ``collectorField``. Controls with no mapping get
    no entry here and therefore harvest an empty ``collectorField`` — before
    issue #257 twenty controls advertised a collector field that no collector
    emitted.
    """
    if not EVIDENCE_CONTRACT.exists():
        return {}
    try:
        with io.open(EVIDENCE_CONTRACT, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}
    out: dict[str, str] = {}
    for m in data.get("mappings", []) or []:
        cid = m.get("controlId")
        field = m.get("collectorField")
        if cid and field and cid not in out:
            out[cid] = field
    return out


def harvest_one(
    control: dict[str, Any],
    adata_entry: dict[str, Any],
    collector_fields: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Return the fields to ADD, plus any field in :data:`REDERIVED_FIELDS`."""
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

    # regulatory — fully derived from the control doc's
    # ``**Regulatory Reference:**`` line, so it is ALWAYS re-derived rather
    # than preserved. Freezing it (issue #257) let controls keep advertising
    # superseded guidance after the doc citation was corrected — e.g. 3.8 and
    # 3.8a carried only SR-11-7 / OCC-2011-12 long after their docs began
    # citing the superseding SR 26-2 / OCC Bulletin 2026-13. There is no
    # author judgment in this field, so doc truth always wins.
    if doc_text:
        derived_regulatory = parse_regulatory(doc_text)
        if derived_regulatory or "regulatory" not in control:
            extension["regulatory"] = derived_regulatory
    elif "regulatory" not in control:
        extension["regulatory"] = []

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

    # collectorField — derived from the evidence contract (single source of
    # truth for what a collector actually emits), so it is always re-derived.
    extension["collectorField"] = (collector_fields or {}).get(cid, "")

    # sectorYesBar — 6 canonical FSI sectors, all TODO
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

    collector_fields = load_collector_fields()
    if not collector_fields:
        print(
            "WARN: evidence-contract.json missing or empty; collectorField "
            "will be cleared for every control.",
            file=sys.stderr,
        )

    enriched_count = 0
    fields_added = 0
    fields_refreshed = 0
    for ctrl in controls:
        before_keys = set(ctrl.keys())
        ext = harvest_one(ctrl, adata.get(ctrl.get("id"), {}), collector_fields)
        added = {k: v for k, v in ext.items() if k not in before_keys}
        refreshed = {
            k: v
            for k, v in ext.items()
            if k in before_keys and k in REDERIVED_FIELDS and ctrl.get(k) != v
        }
        if added:
            ctrl.update(added)
            enriched_count += 1
            fields_added += len(added)
        if refreshed:
            ctrl.update(refreshed)
            fields_refreshed += len(refreshed)

    MANIFEST.write_text(
        json.dumps(controls, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"Enriched {enriched_count} of {len(controls)} controls "
        f"({fields_added} fields added, {fields_refreshed} derived fields refreshed)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
