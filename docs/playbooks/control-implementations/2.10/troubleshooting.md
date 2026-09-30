# Control 2.10: Insider Risk Detection for Copilot Usage — Troubleshooting

Common issues and resolution steps for insider risk detection for Copilot and agent activity.

## Common Issues

### Issue 1: Risky Agents Policy Not Visible

- **Symptoms:** The default Risky Agents (preview) policy does not appear in the IRM policy list
- **Root Cause:** The Risky Agents (preview) policy is available by default only to organizations with supported licenses once Insider Risk Management is set up. Missing setup prerequisites or tenant entitlement can prevent it from appearing.
- **Resolution:**
  1. Verify the tenant has a supported Insider Risk Management subscription and that Insider Risk Management is set up
  2. Check the IRM policy list with a filter for "All" policy states (including disabled or pending)
  3. Confirm the tenant is currently entitled to the Risky Agents (preview) capability
  4. If the default policy is still absent, verify whether a custom policy can be created from the Risky Agents template or open a Microsoft support case
  5. For agent types not listed as supported (Microsoft prebuilt agents, third-party agents, SharePoint agents), configure monitoring via DSPM for AI or Defender for Cloud Apps as a compensating control

### Issue 2: Generative AI Apps or Risky AI Usage Indicators Not Available

- **Symptoms:** The **Generative AI apps indicators** section or **Risky AI usage indicators (preview)** do not appear in IRM Policy indicators settings
- **Root Cause:** The indicators may require specific licensing, pay-as-you-go billing for some data sources, or may not be available in the tenant yet.
- **Resolution:**
  1. Verify the tenant has a supported Insider Risk Management subscription and any required add-ons
  2. Verify Copilot activity logging is enabled in the tenant
  3. Enable pay-as-you-go billing if you need non-Microsoft 365 AI data sources
  4. Use traditional DLP, device, and office indicators as compensating controls until the AI indicators are available

### Issue 3: No Copilot-Specific Indicators Available

- **Symptoms:** Insider Risk Management settings do not show Copilot-specific indicators
- **Root Cause:** The tenant might not yet expose the current **Generative AI apps indicators** or **Risky AI usage indicators (preview)** surfaces, or the browser/extension prerequisites for risky AI usage might be missing.
- **Resolution:**
  1. Verify the current **Policy indicators** page exposes **Generative AI apps indicators**
  2. Configure the Microsoft Compliance Extension and browser signal prerequisites where required for the template
  3. Use general data access and DLP-based indicators as alternatives
  4. Configure custom indicators or audit-backed review using CopilotInteraction audit records

### Issue 4: IRM Triage Agent Not Producing Context Summaries

- **Symptoms:** Alerts do not show Triage Agent context summaries; the Triage Agent feature isn't visible in Purview Agents or Insider Risk alerts
- **Root Cause:** The IRM Triage Agent is deployed through the Purview **Agents** experience and depends on Security Copilot prerequisites, including SCUs and Microsoft 365 data sharing. The feature might not yet be enabled for the tenant.
- **Resolution:**
  1. Verify the tenant currently has access to the IRM Triage Agent capability
  2. Navigate to Microsoft Purview > Agents > Explore agents and confirm the agent is deployed
  3. Verify Security Copilot onboarding, SCU availability, Microsoft 365 data sharing, and the Purview plug-in prerequisites
  4. Review Insider Risk Management > Alerts (preview) for triaged alerts after the agent runs
  5. If the Triage Agent is deployed but context summaries are absent, allow 24-48 hours for the system to process existing alerts
  6. Check that the IRM investigator role has appropriate access to view Triage Agent outputs

### Issue 5: Data Risk Graph Not Loading or Missing Data

- **Symptoms:** The Data risk graph tab is accessible on an alert but does not load, or shows no activity data
- **Root Cause:** The data risk graph will not load if the anonymized usernames privacy setting is enabled in IRM privacy settings; it also does not support admin unit-scoped access. Separately, if the data lake and data risk graph onboarding has only just completed, the graph may not yet have data — the graph initially shows the most recent seven days and takes time to grow to the full 30-day window. Microsoft also plans to retire the experience on November 24, 2026.
- **Resolution:**
  1. Confirm the anonymized usernames privacy setting is disabled (Microsoft Purview > Insider Risk Management > Settings > Privacy) — the data risk graph cannot be used with it enabled
  2. Confirm the investigator viewing the graph is not scoped to an admin unit; admin units are not supported in the data risk graph
  3. Confirm the investigator is assigned the **Insider Risk Management Graph Reader** role (included by default in several built-in IRM role groups)
  4. If the tenant onboarded before **September 24, 2026**, verify the **Set up data lake and data risk graph** recommended action shows Complete; allow 24-48 hours after onboarding for initial data to populate, and expect gradual growth toward the full 30-day window
  5. Confirm the alert's underlying activity is one of the supported exfiltration activities (SharePoint/OneDrive sharing links, downloads, renames) — the graph does not represent Copilot prompt/response content

### Issue 6: High Volume of Low-Quality Alerts

- **Symptoms:** Insider risk generates many alerts for routine Copilot usage, overwhelming investigators
- **Root Cause:** The configured policies or companion indicators may be too broad for the organization's actual use patterns, or analysts may be treating local review heuristics as if they were built-in IRM thresholds.
- **Resolution:**
  1. Review which specific indicators, templates, or companion signals are generating the noise
  2. Narrow the in-scope apps, users, or companion indicators rather than inventing unsupported built-in thresholds
  3. Use priority user groups to focus detection on higher-risk roles
  4. Implement alert filtering to separate low-confidence from high-confidence signals
  5. If you use organization-defined audit heuristics outside IRM, document them separately from the built-in IRM indicators

### Issue 7: Insider Risk Data Not Correlating with Copilot Events

- **Symptoms:** Insider risk alerts do not include Copilot-specific context or activity details
- **Root Cause:** Audit log data for Copilot may not be fully integrated with the insider risk management data pipeline.
- **Resolution:**
  1. Verify audit logging is enabled for Copilot interactions
  2. Check that the Copilot audit record type is included in the insider risk data sources
  3. Use supplementary monitoring (Script 2) to correlate Copilot usage with risk signals
  4. Configure SIEM integration to provide additional correlation context

### Issue 8: Agent Alerts Not Routing to Agent Owners

- **Symptoms:** Risky Agents policy generates alerts, but agent deployment owners are not receiving notifications
- **Root Cause:** Alert routing for the Risky Agents policy may default to the general IRM alert recipients without agent-owner-specific routing.
- **Resolution:**
  1. Navigate to Microsoft Purview > Insider Risk Management > Policies > [Risky Agents policy] > Settings
  2. Review alert notification configuration and add agent-owner-specific notification groups
  3. Consider creating a distribution group for agent deployment owners and adding it to the Risky Agents alert notification recipients
  4. Verify the escalation path in the documented investigation procedures includes agent-owner notification

### Issue 9: Legal Concerns About Employee Monitoring

- **Symptoms:** Legal or HR team raises concerns about the scope of insider risk monitoring for Copilot
- **Root Cause:** Employee monitoring requires careful balancing of security needs with privacy rights and employment law compliance.
- **Resolution:**
  1. Enable pseudonymization to protect employee identity until investigation threshold
  2. Document the legal basis for monitoring (regulatory obligation — FINRA Rule 3110, GLBA §501(b), acceptable use policy)
  3. Obtain legal counsel review of the insider risk program scope
  4. Communicate monitoring expectations through the acceptable use policy and training
  5. Limit investigator access to the minimum necessary for triage

## Diagnostic Steps

1. **Check policy status:** Run Script 1 to verify policies are active
2. **Verify Risky Agents:** Microsoft Purview > Insider Risk Management > Policies — filter for agent policies
3. **Review indicators:** Microsoft Purview > Insider Risk Management > Settings > Policy indicators — confirm the Generative AI apps indicators and any Risky AI usage indicators you require are enabled
4. **Check Triage Agent:** Microsoft Purview > Agents > Explore agents and Insider Risk Management > Alerts (preview) — verify the Triage Agent is deployed and producing output
5. **Test detection:** Generate test activity and monitor for risk signals
6. **Review audit logs:** Verify Copilot events appear in the unified audit log
7. **Check privacy settings:** Verify pseudonymization is properly configured

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Alert tuning needed | Insider risk management team |
| **Medium** | Indicators not detecting expected patterns | Security Operations and Microsoft support |
| **High** | True positive insider risk alert on sensitive data | CISO, Legal, and HR per investigation procedures |
| **High** | Agent risk alert suggesting data exfiltration via agent | CISO, agent deployment owner, Legal per investigation procedures |
| **Critical** | Active data exfiltration detected via Copilot | Incident response team immediately |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Insider risk configuration
- [PowerShell Setup](powershell-setup.md) — Monitoring scripts
- [Verification & Testing](verification-testing.md) — Detection validation
- Back to [Control 2.10](../../../controls/pillar-2-security/2.10-insider-risk-detection.md)
