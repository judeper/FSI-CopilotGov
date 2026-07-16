# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-16
**Run Time:** 2026-07-16T11:26:41.904477+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 6 |
| MEDIUM Changes | 2 |
| Redirects | 13 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | manage-public-web-access | HIGH | 2.6 | Update portal-walkthrough |
| 2 | microsoft-365-copilot-usage | HIGH | 4.5 | Update portal-walkthrough |
| 3 | release-notes | HIGH | 4.12 | Update portal-walkthrough |
| 4 | discovery-setting-ai-experiences | MEDIUM | 4.15 | Update portal-walkthrough |
| 5 | ...-based-billing-manage-copilot-credits | MEDIUM | 4.15 | Update portal-walkthrough |
| 6 | archive-overview | HIGH | 3.2 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Manage Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access
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
--- +++ @@ -34,15 +34,13 @@ Researcher
 and
 Analyst
-in Microsoft 365 Copilot. While web search isn't a prerequisite for using Researcher and Analyst, enabling web search is recommended to get the most value out of using them. The only difference is that Researcher and Analyst don't have a
+in Microsoft 365 Copilot. While web search isn't a prerequisite for using Researcher and Analyst, enabling web search is recommended to get the most value out of using them. Researcher has a
+Web search
+toggle accessible in the input box. Analyst doesn't have a
 Web content
 toggle for users.
 Web search
-When web search is enabled, Microsoft 365 Copilot and Microsoft 365 Copilot Chat may fetch information from the Bing search service when information from the web helps to provide a better, more grounded response. Admin controls and a user-level
-Web content
-toggle (only for Microsoft 365 Copilot) are available to
-manage whether web search is enabled
-in your environment.
+When web search is enabled, Microsoft 365 Copilot and Microsoft 365 Copilot Chat may fetch information from the Bing search service when information from the web helps to provide a better, more grounded response. Admin controls and a user-level Web content toggle are available for eligible Microsoft 365 Copilot and Microsoft 365 Copilot Chat users.
 How web search works
 When web search is enabled, Microsoft 365 Copilot and Microsoft 365 Copilot Chat parse the user's prompt and identifies terms where information from the web would improve the quality of the response. Based on these terms, Copilot generates a search query that it sends to the Bing search service asking for more information.
 This generated search query is different from the user's original prompt-it consists of a few words informed by the user's prompt. The following information isn't included in the generated search query sent to the Bing search service:
@@ -131,7 +129,7 @@ EU Data Boundary
 don't apply to generated search queries.
 Control
```

---

### 2. Copilot usage reports

**URL:** https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-365-copilot-usage?view=o365-worldwide
**Section:** Copilot Administration
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -22,7 +22,7 @@ Microsoft 365 Copilot usage report
 Feedback
 Summarize this article for me
-The Microsoft 365 Copilot usage report provides a summary of how users adopt, retain, and engage with Microsoft 365 Copilot and its associated enabled apps, including agent usage. For Copilot activity on a given day, the report typically becomes available within 72 hours of the end of that day (in UTC).
+The Microsoft 365 Copilot usage report provides a summary of how users adopt, retain, and engage with Microsoft 365 Copilot and its associated enabled apps. For Copilot activity on a given day, the report typically becomes available within 48 hours of the end of that day (in UTC).
 For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see
 Microsoft 365 admin center usage reports overview
 .
@@ -57,7 +57,7 @@ Usage
 tab to view adoption and usage metrics.
 Interpret the Microsoft 365 Copilot usage report
-At the top, you can filter by different timeframes. You can view the Microsoft 365 Copilot report over the last 7, 30, 90, or 180 days.
+At the top, you can filter by different timeframes. You can view the Microsoft 365 Copilot report over the last 7, 28, 90, or 180 days.
 You can view several numbers for Microsoft 365 Copilot usage, which highlight the enablement number and the adoption of the enablement:
 Enabled Users
 shows the total number of unique users in your organization with Microsoft 365 Copilot licenses over the selected timeframe.
@@ -70,10 +70,6 @@ , the recommended action card highlights
 Microsoft Copilot Dashboard
 , where you can deliver insights to your IT leaders to explore Copilot readiness, adoption, and impact in Viva Insights.
-Active agent users
-shows the total number of unique Microsoft 365 Copilot users in your org who used agents built by your org (including admin-approved agents and agents created via agent builder and shared with users in your org).
-Note
-Agent us
```

---

### 3. Microsoft 365 Copilot release notes

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 4.12: Control 4.12: Change Management for Copilot Feature Rollouts
  - File: `controls/pillar-4-operations/4.12-change-management-rollouts.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/4.12/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/4.12/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.12/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -30,6 +30,151 @@ Android
 iOS
 Mac
+July 15, 2026
+Updates released between July 01, 2026, and July 15, 2026.
+Microsoft 365 admin center
+Submit agent to Agent Store from Agent Builder
+[Windows, Web]
+Customers can submit their agents built in Agent Builder to the Agent Store under the "Built by your org" section, after admin review and approval in Microsoft 365 Admin Center. This governed flow enables admins to review, approve, and publish submitted agents so that they can be discovered and used by others in the Agent Store. This helps organizations share validated agents at scale while maintaining quality and governance.
+Roadmap ID:
+557173
+Details:
+What changed:
+Customers can submit agents created in Agent Builder to the Agent Store after admin review and approval in the Microsoft 365 Admin Center. Previously, there was no governed process for publishing custom agents at scale. This update introduces a controlled workflow that maintains quality and governance while enabling agent sharing within organizations.
+Why:
+This change helps organizations share validated custom agents securely and efficiently. Admin review ensures agents meet organizational standards before publication.
+Try this:
+Build an agent in Agent Builder.
+Submit the agent for admin review in the Microsoft 365 Admin Center.
+After approval, find the agent published under 'Built by your org' in the Agent Store.
+Why this matters:
+Governed submission protects organizational security while enabling wider use of custom Copilot agents.
+Business impact:
+Organizations can scale agent deployment with centralized control, improving collaboration and compliance.
+Personal impact:
+You gain access to trusted, organization-approved agents that enhance productivity and reduce duplicated effort.
+Learn
+Submit agents from Agent Builder to your org catalog
+Manage agent requests in Microsoft 365 admin center
+Microsoft 365 Copilot
+Copilot Prompt Gallery - Company-wide prompt publishing
+[W
```

---

### 4. Managing AI experiences enabled by usage-based billing

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
--- +++ @@ -56,6 +56,10 @@ In the side panel, select the checkbox
 Allow users to discover and use AI experiences enabled by usage-based billing in Microsoft 365 Copilot
 .
+Related articles
+Managing AI experiences enabled by usage-based billing
+Usage-Based Billing and Cost Management for Copilot Credits
+Cowork Usage report
 Feedback
 Was this page helpful?
 Yes

```

---

### 5. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
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
--- +++ @@ -385,6 +385,10 @@ Agents and services
 view, review usage for supported services, including Cowork and Work IQ API. This view shows active users, credits used, and session count for each supported service.
 Compare usage across users, groups, agents, and services to help adjust policies or redistribute credit budgets.
+Related articles
+Usage-based billing overview for Copilot credits
+Discovery setting for AI experiences enabled by usage-based billing
+Cowork Usage report
 Feedback
 Was this page helpful?
 Yes

```

---

### 6. Microsoft 365 Archive overview

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
--- +++ @@ -68,8 +68,8 @@ SharePoint admin center: Archiving a site with channel sites is not possible. (Message: "The group connected site with channel sites associated can't be archived.")
 PowerShell and Graph API: Archiving a site with channel sites isn't blocked.
 Only the main site associated to the Team (and its standard channels) is archived. The private and shared channel sites remain active. Archiving the channel sites directly is not possible, as these sites use unsupported site templates.
-File Archive (preview) limitations
-Some Microsoft 365 applications and services don't yet support file-level archiving. These applications might display incorrect error messages, fail to load correctly, or fail actions taken with archived content. Because client support and user awareness for archived files continue to evolve during this preview period, we recommend that you use file-level archive thoughtfully and ensure users understand how to reactivate files at their original location if access is required-especially if they encounter unexpected open or load errors. The list of known limitation includes but isn't limited to:
+File Archive limitations
+Some Microsoft 365 applications and services don't yet support file-level archiving. These applications might display incorrect error messages, fail to load correctly, or fail actions taken with archived content. Because client support and user awareness for archived files continue to evolve, we recommend that you use file-level archive thoughtfully and ensure users understand how to reactivate files at their original location if access is requiredâespecially if they encounter unexpected open or load errors. The list of known limitation includes but isn't limited to:
 Word and PowerPoint online.
 Teams, OneDrive, and SharePoint mobile applications.
 macOS with the OneDrive sync client.

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Managing AI experiences enabled by usage-based billing
**URL:** https://learn.microsoft.com/microsoft-365/copilot/discovery-setting-ai-experiences
**Classification:** MEDIUM (General content update)

---

### 2. Manage Copilot Credits (usage-based billing)
**URL:** https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
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

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*