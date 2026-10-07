# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-07
**Run Time:** 2026-10-07T17:05:39.288875+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 3 |
| HIGH Changes | 1 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | release-notes | HIGH | 4.12, 3.8a | Update portal-walkthrough |
| 2 | ...data-foundation-microsoft-365-copilot | HIGH | 1.7 | Update portal-walkthrough |
| 3 | agent-id-governance-overview | HIGH | None | Review and update |
| 4 | archive-overview | HIGH | 3.2 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot release notes

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
--- +++ @@ -7,6 +7,161 @@ Android
 iOS
 Mac
+October 06, 2026
+Updates released between September 22, 2026, and October 06, 2026.
+Microsoft 365 Copilot
+Seamless Search and Chat Integration
+[Windows, Web]
+Microsoft 365 Chat brings the power of conversational AI directly into Microsoft 365 Copilot Search, enabling users to move effortlessly from finding information to acting on it. Search results become the foundation for contextual chat, allowing you to ask follow-up questions, synthesize insights, and generate contentâall in one unified experience. This integration reduces workflow fragmentation, accelerates decision-making, and delivers a more intuitive way to interact with your organizationâs knowledge.
+Roadmap ID:
+512429
+Details:
+What changed:
+Microsoft 365 Copilot Search now embeds conversational AI chat directly within search results. Previously, users had to switch between search and chat tools separately. This update allows follow-up questions, insight synthesis, and content generation based on search context in a unified interface, reducing workflow fragmentation.
+Why:
+Integrating chat with search streamlines user interaction with organizational knowledge, accelerating decision-making and reducing the need to switch tools.
+Try this:
+Open Microsoft 365 Copilot Search.
+Enter a query and review the search results.
+Use the chat pane to ask follow-up questions or generate content based on the results.
+Why this matters:
+This integration simplifies workflows by combining search and chat, helping users act on information faster.
+Business impact:
+Teams experience faster decision cycles and less disruption from switching between search and chat applications.
+Personal impact:
+You save time by accessing search results and conversational AI in one place, reducing task switching.
+Regenerate response for alternative answers
+[Web]
+The Regenerate action lets you quickly get an alternative response to your latest prompt using options like Try Again
```

---

### 2. Configure secure and governed Copilot foundation

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
--- +++ @@ -14,20 +14,17 @@ Monitor changes and Copilot activity to identify and remediate risk.
 Licensing
 The capabilities described in this article require:
-Microsoft 365 E3
-or
-Microsoft 365 E5
-(or
-Office 365 E3
-or
-Office 365 E5
-) for core Microsoft 365 services and features, such as SharePoint, OneDrive, and Microsoft Purview features.
-This article covers both the
-Microsoft Purview
-foundational capabilities that are included in Microsoft 365 E3. This article also mentions optimized features that are included in Microsoft 365 E5.
-Microsoft Copilot
+A license for Microsoft Copilot. See
+Copilot licensing requirements
+.
 SharePoint Advanced Management
 (included with Copilot licenses)
+An eligible for core Microsoft 365 services and features, such as SharePoint, OneDrive, and Microsoft Purview features. See
+Microsoft 365 apps and services
+.
+At least foundational capabilities in
+Microsoft Purview
+, which are included in Microsoft 365 E3. (This article also mentions optimized features that are included in Microsoft 365 E5 or E7.)
 Admin roles
 You must have an appropriate role assigned to perform the tasks described in this article.
 For more information, see the following resources:
@@ -37,8 +34,6 @@ Permissions in the Microsoft Purview portal
 Step 1: Remediate oversharing
 In this step, you identify and prioritize high-risk sites and sensitive content, apply interim protections to reduce Copilot exposure, and then remediate access and permissions.
-Video: Preventing oversharing in Copilot
-The following video provides a high-level overview of how to prevent oversharing in Copilot by configuring capabilities in SharePoint Advanced Management and Microsoft Purview:
 Identify high-risk sites and content
 Use
 Microsoft Purview

```

---

### 3. Microsoft 365 Archive overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/archive/archive-overview?view=o365-worldwide
**Section:** Microsoft 365 Archive
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 3.2: Control 3.2: Data Retention Policies for Copilot Interactions
  - File: `controls/pillar-3-compliance/3.2-data-retention-policies.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/3.2/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/3.2/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.2/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.2/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -58,6 +58,49 @@ Files that are reactivated cannot be archived again for 120 days.
 Certain file types can't be archived, including OneNote, SharePoint pages, and SharePoint agents.
 The Site Assets library on SharePoint sites does not support file-level archive.
+File types excluded from SAM archive policies
+SharePoint Advanced Management (SAM) automatic file archive policies can't archive files with the following extensions:
+.js
+,
+.css
+,
+.one
+,
+.onepkg
+,
+.onetoc2
+,
+.onetmp
+,
+.spcolor
+,
+.sptheme
+,
+.spfont
+,
+.eot
+,
+.onebin
+,
+.woff
+,
+.woff2
+,
+.xsl
+,
+.json
+,
+.classifier
+,
+.aspx
+,
+.onetoc
+,
+.onebak
+,
+.onebackupconstruction
+.
+These exclusions apply regardless of the file type filters configured for the policy.
 Related article
 Education offering
 Was this page helpful?

```

---

## HIGH: Control Review Recommended

### 1. Microsoft Entra ID Governance for agent identities

**URL:** https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview
**Section:** Agent Governance
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -55,8 +55,8 @@ inherited from their parent agent identity blueprint
 . In addition, agent identities can have resource access assigned to them directly via access packages. Agents can request an access package for own agent IDs, or have their owner or sponsor request one on their behalf. With access packages, you're able to assign agent identities access to the following resources:
 Security Group memberships
-Application OAuth API permissions
-, including Graph application permissions
+OAuth API permissions
+, delegated and application permissions for Microsoft Graph and applications
 Microsoft Entra roles
 To use access packages for agent identities, configure an access package with the required policy settings. When creating an access package assignment policy, in the
 Who can get access

```

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*