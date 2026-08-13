# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-13
**Run Time:** 2026-08-13T10:53:04.448930+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 5 |
| MEDIUM Changes | 3 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | connect-to-ai-models | CRITICAL | 3.8a, 1.10, 2.7 | Update portal-walkthrough |
| 2 | ...lot-ai-provider-user-sec-group-access | MEDIUM | None | Review optional |
| 3 | apply-sensitivity-label-automatically | HIGH | 1.5, 2.2 | Update portal-walkthrough |
| 4 | audit-log-activities | CRITICAL | 3.1, 1.15, 2.13 | Update portal-walkthrough |
| 5 | cowork-models | MEDIUM | 4.15 | Update portal-walkthrough |
| 6 | monitor-your-data | MEDIUM | 4.11 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Connect to xAI models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models
**Section:** Copilot Administration
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`

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
--- +++ @@ -19,40 +19,40 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Connect to xAI's models
+Connect to SpaceXAI models
 Feedback
 Summarize this article for me
-You can now use xAI models within your Microsoft products. These models are hosted by xAI outside of Microsoft. You can elect to use XAI's models with Copilot Studio in Microsoft 365.
-xAI models can help people in your organization with some of the following:
+You can now use SpaceXAI models within your Microsoft products. These models are hosted by SpaceXAI outside of Microsoft. You can elect to use SpaceXAI models with Copilot Studio in Microsoft 365.
+SpaceXAI models can help people in your organization with some of the following:
 Summarize complex information
 Answer questions using source material
 Synthesize across multiple sources
 Idea generation, drafting and editing
-When your organization chooses to use an xAI model, your organization is choosing to share your data with xAI to power Copilot Studio features. This data is processed outside all Microsoft managed environments and audit controls, therefore Microsoft's customer agreements, including the
+When your organization chooses to use a SpaceXAI model, your organization is choosing to share your data with SpaceXAI to power Copilot Studio features. This data is processed outside all Microsoft managed environments and audit controls, therefore Microsoft's customer agreements, including the
 Product Terms
 and
 Data Processing Addendum
-don't apply. In addition, Microsoft's data residency commitments, audit and compliance requirements, service level agreements, and Customer Copyright Commitment don't apply to your use of xAI services. Instead, use of xAI's services is governed by xAI's
-Terms of service
-and
-Data processing addendum
+don't apply. In addition, Microsoft's data residency commitments, audit and compliance requirements, service level agreements, and Customer Copyright Commitment don't apply 
```

---

### 2. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`

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
--- +++ @@ -50,6 +50,10 @@ Failed
 view to see the failure reason. For the full list of reasons and fixes, see
 Resolve auto-labeling failures in SharePoint and OneDrive files
+.
+My active policy has stopped matching Exchange email.
+See
+Policy rule fails to load
 .
 I'm hitting a limit
 (100,000 files/day, 100 policies, 100 locations, or 4,000,000 files in simulation). See
@@ -508,6 +512,7 @@ You have
 enabled sensitivity labels for Office files in SharePoint and OneDrive
 .
+For OneDrive, the OneDrive account must be associated with the corresponding user account. A OneDrive account that isn't associated with its user account (sometimes called a detached OneDrive account) isn't supported for auto-labeling or simulation. Use a properly associated OneDrive account, or move the content to a supported SharePoint or OneDrive location, and then rerun simulation.
 At the time the auto-labeling policy runs, the file mustn't be open by another process or user. A file that's checked out for editing falls into this category, and similarly, all files in a library that's configured to
 require documents to be checked out
 .
@@ -1131,6 +1136,31 @@ Auto-labeling
 page. The total daily files labeled across all policies displays at the top of the page.
 Use this number when you're planning a new policy or troubleshooting whether the tenant is approaching its labeling limit.
+Policy rule fails to load
+In rare cases, a malformed rule in an auto-labeling policy can prevent the policy from loading correctly. The most common symptom is that Exchange messages stop matching an otherwise enabled auto-labeling policy, and there might not be any item-level labeling failure to review because the rule never loaded in the first place.
+This is different from the SharePoint and OneDrive item-level labeling failures described earlier in this section. Those failures mean a specific file was evaluated against the policy but couldn't be labeled (for example, because of file format or existing pr
```

---

### 3. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/3.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/incident-and-risk/agent-behavioral-incident-playbook.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1340,6 +1340,9 @@ Deleted connection by tenant admin
 DeletedGatewayClusterDatasourceAsAdmin
 A tenant admin deleted the connection.
+Deleted connection role assignment by tenant admin
+DeletedGatewayDatasourceByAdmin
+A tenant admin deleted the connection role assignment.
 Deleted workspace relation
 DeletedWorkspaceRelation
 Deleted workspace relation.
@@ -1427,6 +1430,9 @@ Updated authorization setting in GraphQL
 UpdatedAuthorizationSettingGraphQL
 Updated authorization setting in GraphQL.
+Updated connection role assignment by tenant admin
+UpdatedGatewayDatasourceByAdmin
+A tenant admin add or updates the connection role assignment.
 Updated git items selection
 GitItemsSelectionUpdated
 Updated git items selection.
@@ -3092,6 +3098,82 @@ Updated access policy associations
 AccessPolicyAssociationsUpdated
 Logged when a customer updates attribute or app associations to access policies that control access to organizational data.
+People Skills activities
+The following table lists the activities in People Skills (Viva) that are logged in the Microsoft 365 audit log. For more information about this feature, see
+People Skills documentation
+.
+Friendly name
+Operation
+Description
+Added custom skills
+CustomSkillsAdded
+Generated when a tenant administrator adds custom skills to the tenant skills library.
+Added graph skills
+GraphSkillsAdded
+Generated when a tenant administrator adds graph-based skills to the tenant library.
+Added skill from inference
+SkillAddedFromInference
+Generated when the system adds an inferred skill to a user profile via TBA-triggered inference.
+Added skill from learning
+SkillAddedFromLearning
+Generated when the system adds a skill inferred from learning activity.
+Added user skill
+UserSkillAdded
+Generated when a user adds a skill to their own profile.
+Applied external bulk tag
+ExternalBulkTagApplied
+Generated when a third-party application applies bulk content tags via the service-to-service (S2S) API.
+Changed 
```

---

### 4. Copilot Cowork available models

**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
**Section:** Copilot Cowork
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 4.15: Control 4.15: Copilot Cowork Governance
  - File: `controls/pillar-4-operations/4.15-copilot-cowork-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -39,47 +39,38 @@ Available models
 The model picker can include the following models and model modes, depending on what your organization allows.
 Model
-Best for
+Description
 Notes
 Auto
-Most day-to-day work.
+For most day-to-day work.
 The default. Cowork picks the model best suited to the task you describe.
+GPT 5.5 (Frontier)
+Capable model for medium effort work.
+Hosted in Azure AI Foundry.
+GPT 5.6 Sol
+Intelligent and efficient for hard workâ.
+n/a
+GPT 5.6 Terra
+Balanced effort for common tasksâ.
+n/a
+Opus 5
+For complex, high stakes work.
+n/a
 Claude Sonnet 5
-Everyday tasks and fast responses such as drafting, quick lookups, and day-to-day work.
+For everyday tasks and fast responses such as drafting, quick lookups, and day-to-day work.
 Use when you want a shorter response cycle for common tasks. Learn more about data handling in
 Anthropic subprocessor
 .
-Claude Opus 4.8
-Complex, high-stakes work like deep reasoning, multi-step analysis, complex research, and writing.
-Use for work that needs careful reasoning across several sources or steps. Learn more about data handling in
-Anthropic subprocessor
-.
-GPT 5.6 Sol
-Complex work like research.
-Most capable GPT 5.6 model for complex work.
-GPT 5.6 Terra
-High volume work.
-Balanced GPT 5.6 model.
-GPT 5.5 (Frontier)
-Verbose writing and citations. Versatile across task types.
-Hosted in Azure AI Foundry.
 Claude Fable 5 (Preview)
-Your toughest, most demanding challenges.
+For your toughest, most demanding challenges.
 In preview and off by default. An admin must turn it on in the Microsoft 365 admin center under Copilot settings before it appears in your picker. Requires data retention. When you select Fable 5, your prompts and responses are retained by the model provider, and Cowork shows a banner while it's selected. Learn more about data handling in
 Data retention
 and
 Anthropic subprocessor
 .
-Sonnet + Opus Advisor
-Everyday tasks with expert-level guidance. A paired mode w
```

---

### 5. Create workbooks

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/monitor-your-data
**Section:** Microsoft Sentinel
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 4.11: Control 4.11: Microsoft Sentinel Integration for Copilot Events
  - File: `controls/pillar-4-operations/4.11-sentinel-integration.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -67,7 +67,7 @@ Azure portal
 From the details pane, select
 Save
-, and then select the location where you want to save the workbook. Saving the workbook creates an Azure resource in the selected location based on the relevant template. Only the workbook's JSON file is saved in this location, and no data.
+, then select the location where you want to save the workbook. Saving the workbook creates an Azure resource in the selected location based on the relevant template. Only the workbook's JSON file is saved in this location, and no data.
 From the details pane, select
 View saved workbook
 to open it for editing.
@@ -120,7 +120,7 @@ Resource type
 to
 Log Analytics
-, and then choose one or more workspaces.
+, then choose one or more workspaces.
 We recommend that your query uses an
 Advanced Security Information Model (ASIM) parser
 and not a built-in table. A query that uses an ASIM parser supports any current or future relevant data source rather than a single data source.
@@ -217,7 +217,7 @@ | where OperationName == "Create role assignment"
 | project OperationName, RoleAssignmentTime = TimeGenerated, user = Caller) on user
 | project-away user1
-See more information on the following items used in the sample queries above, in the Kusto documentation:
+See more information on the following items used in the preceding examples in the Kusto documentation:
 where
 operator
 extend
@@ -246,8 +246,7 @@ Other resources:
 KQL quick reference
 Kusto Query Language learning resources
-Related articles
-For more information, see:
+Related content
 Commonly used Microsoft Sentinel workbooks
 Azure Monitor workbooks
 Feedback

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Assign AI provider access to users and groups
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-ai-provider-user-sec-group-access
**Classification:** MEDIUM (General content update)

---

### 2. Copilot Cowork available models
**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
**Classification:** MEDIUM (General content update)

---

### 3. Create workbooks
**URL:** https://learn.microsoft.com/en-us/azure/sentinel/monitor-your-data
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/microsoft-365/copilot/cowork/whats-new | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new |
| https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models | https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models |
| https://learn.microsoft.com/microsoft-365/copilot/discovery-setting-ai-experiences | https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences |
| https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits | https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits |
| https://learn.microsoft.com/microsoft-scout/overview | https://learn.microsoft.com/en-us/microsoft-scout/overview |
| https://learn.microsoft.com/microsoft-scout/get-started | https://learn.microsoft.com/en-us/microsoft-scout/get-started |
| https://learn.microsoft.com/microsoft-scout/admin-access-overview | https://learn.microsoft.com/en-us/microsoft-scout/admin-access-overview |
| https://learn.microsoft.com/microsoft-scout/admin-intune-setup | https://learn.microsoft.com/en-us/microsoft-scout/admin-intune-setup |
| https://learn.microsoft.com/microsoft-scout/manage-group-policy | https://learn.microsoft.com/en-us/microsoft-scout/manage-group-policy |
| https://learn.microsoft.com/microsoft-scout/use-microsoft-scout | https://learn.microsoft.com/en-us/microsoft-scout/use-microsoft-scout |
| https://learn.microsoft.com/microsoft-scout/faq | https://learn.microsoft.com/en-us/microsoft-scout/faq |
| https://learn.microsoft.com/microsoft-scout/microsoft-scout-responsible-ai-overview | https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-overview |
| https://learn.microsoft.com/microsoft-scout/microsoft-scout-responsible-ai-faq | https://learn.microsoft.com/en-us/microsoft-scout/microsoft-scout-responsible-ai-faq |
| https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms |
| https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*