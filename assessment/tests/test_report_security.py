"""Security regression tests for generated assessment reports."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import sys

import markdown

REPO_ROOT = Path(__file__).resolve().parents[2]
ENGINE_DIR = REPO_ROOT / "assessment" / "engine"

sys.path.insert(0, str(ENGINE_DIR))
import report as report_mod  # noqa: E402


HTML_PAYLOAD = '<img src=x onerror="alert(1)">'
MARKDOWN_PAYLOAD = (
    "first | forged\r\n"
    "| row | ![pixel](data:image/svg+xml,boom) "
    "[run](javascript:alert(1)) [vb](vbscript:msgbox(1)) "
    "<script>alert(1)</script>\u2028"
    "# heading > quote --- [reference][target]\n"
    "[target]: https://evil.example/"
)


class _RenderedHtml(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[str] = []
        self.attributes: list[tuple[str, str | None]] = []
        self.text: list[str] = []

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        self.tags.append(tag)
        self.attributes.extend(attrs)

    def handle_data(self, data: str) -> None:
        self.text.append(data)


def _report_data(dynamic_text: str = HTML_PAYLOAD) -> dict:
    control = {
        "control_id": dynamic_text,
        "title": dynamic_text,
        "maturity_score": 1,
        "confidence": dynamic_text,
        "status": dynamic_text,
        "evidence_rows": [
            {
                "description": dynamic_text,
                "icon": dynamic_text,
                "result_label": dynamic_text,
                "value": dynamic_text,
                "source_label": dynamic_text,
                "date": dynamic_text,
            }
        ],
        "gap": dynamic_text,
        "needs_manual": True,
        "manual_question": dynamic_text,
        "auto_summary": dynamic_text,
    }
    return {
        "customer": dynamic_text,
        "date": dynamic_text,
        "zone": 2,
        "zone_description": dynamic_text,
        "total_controls": 1,
        "auto_scored": 0,
        "needs_manual": 1,
        "average_maturity": 1.0,
        "pillars": {
            dynamic_text: {
                "name": dynamic_text,
                "controls": [control],
                "manual_controls": [control],
            }
        },
        "summary": {"total_controls": 1},
    }


def _render_html(markdown_text: str) -> tuple[str, _RenderedHtml]:
    rendered = markdown.markdown(markdown_text, extensions=["tables"])
    parsed = _RenderedHtml()
    parsed.feed(rendered)
    return rendered, parsed


def test_markdown_reports_preserve_plain_text_after_rendering() -> None:
    plain_text = "Contoso R&D — A < B — https://example.test/?a=1&b=2"
    data = _report_data(plain_text)

    for output in (
        report_mod.generate_prefilled_md(data),
        report_mod.generate_questionnaire_md(data),
    ):
        _, parsed = _render_html(output)
        assert plain_text in "".join(parsed.text)


def test_rendered_reports_block_markdown_and_html_injection() -> None:
    data = _report_data(MARKDOWN_PAYLOAD)
    prefilled_html, prefilled = _render_html(
        report_mod.generate_prefilled_md(data)
    )
    questionnaire_html, questionnaire = _render_html(
        report_mod.generate_questionnaire_md(data)
    )

    for rendered, parsed in (
        (prefilled_html, prefilled),
        (questionnaire_html, questionnaire),
    ):
        assert not {"a", "img", "script"}.intersection(parsed.tags)
        assert not any(
            name in {"href", "src"} for name, _value in parsed.attributes
        )
        assert "javascript:" in "".join(parsed.text)
        assert "data:image" in "".join(parsed.text)
        assert "vbscript:" in "".join(parsed.text)
        assert "<script>" not in rendered.lower()

    # One header row and one evidence row: injected pipes/newlines cannot add rows.
    assert prefilled.tags.count("tr") == 2
    assert prefilled.tags.count("h1") == 1
    assert prefilled.tags.count("h2") == 1
    assert prefilled.tags.count("h3") == 1
    assert questionnaire.tags.count("h1") == 1
    assert questionnaire.tags.count("h2") == 1


def test_markdown_plain_text_sanitizer_collapses_line_breaks_and_escapes_syntax() -> None:
    sanitized = report_mod._markdown_plain_text(MARKDOWN_PAYLOAD)

    assert isinstance(sanitized, str)
    assert not any(char in sanitized for char in "\r\n\t\u2028")
    assert r"\|" in sanitized
    assert r"\[" in sanitized
    assert r"\]" in sanitized
    assert r"\(" in sanitized
    assert r"\)" in sanitized
    assert r"\!" in sanitized
    assert r"\#" in sanitized


def test_json_summary_preserves_original_plain_text_values() -> None:
    data = _report_data(MARKDOWN_PAYLOAD)

    summary = report_mod.generate_summary_json(
        data,
        ["assessment-prefilled.md", "manual-questionnaire.md"],
    )

    assert summary["customer_name"] == MARKDOWN_PAYLOAD
