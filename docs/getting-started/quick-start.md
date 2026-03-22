# Quick Start Guide

Get Microsoft 365 Copilot governance in place for your financial services organization in **2-4 hours** with these five essential steps.

!!! info "First time here?"
    If you're not sure this framework fits your situation, read the [Start Here](../start-here.md) page first — it covers what this is, what it's not, and which pillar to begin with.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](../disclaimer.md).

---

## Prerequisites

Before you begin, confirm the following are in place.

### Licenses

| Requirement | Details |
|-------------|---------|
| **Microsoft 365 E5** (preferred) or **E3 + add-ons** | E5 includes Purview, Defender, and advanced compliance capabilities required for regulated governance. E3 deployments require additional license add-ons — see [License Requirements](../reference/license-requirements.md). |
| **Microsoft 365 Copilot** | Per-user Copilot license assigned to target users or groups. |
| **Purview add-ons** (if E3) | Information Protection, Data Loss Prevention, Audit (Premium), eDiscovery (Premium), Communication Compliance, and Insider Risk Management require separate licenses on E3. |

### Administrative Roles

You will need accounts with the following roles. A single Global Admin can perform all steps, but least-privilege delegation is recommended for production.

| Role | Where | Purpose |
|------|-------|---------|
| **M365 Global Admin** or **Copilot Admin** | M365 Admin Center | Enable/disable Copilot features and per-app toggles |
| **Purview Compliance Admin** | Microsoft Purview portal | Configure DLP policies, sensitivity labels, audit, retention, eDiscovery |
| **Entra Global Admin** or **Conditional Access Admin** | Microsoft Entra admin center | Conditional Access policies for Copilot |
| **SharePoint Admin** | SharePoint Admin Center | Site permissions, Restricted SharePoint Search, sharing settings |
| **Teams Admin** | Teams Admin Center | Teams Copilot meeting and chat policies |

### Portal Access

Verify you can sign in to each portal before starting:

- [M365 Admin Center](https://admin.microsoft.com)
- [Microsoft Purview portal](https://purview.microsoft.com)
- [Microsoft Entra admin center](https://entra.microsoft.com)
- [SharePoint Admin Center](https://admin.microsoft.com/sharepoint)
- [Teams Admin Center](https://admin.teams.microsoft.com)
- [Microsoft Defender portal](https://security.microsoft.com)

---

## Five-Step Quick Start

### Step 1: Run Oversharing Assessment

**Time:** 30-45 minutes | **Governance Level:** Baseline | **Pillar:** 1 (Readiness)

Copilot respects existing Microsoft 365 permissions. If users have access to content they should not see, Copilot will surface that content. Running an oversharing assessment **before** enabling Copilot is the single most important governance step.

**What to do:**

1. Run a **SharePoint Advanced Management (SAM) oversharing report** to identify sites with broad access (e.g., "Everyone except external users" permissions)
2. Review **OneDrive sharing defaults** to confirm they are set to "Specific people" rather than "Anyone" or "People in your organization"
3. Audit **Microsoft 365 Groups with open membership** that grant unintended SharePoint site access
4. Enable **Restricted SharePoint Search** during assessment if broad exposure is found — this limits Microsoft 365 Copilot Chat grounding to a curated list of up to 100 SharePoint sites while you remediate

**Key controls:**

- Control 1.1 — Copilot Readiness Assessment
- Control 1.2 — Oversharing Detection (DSPM for AI)
- Control 1.3 — Restricted SharePoint Search

**Playbooks:**

- [1.1 — Copilot Readiness Assessment](../playbooks/control-implementations/1.1/portal-walkthrough.md)
- [1.2 — Oversharing Detection](../playbooks/control-implementations/1.2/portal-walkthrough.md)
- [1.3 — Restricted SharePoint Search](../playbooks/control-implementations/1.3/portal-walkthrough.md)

---

### Step 2: Review Sensitivity Labels

**Time:** 30-45 minutes | **Governance Level:** Baseline | **Pillar:** 2 (Security)

Sensitivity labels control how Copilot can interact with classified content. Copilot inherits the highest sensitivity label from all source documents when generating new content.

**What to do:**

1. Review your existing sensitivity label taxonomy — confirm labels exist for at least: Public, Internal, Confidential, Highly Confidential
2. Verify **auto-labeling policies** are active for common patterns (account numbers, SSNs, credit card numbers)
3. Confirm **label inheritance** behavior: when Copilot references a "Highly Confidential" document, the output retains that label
4. Test label behavior in Word, Excel, and PowerPoint with Copilot prompts that reference labeled content
5. Enable **mandatory labeling** for at least Word, Excel, PowerPoint, and Outlook if not already in place

**Key controls:**

- Control 1.5 — Sensitivity Label Taxonomy Review
- Control 2.2 — Sensitivity Labels and Classification

**Playbooks:**

- [1.5 — Sensitivity Label Taxonomy Review](../playbooks/control-implementations/1.5/portal-walkthrough.md)
- [2.2 — Sensitivity Labels and Classification](../playbooks/control-implementations/2.2/portal-walkthrough.md)

---

### Step 3: Configure DLP for Copilot

**Time:** 30-45 minutes | **Governance Level:** Baseline | **Pillar:** 2 (Security)

Data Loss Prevention policies help prevent Copilot from surfacing regulated data (PII, financial account numbers, material nonpublic information) in inappropriate contexts.

**What to do:**

1. Review existing DLP policies and confirm they cover **Microsoft 365 Copilot** as a location (Purview > Data Loss Prevention > Policies)
2. Create or update DLP policies to include the **Microsoft 365 Copilot (preview)** location — this applies DLP scanning to Copilot interactions
3. Define sensitive information types relevant to your FSI context: US Social Security Numbers, credit card numbers, bank account numbers, SWIFT codes, and any custom sensitive information types for internal identifiers
4. Set policy actions: **Block with override** for Confidential content, **Block** for Highly Confidential content
5. Configure **policy tips** so users receive clear notification when DLP policies are triggered during Copilot interactions

**Key controls:**

- Control 2.1 — DLP Policies for Copilot

**Playbooks:**

- [2.1 — DLP Policies for Copilot](../playbooks/control-implementations/2.1/portal-walkthrough.md)

---

### Step 4: Enable Audit Logging

**Time:** 15-30 minutes | **Governance Level:** Baseline | **Pillar:** 3 (Compliance)

Audit logging for Copilot interactions is critical for regulatory record-keeping (FINRA 4511, SEC 17a-3/4) and supports compliance with supervisory review requirements.

**What to do:**

1. Verify **Unified Audit Log** is enabled (Purview > Audit > should show "Recording" status)
2. Confirm **Copilot interaction events** are being captured — search for `CopilotInteraction` activities in the audit log
3. Set **audit log retention** to meet your regulatory requirements: FINRA 4511 requires certain records for 3-6 years; SEC 17a-4 requires 3-6 years depending on record type
4. Enable **Audit (Premium)** if available — this provides extended retention (up to 10 years) and higher-fidelity Copilot audit events
5. Verify audit data flows to your SIEM/log management platform (Microsoft Sentinel or third-party) for long-term archival

**Key controls:**

- Control 3.1 — Copilot Audit Logging
- Control 3.2 — Data Retention Policies
- Control 3.11 — Record Keeping

**Playbooks:**

- [3.1 — Copilot Audit Logging](../playbooks/control-implementations/3.1/portal-walkthrough.md)
- [3.2 — Data Retention Policies](../playbooks/control-implementations/3.2/portal-walkthrough.md)

---

### Step 5: Set Per-App Toggles

**Time:** 15-30 minutes | **Governance Level:** Baseline | **Pillar:** 4 (Operations)

Microsoft 365 Copilot can be enabled or disabled per application. For FSI organizations, a phased rollout with selective app enablement reduces risk.

**What to do:**

1. Navigate to **M365 Admin Center > Copilot > Settings** to review the current tenant controls for Copilot user access, data access, actions, and other feature settings
2. Disable **web search** in Copilot (Baseline recommendation for regulated environments) — this prevents Copilot from querying Bing for grounding data
3. Review **per-app and user access settings** and disable Copilot in applications or user groups not yet approved by your governance committee
4. Configure **Copilot Pages** creation through **Cloud Policy** — determine whether users can create Copilot Pages and Copilot Notebooks, which are stored in user-owned SharePoint Embedded containers and require SharePoint retention/eDiscovery coverage
5. Review **extensibility and agent settings** — disable or restrict third-party plugins, external agents, and custom agents until your governance review process is in place

**Key controls:**

- Control 4.1 — Admin Settings and Feature Management
- Control 2.6 — Web Search Controls
- Control 4.13 — Extensibility Governance

**Playbooks:**

- [4.1 — Admin Settings and Feature Management](../playbooks/control-implementations/4.1/portal-walkthrough.md)
- [2.6 — Web Search Controls](../playbooks/control-implementations/2.6/portal-walkthrough.md)

**Reference:** [Copilot Admin Toggles](../reference/copilot-admin-toggles.md) for a complete list of every toggle, default value, and FSI-recommended setting.

---

## What Comes Next

After completing the five-step quick start, you have **Baseline** governance in place. To move toward **Recommended** and **Regulated** governance levels:

| Next Step | Description | Reference |
|-----------|-------------|-----------|
| **Complete the Implementation Checklist** | Walk through all 56 controls across four pillars | [Implementation Checklist](checklist.md) |
| **Read the Executive Summary** | Understand the strategic governance context for leadership communication | [Executive Summary](../framework/executive-summary.md) |
| **Configure Information Barriers** | Required for broker-dealers and firms with material nonpublic information (MNPI) walls | Control 2.4 |
| **Set up Communication Compliance** | Required for FINRA 3110 supervisory review of Copilot-assisted communications | Control 3.4 |
| **Enable DSPM for AI** | Data Security Posture Management for AI provides Copilot-specific risk insights | Control 1.2 |
| **Review Regulatory Mappings** | Map controls to your specific regulatory obligations | [Regulatory Mappings](../reference/regulatory-mappings.md) |
| **Follow the Adoption Roadmap** | Phase your rollout from pilot to broad deployment | [Adoption Roadmap](../framework/adoption-roadmap.md) |

---

## Estimated Time Summary

| Step | Task | Time |
|------|------|------|
| 1 | Oversharing Assessment | 30-45 min |
| 2 | Sensitivity Labels Review | 30-45 min |
| 3 | DLP for Copilot | 30-45 min |
| 4 | Audit Logging | 15-30 min |
| 5 | Per-App Toggles | 15-30 min |
| **Total** | **Baseline Governance** | **2-4 hours** |

!!! tip "Tip"
    These times assume existing Microsoft 365 infrastructure. If you are deploying Purview, Entra, or sensitivity labels for the first time, allow additional time for initial setup.

---

*FSI Copilot Governance Framework v1.2.1 - March 2026*
