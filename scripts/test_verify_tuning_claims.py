from __future__ import annotations

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "verify_tuning_claims.py"

_spec = importlib.util.spec_from_file_location("verify_tuning_claims", SCRIPT)
verify_tuning_claims = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(verify_tuning_claims)


def test_flags_fabricated_document_threshold_K_suffix() -> None:
    text = "scenario-specific data snapshot minimums (typically 100K+ indexable documents or items)"
    violations = verify_tuning_claims.find_quantitative_violations(text)
    assert len(violations) == 1
    assert "100K" in violations[0][1]


def test_flags_fabricated_document_threshold_comma_form() -> None:
    text = "requires at least 100,000 documents in the tuning corpus"
    violations = verify_tuning_claims.find_quantitative_violations(text)
    assert len(violations) == 1


def test_allows_license_threshold() -> None:
    text = "only tenants with at least 5,000 Microsoft 365 Copilot licenses are eligible"
    assert verify_tuning_claims.find_quantitative_violations(text) == []


def test_allows_small_example_set_minimum() -> None:
    text = "provide at least 20 high-quality example files, each at least one page long"
    assert verify_tuning_claims.find_quantitative_violations(text) == []


def test_flags_public_preview_terminology() -> None:
    text = "During public preview, snapshot data is retained while the agent is active."
    violations = verify_tuning_claims.find_terminology_violations(text)
    assert len(violations) == 1


def test_flags_public_preview_hyphenated() -> None:
    text = "public-preview license thresholds where applicable"
    assert len(verify_tuning_claims.find_terminology_violations(text)) == 1


def test_allows_early_access_preview_terminology() -> None:
    text = "During the early access preview (delivered via Frontier), snapshots are retained."
    assert verify_tuning_claims.find_terminology_violations(text) == []


def test_live_control_file_is_clean() -> None:
    control = (
        REPO_ROOT
        / "docs"
        / "controls"
        / "pillar-1-readiness"
        / "1.16-copilot-tuning-governance.md"
    )
    text = control.read_text(encoding="utf-8")
    assert verify_tuning_claims.find_quantitative_violations(text) == []
    assert verify_tuning_claims.find_terminology_violations(text) == []


def test_main_passes_on_current_tree() -> None:
    assert verify_tuning_claims.main() == 0
