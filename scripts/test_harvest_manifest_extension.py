from __future__ import annotations

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "harvest_manifest_extension.py"

_spec = importlib.util.spec_from_file_location("harvest_manifest_extension", SCRIPT)
harvest_manifest_extension = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(harvest_manifest_extension)


def test_parse_regulatory_maps_finra_partial_amendment_authoritative_release() -> None:
    doc_text = (
        "**Regulatory Reference:** FINRA Rule 2210, "
        "SEC Release No. 34-105845 / SR-FINRA-2026-004 Partial Amendment No. 1, "
        "SEC Marketing Rule (Rule 206(4)-1)"
    )
    tags = harvest_manifest_extension.parse_regulatory(doc_text)
    assert "SEC-34-105845-SR-FINRA-2026-004" in tags


def test_parse_regulatory_maps_ai_washing_press_release_not_risk_alert_label() -> None:
    doc_text = (
        "**Regulatory Reference:** SEC Marketing Rule (Rule 206(4)-1), "
        "SEC Press Release 2024-36 (Delphia and Global Predictions AI washing enforcement actions)"
    )
    tags = harvest_manifest_extension.parse_regulatory(doc_text)
    assert "SEC-2024-36-AI-Washing" in tags
    assert "SEC-AI-Marketing-Risk-Alert" not in tags


def test_parse_regulatory_pairs_sr_11_7_with_its_occ_counterpart() -> None:
    """A compound "SR 11-7 / OCC Bulletin 2011-12" citation yields both tags.

    The single compound token used before issue #257 consumed the OCC span and
    silently dropped ``OCC-2011-12``.
    """
    doc_text = (
        "**Regulatory Reference:** GLBA \u00a7501(b), "
        "SR 11-7 / OCC Bulletin 2011-12 (interim principles)"
    )
    tags = harvest_manifest_extension.parse_regulatory(doc_text)
    assert "SR-11-7" in tags
    assert "OCC-2011-12" in tags


def test_parse_regulatory_tags_superseding_model_risk_guidance() -> None:
    """Model-risk controls must not advertise superseded guidance alone."""
    doc_text = (
        "**Regulatory Reference:** SR 26-2 / OCC Bulletin 2026-13 (Revised "
        "Guidance on Model Risk Management, April 2026 \u2014 supersedes SR 11-7 / "
        "OCC Bulletin 2011-12 but explicitly excludes generative and agentic AI), "
        "OCC Bulletin 2025-26 (Model Risk Management \u2014 Community Bank "
        "Proportionality)"
    )
    tags = harvest_manifest_extension.parse_regulatory(doc_text)
    for expected in ("SR-26-2", "OCC-2026-13", "OCC-2025-26", "SR-11-7", "OCC-2011-12"):
        assert expected in tags, f"{expected} missing from {tags}"


def test_parse_regulatory_prefers_specific_sox_and_glba_sections() -> None:
    doc_text = (
        "**Regulatory Reference:** SOX 802 (Criminal Penalties for Altering "
        "Documents), GLBA Title V (Privacy), SEC Regulation S-ID (Identity "
        "Theft Red Flags)"
    )
    tags = harvest_manifest_extension.parse_regulatory(doc_text)
    assert "SOX-802" in tags
    assert "SOX" not in tags
    assert "GLBA-Title-V" in tags
    assert "GLBA" not in tags
    assert "SEC-Reg-S-ID" in tags


def test_regulatory_and_collector_field_are_rederived() -> None:
    """Derived fields must refresh, not stay frozen at their first value."""
    assert set(harvest_manifest_extension.REDERIVED_FIELDS) == {
        "regulatory",
        "collectorField",
    }


def test_harvest_one_derives_collector_field_from_contract() -> None:
    control = {
        "id": "9.9",
        "title": "Control 9.9: Example",
        "source_file": "",
        "collectorField": "Legacy_OrphanField",
    }
    ext = harvest_manifest_extension.harvest_one(control, {}, {"9.9": "Purview_Real"})
    assert ext["collectorField"] == "Purview_Real"

    ext_unmapped = harvest_manifest_extension.harvest_one(control, {}, {})
    assert ext_unmapped["collectorField"] == ""


def test_load_collector_fields_matches_repo_contract() -> None:
    fields = harvest_manifest_extension.load_collector_fields()
    assert fields, "evidence-contract.json should provide collector fields"
    assert fields.get("4.11") == "Sentinel_CopilotActivityCollection"
