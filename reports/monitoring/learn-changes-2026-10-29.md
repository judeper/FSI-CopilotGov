# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-29
**Run Time:** 2026-10-29T16:30:19.949772+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 9 |
| HIGH Changes | 1 |
| MEDIUM Changes | 4 |
| Redirects | 22 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-requirements | MEDIUM | 1.1, 1.9, 2.15, 1.4 | Update portal-walkthrough |
| 2 | connect-to-ai-models | HIGH | 1.10, 3.8a, 2.7 | Update portal-walkthrough |
| 3 | ...m/en-us/microsoft-365/copilot/cowork/ | MEDIUM | 4.15 | Update portal-walkthrough |
| 4 | whats-new | HIGH | 4.15 | Update portal-walkthrough |
| 5 | cowork-manage-plugins | MEDIUM | 4.15 | Update portal-walkthrough |
| 6 | cowork-faq | HIGH | 4.15 | Update portal-walkthrough |
| 7 | ...-based-billing-manage-copilot-credits | HIGH | 4.15, 1.9, 4.8 | Update portal-walkthrough |
| 8 | ...n.microsoft.com/en-us/entra/agent-id/ | MEDIUM | 2.17 | Update portal-walkthrough |
| 9 | agent-id-governance-overview | HIGH | None | Review and update |
| 10 | ...opilot-sharepoint-advanced-management | CRITICAL | 1.3, 1.13 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot requirements

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

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
--- +++ @@ -194,11 +194,8 @@ Description
 SharePoint Advanced Management
 SharePoint Advanced Management is a set of configurable capabilities that provides administrative content governance controls for SharePoint and OneDrive. SharePoint Advanced Management is available as part of Microsoft 365 Copilot or as an add-on.
-See the following articles:
--
+See
 What is SharePoint Advanced Management?
--
-Get ready for Microsoft Copilot and agents with SharePoint Advanced Management
 Microsoft Purview
 Microsoft Purview helps to mitigate and manage the risks associated with AI usage, and implement corresponding protection and governance controls.
 See the following articles:

```

---

### 2. Connect to xAI models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.10/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.10/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -36,10 +36,10 @@ View all
 .
 Select
-AI providers for other large language models
+AI providers operating as independent processors
 .
 Under
-Available models for your organization
+Available model providers for your organization
 , choose
 SpaceXAI
 .
@@ -79,10 +79,10 @@ View all
 .
 Select
-AI providers for other large language models
+AI providers operating as independent processors
 .
 Under
-Available models for your organization
+Available model providers for your organization
 , choose
 SpaceXAI
 .

```

---

### 3. Copilot Cowork overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
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
--- +++ @@ -84,6 +84,9 @@ As Cowork loads skills during a session, the side panel updates to show which skills are active.
 Extend with plugins
 Cowork supports plugins from the Microsoft 365 App Store that add new skills and connectors. Plugins can give Cowork specialized expertiseâsuch as financial analysis or legal researchâor connect it to external data sources and services. Your organization's admin can also deploy plugins for everyone in your organization.
+Microsoft's
+role-based and industry plugins
+include Accounting for Cowork (Frontier Public), Finance for Cowork, and Capital Markets for Cowork.
 Learn more about browsing, installing, and managing plugins in
 Use plugins with Cowork
 .

```

---

### 4. What's new in Copilot Cowork

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
**Section:** Copilot Cowork
**Classification:** HIGH (Portal references)

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
--- +++ @@ -7,6 +7,9 @@ Feature
 Description
 Learn more
+Accounting, Finance, and Capital Markets plugins
+Accounting for Cowork (Frontier Public), Finance for Cowork, and Capital Markets for Cowork add role-specific skills for accounting work, financial planning and modeling, and investment research and transaction materials.
+Role-based and industry plugins
 GPT 6.1 Sol model
 GPT 6.1 Sol is now available in the model selector as an intelligent and efficient model for hard work, replacing GPT 6 Sol.
 Choose a model for Cowork
@@ -16,6 +19,22 @@ Projects
 Use projects in Copilot Cowork to keep related tasks, instructions, and context together. Start tasks from a project, return to related chats, and review the files those tasks produce.
 Use projects in Copilot Cowork
+Reference past chats and tasks
+Add a past chat or task to your prompt from
+Copilot
+in the context picker to give Cowork context from earlier work.
+Attach files
+Enhancements
+These updates expand the connectors and event-driven triggers you can use with Cowork.
+Feature
+Description
+Learn more
+Expanded connector support
+Use Power Platform and Copilot connectors to connect Cowork to more external data sources and services.
+Use plugins with Cowork
+Non-Microsoft event-driven triggers
+Start tasks from events in supported non-Microsoft connectors and plugins, such as when a new case is added in a customer relationship management system.
+Set up event-driven tasks
 September 2026
 New features
 Feature

```

---

### 5. Manage Copilot Cowork plugins

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
--- +++ @@ -60,6 +60,9 @@ When you install a plugin, it's automatically acquired for the target users. Users don't need to browse the plugin catalog or install it themselves. The plugin's skills and connectors become available in their Cowork conversations.
 Tip
 Cowork provides several plugins for Microsoft applications, including Dynamics 365 Customer Service, Dynamics 365 ERP, Dynamics 365 Sales, and Fabric IQ. You can find these plugins in the Microsoft 365 App Store and deploy them like any other plugin.
+Microsoft also provides
+role-based and industry plugins
+, including Accounting for Cowork (Frontier Public), Finance for Cowork, and Capital Markets for Cowork. These packages provide role-specific skills. Finance for Cowork and Capital Markets for Cowork are separate from Dynamics 365 ERP and don't themselves connect to an ERP system or a financial market data service. Use the same deployment and availability controls described in this article.
 Learn more in
 Deploy agents in Microsoft Copilot
 .

```

---

### 6. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
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
--- +++ @@ -62,9 +62,12 @@ What can Cowork access?
 Cowork inherits your permissions, so it can access only the files and emails you can already access. If you don't have access to a file or email, Cowork can't access it either. When a referenced file or email has a sensitivity label, Cowork shows that label and displays the highest sensitivity label for the session.
 Can I add plugins to Cowork?
-Yes. Cowork supports plugins from the Microsoft 365 App Store that add new skills and connectors. You can browse and install plugins from the
+Yes. Cowork supports plugins from the Microsoft 365 App Store that add skills, connectors, or both. You can browse and install plugins from the
 Browse plugins
-menu. Once acquired, a plugin's skills appear alongside the built-in skills, and its connectors become available for your sessions.
+menu. Once acquired, a plugin's included skills appear alongside the built-in skills, and any included connectors become available for your sessions.
+Microsoft's role-based plugins include Accounting for Cowork (Frontier Public), Finance for Cowork, and Capital Markets for Cowork. See their capabilities and included skills in
+Role-based and industry plugins
+.
 Get step-by-step instructions in
 Use plugins with Cowork
 .

```

---

### 7. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 4.15: Control 4.15: Copilot Cowork Governance
  - File: `controls/pillar-4-operations/4.15-copilot-cowork-governance.md`
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
- Control 4.8: Control 4.8: Cost Allocation and License Optimization
  - File: `controls/pillar-4-operations/4.8-cost-allocation.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.9/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.9/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.9/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.8/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.8/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.8/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.8/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -5,7 +5,7 @@ Automatically apply existing spending policies to future supported services and agents.
 Configure organizational and user-level spending limits.
 Configure threshold notifications for administrators and users.
-Assign model profiles and billing methods.
+Assign billing methods.
 For initial configuration and billing options, see
 Set up usage-based billing for Copilot Credits
 . To review consumption, see
@@ -51,7 +51,6 @@ Define the policy scope
 Select agents and services
 Set limits and alerts
-Model profiles
 Select a billing method
 Review and add the policy
 Define the policy scope
@@ -116,46 +115,6 @@ Select
 Next
 .
-Model profiles
-Model profiles are reusable sets of model providers and models that you can apply to spending policies. Use model profiles to control which models are available for supported experiences.
-You can also add model profiles directly from
-Cost Management > Configuration
-tab. For more information, see
-Configure model profiles
-.
-To understand more about model profile considerations, see
-Model profile considerations
-.
-Note
-Model profiles are currently available only for
-Copilot Cowork
-. The
-Model profiles
-step appears only when you select
-Cowork
-in a spending policy.
-To create and assign a model profile while creating a spending policy:
-By default, supported models and providers that are available in your organization can be used. You can keep the default model selection or customize model access by applying a model profile. In
-Model profiles
-, select from one of the following options:
-Use default model selection
-to allow Cowork to use all supported models and providers available in your tenant.
-Customize model selection
-to apply an existing model profile or create a new one.
-If you choose
-Customize model selection
-, select an existing profile or select
-Create new model profile
-.
-When creating a model profile:
-Enter a name for the profile.
-Select the model providers and models to i
```

---

### 8. Microsoft Entra Agent ID documentation

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/
**Section:** Agent Governance
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.17: Control 2.17: Cross-Tenant Agent Federation (MCP and Entra Agent ID)
  - File: `controls/pillar-2-security/2.17-cross-tenant-agent-federation.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.17/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.17/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.17/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.17/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -18,6 +18,7 @@ ID Governance for agents
 Access packages for agents
 Maintain agent sponsors and lifecycle
+Default agent inactivity policy
 Protect agent access to resources
 Conditional Access for agents
 ID Protection for agents

```

---

### 9. Get ready for Copilot with SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management
**Section:** SharePoint Administration
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.3/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.3/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1,265 +1,183 @@-Get ready for Microsoft Copilot and agents with SharePoint Advanced Management
-Microsoft Copilot and agents work best for your organization when your content is up to date and well governed. Copilot and agents retrieve data from Microsoft Graph and respect existing permissions, sharing settings, and policies.
-This article describes how to prepare your environment for Copilot and agent usage by using capabilities in
+Configure a secure and governed foundation for Microsoft Copilot
+Applies to: Microsoft Copilot, Microsoft Purview, and SharePoint Advanced Management
+Microsoft Copilot
+uses Work IQ to enhance responses to user prompts using data that the user already has permission to access. When your organization's data is well governed, current, and appropriately shared, Copilot can deliver accurate, relevant, and secure responses.
+This article walks through the steps of preparing, securing, and managing Microsoft Copilot using the process described in the
+Foundational deployment blueprint
+.
+By following these steps, you can help Copilot deliver accurate and relevant results while supporting your organization's security, compliance, and regulatory requirements.
+This guidance is intended for IT administrators and security administrators who are either preparing their organization for Microsoft Copilot or making necessary adjustments to security and governance controls after Copilot is enabled.
+What this article helps you achieve
+By completing the steps in this article, you can:
+Establish guardrails to ensure that users have appropriate access to SharePoint, OneDrive, and Exchange, and that Copilot only references accurate, up-to-date information in line with your organization's policies
+Make informed choices about how Copilot can and can't interact with your organization's sensitive data, ensuring control and flexibility in data usage and access
+Monitor changes and Copilot activity to identify and remediate risk.
+Licensing
+T
```

---

## HIGH: Control Review Recommended

### 1. Microsoft Entra ID Governance for agent identities

**URL:** https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -39,7 +39,7 @@ Agents created in
 Microsoft Copilot Studio
 can be configured to automatically be assigned to an agent identity. When an agent identity is first created in a Power Platform environment after enabling this setting, a Microsoft Copilot Studio agent identity blueprint, and an agent identity blueprint principal, are automatically created. For more information, see
-Automatically create Entra agent identities for Copilot Studio agents (preview)
+Microsoft Entra Agent IDs for Copilot Studio agents
 .
 For agents in the
 Microsoft Teams

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot requirements
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Classification:** MEDIUM (General content update)

---

### 2. Copilot Cowork overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
**Classification:** MEDIUM (General content update)

---

### 3. Manage Copilot Cowork plugins
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins
**Classification:** MEDIUM (General content update)

---

### 4. Microsoft Entra Agent ID documentation
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-admin-experience |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-manage |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ | https://learn.microsoft.com/en-us/copilot/cowork/ |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new | https://learn.microsoft.com/en-us/copilot/cowork/whats-new |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started | https://learn.microsoft.com/en-us/copilot/cowork/get-started |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance | https://learn.microsoft.com/en-us/copilot/cowork/cowork-admin-governance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models | https://learn.microsoft.com/en-us/copilot/cowork/cowork-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins | https://learn.microsoft.com/en-us/copilot/cowork/cowork-manage-plugins |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq | https://learn.microsoft.com/en-us/copilot/cowork/cowork-faq |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-settings?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*