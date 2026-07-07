# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-07
**Run Time:** 2026-07-07T12:21:54.519795+00:00
**Total URLs Checked:** 152

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 2 |
| MEDIUM Changes | 3 |
| Redirects | 1 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | release-notes | CRITICAL | 4.12 | Monitor |
| 2 | purview-management | HIGH | None | Review and update |
| 3 | authoring-ask-a-question | MEDIUM | None | Review optional |
| 4 | agent-registry | MEDIUM | 4.13, 2.14 | Review optional |
| 5 | restricted-sharepoint-search | HIGH | 1.3, 2.5 | Review and update |

---

## HIGH: Control Review Recommended

### 1. Purview management for SharePoint Embedded containers

**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/purview-management?view=o365-worldwide
**Section:** Copilot Pages and Notebooks
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -59,12 +59,6 @@ instead. For more information, see
 Grant access to containers
 .
-Note
-The
-Container Redirect URL
-field might not yet be available in the SharePoint admin center. This capability is still rolling out. Track the rollout status on the
-Microsoft 365 public roadmap
-.
 Searching the Audit Logs
 Loop application IDs:
 Loop Web Application ID:

```

---

### 2. Restricted SharePoint Search

**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-sharepoint-search
**Section:** SharePoint Administration
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`
- Control 2.5: Control 2.5: Data Minimization and Grounding Scope
  - File: `controls/pillar-2-security/2.5-data-minimization-grounding-scope.md`

**What Changed:**
```diff
--- +++ @@ -23,21 +23,24 @@ Feedback
 Summarize this article for me
 Important
-Restricted SharePoint Search is designed for customers of Microsoft 365 Copilot chat and agentic experiences. It's designed as a short-term solution to allow time for your organization's administrators to thoroughly review and audit site and file permissions, but it's not intended or scalable for long-term use. Comprehensive data security solutions are available, including
+Restricted SharePoint Search is retiring. Starting July 31, 2026, new enablement is blocked. Use comprehensive data controls such as
+Restricted Content Discovery
+(RCD) for content discoverability.
+Restricted SharePoint Search is designed for customers of Microsoft 365 Copilot chat and agentic experiences. It's a short-term solution that gives your organization's administrators time to review and audit site and file permissions. It's not intended or scalable for long-term use. Comprehensive data security solutions are available, including
 SharePoint Advanced Management
 and
 Microsoft Purview
 .
 What is Restricted SharePoint Search?
-Restricted SharePoint Search is a setting that enables you as a
+Restricted SharePoint Search is a setting that you, as a
 SharePoint Administrator
 or
 other Microsoft 365 administrator
-to maintain a list of SharePoint sites (an "allowed list") for which you have checked permissions and applied data governance. The allowed list defines which SharePoint sites can be used in organization-wide search queries, and, as a temporary measure, Copilot chat and agentic experiences.
-By default, the Restricted SharePoint Search setting is turned off and the allowed list is empty. If Restricted SharePoint Search is enabled, users can interact with files and content they own or have previously accessed in Copilot.
+, use to maintain a list of SharePoint sites (an "allow list") for which you check permissions and apply data governance. The allow list defines which SharePoint sites can be used in 
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot release notes
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Classification:** CRITICAL (UI navigation steps changed)

---

### 2. Adaptive cards in Copilot Studio topics
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-ask-a-question#add-an-adaptive-card
**Classification:** MEDIUM (General content update)

---

### 3. Agent registry in Microsoft 365 admin center
**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/sharepoint/ai-in-sharepoint-get-started | https://learn.microsoft.com/en-us/SharePoint/copilot-in-sharepoint-get-started |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*