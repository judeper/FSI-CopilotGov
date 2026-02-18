# Requirements: FSI-CopilotGov

**Defined:** 2026-02-17
**Core Value:** Financial institutions can deploy M365 Copilot with confidence that every regulatory obligation is addressed through documented, auditable controls with step-by-step implementation guidance.

## v1.1 Requirements

Requirements for Review 01 milestone. Each maps to roadmap phases.

### Global Corrections

- [x] **GLOB-01**: Replace "BizChat" with "Microsoft 365 Copilot Chat" across all 61 affected files (119 occurrences)
- [x] **GLOB-02**: Replace "M365 Chat" / "Microsoft 365 Chat" with "Microsoft 365 Copilot Chat" across 49 affected files
- [ ] **GLOB-03**: Correct SAM licensing in control 1.7 and license-requirements.md — SAM is included with Copilot licenses (currently states the opposite)

### Pillar 1 — Readiness

- [ ] **P1-01**: Update 1.1 to add Optimization Assessment as pre-deployment requirement and Office update channel governance
- [ ] **P1-02**: Update 1.2 to add DSPM unified experience (AI observability, item-level remediation, Purview Posture Agent, Shadow AI discovery)
- [ ] **P1-03**: Update 1.3 to document RCD as complementary tool to RSS with comparison table and SAM licensing note
- [ ] **P1-04**: Update 1.6 to add new RBAC roles (Purview Data Security AI Viewer, AI Content Viewer, AI Administrator from Entra)
- [ ] **P1-05**: Update 1.7 to correct SAM licensing and add Data Access Governance reports, Restricted Access Control
- [x] **P1-06**: Update 1.9 to add Frontline (F1/F3) SKU availability and pay-as-you-go licensing option

### Pillar 2 — Security

- [ ] **P2-01**: Update 2.1 to document two distinct DLP policy types (label-based + SIT-based prompt blocking), default DLP policy for Copilot, and Edge browser DLP
- [ ] **P2-02**: Update 2.2 to add label groups replacing parent labels, Copilot Studio agent label inheritance, auto-labeling nested rule logic
- [ ] **P2-03**: Update 2.3 to document CA "All resources" enforcement tightening (March 2026), verify Enterprise Copilot Platform app ID, add IRM-integrated dynamic blocking
- [x] **P2-04**: Update 2.4 to document Channel Agent in Teams NOT supporting Information Barriers with compensating controls
- [x] **P2-05**: Update 2.9 to add AI app catalog (400+ apps) and agent threat detection in XDR platform
- [ ] **P2-06**: Update 2.10 to add Risky Agents policy template (auto-deployed), AI usage indicator category, data risk graphs, IRM Triage Agent

### Pillar 3 — Compliance

- [ ] **P3-01**: Update 3.1 to add expanded audit schema (AgentId, AgentName, XPIA detection, JailbreakDetected, SensitivityLabelId), new RecordTypes (AgentAdminActivity, AgentSettingsAdminActivity), pay-as-you-go audit billing
- [ ] **P3-02**: Update 3.2 to add restructured retention locations (Microsoft Copilot experiences, Enterprise AI Apps, Other AI Apps), priority cleanup for AI-generated assets, threaded summaries retention
- [ ] **P3-03**: Update 3.3 to document unified eDiscovery experience migration (May 2025) and Feb 2026 UX simplification
- [ ] **P3-04**: Update 3.4 to add expanded Communication Compliance coverage (Security Copilot, Fabric Copilot, Copilot Studio) and IRM integration (CC indicators feeding insider risk)
- [ ] **P3-05**: Update 3.5 to add AI washing enforcement precedent (SEC v. Delphia/Global Predictions) and FINRA 2026 Oversight Report reference
- [ ] **P3-06**: Update 3.6 to add FINRA 2026 agentic AI supervision requirements, full-chain telemetry for decision reconstruction, SEC 2026 internal AI examination focus
- [ ] **P3-07**: Update 3.8 to add OCC Bulletin 2025-26 MRM proportionality for community banks and clarify Copilot's model status under SR 11-7
- [ ] **P3-08**: Update 3.10 to add Reg S-P amendment details (72-hour vendor notification, large/small entity compliance dates, mandatory incident response programs)
- [ ] **P3-09**: Update 3.11 to add SEC 17a-4 audit-trail alternative to WORM, off-channel communications enforcement context ($2B+ in fines), mobile Copilot recordkeeping

### Pillar 4 — Operations

- [ ] **P4-01**: Update 4.1 to add Copilot overview dashboard, Copilot Control System branding, portal consolidation into MAC, Copilot for Admins, Baseline Security Mode
- [ ] **P4-02**: Update 4.2 to document Teams Copilot default change from EnabledWithTranscript → Enabled (March 2026) with FSI recordkeeping impact analysis
- [ ] **P4-03**: Update 4.4 to add expanded Viva Copilot Chat insights and Engage→Teams integration
- [ ] **P4-04**: Update 4.8 to add pay-as-you-go billing model ($0.01/message) with governance controls and per-seat vs PAYG cost comparison

### Framework & Reference

- [ ] **FWRK-01**: Update regulatory-framework.md to add FINRA 2026 Report, SEC 2026 exam priorities, Fed reputational risk removal, OCC 2025-26, Colorado AI Act date correction (Feb→June 2026)
- [ ] **FWRK-02**: Update regulatory-mappings.md to add 7 new regulatory citations
- [ ] **FWRK-03**: Update license-requirements.md to correct SAM licensing, add pay-as-you-go, add Frontline SKUs
- [ ] **FWRK-04**: Verify and update microsoft-learn-urls.md for namespace migration (/copilot/, /purview/ paths)
- [ ] **FWRK-05**: Update copilot-architecture.md to reflect Copilot Control System, Agent 365, Entra Agent ID

### Playbook & Cross-linking

- [ ] **PLAY-01**: Update 4 PnP PowerShell playbooks (1.2, 1.6, 1.8, 2.2) to add custom Entra app registration requirement
- [ ] **PLAY-02**: Verify all 12 Exchange Online playbooks use REST-only patterns (no legacy RPS)
- [ ] **PLAY-03**: Update portal walkthrough playbooks for controls with changed admin paths
- [ ] **PLAY-04**: Add cross-linking (related controls, prerequisites, see-also references) across all control documents

## Future Requirements

### v1.2 — Agent Governance Expansion

- **AGENT-01**: Add dedicated agent governance section (Agent 365 control plane, agent lifecycle, MCP server governance)
- **AGENT-02**: Add Entra Agent ID documentation (non-human identity governance)
- **AGENT-03**: Add agent-specific playbooks (agent approval workflows, ownership reassignment, policy-driven lifecycle)
- **AGENT-04**: Add content safety exception governance for specialized roles (legal/investigative)
- **AGENT-05**: Add Copilot in Edge (Copilot Mode + Agent Mode) browser governance

## Out of Scope

| Feature | Reason |
|---------|--------|
| Agent governance controls (new sections) | Deferred to v1.2 — requires architectural decision on CopilotGov vs AgentGov scope boundary |
| MCP server governance | Deferred to v1.2 — Frontier program feature, not yet GA |
| Copilot in Edge governance | Deferred to v1.2 — browser DLP is new surface requiring new control design |
| Content safety exceptions | Deferred to v1.2 — requires FSI-specific exception approval framework design |
| Full MkDocs navigation overhaul | User scoped to cross-linking, not full nav restructure |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| GLOB-01 | Phase 2 | Complete (02-01 through 02-05: all files corrected, zero BizChat remaining, verified 2026-02-17) |
| GLOB-02 | Phase 2 | Complete (02-01 through 02-05: all files corrected, zero M365 Chat/Microsoft 365 Chat remaining, verified 2026-02-17) |
| GLOB-03 | Phase 5 | Pending |
| P1-01 | Phase 3 | Pending |
| P1-02 | Phase 3 | Pending |
| P1-03 | Phase 3 | Pending |
| P1-04 | Phase 3 | Pending |
| P1-05 | Phase 3 | Pending |
| P1-06 | Phase 3 | Complete |
| P2-01 | Phase 3 | Pending |
| P2-02 | Phase 3 | Pending |
| P2-03 | Phase 3 | Pending |
| P2-04 | Phase 3 | Complete |
| P2-05 | Phase 3 | Complete |
| P2-06 | Phase 3 | Pending |
| P3-01 | Phase 4 | Pending |
| P3-02 | Phase 4 | Pending |
| P3-03 | Phase 4 | Pending |
| P3-04 | Phase 4 | Pending |
| P3-05 | Phase 4 | Pending |
| P3-06 | Phase 4 | Pending |
| P3-07 | Phase 4 | Pending |
| P3-08 | Phase 4 | Pending |
| P3-09 | Phase 4 | Pending |
| P4-01 | Phase 4 | Pending |
| P4-02 | Phase 4 | Pending |
| P4-03 | Phase 4 | Pending |
| P4-04 | Phase 4 | Pending |
| FWRK-01 | Phase 5 | Pending |
| FWRK-02 | Phase 5 | Pending |
| FWRK-03 | Phase 5 | Pending |
| FWRK-04 | Phase 5 | Pending |
| FWRK-05 | Phase 5 | Pending |
| PLAY-01 | Phase 6 | Pending |
| PLAY-02 | Phase 6 | Pending |
| PLAY-03 | Phase 6 | Pending |
| PLAY-04 | Phase 6 | Pending |

**Coverage:**
- v1.1 requirements: 34 total
- Mapped to phases: 34
- Unmapped: 0 ✓

---
*Requirements defined: 2026-02-17*
*Last updated: 2026-02-17 — GLOB-01/02 marked Complete after 02-05 verification pass (zero deprecated terms across all docs/)*
