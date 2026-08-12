# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-12
**Run Time:** 2026-08-12T10:51:37.787635+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 4 |
| MEDIUM Changes | 1 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | copilot-teams-transcription | HIGH | 4.2 | Update portal-walkthrough |
| 2 | release-notes | HIGH | 4.12 | Update portal-walkthrough |
| 3 | apply-sensitivity-label-automatically | HIGH | 1.5, 2.2 | Update portal-walkthrough |
| 4 | cowork-models | HIGH | 4.15 | Update portal-walkthrough |
| 5 | agent-registry | CRITICAL | None | Monitor |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Copilot in Teams meetings

**URL:** https://learn.microsoft.com/en-us/microsoftteams/copilot-teams-transcription
**Section:** Copilot Administration
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 4.2: Control 4.2: Copilot in Teams Meetings Governance
  - File: `controls/pillar-4-operations/4.2-teams-meetings-governance.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.2/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -46,7 +46,8 @@ Only during the meeting
 When organizers create a meeting or event, they can set Copilot's value to
 Only during the meeting
-from the dropdown list in their meeting options. Once someone with a Microsoft 365 Copilot license selects the Copilot button during the meeting or event, Copilot runs for all licensed users. This option relies on speech-to-text audio processing data that isn't saved after the meeting or event ends. Users can't access Copilot in Teams and its history after the meeting or event.
+from the dropdown list in their meeting options. Once someone with a Microsoft 365 Copilot license selects the Copilot button during the meeting or event, Copilot runs for all licensed users. This option relies on speech-to-text audio processing data that isn't saved after the meeting or event ends.
+Depending on your organization's Microsoft Purview retention policies, Copilot prompts and responses during meetings might be retained for compliance purposes, even if recording and transcription are turned off. This applies only to the Commercial cloud and doesn't apply to GCC or DoD cloud environments.
 To learn more about how organizers can use Copilot only during the meeting, see
 Use Microsoft 365 Copilot in Teams without recording a Teams meeting
 .
@@ -65,7 +66,7 @@ Require end-to-end encryption for sensitive Teams meetings
 .
 Note
-Microsoft 365 Copilot in Teams isn't currently available for GCC High and DoD.
+Microsoft 365 Copilot in Teams isn't currently available for GCC High.
 Prerequisites
 An add-on Microsoft 365 Copilot license for intended users. To learn more about the Microsoft 365 Copilot license, see
 Microsoft 365 Copilot documentation
@@ -77,7 +78,7 @@ -AllowTranscription
 parameter in the
 CsTeamsMeetingPolicy
-PowerShell cmdlet to manage your transcription policy. This setting's value impacts how, or if Copilot works for your users. The following table shows how the transcription policy works with the organizer's Copilot 
```

---

### 2. Microsoft 365 Copilot release notes

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.12: Control 4.12: Change Management for Copilot Feature Rollouts
  - File: `controls/pillar-4-operations/4.12-change-management-rollouts.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -30,6 +30,266 @@ Android
 iOS
 Mac
+August 11, 2026
+Updates released between July 28, 2026, and August 11, 2026.
+Microsoft 365 Copilot extensibility
+Parallel content and identity crawl improves content freshness
+[Web]
+Copilot connectors now run content crawl and identity crawl in parallel, making ingested content available to users faster than before.
+Details:
+What changed:
+Previously, content crawl and identity crawl executed sequentially, causing delays before content became accessible in Copilot. Now, both crawls run in parallel, reducing total processing time. This change improves content freshness and availability without compromising security or permission accuracy.
+Why:
+Sequential crawling delayed content availability, impacting user productivity.
+Parallel execution enables:
+Faster ingestion of new and updated content
+Quicker reflection of identity and permission changes
+Try this:
+Add or update content in your connected data source.
+Observe that content appears in Copilot results sooner than before.
+Check that permissions and identity information remain accurate.
+Why this matters:
+Faster content availability helps users access the latest information promptly, supporting timely decision-making.
+Business impact:
+Teams benefit from reduced latency in content updates, improving collaboration and information flow.
+Personal impact:
+You spend less time waiting for new content to appear, increasing efficiency in your work.
+Learn:
+Deploy the ServiceNow Knowledge Copilot connector
+ServiceNow connectors support role-based permissions
+[Web]
+ServiceNow Knowledge and Catalog connectors now enforce access permissions based on user roles such as admin, knowledge manager, and knowledge admin.
+Details:
+What changed:
+Earlier, permissions in ServiceNow Knowledge and Catalog connectors were determined only by user criteria without considering roles. Now, the connectors evaluate access based on the user's assigned roles in ServiceNow, enab
```

---

### 3. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Portal references)

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
--- +++ @@ -98,11 +98,7 @@ These files can be auto-labeled at rest before or after the auto-labeling policies are created. Files can't be auto-labeled if they're part of an open session (the file is open).
 Currently, attachments to list items aren't supported and won't be auto-labeled.
 Maximum of 100,000 automatically labeled files in your tenant per day.
-Maximum of 100 auto-labeling policies per tenant, each targeting up to 100 locations (SharePoint sites or OneDrive individual users or groups) when you specify specific locations by using the
-Included
-or
-Excluded
-options. If you keep the default configuration of
+Maximum of 100 auto-labeling policies per tenant. In the portal, each policy can target up to 100 explicitly included or excluded locations (SharePoint sites or OneDrive individual users or groups). If you keep the default configuration of
 All
 , this configuration is exempt from the 100 locations maximum.
 Existing values for modified, modified by, and the date aren't changed as a result of auto-labeling policiesâfor both simulation mode and when labels are applied.
@@ -1139,6 +1135,13 @@ You can use
 Security & Compliance PowerShell
 to create and configure auto-labeling policies. This means you can fully script the creation and maintenance of your auto-labeling policies, which also provides a more efficient method of specifying multiple locations for SharePoint and OneDrive.
+To target more than 100 SharePoint sites, associate an existing SharePoint adaptive scope with the policy by using the
+-SharePointAdaptiveScopes
+parameter (or
+-SharePointAdaptiveScopesException
+for exclusions) with
+New-AutoSensitivityLabelPolicy
+. This doesn't increase the portal limit; instead, it replaces static site enumeration with dynamic adaptive-scope membership.
 Before you run the commands in PowerShell, you must first
 connect to Security & Compliance PowerShell
 .

```

---

### 4. Copilot Cowork available models

**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
**Section:** Copilot Cowork
**Classification:** HIGH (Policy language)

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
--- +++ @@ -45,32 +45,36 @@ Most day-to-day work.
 The default. Cowork picks the model best suited to the task you describe.
 Claude Sonnet 5
-Efficient for everyday tasks and fast responses such as drafting, quick lookups, and day-to-day work.
-Use when you want a shorter response cycle for common tasks. See
+Everyday tasks and fast responses such as drafting, quick lookups, and day-to-day work.
+Use when you want a shorter response cycle for common tasks. Learn more about data handling in
 Anthropic subprocessor
-info for data handling.
+.
 Claude Opus 4.8
-For complex, high-stakes work like deep reasoning, multi-step analysis, complex research, and writing.
-Use for work that needs careful reasoning across several sources or steps. See
+Complex, high-stakes work like deep reasoning, multi-step analysis, complex research, and writing.
+Use for work that needs careful reasoning across several sources or steps. Learn more about data handling in
 Anthropic subprocessor
-info for data handling.
+.
+GPT 5.6 Sol
+Complex work like research.
+Most capable GPT 5.6 model for complex work.
+GPT 5.6 Terra
+High volume work.
+Balanced GPT 5.6 model.
 GPT 5.5 (Frontier)
-Versatile across task types and great for verbose writing and citations.
-Hosted in Azure AI Foundry
+Verbose writing and citations. Versatile across task types.
+Hosted in Azure AI Foundry.
 Claude Fable 5 (Preview)
-For your toughest, most demanding challenges.
-In preview and off by default. An admin must turn it on in the
-Microsoft 365 admin center
-under Copilot settings before it appears in your picker. Requires data retention. When you select Fable 5, your prompts and responses are retained by the model provider, and Cowork shows a banner while it's selected. See
+Your toughest, most demanding challenges.
+In preview and off by default. An admin must turn it on in the Microsoft 365 admin center under Copilot settings before it appears in your picker. Requires data retention. When you select Fable 5, yo
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft Agent 365 registry sync
**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry
**Classification:** CRITICAL (Deprecation notice)

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