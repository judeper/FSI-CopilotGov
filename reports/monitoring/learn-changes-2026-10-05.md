# Microsoft Learn Documentation Changes

**Run Date:** 2026-10-05
**Run Time:** 2026-10-05T18:57:15.819316+00:00
**Total URLs Checked:** 176

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| MEDIUM Changes | 1 |
| Redirects | 4 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | microsoft-365-copilot-requirements | MEDIUM | 1.1, 1.9, 2.15, 1.4 | Update portal-walkthrough |
| 2 | ...osoft365-copilot-location-learn-about | HIGH | 1.5, 2.6, 2.1 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. Microsoft 365 Copilot requirements

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
--- +++ @@ -155,9 +155,11 @@ Copilot integrations can fail when a network perimeter blocks WSS, a network device performs Transport Layer Security inspection that interferes with the connection, or a proxy enforces aggressive connection timeouts.
 Work with the teams that manage network security, proxies, firewalls, secure web gateways, or SSE/SASE services to allow the required traffic. You can test connectivity to the
 *.cloud.microsoft
-domain by using the
-Microsoft 365 network connectivity test
-.
+domain by using either the
+connectivity test for the Copilot app
+. You can also use the
+Microsoft 365 connectivity test tool
+for broader Microsoft products and service.
 Wildcards, FQDNs, and subdomains
 Where Microsoft 365 network guidance specifies a wildcard, allow the wildcard and its required subdomains. Microsoft 365 services are dynamic and don't provide a fixed list of individual fully qualified domain names for every Copilot feature and scenario.
 Secure and governed foundation

```

---

### 2. DLP for Microsoft 365 Copilot

**URL:** https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.5: Control 1.5: Sensitivity Label Taxonomy Review for Copilot
  - File: `controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md`
- Control 2.6: Control 2.6: Copilot Web Search and Web Grounding Controls
  - File: `controls/pillar-2-security/2.6-web-search-controls.md`
- Control 2.1: Control 2.1: DLP Policies for Microsoft 365 Copilot Interactions
  - File: `controls/pillar-2-security/2.1-dlp-policies-for-copilot.md`

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
--- +++ @@ -1,11 +1,11 @@-Learn about using Microsoft Purview Data Loss Prevention to protect interactions with Microsoft 365 Copilot and Copilot Chat
-Microsoft Purview Data Loss Prevention (DLP) can help you protect interactions with Microsoft 365 Copilot and Copilot Chat in the following ways:
-Restrict Microsoft 365 Copilot from using external web search when prompts contain sensitive data.
-You can use DLP policies to prevent Microsoft 365 Copilot and Copilot Chat from sending sensitive information to external web services. When a prompt contains sensitive information types (SITs)âsuch as credit card numbers, passport numbers, Social Security numbers, or custom SITs defined by your organizationâCopilot automatically blocks the use of external web search as a grounding source for that prompt. Instead, Copilot continues to generate responses using permitted internal Microsoft 365 data sources. This ensures that sensitive data remains protected and isn't shared with external search providers.
-Restrict Microsoft 365 Copilot and Copilot Chat from processing sensitive prompts.
-You can create a DLP policy to help protect against the use of sensitive information types (SITs), such as credit card numbers, passport numbers, or Social Security numbers in Microsoft 365 Copilot prompts. This includes Microsoft-provided SITs and custom SITs that you create. This real-time control helps organizations reduce data leakage and oversharing risks. It prevents Microsoft 365 Copilot and Copilot Chat from returning a response when prompts contain sensitive data and from using that sensitive data for both internal and external web searches.
-Restrict Microsoft 365 Copilot and Copilot Chat from processing sensitive files and emails.
-You can create a DLP policy to prevent Microsoft 365 Copilot and Copilot Chat from using files and emails that have sensitivity labels when generating responses.
+Learn about using Microsoft Purview Data Loss Prevention to protect interactions with M
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Microsoft 365 Copilot requirements
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-requirements
**Classification:** MEDIUM (General content update)

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