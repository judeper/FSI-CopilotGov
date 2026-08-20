# Microsoft Learn Documentation Changes

**Run Date:** 2026-08-20
**Run Time:** 2026-08-20T10:19:43.605265+00:00
**Total URLs Checked:** 165

---

## Executive Summary

| Category | Count |
|----------|-------|
| CRITICAL Changes | 2 |
| MEDIUM Changes | 2 |
| Redirects | 15 |

---

## Change Summary (Quick Scan)

| # | URL | Classification | Affected Controls | Action Required |
|---|-----|----------------|-------------------|-----------------|
| 1 | dlp-policy-tips-reference | HIGH | 2.1 | Update portal-walkthrough |
| 2 | ...m/en-us/microsoft-365/copilot/cowork/ | MEDIUM | None | Review optional |
| 3 | agent-builder-build-agents | MEDIUM | None | Review optional |
| 4 | overview | HIGH | 1.13, 2.3 | Update portal-walkthrough |

---

## CRITICAL: Playbook Updates Required

These changes affect step-by-step procedures and must be addressed.

### 1. DLP policy tips reference

**URL:** https://learn.microsoft.com/en-us/purview/dlp-policy-tips-reference
**Section:** Data Loss Prevention (DLP)
**Classification:** HIGH (Compliance features)

**Affected Controls:**
- Control 2.1: Control 2.1: DLP Policies for Microsoft 365 Copilot Interactions
  - File: `controls/pillar-2-security/2.1-dlp-policies-for-copilot.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/2.1/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.1/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.1/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.1/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -99,18 +99,24 @@ Outlook for Microsoft 365 (ver. 2105 build 14026.20000 and semi-annual channel ver. 2102 build 13801.20862)
 Varies by version and license. See
 Data loss prevention policy tip reference for Outlook for Microsoft 365
-Subset.See
+Subset. See
 Data loss prevention policy tip reference for Outlook for Microsoft 365
 For full details, see
 Data loss prevention policy tip reference for Outlook for Microsoft 365
-Outlook Mobile (iOS, Android)/Outlook Mac
-None
-None
-DLP policy tips aren't supported on Outlook mobile
+Outlook Mobile (iOS, Android)
+Varies by version and license. See
+Data loss prevention policy tip reference for Outlook for Microsoft 365
+Subset. See
+Data loss prevention policy tip reference for Outlook for Microsoft 365
+For full details, see
+Data loss prevention policy tip reference for Outlook for Android, iOS, and macOS
 Outlook Mac
-None
-None
-DLP policy tips are not supported on Outlook for Mac
+Varies by version and license. See
+Data loss prevention policy tip reference for Outlook for Microsoft 365
+Subset. See
+Data loss prevention policy tip reference for Outlook for Microsoft 365
+For full details, see
+Data loss prevention policy tip reference for Outlook for Android, iOS, and macOS
 SharePoint/OneDrive Web client
 All.
 All.

```

---

### 2. Microsoft Agent 365 overview

**URL:** https://learn.microsoft.com/en-us/microsoft-agent-365/overview
**Section:** Agent Governance
**Classification:** HIGH (Portal references)

**Affected Controls:**
- Control 1.13: Control 1.13: Extensibility Readiness (Copilot Connectors, Plugins, Declarative Agents)
  - File: `controls/pillar-1-readiness/1.13-extensibility-readiness.md`
- Control 2.3: Control 2.3: Conditional Access Policies for Copilot Workloads
  - File: `controls/pillar-2-security/2.3-conditional-access-policies.md`

**Affected Playbooks:**
- ⚠️ `playbooks/control-implementations/1.13/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/1.13/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/1.13/verification-testing.md` (HIGH)
- ⚠️ `playbooks/control-implementations/2.3/portal-walkthrough.md` (CRITICAL)
- ℹ️ `playbooks/control-implementations/2.3/powershell-setup.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.3/troubleshooting.md` (HIGH)
- ℹ️ `playbooks/control-implementations/2.3/verification-testing.md` (HIGH)

**What Changed:**
```diff
--- +++ @@ -33,9 +33,7 @@ Microsoft Agent 365 gives organizations real-time visibility into their agentic environment, helping admins understand how agents are used, identify performance or risk signals early, and take action before issues impact the business. Admins can now view all their agents in a single, centralized registry providing a unified view of agent adoption, activity, and agent health. These insights help leaders and AI admins stay in control, operate efficiently, and maximize the value of their agent investments from a centralized AI admin experience. Role-specific oversight extends this visibility to security and business leaders, ensuring the right stakeholders have the tailored insights they need to manage risk and measure agent value within their domains. Learn more:
 Agent registry
 ,
-Registry sync
-,
-Agent Map
+Agent map
 .
 Govern
 Establish consistent guardrails for AI agents by centralizing lifecycle management, access control, and compliance across the enterprise. Through the Agent 365 registry in the Microsoft 365 admin center, Microsoft Entra, and Microsoft Purview, admins can intentionally manage the lifecycle of their organizationâs agents while ensuring the right permissions, policies, and reviews are in place. Together, these controls help organizations reduce risk, stay audit-ready, and ensure agents remain aligned with organizational policies and business needs. Learn more:
@@ -43,15 +41,15 @@ .
 Secure
 Microsoft Agent 365 delivers endâtoâend protection for every agent by extending Microsoftâs enterpriseâgrade identity, data, and threatâdefense capabilities across your AI ecosystem. Microsoft Entra enforces consistent, riskâbased access controls for users and agents acting on their behalf, while Microsoft Purview provides deep visibility into data risks with information protection, DLP, and risk safeguards. Microsoft Defender adds continuous threat detection and realâtime protection to block unsafe behaviors and m
```

---

## MEDIUM: Minor Changes (Review Optional)

### 1. Copilot Cowork overview
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
**Classification:** MEDIUM (General content update)

---

### 2. Build agents with Agent Builder
**URL:** https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents
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
| https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry | https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms |
| https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management | https://learn.microsoft.com/en-us/microsoft-365/copilot/get-ready-copilot-sharepoint-advanced-management |

---

## Errors

No errors detected.

---

*Generated by `scripts/learn_monitor.py` (unified monitoring framework)*