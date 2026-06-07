"""verify_meta_tags.py — post-build OpenGraph + Twitter Card meta gate.

For each representative page (homepage + a deep playbook + a reference page),
this verifier asserts the required meta tags render with non-empty content
attributes.

CopilotGov sampled pages (adapted from FSI-AgentGov):
  - index.html                                         — homepage
  - playbooks/control-implementations/1.1/portal-walkthrough/index.html
                                                       — deep playbook page
  - reference/microsoft-learn-urls/index.html          — top-level reference

Usage:

  python scripts/verify_meta_tags.py site/

Returns non-zero exit code if any required meta tag is missing or empty
on any sampled page.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Pages we sample. Each is a representative slice of the CopilotGov site corpus.
SAMPLED_PAGES = (
    "index.html",
    "playbooks/control-implementations/1.1/portal-walkthrough/index.html",
    "reference/microsoft-learn-urls/index.html",
)

# Meta tags that MUST be present on every page with non-empty content="".
REQUIRED_META = (
    ('property', 'og:title'),
    ('property', 'og:description'),
    ('property', 'og:url'),
    ('property', 'og:type'),
    ('property', 'og:site_name'),
    ('name', 'twitter:card'),
    ('name', 'twitter:title'),
    ('name', 'twitter:description'),
)


def find_meta_content(html: str, attr: str, value: str) -> str | None:
    """Return the content="..." of a <meta {attr}="{value}" content="..."> tag.

    Returns None if the tag is absent. Returns "" if present-but-empty.
    Tolerates attribute order (content first or second) and arbitrary whitespace.
    """
    pattern1 = re.compile(
        rf'<meta\b[^>]*\b{re.escape(attr)}\s*=\s*"{re.escape(value)}"'
        r'[^>]*\bcontent\s*=\s*"([^"]*)"',
        re.IGNORECASE,
    )
    match = pattern1.search(html)
    if match:
        return match.group(1)
    pattern2 = re.compile(
        r'<meta\b[^>]*\bcontent\s*=\s*"([^"]*)"'
        rf'[^>]*\b{re.escape(attr)}\s*=\s*"{re.escape(value)}"',
        re.IGNORECASE,
    )
    match = pattern2.search(html)
    if match:
        return match.group(1)
    return None


def check_page(html: str) -> list[str]:
    """Return a list of human-readable failure messages for one page."""
    failures: list[str] = []
    for attr, value in REQUIRED_META:
        content = find_meta_content(html, attr, value)
        if content is None:
            failures.append(f"missing <meta {attr}=\"{value}\">")
            continue
        if not content.strip():
            failures.append(
                f'<meta {attr}="{value}"> has empty content=""'
            )
    return failures


def scan(site_root: Path, sampled_pages: tuple[str, ...] = SAMPLED_PAGES) -> dict[str, list[str]]:
    """Return {page_path: [failures]} for every sampled page that fails."""
    broken: dict[str, list[str]] = {}
    for rel in sampled_pages:
        page_path = site_root / rel
        if not page_path.is_file():
            broken[rel] = [f"sampled page not found at {page_path}"]
            continue
        html = page_path.read_text(encoding="utf-8")
        failures = check_page(html)
        if failures:
            broken[rel] = failures
    return broken


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "site_root",
        type=Path,
        help="Path to the built MkDocs site/ directory.",
    )
    args = parser.parse_args()

    if not args.site_root.is_dir():
        print(f"ERROR: site root not found: {args.site_root}", file=sys.stderr)
        return 2

    broken = scan(args.site_root)
    if broken:
        print(
            f"FAIL: OpenGraph/Twitter meta missing on "
            f"{len(broken)} of {len(SAMPLED_PAGES)} sampled pages:",
            file=sys.stderr,
        )
        for page, failures in broken.items():
            print(f"  - {page}:", file=sys.stderr)
            for f in failures:
                print(f"      {f}", file=sys.stderr)
        return 1

    print(
        f"OK: all {len(REQUIRED_META)} required meta tags present on "
        f"{len(SAMPLED_PAGES)} sampled pages."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
