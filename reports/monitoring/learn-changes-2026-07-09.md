# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-09
**Run Time:** 2026-07-09T12:31:53.008545+00:00
**Total URLs Checked:** 152

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 3 |
| MEDIUM Changes | 1 |
| Redirects | 1 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | manage-public-web-access | HIGH | 2.6 | Review and update |
| 2 | audit-solutions-overview | HIGH | 3.1 | Review and update |
| 3 | .../microsoft-365/copilot/extensibility/ | HIGH | 4.13, 1.13, 2.14, 2.16, 2.13 | Review and update |
| 4 | ...ication-fundamentals-publish-channels | MEDIUM | None | Review optional |

---

## HIGH: Control Review Recommended

### 1. Manage Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access
**Section:** Copilot Administration
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 2.6: Control 2.6: Copilot Web Search and Web Grounding Controls
  - File: `controls/pillar-2-security/2.6-web-search-controls.md`

**What Changed:**
```diff
--- +++ @@ -183,19 +183,25 @@ Web content
 toggle offers users control over whether or not they want real-time web content in Microsoft 365 Copilot responses based on their personal preference. The
 Web content
-toggle is only available as part of work chat in Microsoft 365 Copilot.
+toggle is now available across work and web chat in Microsoft 365 Copilot.
 If the IT admin enables web search, the
 Web content
 toggle is turned on by default. When turned on, the user receives responses grounded in real-time web content. If the IT admin disables web search, the
 Web content
-toggle isn't available to the Microsoft 365 Copilot user as part of work chat and web search is disabled.
+toggle isn't available to the Microsoft 365 Copilot user and web search is disabled.
 If a Microsoft 365 Copilot user turns off the
 Web content
-toggle in work chat, web content isn't included in Copilot responses.
-Microsoft 365 Copilot users can manage web search in work chat by following these steps:
-Select the menu in the top right corner of the screen in Microsoft 365 Copilot when using work chat.
-Turn off the
-Web content
+toggle, web content isn't included in Copilot responses. User preferences persist across sessions and are applied across supported Copilot clients and devices.
+Microsoft 365 Copilot users can manage web search by following these steps:
+In the Microsoft 365 Copilot app, open
+Settings
+, and then select
+Personalization
+.
+Expand
+Advanced
+, and turn off the
+Web search
 toggle.
 Note
 The privacy setting for optional connected experiences available to users in Microsoft 365 apps (for example, in Word, Excel, or Teams) has no effect on the availability of web search. For example, if a user turns off optional connected experiences, web search can still be available to the user.

```

---

### 2. Microsoft Purview Audit overview

**URL:** https://learn.microsoft.com/en-us/purview/audit-solutions-overview
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/3.1/troubleshooting.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -92,7 +92,7 @@ Longer retention of audit records
 . Microsoft Entra ID, Exchange, OneDrive, and SharePoint audit records are retained for one year by default. Audit records for all other activities are retained for 180 days by default, or you can use audit log retention policies to configure longer retention periods.
 Audit (Premium) intelligent insights
-. Audit records for intelligent insights can help your organization conduct forensic and compliance investigations by providing visibility to events such as when mail items were accessed, or when mail items were replied to and forwarded, or when and what a user searched for in Exchange Online and SharePoint Online. These intelligent insights can help you investigate possible breaches and determine the scope of compromise.
+. Audit records for intelligent insights can help your organization conduct forensic and compliance investigations by providing visibility to insights such as the sensitivity label of mail items which were accessed, or when and what a user searched for in Exchange Online and SharePoint Online. These intelligent insights can help you investigate possible breaches and determine the scope of compromise more precisely.
 Higher bandwidth to the Office 365 Management Activity API
 . Audit (Premium) provides organizations with more bandwidth to access auditing logs through the Office 365 Management Activity API. Although all organizations (that have Audit (Standard) or Audit (Premium)) initially receive a baseline of 2,000 requests per minute, this limit dynamically increases depending on an organization's seat count and their licensing subscription. This change results in organizations with Audit (Premium) getting about twice the bandwidth as organizations with Audit (Standard).
 Long-term retention of audit logs

```

---

### 3. Copilot extensibility overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Graph Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 2.16: Control 2.16: Federated Copilot Connector and Model Context Protocol (MCP) Governance
  - File: `controls/pillar-2-security/2.16-federated-connector-mcp-governance.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`

**What Changed:**
```diff
--- +++ @@ -15,6 +15,7 @@ Build a declarative agent
 Build a custom engine agent
 Evaluate agents
+Use Insights Agent (preview)
 Manage agents in the Microsoft 365 admin center
 Extend with plugins and connectors
 How-To Guide

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Publish and deploy Copilot Studio agents
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels
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