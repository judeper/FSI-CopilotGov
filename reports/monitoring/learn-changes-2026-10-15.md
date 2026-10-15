# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-15
**Run Time:** 2026-10-15T14:32:25.430894+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 6 |
| MEDIUM Changes | 3 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | HIGH | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | endpoint-dlp-learn-about | MEDIUM | 2.1 | Update portal-walkthrough |
| 3 | apply-sensitivity-label-automatically | CRITICAL | 1.5, 2.2 | Update portal-walkthrough |
| 4 | edisc | MEDIUM | 3.3 | Update portal-walkthrough |
| 5 | ...ication-fundamentals-publish-channels | MEDIUM | 2.14, 4.14 | Update portal-walkthrough |
| 6 | connected-platforms | CRITICAL | 1.13, 2.14, 4.13, 2.13 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** HIGH (Policy language)

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
--- +++ @@ -26,9 +26,19 @@ Copilot Chat (Basic) license
 Microsoft 365 Copilot (Basic) license
 Microsoft 365 Copilot (Premium) license
+Usage-based billing capabilities
 Securely interact with Copilot Chat using web data only
 Securely interact with Copilot Chat using web data only
 Securely interact with Copilot using web data and work data (
+Microsoft Graph
+and
+Work IQ
+)
+Securely interact with Copilot,
+Copilot Cowork
+and
+Copilot Code
+using web and work data (
 Microsoft Graph
 and
 Work IQ
@@ -54,8 +64,17 @@ the Microsoft 365 Copilot add-on license with
 priority access
 to the full experience of Copilot in Word, Excel, PowerPoint, and OneNote.
-You have access to
-Microsoft Copilot Cowork
+For more information, see
+Microsoft 365 Copilot (Premium) license and experience
+.
+You
+have
+the Microsoft 365 Copilot add-on license with
+priority access
+to the full experience of Copilot in Word, Excel, PowerPoint, and OneNote, and access to
+Copilot Cowork
+and
+Copilot Code
 via
 usage-based billing
 .
@@ -71,9 +90,15 @@ and
 Work IQ
 ).
+Includes access to Cowork, Code, and agents that use web and work data (
+Microsoft Graph
+and
+Work IQ
+). Usage is billed based on consumption.
 Basic usage management controls and reporting for admins.
 Basic usage management controls and reporting for admins.
 Added advanced management controls and analytics for admins.
+Added usage monitoring, reporting, and cost management controls for admins.
 Note
 In-product labels are displayed in Microsoft 365 apps like Word, Excel, PowerPoint, and OneNote, and in the Microsoft Copilot app, to help users identify their Copilot experience.
 Copilot features in Microsoft 365 apps
@@ -94,6 +119,7 @@ Microsoft Copilot Chat (Basic) license and experience
 Microsoft 365 Copilot (Basic) license and experience
 Microsoft 365 Copilot (Premium) license and experience
+Usage-based billing capabilities
 Copilot Chat (Basic)
 is the standalone baseline experience included with eligible Micros
```

---

### 2. Endpoint DLP

**URL:** https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about
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
--- +++ @@ -472,13 +472,10 @@ .tsv
 Unsupported File types
 Endpoint DLP does not support monitoring for the following file types:
-.exe
-.dll
 .sys
 .lib
 .obj
 .mui
-.spl
 .drv
 .pf
 .crdownload

```

---

### 3. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -22,8 +22,10 @@ .
 My simulation results look wrong or incomplete.
 See
+Auto-labeling classification and simulation concepts
+to distinguish available classification, policy matches, and actual labeling. For simulation requirements and workflow, see
 Learn about simulation mode
-â the caveats cover the most common causes (12-hour completion window, single-policy scope, files modified after the run, and the sensitive info type created-after-modification rule).
+.
 I turned on a policy after simulation and want to review coverage.
 See
 Review coverage by simulation context
@@ -32,12 +34,10 @@ See
 Apply default sensitivity labels from SharePoint document libraries to existing files
 .
-A specific file wasn't labeled and I expected it to be.
-Select the policy, then
-View details
-in the policy details panel. In the newer review experience, open
-Labeling failures
-to investigate the file. For failure navigation, reasons, and fixes, see
+A file wasn't labeled, or has an unexpected label.
+Start with
+Why was â or wasn't â a specific file labeled?
+to choose the checks for your file. For a reported failure, see
 Resolve auto-labeling failures in SharePoint and OneDrive files
 .
 My active policy has stopped matching Exchange email.
@@ -460,10 +460,10 @@ Prerequisites for auto-labeling policies
 .
 [ ]
-The files you expect to be labeled were created or modified after the sensitive information types were created or modified.
-Auto-labeling only evaluates content that was created or modified after the SIT was created or last modified. To classify older unchanged files, run
-on-demand classification
-.
+Classification covers the sensitive information types you intend to use.
+Policies can evaluate existing files using available classification results, but changing a custom SIT doesn't by itself refresh those results for unchanged files. Review
+when historical files need updated classification
+, including the effects of on-demand classification on activ
```

---

### 4. eDiscovery notable changes (classic experiences retired Aug 31 2025)

**URL:** https://learn.microsoft.com/en-us/purview/edisc
**Section:** eDiscovery
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 3.3: Control 3.3: Purview eDiscovery for Copilot-Generated Content
  - File: `controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/3.3/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.3/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.3/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.3/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -41,7 +41,6 @@ to remove or add members to the case to manage access to these searches. You can also select
 Content Search
 in eDiscovery to create a Content Search case in your organization that contains all new and existing content searches.
-The Content Search case has the same capability as other user-created cases. You can create holds, review sets, and more in the content search case, depending on your subscription.
 For more information about the changes to Content Search in eDiscovery, check out the following video:
 Custodians
 : In previous versions of eDiscovery,

```

---

### 5. Publish and deploy Copilot Studio agents

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
**Section:** Copilot Studio
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -2,6 +2,14 @@ Note
 This article describes features used in agents or agent flows powered by the
 standard harness
+.
+Important
+This article includes information about
+Azure Bot Service skills
+, a code-based way to extend the capabilities of an agent in the standard harness. These skills shouldn't be confused with
+agentic skills
+in the GitHub Copilot harness. Learn more about how to use agentic skills in
+Skills overview for agents
 .
 By using Copilot Studio, you can publish agents that engage with your customers on multiple platforms or channels. For example, live websites, mobile apps, Microsoft Copilot, and messaging platforms like Teams and Facebook.
 Each time you update your agent, you can publish it again from within Copilot Studio. Publishing your agent applies to all the channels associated with your agent.
@@ -186,8 +194,8 @@ A user can't send or upload attachments to the chat. If they try to send an attachment, the agent replies:
 Looks like you tried to send an attachment. Currently, I can only process text. Please try sending your message again without the attachment.
 This limitation applies to all channels, even if the channel or user-facing experience supports attachments. For example, this limitation applies to the Direct Line API and Microsoft Teams.
-Attachments can be supported if the message is sent to a skill, where the skill bot supports the processing of attachments. Learn more in
-Use Microsoft Bot Framework skills in Copilot Studio
+Attachments can be supported if the message is sent to an Azure Bot Service skill, where the skill bot supports the processing of attachments. Learn more in
+Use Azure Bot Service skills in Copilot Studio
 .
 Next steps
 Article

```

---

### 6. Connected platforms in Microsoft Agent 365 (manual sync)

**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms
**Section:** Agent Governance
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -15,6 +15,21 @@ creates the source-platform credentials,
 grants the required permissions, and enables platform-side telemetry when
 applicable.
+Security model
+Connected platform connections are read-only by design:
+Agent 365 never invokes, executes, or interacts with agents in the source
+platform.
+Agent 365 doesn't write to, modify, or delete resources in the source
+platform. The only exception is an explicit administrator action to remove
+a synchronized agent, which requires a separate, optional delete permission
+that you can choose not to grant.
+Observability data is read from the telemetry destination that the source
+platform already writes to on its own, such as an activity bucket or a
+managed logging service. Agent 365 doesn't write to that destination.
+For platform-specific permissions, see the relevant guide in
+Supported
+platforms
+.
 Manage external platform connections
 Create and manage external platform connections from the
 Connected
@@ -67,6 +82,44 @@ Yes
 Coming soon
 Connect Snowflake Cortex
+Where supported, observability provides session, exception, runtime, and
+tool-call metrics on the agent's
+Activity
+tab. Coverage varies by
+platform. For metric definitions and platform coverage, see
+Third-party
+agent observability (Frontier)
+.
+Current limitations
+Manual synchronization only.
+Agent 365 doesn't currently sync on a
+schedule, and Microsoft doesn't prescribe a fixed synchronization interval.
+Choose a cadence based on how often agents change in the source platform and
+your organization's governance requirements. Re-run
+Sync agents
+after
+you add, update, or remove agents in the source platform, and before reviews
+that depend on current registry data.
+Deletion reconciliation isn't guaranteed.
+Synchronization doesn't
+currently guarantee that an agent removed from the source platform is
+automatically removed from the Microsoft 365 agent registry. Confirm the
+current behavior with your platform administrator, 
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Endpoint DLP
**URL:** https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about
**Classification:** MEDIUM (General content update)

---

### 2. eDiscovery notable changes (classic experiences retired Aug 31 2025)
**URL:** https://learn.microsoft.com/en-us/purview/edisc
**Classification:** MEDIUM (General content update)

---

### 3. Publish and deploy Copilot Studio agents
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*