---
title: "Homework: Regulated"
description: Pre-session tasks for the Regulated governance tier across all 14 CopilotGov roles.
---

# Pre-Session Homework — Regulated Tier

The Regulated tier is scoped for institutions subject to layered supervisory regimes — OCC-chartered banks, FINRA-member broker-dealers, SEC-registered investment advisers, NAIC-regulated insurers, and state-regulated trust companies. It assumes Baseline and Recommended controls are in place and focuses on evidentiary depth, model-risk rigor, and examiner-ready documentation.

This homework supports engagements where the working session will produce artifacts that may be cited in examiner requests. It helps meet expectations set in **12 CFR part 30, appendix D (OCC Heightened Standards)**, **SR 11-7 / OCC Bulletin 2011-12** for model risk, **FFIEC IT Examination Handbook** modules, and **GLBA §501(b)** safeguarding obligations. Organizations should verify that artifacts are classified and distributed only per internal legal-hold and confidentiality policy, and that evidence intended for examiners is produced through the institution's official regulatory-examination channel.

---

## AI Administrator

- Produce the **complete agent and extension inventory** with owner, data classification, zone assignment, approved use cases, and last review date — for all Copilot surfaces (Chat, Word/Excel/PowerPoint/Outlook/Teams, Pages, Notebooks, Copilot Studio agents, declarative agents, SharePoint agents, Copilot Tuning projects).
- Export **third-party model provider** configurations (Anthropic, xAI) including contractual attestations, data-flow diagrams, and the Entra Agent ID / workload identity posture for each integration.
- Capture **agent-usage telemetry** time series (90+ days) with outlier flagging documented.
- Document **Copilot Tuning** dataset provenance, approval chain, and differential-privacy settings if used (Control 1.16).
- Download the role checklist: [ai-administrator-checklist.xlsx](../assessment/templates/ai-administrator-checklist.xlsx).

## M365 Global Admin or Copilot Admin

- Export the **full tenant configuration baseline** (Copilot toggles, Integrated Apps, Viva, Teams, SharePoint sharing) as a time-stamped JSON/PDF bundle suitable for examiner production.
- Produce **Message Center item acknowledgement log** for the rolling 12 months covering Copilot feature rollouts and opt-in/out decisions.
- Capture **license-assignment change log** (who, when, approval reference) for all Copilot SKUs.
- Download the role checklist: [m365-global-admin-or-copilot-admin-checklist.xlsx](../assessment/templates/m365-global-admin-or-copilot-admin-checklist.xlsx).

## Entra Global Admin

- Export the **full Conditional Access policy set with change history** for the past 12 months, including policies for Copilot apps, agent workload identities, and B2B partners.
- Produce the **Entra Agent ID registry** with credential rotation schedule and last-rotation evidence per agent.
- Capture **PIM assignment history** for Copilot-relevant admin roles with justification text.
- Confirm **break-glass account** review evidence (quarterly attestation recommended).
- Download the role checklist: [entra-global-admin-checklist.xlsx](../assessment/templates/entra-global-admin-checklist.xlsx).

## SharePoint Admin

- Produce the **full SAM control state inventory**: RAC, RCD, Restricted SharePoint Search allow-list, Content Management Assessment output, site lifecycle policy configuration, and M365 Archive status (Controls 1.2, 1.3, 1.7, 1.15).
- Export the **item-level permission scan results** for all Zone 3 (NPI-bearing) sites, not just samples (Control 1.14).
- Capture **permission-drift evidence** — quarterly comparison reports showing change since the last attestation (Control 1.15).
- Download the role checklist: [sharepoint-admin-checklist.xlsx](../assessment/templates/sharepoint-admin-checklist.xlsx).

## Purview Compliance Admin

- Produce **DLP policy effectiveness reports** for Copilot locations including incident volume, false-positive rate, and policy-tuning change log (Control 2.1).
- Export the **sensitivity label analytics** (application coverage per zone), auto-labeling accuracy by SIT, and any prompt-inspection policy evidence.
- Capture **audit log retention attestation** confirming Copilot interaction records are held for the institution's required period (commonly 7 years for FINRA/SEC-scoped records) (Control 3.1, 3.11).
- Produce **eDiscovery (Premium) case inventory** with Copilot-content custodian holds and export-ready status (Control 3.3).
- Export **Communication Compliance** policy coverage, review SLAs, and escalation records for Copilot-touched communications (Control 3.4).
- Download the role checklist: [purview-compliance-admin-checklist.xlsx](../assessment/templates/purview-compliance-admin-checklist.xlsx).

## Security Admin

- Produce the **Defender XDR Copilot-related incident inventory** for the past 12 months with mean-time-to-detect / mean-time-to-respond metrics (Control 2.9, 4.9).
- Export **network security posture** — Private Link configuration, named locations, tenant restrictions v2, and any egress controls specific to Copilot (Control 2.15).
- Capture **Sentinel workbook** evidence aggregating Copilot audit, DLP, insider-risk, and agent-identity signals (Control 4.11).
- Download the role checklist: [security-admin-checklist.xlsx](../assessment/templates/security-admin-checklist.xlsx).

## Compliance Officer

- Produce the **model-risk management file** per SR 11-7 / OCC Bulletin 2011-12 for each Copilot use case classified as a model: purpose, data inputs, validation plan, monitoring cadence, independent review sign-off (Control 3.8).
- Export **supervision evidence** under FINRA Rule 3110 — supervisory systems and WSPs — for Copilot-assisted registered-representative communications, where applicable (Control 3.6).
- Produce **FINRA Rule 2210** communications-review evidence for Copilot-drafted retail communications, where applicable (Control 3.5).
- Capture **AI disclosure** language currently deployed to customers and employees (Control 3.9).
- Download the role checklist: [compliance-officer-checklist.xlsx](../assessment/templates/compliance-officer-checklist.xlsx).

## Teams Admin

- Export **Teams meeting recording and transcription coverage** by business unit, with retention mapping.
- Produce **Copilot-in-Teams policy inventory** per user group, including opt-out exceptions and rationale.
- Capture **intelligent recap governance** evidence — who can access, retention, eDiscoverability.
- Download the role checklist: [teams-admin-checklist.xlsx](../assessment/templates/teams-admin-checklist.xlsx).

## Exchange Online Admin

- Export **mailbox-level retention** policies covering Copilot-generated drafts and Outlook Copilot activity (Control 3.2, 3.11).
- Produce **journaling configuration** evidence where required for broker-dealer supervision.
- Capture **Copilot in Outlook** feature state and any mail-flow rules affecting Copilot-drafted messages.
- Download the role checklist: [exchange-online-admin-checklist.xlsx](../assessment/templates/exchange-online-admin-checklist.xlsx).

## Internal Audit

- Produce the **Copilot audit program** aligned with FFIEC IT Examination Handbook modules (Control 3.13), including test procedures, sample sizes, and evidence templates.
- Export **prior audit findings and remediation status** for Copilot-related issues.
- Capture **evidence-collection automation** artifacts (Log Analytics queries, Sentinel workbooks) used during audit cycles (Control 3.12).
- Download the role checklist: [internal-audit-checklist.xlsx](../assessment/templates/internal-audit-checklist.xlsx).

## Privacy Officer

- Produce **GLBA §501(b) safeguarding** posture evidence for non-public personal information (NPI) flows through Copilot (prompts, responses, grounding sources).
- Export the **data-minimization and grounding-scope** evidence for Zone 3 agents (Control 2.5), including public-web-grounding disablement where NPI is in scope.
- Capture **privacy impact assessments (PIAs)** for each Copilot use case touching NPI or biometric data.
- Confirm **state privacy law** mapping (CCPA/CPRA, Washington My Health My Data where applicable) is documented for Copilot data flows.
- Download the role checklist: [privacy-officer-checklist.xlsx](../assessment/templates/privacy-officer-checklist.xlsx).

## Records Manager

- Produce the **records retention matrix** for all Copilot artifacts (chat transcripts, Pages, Notebooks, Loop, meeting summaries, agent responses) mapped to retention schedules.
- Export **Microsoft 365 Archive** state and cost/retention report.
- Confirm **SEC Rule 17a-4** required-broker-dealer-records mapping is explicit about which Copilot artifacts are in scope and which are not.
- Capture **legal-hold intersection** evidence where Copilot artifacts intersect active preservations.
- Download the role checklist: [records-manager-checklist.xlsx](../assessment/templates/records-manager-checklist.xlsx).

## Vendor / Third-Party Risk Manager

- Produce the **third-party Copilot ecosystem inventory** aligned with **OCC Bulletin 2023-17**, including vendor criticality, contract review cadence, SOC 2 / ISO 27001 / HITRUST attestations, and subprocessor lists.
- Export **ongoing monitoring evidence** for each vendor — performance SLA adherence, security-event notifications, regulatory change notices.
- Capture **exit plan documentation** for critical Copilot extensions and third-party model providers.
- Download the role checklist: [vendor-third-party-risk-manager-checklist.xlsx](../assessment/templates/vendor-third-party-risk-manager-checklist.xlsx).

## Governance Lead

- Produce the **executive governance report** covering all four pillars with scorecard trend lines (quarterly, 12 months).
- Export the **Copilot AI Use Policy version history** with approval records.
- Capture **board/committee reporting** evidence where Copilot risks are discussed at the AI or model-risk committee.
- Confirm **incident reporting** evidence for Copilot-involved incidents, including notification timelines where regulatory reporting was required (Control 4.9, 3.7).
- Download the role checklist: [governance-lead-checklist.xlsx](../assessment/templates/governance-lead-checklist.xlsx).

---

## Next steps

After homework is assembled, run the [Governance Scorecard](../assessment/index.md) in Regulated mode to produce the evidence-backed self-assessment used during the working session. Findings feed the Phase 2 expansion and ongoing [audit readiness checklist](../playbooks/compliance-and-audit/audit-readiness-checklist.md).

*FSI Copilot Governance Framework — pre-session homework (Regulated tier).*
