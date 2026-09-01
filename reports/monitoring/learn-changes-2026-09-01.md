# Microsoft Learn Documentation Changes

**Run Date:** 2026-09-01
**Run Time:** 2026-09-01T14:23:48.731922+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | audit-log-activities | CRITICAL | 1.15, 2.13, 2.2, 3.1 | Update portal-walkthrough |
| 2 | cowork-manage-plugins | HIGH | 4.15 | Update portal-walkthrough |
| 3 | agent-settings | HIGH | 1.13, 2.14, 2.13, 4.13 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
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
--- +++ @@ -1523,6 +1523,9 @@ Accessed file
 FileAccessed
 User or system account accesses a file. After a user accesses a file, the system doesn't log the FileAccessed event again for the same user and file for the next five minutes.
+Archived file
+FileArchived
+A user or system account archived a file with Microsoft 365 Archive. When an automatic file archive policy archives the file, the event includes the policy ID, policy version, and the file's last access date.
 Changed record status to locked
 LockRecord
 The record status of a retention label that classifies a document as a record is locked. This status means the document wasn't modified or deleted. Only users assigned at least the contributor permission for a site can change the record status of a document.
@@ -1585,6 +1588,9 @@ Priority cleanup permanent delete of file
 PriorityCleanupFileDeleted
 An item is permanently deleted by a priority cleanup policy on OneDrive or SharePoint Online.
+Reactivated file
+FileUnarchived
+A file archived with Microsoft 365 Archive was reactivated and is available to access.
 Recycled a file
 FileRecycled
 User moves a file into the SharePoint Recycle Bin.
@@ -1603,6 +1609,9 @@ Renamed file
 FileRenamed
 User renames a document.
+Requested file reactivation
+FileUnarchiveRequested
+A user requested to reactivate a file archived with Microsoft 365 Archive.
 Restored file
 FileRestored
 User restores a document from the recycle bin of a site.
@@ -1660,6 +1669,34 @@ Compliance features
 . When an admin implements compliance features, such as retention policies, eDiscovery holds, and autoapplying sensitivity labels.
 In these and other scenarios, you might also notice that multiple audit records with app@sharepoint as the specified user were created within a short time frame, often within a few seconds of each other. This pattern also means they were probably triggered by the same user-initiated task. Also, the ApplicationDisplayName and EventData fields in the audit record
```

---

### 2. Manage Copilot Cowork plugins

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins
**Section:** Copilot Cowork
**Classification:** HIGH (UI element names)

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
--- +++ @@ -120,16 +120,46 @@ tab.
 Adjust the availability setting:
 Available to all users
-- All licensed Copilot users in your tenant can find and acquire the plugin.
+: All licensed Copilot users in your tenant can find and acquire the plugin.
 Available to specific users or groups
-- Only the users or security groups you specify can see the plugin.
+: Only the users or security groups you specify can see the plugin.
 Select
 Block
-- No users in your tenant can access the plugin.
+: No users in your tenant can access the plugin.
 Note
 Country or region-based scoping isn't supported for plugin availability. Use security groups to represent geographic or organizational segments.
 Learn more in
 Manage agents in the Microsoft 365 admin center
+.
+Prevent plugin sharing in your tenant
+Separate from the plugins you deploy, users can upload their own plugin package from the Cowork
+Customize
+page and then use the
+Share
+dialog to make it available to other people. A user can share a plugin with specific users in your organization, or request that it be published to your whole organization. Use the controls in this section to limit that.
+Important
+There's currently no single tenant setting that turns off plugin sharing for every user. Organization-wide sharing requires your approval, and you can block or unpublish any plugin after the fact. A user can still share an uploaded plugin with specific people they choose. If you need user-to-user plugin sharing disabled for your tenant, contact Microsoft Support.
+Org-wide sharing requires admin approval
+When a user requests that a plugin be published to your entire organization, the plugin doesn't go live on its own. The request is held in a pending state, and the plugin only becomes available to your organization after a tenant administrator approves it. If you reject the request, the plugin stays unavailable to everyone else in your tenant.
+This approval step applies to org-wide publication only. It doesn't apply
```

---

### 3. Agent settings in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

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
--- +++ @@ -47,16 +47,18 @@ - Manage the labels that admins and users apply to agents to organize and find them.
 These settings allow you to customize agent behavior, control access, and maintain compliance with enterprise standards.
 Agent management rules
-Agent Management Rules in the Microsoft 365 Admin Center (MAC) enable tenant administrators to apply governance and lifecycle controls across AI agents at scale by using bulk administrative actions.
-Instead of manually reviewing and taking action on agents individually, use Agent Management Rules to:
+Agent management rules in the Microsoft 365 Admin Center (MAC) enable tenant administrators to apply governance and lifecycle controls across AI agents at scale by using bulk administrative actions.
+Instead of manually reviewing and taking action on agents individually, use agent management rules to:
 Identify agents that meet defined conditions
-Review impacted agents prior to run
+Review impacted agents before running the rule
 Apply governance actions across affected agents in bulk
 This experience helps organizations maintain compliance, ownership accountability, and deployment consistency across agents while keeping administrators in the control loop.
 Supported Rule-Based Bulk Actions
-Agent Management Rules currently support the following governance scenarios:
+Agent management rules currently support the following governance scenarios:
 Install Microsoft agents
 Reassign ownerless agents created with Agent Builder to manager
+Block ownerless agents without usage
+Reject agent publish requests older than a specified number of days
 Install Microsoft agents
 Microsoft first-party (1P) agents are consistently among the most installed and widely used agents. However, administrators currently lack a scalable way to install these agents proactively across their tenant.
 By using the
@@ -76,6 +78,10 @@ Identify agents that no longer have a valid owner
 Review ownerless agents before reassignment
 Transfer owner
```

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