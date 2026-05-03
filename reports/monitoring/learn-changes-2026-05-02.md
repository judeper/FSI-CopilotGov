# Microsoft Learn Documentation Changes

**Run Date:** 2026-05-02
**Run Time:** 2026-05-02T10:42:10.039856+00:00
**Total URLs Checked:** 114

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 8 |
| MEDIUM Changes | 1 |
| Redirects | 34 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | whats-new | HIGH | None | Review and update |
| 2 | ai-m365-copilot | HIGH | None | Review and update |
| 3 | dlp-policy-reference | HIGH | None | Review and update |
| 4 | ai-microsoft-purview | HIGH | 1.1, 1.2, 1.6 | Review and update |
| 5 | ai-microsoft-purview-considerations | HIGH | 1.2 | Review and update |
| 6 | ...curity-posture-management-learn-about | HIGH | 1.14 | Review and update |
| 7 | ...curity-posture-management-oversharing | HIGH | None | Review and update |
| 8 | .../microsoft-365-copilot/extensibility/ | HIGH | 2.14 | Review and update |
| 9 | sharepoint-copilot-best-practices | CRITICAL | 1.13, 1.3 | Monitor |

---

## HIGH: Control Review Recommended

### 1. What's new in Microsoft Purview

**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -37,6 +37,29 @@ for data governance solutions.
 Roadmap
 for data security and risk and compliance solutions.
+May 2026
+Agent 365
+General availability (GA)
+:
+Data security and compliance protections for Microsoft Agent 365
+.
+Data Security Posture Management
+General availability (GA)
+: The new version of
+Data Security Posture Management
+is now generally available. Partner solutions for non-Microsoft data sources remain in preview, as does the Data Security Posture Agent. This current version provides guided workflows for proactive risk management and streamlines data security operations so you can more confidently adopt AI across your digital estate.
+New
+:
+Support for administrative units
+, to bring parity with the classic versions of DSPM and DSPM for AI.
+New
+: To optimize resources, processing is paused for Microsoft 365 data when tenants are inactive for more than 60 days, and automatically resume when you return to the solution. For more information, see
+Data updates paused for inactive tenants
+.
+New
+: The "Responsible AI FAQ for Data Security Posture Management" is replaced with the more detailed
+Application card for Data Security Posture Management
+to better help you understand this solution's AI capabilities, intended uses, limitations, evaluations, safety components, and best practices.
 April 2026
 Collection Policies
 Preview

```

---

### 2. Use Purview for Copilot data security

**URL:** https://learn.microsoft.com/en-us/purview/ai-m365-copilot
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -30,7 +30,7 @@ Use the following table to see at a glance the Microsoft Purview capabilities that are supported with Microsoft 365 Copilot & Microsoft 365 Copilot Chat.
 Capability or solution in Microsoft Purview
 Supported for AI interactions
-DSPM for AI (classic) and DSPM (preview)
+DSPM and DSPM for AI (classic)
 â
 Auditing
 â
@@ -52,11 +52,11 @@ â
 Compliance Manager
 â
-DSPM for AI (classic) and DSPM (preview)
+DSPM and DSPM for AI (classic)
 Use
+Data Security Posture Management
+or
 Data Security Posture Management for AI (classic)
-or
-Data Security Posture Management (preview)
 as your front door to discover, secure, and apply compliance controls for AI usage across your enterprise. Both DSPM versions use existing controls from Microsoft Purview information protection and compliance management with easy-to-use graphical tools and reports to quickly gain insights into AI use within your organization. With personalized recommendations, and one-click policies help you protect your data and comply with regulatory requirements.
 AI app-specific information:
 Data risk assessments
@@ -279,9 +279,9 @@ Getting started recommended steps
 Use the following steps to get started with managing data security & compliance for AI interactions from Microsoft 365 Copilot & Microsoft 365 Copilot Chat.
 Note
-These steps focus on managing a specific AI app or agent. For broader coverage that uses security objectives with guided workflows, use the new
+These steps focus on managing a specific AI app or agent. For broader coverage that uses security objectives with guided workflows, use the current version of
 Data Security Posture Management
-, currently in preview.
+.
 Because Data Security Posture Management for AI is your front door for securing and managing AI interactions, most of the following instructions use that solution:
 Sign in to the Microsoft Purview portal
 >

```

---

### 3. DLP policy reference

**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-reference
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -19,9 +19,31 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Data Loss Prevention policy reference
 Feedback
 Summarize this article for me
+title: "Data Loss Prevention policy reference"
+f1.keywords: CSH
+ms.author: chrfox
+author: chrfox
+manager: laurawi
+ms.date: [DATE]
+audience: Admin
+ms.topic: reference
+ms.service: purview
+ms.subservice: purview-data-loss-prevention
+search.appverid:
+SPO160
+MET150
+ms.assetid: 6501b5ef-6bf7-43df-b60d-f65781847d6c
+ms.collection:
+highpri
+purview-compliance
+SPO_Content
+recommendations: false
+description: "DLP policy component and configuration reference. This article provides a detailed anatomy of a DLP policy."
+ms.custom: seo-marvel-apr2021
+ai-usage: ai-assisted
+Data Loss Prevention policy reference
 Microsoft Purview Data Loss Prevention (DLP) policies have many components to configure. To create an effective policy, you need to understand what the purpose of each component is and how its configuration alters the behavior of the policy. This article provides a detailed anatomy of a DLP policy.
 Tip
 Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about
@@ -1870,7 +1892,7 @@ .ppt, .pptx, .pos, .pps, .pptm, .potx, .potm, .ppam, .ppsx
 The user accessed a sensitive website from Microsoft Edge:
 For more information, see
-Scenario 6 Monitor or restrict user activities on sensitive service domains (preview)
+Help prevent risky user activity by monitoring or restricting access to sensitive service domains
 .
 Insider risk level for Adaptive Protection is:
 Detects the insider risk level.
@@ -2336,7 +2358,7 @@ Detects when protected files are blocked or allowed to be uploaded to cloud service domains. See,
 Browser and domain restrictions to sensitive data
 and
-Scenario 6 Monitor or restrict user activities on sensitive service domains)
+Help prevent risky user activity by monitoring or restrict
```

---

### 4. DSPM for AI overview

**URL:** https://learn.microsoft.com/en-us/purview/ai-microsoft-purview
**Section:** DSPM for AI (Data Security Posture Management for AI)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.2: Control 1.2: SharePoint Oversharing Detection and Remediation (DSPM for AI)
  - File: `controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md`
- Control 1.6: Control 1.6: Permission Model Audit (SharePoint, OneDrive, Exchange, Teams, Graph)
  - File: `controls/pillar-1-readiness/1.6-permission-model-audit.md`

**What Changed:**
```diff
--- +++ @@ -45,12 +45,6 @@ Google Gemini
 Microsoft Copilot (consumer version)
 DeepSeek
-Note
-Now rolling out with the
-Frontier preview program
-data security and compliance protections from Microsoft Purview also support
-Microsoft Agent 365
-. Currently, agent instances are identified and managed like other users.
 For a breakdown of Microsoft Purview security and compliance supported capabilities for AI interactions by app, see the additional pages identified in the following table. Where these AI apps support agents, they inherit the same security and compliance capabilities as their parent AI app. However, for a quick summary, see
 Use Microsoft Purview to manage data security & compliance for AI agents
 .
@@ -73,11 +67,11 @@ If you're new to Microsoft Purview, you might also find an overview of the product helpful:
 Learn about Microsoft Purview
 .
-DSPM for AI (classic) and DSPM (preview)
+DSPM and DSPM for AI (classic)
 Use
+Data Security Posture Management
+or
 Data Security Posture Management for AI (classic)
-or
-Data Security Posture Management (preview)
 as your front door to discover, secure, and apply compliance controls for AI usage across your enterprise. Both DSPM versions use existing controls from Microsoft Purview information protection and compliance management with easy-to-use graphical tools and reports to quickly gain insights into AI use within your organization. With personalized recommendations, and one-click policies help you protect your data and comply with regulatory requirements.
 Microsoft Purview strengthens information protection for AI apps
 Because of the power and speed AI can proactively surface content, generative AI amplifies the problem and risk of oversharing or leaking data. Learn how information protection capabilities from Microsoft Purview can help to strengthen your existing data security solutions.

```

---

### 5. Get started with DSPM for AI

**URL:** https://learn.microsoft.com/en-us/purview/ai-microsoft-purview-considerations
**Section:** DSPM for AI (Data Security Posture Management for AI)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.2: Control 1.2: SharePoint Oversharing Detection and Remediation (DSPM for AI)
  - File: `controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md`

**What Changed:**
```diff
--- +++ @@ -26,10 +26,10 @@ Note
 This article is for the
 classic
-version of Data Security Posture Management that's being replaced with a new version that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.
+version of Data Security Posture Management for AI that's now replaced with a new version that incorporates support for AI apps and agents, new features and broader reach, with simplified management.
 These improvements won't be added to this classic version so we invite you to try the new
 Data Security Posture Management
-, currently in preview.
+.
 For the most part, Data Security Posture Management for AI is easy to use and self-explanatory, guiding you through prerequisites and preconfigured reports and policies. Use this section to complement that information and provide additional details that you might need.
 Prerequisites for Data Security Posture Management for AI
 To use Data Security Posture Management for AI from the Microsoft Purview portal, you must have the following prerequisites:

```

---

### 6. Learn about DSPM

**URL:** https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about
**Section:** DSPM for AI (Data Security Posture Management for AI)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.14: Control 1.14: Item-Level Permission Scanning
  - File: `controls/pillar-1-readiness/1.14-item-level-permission-scanning.md`

**What Changed:**
```diff
--- +++ @@ -25,8 +25,8 @@ Microsoft Purview service description
 Note
 This documentation is for the
-preview
-version of Data Security Posture Management. We invite you to try this preview that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.
+current
+version of Data Security Posture Management that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.
 Most new features will be added to this version only but you can still access the previous versions and their documentation:
 DSPM for AI (classic)
 DSPM (classic)
@@ -72,7 +72,7 @@ options throughout the data security objectives for easy access to the agents' activity.
 These AI capabilities from Data Security Posture Management help ensure that sensitive data is governed, labeled, and monitored, with streamlined management. For more information:
 How AI is used within Data Security Posture Management, see
-Responsible AI FAQ for Data Security Posture Management
+Application card: Microsoft Purview Data Security Posture Management
 For the best experience using Security Copilot prompts, see
 Tips for custom Security Copilot prompts in Data Security Posture Management
 How to use Data Security Posture Management
@@ -90,7 +90,7 @@ >
 Solutions
 >
-DSPM (preview)
+DSPM
 .
 Don't confuse this with the previous versions, that are now named
 Data Security Posture Management (classic)
@@ -118,7 +118,7 @@ Reports
 : To help you track sensitive data usage and labeling, policy usage, and risky behavior of users and AI agents.
 Setup tasks
-: To identify and complete configuration steps independently from the security objectives. They include setting up Microsoft Sentinel data lake to integrate with partner solutions for non-
```

---

### 7. DSPM data risk assessments (oversharing)

**URL:** https://learn.microsoft.com/en-us/purview/data-security-posture-management-oversharing
**Section:** DSPM for AI (Data Security Posture Management for AI)
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -25,8 +25,8 @@ Microsoft Purview service description
 Note
 This documentation is for the
-preview
-version of Data Security Posture Management. We invite you to try this preview that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.
+current
+version of Data Security Posture Management that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.
 Most new features will be added to this version only but you can still access the previous versions and their documentation:
 DSPM for AI (classic)
 DSPM (classic)
@@ -34,7 +34,7 @@ Data Security Posture Management
 help you identify and fix potential data oversharing risks in your organization. Because of the power and speed AI can proactively surface content that might be obsolete, over-permissioned, or lack governance controls, generative AI amplifies the problem of oversharing data. Use data risk assessments to both identify and remediate issues.
 You can access data risk assessments from the Microsoft Purview portal >
-DSPM (preview)
+DSPM
 >
 Discover
 >

```

---

### 8. Copilot extensibility overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`

**What Changed:**
```diff
--- +++ @@ -25,4 +25,4 @@ Microsoft 365 Agents SDK
 Microsoft 365 Copilot APIs
 Copilot Studio documentation
-Microsoft Agent 365 (early access preview)+Microsoft Agent 365
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. SharePoint agents
**URL:** https://learn.microsoft.com/en-us/sharepoint/sharepoint-copilot-best-practices
**Classification:** CRITICAL (Deprecation notice)

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