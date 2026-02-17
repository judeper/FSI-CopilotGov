# FSI-CopilotGov

## What This Is

A comprehensive governance, compliance, and security documentation framework for Microsoft 365 Copilot deployment in US regulated financial services. Provides 54 controls across 4 lifecycle pillars with 216 implementation playbooks, strategic framework documents, regulatory mappings, and reference materials — published as a MkDocs site.

## Core Value

Financial institutions can deploy Microsoft 365 Copilot with confidence that every regulatory obligation (FINRA, SEC, OCC, FFIEC, SOX, GLBA) is addressed through documented, auditable controls with step-by-step implementation guidance.

## Requirements

### Validated

<!-- Shipped and confirmed valuable in v1.0. -->

- ✓ 54 control documents across 4 pillars (Readiness, Security, Compliance, Operations) — v1.0
- ✓ 216 control implementation playbooks (4 per control: portal walkthrough, PowerShell, verification, troubleshooting) — v1.0
- ✓ 9 strategic framework documents (executive summary, architecture, operating model, regulatory, adoption roadmap, surfaces, governance fundamentals, relationship-to-agentgov, index) — v1.0
- ✓ 11 reference documents (glossary, FAQ, regulatory mappings, license requirements, NIST AI RMF crosswalk, admin toggles, portal paths, surfaces matrix, FSI config examples, Microsoft Learn URLs, index) — v1.0
- ✓ Operational playbooks (governance operations, compliance & audit, incident & risk, getting started, regulatory modules) — v1.0
- ✓ Three-tier governance levels per control (Baseline / Recommended / Regulated) — v1.0
- ✓ Regulatory mapping coverage (FINRA 4511/3110/2210, SEC 17a-3/4, SOX, GLBA, OCC/SR 11-7, FFIEC) — v1.0
- ✓ MkDocs site with Material theme — v1.0
- ✓ CI validation scripts (control structure verification, language rules) — v1.0
- ✓ GitHub Actions workflows (docs publish, link check) — v1.0

### Active

<!-- Current scope. Building toward these in Review 01. -->

- [ ] Full quality review of all 54 controls and 216 playbooks
- [ ] Verify accuracy against Microsoft Learn (portal paths, cmdlets, feature names)
- [ ] Ensure internal consistency (terminology, formatting, structure)
- [ ] Deepen FSI-specific substance where content is generic/templated
- [ ] Strengthen regulatory citations across all regulators
- [ ] Add cross-linking (related controls, prerequisites, see-also references)
- [ ] Fix known broken links from MkDocs build

### Out of Scope

- Custom code/tooling — this is a documentation framework, not a software product
- Legal advice — framework is informational, not legal/compliance counsel
- Non-US regulatory frameworks — scoped to US FSI regulators only
- Copilot Studio / Agent Builder governance — covered by companion FSI-AgentGov repo

## Current Milestone: v1.1 Review 01

**Goal:** Comprehensive quality, regulatory, and structural review of every control and playbook in the framework.

**Target features:**
- Quality audit of all 54 controls and 216 playbooks (accuracy, depth, consistency)
- Microsoft Learn verification (portal paths, cmdlet names, feature availability)
- Regulatory citation strengthening across FINRA, SEC, OCC, FFIEC, and banking regulators
- Full cross-linking (related controls, prerequisites, see-also references)
- Broken link resolution and MkDocs navigation improvements

## Context

- Built as MkDocs documentation site using Material theme
- Published to GitHub Pages at judeper.github.io/FSI-CopilotGov
- Companion to FSI-AgentGov (Copilot Studio/agents governance) — standalone, no cross-dependencies
- 328 total files in repository (314 markdown, plus scripts, templates, CI configs)
- All CI checks passing (control structure verification, language rules)
- Initial commit landed as 9be2fa9 on master branch

## Constraints

- **Content type**: Documentation only — no application code
- **Regulatory accuracy**: All regulatory citations must be verifiable against source regulations
- **Language rules**: No promissory language (guarantees, ensures compliance, etc.) — CI enforced
- **Platform**: Microsoft 365 / Purview / Entra / Defender ecosystem only
- **Audience**: FSI IT administrators, compliance officers, CISOs, internal auditors

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| 4 pillars (Readiness/Security/Compliance/Operations) | Maps to M365 Copilot deployment lifecycle | ✓ Good |
| 4 playbooks per control (portal/PowerShell/verification/troubleshooting) | Covers both GUI and automated implementation paths | ✓ Good |
| Three-tier governance (Baseline/Recommended/Regulated) | Accommodates diverse FSI risk profiles | ✓ Good |
| Standalone from FSI-AgentGov | Different governance models (org-wide vs. zone-based) | ✓ Good |
| CI language enforcement | Prevents promissory/guarantee language in regulatory docs | ✓ Good |

---
*Last updated: 2026-02-17 after milestone v1.1 Review 01 started*
