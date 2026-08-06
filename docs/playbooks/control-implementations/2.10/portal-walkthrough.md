# Control 2.10: Insider Risk Detection for Copilot Usage — Portal Walkthrough

Step-by-step portal configuration for deploying insider risk detection that monitors Copilot usage patterns and agent activity for anomalous or risky behavior.

## Prerequisites

- Microsoft Purview Insider Risk Management Administrator role
- Microsoft 365 E5 or E5 Compliance license
- Verify current tenant entitlement for the IRM Triage Agent feature (for example, current Security Copilot / Microsoft 365 E5 availability in your tenant)
- HR connector configured (optional, for departing employee detection)
- Insider risk program approved by legal and compliance

## Steps

### Step 1: Enable Insider Risk Management for Copilot

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Settings > Policy indicators

Enable Copilot-relevant and AI-relevant indicators in the insider risk settings:
- Unusual volume of file access via Copilot
- Sensitive content access patterns through Copilot
- Copilot usage outside normal business hours
- Bulk content summarization or extraction patterns
- AI usage indicator category (Copilot query volume, agent interactions, AI app usage)

### Step 2: Review Default Risky Agents Policy

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Policies

The Risky Agents policy (in preview) is available by default to organizations with supported licenses — when Insider Risk Management is set up, this policy is automatically present and ready to generate alerts based on observed agent activity. It supports Copilot Studio agents, Microsoft Foundry agents, and agents built using the P4AI SDK:

1. Locate the Risky Agents policy in the policy list
2. Review the scope — confirm all deployed Copilot Studio, Microsoft Foundry, and P4AI SDK agents are covered; verify the current preview status, licensing, and tenant availability before relying on it
3. Review alert routing — configure agent risk alerts to route to both the compliance team and agent deployment owners
4. Review default thresholds and customize for FSI context if needed
5. Note: Microsoft prebuilt agents, third-party agents, and SharePoint agents are not listed among the supported agent types — apply compensating monitoring via DSPM for AI or Defender for Cloud Apps for these agent types

### Step 3: Create Insider Risk Policy for Copilot

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Policies > Create Policy

Create an insider risk policy targeting Copilot usage:
- **Template:** Data leaks or Data theft by departing users
- **Users:** All Copilot-licensed users (or priority user groups)
- **Triggering events:** DLP policy match, unusual Copilot activity volume, departing employee signal
- **Indicators:** Enable Copilot-specific indicators, AI usage indicators, and general data access indicators

### Step 4: Configure Risk Levels and Thresholds

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Settings > Risk level thresholds

Configure thresholds that define what constitutes elevated risk for Copilot usage:
- **Low risk:** Slightly above-average Copilot interaction volume
- **Medium risk:** Significant increase in sensitive content access via Copilot, or AI usage volume 2x peer baseline
- **High risk:** Bulk data extraction patterns, off-hours access to restricted content, agent data volume anomaly, or AI usage 3x+ peer baseline

### Step 5: Set Up Data Risk Graphs

**Portal:** Microsoft Purview > Insider Risk Management > Recommended actions

Data risk graphs provide a visual investigation experience — powered by Microsoft Sentinel integration — that summarizes a user's alert-related SharePoint and OneDrive exfiltration activity over the past 30 days:
1. Select the **Set up data lake and data risk graph** recommended action and complete the Microsoft Sentinel data lake onboarding (the data lake uses pay-as-you-go billing; initial onboarding can take up to 60 minutes, with data risk graph availability for investigations taking 24-48 hours)
2. After setup, open an alert at Insider Risk Management > Alerts and select the **Data risk graph** tab to review the connected assets, users, and exfiltration activity (anonymous/company sharing links, downloads, renames in SharePoint and OneDrive)
3. Incorporate data risk graph review into the standard investigation procedure for alerts involving potential cross-department data movement

### Step 6: Enable IRM Triage Agent

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Settings > Triage Agent

The IRM Triage Agent automates initial alert triage:
1. Enable the Triage Agent after verifying the feature is available for your tenant
2. Initial deployment: select **Agent runs manually on one alert at a time** and review categorization quality for 30 days
3. After validation, configure the agent to run automatically on a schedule for the selected alert timeframe
4. For Regulated tier: configure human-in-the-loop requirement — alerts cannot be dismissed without investigator review of Triage Agent recommendation
5. Document the Triage Agent in the firm's model inventory per OCC Bulletin 2011-12 (SR 11-7)

### Step 7: Set Up Alert Triage Workflow

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Alerts

Configure the alert triage workflow incorporating Triage Agent context:
- Assign insider risk investigators
- Set up alert notification rules (include agent-specific routing)
- Define triage SLAs (critical: 4 hours, high: 24 hours, medium: 72 hours; agent risk: 24 hours for Regulated)
- Configure integration with your SIEM or case management system
- Review Triage Agent context summaries as part of standard triage

### Step 8: Enable Privacy Controls

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Settings > Privacy

Configure privacy controls to balance risk detection with employee privacy:
- Enable pseudonymization for user identities until investigation threshold is met
- Configure data access restrictions for insider risk investigators
- Document the legal basis for insider risk monitoring (regulatory requirement)
- Communicate monitoring practices to employees through acceptable use policy

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Enable insider risk detection with Copilot and AI usage indicators; review the default Risky Agents (preview) policy; deploy the IRM Triage Agent in manual, one-alert-at-a-time mode; basic alert monitoring |
| **Recommended** | Policy templates for data leaks and departing employees; priority user groups for high-risk roles; data risk graph set up for alert investigation context (SharePoint/OneDrive exfiltration activity); IRM Triage Agent running automatically on a reviewed schedule; Risky Agents thresholds customized for FSI; SIEM integration |
| **Regulated** | Comprehensive insider risk program with legal review; Risky Agents alerts reviewed within 24 hours; IRM Triage Agent with human-in-the-loop; Triage Agent documented as model per SR 11-7; pseudonymization enabled; formal investigation procedures; documented legal basis for monitoring |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for insider risk monitoring automation
- See [Verification & Testing](verification-testing.md) to validate risk detection
- Review Control 2.3 for Adaptive Protection CA integration
- Review Control 2.9 for Defender for Cloud Apps session monitoring and agent threat detection
- Back to [Control 2.10](../../../controls/pillar-2-security/2.10-insider-risk-detection.md)
