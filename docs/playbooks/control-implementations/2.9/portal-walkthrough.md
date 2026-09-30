# Control 2.9: Defender for Cloud Apps — Copilot Session Controls — Portal Walkthrough

Step-by-step portal configuration for deploying Microsoft Defender for Cloud Apps session controls to monitor and govern browser-based Microsoft 365 sessions used alongside Copilot.

## Prerequisites

- Microsoft Defender for Cloud Apps license for each protected user
- Security Administrator or Cloud App Security Administrator role
- Conditional Access integration configured
- Understanding of session control capabilities

## Steps

### Step 1: Enable Conditional Access App Control

**Portal:** Microsoft Defender portal
**Path:** Settings > Cloud Apps > Connected apps > Conditional Access App Control apps

Enable Conditional Access App Control for the Microsoft 365 web apps your Copilot users rely on. This allows Defender for Cloud Apps to proxy supported browser sessions and apply real-time controls.

Verify Microsoft 365 appears in the connected apps list with "Enabled" status.

### Step 2: Create Session Policy for Copilot Monitoring

**Portal:** Microsoft Defender for Cloud Apps
**Path:** Defender > Policies > Policy Management > Create Policy > Session Policy

Create a session policy targeting the browser-based Microsoft 365 activity you need to govern:
- **Policy name:** "FSI Copilot Session Validation" for a first-pass routing check, then a separate "FSI Copilot Sensitive Session Audit" policy for detailed monitoring
- **Session control type:** Start with **Monitor only** to validate redirection, then use **Block activities** or **Control file download/upload (with inspection)** for detailed monitoring
- **Filters:** Select the onboarded Microsoft 365 web apps in scope and, where needed, activity types such as printing, clipboard actions, sending, sharing, or editing in supported apps
- **Actions:** Use **Audit** first for detailed policies; add **Block**, **Protect**, or **Require step-up authentication** only after validation

### Step 3: Configure Content Inspection for Copilot Sessions

**Portal:** Microsoft Defender for Cloud Apps
**Path:** Defender > Policies > [Session Policy] > Content Inspection

Enable content inspection on the detailed session policies to detect sensitive data in supported browser-session actions:
- Enable DLP or malware inspection for the selected session control type
- Select sensitive information types, sensitivity labels, or classifier conditions relevant to FSI (for example, SSNs, account numbers, or confidential labels)
- Configure actions appropriate to the policy type: **Audit**, **Block**, **Protect**, or **Require step-up authentication**

### Step 4: Set Up Real-Time Alerts

**Portal:** Microsoft Defender for Cloud Apps
**Path:** Defender > Policies > Alert Policies

Configure alerts for the routed web-session events and anomaly detections that matter most:
- Sensitive content detected during supported file download, upload, or send/share actions
- Policy violation attempts in routed browser sessions
- Impossible travel or activity from infrequent country/region after the anomaly-detection learning period
- Malware detection for supported file transfers **after you explicitly enable the built-in malware policy, which Microsoft documents as disabled by default**

### Step 5: Configure Activity Logging

**Portal:** Microsoft Defender portal
**Path:** Defender portal > Cloud Apps > Investigate > Activity Log

Verify that redirected sign-ins and monitored browser-session actions appear in the policy report or activity log. Configure log retention and export settings for compliance documentation. Use Microsoft Purview audit for prompt/response-level Copilot interaction evidence rather than expecting MDCA to expose per-prompt telemetry.

### Step 6: Review Generative AI App Catalog

**Portal:** Microsoft Defender portal
**Path:** Cloud apps > Cloud app catalog, then Cloud apps > Cloud discovery > Discovered apps

1. Navigate to the Cloud app catalog and select the **Generative AI** category filter to display the 1,000+ generative AI apps cataloged by Microsoft
2. Review the cloud app catalog risk scores and note any apps that warrant closer governance review
3. Open **Cloud discovery > Discovered apps** and filter by **Generative AI** to identify the AI apps actually observed in your environment
4. Assess risk scores for any generative AI apps employees are using — high-risk apps may represent Shadow AI usage that exposes customer or financial data
5. For prohibited apps: mark them as **Unsanctioned** and use the supported governance stream (such as Microsoft Defender for Endpoint) or a generated block script to enforce blocking
6. For approved apps: mark them as **Sanctioned** if that tag is part of your governance model, and document the review cadence

**Recommended governance workflow:**
- Monthly: Review newly discovered generative AI apps and assess risk scores
- Quarterly: Update the sanctioned/unsanctioned app list and review block policies

### Step 7: Configure Agent Threat Detection

**Portal:** Microsoft Defender portal (security.microsoft.com)
**Path:** Defender portal > Settings > Security for AI > Get started; agent inventory at Assets > AI agents

1. Confirm the tenant holds a Microsoft Agent 365-eligible license using the [Control 2.9 qualifying-license guidance](../../../controls/pillar-2-security/2.9-defender-cloud-apps.md#agent-365-qualifying-license-guidance); Microsoft 365 E5 is not an exclusive prerequisite. Complete Agent 365 onboarding — required as of July 1, 2026 for Copilot Studio and Microsoft Foundry agent threat-detection coverage
2. On the **Security for AI > Get started** page, confirm the **Security for AI Agents** toggle is enabled. For Copilot Studio real-time protection, copy the onboarding URL from Defender and send it to the Power Platform administrator; after they complete the Power Platform configuration, obtain the App ID from them, paste it into Defender, and save the connection.
3. Verify that your Copilot Studio agents and any Microsoft 365 agents surfaced by Defender inventory appear in **Assets > AI agents** with a current risk level
4. Navigate to Incidents & alerts and filter for agent-related incidents to confirm detection is operational
5. Under **Settings > Security for AI > Policies & rules > Real-time protection**, review the built-in **Default** audit rule and create agent-scoped custom rules for documented detection types that require blocking. Use Advanced Hunting telemetry to create custom detections and downstream automation for organization-specific anomalous behavior.
6. Integrate agent threat alerts into your SIEM or Microsoft Sentinel workspace for correlation with user activity

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Validate browser-session redirection, configure basic alerting, review the generative AI catalog monthly, and enable agent monitoring alerts in Microsoft Defender for supported agent deployments (requires Microsoft Agent 365 license where applicable) |
| **Recommended** | Add content inspection with DLP or malware integration, review Cloud Discovery generative AI usage, and configure custom agent anomaly detection or hunting rules |
| **Regulated** | Full supported browser-session control with blocking or step-up authentication, SIEM integration for MDCA and Purview evidence, agent threat detection in SOC playbooks, and quarterly Shadow AI governance review with sanctioned/unsanctioned app list |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for session control automation
- See [Verification & Testing](verification-testing.md) to validate session controls
- Review Control 2.3 for Conditional Access integration
- Back to [Control 2.9](../../../controls/pillar-2-security/2.9-defender-cloud-apps.md)
