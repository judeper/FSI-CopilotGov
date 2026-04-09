# Changelog

All notable changes to the FSI Copilot Governance Framework are documented in this file.

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
