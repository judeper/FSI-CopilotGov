# Microsoft Learn Documentation Changes

**Run Date:** 2026-06-11
**Run Time:** 2026-06-11T13:52:31.624384+00:00
**Total URLs Checked:** 151

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 3 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | connect-to-ai-subprocessor | HIGH | 2.7, 3.8a | Review and update |
| 2 | ...opilot-sharepoint-advanced-management | HIGH | 1.13, 1.3 | Review and update |
| 3 | content-governance-agent | HIGH | 1.7 | Review and update |

---

## HIGH: Control Review Recommended

### 1. Anthropic as a Microsoft subprocessor

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`

**What Changed:**
```diff
--- +++ @@ -38,7 +38,9 @@ .
 Microsoft will enable Anthropic models on by default for most customers in commercial cloud (excluding EU/EFTA and UK). This update gives users in your organization the ability to use multiple AI models in their Microsoft offerings, including in Microsoft 365 Copilot, Researcher, Copilot Studio, Power Platform, Agent Mode in Excel, and Word, Excel, and PowerPoint agents. This affirms Microsoft's commitment to offering choice between leading AI models while maintaining enterprise-grade security and compliance.
 Important
-Anthropic models deployed in Microsoft offerings (including Microsoft 365 Copilot, Researcher, Copilot Studio, Power Platform, Agent Mode in Excel, and Word, Excel, and PowerPoint agents) are currently excluded from the EU Data Boundary, and when applicable, in-country processing commitments. Customers within the EU Data Boundary and customers in the UK will have Anthropic models disabled by default. Anthropic models aren't currently available for use in government clouds (GCC, GCC High, DoD) or sovereign clouds.
+Anthropic models deployed in Microsoft offerings such as Microsoft 365 Copilot, Researcher, Copilot Studio, Power Platform, and Copilot in Microsoft 365 apps are currently excluded from the EU Data Boundary, and when applicable, in-country processing commitments. Customers within the EU Data Boundary and customers in the UK will have Anthropic models disabled by default.
+Anthropic models deployed in Microsoft offerings are currently deployed outside the FedRAMP-authorized Microsoft Government Community Cloud (GCC) boundary. Customer Data processed through these optional integration capabilities will be processed outside the GCC environment, as described in the applicable Product Terms and subprocessor disclosures.
+Due to the heightened regulatory, security, and procurement requirements under which federal agencies operate, the option to use Anthropic models is currently available only in non-federal GCC envir
```

---

### 2. Get ready for Copilot with SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management
**Section:** SharePoint Administration
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Graph Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`

**What Changed:**
```diff
--- +++ @@ -260,7 +260,9 @@ .
 In the SharePoint admin center, select the
 Copilot
-button.
+button, and then select the
+View prompts
+button in the lower corner of the Copilot pane.
 In Microsoft Teams, select
 Apps
 , and then search for

```

---

### 3. SharePoint Admin Agent (Content Governance Agent)

**URL:** https://learn.microsoft.com/en-us/sharepoint/content-governance-agent
**Section:** SharePoint Administration
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -72,6 +72,12 @@ Microsoft 365 Backup
 , and
 version history
+Manage data residency compliance
+with
+Multi-Geo capabilities
+, such as cross-geography content move status reports (
+Preview
+)
 SharePoint Admin Agent prerequisites
 Your organization must have SharePoint Advanced Management. See
 SharePoint Advanced Management prerequisites
@@ -80,20 +86,23 @@ SharePoint Advanced Management Administrator
 role assigned in Microsoft Entra ID.
 Open the SharePoint Admin Agent
-Open the SharePoint Admin Agent in Microsoft 365 Copilot, the SharePoint admin center, or Microsoft Teams.
-SharePoint Admin Agent in Microsoft 365 Copilot
+Open the SharePoint Admin Agent by using any of the following methods:
+Open the SharePoint Admin Agent in the Microsoft 365 Copilot app
+Access content governance skills for Copilot in the SharePoint admin center
+Open the SharePoint Admin Agent in Microsoft Teams
+Open the SharePoint Admin Agent in Microsoft 365 Copilot
 In the Microsoft 365 Copilot app, expand
 Agents
 , and search for the SharePoint Admin Agent.
-After adding it, you can use the agent in the Copilot app.
-Prompts for Copilot in the SharePoint admin center
-In the SharePoint admin center, select the
+Use the agent in the Copilot app.
+Access content governance skills in Copilot in the SharePoint admin center
+Copilot in the SharePoint admin center includes content governance skills.
+Select the
 Copilot
-button.
-Select the
+button, and then select the
 View prompts
-button to view and use Governance skills.
-SharePoint Admin Agent in Microsoft Teams
+button to view and use governance skills.
+Open the SharePoint Admin Agent in Microsoft Teams
 In Microsoft Teams, select
 Apps
 , and then search for
@@ -101,20 +110,39 @@ .
 Get started with example prompts
 To help you get started, the SharePoint Admin Agent suggests prompts that you can try in your environment.
-Here are some more example prompts:
+As you submit a question, the SharePoint Admin Agent responds 
```

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*