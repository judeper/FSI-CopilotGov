# Control 2.10: Insider Risk Detection for Copilot Usage — Troubleshooting

Common issues and resolution steps for insider risk detection for Copilot and agent activity.

## Common Issues

### Issue 1: Risky Agents Policy Not Visible

- **Symptoms:** The auto-deployed Risky Agents policy does not appear in the IRM policy list
- **Root Cause:** Auto-deployment of the Risky Agents policy (GA December 2025) may not have completed for all tenants. The policy may also be deployed under a different display name, or the deployment may have been delayed due to license provisioning timing.
- **Resolution:**
  1. Verify the tenant has Microsoft 365 E5 Compliance licensing active
  2. Check the IRM policy list with a filter for "All" policy states (including disabled or pending)
  3. Review the Microsoft 365 message center for MC1200579 to check deployment status for your tenant
  4. If the policy has not been auto-deployed, create a Risky Agents policy manually using the available template in IRM
  5. For agents not covered by auto-deployment (prebuilt Microsoft agents, third-party, SharePoint agents), configure monitoring via DSPM for AI or Defender for Cloud Apps as a compensating control

### Issue 2: AI Usage Indicators Not Available

- **Symptoms:** The AI usage indicator category does not appear in IRM Policy indicators settings
- **Root Cause:** AI usage indicators may require specific licensing or may be in staged rollout to tenants.
- **Resolution:**
  1. Verify Microsoft 365 E5 Compliance licensing is active
  2. Verify Copilot activity logging is enabled in the tenant
  3. Check the Microsoft 365 roadmap for AI usage indicator availability in your region
  4. Use general Copilot interaction volume indicators as an alternative until AI usage indicators are available

### Issue 3: No Copilot-Specific Indicators Available

- **Symptoms:** Insider Risk Management settings do not show Copilot-specific indicators
- **Root Cause:** Copilot-specific indicators may require specific licensing or may be in staged rollout.
- **Resolution:**
  1. Verify Microsoft 365 E5 Compliance licensing is active
  2. Check the Microsoft 365 roadmap for Copilot insider risk indicator availability
  3. Use general data access and DLP-based indicators as alternatives
  4. Configure custom indicators using Copilot audit log events

### Issue 4: IRM Triage Agent Not Producing Context Summaries

- **Symptoms:** Alerts do not show Triage Agent context summaries; Triage Agent feature not visible in IRM settings
- **Root Cause:** The IRM Triage Agent entitlement and rollout can vary by tenant. The feature may not yet be available in the tenant, or the tenant might not have the required entitlement enabled.
- **Resolution:**
  1. Verify the tenant currently has access to the IRM Triage Agent capability
  2. Navigate to Microsoft Purview > Insider Risk Management > Settings and look for the Triage Agent configuration
  3. Enable the Triage Agent if it is available but disabled
  4. If the Triage Agent is enabled but context summaries are absent, allow 24-48 hours for the system to process existing alerts
  5. Check that the IRM investigator role has appropriate access to view Triage Agent outputs

### Issue 5: Data Risk Graphs Not Showing Copilot Activity

- **Symptoms:** Data risk graphs are accessible but do not display Copilot interaction data
- **Root Cause:** Data risk graphs depend on audit log data from Copilot interactions being available to IRM. If Copilot audit logging is disabled, or if the IRM data pipeline has not yet ingested the data, graphs will not reflect Copilot activity.
- **Resolution:**
  1. Verify Copilot interaction audit logging is enabled: Microsoft Purview > Audit > Audit log search — filter for CopilotInteraction record type
  2. Confirm audit log data is flowing to IRM (allow up to 48 hours for initial ingestion)
  3. Run Script 2 (Copilot Usage Anomaly Detection) to verify audit log data is accessible
  4. If audit logging is enabled but graphs are still empty, check the graph time window — very recent deployments may not have sufficient historical data for graph generation

### Issue 6: High Volume of Low-Quality Alerts

- **Symptoms:** Insider risk generates many alerts for routine Copilot usage, overwhelming investigators
- **Root Cause:** Risk thresholds may be too sensitive, or the baseline for normal Copilot usage has not been properly established. Organizations that have recently expanded Copilot access may see elevated alert volume as baselines are recalibrated.
- **Resolution:**
  1. Allow 2-4 weeks for the system to establish behavioral baselines after a significant Copilot rollout
  2. Adjust risk level thresholds upward to reduce noise — use the Triage Agent categorizations as a guide for which alert types are generating low-value signals
  3. Use priority user groups to focus detection on higher-risk roles
  4. Implement alert filtering to separate low-confidence from high-confidence signals
  5. For AI usage indicators, set thresholds relative to organizational Copilot deployment scale — a fully deployed tenant will have much higher baseline AI usage than a limited pilot

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
3. **Review indicators:** Microsoft Purview > Insider Risk Management > Settings > Policy indicators — confirm AI usage category enabled
4. **Check Triage Agent:** Microsoft Purview > Insider Risk Management > Settings — verify Triage Agent is enabled
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
