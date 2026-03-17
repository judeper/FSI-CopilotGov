# Changelog

All notable changes to the FSI Copilot Governance Framework are documented in this file.

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
