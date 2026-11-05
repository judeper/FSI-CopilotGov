# Microsoft Learn Documentation Changes

**Run Date:** 2026-11-05
**Run Time:** 2026-11-05T17:45:12.006989+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 12 |
| MEDIUM Changes | 5 |
| Redirects | 32 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | MEDIUM | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | microsoft-365-copilot-requirements | HIGH | 2.15, 1.1, 1.9, 1.4 | Update portal-walkthrough |
| 3 | microsoft-365-copilot-privacy | MEDIUM | 2.6, 2.7, 3.8a, 3.8, 3.10, 1.10, 1.4 | Update portal-walkthrough |
| 4 | release-notes | HIGH | 4.12, 3.8a | Update portal-walkthrough |
| 5 | connect-to-ai-subprocessor | CRITICAL | 2.7, 3.8a, 1.8, 1.10 | Update portal-walkthrough |
| 6 | ...lot-ai-provider-user-sec-group-access | MEDIUM | None | Review optional |
| 7 | apply-sensitivity-label-automatically | HIGH | 2.2, 1.5 | Update portal-walkthrough |
| 8 | audit-log-activities | HIGH | 2.2, 2.13, 3.1, 1.15 | Update portal-walkthrough |
| 9 | cowork-admin-governance | HIGH | 4.15 | Update portal-walkthrough |
| 10 | cowork-models | HIGH | 4.15 | Update portal-walkthrough |
| 11 | cowork-faq | HIGH | 4.15 | Update portal-walkthrough |
| 12 | ...t.com/en-us/microsoft-copilot-studio/ | MEDIUM | 2.14, 4.14 | Update portal-walkthrough |
| 13 | cross-tenant-access-overview | MEDIUM | 2.12 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`

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
--- +++ @@ -20,7 +20,7 @@ Anthropic subprocessors are available only in applicable Microsoft 365 licensed experiences and aren't available to all users by default. Anthropic operates with
 Microsoft Enterprise data protections
 . For more information, see
-Anthropic models in Microsoft Online Services
+Claude models from Anthropic in Microsoft Online Services
 .
 Compare Microsoft 365 Copilot licenses
 Copilot Chat (Basic) license
@@ -393,7 +393,7 @@ Anthropic subprocessors are available only in applicable Microsoft 365 licensed experiences and aren't available to all users by default. Anthropic operates with
 Microsoft Enterprise data protections
 . For more information, see
-Anthropic models in Microsoft Online Services
+Claude models from Anthropic in Microsoft Online Services
 .
 Model
 Description

```

---

### 2. Microsoft 365 Copilot requirements

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Section:** Copilot Administration
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`
- Control 1.1: Control 1.1: Copilot Readiness Assessment and Data Hygiene
  - File: `controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md`
- Control 1.9: Control 1.9: License Planning and Copilot Assignment Strategy
  - File: `controls/pillar-1-readiness/1.9-license-planning.md`
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
--- +++ @@ -30,6 +30,10 @@ Supported Microsoft 365 apps and services
 Required for app-specific experiences
 Required for app-specific experiences
+Operating system requirements
+for the Microsoft Copilot app
+Required
+Required
 Supported browser and cookies
 Required for web-based experiences
 Required for web-based experiences
@@ -113,6 +117,24 @@ Whiteboard
 To use Microsoft Copilot with Microsoft Whiteboard, enable Whiteboard for your tenant. For more information, see
 Manage access to Microsoft Whiteboard for your organization
+.
+Operating system requirements
+The Microsoft Copilot app is supported on the following operating systems:
+Windows
+: Windows 11, version 22H2 or later
+Ensure EdgeUpdate is on version
+1.3.253.25
+or later.
+Installers are available for x64 and ARM64 devices and can be deployed using Microsoft Intune, Microsoft Configuration Manager, Group Policy, or another software deployment solution.
+Mac
+: macOS 13 (Ventura) and later
+Mobile devices
+:
+iPhone: iOS 16.0 or later
+iPad: iPadOS 16.0 or later
+Android 10 or later
+For more detailed information about deploying the Microsoft Copilot app to devices in an organization, see
+Deploy the unified Microsoft Copilot application
 .
 Browser and cookie requirements
 Use a current, supported browser. Microsoft Edge, Google Chrome, Mozilla Firefox, and Apple Safari are supported for Microsoft 365 web experiences.

```

---

### 3. Data, privacy, and security for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.6: Control 2.6: Copilot Web Search and Web Grounding Controls
  - File: `controls/pillar-2-security/2.6-web-search-controls.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 3.8: Control 3.8: Model Risk Management Alignment (SR 26-2 / OCC Bulletin 2026-13, applying SR 11-7 / OCC 2011-12 principles to generative AI)
  - File: `controls/pillar-3-compliance/3.8-model-risk-management.md`
- Control 3.10: Control 3.10: SEC Reg S-P -- Privacy of Consumer Financial Information
  - File: `controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md`
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`

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
--- +++ @@ -21,7 +21,7 @@ blocking prompt injections (jailbreak attacks)
 .
 For information about models provided by Anthropic as a subprocessor within Microsoft Copilot experiences, see
-Anthropic models in Microsoft Online Services
+Claude models from Anthropic in Microsoft Online Services
 .
 For information about models provided by OpenAI as a subprocessor within Microsoft Copilot experiences, see
 OpenAI as a subprocessor in Microsoft Online Services
@@ -58,7 +58,7 @@ Data, privacy, and security for web queries in Microsoft Copilot and Microsoft Copilot Chat
 .
 Microsoft offers third-party AI models in Microsoft Copilot, such as Anthropic and OpenAI models. As an admin, you can decide whether to use these models to power your experiences, and additional terms may apply. Review the following documentation to learn more:
-Anthropic models in Microsoft Online Services
+Claude models from Anthropic in Microsoft Online Services
 and
 OpenAI as a subprocessor in Microsoft Online Services
 .
@@ -100,7 +100,7 @@ . EU traffic stays within the EU Data Boundary while worldwide traffic can be sent to the EU and other countries or regions for LLM processing.
 Note
 Models provided by Anthropic as a subprocessor are currently excluded from the EU Data Boundary. For more information, see
-Anthropic models in Microsoft Online Services
+Claude models from Anthropic in Microsoft Online Services
 .
 Microsoft Copilot and data residency
 Microsoft Copilot is upholding data residency commitments as outlined in the Microsoft Product Terms and Data Protection Addendum. Microsoft Copilot was added as a covered workload in the data residency commitments in Microsoft Product Terms on March 1, 2024.

```

---

### 4. Microsoft 365 Copilot release notes

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 4.12: Control 4.12: Change Management for Copilot Feature Rollouts
  - File: `controls/pillar-4-operations/4.12-change-management-rollouts.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -7,6 +7,204 @@ Android
 iOS
 Mac
+November 4, 2026
+Updates released between October 28, 2026 and November 3, 2026.
+Excel
+Navigate to your workbook changes directly from the Copilot chat pane response
+[Windows, Web, Mac]
+In Copilot in Excel, the response contains links to highlight where changes are made in your workbook. Navigate directly to new sheets, tables, ranges, and objects like charts and shapes.
+What changed:
+In the Copilot chat response, there now is a link you can click that will take you directly to changes in the workbook. Previously, you would need to locate the change in the response and navigate in the sheet on your own.
+Why:
+We want you to understand where copilot made edits and connect you to them directly from the chat response. This will help build confidence in the changes and allow you to review while you're reading the response in the chat pane.
+Try this:
+Send a prompt to Copilot where the workbook is modified.
+The chat response will show the changes in a different format with a highlight to indicate a link you can click for navigation. New Sheets, tables, ranges, and objects will be highlighted.
+Why this matters:
+The feature allows quick review of document changes made by Copilot, increasing transparency of the edits.
+Business impact:
+Teams can understand changes made while reading the response from Copilot and quickly navigate to those places for review.
+Personal impact:
+You can review the Copilot Edits in your document.
+Microsoft 365 admin center
+Agents usage report
+[Web]
+A new agents usage report will be available in the Microsoft 365 admin center. The report will be scoped to include agents in Microsoft 365 Copilot and Copilot Chat with usage by both M365 Copilot licensed and unlicensed users. The report will include total active agent users, total active agents, active users segmentation by licensed and unlicensed users, and active users and active agents segmentation by publisher type (i.e. user-created 
```

---

### 5. Anthropic as a Microsoft subprocessor

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Section:** Copilot Administration
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 1.8: Control 1.8: Information Architecture Review
  - File: `controls/pillar-1-readiness/1.8-information-architecture-review.md`
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.10/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.10/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.10/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.8/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.8/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.8/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.8/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -1,13 +1,13 @@-Anthropic models in Microsoft Online Services
-Microsoft is introducing a new offering with Anthropic AI models as part of Microsoft Online Services, delivering enterprise-grade commitments and safeguards to ensure secure and responsible use of Anthropic models within your organization.
-To enable this change, Anthropic has onboarded as a Microsoft subprocessor. This change simplifies the experience and strengthens compliance and security under Microsoft's enterprise framework. The Microsoft Customer Copyright Commitment (CCC) applies to Anthropic models used within products covered by the CCC, including Microsoft Copilot and Copilot Studio.
+Claude models from Anthropic in Microsoft Online Services
+Microsoft is introducing a new offering with Claude models from Anthropic as part of Microsoft Online Services, delivering enterprise-grade commitments and safeguards to ensure secure and responsible use of Claude models within your organization.
+To enable this change, Anthropic has onboarded as a Microsoft subprocessor. This change simplifies the experience and strengthens compliance and security under Microsoft's enterprise framework. The Microsoft Customer Copyright Commitment (CCC) applies to Claude models used within products covered by the CCC, including Microsoft Copilot and Copilot Studio.
 As a subprocessor, Anthropic operates with Microsoft oversight through contractual safeguards and appropriate technical and organizational measures. Unless models are labeled "Anthropic models with Data Retention," the
 Microsoft Product Terms
 and
 Microsoft Data Protection Addendum (DPA)
-apply to the use of Anthropic models through Microsoft's enterprise Online Services. Such use is also covered under our
+apply to the use of Claude models from Anthropic through Microsoft's enterprise Online Services. Such use is also covered under our
 Enterprise Data Protection
-. Anthropic models have built-in safeguards, instantiated and operated by Anthropic
```

---

### 6. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -45,7 +45,7 @@ Policy rule fails to load
 .
 I'm hitting a limit
-(500,000 files/day, 100 policies, 1,000 explicitly selected SharePoint sites, or 20,000,000 matched files per policy simulation). See
+(a tenant-wide throughput ceiling of 500,000 files/day, not a guaranteed daily rate; 100 policies; 1,000 explicitly selected SharePoint sites; or 20,000,000 matched files per policy simulation). See
 How to configure auto-labeling policies for SharePoint, OneDrive, and Exchange
 , and
 Use PowerShell for auto-labeling policies
@@ -96,7 +96,9 @@ banner in the Microsoft Purview portal, or by using PowerShell. If PDF labeling isn't enabled, PDFs are skipped entirely: PDFs aren't evaluated or sent for labeling, and no label is applied. For instructions, see
 Adding support for PDF
 .
-Maximum of 500,000 automatically labeled files in your tenant per day.
+The
+absolute maximum throughput
+is 500,000 automatically labeled SharePoint and OneDrive files per tenant per day, in aggregate across all auto-labeling policies. This ceiling isn't a guaranteed or consistently expected daily processing rate; actual throughput can be lower.
 Maximum of 100 auto-labeling policies per tenant. In the portal, each policy can target up to 1,000 explicitly included or excluded SharePoint sites, or up to 100 explicitly included or excluded OneDrive individual users or groups. If you keep the default configuration of
 All
 , this configuration is exempt from these maximums.
@@ -1123,7 +1125,9 @@ to verify that the label was applied automatically. Allow
 60 to 90 minutes for the activity to appear
 . Activity explorer identifies the resulting label and how it was applied, but doesn't identify the specific auto-labeling policy or rule that applied the label to an Exchange message.
-The labeling progress includes the files to be labeled or unlabeled by the policy, the affected files for the last seven days, and the total files affected. A maximum of 500,000 SharePoint and OneDrive files
```

---

### 7. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/1.15/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.15/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.2/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/3.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/incident-and-risk/agent-behavioral-incident-playbook.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -429,6 +429,9 @@ Created group
 CreatedGroup
 A user group was created.
+Created organization member
+CreatedOrganizationMember
+An organization member was created.
 Created organization role assignment
 CreatedOrganizationRoleAssignment
 An organization role assignment was created.
@@ -459,6 +462,9 @@ Deleted organization
 DeletedOrganization
 An organization was deleted from the hierarchy.
+Deleted organization member
+DeletedOrganizationMember
+An organization member was deleted.
 Deleted organization role assignment
 DeletedOrganizationRoleAssignment
 An organization role assignment was deleted.
@@ -489,12 +495,18 @@ Listed EHR instances
 ListedEhrInstances
 EHR instances were listed.
+Listed EHR users
+ListedEhrUsers
+EHR users were listed.
 Listed environments
 ListedEnvironments
 All environments were listed.
 Listed extensions
 ListedExtensions
 Extensions were listed.
+Listed group members
+ListedGroupMembers
+Group members were listed.
 Listed groups
 ListedGroups
 User groups were listed.

```

---

### 8. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
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
--- +++ @@ -17,7 +17,7 @@ Managing AI experiences enabled by usage-based billing
 .
 Important
-A spending policy is an access control, not only a budget. Any user in the scope of a spending policy that selects Cowork can use Cowork. To keep a user out of Cowork, don't include them in any spending policy that selects Cowork, rather than lowering their limit. Learn how access is determined across policies, discovery, and model settings in
+A spending policy is an access control, not only a budget. Users in the scope of a spending policy that selects Cowork can use Cowork. To remove access for a user, remove them from every spending policy that includes Cowork. A low credit limit doesn't block access. Learn how access is determined across policies, discovery, and model settings in
 How access to Copilot Cowork is determined
 .
 The agent-based access control from the Frontier and Preview versions is deprecated for access control. Copilot Cowork is generally available and is no longer managed by selecting
@@ -34,10 +34,10 @@ Learn about Copilot admin settings in
 Microsoft Copilot app features that admins can control
 .
-Migrating from Frontier or Preview access control
-If you managed Cowork access during the Frontier or Preview program, the control you used has changed.
+Migrating from Frontier or preview access control
+If you managed Cowork access during the Frontier or preview program, the control you used has changed.
 What the agent control used to do
-: In the Preview version, you allowed or blocked users by configuring the
+: In the preview version, you allowed or blocked users by configuring the
 Cowork
 agent entry under
 All Agents

```

---

### 9. Copilot Cowork available models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models
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
--- +++ @@ -5,7 +5,7 @@ For admins
 : You can turn off the Anthropic model family in the
 Microsoft 365 admin center
-under Copilot settings. This model control has no effect on whether a user can access Cowork. The setting is tenant-wide, so it can't be used to grant Anthropic models to a subset of users. When the Anthropic family is off, users keep working with the non-Anthropic models your organization allows. When you select
+under Copilot settings. This model control has no effect on whether a user can access Cowork. The setting is tenant-wide, and the Anthropic enablement setting can be scoped to sets of users or groups. When the Anthropic family is off, users keep working with the non-Anthropic models your organization allows. When you select
 Auto
 , Cowork chooses from the remaining available models.
 Where you pick a model

```

---

### 10. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
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
--- +++ @@ -364,7 +364,9 @@ Can an administrator disable Cowork?
 Yes. Administrators can manage access to Cowork through the Microsoft 365 admin center:
 Disable for specific users
-: Add users to a security group configured to exclude them from the Copilot experience.
+: To remove access for a user, remove them from every spending policy that includes Cowork. A low credit limit doesn't block access. Learn more in
+Manage Copilot Cowork for your organization
+.
 Control deployment
 : In the Microsoft 365 Apps admin center, administrators can disable automatic installation of the Microsoft Copilot app or manage distribution through Microsoft Intune, Configuration Manager, or Group Policy.
 Manage availability
@@ -388,7 +390,7 @@ Cowork can't delete files or folders in OneDrive or SharePoint.
 Microsoft doesn't validate custom skills created by users. Review custom skill outputs carefully.
 Attached files must be less than 200 MB.
-Cowork can't read encrypted files, even if the user has access.
+Cowork can't read encrypted files unless users have the EXTRACT and VIEW usage rights.
 Is Cowork secure?
 Yes. Every action Cowork takes is authorized through your Microsoft 365 account. Cowork accesses only the services and data you're already permitted to use. Cowork runs in a secure, isolated environment.
 How do I give feedback?

```

---

### 11. Microsoft Copilot Studio documentation

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/
**Section:** Copilot Studio
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.14: Control 2.14: Declarative and SharePoint Agents Governance
  - File: `controls/pillar-2-security/2.14-declarative-agents-governance.md`
- Control 4.14: Control 4.14: Copilot Studio Agent Lifecycle Governance
  - File: `controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.14/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/4.14/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.14/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -66,7 +66,6 @@ Add other agents
 Build and manage agent flows
 Agent flows overview
-Build an agent flow with natural language
 Edit and manage your agent flow in the designer
 Add an agent flow to an agent
 Evaluate your agents

```

---

### 12. Microsoft Entra Cross-Tenant Access Settings

**URL:** https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-overview
**Section:** Agent Governance
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.12: Control 2.12: External Sharing and Guest Access Governance
  - File: `controls/pillar-2-security/2.12-external-sharing-governance.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -168,6 +168,12 @@ or
 Microsoft Entra entitlement management
 .
+When role-enabled group sync is available in your environment, the target tenant also controls inbound role-assignable group synchronization through
+Allow role-enabled group synchronization into this tenant
+. Select this checkbox together with
+Allow group synchronization into this tenant
+to allow role-enabled group sync. This feature synchronizes role-assignability, not the source group's role assignments.
+The screenshot identifies the settings. The group and role-enabled group checkboxes aren't selected in this example.
 To configure these settings using Microsoft Graph, see the
 Update crossTenantIdentitySyncPolicyPartner
 API. For more information, see

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Classification:** MEDIUM (General content update)

---

### 2. Data, privacy, and security for Microsoft 365 Copilot
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy
**Classification:** MEDIUM (General content update)

---

### 3. Assign AI provider access to users and groups
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-ai-provider-user-sec-group-access
**Classification:** MEDIUM (General content update)

---

### 4. Microsoft Copilot Studio documentation
**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/
**Classification:** MEDIUM (General content update)

---

### 5. Microsoft Entra Cross-Tenant Access Settings
**URL:** https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-overview
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/copilot/plan/copilot-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/copilot/adopt/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access | https://learn.microsoft.com/en-us/copilot/plan/manage-public-web-access |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/copilot/plan/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy | https://learn.microsoft.com/en-us/copilot/plan/microsoft-365-copilot-privacy |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/copilot/adopt/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience | https://learn.microsoft.com/en-us/copilot/manage/copilot-search-admin-experience |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage | https://learn.microsoft.com/en-us/copilot/manage/copilot-search-manage |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor | https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-ai-provider-user-sec-group-access | https://learn.microsoft.com/en-us/copilot/implement/copilot-ai-provider-user-sec-group-access |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ | https://learn.microsoft.com/en-us/copilot/cowork/ |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new | https://learn.microsoft.com/en-us/copilot/cowork/whats-new |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started | https://learn.microsoft.com/en-us/copilot/cowork/get-started |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance | https://learn.microsoft.com/en-us/copilot/cowork/cowork-admin-governance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models | https://learn.microsoft.com/en-us/copilot/cowork/cowork-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins | https://learn.microsoft.com/en-us/copilot/cowork/cowork-manage-plugins |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq | https://learn.microsoft.com/en-us/copilot/cowork/cowork-faq |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences | https://learn.microsoft.com/en-us/copilot/implement/discovery-setting-ai-experiences |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits | https://learn.microsoft.com/en-us/copilot/implement/usage-based-billing-manage-copilot-credits |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-admin-guide | https://learn.microsoft.com/en-us/copilot/manage/copilot-tuning-admin-guide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-settings?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*