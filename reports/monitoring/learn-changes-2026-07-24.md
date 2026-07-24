# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-24
**Run Time:** 2026-07-24T11:29:54.172028+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| MEDIUM Changes | 1 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | retention | HIGH | 3.2, 3.14 | Update portal-walkthrough |
| 2 | cowork-manage-plugins | MEDIUM | 4.15 | Update portal-walkthrough |
| 3 | ...-based-billing-manage-copilot-credits | CRITICAL | 4.15 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Learn about retention policies

**URL:** https://learn.microsoft.com/en-us/purview/retention
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 3.2: Control 3.2: Data Retention Policies for Copilot Interactions
  - File: `controls/pillar-3-compliance/3.2-data-retention-policies.md`
- Control 3.14: Control 3.14: Copilot Pages and Notebooks Retention and Provenance
  - File: `controls/pillar-3-compliance/3.14-copilot-pages-notebooks-retention.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/3.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/3.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -438,6 +438,16 @@ condition, and then enter the complete retention label name or part of the label name and use a wildcard. For more information, see
 Keyword queries and search conditions for Content Search
 .
+When the retention period starts
+The start of the retention period depends on how you configure the retention policy or retention label:
+When the content was created.
+The default start of the retention period.
+When the content was last modified.
+Supported only for files in the SharePoint, OneDrive, and Microsoft 365 Groups locations.
+When the content was labeled.
+Available with retention labels, for documents in SharePoint and OneDrive, and for email items.
+When an event occurs.
+Available with retention labels that are configured for event-based retention, such as when employees leave the organization or contracts expire.
 Compare capabilities for retention policies and retention labels
 Use the following table to help you identify whether to use a retention policy or retention label, based on capabilities.
 Capability

```

---

### 2. Manage Copilot Cowork plugins

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins
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
--- +++ @@ -53,9 +53,21 @@ .
 Select
 Agents
->
+along with either
+All agents
+or
 Tools
 .
+Note
+You can find Cowork plugins in
+Agents
+>
+All Agents
+or
+Agents
+>
+Tools
+. This is because some agents also function as Cowork plugins. To find out whether it includes Cowork capabilities, review the agent description.
 Find the plugin you want to deploy. You can search by name or browse the available plugins.
 Select the plugin to open its details.
 Select
@@ -81,10 +93,10 @@ Who gets the plugin
 User can remove it?
 Deployed to entire organization
-All licensed Copilot users - acquired automatically
+All licensed Copilot usersâacquired automatically
 No
 Deployed to specific groups
-Target users - acquired automatically; visible to others if configured
+Target usersâacquired automatically; visible to others if configured
 No (for target users)
 Available in the App Store
 Users acquire it themselves

```

---

### 3. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -30,6 +30,17 @@ .â¯Microsoft is working to bring more agents and services to be managed by this experience.
 To learn more about discovery settings for AI experiences enabled by usage-based billing, see
 Discovery setting for AI experiences enabled by usage-based billing
+.
+Note
+If you are looking for information on other usage-based billing products, use the following articles:
+For Copilot Chat, SharePoint Agents, or Microsoft Copilot Retrieval API (Preview), see
+Microsoft 365 Copilot pay-as-you-go service overview
+.
+For Copilot Studio, see
+Copilot Studio pay-as-you-go
+.
+For non-Copilot services; Microsoft 365 Backup, Microsoft 365 SharePoint Storage, and High Volume Email, see
+Set up and manage pay-as-you-go billing in the Billing node of the Microsoft 365 admin center
 .
 Role requirements
 Global administrator and Billing administrator roles can add, select, and change billing methods, and set billing methods in policies.
@@ -93,25 +104,34 @@ Configuration
 tab within the Cost management page is displayed. Copilot consumptive services are now available. You can configure more policies to scope access to specific groups, users, or services.
 Add or edit spending policies
-You can edit the default spending policy or add more spending policies. Have a policy for
-All users
-as a default policy that applies when no other policy is assigned.
-Set the tenant-level limit for all users when you activate the default spending policy. Each additional spending policy has its own independent limit and doesn't inherit the tenant-level limit.
+You can edit the default spending policy or add more spending policies. There's no set maximum number of policies that you can create.
+Set the tenant-level limit for
+all users
+when you activate the default spending policy. Each additional spending policy has its own independent limit and doesn't inherit the tenant-level limit.
 Select
 +Add spending policy
 and go through the screens to create the spending policy
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Manage Copilot Cowork plugins
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins
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
| https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*