---
title: "Homework: Quick Start"
description: Pre-session tasks for the 2-4 hour M365 Copilot quick-start governance engagement.
---

# Pre-Session Homework — Quick Start

This homework supports the five-step [Quick Start](quick-start.md) engagement that covers the essential guardrails for Microsoft 365 Copilot: oversharing detection (1.2), restricted SharePoint search (1.3), DLP for Copilot (2.1), audit logging (3.1), and admin feature management (4.1).

Completing these tasks ahead of time helps the working session stay focused on *decisions* rather than data collection, and aids in producing a defensible record of tenant state before any Copilot configuration change. Organizations should verify that the artifacts collected here match their internal evidence-handling standards before sharing.

---

## M365 Global Admin or Copilot Admin

Owns tenant-level Copilot feature toggles and the M365 Admin Center Copilot page (Control 4.1).

- Export the current **Copilot & Agents settings** (M365 Admin Center → Copilot → Settings) as a screenshot set or JSON, including per-app toggles for Word, Excel, PowerPoint, Outlook, Teams, and Loop.
- List all users and groups with assigned **Microsoft 365 Copilot** and **Copilot Chat Premium** licenses; note the April 15, 2026 Basic/Premium split status for your tenant.
- Capture the current list of **pinned/blocked agents** from the Integrated Apps blade and the Copilot agent catalog.
- Pull the last 90 days of **Copilot adoption/usage report** from M365 Admin Center for baseline telemetry.
- Confirm which admin roles are assigned to break-glass accounts and which are time-bound via Entra PIM.
- Download the role checklist: [m365-global-admin-or-copilot-admin-checklist.xlsx](../assessment/templates/m365-global-admin-or-copilot-admin-checklist.xlsx).

## SharePoint Admin

Owns Restricted SharePoint Search (1.3) and surfaces the oversharing signal for 1.2.

- Run the **SharePoint Advanced Management (SAM) Data Access Governance reports** for "Everyone except external users", "Shared with Everyone", and "Sensitivity labels applied" and export the CSV output.
- Export the current **tenant sharing settings** (SharePoint Admin Center → Policies → Sharing) and the **default sharing link type** for SharePoint and OneDrive.
- Produce the current **Restricted SharePoint Search allow-list** (PowerShell: `Get-SPOTenantRestrictedSearchAllowedList`) or confirm that RSS is not yet enabled.
- Identify the **top 25 sites by item count** and tag which are in-scope for Copilot rollout.
- Download the role checklist: [sharepoint-admin-checklist.xlsx](../assessment/templates/sharepoint-admin-checklist.xlsx).

## Purview Compliance Admin

Owns DLP for Copilot (2.1), Copilot audit logging (3.1), and DSPM for AI (referenced by 1.2).

- Export the current **DLP policy inventory** from Purview (policy name, scope, locations, rules) with particular focus on policies covering the **Microsoft 365 Copilot** and **Copilot Chat** locations.
- Confirm **Audit (Standard or Premium)** is enabled tenant-wide and export the list of **Copilot interaction audit records** for the past 7 days (`CopilotInteraction` workload) as a representative sample.
- Export the **sensitivity label taxonomy** and which labels apply encryption or content marking.
- Capture the current **DSPM for AI** dashboard state and any active AI interaction policies.
- Download the role checklist: [purview-compliance-admin-checklist.xlsx](../assessment/templates/purview-compliance-admin-checklist.xlsx).

## Security Admin

Supports DLP coverage review (2.1) and provides the Defender/Conditional Access context for quick-start scope.

- Export the **Conditional Access policy set** that targets Copilot apps (Microsoft 365 Copilot, Copilot Chat, SharePoint) and note any gaps for unmanaged devices.
- Pull the current **Defender for Cloud Apps** connector list and any active session/access policies that apply to Copilot traffic.
- List **sign-in risk** and **user risk** policies currently in effect for users with Copilot licenses.
- Download the role checklist: [security-admin-checklist.xlsx](../assessment/templates/security-admin-checklist.xlsx).

---

## Next steps

Bring the exported artifacts to the working session. Once homework is complete, start the self-assessment at [Governance Scorecard](../assessment/index.md) to score your tenant against the five quick-start controls.

*FSI Copilot Governance Framework — pre-session homework (Quick Start tier).*
