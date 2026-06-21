# Microsoft Learn Documentation Changes

**Run Date:** 2026-06-21
**Run Time:** 2026-06-21T12:04:50.359909+00:00
**Total URLs Checked:** 152

---

## Executive Summary

| Category | Count |
|----------|-------|
| HIGH Changes | 27 |
| MEDIUM Changes | 15 |
| Redirects | 1 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-setup | MEDIUM | 2.6 | Review optional |
| 2 | microsoft-365-copilot-usage | HIGH | 4.5 | Review and update |
| 3 | release-notes | CRITICAL | 4.12 | Monitor |
| 4 | whats-new | CRITICAL | 4.12 | Monitor |
| 5 | connect-to-ai-subprocessor | HIGH | 3.8a, 2.7 | Review and update |
| 6 | dlp-policy-reference | HIGH | None | Review and update |
| 7 | ...osoft365-copilot-location-learn-about | HIGH | 2.1 | Review and update |
| 8 | ...e-information-type-entity-definitions | HIGH | None | Review and update |
| 9 | apply-sensitivity-label-automatically | HIGH | 1.5, 2.2 | Review and update |
| 10 | audit-log-activities | CRITICAL | 1.15 | Monitor |
| 11 | create-retention-policies | HIGH | 3.2 | Review and update |
| 12 | cpcn-compliance-summary | HIGH | 2.11 | Review and update |
| 13 | purview-management | HIGH | None | Review and update |
| 14 | ...m/en-us/microsoft-365/copilot/cowork/ | HIGH | None | Review and update |
| 15 | get-started | HIGH | None | Review and update |
| 16 | cowork-admin-governance | HIGH | None | Review and update |
| 17 | cowork-manage-plugins | HIGH | None | Review and update |
| 18 | cowork-faq | HIGH | None | Review and update |
| 19 | ai-microsoft-purview | MEDIUM | 1.2, 1.1, 2.1, index | Review optional |
| 20 | .../microsoft-365/copilot/extensibility/ | HIGH | 4.13, 1.13, 2.14, 2.16, 2.13 | Review and update |
| 21 | overview-copilot-connector | MEDIUM | 2.13 | Review optional |
| 22 | authoring-ask-a-question | HIGH | None | Review and update |
| 23 | agent-365-overview | HIGH | 4.13, 4.5 | Review and update |
| 24 | agent-registry | MEDIUM | 4.13, 2.14 | Review optional |
| 25 | ...n.microsoft.com/en-us/entra/agent-id/ | HIGH | 2.17 | Review and update |
| 26 | what-is-microsoft-entra-agent-id | MEDIUM | None | Review optional |
| 27 | what-are-agent-identities | MEDIUM | None | Review optional |
| 28 | whats-new-agent-id | MEDIUM | None | Review optional |
| 29 | what-is-agent-id-platform | MEDIUM | None | Review optional |
| 30 | configure-third-party-agents | MEDIUM | None | Review optional |
| 31 | agent-id | HIGH | 2.3, 2.17 | Review and update |
| 32 | concept-risky-agents | HIGH | None | Review and update |
| 33 | agent-id-governance-overview | MEDIUM | None | Review optional |
| 34 | concept-secure-web-ai-gateway-agents | MEDIUM | None | Review optional |
| 35 | data-connectors-reference | CRITICAL | 4.11, 3.1 | Monitor |
| 36 | ...opilot-sharepoint-advanced-management | HIGH | 1.13, 1.3 | Review and update |
| 37 | ai-in-sharepoint-get-started | HIGH | None | Review and update |
| 38 | restricted-content-discovery | HIGH | 1.7 | Review and update |
| 39 | content-governance-agent | HIGH | 1.7 | Review and update |
| 40 | zero-trust-microsoft-365-copilot | HIGH | None | Review and update |
| 41 | what-is-defender-for-cloud-apps | HIGH | 2.9 | Review and update |
| 42 | archive-overview | HIGH | 3.2 | Review and update |

---

## HIGH: Control Review Recommended

### 1. Copilot usage reports

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage?view=o365-worldwide
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 4.5: Control 4.5: Copilot Usage Analytics and Adoption Reporting
  - File: `controls/pillar-4-operations/4.5-usage-analytics.md`

**What Changed:**
```diff
--- +++ @@ -26,7 +26,7 @@ For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see
 Microsoft 365 admin center usage reports overview
 .
-View the Microsoft 365 Copilot usage report
+View the Microsoft 365 Copilot usage report in the Microsoft 365 admin center
 For information about the roles needed to view usage reports, see "Before you begin" in
 Microsoft 365 admin center usage reports overview
 Go to the
@@ -253,7 +253,7 @@ Adoption
 section, you might see a recommendation card:
 To learn more about using organizational messages for Microsoft 365 Copilot, see
-Microsoft 365 features adoption using organizational messages
+Drive adoption with Microsoft 365 Copilot Usage report's Organizational Messages feature
 .
 You can export the report data into an Excel .csv file by selecting the ellipses and then
 Export

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
--- +++ @@ -19,29 +19,50 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Anthropic as a subprocessor for Microsoft Online Services
+Anthropic models in Microsoft Online Services
 Feedback
 Summarize this article for me
 Microsoft is introducing a new offering with Anthropic AI models as part of Microsoft Online Services, delivering enterprise-grade commitments and safeguards to ensure secure and responsible use of Anthropic models within your organization.
-To enable this change, Anthropic has onboarded as a Microsoft subprocessor. As part of this update, we're deprecating the previous option that allowed Microsoft tenant admins to opt in to use Anthropic models under Anthropic's separate commercial terms and data processing agreement. This change simplifies the experience and strengthens compliance and security under Microsoft's enterprise framework.
-As a subprocessor, Anthropic will operate with Microsoft oversight through contractual safeguards and appropriate technical and organizational measures. The Microsoft
-Product Terms
+To enable this change, Anthropic has onboarded as a Microsoft subprocessor. This change simplifies the experience and strengthens compliance and security under Microsoft's enterprise framework. The Microsoft Customer Copyright Commitment (CCC) applies to Anthropic models used within products covered by the CCC, including Microsoft 365 Copilot and Copilot Studio.
+As a subprocessor, Anthropic will operate with Microsoft oversight through contractual safeguards and appropriate technical and organizational measures. Unless models are labeled "Preview models with Data Retention," the
+Microsoft Product Terms
 and
 Microsoft Data Protection Addendum (DPA)
 apply to use of Anthropic models through Microsoft's enterprise Online Services. Such use is also covered under our
 Enterprise Data Protection
-. The Microsoft Customer Copyright Commitment (CCC) applies to Anthropic models used within products covered b
```

---

### 3. DLP policy reference

**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-reference
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Compliance features)

**What Changed:**
```diff
--- +++ @@ -958,6 +958,18 @@ - Only available in the
 Custom
 policy template
+Note
+In the
+Devices
+location, the
+Devices and device groups
+setting supports only
+Audit or restrict activities on devices
+. You can't use it with
+Audit or restrict activities when users access sensitive sites in the Microsoft Edge browser on Windows devices
+under
+Rule Actions
+.
 Exchange location scoping
 If you choose to include specific distribution groups in Exchange, the DLP policy is scoped to the emails sent by members of that group or sent to members of that group. Similarly, excluding a distribution group excludes all the emails sent by the members of that distribution group or from policy evaluation.
 Group Type
@@ -1695,10 +1707,10 @@ Document name contains words or phrases
 Document size equals or is greater than
 Document created by
-Document creation date is on or after (preview)
-Document creation date is on or before (preview)
-Document modification date is on or after (preview)
-Document modification date is on or before (preview)
+Document creation date is on or after
+Document creation date is on or before
+Document modification date is on or after
+Document modification date is on or before
 Conditions OneDrive accounts support
 Content contains
 Content is shared from Microsoft 365
@@ -1711,10 +1723,10 @@ Document size equals or is greater than
 Document created by
 Document is shared
-Document creation date is on or after (preview)
-Document creation date is on or before (preview)
-Document modification date is on or after (preview)
-Document modification date is on or before (preview)
+Document creation date is on or after
+Document creation date is on or before
+Document modification date is on or after
+Document modification date is on or before
 Conditions Teams chat and channel messages support
 Content contains
 Insider risk level for Adaptive Protection is
@@ -1921,6 +1933,8 @@ Conditions Microsoft 365 Copilot supports
 This feature is in preview.
 C
```

---

### 4. DLP for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 2.1: Control 2.1: DLP Policies for Microsoft 365 Copilot Interactions
  - File: `controls/pillar-2-security/2.1-dlp-policies-for-copilot.md`

**What Changed:**
```diff
--- +++ @@ -22,13 +22,15 @@ Learn about using Microsoft Purview Data Loss Prevention to protect interactions with Microsoft 365 Copilot and Copilot Chat
 Feedback
 Summarize this article for me
-Microsoft Purview Data Loss Prevention (DLP) can help you protect interactions with Microsoft 365 Copilot and Copilot Chat in two ways:
-Restrict Microsoft 365 Copilot from using external web search when prompts contain sensitive data (preview)
-, you can use Microsoft Purview Data Loss Prevention (DLP) policies to prevent Microsoft 365 Copilot and Copilot Chat from sending sensitive information to external web services. When a prompt contains sensitive information types (SITs)âsuch as credit card numbers, passport numbers, Social Security numbers, or custom SITs defined by your organizationâCopilot automatically blocks the use of external web search as a grounding source for that prompt. Instead, Copilot continues to generate responses using permitted internal Microsoft 365 data sources, where applicable. This ensures that sensitive data remains protected and is not shared with external search providers.
-Restrict Microsoft 365 Copilot and Copilot Chat from processing sensitive prompts
-, you can create a DLP policy to help protect against the use of sensitive information types (SIT), such as credit card numbers, passport identification, or social security numbers in Microsoft Copilot 365 prompts. This includes Microsoft provided SITs and custom SITs that you create. This real-time control helps organizations mitigate data leakage and oversharing risks by preventing Microsoft 365 Copilot and Copilot Chat, including prebuilt agents in Microsoft 365 Copilot and Copilot Chat, from returning a response when prompts contain sensitive data and from using that sensitive data for both internal and external web searches.
-Restrict M365 Copilot and Copilot Chat processing sensitive files and emails (generally available)
-, you can create a DLP policy to help protect against the i
```

---

### 5. Sensitive information type entity definitions

**URL:** https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-entity-definitions
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -112,8 +112,11 @@ Canada social insurance number
 Chile identity card number
 China resident identity card (PRC) number
+China physical addresses
 Client secret / API key
 Credit card number
+Colombia national ID
+Colombia tax identification number
 Croatia driver's license number
 Croatia identity card number
 Croatia passport number
@@ -161,20 +164,21 @@ General password
 General Symmetric key
 Generic medication names
-Germany driver's license number
+German Driver's License Number
 Germany identity card number
-Germany passport number
+German Passport Number
 Germany physical addresses
 Germany tax identification number
 Germany value added tax number
 GitHub Personal Access Token
 Google API key
+Greenland physical addresses
 Greece driver's license number
 Greece national ID card
 Greece passport number
 Greece physical addresses
 Greece Social Security Number (AMKA)
-Greece tax identification number
+Greek Tax Identification Number
 Hong Kong identity card (HKID) number
 Http authorization header
 Hungary driver's license number
@@ -213,11 +217,11 @@ Italy value added tax number
 Japan bank account number
 Japan driver's license number
-Japan My Number - Corporate
-Japan My Number - Personal
+Japanese My Number Corporate
+Japanese My Number Personal
 Japan passport number
 Japan physical addresses
-Japan residence card number
+Japanese Residence Card Number
 Japan resident registration number
 Japan social insurance number (SIN)
 Lab test terms
@@ -270,7 +274,7 @@ Poland driver's license number
 Poland identity card
 Poland national ID (PESEL)
-Poland passport number
+Poland Passport Number
 Poland physical addresses
 Poland REGON number
 Poland tax identification number
@@ -279,16 +283,20 @@ Portugal passport number
 Portugal physical addresses
 Portugal tax identification number
-Qatari identification card number
+Qatari ID Card Number
 Romania driver's license number
 Romania passport number
 Romania personal numeric code (CNP)
 Romania physical
```

---

### 6. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`

**What Changed:**
```diff
--- +++ @@ -754,6 +754,51 @@ However currently, restricted admins won't be able to see labeling activities for OneDrive in activity explorer.
 Tip
 You can also use content explorer to identify locations that have documents with sensitive information, but are unlabeled. Using this information, consider adding these locations to your auto-labeling policy, and include the identified sensitive information types as rules.
+Policy-level labeling activity for SharePoint and OneDrive
+For auto-labeling policies that are turned on and target SharePoint and OneDrive, you can monitor them right from the main
+Auto-labeling
+page and use the per-policy review pages. Use these pages to monitor day-to-day labeling activity, spot-check labeled files, and investigate labeling failures.
+To view the review pages, you need one of the following roles:
+Compliance Administrator
+Compliance Data Administrator
+Information Protection Admin
+Information Protection Analyst
+To see the matched text inside a file from the
+Contextual summary
+tab, you also need the
+Data Classification Content Viewer
+role.
+To open these pages, from
+Information Protection
+>
+Auto-labeling
+, select the name of an auto-labeling policy. Most data on the review pages reflects activity from the last 30 days.
+The policy
+Overview
+page shows labeled and failed file counts, a daily activity trend chart, the top labels applied, and the top sites where labeling occurred. A
+Labeling failures
+card surfaces the total failure count and the top three failure reasons so you can quickly identify whether the policy needs attention.
+From the
+Labeled items
+tab, you can toggle between a
+Labeled
+view (a sample of successfully labeled files) and a
+Failed
+view (files the policy couldn't label, grouped by failure reason). Select any item to open a details flyout pane that includes a file preview, file properties, and a
+Contextual summary
+tab that explains in plain language why the file matched or why labeling faile
```

---

### 7. Create and configure retention policies

**URL:** https://learn.microsoft.com/en-us/purview/create-retention-policies
**Section:** Audit and Retention
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 3.2: Control 3.2: Data Retention Policies for Copilot Interactions
  - File: `controls/pillar-3-compliance/3.2-data-retention-policies.md`

**What Changed:**
```diff
--- +++ @@ -100,7 +100,7 @@ . When you configure retention settings for the
 Teams channel message
 location, if a team has any shared channels, they inherit retention settings from their parent team.
-From late April 20206, retention policies also support newly created Teams call logs when you create the retention policies with PowerShell. For more information, see
+From late April 2026, retention policies also support newly created Teams call logs when you create the retention policies with PowerShell. For more information, see
 Retention policy for Teams call logs
 .
 Sign in to the Microsoft Purview portal
@@ -205,9 +205,7 @@ Retention policy for Teams call logs
 Teams call logs represent the collection of call-related data generated by Teams, including call data records (CDRs) and other call metadata. CDRs are also sometimes referred to as call detail records, or just call records.
 Prior to supporting the retention of Teams call logs in late April 2026, CDRs for Teams chat and Teams channels were included in retention policies for the Teams chat location. Going forward, new CDRs are supported only when you create a retention policy for Teams call logs. CDRs included in previous Teams chat retention policies continue to be managed by those same policies.
-This separate retention policy for call logs can be created only by using PowerShell, and has the following considerations:
-The policy is tenant-wide and can't be scoped to individual users.
-The policy doesn't support adaptive scopes or administrative units.
+This separate retention policy for call logs can be created and modified only by using PowerShell. It has the following considerations:
 The policy includes call logs for both Teams chat and Teams channels.
 The policy applies only to new call logs that are created after the policy is configured and active.
 After you create the retention policy for Teams call logs, it's displayed in
@@ -215,14 +213,13 @@ >
 Policies
 in the Microsoft Purview portal, wh
```

---

### 8. Copilot Pages and Notebooks compliance summary

**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/cpcn-compliance-summary?view=o365-worldwide
**Section:** Copilot Pages and Notebooks
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 2.11: Control 2.11: Copilot Pages Security and Sharing Controls
  - File: `controls/pillar-2-security/2.11-copilot-pages-security.md`

**What Changed:**
```diff
--- +++ @@ -42,9 +42,10 @@  Supported
 eDiscovery
 â- Supported (full-text search in review sets not available)
+ Supported
 Legal Hold
-â Manual - container must be added per user
+â+ Supported; selecting the container in the custodian data source picker is rolling out (expected early August)
 Retention policies
 â  Supported via "All SharePoint Sites"
@@ -78,7 +79,7 @@ EUDB
 : Compliance is supported. See
 What is the EU Data Boundary?
-Data Security, Devices
+Data security and devices
 Intune
 :
 Device Management Support
@@ -111,19 +112,19 @@ and
 Set
 guest app permissions.
-Data Lifecycle
+Data lifecycle
 Scenario: user leaves the organization.
-The Copilot Pages and Copilot Notebooks container follows the OneDrive cleanup schedule (30 days active, then 93 days to permanent deletion). To add owners and preserve content before deletion, see
+The container follows the same
+OneDrive deletion lifecycle
+as the rest of Microsoft 365, with one manual handoff step at departure (access and notification aren't automatic) and the option to permanently reassign the container to a new owner. For the full process, options, and comparison with OneDrive, see
 Grant access to containers
 . To preserve content before departure, export it using Purview or the Graph API, or add the container to a retention policy.
 Storage
 : Copilot Pages and Copilot Notebooks are stored together in a single user-owned SharePoint Embedded container, which is also shared by Loop My workspace. Storage counts against your organization's SharePoint quota. See
 storage
-for the full explanation of the shared container,
+for the full explanation of the shared container and
 Managing SharePoint Embedded containers
-for admin tooling, and
-Grant access to containers
-for the manual access workflow at user departure.
+for admin tooling.
 Limitation
 : There's no admin control to set quota limits on individual containers.
 Admin control note
@@ -137,7 +138,7 @@ preferred data location
 .
 Known 
```

---

### 9. Purview management for SharePoint Embedded containers

**URL:** https://learn.microsoft.com/en-us/microsoft-365/loop/purview-management?view=o365-worldwide
**Section:** Copilot Pages and Notebooks
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -62,7 +62,7 @@ Note
 The
 Container Redirect URL
-field may not yet be available in the SharePoint admin center. This capability is still rolling out. Track the rollout status on the
+field might not yet be available in the SharePoint admin center. This capability is still rolling out. Track the rollout status on the
 Microsoft 365 public roadmap
 .
 Searching the Audit Logs

```

---

### 10. Copilot Cowork overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -19,22 +19,9 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Cowork overview (Frontier)
+Copilot Cowork overview
 Feedback
 Summarize this article for me
-[This article is prerelease documentation and is subject to change.]
-Important
-You need to be part of the
-Frontier preview program
-to get
-early access
-to Microsoft 365 Copilot Cowork. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
-If Cowork isn't visible in Microsoft Admin Center Agent management, ensure that the admin account is also enrolled in Frontier (Copilot -> Settings -> Frontier).
-This is a preview feature.
-Preview features may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
-For more information, go to our
-Microsoft Product Terms
-.
 Microsoft 365 Copilot Cowork can carry out tasks on your behalf. You describe what you need, and Cowork sends emails, schedules meetings, creates documents, posts in Teams, and manages your calendar. You approve each action before it happens.
 What is Cowork?
 Cowork carries out tasks across your Microsoft 365 environment. Rather than describing what you could do, it does the work.
@@ -65,7 +52,7 @@ Reorganize your existing files into new or existing folders.
 Calendar and meetings
 Schedule meetings using natural language, such as "set up a 30-minute check-in with Alex tomorrow at 2 PM."
-Manage your calendar â add events, move things around, or clean up conflicts by declining meetings. Cowork can include a message to the organizer on the reason you're declining.
+Manage your calendarâadd events, move things around, or clean up conflicts by declining meetings. Cowork can include a message to the organize
```

---

### 11. Get started with Copilot Cowork

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -19,31 +19,20 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Get started with Cowork (Frontier)
+Get started with Copilot Cowork
 Feedback
 Summarize this article for me
-[This article is prerelease documentation and is subject to change.]
-Important
-You need to be part of the
-Frontier preview program
-to get
-early access
-to Microsoft 365 Copilot Cowork. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
-If Cowork isn't visible in Microsoft Admin Center Agent management, ensure that the admin account is also enrolled in Frontier (Copilot -> Settings -> Frontier).
-This is a preview feature.
-Preview features may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
-For more information, go to our
-Microsoft Product Terms
-.
 Microsoft 365 Copilot Cowork allows you to describe what you needâdraft an email, build a spreadsheet, schedule a meetingâand Cowork handles it. This article walks you through your first conversation, from sending a request to reviewing the result.
 Prerequisites
 Before you begin, make sure you have:
 Microsoft 365 Copilot access
-: An active Microsoft 365 Copilot license assigned to your account and enrollment in the frontier program.
+: An active Microsoft 365 Copilot license assigned to your account.
 A modern browser
 : Microsoft Edge or Google Chrome recommended.
 Cowork available
 : Cowork is enabled in your Microsoft 365 Copilot environment.
+Usage-based billing
+: Usage-based and Cowork billing has been enabled.
 Anthropic enabled in tenant
 : Cowork uses Anthropic models as a subprocessor to ensure secure and responsible use of Anthropic models within your organization. Details 
```

---

### 12. Copilot Cowork admin and governance

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -19,179 +19,85 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Manage Cowork for your organization
+Manage Copilot Cowork for your organization
 Feedback
 Summarize this article for me
-[This article is prerelease documentation and is subject to change.]
-Important
-You need to be part of the
-Frontier preview program
-to get
-early access
-to Microsoft 365 Copilot Cowork. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
-If Cowork isn't visible in Microsoft Admin Center Agent management, ensure that the admin account is also enrolled in Frontier (Copilot -> Settings -> Frontier).
-This is a preview feature.
-Preview features may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
-For more information, go to our
-Microsoft Product Terms
+Learn how to manage plugins, models, browser use, security and compliance, and usage-based billing in Copilot Cowork.
+Allow access to Cowork
+To allow users to access Cowork, admins must enable usage-based billing. To learn how to set up and enable usage-based billing, see
+Managing AI experiences enabled by usage-based billing
 .
-Microsoft 365 Copilot Cowork is available to all Microsoft 365 Copilot tenants. IT administrators can control who has access to it, deploy it on behalf of users, and pin it in the Copilot experience using the same governance tools in Microsoft 365 Copilot.
-Default availability
-By default, Cowork is
-available to all licensed users
-in your tenant. This means:
-You can discover and install it yourself from the Agent Store.
-It's
-not pre-installed
-or pre-pinned for youâno action is required to enable it.
-If you don't want to use it, you can simply 
```

---

### 13. Manage Copilot Cowork plugins

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -19,25 +19,14 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Manage plugins for Cowork (Frontier)
+Manage plugins for Copilot Cowork
 Feedback
 Summarize this article for me
-[This article is prerelease documentation and is subject to change.]
-Important
-You need to be part of the
-Frontier preview program
-to get
-early access
-to Microsoft 365 Copilot Cowork. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
-If Cowork isn't visible in Microsoft Admin Center Agent management, ensure that the admin account is also enrolled in Frontier (Copilot -> Settings -> Frontier).
-This is a preview feature.
-Preview features may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
-For more information, go to our
-Microsoft Product Terms
-.
 Microsoft 365 Copilot Cowork supports plugins that add skills and connectors to extend what Cowork can do. As an IT administrator, you control which plugins are available in your organization, how they're deployed, and who can use them. This article covers plugin governance from an admin perspective.
 For information on how users browse and use plugins, see
 Use plugins with Cowork
+and
+Customize Copilot Cowork
 . For information on building plugins, see
 Build plugins for Cowork
 .
@@ -60,25 +49,23 @@ Microsoft 365 admin center
 .
 Select
-Copilot
->
 Agents
 >
-All agents
+Tools
 .
 Find the plugin you want to deploy. You can search by name or browse the available plugins.
 Select the plugin to open its details.
-Under
-Deploy to
+Select
+Installed for
 , select
-Entire organization
+All users
 or
 Specific users/groups
 .
 Select
-Deploy
-.
-When you deploy a plugin, it's automaticall
```

---

### 14. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -19,22 +19,9 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Cowork common questions (Frontier)
+Copilot Cowork common questions
 Feedback
 Summarize this article for me
-[This article is prerelease documentation and is subject to change.]
-Important
-You need to be part of the
-Frontier preview program
-to get
-early access
-to Microsoft 365 Copilot Cowork. Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities may change over time.
-If Cowork isn't visible in Microsoft Admin Center Agent management, ensure that the admin account is also enrolled in Frontier (Copilot -> Settings -> Frontier).
-This is a preview feature.
-Preview features may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
-For more information, go to our
-Microsoft Product Terms
-.
 Find answers to common questions about Microsoft 365 Copilot Cowork.
 What is Cowork?
 Cowork is available in Microsoft 365 Copilot. It carries out tasks on your behalf. For example, it can send emails, schedule meetings, create documents, post in Teams, and handle multi-step tasks across your Microsoft 365 environment.
@@ -323,6 +310,22 @@ view, or from the
 Schedule
 section of the side panel.
+Can Cowork use my local browser?
+Yes. Cowork can complete web tasks for you in Microsoft Edge on your device, using the sites you're already signed in to. The browser tab runs on your machine, your credentials and cookies stay on your device, and Cowork uses only the access you already have. If Cowork hits a sign-in step it can't complete on its own, it hands the browser back to you to finish. For details, see
+Use the local browser with Cowork
+.
+Can I generate images with Cowork?
+Yes. Ask Cowork 
```

---

### 15. Copilot extensibility overview

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
--- +++ @@ -25,7 +25,7 @@ Reference
 Microsoft 365 Agents Toolkit
 Microsoft 365 Agents SDK
-Work IQ API (preview)
+Work IQ API
 Microsoft 365 Copilot APIs
-Interactive Demo (preview)
+Interactive Demo
 Microsoft Agent 365
```

---

### 16. Adaptive cards in Copilot Studio topics

**URL:** https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-ask-a-question#add-an-adaptive-card
**Section:** Copilot Studio
**Classification:** HIGH (UI element names)

**What Changed:**
```diff
--- +++ @@ -24,10 +24,10 @@ Summarize this article for me
 A
 Question
-node prompts a user for information and stores their response in a variable for use later on in the conversation.
-The node allows you to choose the type of information to collect, such as a multiple-choice answer, a prebuilt entity, or a custom entity.
+node prompts a user for information and stores their response in a variable for use later in the conversation.
+The node offers options for the type of information to collect, such as a multiple-choice answer, a prebuilt entity, or a custom entity.
 Question behavior properties
-allow you to control the behavior of the node, such as what to do when the user enters an invalid response.
+let you control the behavior of the node, such as what to do when the user enters an invalid response.
 Like
 Message
 nodes,
@@ -97,9 +97,9 @@ question properties
 .
 Configure question properties
-The
+Use the
 Question properties
-panel is where you can adjust behaviors like prompting, validation, and interruptions.
+panel to adjust behaviors like prompting, validation, and interruptions.
 To open the
 Question properties
 panel, select the three dots (
@@ -119,7 +119,7 @@ (available for voice-enabled agents only)
 Hold and resume
 Configure question behavior
-Question behavior properties allow you to control whether the agent can skip the question and how it responds to an invalid response.
+Question behavior properties control whether the agent can skip the question and how it responds to an invalid response.
 Skip behavior
 Skip behavior
 determines what the agent should do if the question node's variable already has a value from earlier in the conversation.
@@ -147,24 +147,34 @@ Customize
 , and then enter the new prompt.
 Configure entity recognition
-Entity recognition properties allow you to expand validation beyond the default rules for the entity to collect, and to choose what happens when your agent isn't able to elicit a valid entity value from the u
```

---

### 17. Agent management in Microsoft 365 admin center

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide
**Section:** Agent Governance
**Classification:** HIGH (Policy language)

**Affected Controls:**
- Control 4.13: Control 4.13: Copilot Extensibility and Agent Operations Governance
  - File: `controls/pillar-4-operations/4.13-extensibility-governance.md`
- Control 4.5: Control 4.5: Copilot Usage Analytics and Adoption Reporting
  - File: `controls/pillar-4-operations/4.5-usage-analytics.md`

**What Changed:**
```diff
--- +++ @@ -53,15 +53,33 @@ The Microsoft Frontier program gives organizations early access to innovative and emerging AI capabilities in Microsoft 365 before those features reach general availability (GA). Frontier previews are subject to the existing preview terms of your customer agreements. For more information, see
 Get started with the Microsoft Frontier program
 .
-Prerequisites
+Prerequisites for agent management
 Before you can manage agents in the Microsoft 365 admin center, confirm the following requirements are met:
-Your organization has the required Microsoft 365 subscription and licenses for either Microsoft 365 Copilot or Microsoft Agent 365 capabilities.
-Users who create, publish, or use agents have the appropriate licenses assigned.
-Youâre assigned an administrator role that includes permissions to manage settings for either Microsoft 365 Copilot or Microsoft Agent 365 in the Microsoft 365 admin center.
+Your organization has the required subscription and licenses for either Microsoft 365, Microsoft 365 Copilot, or Microsoft Agent 365.
+Users at your organization that create, publish, or use agents have the appropriate licenses assigned.
+Youâre assigned an administrator role that includes permissions to manage settings for Microsoft 365, Microsoft 365 Copilot, or Microsoft Agent 365 in the Microsoft 365 admin center.
 For more information, see the following resources:
+Licensing for agent management
+Agent management roles and permissions
+Licensing for agent management
+The following licensing options include agents that can be managed in Microsoft 365 admin center:
+Microsoft 365 plans
+Microsoft 365 (All Suites) includes Copilot Chat. Copilot Chat provides web data agents.
+Microsoft 365 (E7) includes Microsoft 365 E5, Microsoft 365 Copilot, Microsoft Agent 365, and Microsoft Entra Suite.
+Microsoft 365 Copilot
+This license can be added to your Microsoft 365 license (E3, E5). It's included with your Microsoft 365 license (E7). This optio
```

---

### 18. Microsoft Entra Agent ID documentation

**URL:** https://learn.microsoft.com/en-us/entra/agent-id/
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.17: Control 2.17: Cross-Tenant Agent Federation (MCP and Entra Agent ID)
  - File: `controls/pillar-2-security/2.17-cross-tenant-agent-federation.md`

**What Changed:**
```diff
--- +++ @@ -1,46 +1,57 @@-Microsoft Entra Agent ID
-Protect agent identities and secure their access to applications and resources. Part of Microsoft Agent 365, Microsoft Entra Agent ID and the Microsoft agent identity platform provide the foundation for secure and compliant AI agent deployments in the enterprise.
-Learn about Microsoft Entra Agent ID
-Get started with Microsoft Entra Agent ID
-Learn about how Microsoft Entra Agent ID and Agent 365 work together so you can observe, govern, and secure agents across your organization.
-Manage agents
-Learn how to manage all aspects of agents in your ecosystem, such as assigning sponsors and requesting access packages.
+Microsoft Entra Agent ID documentation
+Secure access for AI agents with enterprise-grade access management, protection, and governance. Integrate AI agents with enterprise workflows, apply Zero Trust principles, and govern agent access at scale using the identity and network access capabilities of Microsoft Entra.
+Overview
+What is Microsoft Entra Agent ID?
+Architecture
+Plan your agent identity architecture
+Concept
+Security for AI overview
+What's new
+What's new in Agent ID
+Manage, govern, and protect
+Microsoft Entra Agent ID helps you manage, govern, and protect AI agent identities across your organization.
 Manage agent identities
+Create an agent blueprint
+Create agent identities
+Manage owners and sponsors
 Govern agent lifecycles
-Ensure the lifecycle of your agents is governed with access reviews, entitlement management, and sponsor accountability.
-Get started
+ID Governance for agents
+Access packages for agents
+Maintain agent sponsors and lifecycle
 Protect agent access to resources
-Apply the same Zero Trust principles and access controls to your agents as you do for your users and workloads.
-Security for AI overview
-Build on the Microsoft agent identity platform
-Build agents with enterprise-ready identities using the Microsoft agent identity platform.
+Conditional Access for age
```

---

### 19. Conditional Access for agent identities

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
--- +++ @@ -32,6 +32,7 @@ Guide to managing agent identities across your organization:
 Manage agent identities in your organization
 .
+How to target agent identities in Conditional Access
 Configure policies for autonomous agent access
 How Conditional Access evaluates agent access requests
 To access a corporate resource such as SharePoint file, MCP servers, or Open API services, a user or agent first requests an access token from Microsoft Entra ID.
@@ -70,32 +71,22 @@ In this flow, the agent can't reuse the user's original token because it was issued for a different audience. Instead, the agent uses the OBO flow to exchange tokens with Microsoft Entra ID, obtaining a new token scoped to the target resource. This token exchange is also evaluated by Conditional Access, letting admins enforce granular controls over which resources agents can access on behalf of the user.
 Because the user is the subject in this flow, Conditional Access policies target
 users and groups
-, not agent identities. For step-by-step policy configuration, see
-Conditional Access for agents operating on-behalf-of a user
-.
+, not agent identities.
 Agents acting as an application
 Agents might access resources without a signed-in user. In this case the agent accesses the resource with its own identity. This flow is also known as client credentials flow, or app only access. All types of agents might use this flow. For more information about how agents authenticate with their own identity, see
 Agent OAuth flows: Autonomous apps
 .
-The following diagram shows the application only access authorization flow.
 This flow applies in the following common scenarios:
 Autonomous agents that operate independently
-:
-These agents run in the background, respond to events, or run on a schedule.
-For example, an agent that generates a daily report and sends the result to a group of employees. In this scenario, there's no user present, and the agent operates on its own.
+run in the background, respond 
```

---

### 20. Identity Protection for agents

**URL:** https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -19,7 +19,7 @@ Access to this page requires authorization. You can try
 changing directories
 .
-ID Protection for agents (Preview)
+ID Protection for agents
 Feedback
 Summarize this article for me
 As organizations adopt, build, and deploy autonomous AI agents, the need to monitor and protect those agents becomes critical. Microsoft Entra ID Protection helps protect your organization by automatically detecting and responding to identity-based risks on agents that have agent identities provided by
@@ -35,59 +35,48 @@ Conditional Access Administrator
 role assigned.
 Licensing
-Microsoft Entra Agent ID is a product within Microsoft Entra that provides the platform for creating and managing agent identities and agent identity blueprints. Agent ID is available for all Microsoft Entra customers.
-Integration with
-Microsoft Agent 365
-enables agents to operate across Microsoft 365 services and enterprise workflows, which requires a
-Microsoft Agent 365
-license for each user. For pricing details, see
-Microsoft Agent 365 plans and pricing
-.
-Technical requirements that enable the security features for agents within Microsoft Entra require
-Microsoft 365 E5
-or the following licensing:
-Conditional Access for agents
-: Microsoft Entra ID P1
-ID Protection for agents
-: Microsoft Entra ID P2
-ID Governance for agents
-: Microsoft Entra ID P1
-Network controls for agents
-: Microsoft Entra Internet Access, included in Microsoft Entra Suite or licensed separately. For more information, see
-What is Global Secure Access
+Starting soon, ID Protection for agents will require a
+Microsoft Agent 365 license
+to extend protection to agents through
+Microsoft Entra Agent ID
 .
 How it works
-Because agents can operate autonomously and on behalf of (OBO) a user, they can display unique sign-in behavior. Agents can take initiative, interact with sensitive data, and operate at scale. Microsoft Entra ID Protection for agents is designed to identify and mitigate risks asso
```

---

### 21. Get ready for Copilot with SharePoint Advanced Management

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

### 22. AI in SharePoint (preview)

**URL:** https://learn.microsoft.com/en-us/sharepoint/ai-in-sharepoint-get-started
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -19,81 +19,39 @@ Access to this page requires authorization. You can try
 changing directories
 .
-Get started with AI in SharePoint (preview)
+Get started with Copilot in SharePoint (preview)
 Feedback
 Summarize this article for me
 Note
-This article applies to the preview version of AI capabilities in SharePoint (previously referred to as Knowledge Agent).
-AI in SharePoint isn't currently supported in Microsoft 365 GovernmentâGCC, GCC High, DoD, Office 365 air-gapped cloud environments, or Microsoft 365 operated by 21Vianet.
+This article applies to the preview version of Copilot in SharePoint (previously referred to as AI in SharePoint).
+Copilot in SharePoint isn't currently supported in Microsoft 365 GovernmentâGCC, GCC High, DoD, Office 365 air-gapped cloud environments, or Microsoft 365 operated by 21Vianet.
+Copilot in SharePoint helps you do more with your content. Ask questions, run workflows, and create SharePoint sites, pages, lists, libraries, interactive reports, and Office files using natural language. Starting in mid-June 2026, these capabilities roll out as an opt-out preview and become available automatically to all users with a Microsoft 365 Copilot license.
 Important
-AI in SharePoint capabilities require sites to be explicitly opted in to the AI in SharePoint public preview, or for the tenant to be opted in at the tenant level. Sites that are not opted in do not receive preview benefits.
+Copilot in SharePoint is changing from an opt-in preview to an opt-out preview. No administrator action is required to receive it. If you previously opted out your tenant or specific sites, those settings are honored.
 Prerequisites
-To use AI in SharePoint during Public Preview,
-all
-of the following requirements must be met.
+To use Copilot in SharePoint during the preview:
 Microsoft 365 Copilot license:
-Users must have an active Microsoft 365 Copilot license. AI in SharePoint is included with this license during Public Preview and at Ge
```

---

### 23. Restricted Content Discovery

**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
**Section:** SharePoint Administration
**Classification:** HIGH (UI element names)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`

**What Changed:**
```diff
--- +++ @@ -122,6 +122,8 @@ Restricted Content Discovery is designed to limit the ability of end users to search for content from specific SharePoint sites. For a more comprehensive guidance on preparing your data for Copilot, check out this
 blueprint
 .
+How does Restricted Content Discovery affect the end user experience in SharePoint?
+Restricted Content Discovery will restrict usage of AI-powered features in SharePoint. Users will not see entry points such as the Copilot button, AI actions menus (including creating agents), or Create pages with AI.
 Feedback
 Was this page helpful?
 Yes

```

---

### 24. SharePoint Admin Agent (Content Governance Agent)

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

### 25. Zero Trust for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/security/zero-trust/copilots/zero-trust-microsoft-365-copilot
**Section:** Zero Trust and Security Architecture
**Classification:** HIGH (Policy language)

**What Changed:**
```diff
--- +++ @@ -155,14 +155,14 @@ .
 Govern AI apps and data for regulatory compliance
 Getting started with E3
-First, apply oversharing controls that work with Copilot, as appropriate for your environment. These controls help you protect data immediately. After doing the longer-term work of classifying data and applying sensitivity labels and protection, be sure to revisit the oversharing controls you applied initially to ensure these are still appropriate. Review the
+First, apply oversharing controls that work with Copilot, as appropriate for your environment. These controls help you protect data immediately. After doing the longer-term work of classifying data and applying sensitivity labels and protection, revisit the oversharing controls you applied initially to ensure they're still appropriate. Review the
 oversharing illustration
 and
 download the blueprint to prevent oversharing
 .
 Next, invest in data classification and protection with Microsoft Purview capabilities.
 Sensitivity labels
-form the cornerstone of protecting your data. Before you create the labels to denote the sensitivity of items and the protection actions that are applied, you must understand your organizationâs existing classification taxonomy and how it maps to labels that users see and apply in apps. After creating the sensitivity labels, publish them, and provide guidance to users how and when to apply them in Word, Excel, PowerPoint, and Outlook.
+form the cornerstone of protecting your data. Before you create the labels to denote the sensitivity of items and the protection actions that are applied, understand your organizationâs existing classification taxonomy and how it maps to labels that users see and apply in apps. After creating the sensitivity labels, publish them, and provide guidance to users on how and when to apply them in Word, Excel, PowerPoint, and Outlook.
 For more information, see:
 Get started with sensitivity labels
 Create and configure sensitivity labels and t
```

---

### 26. Microsoft Defender for Cloud Apps

**URL:** https://learn.microsoft.com/en-us/defender-cloud-apps/what-is-defender-for-cloud-apps
**Section:** Zero Trust and Security Architecture
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 2.9: Control 2.9: Defender for Cloud Apps — Copilot Session Controls
  - File: `controls/pillar-2-security/2.9-defender-cloud-apps.md`

**What Changed:**
```diff
--- +++ @@ -65,9 +65,9 @@ Continuous threat protection in eXtended detection and response (XDR)
 While cloud apps continue to be a target for adversaries trying to exfiltrate corporate data, sophisticated attacks often cross modalitiesâmoving laterally from email as the most common entry point, to compromise endpoints and identities, before ultimately gaining access to in-app data.
 Defender for Cloud Apps offers built-in adaptive access control (AAC), provides user and entity behavior analysis (UEBA), and helps you mitigate malware.
-Defender for Cloud Apps is also integrated directly into Microsoft Defender XDR, correlating XDR signals from the Microsoft Defender suite and providing incident-level detection, investigation, and powerful response capabilities. Integrating SaaS security into Microsoft's XDR experience gives SOC teams full kill chain visibility and improves operational efficiency and effectivity.
+Defender for Cloud Apps is also integrated directly into Microsoft Defender, correlating cross-domain signals from the Microsoft Defender suite and providing incident-level detection, investigation, and powerful response capabilities. Integrating SaaS security into Microsoft's unified security experience gives SOC teams full kill chain visibility and improves operational efficiency and effectivity.
 For more information, see
-Microsoft Defender for Cloud Apps in Microsoft Defender XDR
+Microsoft Defender for Cloud Apps in Microsoft Defender
 .
 App to app protection with app governance
 OAuth apps often behave unnoticed, while still having extensive permissions to access data in other apps on behalf of an employee, making OAuth apps susceptible to a compromise.

```

---

### 27. Microsoft 365 Archive overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/archive/archive-overview?view=o365-worldwide
**Section:** Microsoft 365 Archive
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 3.2: Control 3.2: Data Retention Policies for Copilot Interactions
  - File: `controls/pillar-3-compliance/3.2-data-retention-policies.md`

**What Changed:**
```diff
--- +++ @@ -74,7 +74,7 @@ Older versions of Office desktop apps that haven't had updates since March 1, 2026.
 Other apps such as Clipchamp and Power BI fail to load archived content when attempting to import.
 File-level archive is available only for SharePoint sites. When archived files are copied or moved, they retain their archived state. However, if an archived file is moved or copied into OneDrive, that archived state might not always be visually represented in the OneDrive user interface.
-Files that are reactivated cannot be archived again for 30 days.
+Files that are reactivated cannot be archived again for 120 days.
 Certain file types can't be archived, including OneNote, SharePoint pages, and SharePoint agents.
 The Site Assets library on SharePoint sites does not support file-level archive.
 Related articles

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot setup guide
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup
**Classification:** MEDIUM (General content update)

---

### 2. Microsoft 365 Copilot release notes
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Classification:** CRITICAL (Deprecation notice)

---

### 3. What's new in Microsoft Purview
**URL:** https://learn.microsoft.com/en-us/purview/whats-new
**Classification:** CRITICAL (Deprecation notice)

---

### 4. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Classification:** CRITICAL (Deprecation notice)

---

### 5. DSPM for AI (classic) overview
**URL:** https://learn.microsoft.com/en-us/purview/ai-microsoft-purview
**Classification:** MEDIUM (General content update)

---

### 6. Microsoft Graph connectors overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-copilot-connector?toc=%2Fgraph%2Ftoc.json
**Classification:** MEDIUM (General content update)

---

### 7. Agent registry in Microsoft 365 admin center
**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
**Classification:** MEDIUM (General content update)

---

### 8. Microsoft Entra Agent ID overview
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id
**Classification:** MEDIUM (General content update)

---

### 9. Microsoft Entra agent identity concepts
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities
**Classification:** MEDIUM (General content update)

---

### 10. What's new in Microsoft Entra Agent ID
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id
**Classification:** MEDIUM (General content update)

---

### 11. Microsoft Entra Agent identity platform
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/what-is-agent-id-platform
**Classification:** MEDIUM (General content update)

---

### 12. Integrate third-party agents with Microsoft Entra Agent ID
**URL:** https://learn.microsoft.com/en-us/entra/agent-id/configure-third-party-agents
**Classification:** MEDIUM (General content update)

---

### 13. Microsoft Entra ID Governance for agent identities
**URL:** https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview
**Classification:** MEDIUM (General content update)

---

### 14. Network controls for Copilot Studio agents
**URL:** https://learn.microsoft.com/en-us/entra/global-secure-access/concept-secure-web-ai-gateway-agents
**Classification:** MEDIUM (General content update)

---

### 15. Connect Microsoft 365 data
**URL:** https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference#microsoft-365-formerly-office-365
**Classification:** CRITICAL (UI navigation steps changed)

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