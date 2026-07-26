from __future__ import annotations

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "verify_tuning_claims.py"

_spec = importlib.util.spec_from_file_location("verify_tuning_claims", SCRIPT)
verify_tuning_claims = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(verify_tuning_claims)


# ---------------------------------------------------------------------------
# Quantitative-violation tests
# ---------------------------------------------------------------------------

def test_flags_fabricated_document_threshold_K_suffix() -> None:
    text = "scenario-specific data snapshot minimums (typically 100K+ indexable documents or items)"
    violations = verify_tuning_claims.find_quantitative_violations(text)
    assert len(violations) == 1
    assert "100K" in violations[0][1]


def test_flags_fabricated_document_threshold_comma_form() -> None:
    text = "requires at least 100,000 documents in the tuning corpus"
    violations = verify_tuning_claims.find_quantitative_violations(text)
    assert len(violations) == 1


def test_flags_bare_number_document_threshold() -> None:
    """Bare integer ≥ 5 digits (no comma grouping, no K/M suffix) must be caught."""
    text = "requires 100000 indexable documents in the corpus"
    violations = verify_tuning_claims.find_quantitative_violations(text)
    assert len(violations) == 1, f"bare-number bypass not closed: {violations}"


def test_flags_m_suffix_document_threshold() -> None:
    """M-suffix magnitudes (e.g. 1M+) must be caught."""
    text = "tuning requires 1M+ indexable files to be effective"
    violations = verify_tuning_claims.find_quantitative_violations(text)
    assert len(violations) == 1, f"M-suffix bypass not closed: {violations}"


def test_closes_line_global_allowed_noun_bypass() -> None:
    """An allowed noun elsewhere on the line must NOT suppress a distant violation.

    Previous logic applied the allowed-noun exemption globally to the entire
    line, so appending '5,000 licenses' to any bad claim would silence it.
    The fix checks proximity per magnitude match.
    """
    text = "100K+ indexable documents in the tuning corpus (tenant needs 5,000 licenses)"
    violations = verify_tuning_claims.find_quantitative_violations(text)
    assert len(violations) == 1, (
        f"line-global suppression bypass not closed; got {violations}"
    )


def test_allowed_noun_proximate_to_magnitude_exempts_it() -> None:
    """A magnitude immediately adjacent to an allowed noun is still exempt."""
    text = "only tenants with at least 5,000 Microsoft 365 Copilot licenses are eligible"
    assert verify_tuning_claims.find_quantitative_violations(text) == []


def test_allows_license_threshold() -> None:
    text = "only tenants with at least 5,000 Microsoft 365 Copilot licenses are eligible"
    assert verify_tuning_claims.find_quantitative_violations(text) == []


def test_allows_small_example_set_minimum() -> None:
    text = "provide at least 20 high-quality example files, each at least one page long"
    assert verify_tuning_claims.find_quantitative_violations(text) == []


# ---------------------------------------------------------------------------
# Terminology-violation tests
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Required-target-file tests
# ---------------------------------------------------------------------------

def test_required_files_present_in_live_tree() -> None:
    """The mandatory control file must exist in the live repository."""
    assert verify_tuning_claims.check_required_files() == []


def test_missing_required_file_reported() -> None:
    """Passing a non-existent root triggers a missing-file report."""
    missing = verify_tuning_claims.check_required_files(root="C:/nonexistent/fake-root-12345")
    assert len(missing) > 0
    assert any("1.16" in f for f in missing)


# ---------------------------------------------------------------------------
# Live-tree integration tests
# ---------------------------------------------------------------------------

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
