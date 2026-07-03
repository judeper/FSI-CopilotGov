# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-03
**Run Time:** 2026-07-03T12:00:11.460401+00:00
**Total URLs Checked:** 152

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 4 |
| MEDIUM Changes | 6 |
| Redirects | 1 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | release-notes | CRITICAL | 4.12 | Monitor |
| 2 | cowork-admin-governance | HIGH | None | Review and update |
| 3 | cowork-faq | HIGH | None | Review and update |
| 4 | concept-conditional-access-policy-common | CRITICAL | 2.3 | Monitor |
| 5 | overview-copilot-connector | MEDIUM | 2.13 | Review optional |
| 6 | overview-declarative-agent | MEDIUM | 1.13, 2.14 | Review optional |
| 7 | authoring-select-agent-model | CRITICAL | 4.14, 1.16 | Monitor |
| 8 | agents-are-apps | MEDIUM | None | Review optional |
| 9 | data-privacy-security | HIGH | None | Review and update |
| 10 | archive-overview | HIGH | 3.2 | Review and update |

---

## HIGH: Control Review Recommended

### 1. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -40,12 +40,16 @@ Manage plugins in Microsoft 365 admin center
 .
 Manage models
-Cowork ships with several models: Claude Opus and Sonnet variants from Anthropic, the Sonnet+Opus Advisor pairing, GPT 5.5, and Imagen 2 for image generation.
-As an admin, you can turn off individual models in the
+Cowork ships with several models: Claude Opus and Sonnet variants from Anthropic, Claude Fable 5 (Preview), the Sonnet+Opus Advisor pairing, GPT 5.5, and Imagen 2 for image generation. Claude Fable 5 (Preview) is off by default; turn it on in the
+Microsoft 365 admin center
+under Copilot settings if you want to make it available. Some models, such as Claude Fable 5, require data retention, which means a user's prompts and responses for that model are retained by the model provider.
+As an admin, you can turn off the Anthropic model family in the
 Microsoft 365 admin center
 under Copilot settings.
-Microsoft might deploy other AI models for Microsoft 365 Copilot to use that are hosted and operated by Microsoft. These models are governed by the same contractual and data protection commitments already in place, including that no data leaves Microsoft. For more information about models that Microsoft 365 Copilot might use, see
+Microsoft might deploy other AI models for Microsoft 365 Copilot to use that are hosted and operated by Microsoft. These models are governed by the same contractual and data protection commitments already in place, including that no data leaves Microsoft. For more information about the use of Azure-hosted GPT models in Microsoft 365 Copilot, visit
 Understanding AI functionality and models in Microsoft Online Services
+, or for information about the use of Anthropic models, visit
+Anthropic as a subprocessor for Microsoft Online Services
 .
 For details on each model and how end users pick them, see
 Choose a model for Cowork

```

---

### 2. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -323,7 +323,9 @@ Auto
 and Cowork will choose the model that fits your task. To pick a specific model, select
 Auto
-in the chat header and choose from the list that your organization makes available, which can include Claude Opus and Sonnet variants, the Sonnet+Opus Advisor pairing, and GPT 5.5. For details, see
+in the chat header and choose from the list that your organization makes available, which can include Claude Opus and Sonnet variants, Claude Fable 5 (Preview), the Sonnet+Opus Advisor pairing, and GPT 5.5. Claude Fable 5 (Preview) is off by default, so it appears only after an admin turns it on in the
+Microsoft 365 admin center
+under Copilot settings. Some models, such as Claude Fable 5, require data retention, and Cowork shows a note in the picker and a banner while the model is selected. For details, see
 Choose a model for Cowork
 .
 Where are my files saved?

```

---

### 3. Copilot agent security and compliance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/data-privacy-security
**Section:** Agent Governance
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -45,6 +45,72 @@ external group
 .
 Prompts, responses, and data accessed through Microsoft Graph aren't used to train foundation LLMs, including those used by Microsoft 365 Copilot.
+Governance and admin controls for agent sharing
+Agents in Microsoft 365 Copilot operate within existing Microsoft 365 data access boundaries. They do not grant new permissions or provide access to data beyond what a user is already authorized to access. Instead, agents package repeatable prompts and configured data sources, while respecting the controls enforced across Microsoft 365.
+IT administrators can use Microsoft 365 controls and tools to manage how agents are shared, discovered, and governed across their lifecycle.
+Permission inheritance
+Agents respect existing Microsoft 365 permissions. If a user does not have access to a SharePoint site, Teams channel, or Outlook mailbox, the agent cannot retrieve or display content from those sources.
+Agents do not introduce new privileges. They operate within the same identity-based access model enforced by Microsoft Graph across Microsoft 365 services.
+DLP, retention, and compliance controls
+Agents interact with data that remains governed by existing Microsoft 365 data loss prevention (DLP), retention, and compliance policies. Content accessed through connected services, such as SharePoint, Exchange, and Teams, continues to be subject to the policies configured for those services.
+Organizations with DLP and retention policies in place can expect those policies to apply to the underlying data accessed by agents. The behavior of agent interactions may depend on how those interactions are processed within Microsoft 365.
+Audit logs and activity reports
+Microsoft 365 audit logs and reporting capabilities provide visibility into Copilot activity, including agent-related usage. These capabilities help administrators monitor usage and understand how Copilot experiences are used across the organization.
+The level of detail avail
```

---

### 4. Microsoft 365 Archive overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/archive/archive-overview?view=o365-worldwide
**Section:** Microsoft 365 Archive
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 3.2: Control 3.2: Data Retention Policies for Copilot Interactions
  - File: `controls/pillar-3-compliance/3.2-data-retention-policies.md`

**What Changed:**
```diff
--- +++ @@ -27,6 +27,10 @@ Microsoft 365 Archive allows you to retain inactive data by moving it into a cold storage tier within SharePoint. Data archived with Microsoft 365 Archive automatically retains the same searchability, security, and
 compliance
 standards at a reduced cost.
+Note
+Microsoft 365 Archive for SharePoint sites is now available for Government Community Cloud (GCC) organizations. To get started, configure a pay-as-you-go billing policy by following the guidance on
+Setup and manage pay-as-you-go billing in the Billing node of the Microsoft 365 admin center
+guide. After the billing policy is connected, enable SharePoint Site Archive from the Settings page.
 Other advantages of using Microsoft 365 Archive include:
 Copilot optimization
 - Copilot is not trained on archived content, maximizing response relevancy.

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot release notes
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Classification:** CRITICAL (UI navigation steps changed)

---

### 2. Common Conditional Access policies
**URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common
**Classification:** CRITICAL (Deprecation notice)

---

### 3. Microsoft Graph connectors overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-copilot-connector?toc=%2Fgraph%2Ftoc.json
**Classification:** MEDIUM (General content update)

---

### 4. Declarative agents for Copilot
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent
**Classification:** MEDIUM (General content update)

---

### 5. Select an agent model
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
**Classification:** CRITICAL (Deprecation notice)

---

### 6. Microsoft 365 Copilot agent governance
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps
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