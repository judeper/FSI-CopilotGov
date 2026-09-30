# Control 2.10: Insider Risk Detection for Copilot Usage — Portal Walkthrough

Step-by-step portal configuration for deploying insider risk detection that monitors Copilot usage patterns and agent activity for anomalous or risky behavior.

## Prerequisites

- Microsoft Purview Insider Risk Management Administrator role
- Supported Insider Risk Management subscription and assigned user licenses
- If you plan to use the IRM Triage Agent, verify Microsoft Security Copilot onboarding, pay-as-you-go billing, and provisioned SCUs
- HR connector configured (optional, for departing employee detection)
- Insider risk program approved by legal and compliance

## Steps

### Step 1: Enable Insider Risk Management for Copilot

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Settings > Policy indicators

Enable Copilot-relevant and AI-relevant indicators in the insider risk settings:
- Sensitive prompts or responses involving regulated data
- Risky prompt behavior in monitored AI apps
- Agent-related risky behavior where the Risky Agents template applies
- Companion office, device, DLP, or browser indicators approved for your use case
- **Generative AI apps indicators** and **Risky AI usage indicators (preview)** for the Copilot and agent experiences you want to monitor

### Step 2: Review Default Risky Agents Policy

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Policies

The Risky Agents policy (in preview) is available by default to organizations with supported licenses — when Insider Risk Management is set up, this policy is automatically present and ready to generate alerts based on observed agent activity. It supports Copilot Studio agents, Microsoft Foundry agents, and agents built using the P4AI SDK:

1. Locate the Risky Agents policy in the policy list
2. Review the scope — confirm all deployed Copilot Studio, Microsoft Foundry, and P4AI SDK agents are covered; verify the current preview status, licensing, and tenant availability before relying on it
3. Review alert routing — configure agent risk alerts to route to both the compliance team and agent deployment owners
4. Review default policy behavior and customize any permitted settings for FSI context if needed, without assuming undocumented volume thresholds
5. Note: Microsoft prebuilt agents, third-party agents, and SharePoint agents are not listed among the supported agent types — apply compensating monitoring via DSPM for AI or Defender for Cloud Apps for these agent types

### Step 3: Create Insider Risk Policy for Copilot

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Policies > Create Policy

Create an insider risk policy targeting Copilot usage:
- **Template:** Risky AI usage as the primary Copilot policy; add Data leaks or Data theft by departing users only where those trigger models are needed
- **Users:** All Copilot-licensed users (or priority user groups)
- **Triggering events:** Risky AI usage indicators, DLP policy match, or departing employee signal as appropriate to the chosen template. Organization-defined audit analytics can inform review, but they aren't built-in IRM triggers.
- **Indicators:** Enable Generative AI apps indicators, Risky AI usage indicators, and any supporting data-access indicators you need

### Step 4: Configure Supported Indicator Settings in the Policy Workflow

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Policies > Create policy (or edit a custom policy) > Indicators

Configure only the settings Microsoft documents in the policy workflow:
- Select the supported indicators you want the policy to evaluate
- Configure supported indicator-level thresholds where the policy workflow exposes them
- Use real-time analytics recommendations only where Learn documents that capability as available
- Keep organization-defined audit heuristics separate from built-in IRM indicator settings

### Step 5: Set Up Data Risk Graphs

**Portal:** Microsoft Purview > Insider Risk Management > Recommended actions

Data risk graphs provide a visual investigation experience — powered by Microsoft Sentinel integration — for alert-related SharePoint and OneDrive exfiltration activity. Microsoft has announced retirement of this experience on **November 24, 2026**, and Learn now states that new data risk graph onboarding closed on **September 24, 2026**:
1. If your tenant onboarded before **September 24, 2026**, use the existing **Set up data lake and data risk graph** onboarding and complete the Microsoft Sentinel data lake prerequisites (the data lake uses pay-as-you-go billing; historical onboarding took up to 60 minutes, with data risk graph availability for investigations taking 24-48 hours)
2. After setup, open an alert at Insider Risk Management > **Alerts (preview)** and select the **Data risk graph** tab to review the connected assets, users, and exfiltration activity (anonymous/company sharing links, downloads, renames in SharePoint and OneDrive)
3. Incorporate data risk graph review into the standard investigation procedure for alerts involving potential cross-department data movement while the feature remains available
4. Current Learn doesn't name a direct successor to the data risk graph experience, so document the replacement investigation workflow before retirement

### Step 6: Enable IRM Triage Agent

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Agents > Explore agents, then Insider Risk Management > Alerts (preview)

The IRM Triage Agent automates initial alert triage:
1. Enable the Triage Agent only after verifying that Security Copilot prerequisites are met, including SCUs and Microsoft 365 data sharing
2. Deploy the agent from **Agents > Explore agents** and start with **Agent runs manually on one alert at a time**
3. After validation, configure the agent to run automatically on a schedule for the selected alert timeframe
4. For Regulated tier: configure human-in-the-loop requirement — alerts cannot be dismissed without investigator review of Triage Agent recommendation
5. Document the Triage Agent in the firm's model inventory per OCC Bulletin 2011-12 (SR 11-7)

### Step 7: Set Up Alert Triage Workflow

**Portal:** Microsoft Purview
**Path:** Microsoft Purview > Insider Risk Management > Alerts (preview)

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
| **Baseline** | Enable insider risk detection with Generative AI apps indicators and Risky AI usage indicators; review the default Risky Agents (preview) policy; basic alert monitoring |
| **Recommended** | Add policy templates for data leaks and departing employees, priority user groups for high-risk roles, and data risk graph while it remains available; if Security Copilot prerequisites are approved, run the IRM Triage Agent first in manual mode; SIEM integration |
| **Regulated** | Comprehensive insider risk program with legal review; Risky Agents alerts reviewed within 24 hours; if deployed, IRM Triage Agent with human-in-the-loop and documented model governance; pseudonymization enabled except where incompatible with required investigations such as data risk graph; formal investigation procedures and documented legal basis for monitoring |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for insider risk monitoring automation
- See [Verification & Testing](verification-testing.md) to validate risk detection
- Review Control 2.3 for Adaptive Protection CA integration
- Review Control 2.9 for Defender for Cloud Apps session monitoring and agent threat detection
- Back to [Control 2.10](../../../controls/pillar-2-security/2.10-insider-risk-detection.md)
