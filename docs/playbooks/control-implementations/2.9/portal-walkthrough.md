# Control 2.9: Defender for Cloud Apps — Copilot Session Controls — Portal Walkthrough

Step-by-step portal configuration for deploying Microsoft Defender for Cloud Apps session controls to monitor and govern Copilot interactions.

## Prerequisites

- Microsoft Defender for Cloud Apps license (included in M365 E5)
- Security Administrator or Cloud App Security Administrator role
- Conditional Access integration configured
- Understanding of session control capabilities

## Steps

### Step 1: Enable Conditional Access App Control

**Portal:** Microsoft Defender for Cloud Apps
**Path:** Defender > Settings > Conditional Access App Control > Connected Apps

Enable Conditional Access App Control for Microsoft 365 applications. This allows Defender for Cloud Apps to proxy Copilot-related sessions and apply real-time controls.

Verify Microsoft 365 appears in the connected apps list with "Enabled" status.

### Step 2: Create Session Policy for Copilot Monitoring

**Portal:** Microsoft Defender for Cloud Apps
**Path:** Defender > Policies > Policy Management > Create Policy > Session Policy

Create a session policy targeting Copilot interactions:
- **Policy name:** "FSI Copilot Session Monitoring"
- **Session control type:** Monitor all activities
- **Filters:** App equals Microsoft 365; Activity type includes file operations and content interactions
- **Actions:** Log and alert on sensitive content activities

### Step 3: Configure Content Inspection for Copilot Sessions

**Portal:** Microsoft Defender for Cloud Apps
**Path:** Defender > Policies > [Session Policy] > Content Inspection

Enable content inspection to detect sensitive data in Copilot sessions:
- Enable DLP content inspection
- Select sensitive information types relevant to FSI (SSN, account numbers)
- Configure actions: Block download, apply watermark, or alert on detection

### Step 4: Set Up Real-Time Alerts

**Portal:** Microsoft Defender for Cloud Apps
**Path:** Defender > Policies > Alert Policies

Configure alerts for Copilot-related security events:
- Unusual volume of Copilot interactions from a single user
- Copilot access from risky locations or devices
- Sensitive content detected in Copilot sessions
- Policy violation attempts

### Step 5: Configure Activity Logging

**Portal:** Microsoft Defender portal
**Path:** Defender portal > Cloud Apps > Investigate > Activity Log

Verify that Copilot-related activities appear in the activity log. Configure log retention and export settings for compliance documentation. Activity logs provide the evidence trail for regulatory examinations.

### Step 6: Review Generative AI App Catalog

**Portal:** Microsoft Defender portal
**Path:** Defender portal > Cloud Apps > Cloud app catalog

1. Navigate to the Cloud app catalog and select the **Generative AI** category filter to display the 1,000+ generative AI apps cataloged by Microsoft
2. Review apps that appear in your organization's discovered traffic (shown with a "Discovered" indicator)
3. Assess risk scores for any generative AI apps employees are using — high-risk apps may represent Shadow AI usage that exposes customer or financial data
4. For high-risk apps: create an access policy to block the app or mark it as "Unsanctioned" to automatically generate a block script for deployment to your web proxy or firewall
5. For sanctioned apps (including Microsoft 365 Copilot): mark as "Sanctioned" to exclude from Shadow AI alerts

**Recommended governance workflow:**
- Monthly: Review newly discovered generative AI apps and assess risk scores
- Quarterly: Update the sanctioned/unsanctioned app list and review block policies

### Step 7: Configure Agent Threat Detection

**Portal:** Microsoft Defender portal (security.microsoft.com)
**Path:** Defender portal > Settings > Endpoints > Detection rules OR Incidents & alerts

1. Verify that agent-related detection rules are active for your Copilot agent deployments (Copilot Studio agents, SharePoint agents)
2. Navigate to Incidents & alerts and filter for agent-related incidents to confirm detection is operational
3. Configure custom detection rules for agent anomalies specific to your organization:
   - Alerts when an agent accesses data outside its configured knowledge source scope
   - Alerts when agent interaction volume significantly exceeds baseline
4. Integrate agent threat alerts into your SIEM or Microsoft Sentinel workspace for correlation with user activity

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Enable session monitoring for Copilot interactions; configure basic alerting; enable agent monitoring alerts in Defender XDR |
| **Recommended** | Content inspection with DLP integration; real-time alerts for sensitive data; review generative AI app catalog monthly for Shadow AI governance; configure custom agent anomaly detection rules |
| **Regulated** | Full session control with content inspection, blocking capabilities, and comprehensive activity logging; integration with SIEM for correlation; agent threat detection integrated into SOC playbooks with mandatory investigation SLAs; quarterly Shadow AI governance review with sanctioned/unsanctioned app list |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for session control automation
- See [Verification & Testing](verification-testing.md) to validate session controls
- Review Control 2.3 for Conditional Access integration
- Back to [Control 2.9](../../../controls/pillar-2-security/2.9-defender-cloud-apps.md)
