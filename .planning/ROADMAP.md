# Roadmap: FSI-CopilotGov

## Milestones

- ✅ **v1.0 Initial Framework** - Phase 1 (shipped 2026-02-17)
- 🚧 **v1.1 Review 01** - Phases 2-6 (in progress)

## Phases

<details>
<summary>✅ v1.0 Initial Framework (Phase 1) - SHIPPED 2026-02-17</summary>

### Phase 1: Initial Framework
**Goal**: Complete governance framework published as a MkDocs site
**Plans**: 1 plan (bulk initial build — commit 9be2fa9)

Plans:
- [x] 01-01: Build 54 controls, 216 playbooks, 9 framework docs, 11 reference docs, CI, GitHub Actions

</details>

---

### 🚧 v1.1 Review 01 (In Progress)

**Milestone Goal:** Comprehensive quality, regulatory, and structural review of every control and playbook — correcting naming, deepening FSI substance, updating regulatory citations, and adding cross-linking across all 314 markdown files.

## Phase Details

### Phase 2: Global Naming Corrections
**Goal**: All 314 markdown files use correct Microsoft product terminology throughout
**Depends on**: Phase 1
**Requirements**: GLOB-01, GLOB-02
**Success Criteria** (what must be TRUE):
  1. The string "BizChat" does not appear in any documentation file (docs/ or README.md)
  2. The strings "M365 Chat" and "Microsoft 365 Chat" (standalone, not as part of "Microsoft 365 Copilot Chat") do not appear in any documentation file
  3. All affected files use "Microsoft 365 Copilot Chat" for the free/seeded experience and "Microsoft 365 Copilot" for the licensed experience, with correct shortened forms after first mention
  4. No documentation file contains "Azure Active Directory", "Azure AD" (standalone), "O365", "compliance.microsoft.com", "Microsoft Purview compliance portal", "Security & Compliance Center", or "Microsoft 365 Defender"
  5. MkDocs build completes without new broken reference warnings introduced by the renames
**Plans**: 6 plans

Plans:
- [x] 02-01-PLAN.md — Replace BizChat/M365 Chat in Pillar 1 + Pillar 2 controls (28 files) — COMPLETE 2026-02-17
- [x] 02-02-PLAN.md — Replace BizChat/M365 Chat in Pillar 3 + Pillar 4 controls (17 files) — COMPLETE 2026-02-17
- [x] 02-03-PLAN.md — Replace BizChat/M365 Chat in framework, reference, root, and getting-started files (17 files) — COMPLETE 2026-02-17
- [x] 02-04-PLAN.md — Broader terminology audit: Azure AD, Office 365, Purview portal naming (~40 files) — COMPLETE 2026-02-17
- [x] 02-05-PLAN.md — Verification pass + ROADMAP success criteria update — COMPLETE 2026-02-17
- [x] 02-06-PLAN.md — Gap closure: SC-3 shortened-form policy fixes (14 files) — COMPLETE 2026-02-17

### Phase 3: Pillar Updates — Readiness and Security
**Goal**: Pillars 1 and 2 controls accurately reflect current Microsoft 365 Copilot platform capabilities, including new RBAC roles, DLP policy types, Conditional Access changes, and updated licensing
**Depends on**: Phase 2
**Requirements**: P1-01, P1-02, P1-03, P1-04, P1-05, P1-06, P2-01, P2-02, P2-03, P2-04, P2-05, P2-06
**Success Criteria** (what must be TRUE):
  1. Control 1.7 documents corrected SAM licensing (included with Copilot licenses) and adds Data Access Governance reports and Restricted Access Control
  2. Controls 1.1 through 1.9 each reflect their specified updates (Optimization Assessment, DSPM, RCD, new RBAC roles, Frontline SKUs)
  3. Controls 2.1 through 2.10 each reflect their specified updates (dual DLP policy types, label groups, CA enforcement timeline, Information Barriers limitation, AI app catalog, Risky Agents)
  4. No control in Pillar 1 or Pillar 2 contains the now-corrected "BizChat" or "M365 Chat" strings (Phase 2 output validated)
  5. All three governance tiers (Baseline, Recommended, Regulated) are updated consistently within each changed control
**Plans**: 6 plans

Plans:
- [x] 03-01-PLAN.md — Update controls 1.1, 1.2, 1.3 (Optimization Assessment, DSPM unified, RCD/RSS) + playbooks + PnP fix for 1.2
- [x] 03-02-PLAN.md — Update controls 1.6, 1.7 (RBAC roles, SAM licensing rewrite, DAG, RAC) + playbooks + PnP fix for 1.6/1.8
- [x] 03-03-PLAN.md — Update controls 1.9, 2.4, 2.9 (Frontline SKUs, Channel Agent IB, AI app catalog) + playbooks
- [x] 03-04-PLAN.md — Update controls 2.1, 2.2 (dual DLP policy types, label groups, agent inheritance) + playbooks + PnP fix for 2.2
- [x] 03-05-PLAN.md — Update controls 2.3, 2.10 (CA enforcement, app ID fix, Risky Agents, IRM Triage Agent) + playbooks
- [ ] 03-06-PLAN.md — Verification pass (SC-1 through SC-5) + opportunistic playbook review + MkDocs build check

### Phase 4: Pillar Updates — Compliance and Operations
**Goal**: Pillars 3 and 4 controls accurately reflect current regulatory developments, expanded audit schemas, unified eDiscovery, agentic AI supervision requirements, and new billing models
**Depends on**: Phase 3
**Requirements**: P3-01, P3-02, P3-03, P3-04, P3-05, P3-06, P3-07, P3-08, P3-09, P4-01, P4-02, P4-03, P4-04
**Success Criteria** (what must be TRUE):
  1. Controls 3.1 through 3.11 each reflect their specified regulatory updates (expanded audit schema, unified eDiscovery migration, Communication Compliance expansion, SEC v. Delphia precedent, FINRA 2026 agentic supervision, OCC 2025-26, Reg S-P amendments, SEC 17a-4 off-channel enforcement)
  2. Controls 4.1 through 4.8 each reflect their specified updates (Copilot Control System, Teams default change with FSI recordkeeping impact, pay-as-you-go billing model)
  3. Every updated Pillar 3 control cites specific regulatory section numbers, not just regulator names
  4. The Teams Copilot default change (EnabledWithTranscript to Enabled, March 2026) is documented with explicit FSI recordkeeping compliance impact
**Plans**: TBD

Plans: TBD

### Phase 5: Framework and Reference Updates
**Goal**: Framework documents and reference materials reflect current regulatory landscape, correct licensing facts, verified Microsoft Learn URLs, and updated architecture terminology
**Depends on**: Phase 4
**Requirements**: FWRK-01, FWRK-02, FWRK-03, FWRK-04, FWRK-05, GLOB-03
**Success Criteria** (what must be TRUE):
  1. license-requirements.md correctly states SAM is included with Copilot licenses (not a separate purchase) and documents pay-as-you-go and Frontline SKU options
  2. regulatory-framework.md includes FINRA 2026 Report, SEC 2026 exam priorities, OCC 2025-26, Colorado AI Act corrected date (June 2026), and removes the Fed reputational risk item
  3. regulatory-mappings.md contains all 7 new regulatory citations identified in Review 01
  4. microsoft-learn-urls.md contains only current URLs reflecting the /copilot/ and /purview/ namespace migration
  5. copilot-architecture.md reflects Copilot Control System, Agent 365, and Entra Agent ID terminology
**Plans**: TBD

Plans: TBD

### Phase 6: Playbook Updates and Cross-linking
**Goal**: All playbooks use current PowerShell and portal patterns, and every control document is cross-linked to related controls, prerequisites, and see-also references
**Depends on**: Phase 5
**Requirements**: PLAY-01, PLAY-02, PLAY-03, PLAY-04
**Success Criteria** (what must be TRUE):
  1. The 4 PnP PowerShell playbooks (1.2, 1.6, 1.8, 2.2) document the custom Entra app registration requirement
  2. All 12 Exchange Online playbooks use REST-only cmdlet patterns with no legacy RPS usage
  3. Portal walkthrough playbooks for all updated controls reflect current MAC admin center paths
  4. Every control document contains populated Related Controls, Prerequisites, and See Also sections with working internal links
**Plans**: TBD

Plans: TBD

---

## Progress

**Execution Order:** Phases execute in numeric order: 2 → 3 → 4 → 5 → 6

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1. Initial Framework | v1.0 | 1/1 | Complete | 2026-02-17 |
| 2. Global Naming Corrections | 5/6 | Complete    | 2026-02-17 | - |
| 3. Pillar Updates — Readiness and Security | 5/6 | In Progress|  | - |
| 4. Pillar Updates — Compliance and Operations | v1.1 | 0/? | Not started | - |
| 5. Framework and Reference Updates | v1.1 | 0/? | Not started | - |
| 6. Playbook Updates and Cross-linking | v1.1 | 0/? | Not started | - |
