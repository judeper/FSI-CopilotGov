# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-01
**Run Time:** 2026-08-01T11:10:28.727149+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| HIGH Changes | 1 |
| MEDIUM Changes | 1 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | apply-sensitivity-label-automatically | CRITICAL | 1.5, 2.2 | Update portal-walkthrough |
| 2 | whats-new | MEDIUM | 4.15 | Update portal-walkthrough |
| 3 | cowork-faq | HIGH | None | Review and update |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** CRITICAL (Deprecation notice)

**Affected Controls:**
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`

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
--- +++ @@ -27,6 +27,48 @@ For information about automatically applying a sensitivity label to data stored outside Microsoft 365 and in the data map, see
 Labeling in Microsoft Purview Data Map
 .
+Tip
+Start here â pick your task
+I'm setting up my first auto-labeling policy.
+Review the
+Prerequisites for auto-labeling policies
+first, then follow
+Creating an auto-labeling policy
+.
+I'm deciding between labeling in Office apps and an auto-labeling policy.
+See
+Compare auto-labeling for Office apps with auto-labeling policies
+.
+My simulation results look wrong or incomplete.
+See
+Learn about simulation mode
+â the caveats cover the most common causes (12-hour completion window, single-policy scope, files modified after the run, and the sensitive info type created-after-modification rule).
+A specific file wasn't labeled and I expected it to be.
+Open the policy's
+Labeled items
+tab and switch to the
+Failed
+view to see the failure reason. For the full list of reasons and fixes, see
+Resolve auto-labeling failures in SharePoint and OneDrive files
+.
+I'm hitting a limit
+(100,000 files/day, 100 policies, 100 locations, or 4,000,000 files in simulation). See
+How to configure auto-labeling policies for SharePoint, OneDrive, and Exchange
+, and
+Use PowerShell for auto-labeling policies
+when you need to configure more than 100 locations.
+Auto-labeling isn't available in my region.
+The
+Auto-labeling
+page isn't visible in unsupported regions. See
+Azure dependency availability by country/region
+.
+I want to set a default label for Teams meetings, sites, groups, or Microsoft 365 Copilot.
+This article covers files and emails. For container-level default labels (including Teams instant meetings and Meet Now), see
+Use sensitivity labels with Microsoft Teams, Microsoft 365 groups, and SharePoint sites
+. For Copilot default labels, see
+Considerations for Microsoft 365 Copilot
+.
 When you create a sensitivity label, you can automatically assign that labe
```

---

### 2. What's new in Copilot Cowork

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
--- +++ @@ -22,10 +22,19 @@ What's new in Copilot Cowork
 Feedback
 Summarize this article for me
-This article lists recent features, improvements, and changes in Microsoft 365 Copilot Cowork. For a full guide to Cowork's capabilities, see
+This article lists recent features, improvements, and changes in Microsoft 365 Copilot Cowork. Get a full guide to Cowork's capabilities in
 Use Cowork
 .
 July 2026
+Enhancements
+Feature
+Description
+Learn more
+Workspace file input for plugin tools
+Plugin connector tools can now accept files from your session as input. Plugin authors declare a tool parameter with
+contentEncoding: base64
+, and Cowork resolves the workspace file to content before calling the toolâso a tool can convert a document, analyze an image, or attach a file to another system.
+Accept files from the Cowork workspace
 New features
 Feature
 Description

```

---

## HIGH: Control Review Recommended

### 1. Copilot Cowork FAQ

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

**What Changed:**
```diff
--- +++ @@ -27,7 +27,7 @@ Cowork is available in Microsoft 365 Copilot. It carries out tasks on your behalf. For example, it can send emails, schedule meetings, create documents, post in Teams, and handle multi-step tasks across your Microsoft 365 environment.
 What can Cowork do for me?
 Cowork can send emails, schedule meetings, create documents (Word, Excel, PowerPoint, PDF), post in Teams, manage your calendar, prepare daily briefings, search across your organization, conduct deep research, and draft stakeholder communications. You can also schedule prompts to run automatically.
-For a full breakdown by category, see
+Get a full breakdown by category in
 What can Cowork do for you?
 How is Cowork different from Copilot Chat?
 Cowork completes multi-step work across Microsoft 365 by taking action on your behalf, while Copilot Chat helps you generate content and insights within a single session.
@@ -61,7 +61,7 @@ folder (for example,
 /Documents/Cowork/skills/weekly-report/SKILL.md
 ).
-For a detailed description of each skill, see
+Get a detailed description of each skill in
 Cowork skills
 .
 Can I create my own custom skills?
@@ -70,7 +70,7 @@ files in your OneDrive
 /Documents/Cowork/skills/
 folder. Each file contains a YAML frontmatter block with a name and description, followed by the skill instructions. Cowork discovers your custom skills automatically at the start of each session.
-For step-by-step instructions, see
+Get step-by-step instructions in
 Create custom skills
 .
 What can Cowork access?
@@ -79,16 +79,20 @@ Yes. Cowork supports plugins from the Microsoft 365 App Store that add new skills and connectors. You can browse and install plugins from the
 Browse plugins
 menu. Once acquired, a plugin's skills appear alongside the built-in skills, and its connectors become available for your sessions.
-For step-by-step instructions, see
+Get step-by-step instructions in
 Use plugins with Cowork
 .
 Can my admin control which plugins I can use?
 Yes. You
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. What's new in Copilot Cowork
**URL:** https://learn.microsoft.com/microsoft-365/copilot/cowork/whats-new
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
| https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*