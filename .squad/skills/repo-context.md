# FSI-CopilotGov — Repo Context for OceanSquad Agents

## Overview
- **Repo:** `judeper/FSI-CopilotGov` (public, GitHub Pages)
- **Site:** https://judeper.github.io/FSI-CopilotGov/
- **Framework:** FSI Copilot Governance Framework — 62 controls across 4 pillars
- **Current version:** Check `docs/reference/release-notes-v1.4.md` for latest

## Pillars
1. **Readiness** (`docs/controls/pillar-1-readiness/`) — deployment preparation, licensing, tenant config
2. **Security** (`docs/controls/pillar-2-security/`) — DLP, encryption, access control, sensitivity labels
3. **Compliance** (`docs/controls/pillar-3-compliance/`) — regulatory alignment, eDiscovery, retention, audit
4. **Operations** (`docs/controls/pillar-4-operations/`) — monitoring, incident response, change management

## Architecture
- **Docs layer** (`docs/`) — MkDocs Material site with controls, playbooks, framework, reference
- **Assessment engine** (`assessment/engine/`) — Python scorer (manifest + evidence → reports)
- **Collectors** (`assessment/collectors/`) — PowerShell scripts for Graph, Purview, SharePoint, Sentinel
- **Manifest** (`assessment/manifest/controls.json`) — canonical control metadata, schema-validated
- **SPA** (`docs/javascripts/assessment-app.js`) — browser-based Governance Scorecard
- **Monitoring** (`scripts/learn_monitor.py`, `scripts/regulatory_monitor.py`) — scheduled drift detection

## Control Document Structure (10 sections)
Every control doc under `docs/controls/` follows a strict 10-section template:
1. Control Statement
2. Why It Matters in FSI
3. Key Risks Addressed
4. Implementation Approaches
5. Microsoft Technology Mapping
6. Regulatory Alignment
7. Implementation Considerations
8. Related Controls
9. Summary
10. Version footer with Last Verified date

## Key Validation Commands
```bash
# Docs
mkdocs build --strict

# Content validation
python scripts/verify_controls.py
python scripts/verify_language_rules.py
python scripts/verify_excel_templates.py

# Manifest pipeline
python assessment/manifest/generate_manifest.py
python scripts/harvest_manifest_extension.py
python scripts/merge_authored_content.py
python scripts/validate_manifest.py --strict --allow-todo

# Solutions integration
python scripts/check_solutions_drift.py --mode=ci

# Tests
python -m pytest assessment/tests scripts -q
npm install && npm test

# Full local gate sweep
python scripts/verify_controls.py && \
  python scripts/verify_language_rules.py && \
  python scripts/validate_manifest.py --strict --allow-todo && \
  python scripts/check_solutions_drift.py --mode=ci && \
  mkdocs build --strict && \
  npm test && \
  python -m pytest assessment/tests scripts -q
```

## Language Rules (MANDATORY)
See `.github/instructions/fsi-language-rules.instructions.md`. Key rules:
- Never say "ensure" — use "verify", "confirm", "validate"
- Never say "utilize" — use "use"
- Never say "in order to" — use "to"
- Never use "simply" or "just" — remove entirely
- Use present tense, active voice
- Cite specific Microsoft service names, not generic terms

## Playbooks
Each control has implementation playbooks under `docs/playbooks/control-implementations/{control-id}/`.

## Sister Repo
`judeper/FSI-CopilotGov-Solutions` — solutions catalog pinned in `assessment/data/solutions-lock.json`.
Drift is guarded by `scripts/check_solutions_drift.py`.
