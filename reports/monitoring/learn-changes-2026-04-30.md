# Microsoft Learn Documentation Changes

**Run Date:** 2026-04-30
**Run Time:** 2026-04-30T11:23:36.470609+00:00
**Total URLs Checked:** 114

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 7 |
| MEDIUM Changes | 6 |
| Redirects | 34 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | whats-new | HIGH | None | Review and update |
| 2 | ai-m365-copilot | MEDIUM | None | Review optional |
| 3 | ...osoft365-copilot-location-learn-about | MEDIUM | None | Review optional |
| 4 | audit-solutions-overview | HIGH | 3.1 | Review and update |
| 5 | audit-premium | HIGH | 3.1 | Review and update |
| 6 | audit-log-search | HIGH | 3.1 | Review and update |
| 7 | audit-log-activities | HIGH | 1.15 | Review and update |
| 8 | information-barriers-policies | MEDIUM | None | Review optional |
| 9 | information-barriers-in-teams | MEDIUM | None | Review optional |
| 10 | edisc-search-copilot-data | MEDIUM | None | Review optional |
| 11 | ai-microsoft-purview | MEDIUM | 1.1, 1.2, 1.6 | Review optional |
| 12 | ...curity-posture-management-learn-about | HIGH | 1.14 | Review and update |
| 13 | insider-risk-management-configure | HIGH | None | Review and update |

---

## HIGH: Control Review Recommended

### 1. What's new in Microsoft Purview

**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -44,16 +44,26 @@ sensitivity labels as a condition
 for scoping detection to items with specific sensitivity labels applied. This condition is supported with browser and network cloud apps detection.
 Data Governance
+In preview
+: Use a one-time
+glossary migration and asset enablement process
+to curate data assets and columns with glossary terms. This process allows you to centralize the management of glossary terms by migrating glossary terms created in the classic governance experience into Unified Catalog. When you complete the process, you can
+curate data assets and columns
+.
+In preview
+: New bulk import, editing, and moving capabilities can help you quickly scale operations in Unified Catalog:
+Create data products in bulk
+Create critical data elements in bulk
+Create glossary terms in bulk
+and
+bulk edit glossary terms
+Move multiple glossary terms between governance domains
 General availability (GA)
 : Now rolling out, the
 advanced resource sets
 capability is available to all customers. Pricing for advanced resource sets is consistent with existing rates for
 classic Microsoft Purview data governance
 .
-In preview
-: Updates to facilitate editing and managing glossary terms in Unified Catalog:
-Edit glossary terms in bulk
-Move multiple terms at once from one governance domain into another domain
 In preview
 : Data quality provides
 on-premises support for Oracle and SQL server
@@ -102,6 +112,11 @@ and
 Insider Risk Management
 role groups have contributor access without needing explicit role assignment.
+Data Security Posture Management (preview)
+New
+:
+Microsoft Sentinel with partner solutions
+now also supports Varonis to provide holistic data insights for Salesforce.
 eDiscovery
 In preview
 : Organizations using

```

---

### 2. Microsoft Purview Audit overview

**URL:** https://learn.microsoft.com/en-us/purview/audit-solutions-overview
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**What Changed:**
```diff
--- +++ @@ -109,7 +109,7 @@ property (which indicates the service in which the activity occurred) for one year. Retaining audit records for longer periods can help with ongoing forensic or compliance investigations. For more information, see the "Default audit log retention policy" section in
 Manage audit log retention policies
 .
-In addition to the one-year retention capabilities of Audit (Premium), we also released the capability to retain audit logs for 10 years. The 10-year retention of audit logs helps support long running investigations and respond to regulatory, legal, and internal obligations.
+In addition to the one-year retention capabilities of Audit (Premium), Microsoft also released the capability to retain audit logs for 10 years. The 10-year retention of audit logs helps support long running investigations and respond to regulatory, legal, and internal obligations.
 Note
 Retaining audit logs for 10 years requires an additional per-user add-on license. After you assign this license to a user and set an appropriate 10-year audit log retention policy for that user, audit logs covered by that policy start to be retained for the 10-year period. This policy isn't retroactive and can't retain audit logs that were generated before the 10-year audit log retention policy was created.
 Audit log retention policies

```

---

### 3. Audit (Premium)

**URL:** https://learn.microsoft.com/en-us/purview/audit-premium
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**What Changed:**
```diff
--- +++ @@ -109,7 +109,7 @@ property (which indicates the service in which the activity occurred) for one year. Retaining audit records for longer periods can help with ongoing forensic or compliance investigations. For more information, see the "Default audit log retention policy" section in
 Manage audit log retention policies
 .
-In addition to the one-year retention capabilities of Audit (Premium), we also released the capability to retain audit logs for 10 years. The 10-year retention of audit logs helps support long running investigations and respond to regulatory, legal, and internal obligations.
+In addition to the one-year retention capabilities of Audit (Premium), Microsoft also released the capability to retain audit logs for 10 years. The 10-year retention of audit logs helps support long running investigations and respond to regulatory, legal, and internal obligations.
 Note
 Retaining audit logs for 10 years requires an additional per-user add-on license. After you assign this license to a user and set an appropriate 10-year audit log retention policy for that user, audit logs covered by that policy start to be retained for the 10-year period. This policy isn't retroactive and can't retain audit logs that were generated before the 10-year audit log retention policy was created.
 Audit log retention policies

```

---

### 4. Search the audit log

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-search
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**What Changed:**
```diff
--- +++ @@ -98,7 +98,7 @@ cmdlet to a CSV file, see the "Tips for exporting and viewing the audit log" section in
 Export, configure, and view audit log records
 .
-To programmatically download data from the audit log, we recommend that you use the Office 365 Management Activity API instead of using a PowerShell script. The Office 365 Management Activity API is a REST web service that you can use to develop operations, security, and compliance monitoring solutions for your organization. For more information, see
+To programmatically download data from the audit log, use the Office 365 Management Activity API instead of a PowerShell script. The Office 365 Management Activity API is a REST web service that you can use to develop operations, security, and compliance monitoring solutions for your organization. For more information, see
 Office 365 Management Activity API reference
 .
 Microsoft Entra ID is the directory service for Microsoft 365. The unified audit log contains user, group, application, domain, and directory activities performed in the

```

---

### 5. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**What Changed:**
```diff
--- +++ @@ -1097,7 +1097,7 @@ The purpose of logging PageViewedExtended events is to reduce the number of PageViewed events that are logged when a page is continually viewed. This approach helps reduce the noise of multiple PageViewed records for what is essentially the same user activity, and lets you focus on the initial (and more important) PageViewed event.
 Accessed file
 FileAccessed
-User or system account accesses a file. Once a user accesses a file, the system doesn't log the FileAccessed event again for the same user and file for the next five minutes.
+User or system account accesses a file. After a user accesses a file, the system doesn't log the FileAccessed event again for the same user and file for the next five minutes.
 Changed record status to locked
 LockRecord
 The record status of a retention label that classifies a document as a record is locked. This status means the document wasn't modified or deleted. Only users assigned at least the contributor permission for a site can change the record status of a document.
@@ -1206,7 +1206,7 @@ : Because ClientViewSignaled events are signaled by the client, rather than the server, it's possible the event might not be logged by the server and therefore might not appear in the audit log. It's also possible that information in the audit record might not be trustworthy. However, because the user's identity is validated by the token used to create the signal, the user's identity listed in the corresponding audit record is accurate. The system waits five minutes before it logs the same event when the same user's client signals that the page is viewed again by the user.
 Viewed page
 PageViewed
-User views a page on a site. This activity doesn't include using a Web browser to view files located in a document library. Once a user views a page, the system doesn't log the PageViewed event again for the same user and page for the next five minutes.
+User views a page on a site. This activity doesn't include using a
```

---

### 6. Learn about DSPM

**URL:** https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about
**Section:** DSPM for AI (Data Security Posture Management for AI)
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.14: Control 1.14: Item-Level Permission Scanning
  - File: `controls/pillar-1-readiness/1.14-item-level-permission-scanning.md`

**What Changed:**
```diff
--- +++ @@ -32,7 +32,7 @@ DSPM (classic)
 Microsoft Purview Data Security Posture Management (DSPM) helps organizations discover, protect, and investigate sensitive data risks across their digital estate. This solution provides unified visibility and control for both traditional applications and AI apps and agents, supporting data governance across Microsoft 365, Azure, Fabric, and integrated third-party SaaS platforms. Monitor, assess, and remediate data risks, regardless of where sensitive data resides.
 Instead of focusing on infrastructure or endpoints, Data Security Posture Management centers on the data itselfâidentifying where it resides, who can access it, how it's used, and whether itâs adequately protected. This is especially important as data becomes more distributed and exposed in today's AI-driven workplaces where data is constantly moving and changing, making it harder to keep track of and control.
-Data Security Posture Management continuously scans your environment to identify sensitive data, assess risk, and recommend actions to reduce exposure. It consolidates insights from the Microsoft Purview solutions data loss prevention (DLP), Insider Risk Management, information protection with sensitivity labels, and Data Security Investigations. These insights provide a single view for monitoring data risks, policy coverage, and posture trends. This version of Data Security Posture Management extends coverage to third-party SaaS and IaaS platforms, such as Google Cloud Platform, Snowflake, and Databricks, and integrates with partner solutions such as Cyera, BigID, and OneTrust for comprehensive risk insights.
+Data Security Posture Management continuously scans your environment to identify sensitive data, assess risk, and recommend actions to reduce exposure. It consolidates insights from the Microsoft Purview solutions data loss prevention (DLP), Insider Risk Management, information protection with sensitivity labels, and Data Security Investigations.
```

---

### 7. Get started with insider risk management

**URL:** https://learn.microsoft.com/en-us/purview/insider-risk-management-configure
**Section:** Insider Risk Management
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -656,6 +656,9 @@ After you complete these steps to create your first Insider Risk Management policy, you start receiving alerts from activity indicators after about 24 hours. Configure additional policies as needed by using the guidance in Step 4 of this article or the steps in
 Create a new insider risk policy
 .
+To learn more about monitoring agents in your organization, see
+Monitoring Agents in your organization
+.
 To learn more about investigating insider risk alerts and the
 Alerts dashboard
 or the

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Use Purview for Copilot data security
**URL:** https://learn.microsoft.com/en-us/purview/ai-m365-copilot
**Classification:** MEDIUM (General content update)

---

### 2. DLP for Microsoft 365 Copilot
**URL:** https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about
**Classification:** MEDIUM (General content update)

---

### 3. Get started with information barriers
**URL:** https://learn.microsoft.com/en-us/purview/information-barriers-policies
**Classification:** MEDIUM (General content update)

---

### 4. Information barriers in Teams
**URL:** https://learn.microsoft.com/en-us/microsoftteams/information-barriers-in-teams
**Classification:** MEDIUM (General content update)

---

### 5. Search Copilot data in eDiscovery
**URL:** https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data
**Classification:** MEDIUM (General content update)

---

### 6. DSPM for AI overview
**URL:** https://learn.microsoft.com/en-us/purview/ai-microsoft-purview
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview |
| https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup |
| https://learn.microsoft.com/en-us/copilot/microsoft-365/manage-public-web-access | https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access |
| https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements |
| https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy |
| https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage?view=o365-worldwide |
| https://learn.microsoft.com/en-us/purview/sensitive-information-type-entity-definitions | https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions |
| https://learn.microsoft.com/en-us/purview/create-a-custom-sensitive-information-type | https://learn.microsoft.com/en-us/purview/sit-create-a-custom-sensitive-information-type |
| https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-securebydefault-intro | https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-intro |
| https://learn.microsoft.com/en-us/purview/audit-standard-setup | https://learn.microsoft.com/en-us/purview/audit-get-started |
| https://learn.microsoft.com/en-us/purview/audit-premium | https://learn.microsoft.com/en-us/purview/audit-solutions-overview |
| https://learn.microsoft.com/en-us/purview/audit-log-search | https://learn.microsoft.com/en-us/purview/audit-search |
| https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-admin-configuration | https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-admin-configuration?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-compliance-summary | https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-compliance-summary?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-loop-purview-management | https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-loop-purview-management?view=o365-worldwide |
| https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-compliant-device | https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-alt-all-users-compliant-hybrid-or-mfa |
| https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-risk | https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-risk-based-sign-in |
| https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-location | https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-by-location |
| https://learn.microsoft.com/en-us/microsoftteams/information-barriers-in-teams | https://learn.microsoft.com/en-us/purview/information-barriers-teams |
| https://learn.microsoft.com/en-us/sharepoint/information-barriers | https://learn.microsoft.com/en-us/purview/information-barriers-sharepoint |
| https://learn.microsoft.com/en-us/onedrive/information-barriers | https://learn.microsoft.com/en-us/purview/information-barriers-onedrive |
| https://learn.microsoft.com/en-us/purview/ai-microsoft-purview-considerations | https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations |
| https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/ | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/ |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-plugins-for-copilot-in-integrated-apps | https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/graph/connecting-external-content-connectors-overview | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-copilot-connector?toc=%2Fgraph%2Ftoc.json |
| https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/overview-declarative-agent | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent |
| https://learn.microsoft.com/en-us/sharepoint/sharepoint-copilot-best-practices | https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps | https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps |
| https://learn.microsoft.com/en-us/azure/sentinel/data-connectors/office-365 | https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365 |
| https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom | https://learn.microsoft.com/en-us/azure/sentinel/create-analytics-rules |
| https://learn.microsoft.com/en-us/sharepoint/get-started-new-admin-center | https://learn.microsoft.com/en-us/sharepoint/manage-sites-in-new-admin-center |
| https://learn.microsoft.com/en-us/microsoft-365/archive/archive-overview | https://learn.microsoft.com/en-us/microsoft-365/archive/archive-overview?view=o365-worldwide |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*