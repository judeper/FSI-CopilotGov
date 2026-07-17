#!/usr/bin/env python3
"""
Regulatory Monitoring Source Adapter for FSI-CopilotGov

Monitors regulatory changes from Federal Register API and FINRA notices page
that may require updates to the FSI-CopilotGov framework. This is a source
adapter for the unified monitoring framework - it uses shared utilities from
monitoring_shared.py.

Sources:
- Federal Register API (SEC, CFTC, OCC, Federal Reserve)
- FINRA Regulatory Notices (HTML scraping)

Usage:
    python scripts/regulatory_monitor.py [--dry-run] [--limit N] [--verbose] [--source SOURCE]

Exit Codes:
    0 - No new regulatory items detected
    1 - New regulatory items detected (triggers PR in CI)
    2 - Error during execution

Environment Variables:
    REGULATORY_MONITOR_DEBUG=1  - Enable debug output
"""

import argparse
import json
import logging
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

# Import shared monitoring framework
from monitoring_shared import (
    fetch_page,
    compute_hash,
    load_state,
    save_state_atomic,
    get_source_state,
    set_source_state,
    generate_report_header,
    generate_executive_summary,
    format_change_summary,
    write_report,
    load_monitoring_config,
    validate_config,
    DEFAULT_CONFIG_PATH,
    CLASSIFICATION_CRITICAL,
    CLASSIFICATION_HIGH,
    CLASSIFICATION_MEDIUM,
    CLASSIFICATION_NOISE,
)

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError as e:
    print(f"ERROR: Missing dependency: {e}")
    print("Install with: pip install requests beautifulsoup4")
    sys.exit(2)

# === Configuration ===
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR = PROJECT_ROOT / 'data'
REPORTS_DIR = PROJECT_ROOT / 'reports' / 'monitoring'
STATE_FILE = DATA_DIR / 'monitor-state.json'

# Source keys for unified state file
SOURCE_KEY_FEDERAL_REGISTER = "regulatory-federal-register"
SOURCE_KEY_FINRA = "regulatory-finra"

# Federal Register API configuration
FEDERAL_REGISTER_API_BASE = "https://www.federalregister.gov/api/v1"

# FINRA notices page
FINRA_NOTICES_URL = "https://www.finra.org/rules-guidance/notices"

FEDERAL_REGISTER_DETAIL_FETCH_LIMIT = 20
FINRA_DETAIL_FETCH_LIMIT = 20
FALLBACK_TEXT_MAX_CHARS = 4000
FEDERAL_REGISTER_DETAIL_SIGNAL = re.compile(
    r'\b(finra|rule\s*2210|communications?\s+with\s+the\s+public|retail\s+communications?|project(?:ed|ion)\s+performance|target(?:ed)?\s+returns?)\b',
    re.IGNORECASE,
)
FINRA_NOTICE_ID_PATTERN = re.compile(r'/notices/(\d{2})-(\d{2})', re.IGNORECASE)
FINRA_DETAIL_TITLE_SIGNAL = re.compile(
    r'\b(request\s+for\s+comment|regulatory\s+notice\s+\d{2}-\d{2}|rule\s*2210|communications?\s+with\s+the\s+public)\b',
    re.IGNORECASE,
)

# Configure logging
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(verbose: bool = False) -> logging.Logger:
    """Configure logging based on verbosity level."""
    level = logging.DEBUG if os.environ.get("REGULATORY_MONITOR_DEBUG") else (
        logging.INFO if verbose else logging.WARNING
    )

    logging.basicConfig(
        level=level,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    return logging.getLogger(__name__)


logger = logging.getLogger(__name__)


@dataclass
class RegulatoryItem:
    """Represents a regulatory document or notice."""
    source: str  # 'Federal Register' or 'FINRA'
    agency: str  # 'SEC', 'CFTC', 'OCC', 'Federal Reserve', 'FINRA'
    title: str
    url: str
    publication_date: str  # ISO format YYYY-MM-DD
    doc_type: Optional[str] = None  # 'RULE', 'PRORULE', 'NOTICE' (Federal Register only)
    abstract: str = ""
    document_id: str = ""  # Federal Register document number or FINRA URL
    classification: str = CLASSIFICATION_NOISE
    classification_reason: str = ""
    affected_controls: list = None

    def __post_init__(self):
        if self.affected_controls is None:
            self.affected_controls = []


def classify_regulatory_relevance(title: str, abstract: str, config: dict) -> tuple[str, str]:
    """
    Classify regulatory item for FSI Copilot governance relevance.

    Uses the unified 4-tier system (CRITICAL/HIGH/MEDIUM/NOISE) for consistency
    with Learn Monitor. Patterns are loaded from config.

    Args:
        title: Document title
        abstract: Document abstract
        config: Configuration dict with pattern definitions

    Returns:
        tuple: (tier, reason)
    """
    # Handle None values
    title = title or ""
    abstract = abstract or ""
    combined = f"{title.lower()} {abstract.lower()}"

    # Get regulatory patterns from config
    regulatory_config = config.get('regulatory', {})

    # CRITICAL: Directly mentions AI agents, copilot, or automated advice in FSI context
    critical_patterns = [
        (p['pattern'], p['reason'])
        for p in regulatory_config.get('critical_patterns', [])
    ]
    for pattern, reason in critical_patterns:
        if re.search(pattern, combined):
            return (CLASSIFICATION_CRITICAL, reason)

    # HIGH: AI, ML, automation terms + FSI-specific requirements
    high_patterns = [
        (p['pattern'], p['reason'])
        for p in regulatory_config.get('high_patterns', [])
    ]
    for pattern, reason in high_patterns:
        if re.search(pattern, combined):
            return (CLASSIFICATION_HIGH, reason)

    # MEDIUM: General FSI regulations that may indirectly affect AI agents
    medium_patterns = [
        (p['pattern'], p['reason'])
        for p in regulatory_config.get('medium_patterns', [])
    ]
    for pattern, reason in medium_patterns:
        if re.search(pattern, combined):
            return (CLASSIFICATION_MEDIUM, reason)

    # NOISE: Everything else (general regulatory items with no FSI/AI relevance)
    return (CLASSIFICATION_NOISE, "No FSI Copilot governance relevance detected")


def find_affected_controls_by_keywords(title: str, abstract: str, config: dict) -> list[str]:
    """
    Find potentially affected controls based on keyword matching.

    Args:
        title: Document title
        abstract: Document abstract
        config: Configuration dict with keyword_control_map

    Returns:
        list: Control IDs (e.g., ['1.3', '1.5', '2.6'])
    """
    # Handle None values
    title = title or ""
    abstract = abstract or ""
    combined = f"{title.lower()} {abstract.lower()}"
    affected = set()

    # Build keyword map from config
    keyword_map = {
        entry['keyword']: [c['id'] for c in entry['controls']]
        for entry in config.get('keyword_control_map', [])
    }

    for keyword, controls in keyword_map.items():
        # Use word boundary matching to avoid partial matches
        pattern = rf'\b{re.escape(keyword)}\b'
        if re.search(pattern, combined, re.IGNORECASE):
            affected.update(controls)

    return sorted(list(affected))


def _get_operational_settings(config: dict) -> tuple[int, int, float]:
    """Return request timeout, max retries, and request delay from config."""
    operational = config.get("operational", {})
    request_timeout = int(operational.get("request_timeout", 30))
    max_retries = int(operational.get("max_retries", 3))
    request_delay = float(operational.get("request_delay", 1.0))
    return request_timeout, max_retries, request_delay


def _extract_compact_text(html: str, selectors: list[str]) -> str:
    """Extract compact text from the first selector that yields content."""
    soup = BeautifulSoup(html or "", "html.parser")

    for selector in selectors:
        node = soup.select_one(selector)
        if node:
            text = re.sub(r"\s+", " ", node.get_text(" ", strip=True)).strip()
            if text:
                return text[:FALLBACK_TEXT_MAX_CHARS]

    body = soup.find("body")
    if not body:
        return ""
    return re.sub(r"\s+", " ", body.get_text(" ", strip=True)).strip()[:FALLBACK_TEXT_MAX_CHARS]


def _extract_federal_register_fallback_text(html: str) -> str:
    """Extract fallback text from a Federal Register document page."""
    return _extract_compact_text(
        html,
        selectors=[
            "section#fulltext_content",
            "div#fulltext_content",
            "article",
            "main",
        ],
    )


def _extract_finra_notice_fallback_text(html: str) -> str:
    """Extract fallback text from a FINRA notice page."""
    return _extract_compact_text(
        html,
        selectors=[
            "div.field--name-body",
            "article",
            "main",
            "div.layout-content",
        ],
    )


def _fetch_cached_fallback_text(
    *,
    url: str,
    session: requests.Session,
    cache: dict[str, str],
    request_delay: float,
    max_retries: int,
    extractor,
) -> tuple[str, bool]:
    """Fetch fallback text once per URL and return (text, fetched_new)."""
    if not url:
        return "", False

    if url in cache:
        return cache[url], False

    if request_delay > 0:
        time.sleep(request_delay)

    result = fetch_page(url, session, max_retries=max_retries)
    if result["status_code"] != 200:
        logger.warning(
            "Detail fetch failed for %s (status=%s, error=%s)",
            url,
            result["status_code"],
            result.get("error"),
        )
        cache[url] = ""
        return "", True

    fallback_text = extractor(result["content"])
    cache[url] = fallback_text
    return fallback_text, True


def _should_fetch_federal_register_detail(
    title: str,
    abstract: str,
    classification: str,
    doc_type: str,
) -> bool:
    """Determine if a Federal Register body fetch is warranted."""
    if (abstract or "").strip():
        return False
    if classification in {CLASSIFICATION_CRITICAL, CLASSIFICATION_HIGH}:
        return False
    if doc_type not in {"NOTICE", "PRORULE"}:
        return False
    return bool(FEDERAL_REGISTER_DETAIL_SIGNAL.search(title or ""))


def _should_fetch_finra_notice_detail(title: str, url: str, classification: str) -> bool:
    """Determine if a FINRA notice body fetch is warranted."""
    if classification in {CLASSIFICATION_CRITICAL, CLASSIFICATION_HIGH}:
        return False

    if FINRA_DETAIL_TITLE_SIGNAL.search(title or ""):
        return True

    match = FINRA_NOTICE_ID_PATTERN.search(url or "")
    if not match:
        return False

    notice_year_short = int(match.group(1))
    current_year_short = datetime.now(timezone.utc).year % 100
    return notice_year_short >= (current_year_short - 1)


def fetch_federal_register_documents(
    session: requests.Session,
    since_date: str,
    config: dict,
    limit: Optional[int] = None,
    detail_fetch_limit: int = FEDERAL_REGISTER_DETAIL_FETCH_LIMIT,
) -> list[RegulatoryItem]:
    """
    Fetch documents from Federal Register API.

    Args:
        session: requests.Session instance
        since_date: ISO date string (YYYY-MM-DD) - fetch documents published on or after this date
        config: Configuration dict with federal_register settings
        limit: Maximum documents to fetch (for testing)
        detail_fetch_limit: Maximum detail pages to fetch for fallback text

    Returns:
        list[RegulatoryItem]: New regulatory items
    """
    items = []

    request_timeout, max_retries, request_delay = _get_operational_settings(config)

    # Get agencies and doc types from config
    fed_config = config.get('federal_register', {})
    agencies = [a['slug'] for a in fed_config.get('agencies', [])]
    doc_types = fed_config.get('document_types', ['RULE', 'PRORULE', 'NOTICE'])

    # Build agency short name map from config
    agency_short_map = {
        a['slug']: a.get('short_name', a['slug'])
        for a in fed_config.get('agencies', [])
    }

    # Build query parameters
    params = {
        'conditions[agencies][]': agencies,
        'conditions[type][]': doc_types,
        'conditions[publication_date][gte]': since_date,
        'per_page': 100,  # API max is 1000
        'order': 'newest',
        'fields[]': ['document_number', 'title', 'abstract', 'publication_date', 'type', 'html_url', 'agencies'],
    }

    data = {}
    for attempt in range(max_retries):
        try:
            logger.info(f"Querying Federal Register API for documents since {since_date}...")
            response = session.get(
                f"{FEDERAL_REGISTER_API_BASE}/documents.json",
                params=params,
                timeout=request_timeout,
            )
            response.raise_for_status()
            data = response.json()
            break
        except requests.RequestException as e:
            if attempt == max_retries - 1:
                logger.error(f"Federal Register API error: {e}")
                return items
            sleep_seconds = request_delay if request_delay > 0 else (2 ** attempt)
            logger.warning(
                "Federal Register API request failed (attempt %s/%s): %s; retrying in %.1fs",
                attempt + 1,
                max_retries,
                e,
                sleep_seconds,
            )
            time.sleep(sleep_seconds)
        except json.JSONDecodeError as e:
            logger.error(f"Federal Register API response parsing error: {e}")
            return items

    documents = data.get('results', [])
    logger.info(f"Federal Register API returned {len(documents)} documents")

    # Apply limit if specified
    if limit:
        documents = documents[:limit]
        logger.info(f"Limited to {limit} documents for testing")

    detail_cache: dict[str, str] = {}
    detail_fetches = 0
    detail_limit_logged = False

    for doc in documents:
        # Extract agency names
        doc_agencies = doc.get('agencies', [])
        agency_slugs = [agency.get('slug', '') for agency in doc_agencies]
        agency_names = [agency.get('name', 'Unknown') for agency in doc_agencies]
        agency_name = ', '.join(agency_names) if agency_names else 'Unknown'

        # Map to canonical short names using config
        agency_short = 'Unknown'
        for slug in agency_slugs:
            if slug in agency_short_map:
                agency_short = agency_short_map[slug]
                break
        if agency_short == 'Unknown':
            agency_short = agency_name

        title = doc.get('title', 'Untitled')
        abstract = doc.get('abstract', '') or ''
        doc_type = doc.get('type', '')
        url = doc.get('html_url', '')

        tier, reason = classify_regulatory_relevance(title, abstract, config)
        effective_text = abstract

        should_fetch_detail = _should_fetch_federal_register_detail(
            title=title,
            abstract=abstract,
            classification=tier,
            doc_type=doc_type,
        )
        if should_fetch_detail and detail_fetches < detail_fetch_limit:
            fallback_text, fetched_new = _fetch_cached_fallback_text(
                url=url,
                session=session,
                cache=detail_cache,
                request_delay=request_delay,
                max_retries=max_retries,
                extractor=_extract_federal_register_fallback_text,
            )
            if fetched_new:
                detail_fetches += 1
            if fallback_text:
                effective_text = fallback_text
                tier, reason = classify_regulatory_relevance(title, effective_text, config)
        elif should_fetch_detail and not detail_limit_logged:
            logger.info(
                "Federal Register detail fetch limit reached (%s); skipping additional fallback fetches",
                detail_fetch_limit,
            )
            detail_limit_logged = True

        affected_controls = find_affected_controls_by_keywords(title, effective_text, config)

        item = RegulatoryItem(
            source='Federal Register',
            agency=agency_short,
            title=title,
            url=url,
            publication_date=doc.get('publication_date', ''),
            doc_type=doc_type,
            abstract=effective_text,
            document_id=doc.get('document_number', ''),
            classification=tier,
            classification_reason=reason,
            affected_controls=affected_controls,
        )
        items.append(item)

    return items


def fetch_finra_notices(
    session: requests.Session,
    config: dict,
    limit: Optional[int] = None,
    detail_fetch_limit: int = FINRA_DETAIL_FETCH_LIMIT,
) -> list[RegulatoryItem]:
    """
    Scrape FINRA regulatory notices page.

    Args:
        session: requests.Session instance
        config: Configuration dict for classification
        limit: Maximum notices to fetch (for testing)
        detail_fetch_limit: Maximum notice pages to fetch for fallback text

    Returns:
        list[RegulatoryItem]: FINRA notices
    """
    items = []
    _, max_retries, request_delay = _get_operational_settings(config)

    logger.info(f"Fetching FINRA notices from {FINRA_NOTICES_URL}...")
    result = fetch_page(FINRA_NOTICES_URL, session, max_retries=max_retries)

    if result['status_code'] != 200:
        logger.error(f"FINRA notices page returned status {result['status_code']}")
        if result.get("error"):
            logger.error("FINRA notices fetch error: %s", result["error"])
        return items

    soup = BeautifulSoup(result['content'], 'html.parser')

    # FINRA notices are in a table with class 'notices-table' or similar.
    notice_links = []

    for article in soup.find_all(['article', 'div'], class_=re.compile(r'notice|regulatory')):
        link = article.find('a', href=re.compile(r'/rules-guidance/notices/'))
        if link:
            notice_links.append(link)

    if not notice_links:
        notice_links = soup.find_all('a', href=re.compile(r'/rules-guidance/notices/\d{2}-\d{2}'))

    logger.info(f"Found {len(notice_links)} FINRA notice links")

    if limit:
        notice_links = notice_links[:limit]
        logger.info(f"Limited to {limit} notices for testing")

    detail_cache: dict[str, str] = {}
    detail_fetches = 0
    detail_limit_logged = False

    for link in notice_links:
        title = link.get_text(strip=True)
        url = link.get('href', '')

        if url.startswith('/'):
            url = f"https://www.finra.org{url}"

        match = FINRA_NOTICE_ID_PATTERN.search(url)
        if match:
            year_short = match.group(1)
            notice_num = match.group(2)
            year = f"20{year_short}"
            publication_date = f"{year}-01-01"
            document_id = f"FINRA {year_short}-{notice_num}"
        else:
            publication_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
            document_id = url

        tier, reason = classify_regulatory_relevance(title, "", config)
        effective_text = ""

        should_fetch_detail = _should_fetch_finra_notice_detail(title, url, tier)
        if should_fetch_detail and detail_fetches < detail_fetch_limit:
            fallback_text, fetched_new = _fetch_cached_fallback_text(
                url=url,
                session=session,
                cache=detail_cache,
                request_delay=request_delay,
                max_retries=max_retries,
                extractor=_extract_finra_notice_fallback_text,
            )
            if fetched_new:
                detail_fetches += 1
            if fallback_text:
                effective_text = fallback_text
                tier, reason = classify_regulatory_relevance(title, effective_text, config)
        elif should_fetch_detail and not detail_limit_logged:
            logger.info(
                "FINRA detail fetch limit reached (%s); skipping additional fallback fetches",
                detail_fetch_limit,
            )
            detail_limit_logged = True

        affected_controls = find_affected_controls_by_keywords(title, effective_text, config)

        item = RegulatoryItem(
            source='FINRA',
            agency='FINRA',
            title=title,
            url=url,
            publication_date=publication_date,
            doc_type='NOTICE',
            abstract=effective_text,
            document_id=document_id,
            classification=tier,
            classification_reason=reason,
            affected_controls=affected_controls,
        )
        items.append(item)

    return items


def _normalize_hash_field(text: str) -> str:
    """Collapse incidental whitespace for change-detection hashing.

    Federal Register abstracts (and fetched fallback bodies) churn cosmetically
    within the ``since_date`` window -- leading/trailing spaces, doubled spaces,
    and newline reflow -- without any substantive change. Hashing the raw text
    made those cosmetic edits flip the content hash and re-emit an otherwise
    unchanged item (observed: 17 Federal Register NOISE items re-reported). This
    normalization only strips/collapses whitespace; it does not lowercase, decode
    entities, or otherwise alter meaning, so a genuine wording change still
    produces a different hash and is still reported. Substantive relevance
    classification is computed separately (``classify_regulatory_relevance``) and
    is unaffected.
    """
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


def _content_fingerprint(item: RegulatoryItem) -> str:
    """Whitespace-normalized ``title|abstract|publication_date`` used as the
    change-detection hash input, so cosmetic churn does not re-emit an item."""
    return "|".join(
        _normalize_hash_field(part)
        for part in (item.title, item.abstract, item.publication_date)
    )


def check_for_new_items(source_key: str, items: list[RegulatoryItem], source_state: dict) -> list[RegulatoryItem]:
    """
    Compare fetched items against source state to find new items.

    Args:
        source_key: Source key in unified state file
        items: List of fetched regulatory items
        source_state: Source-specific state dict

    Returns:
        list[RegulatoryItem]: New items not in state
    """
    new_items = []
    existing_entries = source_state.get('entries', {})

    for item in items:
        # Use document_id or URL as the key
        entry_key = item.document_id if item.document_id else item.url

        # Compute hash of the item content (whitespace-normalized so cosmetic
        # abstract churn within the since_date window does not re-emit an item).
        content_hash = compute_hash(_content_fingerprint(item))

        # Check if this is a new item or changed item
        if entry_key not in existing_entries:
            logger.info(f"  New item: {item.title[:60]}... ({item.agency})")
            new_items.append(item)
        elif existing_entries[entry_key] != content_hash:
            logger.info(f"  Updated item: {item.title[:60]}... ({item.agency})")
            new_items.append(item)

    return new_items


def update_source_state(source_key: str, items: list[RegulatoryItem], state: dict) -> None:
    """
    Update source state with new item hashes.

    Args:
        source_key: Source key in unified state file
        items: List of regulatory items to add to state
        state: Full state dict (modified in place)
    """
    source_state = get_source_state(state, source_key)
    entries = source_state.get('entries', {})

    for item in items:
        entry_key = item.document_id if item.document_id else item.url
        entries[entry_key] = compute_hash(_content_fingerprint(item))

    source_state['entries'] = entries
    source_state['last_run'] = datetime.now(timezone.utc).isoformat()

    set_source_state(state, source_key, source_state)


def generate_regulatory_report(
    all_new_items: list[RegulatoryItem],
    report_path: Path
) -> None:
    """
    Generate regulatory change report using shared report format helpers.

    Args:
        all_new_items: All new regulatory items from all sources
        report_path: Path to write report
    """
    # Categorize by classification tier
    critical_items = [item for item in all_new_items if item.classification == CLASSIFICATION_CRITICAL]
    high_items = [item for item in all_new_items if item.classification == CLASSIFICATION_HIGH]
    medium_items = [item for item in all_new_items if item.classification == CLASSIFICATION_MEDIUM]
    noise_items = [item for item in all_new_items if item.classification == CLASSIFICATION_NOISE]

    # Build report content
    lines = []

    # Header
    run_date = datetime.now(timezone.utc).isoformat(timespec='seconds')
    lines.append(generate_report_header(
        title="Regulatory Monitor Report",
        run_date=run_date,
        metadata={
            "New Items": len(all_new_items),
            "Sources": "Federal Register (SEC, CFTC, OCC, Federal Reserve) + FINRA Regulatory Notices"
        }
    ))

    # Executive summary
    lines.append(generate_executive_summary({
        'CRITICAL': len(critical_items),
        'HIGH': len(high_items),
        'MEDIUM': len(medium_items),
        'NOISE': len(noise_items),
    }))

    # Summary table (for CRITICAL + HIGH only, for quick scanning)
    priority_items = critical_items + high_items
    if priority_items:
        lines.append("## Summary (Quick Scan)\n")
        lines.append("| # | Source | Agency | Classification | Affected Controls | Action |\n")
        lines.append("|---|--------|--------|----------------|-------------------|--------|\n")

        for i, item in enumerate(priority_items, 1):
            # Shorten URL for table
            url_short = item.title[:40] + "..." if len(item.title) > 40 else item.title
            controls = ", ".join(item.affected_controls) if item.affected_controls else "None identified"
            action = "Review and update framework" if item.classification == CLASSIFICATION_CRITICAL else "Review"

            lines.append(f"| {i} | {item.source} | {item.agency} | {item.classification} | {controls} | {action} |\n")

        lines.append("\n")

    # CRITICAL items (detailed)
    if critical_items:
        lines.append("## CRITICAL Items\n")
        lines.append("These regulatory changes directly mention AI agents, copilot, or automated advice in FSI context.\n\n")

        for i, item in enumerate(critical_items, 1):
            lines.append(f"### {i}. [{item.title}]({item.url})\n\n")
            lines.append(f"- **Source:** {item.agency} via {item.source}\n")
            lines.append(f"- **Published:** {item.publication_date}\n")
            if item.doc_type:
                lines.append(f"- **Type:** {item.doc_type}\n")
            lines.append(f"- **Classification:** {item.classification} — {item.classification_reason}\n")

            if item.abstract:
                lines.append(f"- **Abstract:** {item.abstract[:500]}{'...' if len(item.abstract) > 500 else ''}\n")

            if item.affected_controls:
                lines.append(f"- **Potentially Affected Controls:**\n")
                for control in item.affected_controls:
                    lines.append(f"  - Control {control}\n")

            lines.append("\n")

    # HIGH items (detailed)
    if high_items:
        lines.append("## HIGH Priority Items\n")
        lines.append("These regulatory changes reference AI, ML, automation, or FSI-specific requirements relevant to Copilot governance.\n\n")

        for i, item in enumerate(high_items, 1):
            lines.append(f"### {i}. [{item.title}]({item.url})\n\n")
            lines.append(f"- **Source:** {item.agency} via {item.source}\n")
            lines.append(f"- **Published:** {item.publication_date}\n")
            if item.doc_type:
                lines.append(f"- **Type:** {item.doc_type}\n")
            lines.append(f"- **Classification:** {item.classification} — {item.classification_reason}\n")

            if item.abstract:
                lines.append(f"- **Abstract:** {item.abstract[:300]}{'...' if len(item.abstract) > 300 else ''}\n")

            if item.affected_controls:
                lines.append(f"- **Potentially Affected Controls:** {', '.join(item.affected_controls)}\n")

            lines.append("\n")

    # MEDIUM items (abbreviated)
    if medium_items:
        lines.append("## MEDIUM Priority Items\n")
        lines.append("General FSI regulations that may indirectly affect AI agent deployments.\n\n")

        for item in medium_items:
            lines.append(f"- [{item.title}]({item.url}) ({item.agency}, {item.publication_date})\n")

        lines.append("\n")

    # NOISE items (list only)
    if noise_items:
        lines.append("## NOISE Items\n")
        lines.append("Regulatory items with no FSI Copilot governance relevance.\n\n")

        for item in noise_items:
            lines.append(f"- [{item.title}]({item.url}) ({item.agency})\n")

        lines.append("\n")

    # Write report
    content = "".join(lines)
    write_report(content, REPORTS_DIR, report_path.name)
    logger.info(f"Report written to {report_path}")


def main():
    """Main execution."""
    parser = argparse.ArgumentParser(
        description="Monitor regulatory changes from Federal Register and FINRA"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help="Fetch and analyze without updating state file"
    )
    parser.add_argument(
        '--limit',
        type=int,
        help="Limit number of items per source (for testing)"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="Enable verbose output"
    )
    parser.add_argument(
        '--source',
        choices=['federal-register', 'finra', 'all'],
        default='all',
        help="Which source(s) to monitor"
    )
    parser.add_argument(
        '--config',
        type=str,
        default=None,
        help='Path to config file (default: scripts/config/monitoring-config.yaml)'
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate config file and exit without running'
    )

    args = parser.parse_args()

    # Setup logging
    global logger
    logger = setup_logging(verbose=args.verbose)

    # Load and validate config
    config_path = args.config or DEFAULT_CONFIG_PATH
    config = load_monitoring_config(config_path)

    if args.validate:
        is_valid, errors = validate_config(config)
        if is_valid:
            print(f"Config valid: {config_path}")
            sys.exit(0)
        else:
            print(f"Config errors in {config_path}:")
            for err in errors:
                print(f"  - {err}")
            sys.exit(2)

    logger.info("=== Regulatory Monitor ===")
    logger.info(f"Source: {args.source}")
    logger.info(f"Dry run: {args.dry_run}")
    logger.info(f"Config: {config_path}")
    if args.limit:
        logger.info(f"Limit: {args.limit} items per source")

    # Ensure directories exist
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Load unified state
    state = load_state(STATE_FILE)

    # Graceful degradation: --dry-run skips all network calls so the script
    # can be smoke-tested in CI environments without outbound access.
    if args.dry_run:
        logger.info("Dry run: skipping all network calls (offline mode)")
        print("INFO: regulatory_monitor dry-run — network calls skipped (offline mode).")
        sys.exit(0)

    # Create session
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'FSI-CopilotGov-Regulatory-Monitor/1.0 (https://github.com/judeper/FSI-CopilotGov)'
    })

    all_new_items = []

    # Fetch from Federal Register
    if args.source in ['federal-register', 'all']:
        logger.info("\n--- Federal Register ---")
        fed_state = get_source_state(state, SOURCE_KEY_FEDERAL_REGISTER)

        # Determine since_date (last check or 30 days ago)
        since_date = fed_state.get('last_checked')
        if not since_date:
            since_date = (datetime.now(timezone.utc) - timedelta(days=30)).strftime('%Y-%m-%d')
            logger.info(f"No prior state, fetching documents from last 30 days")
        else:
            logger.info(f"Fetching documents since {since_date}")

        fed_items = fetch_federal_register_documents(session, since_date, config, limit=args.limit)
        new_fed_items = check_for_new_items(SOURCE_KEY_FEDERAL_REGISTER, fed_items, fed_state)

        logger.info(f"Federal Register: {len(new_fed_items)} new items")
        all_new_items.extend(new_fed_items)

        # Update state
        if not args.dry_run:
            update_source_state(SOURCE_KEY_FEDERAL_REGISTER, fed_items, state)
            # Update last_checked to today
            fed_state = get_source_state(state, SOURCE_KEY_FEDERAL_REGISTER)
            fed_state['last_checked'] = datetime.now(timezone.utc).strftime('%Y-%m-%d')
            set_source_state(state, SOURCE_KEY_FEDERAL_REGISTER, fed_state)

    # Fetch from FINRA
    if args.source in ['finra', 'all']:
        logger.info("\n--- FINRA Notices ---")
        finra_state = get_source_state(state, SOURCE_KEY_FINRA)

        finra_items = fetch_finra_notices(session, config, limit=args.limit)
        new_finra_items = check_for_new_items(SOURCE_KEY_FINRA, finra_items, finra_state)

        logger.info(f"FINRA: {len(new_finra_items)} new items")
        all_new_items.extend(new_finra_items)

        # Update state
        if not args.dry_run:
            update_source_state(SOURCE_KEY_FINRA, finra_items, state)

    # Generate report if new items found
    if all_new_items:
        logger.info(f"\n=== {len(all_new_items)} total new regulatory items detected ===")

        report_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        report_path = REPORTS_DIR / f"regulatory-changes-{report_date}.md"

        generate_regulatory_report(all_new_items, report_path)

        # Save state
        if not args.dry_run:
            save_state_atomic(state, STATE_FILE)
            logger.info(f"State updated: {STATE_FILE}")
        else:
            logger.info("Dry run: state not updated")

        # Exit code 1 indicates new items (triggers PR in CI)
        sys.exit(1)

    else:
        logger.info("\n=== No new regulatory items detected ===")

        # Save state even if no changes (updates last_run timestamps)
        if not args.dry_run:
            save_state_atomic(state, STATE_FILE)

        # Exit code 0 indicates no changes
        sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        logger.debug("Traceback:", exc_info=True)
        sys.exit(2)
