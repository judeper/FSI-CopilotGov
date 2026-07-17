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
