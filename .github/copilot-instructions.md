# Copilot Instructions for FSI-CopilotGov

## Project Overview

This is a **documentation-only** MkDocs Material site — a governance framework for Microsoft 365 Copilot in US Financial Services. There is no application code; all content lives in `docs/` as Markdown. CI validates structure and language rules, then deploys to GitHub Pages.

## Build and Validation Commands

```bash
# Serve docs locally
pip install mkdocs-material
mkdocs serve

# Build with strict validation (what CI runs)
mkdocs build --strict

# Validate control file structure (required sections/metadata)
python scripts/verify_controls.py

# Validate FSI language rules (prohibited phrases)
python scripts/verify_language_rules.py

# Run all CI checks locally
python scripts/verify_controls.py && python scripts/verify_language_rules.py && mkdocs build --strict
```

## Architecture

The framework has three content layers:

- **Framework** (`docs/framework/`) — Strategic governance context (executive summary, architecture, regulatory landscape, operating model)
- **Controls** (`docs/controls/pillar-{1-4}-*/`) — 54 technical controls across 4 lifecycle pillars specifying *what* to configure and *why*
- **Playbooks** (`docs/playbooks/control-implementations/{control-id}/`) — 4 playbooks per control specifying *how*: `portal-walkthrough.md`, `powershell-setup.md`, `verification-testing.md`, `troubleshooting.md`

Supporting content: `docs/getting-started/` (quick start, checklist), `docs/reference/` (regulatory mappings, glossary, admin toggles, FAQ).

## Control File Structure

Every control file in `docs/controls/` must include:

**Required metadata** (top of file):
- `Control ID:`, `Pillar:`, `Last Verified:`

**Required sections** (CI will fail without these):
- `## Objective`, `## Why This Matters for FSI`, `## Control Description`, `## Verification Criteria`, `## Additional Resources`

**Recommended sections** (CI warns if missing):
- `## Copilot Surface Coverage`, `## Governance Levels`, `## Setup & Configuration`, `## Financial Sector Considerations`

Each control provides three governance tiers: **Baseline**, **Recommended**, and **Regulated**.

## FSI Regulatory Language Rules (Critical)

CI enforces strict language rules via `scripts/verify_language_rules.py`. When writing documentation:

**Never use:** "ensures compliance", "guarantees", "will prevent", "eliminates risk"

**Instead use:** "supports compliance with", "helps meet", "aids in", "recommended to"

Always include implementation caveats ("Organizations should verify...") and reference specific regulations by name and section (e.g., "FINRA Rule 4511(a)"). Never claim a single control satisfies a regulation in isolation.

**Exemptions:** Control 3.5 (FINRA 2210) and its playbooks are exempt from language scanning because they intentionally contain prohibited marketing phrases as detection examples. New files containing intentional examples of prohibited language must be added to `EXEMPT_FILES` in `scripts/verify_language_rules.py`.

## Admin Role Naming

Use canonical short names in all documentation:

| Use This | NOT This |
|----------|----------|
| Entra Global Admin | Global Administrator |
| Purview Compliance Admin | Compliance Administrator |
| M365 Global Admin | Microsoft 365 Admin |
| Exchange Online Admin | Exchange Administrator |
| SharePoint Admin | SharePoint Administrator |
| Teams Admin | Teams Administrator |

## Navigation

All pages must be listed in `mkdocs.yml` under the `nav:` key. The `mkdocs build --strict` step will warn on omitted or not-found files.

## CI/CD

Two GitHub Actions workflows run on push to `main`:

1. **Publish Docs** — Runs `verify_controls.py` → `verify_language_rules.py` → `mkdocs build --strict` → deploys to GitHub Pages
2. **Link Validation** — Checks markdown links in `docs/` (also runs weekly on schedule); Microsoft admin portal URLs are excluded from link checking

Both workflows block commits containing internal-only artifacts (PDFs, TXT, JSON in `docs/reference/` or `docs/controls/`, and files like `docs/HANDOFF.md`).
