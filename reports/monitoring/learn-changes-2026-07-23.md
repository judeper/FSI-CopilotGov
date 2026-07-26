# Microsoft Learn Documentation Changes

**Run Date:** 2026-07-23
**Run Time:** 2026-07-23T11:45:16.829326+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| Redirects | 14 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | connect-to-ai-subprocessor | HIGH | 3.8a, 2.7 | Update portal-walkthrough |
| 2 | restricted-content-discovery | HIGH | 1.7 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Anthropic as a Microsoft subprocessor

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.7/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.7/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.7/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -78,7 +78,7 @@ in EU/EFTA and UK to enable Anthropic as the default model for Copilot in Microsoft 365 apps. For more information, see
 Copilot in Microsoft 365 apps with Anthropic models
 .
-Starting on July 15, 2026, a new setting will begin rolling out in the Microsoft 365 admin center that allows non-federal customers in Government Community Cloud (GCC) to use Anthropic models. For more information, see the
+As of July 22, 2026, a new setting is available in the Microsoft 365 admin center that allows non-federal customers in Government Community Cloud (GCC) to use Anthropic models. For more information, see the
 Enable the use of Anthropic models for non-federal customers in GCC
 section later in this article.
 Anthropic models aren't available for federal customers in GCC or for any customers in GCC High and Department of Defense (DoD) environments. They're also not available in other sovereign clouds. The option to use Anthropic models doesn't appear in the Microsoft 365 admin center for these government and sovereign cloud customers.
@@ -178,7 +178,7 @@ Enable the use of Anthropic models for non-federal customers in GCC
 Note
 The information in this section applies only to non-federal customers in Government Community Cloud (GCC). It doesnât apply to federal customers in GCC or to all customers in GCC High and Department of Defense (DoD) environments.
-Starting on July 15, 2026, a new setting will begin rolling out in the Microsoft 365 admin center that allows non-federal customers in GCC to use Anthropic models. This capability is optional and the setting is disabled by default.
+As of July 22, 2026, a new setting is available in the Microsoft 365 admin center that allows non-federal customers in GCC to use Anthropic models. This capability is optional and the setting is disabled by default.
 This setting allows non-federal GCC customers to use Anthropic-powered AI features in supported workflows, subject to specific technical, contractual, and
```

---

### 2. Restricted Content Discovery

**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -87,17 +87,6 @@ Remove Restricted Content Discovery from a site
 To disable Restricted Content Discovery for a site, open PowerShell as an administrator and run the following command:
 Set-SPOSite -Identity <site-url> -RestrictContentOrgWideSearch $false
-Apply Restricted Content Discovery to multiple sites
-Organizations often need to apply Restricted Content Discovery across large groups of sites during Copilot deployment or governance initiatives. Bulk application allows administrators to apply the feature to collections of sites instead of configuring sites individually.
-Bulk operations retain existing Restricted Content Discovery behavior:
-Restricted Content Discovery remains a site-level property.
-Sites that already have Restricted Content Discovery enabled aren't modified.
-Existing permissions remain unchanged.
-Standard propagation behavior continues to apply.
-When planning bulk operations, keep the following considerations in mind:
-Service guardrails and throttling limits apply to bulk operations.
-Large-scale updates can increase propagation time.
-Sites containing more than 500,000 items can require extended processing time before updates are fully reflected in search and Microsoft 365 Copilot.
 Delegate management to site administrators
 By default, only SharePoint administrators can manage Restricted Content Discovery.
 If you want site administrators to manage the setting for their own sites, enable delegation by using the following PowerShell command:

```

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