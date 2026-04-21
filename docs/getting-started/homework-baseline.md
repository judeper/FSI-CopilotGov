---
title: "Homework: Baseline"
description: Pre-session tasks for the Pillar 1 (Readiness) Baseline tier — all 16 controls.
---

# Pre-Session Homework — Baseline (Pillar 1: Readiness)

This homework supports the Baseline tier of Pillar 1 — **Readiness** — which covers all 16 Pillar 1 controls (1.1 through 1.16). Baseline readiness is the recommended starting point for any financial-services organization turning on Microsoft 365 Copilot: it addresses the oversharing, permission-drift, license, and extensibility fundamentals that determine whether Copilot responses stay inside appropriate data boundaries.

Collecting these artifacts before the working session helps meet FFIEC IT Examination Handbook expectations for change pre-assessment and supports internal model-risk documentation requirements. Organizations should verify that exported reports are handled per their data classification policy.

---

## AI Administrator

Coordinates readiness across Copilot surfaces (Chat, agents, declarative agents, Copilot Tuning). Contributes to controls 1.1, 1.4, 1.13, 1.16.

- Produce an **inventory of Copilot surfaces in use** (Copilot Chat, Microsoft 365 Copilot, Copilot Studio agents, declarative agents, SharePoint agents, Copilot Pages, Notebooks).
- List any **Copilot Tuning** projects and the datasets they reference (Control 1.16).
- Export the **semantic index status** per workload (SharePoint, OneDrive, Graph connectors) (Control 1.4).
- Document any **third-party model providers** configured (Anthropic, xAI) or planned (Control 1.13 extensibility).
- Download the role checklist: [ai-administrator-checklist.xlsx](../assessment/templates/ai-administrator-checklist.xlsx).

## M365 Global Admin or Copilot Admin

Owns license assignment (1.9), tenant toggles, and change windows (1.11).

- Export **Copilot license assignments** (user list + group assignments) and unused-license report.
- Capture current **Copilot tenant feature toggles** including Copilot Chat Basic/Premium, Pages, Notebooks, and Researcher/Analyst agents.
- Pull **Message Center items** tagged "Copilot" for the past 90 days and current **Copilot release wave** (Targeted Release / Standard).
- Download the role checklist: [m365-global-admin-or-copilot-admin-checklist.xlsx](../assessment/templates/m365-global-admin-or-copilot-admin-checklist.xlsx).

## SharePoint Admin

Owns the lion's share of Pillar 1: oversharing, RSS, permissions, SAM, information architecture (1.2, 1.3, 1.6, 1.7, 1.8, 1.14, 1.15).

- Run the full **SAM Data Access Governance** suite: Sharing Links, Sensitivity Labels Applied, Everyone Except External Users, and Site Access Reviews (Controls 1.2, 1.7).
- Export **Restricted SharePoint Search** configuration or gap list (Control 1.3).
- Produce the **site permissions inventory** for top 50 sites by user count (Control 1.6).
- Run **item-level permission scan** samples on 3-5 representative sites per zone (Control 1.14).
- Capture the current **Restricted Access Control (RAC)** and **Restricted Content Discovery (RCD)** site lists (Controls 1.7, 1.15).
- Export **OneDrive sharing defaults** and any delegated OneDrive admin configuration.
- Download the role checklist: [sharepoint-admin-checklist.xlsx](../assessment/templates/sharepoint-admin-checklist.xlsx).

## Purview Compliance Admin

Supports sensitivity label taxonomy review (1.5) and DSPM for AI readiness inputs (1.2).

- Export the **sensitivity label taxonomy**, including sublabels, scopes (Files/Emails, Groups/Sites, Schematized data), and auto-labeling policies (Control 1.5).
- Produce an **auto-labeling simulation report** showing match rates per SIT on recent content.
- Capture the **DSPM for AI** readiness assessment output and any flagged sites/files (Control 1.2 input).
- Download the role checklist: [purview-compliance-admin-checklist.xlsx](../assessment/templates/purview-compliance-admin-checklist.xlsx).

## Governance Lead

Owns change management and training program rollout (1.11, 1.12), and cross-pillar readiness sign-off (1.1).

- Produce the draft **Copilot change-management plan**: wave schedule, acceptance criteria, rollback procedure (Control 1.11).
- Export the **training attendance roster** for Copilot launch training and list role-based curricula in place (Control 1.12).
- Draft the **Readiness Assessment scorecard** inputs for Control 1.1, including scope (business units, geographies, zones).
- Download the role checklist: [governance-lead-checklist.xlsx](../assessment/templates/governance-lead-checklist.xlsx).

## Compliance Officer

Reviews information-architecture and extensibility readiness for regulatory fit (1.8, 1.13).

- Produce a **records-classification map** showing which SharePoint sites contain FINRA/SEC required records that intersect with Copilot grounding scope (Control 1.8).
- List **third-party connectors and agents** planned or deployed, with vendor risk-review status (Control 1.13 input).
- Confirm that the **Copilot AI Use Policy** is drafted and has an owner.
- Download the role checklist: [compliance-officer-checklist.xlsx](../assessment/templates/compliance-officer-checklist.xlsx).

## Vendor / Third-Party Risk Manager

Supports extensibility readiness (1.13) and license/vendor due diligence (1.9).

- Produce the **third-party risk review status** for each connector, plugin, declarative agent, or Copilot Studio vendor integration planned for the rollout (Control 1.13).
- Confirm **OCC Bulletin 2023-17** third-party risk management expectations are reflected in the onboarding checklist for new Copilot extensions.
- Capture **vendor data-residency and subprocessor attestations** for any non-Microsoft model providers (Anthropic, xAI) (Control 1.13).
- Download the role checklist: [vendor-third-party-risk-manager-checklist.xlsx](../assessment/templates/vendor-third-party-risk-manager-checklist.xlsx).

---

## Next steps

With these artifacts in hand, run the [Governance Scorecard](../assessment/index.md) to self-score Pillar 1 Baseline coverage. Gaps identified feed directly into the Phase 0 and Phase 1 [playbook sequence](../playbooks/getting-started/phase-0-governance-setup.md).

*FSI Copilot Governance Framework — pre-session homework (Baseline tier, Pillar 1: Readiness).*
