"""Regression tests for Learn classification noise filtering."""
from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

import monitoring_shared  # noqa: E402


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
    old = "\n".join(
        [
            "Connected platforms in Microsoft Agent 365",
            "Rotate or revoke credentials",
        ]
    )
    new = "\n".join(
        [
            "Table of contents",
            "Access to this page requires authorization. You can try signing in or changing directories.",
            "Rotate or revoke credentials",
            "remove connections when they're no longer needed.",
        ]
    )

    classification, reason, _ = monitoring_shared.classify_change(old, new)

    assert classification == monitoring_shared.CLASSIFICATION_NOISE
    assert reason == "Authorization interstitial"


def test_real_deprecation_notice_remains_critical():
    old = "This connector is available."
    new = "This connector is deprecated and will be removed next quarter."

    classification, reason, _ = monitoring_shared.classify_change(old, new)

    assert classification == monitoring_shared.CLASSIFICATION_CRITICAL
    assert reason == "Deprecation notice"
