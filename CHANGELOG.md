# Changelog

All notable changes to the FSI Copilot Governance Framework are documented in this file.

---

## [Unreleased]

### Fixed
- **Drift correction:** `docs/index.md` now reports 243 playbooks (was 224). The framework actually publishes 225 control-implementation playbooks plus 18 cross-cutting playbooks (e.g., governance-operations, regulatory-modules) for a total of 243.
- **Citation remediation (regulator escalation):** Replaced rescinded/incorrect regulatory citations across multiple control and reference pages.
  - `controls/pillar-2-security/2.16-federated-connector-mcp-governance.md` — replaced 3 occurrences of rescinded **OCC Bulletin 2013-29** with current **OCC Bulletin 2023-17 (Third-Party Relationships: Risk Management)**.
  - `controls/pillar-4-operations/4.13-extensibility-governance.md` and `reference/fsi-use-case-risk-scenarios.md` and `playbooks/regulatory-modules/state-ai-laws-compliance-matrix.md` — corrected "OCC SR 11-7" attributions to the canonical paired citation **SR 11-7 / OCC Bulletin 2011-12** (SR 11-7 is a Federal Reserve issuance; OCC Bulletin 2011-12 is the OCC counterpart).
  - `playbooks/control-implementations/3.10/portal-walkthrough.md` and `verification-testing.md` — replaced "FTC Safeguards Rule" line items with the correct authority **GLBA §501(b)**. Reg S-P (SEC Rule 248.30) implements GLBA §501(b) for SEC-regulated broker-dealers; the FTC Safeguards Rule is a separate implementing regulation that applies only to FTC-jurisdiction institutions and is not the operative authority for SEC-regulated entities.
- **Dead URL:** `controls/pillar-3-compliance/3.8-model-risk-management.md` — replaced the dead Federal Reserve `sr1107.htm` URL with the live **SR 26-2** URL.

### Added
- **Regulatory update notice on Control 3.8 (Model Risk Management):** A prominent callout at the top of the control documents that on **April 17, 2026**, Federal Reserve / OCC / FDIC jointly issued **SR 26-2** and **OCC Bulletin 2026-13** (*Revised Guidance on Model Risk Management*), which supersede SR 11-7 / OCC Bulletin 2011-12. The revised interagency guidance **explicitly excludes generative and agentic AI models pending further regulatory consideration**. Because Microsoft 365 Copilot is a generative AI system, the operative MRM expectations for Copilot remain undefined under the revised framework; this control therefore continues to map to the SR 11-7 / OCC Bulletin 2011-12 principles as the most recent applicable guidance, supplemented by institution-specific policy. Organizations should monitor for forthcoming agency guidance on generative AI MRM.

### Notes
- Acknowledgement: the headline-counts drift (56/57/58 controls; 224/228/243 playbooks across README, AGENTS, and index pages) is a recurring class of issue caused by hand-typed metadata. A canonical content graph (Phase U.D.3-lite) is planned to render counts from a single source.
- A broader citation modernization sweep (replacing all SR 11-7 / OCC 2011-12 references with paired SR 26-2 / OCC 2026-13 citations) is **deferred** pending decision on whether to update the project's regulatory-citation canon (AGENTS.md). Tracked in session plan files.

---

## v1.4.0 — 2026-04-21

Major feature port from FSI-AgentGov bringing governance assessment parity for M365 Copilot.

### Added
- Manifest-driven assessment engine with Python scoring and YAML collectors (Phase B)
- Evidence drawer with verifyIn links and persistent notes (Phase D1)
- Facilitator mode with per-control ask/followUp prompts (Phase D1)
- Sector-calibration yes-bars per tier (Phase D1)
- Solution recommendation cards referencing FSI-CopilotGov-Solutions@v0.1.0-rc1 (Phase C2/D1)
- Collector evidence import (CSV/JSON drop) (Phase D2)
- Portal export envelope schema v0.1.0 (Phase E)
- Solutions catalog view with reverse-lookup and filters (Phase C3)
- Pre-session homework pages for 14 curated FSI roles (Phase F)
- Role-specific Excel checklists and governance dashboard (Phase G)
- Microsoft Learn URL monitoring (Phase I1)
- Regulatory monitoring (Federal Register + FINRA) (Phase I1)
- Solutions drift detection with weekly CI (Phase C4)
- Vitest harness with 60+ SPA tests across 11 files (Phase H1/H2)

### Changed
- Manifest validator accepts object-shaped solutions entries
- `merge_authored_content.py` now treats `solutions` as a replace-only field

### Reference
- [Phased rollout](docs/getting-started/phased-rollout.md)
- [Homework pages](docs/getting-started/homework-quickstart.md)

---

## v1.3.4 — 2026-04-17

### New Control, Playbooks, and Reference Content

- **2.16** Federated Copilot Connector and MCP Governance — new Baseline control for governing default-enabled federated connectors, user-credential authentication, data residency, and third-party risk (57 → 58 controls, Pillar 2: 15 → 16 controls)

#### New Playbooks
- **Agent Behavioral Incident Playbook** — incident response procedures for agent misuse, prompt injection, and runaway behavior
- **Teams Copilot Mode Governance** — governance playbook for Teams Copilot Mode group chat, covering FINRA 3110/4511, WSPs, retention, and communications compliance
- **State AI Laws Compliance Matrix** — regulatory module mapping Colorado, Texas, Utah, and Illinois AI laws to framework controls

#### New Reference Content
- **FSI Use Case Risk Scenarios** — risk matrix by use case (AML, client communications, research, financial reporting, meetings) with control mappings

#### Documentation Updates
- Updated control count from 57 to 58 across homepage, README, and AI instruction files
- Added Copilot surface coverage and playbook backlinks to multiple Pillar 2–4 controls
- Updated `docs/reference/copilot-surfaces-matrix.md` with new surface coverage entries

---

## v1.3.3 — 2026-04-15

### AI Council Deep Review — All 57 Controls

Comprehensive review of all 57 controls across 4 pillars using a multi-agent AI Council (GPT 5.4). Each control was reviewed for technical accuracy, regulatory accuracy, structural compliance, FSI language rules, and cross-reference integrity. Disagreements between council members were resolved through targeted research against authoritative sources.

**246 files changed, 458 insertions, 246 deletions across 12 commits.**

#### Critical Regulatory Corrections
- **1.1** Copilot Readiness Assessment — "Interagency AI Guidance (2023)" was misattributed; OCC Bulletin 2023-17 is about third-party risk management, not AI. Replaced with SR 11-7 / OCC Bulletin 2011-12 (model risk) and OCC Bulletin 2023-17 (third-party risk)
- **3.10** SEC Reg S-P Privacy — 72-hour breach notification direction was reversed; service providers must notify the firm, not the other way around
- **3.9** AI Disclosure & Transparency — SEC Marketing Rule was incorrectly described as prohibiting testimonials; it permits them with conditions and disclosures
- **1.5** Sensitivity Label Taxonomy — Copilot label inheritance was claimed as universal; behavior varies by workload

#### Recurring Pattern Fixes (All 57 Controls)
- **GLBA Safeguards Rule** → GLBA §501(b) — FTC Safeguards Rule applies to non-bank institutions only; bank/broker-dealer contexts require GLBA §501(b) and sector-specific implementing guidelines
- **OCC Bulletin 2013-29** → OCC Bulletin 2023-17 — 2013-29 was rescinded/superseded by 2023-17
- **OCC Heightened Standards** → 12 CFR part 30, appendix D (OCC Heightened Standards) — formal regulatory citation
- **FINRA Rule 3110** descriptions corrected — supervision rule for supervisory systems/WSPs, not a direct access-control or records-organization mandate
- **SOX 302/404** claims narrowed to ICFR-relevant scope
- **SR 11-7** dual citation — Federal Reserve SR 11-7 / OCC Bulletin 2011-12 (not "OCC SR 11-7")
- **Admin role names** standardized to canonical short forms across all playbooks (Entra Global Admin, SharePoint Admin, Purview Compliance Admin)
- **`Request-SPOReIndex`** replaced — not a valid SPO Management Shell cmdlet; replaced with PnP PowerShell `Invoke-PnPSiteSearchReindex`

#### Technical Accuracy Fixes
- **1.2** Fix `Register-PnPEntraIDAppForInteractiveLogin` invalid `-Interactive` parameter
- **1.2** Fix `$global:PnPConnection.Timeout` → `Connect-PnPOnline -RequestTimeout`
- **1.3** Fix RSS mode return value (`Restricted` → `Enabled`); fix RCD portal label
- **1.4** Fix Bookmarks/Acronyms admin path (Search & intelligence, not Copilot > Search)
- **1.5** Remove invalid `Get-MgReportSecurity` cmdlet; replace deprecated AIP unified labeling client
- **1.6** Fix hub site permissions claim (hub association does not inherit permissions)
- **1.8** Fix `-IncludePersonalSite` parameter (`$false` → `Exclude`)
- **2.3** Fix Adaptive Protection CA condition (`User risk` → `Insider risk`)
- **2.8** Fix PowerShell syntax error (`Get-DataEncryptionPolicy-ErrorAction`)
- **3.13** Remove invalid `Get-UnifiedAuditLogRetentionPolicy` cmdlet
- **4.11** Fix Sentinel connector name (`Microsoft 365` → `Office 365`)
- Multiple admin portal path corrections (SharePoint DAG, Copilot Security, Intune update channels)

#### Structural Improvements
- ~216 playbook backlinks added to parent control files across all 4 pillars
- Broken `**Related Controls:**[` formatting fixed in 11 Pillar 4 control files
- Plain text cross-references converted to markdown links across multiple playbooks

#### AI Instruction Updates
- Added regulatory citation conventions to `.github/copilot-instructions.md`
- Added regulatory accuracy rules to `.github/instructions/fsi-language-rules.instructions.md`

---

## v1.3.2 — 2026-04-14

### Microsoft Secure and Govern Blueprint Alignment

Aligned documentation with Microsoft's [Secure and Govern Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance) deployment blueprint (published 2026-04-09).

#### Content Updates
- **1.2** SharePoint Oversharing Detection — aligned "oversharing assessment" terminology with Microsoft's canonical "data risk assessments" term
- **1.7** SharePoint Advanced Management — expanded SharePoint Admin Agent (Content Governance Agent) with Copilot governance capabilities; added SAM Content Management Assessment section; added Microsoft 365 Archive to SAM feature table
- **2.2** Sensitivity Labels — added Purview "Secure by Default" label derivation model (site-to-file label inheritance) with FSI scale considerations; added sensitivity labels for Teams/Groups/sites reference
- **3.2** Data Retention — added Microsoft 365 Archive for inactive content section with FSI regulatory preservation use case
- **3.12** Evidence Collection — expanded Compliance Manager AI governance guidance with improvement actions, remediation tracking workflow, and framework integration

#### Architecture
- **copilot-architecture.md** — added Microsoft Secure and Govern blueprint cross-reference with 3-pillar summary (Remediate Oversharing, Set Up Guardrails, Meet Regulations)

#### Reference Updates
- Added 18 new Microsoft Learn URLs across 8 sections (blueprint, DSPM, Compliance Manager, M365 Archive, SharePoint Admin Agent, eDiscovery, site sensitivity labels, Secure by Default)
- Added new Compliance Manager and Microsoft 365 Archive URL sections

#### AI Instruction Updates
- Fixed control count (56 → 57) in `.github/copilot-instructions.md`
- Added DSPM, Compliance Manager, SAM, and M365 Archive to platform areas

---

## v1.3.1 — 2026-04-09

### New Controls
- **1.16** Copilot Tuning Governance — new control for governing fine-tuned AI agents (5,000+ license orgs), covering data selection, audit trails, output supervision, and data residency (56 → 57 controls, Pillar 1: 15 → 16 controls)

### Feature Gap Remediation (7 High-Priority)
- **2.6** Web Search Controls — added domain exclusion for web grounding (block specific domains from Copilot responses)
- **1.4** Semantic Index Governance — added authoritative sources management (designate up to 100 SharePoint sites via admin center)
- **1.7** SharePoint Advanced Management — added Agent insight report (GA), Catalog management (Preview), SharePoint Admin Agent (Preview)
- **4.1** Admin Settings — added Baseline Security Mode (BSM, 18-20 settings, simulation mode) and expanded Entra AI Administrator with dedicated homepage
- **2.14** Declarative Agents Governance — added agent pinning controls (up to 3 agents per user, admin-enforced)
- **2.1** DLP Policies — made prompt-level DLP policy location explicit (Roadmap 548671, Public Preview March 2026, GA June 2026)
- **3.11** Record Keeping — added Cohasset Associates December 2024 compliance assessment reference (SEC 17a-4, FINRA 4511, CFTC 1.31)

### Feature Gap Remediation (5 Moderate)
- **4.5** Usage Analytics — added Copilot Dashboard satisfaction/intent metrics and high-usage user identification
- **4.8** Cost Allocation — added high-usage user monitoring and message pack tracking for PAYG governance
- **1.11** Change Management — added organizational branded footer for M365 Copilot app as user trust mechanism
- **1.8** Information Architecture — added AI in SharePoint (Knowledge Agent) advisory with security implications for metadata extraction
- **README** — added governance boundary clarification (CopilotGov vs AgentGov scope)

### Reference Updates
- Updated glossary with 5 new terms (AI in SharePoint, Authoritative Sources, Baseline Security Mode, Copilot Tuning, Domain Exclusion)
- Updated admin toggles with domain exclusion, BSM, and agent pinning controls
- Updated Microsoft Learn URLs with 7 new entries across 4 sections

---

## v1.3 — 2026-04-09

### Critical — Copilot Licensing Changes (April 15, 2026)
- Added Copilot Chat Basic vs Premium tier distinction across license requirements, Control 1.9, admin toggles, FAQ, glossary, and getting-started content
- Documented April 15, 2026 deadline: organizations >2,000 users lose embedded Copilot Chat in Word, Excel, PowerPoint, OneNote for unlicensed users
- Added Edit with Copilot (Agent Mode) governance — available to all M365 users regardless of license, web data only for unlicensed users
- Added third-party model provider support (Anthropic Claude, xAI) and recommended FSI posture (disabled by default)

### Platform & Architecture Updates
- Added **Agent 365** platform — centralized agent monitoring, management, and configuration across M365 apps, Copilot Studio, and third-party integrations
- Added **Entra Agent ID** — unique agent identities in Entra ID for security tracking, policy enforcement, and audit trails
- Added **Work IQ** — persistent organizational memory for prioritized and personalized Copilot assistance
- Added **Copilot Cowork** — multi-step business task delegation with user monitoring and intervention
- Added **Researcher** and **Analyst** as distinct Copilot Chat experiences to surfaces documentation
- Updated Copilot architecture diagram and surfaces matrix with Basic vs Premium access distinction
- Added Copilot security pivot in M365 Admin Center for data access policy creation

### Control Updates (Pillar 1 — Readiness & Assessment)
- **1.9** License Planning — added Copilot Chat Basic/Premium planning, Edit with Copilot governance gap, third-party model provider assessment
- **1.13** Extensibility Readiness — added Agent 365 platform assessment, Entra Agent ID readiness, third-party model provider readiness

### Control Updates (Pillar 2 — Security & Protection)
- **2.1** DLP Policies — added Mac endpoint DLP expansion (~40→100+ file types), adaptive scoping for SharePoint, AI-powered policy explanations via Security Copilot, web-grounding DLP restrictions
- **2.2** Sensitivity Labels — added auto-labeling override for files (April 2026), permission level renames (Reviewer→Restricted Editor, Co-author→Editor), default labeling for Teams meetings
- **2.10** Insider Risk — added content preview in IRM alerts, enhanced Copilot risky AI usage indicators
- **2.11** Copilot Pages Security — added Information Barriers NOT supported for SharePoint Embedded (critical for FSI Chinese wall requirements), Notebook sensitivity labeling limitations, departed user workflow, recycle bin status, group-owned workspace policy
- **2.14** Declarative Agents Governance — added Agent 365 governance surface, Entra Agent ID security controls, third-party model provider risk factors

### Control Updates (Pillar 3 — Compliance & Audit)
- **3.2** Data Retention — added Copilot Notebooks deletion bug (MC1213768) with workaround, retention via All SharePoint Sites scope, bulk/manual label limitations
- **3.3** eDiscovery — added unified Purview eDiscovery portal transition (classic Content Search retirement), deprecated export PowerShell cmdlets, case-centric access model
- **3.4** Communication Compliance — added content preview in IRM alerts, case creation without content, PAYG AI indicators, multicloud coverage (Azure, Fabric, third-party)

### Control Updates (Pillar 4 — Operations & Monitoring)
- **4.1** Admin Settings — added Agent 365 admin surface, third-party model provider toggles, Copilot security pivot
- **4.13** Extensibility Governance — added Agent 365 operational governance procedures with cadences, agent inventory dashboards, usage reporting

### Framework Updates
- Updated executive summary with Agent 365, third-party models, and Basic/Premium licensing considerations
- Updated regulatory framework with EU AI Act compliance tracking references and Agent 365/Entra Agent ID audit capabilities
- Updated governance fundamentals with Agent 365 governance surface and Basic/Premium governance model
- Updated adoption roadmap with Agent Mode rollout milestone, April 15 licensing deadline, and Agent 365 adoption steps

### Reference Updates
- Updated Microsoft Learn URLs reference — added 9 new URLs across 2 new sections (Agent Governance, Copilot Pages and Notebooks) and 2 existing sections; all 220 existing URLs validated (0 broken)
- Updated glossary with 10 new terms (Agent 365, Copilot Chat Basic/Premium, Copilot Cowork, Edit with Copilot, Entra Agent ID, Work IQ, Editor/Restricted Editor)
- Updated FAQ with 4 new entries (Basic vs Premium, Edit with Copilot licensing, third-party models, Information Barriers limitations)
- Updated portal paths quick reference with Agent 365, third-party model, and Copilot security paths
- Updated admin toggles with third-party model provider controls and Edit with Copilot row
- Updated license requirements with Basic/Premium tiers and third-party model providers

### Playbook Updates
- Updated eDiscovery playbooks (3.3) — unified portal transition, deprecated cmdlets, case-centric access
- Updated DLP playbooks (2.1) — Mac file types, adaptive scoping, AI-powered explanations
- Updated sensitivity labels playbooks (2.2) — auto-labeling overrides, permission renames, Teams meeting labels
- Updated Copilot Pages playbooks (2.11) — IB limitations, departed user workflow, Notebook labeling
- Updated agent governance playbooks (2.14) — Agent 365, Entra Agent ID, third-party models
- Updated getting-started checklist and quick-start guide with licensing, Agent 365, and third-party model items

### Metadata
- Updated all modified control `Last Verified:` dates to `2026-04-09`
- Updated version stamps across 84 files from `v1.2.1` to `v1.3`
- Validated all Microsoft Learn URLs (220 unique, 0 broken, 0 errors)

---

## v1.2.1 — 2026-03-17

### New Controls (Pillar 1 — Readiness & Assessment)
- **1.14** Item-Level Permission Scanning — new control for scanning and governing item-level permissions before Copilot deployment
- **1.15** SharePoint Permissions Drift Detection — new control for detecting and remediating permissions drift in SharePoint sites exposed to Copilot

### Metadata Updates
- Updated control and pillar counts across README and instruction files (54 → 56 controls, Pillar 1: 13 → 15 controls)

---

## v1.2 — March 2026

### Content Quality Improvements
- Enriched Governance Levels sections in 12 controls with specific portal paths, PowerShell cmdlets, configuration values, and regulatory thresholds (2.10, 3.1, 3.2, 3.6, 3.8, 3.10, 3.11, 3.13, 4.2, 4.3, 4.4, 4.8)
- Rewrote 6 thin PowerShell playbooks with real cmdlets replacing pseudo-code (3.7, 3.8, 3.9, 4.3, 4.7, 4.12)
- Improved 6 moderate PowerShell playbooks — replaced hardcoded data with parameterized scripts (2.11, 3.12, 3.13, 4.6, 4.9, 4.10)

### Research-Backed Updates
- Added Copilot-specific UAL RecordTypes and operations (CopilotInteraction, TeamCopilotInteraction, AgentAdminActivity) to audit logging controls and playbooks
- Added IRM "Risky AI usage (preview)" template and Generative AI indicators to insider risk control
- Added amended SEC Reg S-P timeline (Dec 3, 2025 compliance deadline) and 72-hour vendor notification details
- Added OCC Bulletin 2025-26 proportionality principle to model risk management control
- Added FFIEC AIO (2021) booklet examination procedures and examiner documentation request checklist
- Added Teams meeting default change (MC1139493, September 2025) to Teams meetings governance
- Added PAYG billing model details ($0.01/message) and Graph API usage endpoints to cost allocation control
- Added Viva Copilot per-app features and portal-only limitation documentation

### CI and Validation
- Fixed pre-existing FSI language rule violation in Control 4.2 ("guarantees" → "requires")
- Added FINRA 2210 control and playbooks to language rule scanner exemptions (intentional prohibited phrase examples)
- Added `.github/copilot-instructions.md` for Copilot session context

---

## v1.1 — February 2026

### Framework Updates
- Added FINRA 2026 agentic AI supervision guidance to regulatory framework
- Added SEC 2026 examination priorities (internal AI tool focus)
- Added OCC Bulletin 2025-26 MRM proportionality guidance
- Added SEC v. Delphia/Global Predictions enforcement precedent
- Fixed Colorado AI Act effective date to June 2026 (SB 25B-004 amendment)
- Added Copilot Control System section to architecture documentation
- Verified all Microsoft Learn URLs use current namespaces

### Control Updates (Pillar 3 — Compliance & Audit)
- **3.1** Copilot Audit Logging — restructured retention locations, threaded summaries
- **3.2** Data Retention Policies — updated retention location coverage
- **3.3** eDiscovery — unified experience update, enhanced Copilot content search
- **3.4** Communication Compliance — IRM integration, expanded Copilot surface coverage
- **3.5** FINRA 2210 — SEC v. Delphia enforcement precedent, AI disclosure requirements
- **3.6** Supervision and Oversight — FINRA 2026 agentic AI supervision, SEC 2026 exam focus
- **3.8** Model Risk Management — OCC Bulletin 2025-26 proportionality principle
- **3.10** SEC Reg S-P Privacy — 72-hour vendor notification requirement
- **3.11** Record Keeping — 17a-4(f)(2)(ii)(A) audit-trail alternative, off-channel enforcement

### Control Updates (Pillar 4 — Operations & Monitoring)
- **4.1** Admin Settings — Copilot Control System branding, Baseline Security Mode
- **4.2** Teams Meetings Governance — default Copilot behavior change (effective March 2026)
- **4.4** Viva Suite Governance — Copilot Chat insights, Engage-to-Teams migration
- **4.8** Cost Allocation — PAYG billing model ($0.01/message), budget cap governance

### Reference Updates
- Updated regulatory mappings with 7 new citations from Phase 3-4 controls
- Updated license requirements: SAM included with Copilot licenses, PAYG option, Frontline SKU availability
- Added cross-pillar Related Controls links to all 54 control documents

### Navigation and Build Fixes
- Rebuilt implementation checklist with correct control taxonomy (all 56 controls)
- Updated quick-start guide control references and playbook links
- Populated Pillar 3 and 4 playbook index tables (replacing "Coming soon" stubs)
- Fixed broken cross-references in playbook troubleshooting guides
- Fixed pillar deep-links in playbooks overview

### Repository Hygiene
- Added .gitignore for build artifacts, planning files, and research documents
- Removed internal planning artifacts from git tracking

---

## v1.0 — February 2026

### Initial Release
- 54 governance controls across 4 lifecycle pillars (Readiness, Security, Compliance, Operations)
- 216 implementation playbooks (portal walkthrough, PowerShell setup, verification, troubleshooting per control)
- 9 framework documents (executive summary, architecture, regulatory framework, operating model, adoption roadmap)
- 11 reference documents (regulatory mappings, license requirements, admin toggles, glossary, FAQ)
- MkDocs Material site with search, dark/light mode, and structured navigation
- Coverage for 12+ US financial regulations (FINRA, SEC, OCC, FFIEC, CFPB, GLBA, SOX)
