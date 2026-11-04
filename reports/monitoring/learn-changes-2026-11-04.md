# Microsoft Learn Documentation Changes

**Run Date:** 2026-11-04
**Run Time:** 2026-11-04T17:38:57.010254+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 20 |
| HIGH Changes | 1 |
| MEDIUM Changes | 17 |
| Redirects | 32 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-overview | MEDIUM | 1.4, 1.1, 1.9, 2.15 | Update portal-walkthrough |
| 2 | microsoft-365-copilot-setup | MEDIUM | 2.6 | Update portal-walkthrough |
| 3 | manage-public-web-access | MEDIUM | 2.6, 2.15 | Update portal-walkthrough |
| 4 | microsoft-365-copilot-requirements | MEDIUM | 1.1, 1.9, 2.15, 1.4 | Update portal-walkthrough |
| 5 | microsoft-365-copilot-privacy | MEDIUM | 1.4, 1.10, 3.10, 3.8a, 3.8, 2.7, 2.6 | Update portal-walkthrough |
| 6 | ...soft-365-copilot-enablement-resources | MEDIUM | 1.11, 1.12 | Update portal-walkthrough |
| 7 | ...t-365-copilot-search-admin-experience | MEDIUM | 1.4 | Update portal-walkthrough |
| 8 | microsoft-365-copilot-search-manage | MEDIUM | None | Review optional |
| 9 | ...ilot-foundational-deployment-guidance | MEDIUM | 1.2 | Update portal-walkthrough |
| 10 | ...data-foundation-microsoft-365-copilot | MEDIUM | 1.7 | Update portal-walkthrough |
| 11 | connect-to-ai-models | MEDIUM | 1.10, 3.8a, 2.7 | Update portal-walkthrough |
| 12 | connect-to-ai-subprocessor | MEDIUM | 1.8, 1.10, 3.8a, 2.7 | Update portal-walkthrough |
| 13 | ...lot-ai-provider-user-sec-group-access | HIGH | None | Review and update |
| 14 | ...osoft365-copilot-location-learn-about | HIGH | 1.5, 2.1, 2.6 | Update portal-walkthrough |
| 15 | audit-log-activities | MEDIUM | 1.15, 3.1, 2.2, 2.13 | Update portal-walkthrough |
| 16 | ...m/en-us/microsoft-365/copilot/cowork/ | HIGH | 4.15 | Update portal-walkthrough |
| 17 | whats-new | HIGH | 4.15 | Update portal-walkthrough |
| 18 | cowork-faq | HIGH | 4.15 | Update portal-walkthrough |
| 19 | discovery-setting-ai-experiences | MEDIUM | 4.15, 1.9, 4.8 | Update portal-walkthrough |
| 20 | ...-based-billing-manage-copilot-credits | MEDIUM | 4.15, 1.9, 4.8 | Update portal-walkthrough |
| 21 | copilot-tuning-admin-guide | MEDIUM | 1.16 | Update portal-walkthrough |
| 22 | ...opilot-sharepoint-advanced-management | MEDIUM | 1.3, 1.13 | Update portal-walkthrough |

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
--- +++ @@ -468,10 +468,4 @@ : is a low-code graphical tool that you can use to create agents and connect to other data sources. Agents let you customize your organization's Copilot experience. They can automate and execute business processes, like help desk, change management, and managing guests in meetings.
 For other Microsoft Copilot products, see the
 Microsoft Copilot learning hub
-.
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+.
```

---

### 2. Microsoft 365 Copilot setup guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -69,10 +69,4 @@ Copilot Prompt Gallery
 Configure a secure and governed data foundation for Microsoft Copilot
 Microsoft Copilot reports
-Manage Microsoft Copilot onboarding
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Manage Microsoft Copilot onboarding
```

---

### 3. Manage Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 2.6: Control 2.6: Copilot Web Search and Web Grounding Controls
  - File: `controls/pillar-2-security/2.6-web-search-controls.md`
- Control 2.15: Control 2.15: Network Security and Private Connectivity
  - File: `controls/pillar-2-security/2.15-network-security.md`

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
--- +++ @@ -177,10 +177,4 @@ Web search
 toggle.
 Note
-The privacy setting for optional connected experiences available to users in Microsoft 365 apps (for example, in Word, Excel, or Teams) has no effect on the availability of web search. For example, if a user turns off optional connected experiences, web search can still be available to the user.
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+The privacy setting for optional connected experiences available to users in Microsoft 365 apps (for example, in Word, Excel, or Teams) has no effect on the availability of web search. For example, if a user turns off optional connected experiences, web search can still be available to the user.
```

---

### 4. Microsoft 365 Copilot requirements

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
--- +++ @@ -57,8 +57,8 @@ .
 Microsoft Copilot isn't available with device-based licensing for Microsoft 365 Apps for enterprise.
 Microsoft Copilot Chat
-Microsoft Copilot Chat is available to users with an eligible Microsoft 365 subscription. For the current eligibility details, see
-Microsoft Copilot Chat eligibility
+Microsoft Copilot Chat is available to users with an eligible Microsoft 365 subscription. For guidance on managing user access, see
+Ensure users can access Microsoft Copilot Chat
 .
 Identity and sign-in requirements
 Users must have a work or school account in Microsoft Entra ID. You can add or synchronize users by using the
@@ -213,10 +213,4 @@ Related content
 Microsoft Copilot overview
 License options for Microsoft Copilot
-Add Microsoft Copilot endpoints to your allow list
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Add Microsoft Copilot endpoints to your allow list
```

---

### 5. Data, privacy, and security for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`
- Control 1.10: Control 1.10: Vendor Risk Management for Microsoft AI Services
  - File: `controls/pillar-1-readiness/1.10-vendor-risk-management.md`
- Control 3.10: Control 3.10: SEC Reg S-P -- Privacy of Consumer Financial Information
  - File: `controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md`
- Control 3.8a: Control 3.8a: Generative AI Model Governance for Microsoft 365 Copilot
  - File: `controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md`
- Control 3.8: Control 3.8: Model Risk Management Alignment (SR 26-2 / OCC Bulletin 2026-13, applying SR 11-7 / OCC 2011-12 principles to generative AI)
  - File: `controls/pillar-3-compliance/3.8-model-risk-management.md`
- Control 2.7: Control 2.7: Data Residency and Cross-Border Data Flow Governance
  - File: `controls/pillar-2-security/2.7-data-residency.md`
- Control 2.6: Control 2.6: Copilot Web Search and Web Grounding Controls
  - File: `controls/pillar-2-security/2.6-web-search-controls.md`

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
--- +++ @@ -220,10 +220,4 @@ Related articles
 Microsoft Copilot requirements
 Get started with Microsoft Copilot
-Microsoft Copilot adoption site
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Microsoft Copilot adoption site
```

---

### 6. Microsoft 365 Copilot adoption guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.11: Control 1.11: Organizational Change Management and Adoption Planning
  - File: `controls/pillar-1-readiness/1.11-change-management-adoption.md`
- Control 1.12: Control 1.12: Training and Awareness Program
  - File: `controls/pillar-1-readiness/1.12-training-awareness.md`

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
--- +++ @@ -69,10 +69,4 @@ Copilot Prompt Gallery
 Configure a secure and governed data foundation for Microsoft Copilot
 Microsoft Copilot reports
-Manage Microsoft Copilot onboarding
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Manage Microsoft Copilot onboarding
```

---

### 7. Copilot Search admin experience

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -188,10 +188,4 @@ Don't use the same URL in different bookmarks. You get an error if you try to import a bookmark with a URL used in an existing one. This rule also applies to duplicate URLs in other types of answers.
 When updating existing bookmarks, use the bookmark ID column. You can update any other property of an existing bookmark, such as keyword or description, but you should make sure the bookmark ID is in the appropriate column of the import file. If the bookmark ID is present, it isn't treated as a new addition and isn't processed as an error.
 Video: Acronyms and bookmarks
-The following video is an overview of creating and managing acronyms and bookmarks in Microsoft Copilot search. It's 1 minute and 54 seconds long.
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+The following video is an overview of creating and managing acronyms and bookmarks in Microsoft Copilot search. It's 1 minute and 54 seconds long.
```

---

### 8. Secure and Govern Copilot blueprint

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -30,10 +30,4 @@ Microsoft Purview blueprint: Secure by default
 Microsoft Purview
 SharePoint Advanced Management
-Microsoft Zero Trust Assessment
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Microsoft Zero Trust Assessment
```

---

### 9. Configure secure and governed Copilot foundation

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot
**Section:** Copilot Administration
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
--- +++ @@ -30,10 +30,4 @@ Microsoft Purview blueprint: Secure by default
 Microsoft Purview
 SharePoint Advanced Management
-Microsoft Zero Trust Assessment
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Microsoft Zero Trust Assessment
```

---

### 10. Connect to xAI models

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -93,10 +93,4 @@ , and then choose
 Save
 .
-Once you disconnect SpaceXAI, users can't use SpaceXAI models. After completing the steps to disable SpaceXAI in Microsoft 365, it may take several hours for the service to be fully disabled for your users.
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Once you disconnect SpaceXAI, users can't use SpaceXAI models. After completing the steps to disable SpaceXAI in Microsoft 365, it may take several hours for the service to be fully disabled for your users.
```

---

### 11. Anthropic as a Microsoft subprocessor

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Section:** Copilot Administration
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.8: Control 1.8: Information Architecture Review
  - File: `controls/pillar-1-readiness/1.8-information-architecture-review.md`
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
--- +++ @@ -150,10 +150,4 @@ Understanding AI functionality and models in Microsoft Online Services
 Data, Privacy, and Security for Microsoft Copilot
 Overview of AI subprocessors in Microsoft Copilot
-Supplier Security & Privacy Assurance
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Supplier Security & Privacy Assurance
```

---

### 12. DLP for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`
- Control 2.1: Control 2.1: DLP Policies for Microsoft 365 Copilot Interactions
  - File: `controls/pillar-2-security/2.1-dlp-policies-for-copilot.md`
- Control 2.6: Control 2.6: Copilot Web Search and Web Grounding Controls
  - File: `controls/pillar-2-security/2.6-web-search-controls.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.5/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.5/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.5/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.1/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.6/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.6/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.6/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -127,7 +127,7 @@ Internal
 Public
 Personal
-They deploy Microsoft 365 Copilot and Copilot Chat to help users find and use Contoso enterprise information in their organization. They want to minimize the risk of General Data Protection Regulation (GDPR) data being included in Microsoft 365 Copilot and Copilot Chat summaries and also exclude private information from summaries. They create a DLP policy that uses the
+They deploy Microsoft 365 Copilot and Copilot Chat to help users find and use Contoso enterprise information in their organization. They want to exclude personal data and highly confidential information from Microsoft 365 Copilot and Copilot Chat summaries. They create a DLP policy that uses the
 Microsoft 365 Copilot and Copilot Chat
 policy location with the
 Content contains

```

---

### 13. Audit log activities

**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Section:** Audit and Retention
**Classification:** MEDIUM (General content update)

**Affected Controls:**
- Control 1.15: Control 1.15: SharePoint Permissions Drift Detection
  - File: `controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md`
- Control 3.1: Control 3.1: Copilot Interaction Audit Logging (Purview Unified Audit Log)
  - File: `controls/pillar-3-compliance/3.1-copilot-audit-logging.md`
- Control 2.2: Control 2.2: Sensitivity Labels and Copilot Content Classification
  - File: `controls/pillar-2-security/2.2-sensitivity-labels-classification.md`
- Control 2.13: Control 2.13: Plugin and Copilot Connector Security Governance
  - File: `controls/pillar-2-security/2.13-plugin-connector-security.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/4.14/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/4.15/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/verification-testing.md` (HIGH)
- ℹ️ `playbooks/control-implementations/3.1/powershell-setup.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.13/powershell-setup.md` (HIGH)
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
--- +++ @@ -597,6 +597,9 @@ Viewed setting
 ViewedSetting
 A setting value was viewed.
+Viewed user licenses
+ViewedUserLicenses
+User licenses were viewed.
 Dragon Copilot Web activities
 The following table lists user and application activities for Dragon Copilot Web recorded in the Microsoft 365 audit log. These events capture user access, clinical workflow actions, AI-assisted operations, and session lifecycle events performed within Dragon Copilot Web. Dragon Copilot Web supports clinical documentation workflows including ambient recording, transcript review, AI-assisted note generation, clinical chat, and EHR-integrated experiences.
 If your organization uses Dragon Copilot Web, you can search for these activities in Microsoft Purview Audit by selecting the appropriate activity name or by filtering on the Dragon Copilot record types. Audit records are emitted under the following record types:
@@ -1533,6 +1536,9 @@ Unassign Warehouse Server Alias
 UnassignWarehouseServerAlias
 A workspace administrator assigned a server alias to a Fabric Warehouse workspace.
+Viewed Workspace App
+ViewedWorkspaceApp
+Viewed Workspace App is generated when a user opens a Power BI workspace app.
 Workspace relations retrieved
 WorkspaceRelationsRetrieved
 Workspace relations retrieved.
@@ -2647,9 +2653,6 @@ Removed an automation rule
 AutomationRuleRemoved
 A user removed an automation rule.
-Triggered a generated playbook
-TriggerGeneratedPlaybook
-A user manually triggered a generated playbook.
 Microsoft Defender XDR case management activities
 The following table lists the case management activities that are logged in the Microsoft 365 audit log when users create and manage cases in the Microsoft Defender portal. For more information, see
 Microsoft Defender XDR

```

---

### 14. Copilot Cowork overview

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
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
--- +++ @@ -1,5 +1,15 @@ Copilot Cowork overview
 Microsoft Copilot Cowork can carry out tasks on your behalf. You describe what you need, and Cowork sends emails, schedules meetings, creates documents, posts in Teams, and manages your calendar. You approve each action before it happens.
+Note
+For users enrolled in the
+Frontier program
+, the tab options at the top of the left navigation might look different. To open Cowork, select the
+Home
+tab. The
+Chat
+and
+Cowork
+toggle appears in the conversation box. The default is the last choice you made.
 What is Cowork?
 Cowork carries out tasks across your Microsoft 365 environment. Rather than describing what you could do, it does the work.
 Sends emails
@@ -22,6 +32,10 @@ : Drafts stakeholder communications such as status updates and announcements.
 Schedules prompts
 : Runs prompts on a schedule so recurring tasks happen automatically.
+Builds on earlier work
+: Uses previous Copilot Chat conversations and Cowork tasks that you select as context for a new request. Learn how in
+Reference previous chats and tasks
+.
 Allows faculty and staff in the education industry to complete multi-step work across Microsoft 365
 : Prepares course materials, coordinates research and grant work, prepares materials for department or curriculum meetings, and other tasks.
 Create apps (Frontier)
@@ -102,10 +116,10 @@ This is a preview feature provided under
 Microsoft Product Terms
 .
-Preview features may have restricted functionality and may not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
+Preview features might have restricted functionality and might not be released for general availability. These features are available before an official release so that customers can get early access and provide feedback.
 You need to be part of the
 Frontier preview program
-to get early access. Frontier connects you directly with Mic
```

---

### 15. What's new in Copilot Cowork

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
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
--- +++ @@ -15,6 +15,19 @@ Feature
 Description
 Learn more
+Open Cowork in the
+Home
+tab (
+Frontier
+)
+Select the
+Home
+tab. The
+Chat
+and
+Cowork
+toggle appears in the conversation box.
+Copilot Cowork overview
 Accounting, Finance, and Capital Markets plugins
 Accounting for Cowork (Frontier Public), Finance for Cowork, and Capital Markets for Cowork add role-specific skills for accounting work, financial planning and modeling, and investment research and transaction materials.
 Role-based and industry plugins
@@ -28,10 +41,10 @@ Use projects in Copilot Cowork to keep related tasks, instructions, and context together. Start tasks from a project, return to related chats, and review the files those tasks produce.
 Use projects in Copilot Cowork
 Reference past chats and tasks
-Add a past chat or task to your prompt from
+Add previous Copilot Chat conversations and Cowork tasks to your prompt from
 Copilot
-in the context picker to give Cowork context from earlier work.
-Attach files
+in the context picker to build on earlier decisions and results.
+Reference previous chats and tasks
 Enhancements
 These updates expand the connectors and event-driven triggers you can use with Cowork.
 Feature

```

---

### 16. Copilot Cowork FAQ

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
--- +++ @@ -30,6 +30,10 @@ Quick daily catch-up, project status, Q&A, or drafting content
 Inbox and calendar clean-up, project launches, or meeting preparation.
 Copilot Chat helps you think through your work, supports fast, single-step inputs, and generates output for you to act on. Cowork helps you get work done by completing complex, coordinated actions across your apps, files, and data.
+Can I use a previous chat or task as context?
+Yes. You can select previous Copilot Chat conversations and Cowork tasks as context for a new request, so you can build on earlier decisions and results without restating them. Learn how in
+Reference previous chats and tasks
+.
 What skills does Cowork have?
 Cowork has built-in skills: Word, Excel, PowerPoint, PDF, Email, Scheduling, Calendar Management, Meetings, Daily Briefing, Enterprise Search, Communications, Deep Research, Adaptive Cards, and App (Frontier). The App skill lets you build lightweight, interactive apps in Cowork without writing code. You can also create your own custom skills by placing a
 SKILL.md
@@ -102,7 +106,7 @@ +
 ) >
 Skills
-. Plugins are also accessible in the Cowork mobile app if you set it up on your desktop.
+. You can also access plugins in the Cowork mobile app if you set it up on your desktop.
 From your browser at
 copilot.cloud.microsoft
 (desktop)
@@ -335,7 +339,7 @@ Auto
 and Cowork chooses the model that fits your task. To pick a specific model, select
 Auto
-in the compose box and choose from the list that your organization makes available. The choices include GPT 5.5, GPT 5.6, and GPT 6 variants, Claude Opus, Claude Sonnet, Claude Fable, and Grok 4.7. Model availability may vary based on tenant configuration. If your organization is within the
+in the compose box and choose from the list that your organization makes available. The choices include GPT 5.5, GPT 5.6, and GPT 6 variants, Claude Opus, Claude Sonnet, Claude Fable, and Grok 4.7. Model availability might vary based on tenant con
```

---

### 17. Discovery setting for AI experiences enabled by usage-based billing

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences
**Section:** Copilot Cowork
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -42,10 +42,4 @@ Related articles
 Set up usage-based billing for Copilot Credits
 Usage-Based Billing and Cost Management for Copilot Credits
-Cowork Usage report
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Cowork Usage report
```

---

### 18. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -216,10 +216,4 @@ .
 Monitor Copilot Credit spending
 Usage-based-billing guidance for CSPs, partner-managed customers, and MACC
-Understanding the user subscription license (USL) and usage-based billing (UBB)
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Understanding the user subscription license (USL) and usage-based billing (UBB)
```

---

### 19. Copilot Tuning admin guide

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-admin-guide
**Section:** Copilot Extensibility
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -174,10 +174,4 @@ Microsoft access to customer data
 Microsoft doesn't have default access to customer data used for tuning or stored at rest. Any access requires explicit customer approval through Customer Lockbox and is limited to approved support scenarios.
 Related content
-Copilot Tuning overview
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Copilot Tuning overview
```

---

### 20. Get ready for Copilot with SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management
**Section:** SharePoint Administration
**Classification:** MEDIUM (General content update)

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
--- +++ @@ -30,10 +30,4 @@ Microsoft Purview blueprint: Secure by default
 Microsoft Purview
 SharePoint Advanced Management
-Microsoft Zero Trust Assessment
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Microsoft Zero Trust Assessment
```

---

## HIGH: Control Review Recommended

### 1. Assign AI provider access to users and groups

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-ai-provider-user-sec-group-access
**Section:** Copilot Administration
**Classification:** HIGH (Portal references)

**What Changed:**
```diff
--- +++ @@ -27,10 +27,4 @@ This enforcement applies across:
 Microsoft Copilot apps
 Custom agents built in Copilot Studio
-Experiences managed through Power Platform admin center
-Was this page helpful?
-Yes
-No
-No
-Need help with this topic?
-Want to try using Ask Learn to clarify or guide you through this topic?+Experiences managed through Power Platform admin center
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
**Classification:** MEDIUM (General content update)

---

### 2. Microsoft 365 Copilot setup guide
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup
**Classification:** MEDIUM (General content update)

---

### 3. Manage Microsoft 365 Copilot
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access
**Classification:** MEDIUM (General content update)

---

### 4. Microsoft 365 Copilot requirements
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Classification:** MEDIUM (General content update)

---

### 5. Data, privacy, and security for Microsoft 365 Copilot
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy
**Classification:** MEDIUM (General content update)

---

### 6. Microsoft 365 Copilot adoption guide
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources
**Classification:** MEDIUM (General content update)

---

### 7. Copilot Search admin experience
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience
**Classification:** MEDIUM (General content update)

---

### 8. Manage Copilot Search
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage
**Classification:** MEDIUM (General content update)

---

### 9. Secure and Govern Copilot blueprint
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance
**Classification:** MEDIUM (General content update)

---

### 10. Configure secure and governed Copilot foundation
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot
**Classification:** MEDIUM (General content update)

---

### 11. Connect to xAI models
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models
**Classification:** MEDIUM (General content update)

---

### 12. Anthropic as a Microsoft subprocessor
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor
**Classification:** MEDIUM (General content update)

---

### 13. Audit log activities
**URL:** https://learn.microsoft.com/en-us/purview/audit-log-activities
**Classification:** MEDIUM (General content update)

---

### 14. Discovery setting for AI experiences enabled by usage-based billing
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/discovery-setting-ai-experiences
**Classification:** MEDIUM (General content update)

---

### 15. Manage Copilot Credits (usage-based billing)
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Classification:** MEDIUM (General content update)

---

### 16. Copilot Tuning admin guide
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-admin-guide
**Classification:** MEDIUM (General content update)

---

### 17. Get ready for Copilot with SharePoint Advanced Management
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management
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