# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-02
**Run Time:** 2026-07-02T12:02:41.010320+00:00
**Total URLs Checked:** 152

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 7 |
| MEDIUM Changes | 3 |
| Redirects | 1 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | release-notes | CRITICAL | 4.12 | Monitor |
| 2 | whats-new | HIGH | 4.12 | Review and update |
| 3 | connect-to-ai-subprocessor | HIGH | 3.8a, 2.7 | Review and update |
| 4 | ...e-information-type-entity-definitions | HIGH | None | Review and update |
| 5 | security-for-ai-overview | HIGH | None | Review and update |
| 6 | agent-id | HIGH | 2.3, 2.17 | Review and update |
| 7 | compliance-manager-update-actions | MEDIUM | 3.12 | Review optional |
| 8 | compliance-manager-assessments | HIGH | None | Review and update |
| 9 | ...opilot-sharepoint-advanced-management | HIGH | 1.13, 1.3 | Review and update |
| 10 | site-lifecycle-management | MEDIUM | 1.7 | Review optional |

---

## HIGH: Control Review Recommended

### 1. What's new in Microsoft Purview

**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.12: Control 4.12: Change Management for Copilot Feature Rollouts
  - File: `controls/pillar-4-operations/4.12-change-management-rollouts.md`

**What Changed:**
```diff
--- +++ @@ -37,6 +37,25 @@ for data governance solutions.
 Roadmap
 for data security and risk and compliance solutions.
+July 2026
+Data Loss Prevention
+In preview
+: Protect sensitive data in text and prompts by integrating with Microsoft Entra Global Secure Access (GSA). This integration enables organizations to intercept and inspect text and AI interactions at the network layer, enforce restrictive actions based on DLP policies, and detect risky user activity through Insider Risk Management. It helps prevent sensitive data from being shared with untrusted cloud applications through browsers, apps, APIs, and add-ins, including generative AI platforms, social media, and collaborative platforms. See
+Learn about Microsoft Purview Network Data Security
+.
+Insider Risk Management
+In preview
+:
+Unified alert experience
+combines the Triage Agent and Standard alert dashboards into a single alerts list page. View and manage both classic and agent-triaged alerts from one location, with the ability to preview agent summaries, alert and user details directly on the alerts list page.
+In preview
+:
+Expanded user profile details
+in the unified alert experience add additional user profile signals from Microsoft Entra, including office location, employee type, department, and last working date.
+In preview
+:
+Expanded note capabilities
+across alerts and cases. Analysts and investigators can now add and view notes on both alerts and cases. System-generated notes are automatically applied when there's a change in alert or case status, assigned user, closure, or case escalation.
 June 2026
 Copilot Cowork
 General availability (GA)
@@ -577,83 +596,6 @@ : The client-side improvements for
 sensitivity labels that extend SharePoint permissions to downloaded documents
 that started to roll out to Windows version 2601+ in January for the Current Channel is complete, and now also available with the Monthly Enterprise Channel.
-January 2026
-Adaptive scopes
-New
-: As an alterna
```

---

### 2. Anthropic as a Microsoft subprocessor

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`

**What Changed:**
```diff
--- +++ @@ -24,7 +24,7 @@ Summarize this article for me
 Microsoft is introducing a new offering with Anthropic AI models as part of Microsoft Online Services, delivering enterprise-grade commitments and safeguards to ensure secure and responsible use of Anthropic models within your organization.
 To enable this change, Anthropic has onboarded as a Microsoft subprocessor. This change simplifies the experience and strengthens compliance and security under Microsoft's enterprise framework. The Microsoft Customer Copyright Commitment (CCC) applies to Anthropic models used within products covered by the CCC, including Microsoft 365 Copilot and Copilot Studio.
-As a subprocessor, Anthropic will operate with Microsoft oversight through contractual safeguards and appropriate technical and organizational measures. Unless models are labeled "Preview models with Data Retention," the
+As a subprocessor, Anthropic operates with Microsoft oversight through contractual safeguards and appropriate technical and organizational measures. Unless models are labeled "Preview models with Data Retention," the
 Microsoft Product Terms
 and
 Microsoft Data Protection Addendum (DPA)
@@ -36,10 +36,12 @@ . To see a list of Microsoft subprocessors, see
 Service Trust Portal
 .
-Microsoft will enable Anthropic models on by default for most customers in commercial cloud (excluding EU/EFTA and UK). This update gives users in your organization the ability to use multiple AI models in their Microsoft offerings, such as in Microsoft 365 Copilot, Researcher, Copilot Studio, Power Platform, and Copilot in Microsoft 365 apps. This affirms Microsoft's commitment to offering choice between leading AI models while maintaining enterprise-grade security and compliance.
+Microsoft enables Anthropic models on by default for most customers in commercial cloud (excluding EU/EFTA and UK). This update gives users in your organization the ability to use multiple AI models in their Microsoft offerings, such as in Mi
```

---

### 3. Sensitive information type entity definitions

**URL:** https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -29,8 +29,8 @@ Low confidence: 65 or below
 Medium confidence: 75
 High confidence: 85
-ABA routing number
-All credentials
+ABA Routing Number
+All Credential Types
 All full names
 All medical terms and conditions
 All Physical Addresses
@@ -39,20 +39,20 @@ Argentina Unique Tax Identification Key (CUIT/CUIL)
 ASP.NET machine Key
 Australia bank account number
-Australia business number
-Australia company number
-Australia drivers license number
+Australian Business Number
+Australian Company Number
+Australia Driver's License Number
 Australia medical account number
 Australia passport number
 Australia physical addresses
 Australia tax file number
-Austria drivers license number
+Austria Driver's License Number
 Austria identity card
 Austria passport number
 Austria physical addresses
 Austria social security number
 Austria tax identification number
-Austria value added tax
+Austria Value Added Tax (VAT) Number
 Azure App Service deployment password
 Azure Batch shared access key
 Azure Bot Framework secret key
@@ -97,7 +97,7 @@ Brand medication names
 Brazil CPF number
 Brazil legal entity number (CNPJ)
-Brazil national identification card (RG)
+Brazil National ID Card (RG)
 Brazil physical addresses
 Bulgaria driver's license number
 Bulgaria passport number
@@ -122,7 +122,7 @@ Croatia passport number
 Croatia personal identification (OIB) number
 Croatia physical addresses
-Cyprus drivers license number
+Cyprus Driver's License Number
 Cyprus identity card
 Cyprus passport number
 Cyprus physical addresses
@@ -146,8 +146,8 @@ EU driver's license number
 EU national identification number
 EU passport number
-EU social security number or equivalent identification
-EU Tax identification number
+EU Social Security Number (SSN) or Equivalent ID
+EU Tax Identification Number (TIN)
 Finland driver's license number
 Finland European health insurance number
 Finland national ID
@@ -159,7 +159,7 @@ France passport number
 France physical addresses
 France s
```

---

### 4. Microsoft Entra security for AI overview

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/security-for-ai-overview
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -27,8 +27,8 @@ This article explains why AI systems need identity-based security, introduces the key Microsoft Entra capabilities that address these challenges, and links to detailed documentation for each area.
 Why AI systems need identity-based security
 Organizations are deploying AI agents for increasingly diverse tasks, and each deployment model presents distinct security challenges:
-Assistive agents (interactive)
-Assistive agents (also called interactive agents) perform specific tasks on demand on behalf of a signed-in user, often through a chat interface. Tasks include analyzing customer data for sales recommendations or answering support questions with escalation to human representatives. These agents are granted Microsoft Entra delegated permissions that allow them to act on behalf of users. Common scenarios include customer support assistants, research helpers, and real-time collaboration agents.
+Interactive agents
+Interactive agents perform specific tasks on demand on behalf of a signed-in user, often through a chat interface. Tasks include analyzing customer data for sales recommendations or answering support questions with escalation to human representatives. These agents are granted Microsoft Entra delegated permissions that allow them to act on behalf of users using the on-behalf-of (OBO) authentication flow. Common scenarios include customer support assistants, research helpers, and real-time collaboration agents.
 Autonomous agents
 Autonomous agents operate independently using their own identity, not a human user's identity. These agents run in the background, making decisions and taking actions without human intervention, such as monitoring network logs for security operations, managing infrastructure deployments with autoscaling, or processing scheduled maintenance tasks. Autonomous agents authenticate directly with the Microsoft Entra ID platform using their agent identity and the client credentials flow.
 Agent's user account

```

---

### 5. Conditional Access for agent identities

**URL:** https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.3: Control 2.3: Conditional Access Policies for Copilot Workloads
  - File: `controls/pillar-2-security/2.3-conditional-access-policies.md`
- Control 2.17: Control 2.17: Cross-Tenant Agent Federation (MCP and Entra Agent ID)
  - File: `controls/pillar-2-security/2.17-cross-tenant-agent-federation.md`

**What Changed:**
```diff
--- +++ @@ -67,7 +67,7 @@ Agent OAuth flows: On-behalf-of
 .
 Note
-The on-behalf-of flow is also known as delegated access. Agents using this type of access are sometimes called interactive agents or assistive agents, as they involve a user interface for human interaction.
+The on-behalf-of flow is also known as delegated access. "On-behalf-of" describes the authentication flow, not the type of agent. These interactive agents involve a user interface for human interaction. Any agent can use this flow when a signed-in user is present and the agent needs to access resources with that user's identity and permissions.
 In this flow, the agent can't reuse the user's original token because it was issued for a different audience. Instead, the agent uses the OBO flow to exchange tokens with Microsoft Entra ID, obtaining a new token scoped to the target resource. This token exchange is also evaluated by Conditional Access, letting admins enforce granular controls over which resources agents can access on behalf of the user.
 Because the user is the subject in this flow, Conditional Access policies target
 users and groups
@@ -92,9 +92,9 @@ Agents acting as a user
 Sometimes it's not enough for an agent to perform tasks on behalf of a user or operate with its own identity. In certain scenarios, an agent has its own
 agent's user account
-. For example, digital workers that function as team members with their own mailboxes, access to chat, and can participate in collaborative workflows as a team member.
+that functions as a digital worker with its own mailbox, access to chat, and the ability to participate in collaborative workflows as a team member.
 In this model, an admin creates a user account in the directory and links it to the agent's identity. From there, it's like any other user account. Licenses can be assigned to access Microsoft 365 resources such as a mailbox and calendar. The account can be added to administrative units and security groups just like a human user
```

---

### 6. Build and manage Compliance Manager assessments

**URL:** https://learn.microsoft.com/en-us/purview/compliance-manager-assessments
**Section:** Compliance Manager
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -68,7 +68,7 @@ : The services covered by the assessment, such as Microsoft 365, Microsoft Azure, or other cloud services.
 Regulation
 : The regulatory template serving as the basis for the assessment.
-To filter your view of assessments:
+To filter your view of assessments, follow these steps:
 Select
 Filter
 at the top-left corner of your assessments list.
@@ -84,8 +84,8 @@ Data protection baseline default assessment
 To get you started, Microsoft provides a default
 Data Protection Baseline
-assessment that's included at all subscription levels. This baseline assessment has a set of controls for key regulations and standards for data protection and general data governance. This baseline draws elements primarily from NIST CSF (National Institute of Standards and Technology Cybersecurity Framework) and ISO (International Organization for Standardization), as well as from FedRAMP (Federal Risk and Authorization Management Program) and GDPR (General Data Protection Regulation of the European Union).
-This assessment is used to calculate your initial compliance score the first time you come to Compliance Manager, before you configure any other assessments. Compliance Manager collects initial signals from your Microsoft 365 solutions. You see at a glance how your organization is performing relative to key data protection standards and regulations, and see suggested improvement actions to take. Compliance Manager becomes more helpful as you build and manage your own assessments to meet your organization's particular needs.
+assessment that's included at all subscription levels. This baseline assessment has a set of controls for key regulations and standards for data protection and general data governance. The Data Protection Baseline assessment draws elements primarily from NIST CSF (National Institute of Standards and Technology Cybersecurity Framework) and ISO (International Organization for Standardization), as well as from FedRAMP (Federal Risk and Autho
```

---

### 7. Get ready for Copilot with SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Graph Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`

**What Changed:**
```diff
--- +++ @@ -49,7 +49,8 @@ Step 2: Employ site lifecycle management and archiving
 Site lifecycle management policies and archiving help ensure that your sites are up to date, compliant, and use storage efficiently. These capabilities help ensure Copilot and agentic experiences reference current content and can reduce storage costs.
 Site lifecycle management
-Site lifecycle management policies help reduce content sprawl by automating the process of ensuring that your organization's SharePoint sites are well governed.
+Site lifecycle management policies
+help reduce content sprawl by automating the process of ensuring that your organization's SharePoint sites are well governed.
 When you set up your site lifecycle management policies, the system automatically identifies potential problems. You can configure enforcement actions and email notifications that ask site owners or administrators to take action.
 View or create site lifecycle management policies
 In the SharePoint admin center, in the navigation pane, select

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot release notes
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Classification:** CRITICAL (Deprecation notice)

---

### 2. Update improvement actions
**URL:** https://learn.microsoft.com/en-us/purview/compliance-manager-update-actions
**Classification:** MEDIUM (General content update)

---

### 3. SharePoint site lifecycle management
**URL:** https://learn.microsoft.com/en-us/sharepoint/site-lifecycle-management
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