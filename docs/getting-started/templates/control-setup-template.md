# Control Setup Template

Use this template to document the configuration of a single control across its
three governance tiers. Keep one page per control in your internal governance
tracker; the format here matches the role-specific Excel checklists generated
by `scripts/build_checklist_templates.py`.

!!! note "FSI language rules"
    This framework is provided for informational purposes only and does not
    constitute legal, regulatory, or compliance advice. Use "supports
    compliance with" and "helps meet" — not "ensures compliance" or
    "guarantees". See the [full disclaimer](../../disclaimer.md).

---

## Control identification

| Field | Value |
|-------|-------|
| Control ID | *e.g. 2.1* |
| Control name | *e.g. DLP Policies for Microsoft 365 Copilot Interactions* |
| Pillar | *1 Readiness / 2 Security / 3 Compliance / 4 Operations* |
| Surface(s) | *e.g. Copilot Chat; Pages; Declarative Agents* |
| Owner (accountable) | *role or named individual* |
| Contributors (consulted) | *roles / teams* |
| Last reviewed | *YYYY-MM-DD* |

---

## Objective

> Summarise what the control aims to achieve in the organization's Copilot
> deployment, in one or two sentences. Reference specific regulations by name
> and section where applicable (e.g. "supports compliance with FINRA Rule
> 4511(a)").

---

## Configuration by governance tier

### Baseline

| Item | Value / Setting | Evidence location |
|------|-----------------|-------------------|
| *Setting 1* | *value* | *link, screenshot path, report ID* |
| *Setting 2* | *value* | *…* |

**Implementation notes:** *…*

### Recommended

| Item | Value / Setting | Evidence location |
|------|-----------------|-------------------|
| *Setting 1* | *value* | *…* |

**Implementation notes:** *…*

### Regulated

| Item | Value / Setting | Evidence location |
|------|-----------------|-------------------|
| *Setting 1* | *value* | *…* |

**Implementation notes:** *…*

---

## Verification steps

1. *How the control is verified — portal report, PowerShell check, audit log
   query, etc.*
2. *Cadence (daily / weekly / quarterly).*
3. *Who signs off on the evidence.*

---

## Evidence register

| Date | Evidence artifact | Stored at | Reviewer |
|------|-------------------|-----------|----------|
| *YYYY-MM-DD* | *screenshot / report / export* | *path or link* | *name* |

---

## Related controls and playbooks

- *Control X.Y — short description of dependency*
- *Playbook link — `playbooks/control-implementations/<id>/...`*

---

*Organizations should verify that documented values meet their specific
regulatory obligations. This template aids in maintaining examination-ready
records; it does not itself establish compliance.*
