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

### Step 2: Review Auto-Deployed Risky Agents Policy

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Policies

Microsoft auto-deploys a Risky Agents policy for all Copilot Studio and Azure AI Foundry agents in the tenant (GA December 2025):

1. Locate the Risky Agents policy in the policy list
2. Review the scope — confirm all deployed Copilot Studio and Azure AI Foundry agents are covered
3. Review alert routing — configure agent risk alerts to route to both the compliance team and agent deployment owners
4. Review default thresholds and customize for FSI context if needed
5. Note: Microsoft prebuilt agents, third-party agents, and SharePoint agents are not yet covered by auto-deployment — apply compensating monitoring via DSPM for AI or Defender for Cloud Apps for these agent types

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

### Step 5: Enable Data Risk Graphs

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Investigations > Data risk graphs

Data risk graphs (GA December 2025) visualize relationships between users, data assets, and AI interactions:
1. Navigate to the investigation workspace and select the Data risk graphs view
2. Configure graph time windows (14-day or 30-day views recommended for FSI environments)
3. Use graphs to identify cross-department Copilot data access patterns (e.g., operations staff accessing trading data via Copilot)
4. Incorporate graph review into the standard investigation procedure for high-risk alerts

### Step 6: Enable IRM Triage Agent

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Settings > Triage Agent

The IRM Triage Agent automates initial alert triage:
1. Enable the Triage Agent after verifying the feature is available for your tenant
2. Initial deployment: enable in read-only mode and review categorization quality for 30 days
3. After validation, enable auto-categorization to drive investigator queue prioritization
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
| **Baseline** | Enable insider risk detection with Copilot and AI usage indicators; review auto-deployed Risky Agents policy; enable IRM Triage Agent in read-only mode; basic alert monitoring |
| **Recommended** | Policy templates for data leaks and departing employees; priority user groups for high-risk roles; data risk graphs for cross-department access visualization; IRM Triage Agent with auto-categorization; Risky Agents thresholds customized for FSI; SIEM integration |
| **Regulated** | Comprehensive insider risk program with legal review; Risky Agents alerts reviewed within 24 hours; IRM Triage Agent with human-in-the-loop; Triage Agent documented as model per SR 11-7; pseudonymization enabled; formal investigation procedures; documented legal basis for monitoring |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for insider risk monitoring automation
- See [Verification & Testing](verification-testing.md) to validate risk detection
- Review Control 2.3 for Adaptive Protection CA integration
- Review Control 2.9 for Defender for Cloud Apps session monitoring and agent threat detection
