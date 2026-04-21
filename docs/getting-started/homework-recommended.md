---
title: "Homework: Recommended"
description: Pre-session tasks for the Recommended governance tier across Pillars 1-4.
---

# Pre-Session Homework — Recommended Tier

The Recommended tier extends beyond the Baseline guardrails into proactive controls across all four pillars — Readiness, Security, Compliance, and Operations. It is aimed at FSI organizations that have completed an initial Copilot rollout and want governance depth closer to what regulators have signaled in FFIEC, FINRA Rule 3110 supervisory guidance, and SR 11-7 / OCC Bulletin 2011-12 model-risk expectations.

Doing this homework up front helps meet examiner expectations that governance decisions are grounded in current tenant state rather than assumptions. Organizations should verify that the evidence gathered aligns with their internal records-management schedule before sharing.

---

## AI Administrator

Coordinates Copilot surface expansion — agents, Pages, Notebooks, third-party models.

- Export the **declarative agents and Copilot Studio agents inventory**, with owner, publish status, and grounding sources.
- Capture **Copilot Pages** and **Notebooks** tenant toggles and any scoped-group configurations.
- Document **web search** and **third-party model provider** states (Control 2.6, 1.13).
- Pull a sample of **agent usage telemetry** (per-agent invocation counts, latency, error rates).
- Download the role checklist: [ai-administrator-checklist.xlsx](../assessment/templates/ai-administrator-checklist.xlsx).

## M365 Global Admin or Copilot Admin

- Export **Integrated Apps** full inventory (declarative agents, Copilot extensions, connected apps) with admin-consent posture.
- Produce **Copilot feature release ring** configuration (Targeted Release membership, pilot groups).
- Capture **Viva suite governance** settings where Viva Insights / Glint telemetry intersects with Copilot (Control 4.4, 4.6).
- Download the role checklist: [m365-global-admin-or-copilot-admin-checklist.xlsx](../assessment/templates/m365-global-admin-or-copilot-admin-checklist.xlsx).

## Entra Global Admin

Owns Conditional Access depth and Entra Agent ID posture (2.3).

- Export the full **Conditional Access policy set** (JSON), including policies for Copilot apps, agent workload identities, and Intune-compliant device requirements.
- Produce the **Entra Agent ID inventory** for agents registered as workload identities, with credential type and rotation status.
- Capture **Privileged Identity Management (PIM)** assignments for Copilot-relevant admin roles.
- Download the role checklist: [entra-global-admin-checklist.xlsx](../assessment/templates/entra-global-admin-checklist.xlsx).

## SharePoint Admin

- Run the full **SharePoint Advanced Management Content Management Assessment** and export output.
- Capture **site lifecycle management** configuration (inactive site policies, M365 Archive onboarding).
- Produce **external sharing governance** posture (guest access policies, B2B direct connect) (Control 2.12).
- Download the role checklist: [sharepoint-admin-checklist.xlsx](../assessment/templates/sharepoint-admin-checklist.xlsx).

## Purview Compliance Admin

Owns deeper DLP, retention, eDiscovery, and communication compliance (2.1, 3.2, 3.3, 3.4).

- Export **DLP policies with Copilot location coverage** and any prompt-inspection policies (Control 2.1).
- Produce the **retention policy and label inventory** mapped to FINRA 4511 / SEC 17a-4-required record types (Control 3.2, 3.11).
- Capture **eDiscovery (Premium)** case list and custodian hold status intersecting Copilot-generated content (Control 3.3).
- Export **Communication Compliance** policy list and recent review queue statistics (Control 3.4).
- Download the role checklist: [purview-compliance-admin-checklist.xlsx](../assessment/templates/purview-compliance-admin-checklist.xlsx).

## Security Admin

- Export **Defender for Cloud Apps** session policies, anomaly detection policies, and Copilot-connected app risk scores (Control 2.9).
- Produce **network security** posture for Copilot egress — Private Link, named locations, tenant restrictions (Control 2.15).
- Capture **Sentinel analytics rules** subscribed to Copilot audit data (Control 4.11).
- Download the role checklist: [security-admin-checklist.xlsx](../assessment/templates/security-admin-checklist.xlsx).

## Compliance Officer

- Draft the **AI disclosure and transparency** customer-communications review (Control 3.9) and map to any FINRA Rule 2210 communications touched by Copilot drafting assistance (Control 3.5).
- Produce **model risk management** documentation status aligned with SR 11-7 / OCC Bulletin 2011-12 for each Copilot use case classified as a model (Control 3.8).
- Capture **supervision and oversight** evidence per FINRA Rule 3110 — supervisory systems / WSPs — where applicable to Copilot-assisted communications (Control 3.6).
- Download the role checklist: [compliance-officer-checklist.xlsx](../assessment/templates/compliance-officer-checklist.xlsx).

## Teams Admin

- Export **Teams meetings and Copilot-in-Teams policies** (recording, transcription, intelligent recap, Copilot answers scope) (Control 4.2).
- Produce **Teams Phone queue Copilot configuration** where enabled (Control 4.3).
- Capture **meeting retention** and **transcript eDiscovery** configuration intersecting Copilot meeting summaries.
- Download the role checklist: [teams-admin-checklist.xlsx](../assessment/templates/teams-admin-checklist.xlsx).

## Internal Audit

- Produce the **evidence-collection plan** aligned with Control 3.12 — which logs, screenshots, and configuration exports are captured per audit cycle.
- Pull a **sample audit trail** of Copilot interactions including admin action logs, policy changes, and user prompts (where retained) (Control 3.1).
- Confirm **FFIEC alignment** mapping is documented for the audit plan (Control 3.13).
- Download the role checklist: [internal-audit-checklist.xlsx](../assessment/templates/internal-audit-checklist.xlsx).

## Records Manager

- Export the **retention label application report** for Copilot-generated artifacts (Pages, Notebooks, Loop components, Teams meeting notes) (Control 3.2, 3.11).
- Confirm **Microsoft 365 Archive** onboarding status for inactive SharePoint sites containing Copilot grounding sources.
- Map Copilot artifacts against **required-records obligations** (SEC Rule 17a-4 for broker-dealer required records only, FINRA 4511) where applicable.
- Download the role checklist: [records-manager-checklist.xlsx](../assessment/templates/records-manager-checklist.xlsx).

## Governance Lead

- Produce the **cross-pillar governance dashboard** (traffic-light status by control) for the current quarter.
- Capture **incident reporting** workflow status and any Copilot-involved incidents in the past quarter (Control 4.9).
- Confirm **change management rollout** cadence and current wave (Control 4.12).
- Download the role checklist: [governance-lead-checklist.xlsx](../assessment/templates/governance-lead-checklist.xlsx).

---

## Next steps

Run the [Governance Scorecard](../assessment/index.md) to score Recommended-tier coverage across Pillars 1-4 and identify which controls need deeper work before pursuing Regulated-tier posture.

*FSI Copilot Governance Framework — pre-session homework (Recommended tier).*
