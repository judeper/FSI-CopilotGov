# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-19
**Run Time:** 2026-09-19T13:34:46.208842+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| MEDIUM Changes | 3 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | connect-to-ai-models | MEDIUM | 3.8a, 2.7, 1.10 | Update portal-walkthrough |
| 2 | connect-to-ai-subprocessor | HIGH | 3.8a, 2.7, 1.10 | Update portal-walkthrough |
| 3 | dlp-policy-tips-reference | MEDIUM | 2.1 | Update portal-walkthrough |
| 4 | audit-log-activities | MEDIUM | 3.1, 2.2, 2.13, 1.15 | Update portal-walkthrough |
| 5 | authoring-select-agent-model | HIGH | 4.14, 1.16 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Connect to xAI models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.10/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.10/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -19,7 +19,7 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Connect to SpaceXAI models
+Connect to SpaceXAI models (as an independent processor)
 Feedback
 Summarize this article for me
 You can now use SpaceXAI models within your Microsoft products. These models are hosted by SpaceXAI outside of Microsoft. You can elect to use SpaceXAI models with Copilot Studio in Microsoft 365.

```

---

### 2. Anthropic as a Microsoft subprocessor

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.10/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.10/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -68,9 +68,9 @@ in EU/EFTA and UK to enable Anthropic as the default model for Copilot in Microsoft 365 apps. For more information, see
 Copilot in Microsoft 365 apps with Anthropic models
 .
-As of July 22, 2026, a new setting is available in the Microsoft 365 admin center that allows non-federal customers in Government Community Cloud (GCC) to use Anthropic models. For more information, see the
-Enable the use of Anthropic models for non-federal customers in GCC
-section later in this article.
+As of July 22, 2026, a new setting is available in the Microsoft 365 admin center that allows non-federal customers in Government Community Cloud (GCC) to use Anthropic models. For more information, see
+Anthropic operated models for non-federal customers in GCC
+.
 Anthropic models aren't available for federal customers in GCC or for any customers in GCC High and Department of Defense (DoD) environments. They're also not available in other sovereign clouds. The option to use Anthropic models doesn't appear in the Microsoft 365 admin center for these government and sovereign cloud customers.
 Opt-in to use Anthropic's models
 If your organization is in a region that has Anthropic as a subprocessor set to
@@ -168,55 +168,6 @@ Disable Anthropic as a Microsoft subprocessor
 .
 Once you disable Anthropic as an AI subprocessor, users won't have the option to use Anthropic's AI models. You can choose to enable Anthropic models at a later date if desired.
-Enable the use of Anthropic models for non-federal customers in GCC
-Note
-The information in this section applies only to non-federal customers in Government Community Cloud (GCC). It doesnât apply to federal customers in GCC or to all customers in GCC High and Department of Defense (DoD) environments.
-As of July 22, 2026, a new setting is available in the Microsoft 365 admin center that allows non-federal customers in GCC to use Anthropic models. This capability is optional and the setting is disabled by default.

```

---

### 3. DLP policy tips reference

**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-tips-reference
**Section:** Data Loss Prevention (DLP)
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.1: Control 2.1: DLP Policies for Microsoft 365 Copilot Interactions
  - File: `controls/pillar-2-security/2.1-dlp-policies-for-copilot.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.1/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -60,11 +60,11 @@ Customized Oversharing Dialog
 Yes
 No
-No
+Yes
 Wait on Send dialog support for Oversharing for Outlook for Microsoft 365
 Yes
 No
-No
+Yes
 Microsoft provided sensitive information types (SIT)
 Yes
 Yes

```

---

### 4. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/3.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/incident-and-risk/agent-behavioral-incident-playbook.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1676,7 +1676,7 @@ Both the FilePreviewed and FileAccessed events indicate that a user's call led to a read of the file (or a read of a thumbnail rendering of the file). While these events are intended to align with preview versus access intention, the event distinction isn't a guarantee of the user's intent.
 What causes FileAccessed audit events in Insider Risk Management scenarios?
 Creating a case in Insider Risk Management and enabling Content Explorer generates and records a FileAccessed event in the audit log. In this scenario, the event is generated by the Insider Risk Management/Content Explorer workflow rather than by a direct user file-open action, and the same ApplicationId value,
-92876b03-76a3-4da8-ad6a-0511ffdf8647
+00001111-aaaa-2222-bbbb-3333cccc4444
 , is used for these events. This is important for administrators because it helps distinguish these system-generated FileAccessed events from other FileAccessed activity during an investigation. You can use the ApplicationId field as one of the properties to help identify or filter these specific events when reviewing audit log results.
 The app@sharepoint user in audit records
 In audit records for some file activities (and other SharePoint-related activities), you might notice the user who performed the activity (identified in the User and UserId fields) is app@sharepoint. This user means that an application performed the activity. In this case, the application was granted permissions in SharePoint to perform organization-wide actions (such as searching a SharePoint site or OneDrive account) on behalf of a user, admin, or service. This process of giving permissions to an application is called

```

---

### 5. Select an agent model

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Section:** Copilot Studio
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`
- Control 1.16: Control 1.16: Copilot Tuning Governance
  - File: `controls/pillar-1-readiness/1.16-copilot-tuning-governance.md`

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
--- +++ @@ -82,19 +82,19 @@ Retired
 GPT-4.1
 General
-Default
-Default
-Default
-Default
-Default
-Default
-Default
-Default
-Default
-Default
-Default
-Default
-Default
+GA (cross-geo)
+GA
+GA (cross-geo)
+GA (cross-geo)
+GA
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA (cross-geo)
+GA
+GA
 GPT-5 Chat
 General
 GA (cross-geo)
@@ -172,19 +172,19 @@ Experimental (early access environment)
 GPT-5.5 Chat
 General
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA (cross-geo)
-GA
+Default
+Default
+Default
+Default
+Default
+Default
+Default
+Default
+Default
+Default
+Default
+Default
+Default
 GPT-5.5 Reasoning
 Deep
 -

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Connect to xAI models
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models
**Classification:** MEDIUM (General content update)

---

### 2. DLP policy tips reference
**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-tips-reference
**Classification:** MEDIUM (General content update)

---

### 3. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Classification:** MEDIUM (General content update)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*