# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-10
**Run Time:** 2026-09-10T13:57:04.895391+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| HIGH Changes | 1 |
| MEDIUM Changes | 2 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | MEDIUM | 1.4 | Update portal-walkthrough |
| 2 | microsoft-365-copilot-setup | HIGH | 2.6 | Update portal-walkthrough |
| 3 | ...t-365-copilot-search-admin-experience | MEDIUM | 1.4 | Update portal-walkthrough |
| 4 | apply-sensitivity-label-automatically | CRITICAL | 2.2, 1.5 | Update portal-walkthrough |
| 5 | copilot-tuning-admin-guide | HIGH | 1.16 | Update portal-walkthrough |
| 6 | m365-agents-admin-guide | HIGH | None | Review and update |

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

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -327,11 +327,11 @@ Think deeper
 For complex or more open-ended questions, Copilot might detect that the prompt requires advanced reasoning. In these cases, Copilot uses a deeper reasoning model, taking its time to craft a plan, gather and comprehend all relevant context, and check its work before providing a thorough response.
 These options update as new models become available.
-Copilot Control System
+Copilot controls
 In the admin center, use the
-Copilot Control System
+Copilot controls
 to manage Copilot Chat experiences, including Copilot Chat (Basic), Microsoft 365 Copilot (Basic), and Microsoft 365 Copilot (Premium).
-In the Copilot Control System, you can configure how users interact with Copilot and related AI experiences, including:
+In Copilot controls, you can configure how users interact with Copilot and related AI experiences, including:
 Control whether Copilot Chat is
 pinned across experiences
 , such as in the Microsoft 365 app and other Copilot surfaces, based on licensing.

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
--- +++ @@ -205,13 +205,13 @@ Step 3: Configure settings for Copilot
 â
 Configure more Copilot features
-You can manage settings by using the Copilot Control System. It provides centralized access to admin features and controls that benefit your organization.
+You can manage settings by using Copilot controls. They provide centralized access to admin features and capabilities that benefit your organization.
 To access these settings, go to the
 Microsoft 365 admin center
 >
 Copilot
 .
-With the Copilot Control System, you can:
+With Copilot controls, you can:
 View the status of Copilot license assignments.
 Access the latest information on Copilot.
 Manage data security and compliance controls.
@@ -262,7 +262,7 @@ Focus on preventing oversharing by limiting external sharing, restricting access to certain files or folders, and setting up alerts to notify you of any unusual activity.
 Use sensitivity labels to classify and protect sensitive information. These labels allow you to automatically encrypt files containing sensitive data or restrict access to files marked as "confidential."
 For more information on these important data security steps, see
-Copilot Control System security and governance
+Copilot controls security and governance
 .
 Operate
 â
@@ -273,13 +273,13 @@ Microsoft 365 usage reports in the admin center
 . These tools provide organizational leaders and IT decision makers with insights into readiness, adoption, impact, and user sentiment.
 For more information, see the following articles:
-Copilot Control System measurement and reporting
+Copilot controls measurement and reporting
 Open the Microsoft Copilot Dashboard from Viva Insights
 Learn more about the Microsoft Copilot Dashboard from Viva Insights
 Microsoft 365 reports in the admin center - Microsoft Copilot usage
 Microsoft 365 reports in the admin center - Microsoft Copilot readiness
 Related content
-Copilot Control System overview
+Copilot controls overview
 Microsoft Copilot setup gu
```

---

### 3. Copilot Search admin experience

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -156,9 +156,9 @@ That makes it easier to sort and filter bookmarks in the admin center. Your users never see the assigned categories.
 Create bookmark answers
 In the Microsoft 365 admin center:
-Go to the
-Copilot
-Control System and select
+Go to
+Copilot controls
+and select
 Search
 .
 Select

```

---

### 4. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -535,6 +535,16 @@ ), this option uses SharePoint managed properties in the same way as they are used for DLP policies. Use exact string matches; regex patterns aren't supported. For more information about managed properties as a search method, see
 Manage the search schema in SharePoint
 .
+Important
+When a document property is mapped to a SharePoint managed property, such as
+RefinableString11
+, values containing an ampersand (
+&
+) might not match an auto-labeling rule that uses
+Document property is
+. For example, documents with the mapped value
+Billing & payment document
+might remain unlabeled. Plan around this known limitation rather than relying on a future fix. Consider using a classification value without ampersands, keeping the document metadata and rule value consistent. Before deploying broadly, review simulation results and confirm actual label application in a limited scope.
 If you have an auto-labeling policy configured to replace a manually applied label but another active auto-labeling policy is configured to apply a label without this option, the label won't be replaced. Because simulation shows the result of one policy, simulation results for the replace label policy show the label as replaced but the conflict is resolved when all policies run.
 If you have an auto-labeling policy configured to remove a label but another active auto-labeling policy is configured to apply a label and the conditions are matched, the label will be applied rather than removed. Because simulation shows the result of one policy, simulation results for the label removal policy show the label as removed but the conflict is resolved when all policies run.
 If you choose to remove a label that applies encryption, encryption is automatically removed with the label.
@@ -1018,10 +1028,10 @@ Simulation reports every file that matches the policy's conditions. On activation, the service only re-evaluates files whose state has recently changed (new, modified, or e
```

---

### 5. Copilot Tuning admin guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-admin-guide
**Section:** Copilot Extensibility
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.16: Control 1.16: Copilot Tuning Governance
  - File: `controls/pillar-1-readiness/1.16-copilot-tuning-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -22,7 +22,7 @@ Microsoft Copilot Tuning admin guide (early access preview)
 Feedback
 Summarize this article for me
-Microsoft Copilot Tuning (early access preview) is an AI customization capability that enables organizations to create task-specific Copilot agents by tuning large language models (LLMs) with their own organizational data. AI admins manage Copilot Tuning through the Copilot control system in the Microsoft 365 admin center. Copilot Tuning provides multiple layers of control to balance innovation with governance.
+Microsoft Copilot Tuning (early access preview) is an AI customization capability that enables organizations to create task-specific Copilot agents by tuning large language models (LLMs) with their own organizational data. AI admins manage Copilot Tuning through Copilot controls in the Microsoft 365 admin center. Copilot Tuning provides multiple layers of governance to balance innovation with oversight.
 This article describes how administrators manage Microsoft Copilot Tuning, including role requirements, availability controls, agent lifecycle management, and data protection considerations.
 Important
 Microsoft Copilot Tuning is currently available to a limited set of customers through early access programs. Access through

```

---

## HIGH: Control Review Recommended

### 1. M365 Agents admin guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/m365-agents-admin-guide
**Section:** Copilot Extensibility
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -34,7 +34,7 @@ Helps you understand how to manage, assign, and deploy agents
 Provides resources about Copilot and agent security, compliance, and privacy
 Note
-You must have specific permissions for your tenant to configure, manage, assign, and deploy agents in Copilot Control System within Microsoft 365 admin center. For more information, see
+You must have specific permissions for your tenant to configure, manage, assign, and deploy agents in Copilot controls within Microsoft 365 admin center. For more information, see
 Admin permissions
 .
 Identify your Copilot licensing scenario
@@ -243,7 +243,7 @@ Microsoft 365 Agents Toolkit
 .
 Set agent policies
-Agent policies refer to the tenant settings you can make as an administrator in the Copilot Control System within Microsoft 365 admin center. Agent policies relate to the available settings for all agents in your tenant. Additionally, these policies include agent access, agent sharing, and agent publishing settings. You must have appropriate
+Agent policies refer to the tenant settings you can make as an administrator in Copilot controls within Microsoft 365 admin center. Agent policies relate to the available settings for all agents in your tenant. Additionally, these policies include agent access, agent sharing, and agent publishing settings. You must have appropriate
 admin permissions
 to access Copilot agent settings for your tenant. Setting
 agent policies
@@ -293,7 +293,7 @@ admin roles in the Microsoft 365 admin center
 .
 Settings for all agents
-In the Copilot Control System within Microsoft 365 admin center, you can manage the following overall Copilot settings:
+In Copilot controls within Microsoft 365 admin center, you can manage the following overall Copilot settings:
 User access to Copilot in different products or services where controls are available
 Copilot data access when securely retrieving and handling information
 Copilot actions pertaining to available functionality and use
@@ 
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Classification:** MEDIUM (General content update)

---

### 2. Copilot Search admin experience
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience
**Classification:** MEDIUM (General content update)

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*