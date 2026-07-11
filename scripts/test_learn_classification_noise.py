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
