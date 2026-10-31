# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-31
**Run Time:** 2026-10-31T15:32:12.004967+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 8 |
| MEDIUM Changes | 1 |
| Redirects | 23 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-requirements | HIGH | 1.1, 1.9, 2.15, 1.4 | Update portal-walkthrough |
| 2 | ...ilot-foundational-deployment-guidance | MEDIUM | 1.2 | Update portal-walkthrough |
| 3 | ...data-foundation-microsoft-365-copilot | CRITICAL | 1.7 | Update portal-walkthrough |
| 4 | apply-sensitivity-label-automatically | HIGH | 1.5, 2.2 | Update portal-walkthrough |
| 5 | ...-based-billing-manage-copilot-credits | HIGH | 4.15, 1.9, 4.8 | Update portal-walkthrough |
| 6 | advanced-management | HIGH | 1.7, 2.5 | Update portal-walkthrough |
| 7 | ...opilot-sharepoint-advanced-management | CRITICAL | 1.3, 1.13 | Update portal-walkthrough |
| 8 | restricted-content-discovery | HIGH | 1.7, 1.4, 1.3, 1.2, 1.13, 2.5 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot requirements

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Section:** Copilot Administration
**Classification:** HIGH (Policy language)

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
--- +++ @@ -181,9 +181,7 @@ Wildcards, FQDNs, and subdomains
 Where Microsoft 365 network guidance specifies a wildcard, allow the wildcard and its required subdomains. Microsoft 365 services are dynamic and don't provide a fixed list of individual fully qualified domain names for every Copilot feature and scenario.
 Secure and governed foundation
-Although not required, it's strongly recommended to
-configure a secure and governed foundation for Microsoft Copilot
-. When your organization's data is well governed, current, and appropriately shared, Copilot can deliver accurate, relevant, and secure responses. By using SharePoint Advanced Management and Microsoft Purview capabilities, you can:
+Although not required, it's strongly recommended to configure a secure and governed foundation for Microsoft Copilot. When your organization's data is well governed, current, and appropriately shared, Copilot can deliver accurate, relevant, and secure responses. By using SharePoint Advanced Management and Microsoft Purview capabilities, you can:
 Remediate oversharing
 Set up guardrails to protect data by default
 Meet AI regulations and regulatory requirements

```

---

### 2. Secure and Govern Copilot blueprint

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
--- +++ @@ -7,9 +7,6 @@ Set up guardrails
 Meet regulations
 https://aka.ms/Copilot/SecureGovernBlueprintPDF
-For a more detailed walkthrough of these steps, see
-Configure a secure and governed foundation for Microsoft Copilot
-.
 What the blueprint covers
 The blueprint covers the following areas:
 A practical framework to reduce Copilot exposure quickly, then harden your environment with enforceable defaults
@@ -30,7 +27,6 @@ -
 PowerPoint
 Related guidance
-Configure a secure and governed foundation for Microsoft Copilot
 Microsoft Purview blueprint: Secure by default
 Microsoft Purview
 SharePoint Advanced Management

```

---

### 3. Configure secure and governed Copilot foundation

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot
**Section:** Copilot Administration
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
--- +++ @@ -1,183 +1,36 @@-Configure a secure and governed foundation for Microsoft Copilot
-Applies to: Microsoft Copilot, Microsoft Purview, and SharePoint Advanced Management
-Microsoft Copilot
-uses Work IQ to enhance responses to user prompts using data that the user already has permission to access. When your organization's data is well governed, current, and appropriately shared, Copilot can deliver accurate, relevant, and secure responses.
-This article walks through the steps of preparing, securing, and managing Microsoft Copilot using the process described in the
-Foundational deployment blueprint
-.
-By following these steps, you can help Copilot deliver accurate and relevant results while supporting your organization's security, compliance, and regulatory requirements.
-This guidance is intended for IT administrators and security administrators who are either preparing their organization for Microsoft Copilot or making necessary adjustments to security and governance controls after Copilot is enabled.
-What this article helps you achieve
-By completing the steps in this article, you can:
-Establish guardrails to ensure that users have appropriate access to SharePoint, OneDrive, and Exchange, and that Copilot only references accurate, up-to-date information in line with your organization's policies
-Make informed choices about how Copilot can and can't interact with your organization's sensitive data, ensuring control and flexibility in data usage and access
-Monitor changes and Copilot activity to identify and remediate risk.
-Licensing
-The capabilities described in this article require:
-A license for Microsoft Copilot. See
-Copilot licensing requirements
-.
+Secure and govern Microsoft Copilot: Foundational deployment guidance
+Microsoft Copilot can accelerate how people find information, summarize content, and get work done by grounding responses in the data users already have permission to access. To realize that value confidently, organizations req
```

---

### 4. Apply sensitivity labels automatically

**URL:** https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically
**Section:** Information Protection (Sensitivity Labels)
**Classification:** HIGH (Portal references)

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
--- +++ @@ -49,7 +49,7 @@ How to configure auto-labeling policies for SharePoint, OneDrive, and Exchange
 , and
 Use PowerShell for auto-labeling policies
-to target up to 50,000 SharePoint sites by using an adaptive scope.
+to target SharePoint sites by using an adaptive scope.
 Auto-labeling isn't available in my region.
 The
 Auto-labeling
@@ -100,7 +100,7 @@ Maximum of 100 auto-labeling policies per tenant. In the portal, each policy can target up to 1,000 explicitly included or excluded SharePoint sites, or up to 100 explicitly included or excluded OneDrive individual users or groups. If you keep the default configuration of
 All
 , this configuration is exempt from these maximums.
-For SharePoint, an auto-labeling policy can use an adaptive scope to target up to 50,000 sites. For configuration instructions, see
+For SharePoint, an auto-labeling policy can use an adaptive scope to target sites. For configuration instructions, see
 Use PowerShell for auto-labeling policies
 .
 Existing values for modified, modified by, and the date aren't changed as a result of auto-labeling policiesâfor both simulation mode and when labels are applied.
@@ -780,7 +780,7 @@ All
 included but specify users or groups to exclude, email that these excluded users send will be exempt from the policy, but not email that they receive.
 For the OneDrive location, you must specify users or groups. Previously, you had to specify sites by URLs. Any existing OneDrive URL sites in auto-labeling policies will continue to work but before you can specify new OneDrive locations, or for restricted admins, you must first delete any existing site URLs. Groups supported: distribution groups, Microsoft 365 groups, mail-enabled security groups, and security groups.
-For the SharePoint location, you can explicitly select up to 1,000 individual sites. To dynamically target up to 50,000 sites, use a
+For the SharePoint location, you can explicitly select up to 1,000 individual sites. To dynamically targe
```

---

### 5. Manage Copilot Credits (usage-based billing)

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
**Section:** Copilot Cowork
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -1,14 +1,9 @@ Managing AI experiences enabled by usage-based billing
 Use spending policies in the Cost Management dashboard to control access and Copilot Credit spending for AI experiences enabled by usage-based billing.
-Administrators can:
-Create spending policies that control access to supported agents and services.
-Automatically apply existing spending policies to future supported services and agents.
-Configure organizational and user-level spending limits.
-Configure threshold notifications for administrators and users.
-Assign billing methods.
 For initial configuration and billing options, see
 Set up usage-based billing for Copilot Credits
-. To review consumption, see
+.
+To review consumption, see
 Monitor Copilot Credit spending
 .
 Important
@@ -36,7 +31,8 @@ Before you create additional spending policies, complete the initial usage-based billing setup and activate the default spending policy. For more information, see
 Getting started with usage-based billing
 .
-Add spending policy
+Add Identity-based spending policy
+Use this option when you want a policy to apply to the people who use selected agents and services. For example, a group using Cowork.
 In the Microsoft 365 admin center, go to
 Copilot > Cost Management
 .
@@ -53,10 +49,12 @@ Set limits and alerts
 Select a billing method
 Review and add the policy
-Define the policy scope
+Policy scope
 The system supports user, group, and tenant policies.
 Give the policy a name and select the specific groups that the policy applies to.
-Create and name the policy.
+Create and name the policy and then choose
+Identity
+as the scope. Use this option when you need to manage usage by users or groups for a supported service.
 Select the users or groups to which the policy applies. By default,
 All users
 is selected. To target this rule to a subset of users, switch to
@@ -140,7 +138,7 @@ You're notified that the spending policy is created. Select
 Done
 . The spending policy now shows up in 
```

---

### 6. SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/sharepoint/advanced-management
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

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
--- +++ @@ -5,9 +5,6 @@ Manage the content lifecycle
 ; and
 Prevent oversharing
-.
-SAM capabilities are helpful as organizations
-prepare for Microsoft Copilot and agents
 .
 Video: SharePoint Advanced Management overview
 Watch the following video to get an overview of SharePoint Advanced Management:
@@ -84,7 +81,6 @@ .
 Related articles
 SharePoint Admin Agent
-Get ready for Microsoft Copilot and Agents with SharePoint Advanced Management
 Configure a secure and governed foundation for Microsoft Copilot
 SharePoint Advanced Management features in Microsoft Copilot licenses
 Was this page helpful?

```

---

### 7. Get ready for Copilot with SharePoint Advanced Management

**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management
**Section:** SharePoint Administration
**Classification:** CRITICAL (Deprecation notice)

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
--- +++ @@ -1,183 +1,36 @@-Configure a secure and governed foundation for Microsoft Copilot
-Applies to: Microsoft Copilot, Microsoft Purview, and SharePoint Advanced Management
-Microsoft Copilot
-uses Work IQ to enhance responses to user prompts using data that the user already has permission to access. When your organization's data is well governed, current, and appropriately shared, Copilot can deliver accurate, relevant, and secure responses.
-This article walks through the steps of preparing, securing, and managing Microsoft Copilot using the process described in the
-Foundational deployment blueprint
-.
-By following these steps, you can help Copilot deliver accurate and relevant results while supporting your organization's security, compliance, and regulatory requirements.
-This guidance is intended for IT administrators and security administrators who are either preparing their organization for Microsoft Copilot or making necessary adjustments to security and governance controls after Copilot is enabled.
-What this article helps you achieve
-By completing the steps in this article, you can:
-Establish guardrails to ensure that users have appropriate access to SharePoint, OneDrive, and Exchange, and that Copilot only references accurate, up-to-date information in line with your organization's policies
-Make informed choices about how Copilot can and can't interact with your organization's sensitive data, ensuring control and flexibility in data usage and access
-Monitor changes and Copilot activity to identify and remediate risk.
-Licensing
-The capabilities described in this article require:
-A license for Microsoft Copilot. See
-Copilot licensing requirements
-.
+Secure and govern Microsoft Copilot: Foundational deployment guidance
+Microsoft Copilot can accelerate how people find information, summarize content, and get work done by grounding responses in the data users already have permission to access. To realize that value confidently, organizations req
```

---

### 8. Restricted Content Discovery

**URL:** https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery
**Section:** SharePoint Administration
**Classification:** HIGH (Feature availability)

**Affected Controls:**
- Control 1.7: Control 1.7: SharePoint Advanced Management Readiness for Copilot
  - File: `controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md`
- Control 1.4: Control 1.4: Semantic Index Governance and Scope Control
  - File: `controls/pillar-1-readiness/1.4-semantic-index-governance.md`
- Control 1.3: Control 1.3: Restricted SharePoint Search Configuration
  - File: `controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md`
- Control 1.2: Control 1.2: SharePoint Oversharing Detection and Remediation (DSPM for AI)
  - File: `controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md`
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.5: Control 2.5: Data Minimization and Grounding Scope
  - File: `controls/pillar-2-security/2.5-data-minimization-grounding-scope.md`

**Affected Playbooks:**
- ℹ️ `playbooks/control-implementations/1.4/troubleshooting.md` (HIGH)
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
--- +++ @@ -119,9 +119,9 @@ How long does it take for updates to Restricted Content Discovery to take effect?
 Restricted Content Discovery is a site-level property. Index update latency is highly dependent on the number of items in the site and the number of sites getting updated at the same time. For sites with more than 500,000 items, an update to Restricted Content Discovery could take more than a week to fully process and reflect in search and Copilot experiences.
 How does Restricted Content Discovery fit into a Copilot readiness strategy?
-Restricted Content Discovery helps organizations temporarily limit discovery of selected sites while permissions, ownership, and governance controls are reviewed. It's one component of a broader SharePoint governance and Copilot readiness strategy. See the following resources:
+Restricted Content Discovery helps organizations temporarily limit discovery of selected sites while permissions, ownership, and governance controls are reviewed. It's one component of a broader SharePoint governance and Copilot readiness strategy. See
 Secure and govern Microsoft Copilot: Foundational deployment guidance
-Get ready for Microsoft Copilot and agents with SharePoint Advanced Management
+.
 Next steps
 Review
 Data access governance reports for SharePoint and OneDrive sites

```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Secure and Govern Copilot blueprint
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance
**Classification:** MEDIUM (General content update)

---

## URL Redirects Detected

Consider updating microsoft-learn-urls.md:

| Original URL | Redirects To |
|--------------|--------------|
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-setup | https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-enablement-resources | https://learn.microsoft.com/en-us/microsoft-365/copilot/enablement-resources |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-admin-experience | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-admin-experience |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-search-manage | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-search-manage |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot | https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ | https://learn.microsoft.com/en-us/copilot/cowork/ |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new | https://learn.microsoft.com/en-us/copilot/cowork/whats-new |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/get-started | https://learn.microsoft.com/en-us/copilot/cowork/get-started |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance | https://learn.microsoft.com/en-us/copilot/cowork/cowork-admin-governance |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models | https://learn.microsoft.com/en-us/copilot/cowork/cowork-models |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-manage-plugins | https://learn.microsoft.com/en-us/copilot/cowork/cowork-manage-plugins |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq | https://learn.microsoft.com/en-us/copilot/cowork/cowork-faq |
| https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report | https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/cowork-usage-report?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/managed-apps/index | https://learn.microsoft.com/en-us/microsoft-365/managed-apps/?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-365-overview?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-settings?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?view=o365-worldwide | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps?view=o365-worldwide |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agents-are-apps | https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview |
| https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*