"""Regression tests for monitoring_shared.fetch_page retry semantics."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
import sys
from pathlib import Path

import pytest
import requests

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

import monitoring_shared  # noqa: E402


@dataclass
class _FakeResponse:
    status_code: int
    text: str
    headers: dict
    url: str


class _SequencedSession:
    def __init__(self, outcomes):
        self._outcomes = list(outcomes)

    def get(self, *_args, **_kwargs):
        if not self._outcomes:
            raise AssertionError("session.get called more times than configured")
        outcome = self._outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


def _response(status_code: int, *, url: str, retry_after=None) -> _FakeResponse:
    headers = {"Content-Type": "text/html"}
    if retry_after is not None:
        headers["Retry-After"] = retry_after
    return _FakeResponse(status_code=status_code, text=f"body-{status_code}", headers=headers, url=url)


def test_fetch_page_recovers_after_repeated_429_with_retry_after(monkeypatch):
    sleeps = []
    monkeypatch.setattr(monitoring_shared.time, "sleep", sleeps.append)
    session = _SequencedSession(
        [
            _response(429, url="https://example.com/page", retry_after="3"),
            _response(429, url="https://example.com/page", retry_after="1"),
            _response(200, url="https://example.com/page"),
        ]
    )

    result = monitoring_shared.fetch_page("https://example.com/page", session, max_retries=4)

    assert result["status_code"] == 200
    assert result["error"] is None
    assert sleeps == [3, 1]


def test_fetch_page_honors_http_date_retry_after(monkeypatch):
    fixed_now = datetime(2026, 9, 2, 12, 0, 0, tzinfo=timezone.utc)
    retry_at = format_datetime(fixed_now + timedelta(seconds=7), usegmt=True)

    class _FrozenDateTime(datetime):
        @classmethod
        def now(cls, tz=None):
            return fixed_now if tz is not None else fixed_now.replace(tzinfo=None)

    sleeps = []
    monkeypatch.setattr(monitoring_shared, "datetime", _FrozenDateTime)
    monkeypatch.setattr(monitoring_shared.time, "sleep", sleeps.append)
    session = _SequencedSession(
        [
            _response(429, url="https://example.com/page", retry_after=retry_at),
            _response(200, url="https://example.com/page"),
        ]
    )

    result = monitoring_shared.fetch_page("https://example.com/page", session, max_retries=3)

    assert result["status_code"] == 200
    assert sleeps == [7]


@pytest.mark.parametrize(
    "retry_after",
    [None, "", "not-a-number", "-5", "5000"],
)
def test_fetch_page_uses_bounded_backoff_for_invalid_or_excessive_retry_after(
    monkeypatch,
    retry_after,
):
    sleeps = []
    monkeypatch.setattr(monitoring_shared.time, "sleep", sleeps.append)
    session = _SequencedSession(
        [
            _response(429, url="https://example.com/page", retry_after=retry_after),
            _response(200, url="https://example.com/page"),
        ]
    )

    result = monitoring_shared.fetch_page("https://example.com/page", session, max_retries=3)

    assert result["status_code"] == 200
    assert sleeps == [monitoring_shared.RATE_LIMIT_BACKOFF_BASE_SECONDS]


def test_fetch_page_429_exhaustion_reports_truthful_status(monkeypatch):
    sleeps = []
    monkeypatch.setattr(monitoring_shared.time, "sleep", sleeps.append)
    session = _SequencedSession(
        [
            _response(429, url="https://example.com/page", retry_after="5000"),
            _response(429, url="https://example.com/page", retry_after="5000"),
            _response(429, url="https://example.com/page", retry_after="5000"),
        ]
    )

    result = monitoring_shared.fetch_page("https://example.com/page", session, max_retries=3)

    assert result["status_code"] == 429
    assert "rate limit persisted" in result["error"]
    assert result["error"].startswith("HTTP 429")
    assert result["was_redirected"] is False
    assert sleeps == [
        monitoring_shared.RATE_LIMIT_BACKOFF_BASE_SECONDS,
        monitoring_shared.RATE_LIMIT_BACKOFF_BASE_SECONDS * 2,
    ]


def test_fetch_page_429_wait_budget_is_bounded(monkeypatch):
    sleeps = []
    monkeypatch.setattr(monitoring_shared.time, "sleep", sleeps.append)
    session = _SequencedSession(
        [_response(429, url="https://example.com/page")] * 20
    )

    result = monitoring_shared.fetch_page("https://example.com/page", session, max_retries=20)

    assert result["status_code"] == 429
    assert sum(sleeps) == monitoring_shared.MAX_RATE_LIMIT_WAIT_SECONDS
    assert "waited 120s" in result["error"]


def test_fetch_page_request_exception_retries_and_returns_real_error(monkeypatch):
    sleeps = []
    monkeypatch.setattr(monitoring_shared.time, "sleep", sleeps.append)
    session = _SequencedSession(
        [
            requests.Timeout("temporary timeout"),
            requests.Timeout("temporary timeout"),
            requests.Timeout("final timeout"),
        ]
    )

    result = monitoring_shared.fetch_page("https://example.com/page", session, max_retries=3)

    assert result["status_code"] == 0
    assert "final timeout" in result["error"]
    assert sleeps == [1, 2]
