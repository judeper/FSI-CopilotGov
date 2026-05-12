# Microsoft Learn Documentation Changes

**Run Date:** 2026-05-05
**Run Time:** 2026-05-05T11:11:19.919799+00:00
**Total URLs Checked:** 114

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | dlp-policy-reference | HIGH | None | Review and update |
| 2 | encryption-sensitivity-labels | HIGH | None | Review and update |
| 3 | audit-log-activities | HIGH | 1.15 | Review and update |
| 4 | data-connectors-reference | HIGH | None | Review and update |

---

## HIGH: Control Review Recommended

### 1. DLP policy reference

**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-reference
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -19,31 +19,9 @@ Access to this page requires authorization. You can try
 changing directories
 .
+Data Loss Prevention policy reference
 Feedback
 Summarize this article for me
-title: "Data Loss Prevention policy reference"
-f1.keywords: CSH
-ms.author: chrfox
-author: chrfox
-manager: laurawi
-ms.date: [DATE]
-audience: Admin
-ms.topic: reference
-ms.service: purview
-ms.subservice: purview-data-loss-prevention
-search.appverid:
-SPO160
-MET150
-ms.assetid: 6501b5ef-6bf7-43df-b60d-f65781847d6c
-ms.collection:
-highpri
-purview-compliance
-SPO_Content
-recommendations: false
-description: "DLP policy component and configuration reference. This article provides a detailed anatomy of a DLP policy."
-ms.custom: seo-marvel-apr2021
-ai-usage: ai-assisted
-Data Loss Prevention policy reference
 Microsoft Purview Data Loss Prevention (DLP) policies have many components to configure. To create an effective policy, you need to understand what the purpose of each component is and how its configuration alters the behavior of the policy. This article provides a detailed anatomy of a DLP policy.
 Tip
 Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about

```

---

### 2. Encryption with sensitivity labels

**URL:** https://learn.microsoft.com/en-us/purview/encryption-sensitivity-labels
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -48,8 +48,8 @@ Understand how the encryption works
 Unless you're using
 S/MIME for Outlook
-, encryption that's applied by sensitivity labels to documents, emails, and meeting invites all use the Azure Rights Management service (Azure RMS) from Microsoft Purview Information Protection. This protection solution uses encryption, identity, and authorization policies. To learn more, see
-What is Azure Rights Management?
+, encryption that's applied by sensitivity labels to documents, emails, and meeting invites all use the Azure Rights Management service from Microsoft Purview Information Protection. This protection solution uses encryption, identity, and authorization policies. To learn more, see
+Learn about the Azure Rights Management encryption service
 .
 When you use this encryption solution, the
 super user
@@ -76,8 +76,8 @@ There are some Microsoft Entra configurations that can prevent authorized access to encrypted content. For example, cross-tenant access settings and Conditional Access policies. For more information, see
 Microsoft Entra configuration for encrypted content
 .
-Configure Exchange for Azure Rights Management
-Exchange doesn't have to be configured for Azure Rights Management before users can apply labels in Outlook to encrypt their emails. However, until Exchange is configured for Azure Rights Management, you don't get the full functionality of encryption with rights management.
+Configure Exchange for the Azure Rights Management service
+Exchange doesn't have to be configured for the Azure Rights Management service before users can apply labels in Outlook to encrypt their emails. However, until Exchange is configured for the Azure Rights Management service, you don't get the full functionality of encryption with rights management.
 For example, users can't view encrypted emails or encrypted meeting invites on mobile phones or with Outlook on the web, encrypted emails can't be indexed for search, and you can't configure Exchange Onl
```

---

### 3. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**What Changed:**
```diff
--- +++ @@ -993,6 +993,9 @@ Friendly name
 Operation
 Description
+Analyzed dataflow refresh logs
+AnalyzedDataflowRefreshLogs
+Analyzed dataflow refresh logs.
 Automatically bound user credentials to Git
 AutoBoundGitCredentials
 Automatically bound user credentials to Git.
@@ -1056,9 +1059,15 @@ Planning session upgraded
 PlanningSessionUpgraded
 Session type is upgraded in planning workload.
+Recover an artifact
+ArtifactRecovered
+A user recovered a previously soft-deleted artifact, such as a gateway or gateway cluster member, restoring it to active state.
 Retrieved artifact's Logical Id
 ArtifactLogicalIdRetrieved
 Retrieved artifact's Logical Id.
+Soft delete an artifact
+ArtifactSoftDeleted
+A user soft deleted an artifact, such as a gateway or gateway cluster member, marking it for deletion while allowing recovery within a retention period.
 Switched Git branch
 GitSwitchedBranch
 Switched Git branch for workspace.

```

---

### 4. Connect Microsoft 365 data

**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
**Section:** Microsoft Sentinel
**Classification:** HIGH (Policy language)

**What Changed:**
```diff
--- +++ @@ -61,8 +61,8 @@ Cloud feature availability for US Government customers
 .
 Data connector prerequisites
-Each data connector has its own set of prerequisites. Prerequisites might include that you must have specific permissions on your Azure workspace, subscription, or policy. Or, you must meet other requirements for the partner data source you're connecting to.
-Prerequisites for each data connector are listed on the relevant data connector page in Microsoft Sentinel.
+Each data connector has its own set of prerequisites. Prerequisites might include having specific permissions on your Azure workspace, subscription, or policy. You might also need to meet other requirements for the partner data source you're connecting to.
+Prerequisites for each data connector are listed in this article and on the relevant data connector page in Microsoft Sentinel.
 Azure Monitor agent (AMA) based data connectors require an internet connection from the system where the agent is installed. Enable port 443 outbound to allow a connection between the system where the agent is installed and Microsoft Sentinel.
 Syslog and Common Event Format (CEF) connectors
 Log collection from many security appliances and devices are supported by the data connectors

```

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*