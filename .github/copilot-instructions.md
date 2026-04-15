# Copilot Instructions for FSI-CopilotGov

## Project Overview

This is a **documentation-only** MkDocs Material site — a governance framework for Microsoft 365 Copilot in US Financial Services. There is no application code; all content lives in `docs/` as Markdown. CI validates structure and language rules, then deploys to GitHub Pages.

Key platform areas covered: Copilot Chat (Basic and Premium tiers), Agent 365 governance, Entra Agent ID, Work IQ, Copilot Cowork, Edit with Copilot (Agent Mode), Copilot Pages and Notebooks, declarative and SharePoint agents, third-party model providers (Anthropic, xAI), Microsoft Purview compliance controls (DLP, sensitivity labels, eDiscovery, communication compliance, insider risk, data retention, DSPM data risk assessments, Compliance Manager), and SharePoint Advanced Management (RCD, RAC, Content Management Assessment, site lifecycle management, Microsoft 365 Archive).

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
- **Controls** (`docs/controls/pillar-{1-4}-*/`) — 57 technical controls across 4 lifecycle pillars specifying *what* to configure and *why*
- **Playbooks** (`docs/playbooks/`) — control implementation playbooks in `control-implementations/{control-id}/` plus cross-control operational guidance in folders such as `governance-operations/` and `compliance-and-audit/`

Supporting content: `docs/getting-started/` (quick start, checklist, phased rollout), `docs/reference/` (regulatory mappings, glossary, admin toggles, FAQ, external tool references), `docs/start-here.md` (newcomer orientation page).

### Interactive Assessment Tool

- **Page**: `docs/assessment/index.md` — Governance Scorecard, a browser-based self-assessment across all 57 controls
- **App code**: `docs/javascripts/assessment-app.js` (main app), `docs/javascripts/assessment-loader.js` (bootstrap)
- **Styles**: `docs/stylesheets/assessment.css`
- **Data extraction**: `scripts/extract_assessment_data.py` — parses control markdown files to generate `docs/javascripts/assessment-data.json`
- **Vendor libs**: `docs/javascripts/lib/chart.min.js` (Chart.js for radar/bar charts); see `docs/javascripts/lib/VENDOR-MANIFEST.md` for license info

All assessment data stays client-side (no server calls). The assessment-data.json file is generated, not hand-edited.

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

## Regulatory Citation Conventions

Use these validated citations consistently across all controls and playbooks:

| Topic | Use This | NOT This | Why |
|-------|----------|----------|-----|
| Third-party risk (OCC) | OCC Bulletin 2023-17 | OCC Bulletin 2013-29 | 2013-29 was rescinded/superseded by 2023-17 |
| GLBA for banks/broker-dealers | GLBA §501(b) | GLBA Safeguards Rule | FTC Safeguards Rule applies to non-bank FTC-regulated institutions only |
| Model risk management | SR 11-7 / OCC Bulletin 2011-12 | OCC SR 11-7 | SR 11-7 is a Federal Reserve issuance; OCC counterpart is Bulletin 2011-12 |
| OCC Heightened Standards | 12 CFR part 30, appendix D (OCC Heightened Standards) | OCC Heightened Standards | Formal citation required |
| FINRA supervision | FINRA Rule 3110 — supervisory systems and WSPs | FINRA Rule 3110 — access controls / records organization | Rule 3110 is about supervision, not direct access controls |
| SOX applicability | Sarbanes-Oxley §§302/404 — where applicable to ICFR | SOX 302/404 — blanket applicability | Only applies where AI tools affect financial reporting controls |
| SEC records retention | SEC Rule 17a-4 — required broker-dealer records only | SEC Rule 17a-4 — all Copilot artifacts | 17a-4 applies to specific required records, not all audit logs |

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

## Site Design System

The documentation site uses a unified FSI design system shared across all FSI-AgentGov and FSI-CopilotGov repositories.

- **Theme:** MkDocs Material with `primary: custom` / `accent: custom` palette
- **Colors:** Microsoft Blue (`#0078D4`) primary, WCAG AA teal (`#007A7E`) accent, full dark mode tokens in `docs/stylesheets/extra.css`
- **Logo:** Shield + circuit motif SVG (`docs/assets/logo.svg`, `docs/assets/favicon.svg`)
- **Homepage pattern:** Hero section → metrics strip → role cards → architecture diagram (uses `hide: navigation, toc` frontmatter, `md_in_html` extension, `attr_list` for buttons)
- **Navigation:** `navigation.sections` is intentionally removed so sidebar sections collapse by default
- **Font:** `font: false` — avoids Google Fonts CDN (blocked in FSI network environments)
- **Extensions required:** `pymdownx.emoji` (icon shortcodes), `md_in_html` (hero/cards), `pymdownx.highlight` (code blocks)

When modifying the site theme, update `docs/stylesheets/extra.css` — do not change `primary`/`accent` in `mkdocs.yml` (they must stay `custom`).
