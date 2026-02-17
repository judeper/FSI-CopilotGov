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

Enable Conditional Access App Control for Office 365 applications. This allows Defender for Cloud Apps to proxy Copilot-related sessions and apply real-time controls.

Verify Office 365 appears in the connected apps list with "Enabled" status.

### Step 2: Create Session Policy for Copilot Monitoring

**Portal:** Microsoft Defender for Cloud Apps
**Path:** Defender > Policies > Policy Management > Create Policy > Session Policy

Create a session policy targeting Copilot interactions:
- **Policy name:** "FSI Copilot Session Monitoring"
- **Session control type:** Monitor all activities
- **Filters:** App equals Office 365; Activity type includes file operations and content interactions
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

**Portal:** Microsoft Defender for Cloud Apps
**Path:** Defender > Investigate > Activity Log

Verify that Copilot-related activities appear in the activity log. Configure log retention and export settings for compliance documentation. Activity logs provide the evidence trail for regulatory examinations.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Enable session monitoring for Copilot interactions; configure basic alerting |
| **Recommended** | Content inspection with DLP integration; real-time alerts for sensitive data; session recording |
| **Regulated** | Full session control with content inspection, blocking capabilities, and comprehensive activity logging; integration with SIEM for correlation |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for session control automation
- See [Verification & Testing](verification-testing.md) to validate session controls
- Review Control 2.3 for Conditional Access integration
