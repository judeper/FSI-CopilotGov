# Control 4.11: Microsoft Sentinel Integration for Copilot Events — Verification & Testing

Test cases and evidence collection procedures for Microsoft Sentinel integration with Copilot events.

## Test Cases

### Test 1: Data Connector Validation

- **Objective:** Verify that Copilot events are being ingested into the Sentinel workspace
- **Steps:**
  1. Navigate to Sentinel > Logs in the Azure Portal.
  2. Run the query: `OfficeActivity | where RecordType == "CopilotInteraction" | take 10`
  3. Verify results are returned with recent timestamps.
  4. Confirm data freshness (events within the last 2 hours).
- **Expected Result:** Copilot events are present in the Sentinel workspace with near-real-time ingestion.
- **Evidence:** Query results screenshot showing recent Copilot events.

### Test 2: Analytics Rule Trigger Verification

- **Objective:** Confirm that Copilot analytics rules trigger alerts when conditions are met
- **Steps:**
  1. Review the analytics rule configuration for the "Unusual Copilot Access Pattern" rule.
  2. Generate test activity that matches the rule conditions (or review historical triggers).
  3. Verify an incident is created in the Sentinel incidents queue.
  4. Confirm the incident contains relevant context (user, time, activity details).
- **Expected Result:** Analytics rule triggers and creates an incident with appropriate context.
- **Evidence:** Sentinel incident screenshot showing the triggered alert and details.

### Test 3: Workbook Dashboard Functionality

- **Objective:** Validate that the Copilot monitoring workbook displays accurate, current data
- **Steps:**
  1. Open the Copilot Security and Governance Dashboard workbook.
  2. Verify each visualization loads with current data.
  3. Test the time range filter to confirm historical data is available.
  4. Verify the dashboard is accessible to authorized security and compliance team members.
- **Expected Result:** Workbook displays current data across all visualizations with working filters.
- **Evidence:** Dashboard screenshot showing populated visualizations.

### Test 4: Hunting Query Effectiveness

- **Objective:** Verify that hunting queries return actionable results for Copilot security analysis
- **Steps:**
  1. Run each hunting query from the query library.
  2. Review results for relevance and accuracy.
  3. Identify any false positives or missed detections.
  4. Document query tuning recommendations.
- **Expected Result:** Hunting queries return relevant results that support security investigation.
- **Evidence:** Query results with analyst notes on relevance and accuracy.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Data connector status | Azure Portal | Screenshot | With control documentation |
| Analytics rule configuration | Sentinel | Screenshot/Export | With control documentation |
| Workbook dashboard | Sentinel | Screenshot | Monthly archive |
| Hunting query results | Sentinel Logs | CSV export | Per investigation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FFIEC IT Handbook | Continuous security monitoring | Supports compliance with security monitoring and threat detection |
| NYDFS 23 NYCRR 500 | Continuous monitoring | Helps meet continuous monitoring requirements for AI systems |
| 12 CFR part 30, appendix D (OCC Heightened Standards) | Threat detection | Supports expectations for advanced threat detection capabilities |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for Sentinel integration issues
- Proceed to [Control 4.12](../4.12/portal-walkthrough.md) for change management
- Back to [Control 4.11](../../../controls/pillar-4-operations/4.11-sentinel-integration.md)
