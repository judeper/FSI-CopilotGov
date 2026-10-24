# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-24
**Run Time:** 2026-10-24T13:43:17.944553+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| HIGH Changes | 2 |
| MEDIUM Changes | 1 |
| Redirects | 9 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | MEDIUM | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | microsoft-365-copilot-setup | HIGH | 2.6 | Update portal-walkthrough |
| 3 | ...soft-365-copilot-enablement-resources | HIGH | 1.11, 1.12 | Update portal-walkthrough |
| 4 | connect-to-ai-subprocessor | HIGH | 1.10, 1.8, 3.8a, 2.7 | Update portal-walkthrough |
| 5 | ...lot-ai-provider-user-sec-group-access | HIGH | None | Review and update |
| 6 | dlp-create-deploy-policy | HIGH | None | Review and update |
| 7 | authoring-select-agent-model | CRITICAL | 1.16, 4.14 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.9/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.9/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.15/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -412,8 +412,8 @@ Control whether Copilot Chat is
 pinned across experiences
 , such as in the Microsoft 365 app and other Copilot surfaces, based on licensing.
-Manage whether users can
-generate images in Copilot Chat
+Manage whether users can generate images in Copilot Chat by
+configuring Copilot actions
 .
 Control how users can
 create and use agents

```

---

### 2. Microsoft 365 Copilot setup guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.6: Control 2.6: Copilot Web Search and Web Grounding Controls
  - File: `controls/pillar-2-security/2.6-web-search-controls.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.6/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.6/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1,269 +1,75 @@-Set up Microsoft Copilot and assign licenses
-As part of your
+Microsoft Copilot adoption guide and overview for IT admins
+Microsoft Copilot
+is an AI tool that can find information, get answers to questions, and help with tasks. To help you onboard and adopt Microsoft Copilot in your organization, use the steps in this article.
+This article provides an overview of the steps and resources that can help you enable and start using Microsoft Copilot in your organization.
+This article applies to:
+Microsoft Copilot
+Step 1 - Get your organization ready and use the Microsoft Adoption site
+â
+Use the Microsoft Copilot Optimization Assessment
+The
+Microsoft Copilot Optimization Assessment
+can help you understand your organization's readiness for Microsoft Copilot. It evaluates your data governance maturity and data security controls.
+Microsoft recommends you complete the assessment before deploying Microsoft Copilot in your organization. Based on the outcomes of the assessment, you can determine your path forward so your organization is ready for Copilot.
+â
+Get your data ready
+Use the features in your Microsoft 365 subscription and SharePoint Advanced Management (SAM) licenses to help get your data ready for Copilot.
+See
+Configure a secure and governed data foundation for Microsoft Copilot
+.
+â
+Use the Microsoft Adoption site
+Microsoft Adoption
+includes resources that help you enable and use Copilot in your organization, including:
+A downloadable
+Success Kit
+to help drive user enablement and technical readiness in your organization.
+A
+Launch Day
+kit to help create hype around your rollout.
+The
+Interactive Scenario Library
+with example outcomes and success measures for several different industries and roles.
+Instructor-led
+QuickStart training
+sessions to learn how AI can help.
+To get started, go to
 Microsoft Copilot adoption
-, the next step is to enable security features, configure the update channel, and assign C
```

---

### 3. Microsoft 365 Copilot adoption guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.11: Control 1.11: Organizational Change Management and Adoption Planning
  - File: `controls/pillar-1-readiness/1.11-change-management-adoption.md`
- Control 1.12: Control 1.12: Training and Awareness Program
  - File: `controls/pillar-1-readiness/1.12-training-awareness.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.11/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -37,23 +37,22 @@ Microsoft Copilot adoption
 to explore and download resources.
 Step 2 - Choose your Microsoft Copilot license
-There are different license options for Microsoft Copilot. The license you choose depends on your organization's needs and any existing Microsoft 365 subscriptions you have.
+Microsoft Copilot offers different license options. Choose the license that fits your organization's needs and consider any existing Microsoft 365 subscriptions you have.
 To learn more, see
 Microsoft Copilot license plans
 .
 Step 3 - Get your Microsoft 365 apps and network ready
-Microsoft Copilot integrates with your Microsoft 365 apps, including Microsoft Teams. To use Microsoft Copilot with your apps, make sure that your Microsoft 365 apps and network meet the requirements, and that your app privacy settings allow Copilot.
+Microsoft Copilot integrates with your Microsoft 365 apps, including Microsoft Teams. To use Microsoft Copilot with your apps, ensure that your Microsoft 365 apps and network meet the requirements, and that your app privacy settings allow Copilot.
 To learn more, see
 Microsoft 365 app and service requirements
 .
 Step 4 - Set up Copilot and assign licenses
-In this step, you assign Copilot licenses to your users and can configure some Microsoft Copilot features.
-To learn more and get started:
-Set up Microsoft Copilot - Admin guide on Learn
-Set up Microsoft Copilot - Setup guide in the Microsoft 365 admin center
+In this step, assign Copilot licenses to your users and configure some Microsoft Copilot features.
+To learn more, see the
+Setup guide in the Microsoft 365 admin center
 Step 5 - Send a welcome email and enable feedback
-After your licenses are assigned, you can send a welcome email to your users. This email can include information about Microsoft Copilot, how to use it, and any training resources you have available.
-You can also use the Copilot onboarding experience to help users get started with Copilot. Copilot onb
```

---

### 4. Anthropic as a Microsoft subprocessor

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`
- Control 1.8: Control 1.8: Information Architecture Review
  - File: `controls/pillar-1-readiness/1.8-information-architecture-review.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.10/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.10/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.8/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.8/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.8/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.8/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1,6 +1,4 @@ Anthropic models in Microsoft Online Services
-Note
-Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat. There are no changes to security, compliance, and privacy for organizations.
 Microsoft is introducing a new offering with Anthropic AI models as part of Microsoft Online Services, delivering enterprise-grade commitments and safeguards to ensure secure and responsible use of Anthropic models within your organization.
 To enable this change, Anthropic has onboarded as a Microsoft subprocessor. This change simplifies the experience and strengthens compliance and security under Microsoft's enterprise framework. The Microsoft Customer Copyright Commitment (CCC) applies to Anthropic models used within products covered by the CCC, including Microsoft Copilot and Copilot Studio.
 As a subprocessor, Anthropic operates with Microsoft oversight through contractual safeguards and appropriate technical and organizational measures. Unless models are labeled "Anthropic models with Data Retention," the

```

---

### 5. Select an agent model

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Section:** Copilot Studio
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 1.16: Control 1.16: Copilot Tuning Governance
  - File: `controls/pillar-1-readiness/1.16-copilot-tuning-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -3,14 +3,13 @@ This article describes features used in agents or agent flows powered by the
 standard harness
 .
-AI capabilities evolve rapidly, and each generative model brings distinct strengths, whether it's faster responses, higher-quality outputs, or improved cost efficiency. By using Copilot Studio, you can choose the best model for your agent's orchestration by using a simple dropdown menu.
-Want to try out cutting-edge models before they're production-ready? Access the latest experimental models to evaluate them early. However, they might have limited testing, availability, and functionality.
-This article describes how to select an AI model for your agent's generative orchestration. Separate settings exist for changing models for
+In Microsoft Copilot Studio, the primary AI model you select for your agent powers generative orchestration. Choose a model based on how much your agent needs in response speed, output quality, reasoning, and cost.
+Primary model selection is separate from the settings for
 deep reasoning (preview)
 ,
 generative responses (preview)
-, and the
-prompt builder
+, and
+prompt builder models
 .
 Important
 Experimental models are available for exploration and testing but aren't recommended for production use. Review
@@ -21,11 +20,10 @@ .
 This article contains Copilot Studio documentation on model selection, which includes experimental model previews, and is subject to change.
 Model availability by region
-Copilot Studio offers different types of models. These model types are based on their intended use and availability.
-You can see each model's tags in the
-list of models
-in Copilot Studio.
-The following tables show the availability status of selected models across regions and special scopes.
+Copilot Studio models vary by intended use, release status, and region. You can see each model's tags when you
+change your agent's AI model
+.
+The following tables show selected models' regional availability. GA means general
```

---

## HIGH: Control Review Recommended

### 1. Assign AI provider access to users and groups

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-ai-provider-user-sec-group-access
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

**What Changed:**
```diff
--- +++ @@ -1,6 +1,4 @@ Assign AI provider access to users and groups
-Note
-Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat. There are no changes to security, compliance, and privacy for organizations.
 Organizations that use third-party AI providers with Microsoft Copilot or Copilot Studio can restrict access to those AI providers by assigning permissions to specific users or Microsoft Entra ID security groups.
 AI provider user and group access
 You can assign AI providers to selected users or groups in the Microsoft 365 admin center. For more information, see:

```

---

### 2. Create and deploy a DLP policy

**URL:** https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Compliance features)

**What Changed:**
```diff
--- +++ @@ -175,6 +175,11 @@ Change the state to
 Turn it on right away
 . The policy is fully deployed. Monitor DLP alerts and DLP activity explorer. Address alerts.
+Reordering DLP policies
+Microsoft Purview DLP lets you reorder policies to change their priority without changing their rules, conditions, or actions.
+DLP uses internal ordering values with gaps between them to maintain the priority order displayed in the portal. These gaps allow the service to move a policy without updating every policy in the list.
+After repeated moves, a gap can become too small to accommodate another move. When this happens, the service redistributes the internal ordering values to create new gaps. This preserves your chosen policy order but can require additional policies to be updated and synchronized, including policies you didnât move.
+Affected policies may show a new Last modified timestamp or a change in Policy sync status while the updates are distributed. These changes reflect updates to policy ordering, not changes to the policiesâ rules, conditions, or actions. There is no fixed number of moves that triggers this process; it depends on the existing order and which policies you move.
 Was this page helpful?
 Yes
 No

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-admin-experience |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-manage |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*