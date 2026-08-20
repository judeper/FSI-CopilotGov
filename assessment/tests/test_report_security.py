"""Security regression tests for generated assessment reports."""

from __future__ import annotations

from html import unescape
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ENGINE_DIR = REPO_ROOT / "assessment" / "engine"

sys.path.insert(0, str(ENGINE_DIR))
import report as report_mod  # noqa: E402


HTML_PAYLOAD = '<img src=x onerror="alert(1)">'


def _report_data() -> dict:
    control = {
        "control_id": "1.1",
        "title": f"R&D review — A < B — {HTML_PAYLOAD}",
        "maturity_score": 1,
        "confidence": "high",
        "status": "Partial Gap",
        "evidence_rows": [
            {
                "description": "Evidence URL",
                "icon": "⚠️",
                "result_label": "UNKNOWN",
                "value": f"https://example.test/?a=1&b=2 {HTML_PAYLOAD}",
                "source_label": "test",
                "date": "2026-08-20",
            }
        ],
        "gap": HTML_PAYLOAD,
        "needs_manual": True,
        "manual_question": f"Explain R&D when A < B. {HTML_PAYLOAD}",
        "auto_summary": f"0/1 checks passed {HTML_PAYLOAD}",
    }
    return {
        "customer": f"Contoso R&D {HTML_PAYLOAD}",
        "date": "2026-08-20",
        "zone": 2,
        "zone_description": "Team / Medium Risk",
        "total_controls": 1,
        "auto_scored": 0,
        "needs_manual": 1,
        "average_maturity": 1.0,
        "pillars": {
            "1": {
                "name": f"Readiness {HTML_PAYLOAD}",
                "controls": [control],
                "manual_controls": [control],
            }
        },
        "summary": {"total_controls": 1},
    }


def test_markdown_reports_escape_dynamic_html_without_double_escaping() -> None:
    data = _report_data()
    prefilled = report_mod.generate_prefilled_md(data)
    questionnaire = report_mod.generate_questionnaire_md(data)

    for output in (prefilled, questionnaire):
        assert "<img" not in output.lower()
        assert "&lt;img" in output
        assert "R&amp;D" in output
        assert "R&amp;amp;D" not in output

        rendered_text = unescape(output)
        assert "R&D" in rendered_text
        assert "A < B" in rendered_text

    assert "https://example.test/?a=1&amp;b=2" in prefilled
    assert "https://example.test/?a=1&b=2" in unescape(prefilled)


def test_json_summary_preserves_original_plain_text_values() -> None:
    data = _report_data()

    summary = report_mod.generate_summary_json(
        data,
        ["assessment-prefilled.md", "manual-questionnaire.md"],
    )

    assert summary["customer_name"] == f"Contoso R&D {HTML_PAYLOAD}"
