# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-19
**Run Time:** 2026-08-19T10:18:41.150772+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 33 |
| HIGH Changes | 9 |
| MEDIUM Changes | 6 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | HIGH | 1.4 | Update portal-walkthrough |
| 2 | microsoft-365-copilot-setup | HIGH | 2.6 | Update portal-walkthrough |
| 3 | manage-public-web-access | HIGH | 2.15, 2.6 | Update portal-walkthrough |
| 4 | microsoft-365-copilot-requirements | HIGH | 1.9, 1.1, 2.15 | Update portal-walkthrough |
| 5 | microsoft-365-copilot-privacy | HIGH | 1.10, 1.4, 2.7, 2.6, 3.8, 3.8a, 3.10 | Update portal-walkthrough |
| 6 | ...soft-365-copilot-enablement-resources | HIGH | 1.12, 1.11 | Update portal-walkthrough |
| 7 | copilot-teams-transcription | HIGH | 4.2 | Update portal-walkthrough |
| 8 | microsoft-365-copilot-usage | CRITICAL | 4.5 | Update portal-walkthrough |
| 9 | semantic-index-for-copilot | HIGH | 1.4 | Update portal-walkthrough |
| 10 | ...t-365-copilot-search-admin-experience | HIGH | 1.4 | Update portal-walkthrough |
| 11 | microsoft-365-copilot-search-manage | HIGH | None | Review and update |
| 12 | ...ilot-foundational-deployment-guidance | HIGH | 1.2 | Update portal-walkthrough |
| 13 | ...data-foundation-microsoft-365-copilot | HIGH | 1.7 | Update portal-walkthrough |
| 14 | connect-to-ai-models | HIGH | 1.10, 2.7, 3.8a | Update portal-walkthrough |
| 15 | connect-to-ai-subprocessor | HIGH | 1.10, 2.7, 3.8a | Update portal-walkthrough |
| 16 | ...lot-ai-provider-user-sec-group-access | HIGH | None | Review and update |
| 17 | cpcn-admin-configuration | HIGH | 2.11 | Update portal-walkthrough |
| 18 | cpcn-compliance-summary | MEDIUM | 2.11 | Update portal-walkthrough |
| 19 | ...m/en-us/microsoft-365/copilot/cowork/ | HIGH | None | Review and update |
| 20 | whats-new | MEDIUM | 4.15 | Update portal-walkthrough |
| 21 | get-started | HIGH | None | Review and update |
| 22 | cowork-admin-governance | HIGH | 4.15 | Update portal-walkthrough |
| 23 | cowork-models | HIGH | 4.15 | Update portal-walkthrough |
| 24 | cowork-manage-plugins | HIGH | 4.15 | Update portal-walkthrough |
| 25 | cowork-faq | HIGH | None | Review and update |
| 26 | discovery-setting-ai-experiences | MEDIUM | 4.15 | Update portal-walkthrough |
| 27 | ...-based-billing-manage-copilot-credits | HIGH | 4.15 | Update portal-walkthrough |
| 28 | communication-compliance-channels | HIGH | None | Review and update |
| 29 | manage-copilot-agents-integrated-apps | HIGH | 1.13, 2.14, 2.13, 2.17, 4.1, 4.13 | Update portal-walkthrough |
| 30 | copilot-tuning-admin-guide | HIGH | 1.16 | Update portal-walkthrough |
| 31 | m365-agents-admin-guide | HIGH | None | Review and update |
| 32 | agent-365-overview | HIGH | 1.13, 4.5, 4.13 | Update portal-walkthrough |
| 33 | agent-registry | HIGH | 2.14, 4.13, 4.14 | Update portal-walkthrough |
| 34 | agent-settings | MEDIUM | 1.13, 2.14, 2.13, 4.13 | Update portal-walkthrough |
| 35 | restricted-sharepoint-search | HIGH | 1.4, 1.3, 2.5 | Update portal-walkthrough |
| 36 | advanced-management | MEDIUM | 1.7, 2.5 | Update portal-walkthrough |
| 37 | ...opilot-sharepoint-advanced-management | HIGH | 1.13, 1.3 | Update portal-walkthrough |
| 38 | insights-on-sharepoint-agents | HIGH | None | Review and update |
| 39 | copilot-in-sharepoint-get-started | HIGH | None | Review and update |
| 40 | site-lifecycle-management | CRITICAL | 1.7 | Update portal-walkthrough |
| 41 | restricted-content-discovery | HIGH | 1.7, 1.13, 1.4, 1.2, 1.3, 2.5 | Update portal-walkthrough |
| 42 | content-governance-agent | MEDIUM | 1.7 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -19,7 +19,7 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Microsoft 365 Copilot overview
+Microsoft Copilot overview
 Feedback
 Summarize this article for me
 Note
@@ -29,30 +29,30 @@ Microsoft has onboarded Anthropic as a Microsoft subprocessor. For more information, see
 Anthropic as a subprocessor for Microsoft Online Services
 .
-Microsoft 365 Copilot is an AI-powered tool that helps with your work tasks
+Microsoft Copilot is an AI-powered tool that helps with your work tasks
 .
 Users enter a prompt in Copilot and Copilot responds with AI-generated information. The responses are in real-time and can include internet-based content and work content that users have permission to access.
 Users get content relevant to their work tasks, and in the context of the Microsoft 365 app they're using.
-The following video provides an overview of Microsoft 365 Copilot. It's 1 minute and 49 seconds long.
-Using Microsoft 365 Copilot
+The following video provides an overview of Microsoft Copilot. It's 1 minute and 49 seconds long.
+Using Microsoft Copilot
 Say, for example, you're an operations manager and are working with human resources to update job descriptions. By providing Copilot the basic job requirements, you can ask Copilot to create a job description. You can also have Copilot add various job requirements and qualifications that should be included in the description. In the same prompting session, you can expand the generated job description to create different levels, like Level 1, Level 2, and Level 3.
 You can also
 create and use agents
 to customize your Copilot experience with your organization's data sources. For example, say you're a warehouse manager and you need to know the status of a shipment. You can ask your Copilot shipping agent "What is the status of shipment 1234?" Copilot uses your data sources to get the information and can respond with the status.
-This article is for IT admins. It describes the
```

---

### 2. Microsoft 365 Copilot setup guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.6: Control 2.6: Copilot Web Search and Web Grounding Controls
  - File: `controls/pillar-2-security/2.6-web-search-controls.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.6/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.6/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -19,12 +19,12 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Set up Microsoft 365 Copilot and assign licenses
+Set up Microsoft Copilot and assign licenses
 Feedback
 Summarize this article for me
 As part of your
-Microsoft 365 Copilot adoption
-, the next step is to enable security features, configure the update channel, and assign Copilot licenses to users. This article provides guidance for IT administrators on how to prepare your organization for Microsoft 365 Copilot. It covers foundational implementation and readiness activities, licensing, and steps to ensure a secure and compliant deployment.
+Microsoft Copilot adoption
+, the next step is to enable security features, configure the update channel, and assign Copilot licenses to users. This article provides guidance for IT administrators on how to prepare your organization for Microsoft Copilot. It covers foundational implementation and readiness activities, licensing, and steps to ensure a secure and compliant deployment.
 Prerequisites
 Admin center roles
 This article uses the following admin centers. These admin centers require a specific role to complete the tasks in the article.
@@ -41,10 +41,10 @@ Permissions in the Microsoft Purview portal
 .
 Licensing
-To purchase Microsoft 365 Copilot, make sure you have an appropriate subscription plan. Microsoft 365 Copilot is included as part of the Microsoft 365 E7 subscription plan. Microsoft 365 Copilot licenses are available as an add-on to other licensing plans. For more information, see
-Microsoft 365 Copilot license options
-.
-You can purchase Microsoft 365 Copilot licenses through the
+To purchase Microsoft Copilot, make sure you have an appropriate subscription plan. Microsoft Copilot is included as part of the Microsoft 365 E7 subscription plan. Microsoft Copilot licenses are available as an add-on to other licensing plans. For more information, see
+Microsoft Copilot license options
+.
+You can purcha
```

---

### 3. Manage Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`
- Control 2.6: Control 2.6: Copilot Web Search and Web Grounding Controls
  - File: `controls/pillar-2-security/2.6-web-search-controls.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.15/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.6/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.6/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -18,65 +18,67 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Data, privacy, and security for web search in Microsoft 365 Copilot and Microsoft 365 Copilot Chat
+Data, privacy, and security for web search in Microsoft Copilot and Microsoft Copilot Chat
 Feedback
 Summarize this article for me
-Microsoft 365 Copilot and
-Microsoft 365 Copilot Chat
-have an optional feature that allows Copilot to reference web content when responding to user prompts. Allowing Microsoft 365 Copilot and Microsoft 365 Copilot Chat to reference web content improves the quality of Copilot responses by grounding them in the latest information from the web.
-Note
-This article concerns the web search functionality in Microsoft 365 Copilot and Microsoft 365 Copilot Chat. Microsoft 365
-Copilot Search
-is an additional, universal search experience that allows users with a Microsoft 365 Copilot license to search across all their Microsoft 365 and third-party data sources. Learn more about
-Microsoft 365 Copilot Search
+Note
+Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat. Some experiences, licenses, and capabilities might continue to reference Microsoft 365 Copilot and Microsoft 365 Copilot Chat during the transition period. There are no changes to security, compliance, and privacy for organizations.
+Microsoft Copilot and
+Microsoft Copilot Chat
+have an optional feature that allows Copilot to reference web content when responding to user prompts. Allowing Microsoft Copilot and Microsoft Copilot Chat to reference web content improves the quality of Copilot responses by grounding them in the latest information from the web.
+Note
+This article concerns the web search functionality in Microsoft Copilot and Microsoft Copilot Chat. Microsoft Copilot Search is an additional, universal search experience that allows users with a Microsoft Copilot license to search across all their
```

---

### 4. Microsoft 365 Copilot requirements

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.1/verification-testing.md` (HIGH)
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
--- +++ @@ -19,21 +19,21 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Microsoft 365 app and network requirements for Microsoft 365 Copilot
+Microsoft 365 app and network requirements for Microsoft Copilot
 Feedback
 Summarize this article for me
-Microsoft 365 Copilot
+Microsoft Copilot
 is an AI-powered productivity tool that integrates with Microsoft 365 Apps. This integration allows users to use Copilot in individual apps, such as Word, PowerPoint, Teams, Excel, Outlook, and more. The Copilot experiences are designed to provide users with an AI assistant in the apps they use every day.
-As a result of this integration, there are some app and network requirements for Microsoft 365 Copilot to integrate with your Microsoft 365 apps. These requirements are nearly identical to the requirements for using Microsoft 365 Apps.
+As a result of this integration, there are some app and network requirements for Microsoft Copilot to integrate with your Microsoft 365 apps. These requirements are nearly identical to the requirements for using Microsoft 365 Apps.
 As part of your
-Microsoft 365 Copilot adoption
+Microsoft Copilot adoption
 , make sure you configure the app and network requirements that allow the app integration.
-This article lists the Microsoft 365 app and network requirements to use Microsoft 365 Copilot in your Microsoft 365 apps.
+This article lists the Microsoft 365 app and network requirements to use Microsoft Copilot in your Microsoft 365 apps.
 This article applies to:
-Microsoft 365 Copilot
+Microsoft Copilot
 Prerequisites
 Users must have a Microsoft 365 license assigned to them. You can find the list of eligible base licenses in
-Microsoft 365 Copilot license options
+Microsoft Copilot license options
 or in the
 Microsoft 365 Copilot service description guide
 .
@@ -42,13 +42,13 @@ accounts. You can add or sync users using the
 onboarding wizard in the Microsoft 365 admin center
 .
-Microsoft 365 Copilot is onl
```

---

### 5. Data, privacy, and security for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`
- Control 2.6: Control 2.6: Copilot Web Search and Web Grounding Controls
  - File: `controls/pillar-2-security/2.6-web-search-controls.md`
- Control 3.8: Control 3.8: Model Risk Management Alignment (SR 26-2 / OCC Bulletin 2026-13, applying SR 11-7 / OCC 2011-12 principles to generative AI)
  - File: `controls/pillar-3-compliance/3.8-model-risk-management.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 3.10: Control 3.10: SEC Reg S-P -- Privacy of Consumer Financial Information
  - File: `controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.10/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.10/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.6/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.6/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/3.10/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.10/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.10/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.10/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/3.8/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.8/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.8/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.8/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -18,90 +18,92 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Data, Privacy, and Security for Microsoft 365 Copilot
+Data, Privacy, and Security for Microsoft Copilot
 Feedback
 Summarize this article for me
-Microsoft 365 Copilot is a sophisticated processing and orchestration engine that provides AI-powered productivity capabilities by coordinating the following components:
+Note
+Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat. Some experiences, licenses, and capabilities might continue to reference Microsoft 365 Copilot and Microsoft 365 Copilot Chat during the transition period. There are no changes to security, compliance, and privacy for organizations.
+Microsoft Copilot is a sophisticated processing and orchestration engine that provides AI-powered productivity capabilities by coordinating the following components:
 Large language models (LLMs)
 Content in Microsoft Graph, such as emails, chats, and documents that you have permission to access.
 The Microsoft 365 productivity apps that you use every day, such as Word and PowerPoint.
 For an overview of how these three components work together, see
-Microsoft 365 Copilot overview
-. For links to other content related to Microsoft 365 Copilot, see
-Microsoft 365 Copilot documentation
+Microsoft Copilot overview
+. For links to other content related to Microsoft Copilot, see
+Microsoft Copilot documentation
 .
 Important
-Microsoft 365 Copilot, including
-Microsoft 365 Copilot Search
+Microsoft Copilot, including
+Microsoft Copilot Search
 , is compliant with our existing privacy, security, and compliance commitments to Microsoft 365 commercial customers, including the General Data Protection Regulation (GDPR) and European Union (EU) Data Boundary.
-Prompts, responses, and data accessed through Microsoft Graph aren't used to train foundation LLMs, including those used by Microsoft 365 Copilot
```

---

### 6. Microsoft 365 Copilot adoption guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.12: Control 1.12: Training and Awareness Program
  - File: `controls/pillar-1-readiness/1.12-training-awareness.md`
- Control 1.11: Control 1.11: Organizational Change Management and Adoption Planning
  - File: `controls/pillar-1-readiness/1.11-change-management-adoption.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.11/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -19,26 +19,26 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Microsoft 365 Copilot adoption guide and overview for IT admins
+Microsoft Copilot adoption guide and overview for IT admins
 Feedback
 Summarize this article for me
-Microsoft 365 Copilot
-is an AI tool that can find information, get answers to questions, and help with tasks. To help you onboard and adopt Microsoft 365 Copilot in your organization, use the steps in this article.
-This article provides an overview of the steps and resources that can help you enable and start using Microsoft 365 Copilot in your organization.
+Microsoft Copilot
+is an AI tool that can find information, get answers to questions, and help with tasks. To help you onboard and adopt Microsoft Copilot in your organization, use the steps in this article.
+This article provides an overview of the steps and resources that can help you enable and start using Microsoft Copilot in your organization.
 This article applies to:
-Microsoft 365 Copilot
+Microsoft Copilot
 Step 1 - Get your organization ready and use the Microsoft Adoption site
 â
-Use the Microsoft 365 Copilot Optimization Assessment
+Use the Microsoft Copilot Optimization Assessment
 The
-Microsoft 365 Copilot Optimization Assessment
-can help you understand your organization's readiness for Microsoft 365 Copilot. It evaluates your data governance maturity and data security controls.
-Microsoft recommends you complete the assessment before deploying Microsoft 365 Copilot in your organization. Based on the outcomes of the assessment, you can determine your path forward so your organization is ready for Copilot.
+Microsoft Copilot Optimization Assessment
+can help you understand your organization's readiness for Microsoft Copilot. It evaluates your data governance maturity and data security controls.
+Microsoft recommends you complete the assessment before deploying Microsoft Copilot in your organization. Based on the outcomes
```

---

### 7. Copilot in Teams meetings

**URL:** https://learn.microsoft.com/en-us/microsoftteams/copilot-teams-transcription
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.2: Control 4.2: Copilot in Teams Meetings Governance
  - File: `controls/pillar-4-operations/4.2-teams-meetings-governance.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.2/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -25,8 +25,8 @@ APPLIES TO:
 Meetings
 Events
-Microsoft 365 Copilot in Teams meetings and events is an artificial intelligence (AI) tool that captures important conversation points.
-Each participant with a Microsoft 365 Copilot license in a meeting or in an event with up to 1,000 attendees can ask prompts that are only visible to them. Participants and organizers can learn things like who said what and where people agree or disagree. Microsoft 365 Copilot in Teams can also recommend follow-up tasks, all in real time during a meeting. In events
+Microsoft Copilot in Teams meetings and events is an artificial intelligence (AI) tool that captures important conversation points.
+Each participant with a Microsoft Copilot license in a meeting or in an event with up to 1,000 attendees can ask prompts that are only visible to them. Participants and organizers can learn things like who said what and where people agree or disagree. Microsoft Copilot in Teams can also recommend follow-up tasks, all in real time during a meeting. In events
 optimized for large audiences
 , only organizers, co-organizers, and presenters can use Copilot during the event.
 As an admin, you can manage how users in your organization use Copilot for Teams meetings and events.
@@ -41,15 +41,15 @@ During and after the meeting
 from the dropdown list in their meeting options. Once someone starts transcription, licensed users can select the Copilot button for use during, and after the meeting or event.
 To learn more about how organizers can use Copilot during and after the meeting, see
-Get started with Microsoft 365 Copilot in Teams in Microsoft Teams meetings
+Get started with Microsoft Copilot in Teams in Microsoft Teams meetings
 .
 Only during the meeting
 When organizers create a meeting or event, they can set Copilot's value to
 Only during the meeting
-from the dropdown list in their meeting options. Once someone with a Microsoft 365 Copilot license selects the Copilot button during 
```

---

### 8. Copilot usage reports

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage?view=o365-worldwide
**Section:** Copilot Administration
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 4.5: Control 4.5: Copilot Usage Analytics and Adoption Reporting
  - File: `controls/pillar-4-operations/4.5-usage-analytics.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.5/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -19,14 +19,14 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Microsoft 365 Copilot usage report
+Microsoft Copilot usage report
 Feedback
 Summarize this article for me
-The Microsoft 365 Copilot usage report provides a summary of how users adopt, retain, and engage with Microsoft 365 Copilot and its associated enabled apps. For Copilot activity on a given day, the report typically becomes available within 48 hours of the end of that day (in UTC).
+The Microsoft Copilot usage report provides a summary of how users adopt, retain, and engage with Microsoft Copilot and its associated enabled apps. For Copilot activity on a given day, the report typically becomes available within 48 hours of the end of that day (in UTC).
 For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see
 Microsoft 365 admin center usage reports overview
 .
-View the Microsoft 365 Copilot usage report in the Microsoft 365 admin center
+View the Microsoft Copilot usage report in the Microsoft 365 admin center
 For information about the roles needed to view usage reports, see "Before you begin" in
 Microsoft 365 admin center usage reports overview
 Go to the
@@ -49,20 +49,20 @@ page, under
 Reports
 , select
-Microsoft 365 Copilot
+Microsoft Copilot
 , and then select
 Copilot
 .
 On the report page, select the
 Usage
 tab to view adoption and usage metrics.
-Interpret the Microsoft 365 Copilot usage report
-At the top, you can filter by different timeframes. You can view the Microsoft 365 Copilot report over the last 7, 28, 90, or 180 days.
-You can view several numbers for Microsoft 365 Copilot usage, which highlight the enablement number and the adoption of the enablement:
+Interpret the Microsoft Copilot usage report
+At the top, you can filter by different timeframes. You can view the Microsoft Copilot report over the last 7, 28, 90, or 180 days.
+You can view several numbers 
```

---

### 9. Semantic Index for Copilot

**URL:** https://learn.microsoft.com/en-us/microsoftsearch/semantic-index-for-copilot
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -19,12 +19,12 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Semantic indexing for Microsoft 365 Copilot
+Semantic indexing for Microsoft Copilot
 Feedback
 Summarize this article for me
-Microsoft 365 Copilot maps your organizationâs data into an advanced lexical and semantic index to power search relevance and accuracy. Copilot can access the context and relationships within your data by utilizing Microsoft Graph, enabling more contextually precise information retrieval. The index enhances interactions with your data, offering users a richer and more seamless experience. Built with a comprehensive approach to security, compliance, and privacy, Copilot ensures that all organizational boundaries within your tenant are respected. With Microsoft 365 Copilot, users can trust that their searches are relevant, accurate, and secure.
+Microsoft Copilot maps your organizationâs data into an advanced lexical and semantic index to power search relevance and accuracy. Copilot can access the context and relationships within your data by utilizing Microsoft Graph, enabling more contextually precise information retrieval. The index enhances interactions with your data, offering users a richer and more seamless experience. Built with a comprehensive approach to security, compliance, and privacy, Copilot ensures that all organizational boundaries within your tenant are respected. With Microsoft Copilot, users can trust that their searches are relevant, accurate, and secure.
 What is an index?
-Microsoft 365 Copilot enhances search with an advanced lexical and semantic understanding of your organizationâs data.
+Microsoft Copilot enhances search with an advanced lexical and semantic understanding of your organizationâs data.
 The concept of indexing data is well established in Microsoft 365. Indexing is one of the important ways that Microsoft 365 services access the tremendous amount of data in Microsoft Graph, where your Mic
```

---

### 10. Copilot Search admin experience

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -19,14 +19,14 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Microsoft 365 Copilot Search admin experience
+Microsoft Copilot Search admin experience
 Feedback
 Summarize this article for me
-The Microsoft 365 Copilot Search admin experience is a new capability in the Microsoft 365 admin center. Use it to manage, customize, and optimize the Copilot Search experience across your organization.
+The Microsoft Copilot Search admin experience is a new capability in the Microsoft 365 admin center. Use it to manage, customize, and optimize the Copilot Search experience across your organization.
 Access Copilot Search in the Microsoft 365 admin center
-You don't need to take any action to set up Microsoft 365 Copilot Search. If a user has an eligible Microsoft 365 Copilot license, they can access Copilot Search from the
-Search
-module in the Microsoft 365 Copilot app. Users without an eligible Microsoft 365 Copilot license receive the Microsoft Search experience when they select the
+You don't need to take any action to set up Microsoft Copilot Search. If a user has an eligible Microsoft Copilot license, they can access Copilot Search from the
+Search
+module in the Microsoft Copilot app. Users without an eligible Microsoft Copilot license receive the Microsoft Search experience when they select the
 Search
 module in the Microsoft 365 app.
 Configure Copilot Search for your organization
@@ -211,7 +211,7 @@ Don't use the same URL in different bookmarks. You get an error if you try to import a bookmark with a URL used in an existing one. This rule also applies to duplicate URLs in other types of answers.
 When updating existing bookmarks, use the bookmark ID column. You can update any other property of an existing bookmark, such as keyword or description, but you should make sure the bookmark ID is in the appropriate column of the import file. If the bookmark ID is present, it isn't treated as a new addition and isn't process
```

---

### 11. Secure and Govern Copilot blueprint

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.2: Control 1.2: SharePoint Oversharing Detection and Remediation (DSPM for AI)
  - File: `controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -19,11 +19,11 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Secure and govern Microsoft 365 Copilot: Foundational deployment guidance
+Secure and govern Microsoft Copilot: Foundational deployment guidance
 Feedback
 Summarize this article for me
-Microsoft 365 Copilot can accelerate how people find information, summarize content, and get work done by grounding responses in the data users already have permission to access. To realize that value confidently, organizations require a foundation that is both secure and well-governed, with robust safeguards in place, including measures to protect interactions when using Copilot and meeting AI regulatory standards.
-How this blueprint can help you secure and govern Microsoft 365 Copilot
+Microsoft Copilot can accelerate how people find information, summarize content, and get work done by grounding responses in the data users already have permission to access. To realize that value confidently, organizations require a foundation that is both secure and well-governed, with robust safeguards in place, including measures to protect interactions when using Copilot and meeting AI regulatory standards.
+How this blueprint can help you secure and govern Microsoft Copilot
 This deployment blueprint outlines the essential steps for establishing a secure and governed foundation for Copilot by remediating oversharing, implementing reliable guardrails, and fulfilling AI-related regulatory obligations, delivering a straightforward, approachable path to help every organization get started with confidence.
 This blueprint is organized into three pillars:
 Remediate oversharing
@@ -31,7 +31,7 @@ Meet regulations
 https://aka.ms/Copilot/SecureGovernBlueprintPDF
 For a more detailed walkthrough of these steps, see
-Configure a secure and governed foundation for Microsoft 365 Copilot
+Configure a secure and governed foundation for Microsoft Copilot
 .
 What the blueprint covers
 The blueprint 
```

---

### 12. Configure secure and governed Copilot foundation

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -19,17 +19,17 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Configure a secure and governed foundation for Microsoft 365 Copilot
+Configure a secure and governed foundation for Microsoft Copilot
 Feedback
 Summarize this article for me
-Applies to: Microsoft 365 Copilot, Microsoft Purview, and SharePoint Advanced Management
-Microsoft 365 Copilot
+Applies to: Microsoft Copilot, Microsoft Purview, and SharePoint Advanced Management
+Microsoft Copilot
 uses Work IQ to enhance responses to user prompts using data that the user already has permission to access. When your organization's data is well governed, current, and appropriately shared, Copilot can deliver accurate, relevant, and secure responses.
-This article walks through the steps of preparing, securing, and managing Microsoft 365 Copilot using the process described in the
+This article walks through the steps of preparing, securing, and managing Microsoft Copilot using the process described in the
 Foundational deployment blueprint
 .
 By following these steps, you can help Copilot deliver accurate and relevant results while supporting your organization's security, compliance, and regulatory requirements.
-This guidance is intended for IT administrators and security administrators who are either preparing their organization for Microsoft 365 Copilot or making necessary adjustments to security and governance controls after Copilot is enabled.
+This guidance is intended for IT administrators and security administrators who are either preparing their organization for Microsoft Copilot or making necessary adjustments to security and governance controls after Copilot is enabled.
 What this article helps you achieve
 By completing the steps in this article, you can:
 Establish guardrails to ensure that users have appropriate access to SharePoint, OneDrive, and Exchange, and that Copilot only references accurate, up-to-date information in line with your organization'
```

---

### 13. Connect to xAI models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`

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
--- +++ @@ -49,9 +49,9 @@ and conduct their own evaluations before choosing Grok-4.1 Fast (Non-Reasoning).
 Before you begin
 Before users in your organization can use SpaceXAI, they need to be assigned a
-Microsoft 365 Copilot license
+Microsoft Copilot license
 .
-Connect to SpaceXAI in the Microsoft 365 Admin Center
+Connect to SpaceXAI in the Microsoft 365 admin center
 Before your organization can connect to SpaceXAI models, you must allow access in the Microsoft 365 admin center.
 You have to be a member of the Global administrator role to perform this task. For more information, see
 About admin roles
@@ -87,7 +87,7 @@ Save
 .
 Note
-You can restrict user access to AI independent providers by assigning permissions to specific users or Microsoft Entra ID security groups in the Microsoft 365 admin center. These assignments are applied at the provider level and enforced across Microsoft 365 Copilot and Copilot Studio experiences. When access is limited by user or group membership, only the assigned users can use Copilot features or agents that rely on that AI provider. Review existing user or group assignments and update policies or configurations as needed. For more information on user and security group access, see
+You can restrict user access to AI independent providers by assigning permissions to specific users or Microsoft Entra ID security groups in the Microsoft 365 admin center. These assignments are applied at the provider level and enforced across Microsoft Copilot and Copilot Studio experiences. When access is limited by user or group membership, only the assigned users can use Copilot features or agents that rely on that AI provider. Review existing user or group assignments and update policies or configurations as needed. For more information on user and security group access, see
 Assign AI provider access to users and groups
 . For more information on creating security groups, see
 Create a security group

```

---

### 14. Anthropic as a Microsoft subprocessor

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Section:** Copilot Administration
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`

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
--- +++ @@ -22,8 +22,10 @@ Anthropic models in Microsoft Online Services
 Feedback
 Summarize this article for me
+Note
+Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat. There are no changes to security, compliance, and privacy for organizations.
 Microsoft is introducing a new offering with Anthropic AI models as part of Microsoft Online Services, delivering enterprise-grade commitments and safeguards to ensure secure and responsible use of Anthropic models within your organization.
-To enable this change, Anthropic has onboarded as a Microsoft subprocessor. This change simplifies the experience and strengthens compliance and security under Microsoft's enterprise framework. The Microsoft Customer Copyright Commitment (CCC) applies to Anthropic models used within products covered by the CCC, including Microsoft 365 Copilot and Copilot Studio.
+To enable this change, Anthropic has onboarded as a Microsoft subprocessor. This change simplifies the experience and strengthens compliance and security under Microsoft's enterprise framework. The Microsoft Customer Copyright Commitment (CCC) applies to Anthropic models used within products covered by the CCC, including Microsoft Copilot and Copilot Studio.
 As a subprocessor, Anthropic operates with Microsoft oversight through contractual safeguards and appropriate technical and organizational measures. Unless models are labeled "Preview models with Data Retention," the
 Microsoft Product Terms
 and
@@ -36,9 +38,9 @@ . To see a list of Microsoft subprocessors, see
 Service Trust Portal
 .
-Microsoft enables Anthropic models on by default for most customers in commercial cloud (excluding EU/EFTA and UK). This update gives users in your organization the ability to use multiple AI models in their Microsoft offerings, such as in Microsoft 365 Copilot, Researcher, Copilot Studio, Power Platform, and Copilot in Microsoft 365 apps. This affirms Microsoft's com
```

---

### 15. Manage Copilot Pages and Notebooks

**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-admin-configuration?view=o365-worldwide
**Section:** Copilot Pages and Notebooks
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.11: Control 2.11: Copilot Pages Security and Sharing Controls
  - File: `controls/pillar-2-security/2.11-copilot-pages-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -39,7 +39,7 @@ Enabled
 Code previews in Copilot Chat and Copilot Pages
 Cloud Policy:
-Enable code previews for AI-generated content in Microsoft 365 Copilot Chat and Copilot Pages
+Enable code previews for AI-generated content in Microsoft Copilot Chat and Copilot Pages
 Enabled
 Tip
 Quick reference scenarios
@@ -55,7 +55,7 @@ : Disable both policies
 Block code previews only
 : Disable
-Enable code previews for AI-generated content in Microsoft 365 Copilot Chat and Copilot Pages
+Enable code previews for AI-generated content in Microsoft Copilot Chat and Copilot Pages
 ; leave
 Create and view Copilot Pages and Copilot Notebooks
 enabled
@@ -84,15 +84,15 @@ See
 storage
 for the full explanation of the shared container, including naming and lifecycle.
-To share Copilot Pages as interactive components (instead of just hyperlinks) in Teams, Outlook, Whiteboard, OneNote, or the Loop application, Loop components must be enabled. Without Loop components enabled in the Microsoft 365 ecosystem, Copilot Pages are only interactive within the Microsoft 365 Copilot app and supported chat experiences. For details on enabling Loop components in the Microsoft 365 ecosystem, see
+To share Copilot Pages as interactive components (instead of just hyperlinks) in Teams, Outlook, Whiteboard, OneNote, or the Loop application, Loop components must be enabled. Without Loop components enabled in the Microsoft 365 ecosystem, Copilot Pages are only interactive within the Microsoft Copilot app and supported chat experiences. For details on enabling Loop components in the Microsoft 365 ecosystem, see
 Loop admin policies
 .
 User experience when Copilot Pages and Copilot Notebooks are disabled
-When creation is disabled, users are unable to create new Copilot Pages or Notebooks. The Pages module is visible in the Microsoft 365 Copilot app, but the Notebooks module is hidden, preventing users from accessing existing Notebooks through the Copilot App. If Loop My workspace is still
```

---

### 16. Copilot Pages and Notebooks compliance summary

**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-compliance-summary?view=o365-worldwide
**Section:** Copilot Pages and Notebooks
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.11: Control 2.11: Copilot Pages Security and Sharing Controls
  - File: `controls/pillar-2-security/2.11-copilot-pages-security.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.11/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.11/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.11/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.11/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -34,7 +34,7 @@ â  Supported
 Conditional Access
-â App-level only (entire Microsoft 365 Copilot app)
+â App-level only (entire Microsoft Copilot app)
 Information Barriers
 â Not supported
 Customer Lockbox
@@ -85,7 +85,7 @@ Device Management Support
 is available for the Microsoft 365 app and Teams app on iOS and Android.
 Conditional Access
-: Only applies at the app level. Because Copilot Pages and Copilot Notebooks are features of the Microsoft 365 Copilot app,
+: Only applies at the app level. Because Copilot Pages and Copilot Notebooks are features of the Microsoft Copilot app,
 Conditional Access
 applies to the entire app at m365.cloud.microsoft. Use
 admin policies

```

---

### 17. What's new in Copilot Cowork

**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/whats-new
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
--- +++ @@ -43,7 +43,7 @@ Set up tasks that run when something happens, such as when you receive a matching email or a Teams message (including when you're
 @mentioned)
 . Describe what to watch for in your message, and Cowork proposes the automation for you to review and confirm. Event-driven tasks appear alongside scheduled prompts on the
-Scheduled
+Automations
 page.
 Set up event-driven tasks
 June 2026 (general availability)

```

---

### 18. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
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
--- +++ @@ -65,7 +65,7 @@ As an admin, you can turn off the Anthropic model family in the
 Microsoft 365 admin center
 under Copilot settings.
-Microsoft might deploy other AI models for Microsoft 365 Copilot to use that are hosted and operated by Microsoft. These models are governed by the same contractual and data protection commitments already in place, including that no data leaves Microsoft. For more information about the use of Azure-hosted GPT models in Microsoft 365 Copilot, visit
+Microsoft might deploy other AI models for Microsoft Copilot to use that are hosted and operated by Microsoft. These models are governed by the same contractual and data protection commitments already in place, including that no data leaves Microsoft. For more information about the use of Azure-hosted GPT models in Microsoft Copilot, visit
 Understanding AI functionality and models in Microsoft Online Services
 , or for information about the use of Anthropic models, visit
 Anthropic as a subprocessor for Microsoft Online Services
@@ -109,29 +109,29 @@ âAutomated task activity is recorded in the unified audit log alongside other Cowork activity, and Microsoft Purview data security and compliance policies apply.
 Security and compliance
 Microsoft Purview is available to secure and govern Cowork. Learn more in
-Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot Cowork
+Use Microsoft Purview to manage data security & compliance for Microsoft Copilot Cowork
 .
 Data residency
 Copilot Cowork follows the same data residency model as Copilot. For more details, see
-Data residency for Microsoft 365 Copilot
+Data residency for Microsoft Copilot
 .
 How Cowork processes your data during a task
 When Cowork runs a task, it processes your files in a temporary, isolated environment inside the
 Microsoft 365 service boundary
 . The process uses those files only for the length of the task. This temporary environment is removed when the task finishesâit does
```

---

### 19. Copilot Cowork available models

**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-models
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
--- +++ @@ -49,25 +49,26 @@ Hosted in Azure AI Foundry.
 GPT 5.6 Sol
 Intelligent and efficient for hard workâ.
-n/a
+Provided by OpenAI as a subprocessor. More information:
+OpenAI as a subprocessor in Microsoft Online Services
 GPT 5.6 Terra
 Balanced effort for common tasksâ.
-n/a
+Provided by OpenAI as a subprocessor. More information:
+OpenAI as a subprocessor in Microsoft Online Services
 Opus 5
 For complex, high stakes work.
-n/a
+More information:
+Anthropic subprocessor
 Claude Sonnet 5
 For everyday tasks and fast responses such as drafting, quick lookups, and day-to-day work.
-Use when you want a shorter response cycle for common tasks. Learn more about data handling in
+Use when you want a shorter response cycle for common tasks. More information:
 Anthropic subprocessor
-.
 Claude Fable 5 (Preview)
 For your toughest, most demanding challenges.
-In preview and off by default. An admin must turn it on in the Microsoft 365 admin center under Copilot settings before it appears in your picker. Requires data retention. When you select Fable 5, your prompts and responses are retained by the model provider, and Cowork shows a banner while it's selected. Learn more about data handling in
+In preview and off by default. An admin must turn it on in the Microsoft 365 admin center under Copilot settings before it appears in your picker. Requires data retention. When you select Fable 5, your prompts and responses are retained by the model provider, and Cowork shows a banner while it's selected. More information:
 Data retention
 and
 Anthropic subprocessor
-.
 How model choice affects responses
 Changing the model can affect response speed, response depth, and output style. Some models are optimized for faster drafting, while others spend more time on reasoning and review.
 Cowork shows a model badge in the conversation so you can see which model produced a response.
@@ -89,7 +90,7 @@ Manage preview AI models in Microsoft Online Services
 .
 Models hosted by Mi
```

---

### 20. Manage Copilot Cowork plugins

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -22,7 +22,7 @@ Manage plugins for Copilot Cowork
 Feedback
 Summarize this article for me
-Microsoft 365 Copilot Cowork supports plugins that add skills and connectors to extend what Cowork can do. As an IT administrator, you control which plugins are available in your organization, how they're deployed, and who can use them. This article covers plugin governance from an admin perspective.
+Microsoft Copilot Cowork supports plugins that add skills and connectors to extend what Cowork can do. As an IT administrator, you control which plugins are available in your organization, how they're deployed, and who can use them. This article covers plugin governance from an admin perspective.
 Learn how users browse and use plugins in
 Use plugins with Cowork
 and
@@ -84,7 +84,7 @@ Tip
 Cowork provides several plugins for Microsoft applications, including Dynamics 365 Customer Service, Dynamics 365 ERP, Dynamics 365 Sales, and Fabric IQ. You can find these plugins in the Microsoft 365 App Store and deploy them like any other plugin.
 Learn more in
-Deploy agents in Microsoft 365 Copilot
+Deploy agents in Microsoft Copilot
 .
 Control plugin availability
 After you deploy a plugin, you can configure who can see it and how users interact with it.
@@ -160,7 +160,7 @@ Copilot activities
 in Microsoft Purview. Audit Standard provides these logs at no extra cost.
 Learn more in
-Audit log activities for Microsoft 365 Copilot
+Audit log activities for Microsoft Copilot
 .
 Plugin support for MCP servers
 Cowork supports plugins with MCP servers and/or skills, packaged as Teams apps. Cowork performs dynamic tool discoveryâwhen a plugin declares an MCP server, Cowork calls initialize and tools/list at runtime to discover available tools automatically. Plugins declare their MCP servers and skills in manifest.json:

```

---

### 21. Managing AI experiences enabled by usage-based billing

**URL:** https://learn.microsoft.com/microsoft-365/copilot/discovery-setting-ai-experiences
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
--- +++ @@ -54,7 +54,7 @@ AI experiences enabled by usage-based billing
 .
 In the side panel, select the checkbox
-Allow users to discover and use AI experiences enabled by usage-based billing in Microsoft 365 Copilot
+Allow users to discover and use AI experiences enabled by usage-based billing in Microsoft Copilot
 .
 Related articles
 Managing AI experiences enabled by usage-based billing

```

---

### 22. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -34,7 +34,7 @@ Note
 If you are looking for information on other usage-based billing products, use the following articles:
 For Copilot Chat, SharePoint Agents, or Microsoft Copilot Retrieval API (Preview), see
-Microsoft 365 Copilot pay-as-you-go service overview
+Microsoft Copilot pay-as-you-go service overview
 .
 For Copilot Studio, see
 Copilot Studio pay-as-you-go
@@ -341,7 +341,7 @@ Ensure the setting that allows users to discover and use usage-based services is turned on
 more details
 .
-Understanding Azure Consumption Commitment (MACC) in Microsoft 365 Copilot
+Understanding Azure Consumption Commitment (MACC) in Microsoft Copilot
 If your organization has an Azure Consumption Commitment (MACC), you can apply those committed funds toward eligible Copilot consumption. This approach helps you maximize existing investments while adopting AI-powered capabilities.
 To ensure correct application of MACC, administrators must configure billing in the Microsoft 365 admin center by using an Azure subscription associated with the correct billing account. MACC benefits apply only when the selected subscription links to a billing account that includes the commitment. If you use a different billing account or subscription, you still pay for consumption, but it might not count toward your MACC. Therefore, proper setup is critical.
 Administrators should:
@@ -349,7 +349,7 @@ Select an Azure subscription associated with that billing account during setup.
 Ensure the correct billing relationship is established before enabling consumption-based services.
 When you configure it correctly, eligible Copilot usage automatically applies against your MACC. You don't need to take any extra action during ongoing usage.
-This model allows organizations to seamlessly extend their Azure investment into Microsoft 365 Copilot scenarios while maintaining control over billing, governance, and cost visibility.
+This model allows organizations to seamlessly extend their Azure inve
```

---

### 23. Manage plugins for Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide
**Section:** Copilot Extensibility
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 2.17: Control 2.17: Cross-Tenant Agent Federation (MCP and Entra Agent ID)
  - File: `controls/pillar-2-security/2.17-cross-tenant-agent-federation.md`
- Control 4.1: Control 4.1: Copilot Admin Settings and Feature Management
  - File: `controls/pillar-4-operations/4.1-admin-settings-feature-management.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.17/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.17/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.17/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.17/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -24,15 +24,15 @@ Summarize this article for me
 Important
 This article is intended for IT administrators.
-The capability is enabled by default in all Microsoft 365 Copilot licensed tenants.
-Microsoft 365 Copilot combines the power of large language models with your data and apps in Microsoft 365. It captures natural language commands to produce content and analyze data. It enables access to and use of other apps, such as Jira,
+The capability is enabled by default in all Microsoft Copilot licensed tenants.
+Microsoft Copilot combines the power of large language models with your data and apps in Microsoft 365. It captures natural language commands to produce content and analyze data. It enables access to and use of other apps, such as Jira,
 Dynamics 365
 , or Bing Web Search.
 You can manage agents for Copilot by using the
 Microsoft 365 admin center
 . You can enable, disable, assign, block, or remove agents for your organization, and manage Copilot capabilities.
 Note
-Researcher and Analyst are first-party Microsoft experiences built on the same foundation as Microsoft 365 Copilot, operating entirely within the Microsoft 365 commercial data processing boundary. These tools inherit all existing security, privacy, and compliance commitments that apply across the suite of Microsoft 365 products. These tools are available in Microsoft 365 Copilot Chat under
+Researcher and Analyst are first-party Microsoft experiences built on the same foundation as Microsoft Copilot, operating entirely within the Microsoft 365 commercial data processing boundary. These tools inherit all existing security, privacy, and compliance commitments that apply across the suite of Microsoft 365 products. These tools are available in Microsoft Copilot Chat under
 Tools
 and can be invoked by the user anytime. While Researcher and Analyst coexist with agents and abide by all the agent-related governance capabilities, Researcher and Analyst are part of the core Copilot chat experie
```

---

### 24. Copilot Tuning admin guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-admin-guide
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.16: Control 1.16: Copilot Tuning Governance
  - File: `controls/pillar-1-readiness/1.16-copilot-tuning-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.16/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.16/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.16/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -19,19 +19,19 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Microsoft 365 Copilot Tuning admin guide (early access preview)
+Microsoft Copilot Tuning admin guide (early access preview)
 Feedback
 Summarize this article for me
-Microsoft 365 Copilot Tuning (early access preview) is an AI customization capability that enables organizations to create task-specific Copilot agents by tuning large language models (LLMs) with their own organizational data. AI admins manage Copilot Tuning through the Copilot control system in the Microsoft 365 admin center. Copilot Tuning provides multiple layers of control to balance innovation with governance.
-This article describes how administrators manage Microsoft 365 Copilot Tuning, including role requirements, availability controls, agent lifecycle management, and data protection considerations.
+Microsoft Copilot Tuning (early access preview) is an AI customization capability that enables organizations to create task-specific Copilot agents by tuning large language models (LLMs) with their own organizational data. AI admins manage Copilot Tuning through the Copilot control system in the Microsoft 365 admin center. Copilot Tuning provides multiple layers of control to balance innovation with governance.
+This article describes how administrators manage Microsoft Copilot Tuning, including role requirements, availability controls, agent lifecycle management, and data protection considerations.
 Important
-Microsoft 365 Copilot Tuning is currently available to a limited set of customers through early access programs. Access through
+Microsoft Copilot Tuning is currently available to a limited set of customers through early access programs. Access through
 Frontier
 is planned for April 2026. Features and requirements are subject to change.
 Tuning availability settings
 Admins can control who can access Copilot Tuning at the tenant level. Three availability options are supported:
 Enab
```

---

### 25. Agent management in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 4.5: Control 4.5: Copilot Usage Analytics and Adoption Reporting
  - File: `controls/pillar-4-operations/4.5-usage-analytics.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.5/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -55,9 +55,9 @@ .
 Prerequisites for agent management
 Before you can manage agents in the Microsoft 365 admin center, confirm the following requirements are met:
-Your organization has the required subscription and licenses for either Microsoft 365, Microsoft 365 Copilot, or Microsoft Agent 365.
+Your organization has the required subscription and licenses for either Microsoft 365, Microsoft Copilot, or Microsoft Agent 365.
 Users at your organization that create, publish, or use agents have the appropriate licenses assigned.
-Youâre assigned an administrator role that includes permissions to manage settings for Microsoft 365, Microsoft 365 Copilot, or Microsoft Agent 365 in the Microsoft 365 admin center.
+Youâre assigned an administrator role that includes permissions to manage settings for Microsoft 365, Microsoft Copilot, or Microsoft Agent 365 in the Microsoft 365 admin center.
 For more information, see the following resources:
 Licensing for agent management
 Agent management roles and permissions
@@ -65,14 +65,14 @@ The following licensing options include agents that can be managed in Microsoft 365 admin center:
 Microsoft 365 plans
 Microsoft 365 (All Suites) includes Copilot Chat. Copilot Chat provides web data agents.
-Microsoft 365 (E7) includes Microsoft 365 E5, Microsoft 365 Copilot, Microsoft Agent 365, and Microsoft Entra Suite.
-Microsoft 365 Copilot
+Microsoft 365 (E7) includes Microsoft 365 E5, Microsoft Copilot, Microsoft Agent 365, and Microsoft Entra Suite.
+Microsoft Copilot
 This license can be added to your Microsoft 365 license (E3, E5). It's included with your Microsoft 365 license (E7). This option provides both web and work data agents.
 Microsoft Agent 365
 Microsoft Agent 365 is also included in Microsoft 365 (E7).
 Note
-To compare Copilot Chat and Microsoft 365 Copilot, see
-License options for Microsoft 365 Copilot
+To compare Copilot Chat and Microsoft Copilot, see
+License options for Microsoft Copilot
 .
 For more 
```

---

### 26. Agent registry in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -102,7 +102,7 @@ refers to agents that include files that were uploaded by the agent maker or developer as knowledge sources.
 Fine-tuned models
 indicates that the agent was created using
-Microsoft 365 Copilot Tuning
+Microsoft Copilot Tuning
 , allowing the agent to tune LLMs with their own organization data.
 Tip
 If you don't see the agents that you expect to see in the agent registry list, check to make sure you don't have an existing filter set.
@@ -243,7 +243,7 @@ Medium
 Microsoft 365 admin center
 Errors or failures in agent conversation or tool execution
-Use developer mode in Microsoft 365 Copilot to test and debug agents
+Use developer mode in Microsoft Copilot to test and debug agents
 Compliance/retention gap
 Medium
 Microsoft Purview
@@ -366,7 +366,7 @@ >
 Channels
 . Select the channel you use to publish, such as
-Teams and Microsoft 365 Copilot
+Teams and Microsoft Copilot
 . Select
 Availability options
 >
@@ -432,18 +432,18 @@ Manage pinned agents
 As an administrator, you can choose to pin a deployed agent to the
 Agents
-list within Microsoft 365 Copilot. By pinning agents in Microsoft 365 Copilot, you can ensure that those agents are visible and accessible for all members of your organization, or only specific users or groups. You can choose to pin and unpin agents. Also, you can rank the list of pinned agents.
-Microsoft 365 Copilot includes agents pinned by Microsoft, admins, and users. Microsoft pinned agents are specific agents that are pinned by default for all users. You can pin agents for your organization within Microsoft 365 admin center. In addition, individual users can pin agents in their own Microsoft 365 Copilot Chat or Microsoft 365 Copilot experience.
+list within Microsoft Copilot. By pinning agents in Microsoft Copilot, you can ensure that those agents are visible and accessible for all members of your organization, or only specific users or groups. You can choose to pin and unpin agents. Also, you can rank the li
```

---

### 27. Agent settings in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide
**Section:** Agent Governance
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 2.13: Control 2.13: Plugin and Graph Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.13/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -69,7 +69,7 @@ Reassign ownerless agents created with Agent Builder to manager
 Agents become ownerless when their original creator leaves the organization. Administrators must currently identify and transfer ownership manually, which can result in lifecycle governance gaps.
 Note
-This rule only supports agents created by using Microsoft 365 Copilot Agent Builder.
+This rule only supports agents created by using Microsoft Copilot Agent Builder.
 By using the
 Reassign Ownerless Agents
 rule, you can:
@@ -105,7 +105,7 @@ Specific users
 - Restrict broad sharing permissions to designated groups.
 Sharing control only applies to agents built with
-Microsoft 365 Copilot Agent Builder
+Microsoft Copilot Agent Builder
 .
 User access
 Use

```

---

### 28. Restricted SharePoint Search

**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-sharepoint-search
**Section:** SharePoint Administration
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`
- Control 2.5: Control 2.5: Data Minimization and Grounding Scope
  - File: `controls/pillar-2-security/2.5-data-minimization-grounding-scope.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.3/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.3/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.5/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -26,7 +26,7 @@ Restricted SharePoint Search is retiring. Starting July 31, 2026, new enablement is blocked. Use comprehensive data controls such as
 Restricted Content Discovery
 (RCD) for content discoverability.
-Restricted SharePoint Search is designed for customers of Microsoft 365 Copilot chat and agentic experiences. It's a short-term solution that gives your organization's administrators time to review and audit site and file permissions. It's not intended or scalable for long-term use. Comprehensive data security solutions are available, including
+Restricted SharePoint Search is designed for customers of Microsoft Copilot Chat and agentic experiences. It's a short-term solution that gives your organization's administrators time to review and audit site and file permissions. It's not intended or scalable for long-term use. Comprehensive data security solutions are available, including
 SharePoint Advanced Management
 and
 Microsoft Purview

```

---

### 29. SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/sharepoint/advanced-management
**Section:** SharePoint Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`
- Control 2.5: Control 2.5: Data Minimization and Grounding Scope
  - File: `controls/pillar-2-security/2.5-data-minimization-grounding-scope.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.5/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -30,7 +30,7 @@ Prevent oversharing
 .
 SAM capabilities are helpful as organizations
-prepare for Microsoft 365 Copilot and agents
+prepare for Microsoft Copilot and agents
 .
 Video: SharePoint Advanced Management overview
 Watch the following video to get an overview of SharePoint Advanced Management:
@@ -74,7 +74,7 @@ Get insights on agents in SharePoint
 : Use this report to identify recently created agents across SharePoint and OneDrive sites, and identify sites with the highest number of agents created.
 Use restricted content discovery (RCD)
-: Prevent high-risk SharePoint sites and files from surfacing in Microsoft 365 Copilot and Agentic experiences.
+: Prevent high-risk SharePoint sites and files from surfacing in Microsoft Copilot and Agentic experiences.
 Use data access governance (DAG) reports for SharePoint and OneDrive sites
 : Identify sites that might contain overshared or sensitive content. AI insights can be generated from DAG reports to highlight access risk patterns and recommend next steps. You can also initiate site access reviews from a DAG report. DAG reports include:
 Permission state reports for sites, OneDrive sites, and files
@@ -107,9 +107,9 @@ .
 Related articles
 SharePoint Admin Agent
-Get ready for Microsoft 365 Copilot and Agents with SharePoint Advanced Management
-Configure a secure and governed foundation for Microsoft 365 Copilot
-SharePoint Advanced Management features in Microsoft 365 Copilot licenses
+Get ready for Microsoft Copilot and Agents with SharePoint Advanced Management
+Configure a secure and governed foundation for Microsoft Copilot
+SharePoint Advanced Management features in Microsoft Copilot licenses
 Feedback
 Was this page helpful?
 Yes

```

---

### 30. Get ready for Copilot with SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`

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
--- +++ @@ -19,10 +19,10 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Get ready for Microsoft 365 Copilot and agents with SharePoint Advanced Management
+Get ready for Microsoft Copilot and agents with SharePoint Advanced Management
 Feedback
 Summarize this article for me
-Microsoft 365 Copilot and agents work best for your organization when your content is up to date and well governed. Copilot and agents retrieve data from Microsoft Graph and respect existing permissions, sharing settings, and policies.
+Microsoft Copilot and agents work best for your organization when your content is up to date and well governed. Copilot and agents retrieve data from Microsoft Graph and respect existing permissions, sharing settings, and policies.
 This article describes how to prepare your environment for Copilot and agent usage by using capabilities in
 SharePoint Advanced Management
 .
@@ -244,7 +244,7 @@ responds to your questions by gathering the relevant data and reports, offering analysis and recommendations, and suggesting other prompts. Ask a question, such as "Show me how my content is distributed across my tenant," and get useful information with suggested prompts and next steps.
 Open the SharePoint Admin Agent
 Take one of the following steps:
-In the Microsoft 365 Copilot app, expand
+In the Microsoft Copilot app, expand
 Agents
 , and search for
 SharePoint Admin Agent

```

---

### 31. SharePoint site lifecycle management

**URL:** https://learn.microsoft.com/en-us/sharepoint/site-lifecycle-management
**Section:** SharePoint Administration
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -78,6 +78,25 @@ For more information, see
 Request recurring site attestations for SharePoint sites
 .
+Overlapping policies of same policy type
+When more than one policy of the same policy type includes the same site, SharePoint helps reduce duplicate notifications by using stored site-level policy history.
+If a notification was sent within the last 30 days from any policy of that type, and the site remains uncertified, no further notifications are sent and the policy execution report shows the site's status as "Notified by another policy."
+For example, if a site is covered by two different inactive site policies and receives a notification email from the first policy, the second policy doesn't send additional notifications within the next 30 days if the site remains uncertified.
+We recommend that policies of the same type don't have overlapping scopes. If sites fall under multiple policies of the same type, notification schedules and enforcement actions can become difficult to predict.
+Overlapping policies of different types
+Policies of different types operate independently for notification purposes. Notification history is tracked separately for each policy type.
+For example, if a site falls within the scope of both a Site Ownership policy and an Inactive site policy, site owners may receive notifications from both policies when the respective policy conditions are met.
+Enforcement actions are evaluated independently by each policy. If a policy applies an enforcement action that changes the site's state, the site may no longer qualify for processing by other policies:
+If a policy places the site in a read-only (locked) state, the site is no longer included in the scope of other policies.
+If a policy archives the site, the site reaches a terminal state and is no longer considered for enforcement by other policies.
+When multiple policy types target the same site, the enforcement action from the policy whose conditions are satisfied first is ap
```

---

### 32. Restricted Content Discovery

**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`
- Control 1.2: Control 1.2: SharePoint Oversharing Detection and Remediation (DSPM for AI)
  - File: `controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md`
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`
- Control 2.5: Control 2.5: Data Minimization and Grounding Scope
  - File: `controls/pillar-2-security/2.5-data-minimization-grounding-scope.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.2/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.3/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.3/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.3/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.4/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.4/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.4/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.5/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -22,7 +22,7 @@ Restrict discovery of SharePoint sites and content
 Feedback
 Summarize this article for me
-Organizations preparing for Microsoft 365 Copilot often need time to review SharePoint sites, validate permissions, and implement governance controls before making content broadly discoverable. Restricted Content Discovery (RCD) helps you limit discovery of content from specific SharePoint sites, including recently interacted files, in organization-wide search results and Microsoft 365 Copilot responses while those reviews are taking place.
+Organizations preparing for Microsoft Copilot often need time to review SharePoint sites, validate permissions, and implement governance controls before making content broadly discoverable. Restricted Content Discovery (RCD) helps you limit discovery of content from specific SharePoint sites, including recently interacted files, in organization-wide search results and Microsoft Copilot responses while those reviews are taking place.
 RCD also removes AI-powered entry points from these SharePoint sites. Users don't see entry points such as the Copilot button, AI actions menus (including creating agents), or
 Create pages with AI
 . This restriction helps reduce the likelihood of accidental discovery of content while permissions and governance controls are being evaluated.
@@ -33,13 +33,13 @@ You can only apply this feature to SharePoint sites. It isn't supported for OneDrive sites.
 Restricted Content Discovery doesn't affect searches that originate from site context or other intelligent experiences such as Microsoft 365 Feed and Recommendations.
 Caution
-Use Restricted Content Discovery selectively. Excessive use can reduce the amount of content available to organization-wide search and Microsoft 365 Copilot experiences, which can affect the completeness and relevance of search results and AI-generated responses.
+Use Restricted Content Discovery selectively. Excessive use can reduce the amount of content avail
```

---

### 33. SharePoint Admin Agent (Content Governance Agent)

**URL:** https://learn.microsoft.com/en-us/sharepoint/content-governance-agent
**Section:** SharePoint Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -25,7 +25,7 @@ The SharePoint Admin Agent is an AI-powered governance experience that helps your administrators assess and remediate content-related risks across your SharePoint and OneDrive environments. Instead of running reports manually, use natural language queries to investigate tenant-level conditions and take guided remediation actions.
 Video: Overview of the SharePoint Admin Agent
 The following video provides an overview of the SharePoint Admin Agent:
-Microsoft 365 Copilot
+Microsoft Copilot
 (Copilot) and
 Agents
 work best when SharePoint and OneDrive content is well-governed, relevant, and securely accessible. The SharePoint Admin Agent helps by enabling your administrators to move quickly from assessment to action using a conversational interface. It analyzes data drawn from SharePoint and
@@ -89,11 +89,11 @@ role assigned in Microsoft Entra ID.
 Open the SharePoint Admin Agent
 Open the SharePoint Admin Agent by using any of the following methods:
-Open the SharePoint Admin Agent in the Microsoft 365 Copilot app
+Open the SharePoint Admin Agent in the Microsoft Copilot app
 Access content governance skills for Copilot in the SharePoint admin center
 Open the SharePoint Admin Agent in Microsoft Teams
-Open the SharePoint Admin Agent in Microsoft 365 Copilot
-In the Microsoft 365 Copilot app, expand
+Open the SharePoint Admin Agent in Microsoft Copilot
+In the Microsoft Copilot app, expand
 Agents
 , and search for the SharePoint Admin Agent.
 Use the agent in the Copilot app.

```

---

## HIGH: Control Review Recommended

### 1. Manage Copilot Search

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage
**Section:** Copilot Administration
**Classification:** HIGH (Policy language)

**What Changed:**
```diff
--- +++ @@ -19,19 +19,19 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Manage Microsoft 365 Copilot Search
+Manage Microsoft Copilot Search
 Feedback
 Summarize this article for me
-No action is required by admins to set up Microsoft 365 Copilot Search. If a user has a Microsoft 365 Copilot license, they can access Copilot Search from the
+No action is required by admins to set up Microsoft Copilot Search. If a user has a Microsoft Copilot license, they can access Copilot Search from the
 Search
-module in the Microsoft 365 Copilot app across web, desktop, and mobile. Users who don't have the Microsoft 365 Copilot app will receive the Microsoft Search experience when clicking the
+module in the Microsoft Copilot app across web, desktop, and mobile. Users who don't have the Microsoft Copilot app will receive the Microsoft Search experience when clicking the
 Search
 module in the Microsoft 365 app.
 Learn more about
-setting up Microsoft 365 Copilot
+setting up Microsoft Copilot
 for your users.
 For more details on how to manage, customize, and optimize Copilot Search across your organization, learn about the
-Microsoft 365 Copilot Search admin experience
+Microsoft Copilot Search admin experience
 .
 Copilot Search and third-party systems
 Copilot Search can access data in third-party systems as well as Microsoft 365 apps and other systems in the Microsoft Graph. This is achieved through Microsoft 365 Copilot connectors, which allow organizations to ingest data from external platforms like Salesforce, ServiceNow, Confluence, and more.
@@ -39,15 +39,15 @@ Microsoft 365 Copilot connectors
 .
 Privacy and security
-Microsoft 365 Copilot Search adheres to the same data protection, privacy standards, and security configurations as Microsoft 365 Copilot. Learn more about
-data, privacy, and security in Microsoft 365 Copilot
+Microsoft Copilot Search adheres to the same data protection, privacy standards, and security configurations 
```

---

### 2. Assign AI provider access to users and groups

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-ai-provider-user-sec-group-access
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -22,12 +22,14 @@ Assign AI provider access to users and groups
 Feedback
 Summarize this article for me
-Organizations that use third-party AI providers with Microsoft 365 Copilot or Copilot Studio can restrict access to those AI providers by assigning permissions to specific users or Microsoft Entra ID security groups.
+Note
+Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat. There are no changes to security, compliance, and privacy for organizations.
+Organizations that use third-party AI providers with Microsoft Copilot or Copilot Studio can restrict access to those AI providers by assigning permissions to specific users or Microsoft Entra ID security groups.
 AI provider user and group access
 You can assign AI providers to selected users or groups in the Microsoft 365 admin center. For more information, see:
 Anthropic as a subprocessor for Microsoft Online Services
 Connect to SpaceXAI models
-This allows your organization to control which users can access specific AI providers that are enabled for use with Microsoft 365 Copilot experiences, agents, or Copilot Studio.
+This allows your organization to control which users can access specific AI providers that are enabled for use with Microsoft Copilot experiences, agents, or Copilot Studio.
 Administrators can assign access to:
 Individual users
 Microsoft Entra ID security groups
@@ -44,11 +46,11 @@ Copilot Studio
 User and security group access will apply to AI subprocessors and AI independent processors for all current and future third-party model providers.
 Enforcement across Copilot experiences
-Provider-level assignments are enforced across Microsoft 365 Copilot and Copilot Studio experiences. If a user isn't assigned access to an AI provider, they might:
+Provider-level assignments are enforced across Microsoft Copilot and Copilot Studio experiences. If a user isn't assigned access to an AI provider, they might:
 Be unable
```

---

### 3. Copilot Cowork overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -22,7 +22,7 @@ Copilot Cowork overview
 Feedback
 Summarize this article for me
-Microsoft 365 Copilot Cowork can carry out tasks on your behalf. You describe what you need, and Cowork sends emails, schedules meetings, creates documents, posts in Teams, and manages your calendar. You approve each action before it happens.
+Microsoft Copilot Cowork can carry out tasks on your behalf. You describe what you need, and Cowork sends emails, schedules meetings, creates documents, posts in Teams, and manages your calendar. You approve each action before it happens.
 What is Cowork?
 Cowork carries out tasks across your Microsoft 365 environment. Rather than describing what you could do, it does the work.
 Sends emails
@@ -47,11 +47,17 @@ : Runs prompts on a schedule so recurring tasks happen automatically.
 Cowork shows each step in your session, so you can follow along as it works.
 Note
-Cowork is available in two versions. Both versions contain similar features.
-Cowork for work or school accounts
-is generally available. The articles here in the Microsoft 365 Copilot Hub focus on this version.
-Cowork for personal accounts
-is in preview. Learn more in
+Cowork is available for
+personal
+and
+work or school
+accounts with similar features.
+Cowork for work or school accounts is
+generally available
+.
+Cowork for personal accounts is in
+preview
+. Learn more in
 Get started with Cowork
 .
 What can Cowork do for you?
@@ -132,7 +138,7 @@ Cowork helps you stay organized with built-in project and task management.
 Task views
 : Display all of your tasks or filtered views based on task status or use the
-Scheduled
+Automations
 tab to manage your scheduled prompts.
 Data protection and privacy
 Cowork adheres to the data protection policies detailed in
@@ -141,7 +147,7 @@ Get started
 You can use Cowork in your browser at
 m365.cloud.microsoft
-, in the Microsoft 365 Copilot desktop app for Windows and Mac, and in the Microsoft 365 Copilot mobile app for iPhone 
```

---

### 4. Get started with Copilot Cowork

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started
**Section:** Copilot Cowork
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -22,15 +22,15 @@ Get started with Copilot Cowork
 Feedback
 Summarize this article for me
-Microsoft 365 Copilot Cowork allows you to describe what you needâdraft an email, build a spreadsheet, schedule a meetingâand Cowork handles it. This article walks you through your first conversation, from sending a request to reviewing the result.
+Microsoft Copilot Cowork allows you to describe what you needâdraft an email, build a spreadsheet, schedule a meetingâand Cowork handles it. This article walks you through your first conversation, from sending a request to reviewing the result.
 Prerequisites
 Before you begin, make sure you have:
-Microsoft 365 Copilot access
+Microsoft Copilot access
 : An active Microsoft 365 Copilot license assigned to your account.
 A modern browser
 : Microsoft Edge or Google Chrome recommended.
 Cowork available
-: Cowork is enabled in your Microsoft 365 Copilot environment.
+: Cowork is enabled in your Microsoft Copilot environment.
 Usage-based billing
 : Usage-based and Cowork billing has been enabled.
 Cowork can optionally use Anthropic models as a subprocessor. Integration details can be found at
@@ -38,10 +38,10 @@ .
 Cowork works in your browser at
 m365.cloud.microsoft
-, in Outlook and Teams, in the Microsoft 365 Copilot desktop app for Windows and Mac, and in the Microsoft 365 Copilot mobile app for iPhone and Android.
+, in Outlook and Teams, in the Microsoft Copilot desktop app for Windows and Mac, and in the Microsoft Copilot mobile app for iPhone and Android.
 Open Cowork
 Open
-Microsoft 365 Copilot
+Microsoft Copilot
 .
 Select
 Cowork
@@ -49,7 +49,7 @@ When the Cowork homepage loads, you have access to:
 A chat input where you can describe what you need, along with any recent tasks you can pick up where you left off.
 Search: Instantly search and revisit your previous tasks, so your past work is always at your fingertips.
-Scheduled: View, edit, reschedule, and clean up your scheduled tasks without huntin
```

---

### 5. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Section:** Copilot Cowork
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -22,9 +22,9 @@ Copilot Cowork common questions
 Feedback
 Summarize this article for me
-Find answers to common questions about Microsoft 365 Copilot Cowork.
+Find answers to common questions about Microsoft Copilot Cowork.
 What is Cowork?
-Cowork is available in Microsoft 365 Copilot. It carries out tasks on your behalf. For example, it can send emails, schedule meetings, create documents, post in Teams, and handle multi-step tasks across your Microsoft 365 environment.
+Cowork is available in Microsoft Copilot. It carries out tasks on your behalf. For example, it can send emails, schedule meetings, create documents, post in Teams, and handle multi-step tasks across your Microsoft 365 environment.
 What can Cowork do for me?
 Cowork can send emails, schedule meetings, create documents (Word, Excel, PowerPoint, PDF), post in Teams, manage your calendar, prepare daily briefings, search across your organization, conduct deep research, and draft stakeholder communications. You can also schedule prompts to run automatically.
 Get a full breakdown by category in
@@ -96,7 +96,7 @@ How do I start using Cowork?
 Getting started takes just a few steps.
 Open
-Microsoft 365 Copilot
+Microsoft Copilot
 .
 Select
 Cowork
@@ -105,11 +105,11 @@ Send your message. Cowork begins processing your request.
 Does Cowork work on mobile devices?
 Yes. You can access Cowork in the following ways:
-In the Microsoft 365 Copilot mobile app for iPhone and Android
+In the Microsoft Copilot mobile app for iPhone and Android
 In your browser at
 m365.cloud.microsoft
 (desktop)
-In the Microsoft 365 Copilot desktop app for Windows and Mac
+In the Microsoft Copilot desktop app for Windows and Mac
 What file types does Cowork support?
 You can attach a wide variety of files to your sessions. Cowork supports the following categories:
 Word
@@ -306,12 +306,12 @@ from the main navigation. You can switch between two views:
 Recent
 : Shows your tasks in reverse chronological order. You can 
```

---

### 6. Communication compliance for financial services

**URL:** https://learn.microsoft.com/en-us/purview/communication-compliance-channels
**Section:** Communication Compliance
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -67,7 +67,7 @@ You can analyze chats in public and private Microsoft Teams channels and individual communications. When you assign users to a Communication Compliance policy with Microsoft Teams coverage selected, the solution automatically detects chat communications across all Microsoft Teams where users are a member.
 To learn how to detect communication risks in Microsoft Teams with Communication Compliance, watch the following video:
 Microsoft Purview Communication Compliance automatically includes Microsoft Teams coverage for predefined policy templates and selects it as the default in the custom policy template. Teams transcripts are also included. Teams chats matching Communication Compliance policy conditions might take up to 48 hours to process.
-For Teams private chat and private channels, Communication Compliance policies support modern attachment analysis. Shared Channels support in Teams is handled automatically and doesn't require additional Communication Compliance configuration changes. The following table summarizes Communication Compliance behavior when sharing Teams channels with groups and users:
+For Teams private chat and private channels, Communication Compliance policies support modern attachment analysis. Shared Channels support in Teams is handled automatically and doesn't require additional Communication Compliance configuration changes. Communication Compliance policies do not support modern attachments in shared channels. The following table summarizes Communication Compliance behavior when sharing Teams channels with groups and users:
 Scenario
 Communication Compliance behavior
 Share a channel with an internal team

```

---

### 7. M365 Agents admin guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/m365-agents-admin-guide
**Section:** Copilot Extensibility
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -23,9 +23,9 @@ Feedback
 Summarize this article for me
 When you add
-Microsoft 365 Copilot
+Microsoft Copilot
 to your qualifying Microsoft 365 for business subscription, you provide generative AI capabilities to your organization. With these capabilities, you help enhance your organization's productivity, improve accuracy, and provide personalized assistance.
-In addition to the generative AI capabilities provided by Microsoft 365 Copilot, you can extend your AI implementation to include agents. Agents allow you to customize your Copilot experience. You can connect agents to your organization's knowledge and data sources to help members of your organization answer questions, automate tasks, and run business processes. These AI-driven agents can perform various tasks, working alongside you to offer suggestions, automate repetitive tasks, and provide insights to help you and your organization make more informed decisions.
+In addition to the generative AI capabilities provided by Microsoft Copilot, you can extend your AI implementation to include agents. Agents allow you to customize your Copilot experience. You can connect agents to your organization's knowledge and data sources to help members of your organization answer questions, automate tasks, and run business processes. These AI-driven agents can perform various tasks, working alongside you to offer suggestions, automate repetitive tasks, and provide insights to help you and your organization make more informed decisions.
 This guide:
 Helps you determine which Copilot agent capabilities your organization needs
 Helps you understand where members of your organization view agents
@@ -38,20 +38,20 @@ Admin permissions
 .
 Identify your Copilot licensing scenario
-Organizations typically deploy a combination of Microsoft 365 Copilot Chat and Microsoft 365 Copilot. Before you get started, it's important to understand the differences between these two offerings when it comes to deploying and using agent
```

---

### 8. Agent insights report in SharePoint

**URL:** https://learn.microsoft.com/en-us/sharepoint/insights-on-sharepoint-agents
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -80,7 +80,7 @@ in Microsoft 365. For more information, see
 Getting started with SharePoint Online Management Shell
 .
-To generate and view these reports, ensure the organization has the SharePoint Advanced Management add-on SKU or Microsoft 365 Copilot license.
+To generate and view these reports, ensure the organization has the SharePoint Advanced Management add-on SKU or Microsoft Copilot license.
 With permissions of at least a SharePoint administrator, you can generate and view the insights report by using the following commands:
 To generate a report for the default one-day report duration, run the following command:
 Start-SPOCopilotAgentInsightsReport

```

---

### 9. Copilot in SharePoint (preview)

**URL:** https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-get-started
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -25,13 +25,13 @@ Note
 This article applies to the preview version of Copilot in SharePoint (previously referred to as AI in SharePoint).
 Microsoft 365 GovernmentâGCC, GCC High, DoD, Office 365 air-gapped cloud environments, and Microsoft 365 operated by 21Vianet don't currently support Copilot in SharePoint.
-Copilot in SharePoint helps you do more with your content. Ask questions, run workflows, and create SharePoint sites, pages, lists, libraries, interactive reports, and Office files by using natural language. Starting in mid-June 2026, these capabilities roll out as an opt-out preview and become available automatically to all users with a Microsoft 365 Copilot license.
+Copilot in SharePoint helps you do more with your content. Ask questions, run workflows, and create SharePoint sites, pages, lists, libraries, interactive reports, and Office files by using natural language. Starting in mid-June 2026, these capabilities roll out as an opt-out preview and become available automatically to all users with a Microsoft Copilot license.
 Important
 Copilot in SharePoint is changing from an opt-in preview to an opt-out preview. No administrator action is required to receive it. If you previously opted out your tenant or specific sites, those settings are honored.
 Prerequisites
 To use Copilot in SharePoint during the preview:
-Microsoft 365 Copilot license:
-Users must have an active Microsoft 365 Copilot license. Copilot in SharePoint is included with this license during preview and at General Availability, at no extra cost.
+Microsoft Copilot license:
+Users must have an active Microsoft Copilot license. Copilot in SharePoint is included with this license during preview and at General Availability, at no extra cost.
 No opt-in step is required.
 Copilot in SharePoint is on by default for licensed users when the opt-out preview reaches your tenant. To control availability, see
 Manage availability of Copilot in SharePoint
@@ -96,7 +96,7 @@ NoSites
 : Co
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Copilot Pages and Notebooks compliance summary
**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-compliance-summary?view=o365-worldwide
**Classification:** MEDIUM (General content update)

---

### 2. What's new in Copilot Cowork
**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/whats-new
**Classification:** MEDIUM (General content update)

---

### 3. Managing AI experiences enabled by usage-based billing
**URL:** https://learn.microsoft.com/microsoft-365/copilot/discovery-setting-ai-experiences
**Classification:** MEDIUM (General content update)

---

### 4. Agent settings in Microsoft 365 admin center
**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide
**Classification:** MEDIUM (General content update)

---

### 5. SharePoint Advanced Management
**URL:** https://learn.microsoft.com/en-us/sharepoint/advanced-management
**Classification:** MEDIUM (General content update)

---

### 6. SharePoint Admin Agent (Content Governance Agent)
**URL:** https://learn.microsoft.com/en-us/sharepoint/content-governance-agent
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
| https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms |
| https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*