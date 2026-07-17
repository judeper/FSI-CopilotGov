from __future__ import annotations

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "verify_regulatory_citations.py"

_spec = importlib.util.spec_from_file_location("verify_regulatory_citations", SCRIPT)
verify_regulatory_citations = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(verify_regulatory_citations)


def test_finra_partial_amendment_pairing_accepts_authoritative_release() -> None:
    content = (
        "SEC Release No. 34-105845 / SR-FINRA-2026-004 Partial Amendment No. 1 "
        "(Federal Register document 2026-13713)"
    )
    assert verify_regulatory_citations.check_finra_partial_amendment_pairing(content) == []


def test_finra_partial_amendment_pairing_rejects_stale_release_number() -> None:
    content = (
        "SEC Release No. 34-103492 / SR-FINRA-2026-004 Partial Amendment No. 1 "
        "(Federal Register document 2026-13713)"
    )
    errors = verify_regulatory_citations.check_finra_partial_amendment_pairing(content)
    assert any("34-103492" in err for err in errors)


def test_finra_partial_amendment_pairing_requires_release_with_fr_doc() -> None:
    content = "Federal Register document 2026-13713 for SR-FINRA-2026-004"
    errors = verify_regulatory_citations.check_finra_partial_amendment_pairing(content)
    assert any("2026-13713 appears without SEC Release 34-105845" in err for err in errors)


def test_find_mislabeled_risk_alert_links_flags_generic_division_pages() -> None:
    markdown = (
        "[SEC Risk Alert on AI Marketing Claims]"
        "(https://www.sec.gov/about/divisions-offices/division-examinations)"
    )
    violations = verify_regulatory_citations.find_mislabeled_risk_alert_links(markdown)
    assert violations == [
        (
            "SEC Risk Alert on AI Marketing Claims",
            "https://www.sec.gov/about/divisions-offices/division-examinations",
        )
    ]


def test_find_mislabeled_risk_alert_links_allows_specific_risk_alert_urls() -> None:
    markdown = (
        "[Division of Examinations Risk Alert]"
        "(https://www.sec.gov/files/exams-risk-alert-marketing-rule.pdf)"
    )
    violations = verify_regulatory_citations.find_mislabeled_risk_alert_links(markdown)
    assert violations == []
