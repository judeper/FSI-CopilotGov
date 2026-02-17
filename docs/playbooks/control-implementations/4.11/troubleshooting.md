# Control 4.11: Microsoft Sentinel Integration for Copilot Events — Troubleshooting

Common issues and resolution steps for Microsoft Sentinel integration with Copilot events.

## Common Issues

### Issue 1: Copilot Events Not Appearing in Sentinel

- **Symptoms:** Queries for CopilotInteraction record type return no results in Sentinel logs.
- **Root Cause:** Data connector may not be configured, the connector may not include Copilot event types, or there is an ingestion delay.
- **Resolution:**
  1. Verify the Microsoft 365 data connector is enabled and showing "Connected" status.
  2. Check that Exchange, SharePoint, and Teams data types are enabled in the connector.
  3. Enable the Microsoft Purview connector if Copilot events are routed through Purview.
  4. Allow up to 24 hours for initial data ingestion after connector configuration.
  5. Check the Sentinel workspace data ingestion health in Azure Monitor.

### Issue 2: Analytics Rules Generating Excessive False Positives

- **Symptoms:** Copilot analytics rules trigger too many incidents, overwhelming the SOC team.
- **Root Cause:** Rule thresholds may be set too low, or the detection query is too broad for the organization's usage patterns.
- **Resolution:**
  1. Review the last 30 days of triggered incidents to identify false positive patterns.
  2. Adjust thresholds based on actual usage baselines (run the query without the threshold to understand normal volume).
  3. Add exclusion conditions for known legitimate patterns (e.g., specific users with high Copilot usage by role).
  4. Use Sentinel's ML-based anomaly detection rather than static thresholds where possible.

### Issue 3: Sentinel Workspace Costs Increasing Unexpectedly

- **Symptoms:** Azure Sentinel costs are significantly higher than expected after enabling Copilot event ingestion.
- **Root Cause:** High-volume Copilot interactions generating large amounts of audit data that increase ingestion costs.
- **Resolution:**
  1. Review Sentinel workspace data volume: check Usage and estimated costs in the workspace settings.
  2. Consider filtering Copilot events at ingestion to reduce volume (only ingest events matching specific criteria).
  3. Use Sentinel's basic log tier for high-volume, low-priority Copilot events.
  4. Implement data collection rules to filter events before ingestion.
  5. Set up cost alerts in Azure to monitor workspace spending.

### Issue 4: Workbook Queries Timing Out

- **Symptoms:** Copilot monitoring workbook visualizations fail to load or time out.
- **Root Cause:** Queries may be scanning too much data, or the time range is too broad for the data volume.
- **Resolution:**
  1. Optimize queries by adding time filters and reducing the query scope.
  2. Use summarized or pre-aggregated data where possible.
  3. Reduce the default time range in the workbook (e.g., 7 days instead of 30).
  4. Consider creating a summary table using Sentinel playbooks for dashboard queries.

## Diagnostic Steps

1. **Check connector status:** Navigate to Sentinel > Data connectors and verify connector health.
2. **Test data ingestion:** Run `OfficeActivity | where TimeGenerated > ago(1h) | take 10` in Logs.
3. **Review analytics rule health:** Check Sentinel > Analytics for rule execution status.
4. **Monitor workspace costs:** Navigate to the workspace > Usage and estimated costs.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | No security monitoring for Copilot events | SOC lead + Azure admin — restore data ingestion |
| High | Analytics rules not detecting known incidents | Security engineering — rule tuning |
| Medium | Unexpected cost increases | Azure admin + Finance — cost optimization |
| Low | Workbook performance issues | Security engineering — query optimization |

## Related Resources

- [Control 3.1: Copilot Interaction Audit Logging](../3.1/portal-walkthrough.md)
- [Control 4.9: Incident Reporting](../4.9/portal-walkthrough.md)
- [Control 4.12: Change Management](../4.12/portal-walkthrough.md)
