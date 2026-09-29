"""Regression tests for Learn classification noise filtering."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent
FIXTURES_DIR = SCRIPTS_DIR / "fixtures" / "learn_monitor"
sys.path.insert(0, str(SCRIPTS_DIR))

import monitoring_shared  # noqa: E402


def _fixture(name: str) -> str:
    return (FIXTURES_DIR / name).read_text(encoding="utf-8")


@pytest.mark.parametrize(
    "phrase",
    [
        "This connector is deprecated.",
        "This connector will be retired next quarter.",
        "This connector is no longer supported.",
        "This connector has been removed.",
        "This connector is being deprecated.",
        "This connector is no longer available.",
        "This connector will be removed next quarter.",
        "This connector is being retired.",
        "Legacy connector will no longer be supported after June 2026.",
        "Microsoft will no longer support this API.",
        "This setting is no longer applicable.",
        "Feature is no longer in preview.",
        "Users are no longer able to configure this option.",
        "Option is no longer visible in the admin center.",
    ],
)
def test_deprecation_language_stays_critical_by_default(phrase: str):
    old = "This connector is available."
    new = phrase

    classification, reason, _ = monitoring_shared.classify_change(old, new)

    assert classification == monitoring_shared.CLASSIFICATION_CRITICAL
    assert reason == "Deprecation notice"


@pytest.mark.parametrize(
    "phrase",
    [
        "and remove connections when they're no longer needed.",
        "Delete the connector when you no longer need to collect these logs.",
    ],
)
def test_known_benign_no_longer_phrases_are_not_deprecation(phrase: str):
    old = "Connector operations are documented."
    new = f"Connector operations are documented.\n{phrase}"

    classification, reason, diff_text = monitoring_shared.classify_change(old, new)

    assert phrase in diff_text
    assert (classification, reason) != (
        monitoring_shared.CLASSIFICATION_CRITICAL,
        "Deprecation notice",
    )


def test_learn_command_bar_churn_is_noise():
    old = "\n".join(
        [
            "Table of contents",
            "Read in English",
            "Add to plan",
            "Copy Markdown",
            "Print",
        ]
    )
    new = "\n".join(
        [
            "Table of contents",
            "Read in English",
            "Add to Plans",
            "Copy Markdown",
            "Print",
        ]
    )

    classification, _, _ = monitoring_shared.classify_change(old, new)
    assert classification == monitoring_shared.CLASSIFICATION_NOISE


def test_preview_and_ga_terms_remain_high_signal():
    old = "Feature status: preview"
    new = "Feature status: generally available (GA)"

    classification, reason, _ = monitoring_shared.classify_change(old, new)
    assert classification == monitoring_shared.CLASSIFICATION_HIGH
    assert reason == "Feature availability"


def test_authorization_interstitial_noise_beats_deprecation_regex():
    config = monitoring_shared.load_monitoring_config()
    snapshot = monitoring_shared.extract_learn_content_snapshot(
        "https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms",
        _fixture("learn-auth-note-only.html"),
        config,
    )

    assert snapshot.page_shape == "Authorization interstitial"


def test_real_deprecation_notice_remains_critical():
    old = "This connector is available."
    new = "This connector is deprecated and will be removed next quarter."

    classification, reason, _ = monitoring_shared.classify_change(old, new)

    assert classification == monitoring_shared.CLASSIFICATION_CRITICAL
    assert reason == "Deprecation notice"


def test_real_article_fixture_with_hidden_auth_banner_is_not_page_shape_noise():
    config = monitoring_shared.load_monitoring_config()

    snapshot = monitoring_shared.extract_learn_content_snapshot(
        "https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms",
        _fixture("connected-platforms-main.html"),
        config,
    )

    assert snapshot.page_shape is None
    assert "Access to this page requires authorization" not in snapshot.normalized_content
    assert "Connected platforms in Microsoft Agent 365" in snapshot.normalized_content


def test_real_authorization_article_is_not_misclassified_as_interstitial():
    config = monitoring_shared.load_monitoring_config()

    snapshot = monitoring_shared.extract_learn_content_snapshot(
        "https://learn.microsoft.com/en-us/rest/api/authorization/",
        _fixture("authorization-rest-main.html"),
        config,
    )

    assert snapshot.page_shape is None
    assert "Authorization" in snapshot.normalized_content


def test_stored_baseline_samples_do_not_false_positive_on_auth_banner():
    config = monitoring_shared.load_monitoring_config()
    fixtures = sorted(FIXTURES_DIR.glob("baseline-*.txt"))
    assert fixtures, "expected trimmed baseline fixtures"

    flagged = [
        fixture.name
        for fixture in fixtures
        if monitoring_shared.detect_learn_page_shape(
            fixture.read_text(encoding="utf-8"),
            config,
        )
    ]

    assert flagged == []


def test_no_longer_needed_article_line_is_not_treated_as_deprecation():
    config = monitoring_shared.load_monitoring_config()
    full = monitoring_shared.extract_learn_content_snapshot(
        "https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms",
        _fixture("connected-platforms-main.html"),
        config,
    ).normalized_content
    removed_line = "and remove connections when they're no longer needed."
    assert removed_line in full
    old = full.replace(removed_line, "").replace("\n\n", "\n")

    classification, reason, diff_text = monitoring_shared.classify_change(
        old,
        full,
        "https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms",
        config=config,
    )

    assert removed_line in diff_text
    assert (classification, reason) != (
        monitoring_shared.CLASSIFICATION_CRITICAL,
        "Deprecation notice",
    )
