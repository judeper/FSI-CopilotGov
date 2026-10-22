# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-22
**Run Time:** 2026-10-22T14:45:29.948042+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| Redirects | 9 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-requirements | HIGH | 1.9, 1.1, 2.15, 1.4 | Update portal-walkthrough |
| 2 | archive-overview | HIGH | 3.2 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot requirements

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
--- +++ @@ -117,6 +117,24 @@ Browser and cookie requirements
 Use a current, supported browser. Microsoft Edge, Google Chrome, Mozilla Firefox, and Apple Safari are supported for Microsoft 365 web experiences.
 For Copilot to work in Word for the web, Excel for the web, and PowerPoint for the web, third-party cookies must be enabled.
+When users select a link in a Copilot Chat response, including responses from agents built in Copilot Studio, Copilot checks the link with
+Safe Links in Microsoft Defender for Office 365
+before it opens. This check requires third-party cookies for
+*.safelinks.protection.outlook.com
+. If the browser blocks third-party cookies, for example through an organization-managed browser policy, users see an
+Unable to verify link
+message and the link doesn't open.
+To avoid this issue, allow third-party cookies for
+[*.]safelinks.protection.outlook.com
+. For example:
+In Microsoft Edge or Google Chrome, add
+[*.]safelinks.protection.outlook.com
+to the
+CookiesAllowedForUrls
+policy.
+In the browser cookie settings, add
+[*.]safelinks.protection.outlook.com
+as a site that's allowed to use third-party cookies.
 Mobile requirements
 Use a supported version of the Microsoft 365 or Copilot mobile app and a supported mobile operating system. For current operating system requirements, see the app listing in the Apple App Store or Google Play Store and the applicable Microsoft 365 mobile app documentation.
 Network requirements

```

---

### 2. Microsoft 365 Archive overview

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
--- +++ @@ -1,5 +1,8 @@ Overview of Microsoft 365 Archive
 Microsoft 365 Archive provides cost-effective storage for inactive SharePoint files and sites.
+To automatically archive eligible files within SharePoint sites that remain in use, use
+inactive files policies in SharePoint Advanced Management (preview)
+. Policies use the file's recorded last human access date and are configured through PowerShell during the current preview.
 Organizations often need to retain inactive or aging data for long periods in case they need to retrieve it later. Storing this data in SharePoint helps simplify searchability, security, compliance, and data lifecycle management.
 Microsoft 365 Archive allows you to retain inactive data by moving it into a cold storage tier within SharePoint. Data archived with Microsoft 365 Archive automatically retains the same searchability, security, and
 compliance

```

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-setup-assign-licenses |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-admin-experience |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-manage |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*