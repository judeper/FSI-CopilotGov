# Control 4.6: Viva Insights — Copilot Impact Measurement — Troubleshooting

Common issues and resolution steps for Copilot impact measurement using Viva Insights.

## Common Issues

### Issue 1: Viva Insights Dashboard Not Showing Copilot Data

- **Symptoms:** The Copilot impact dashboard shows no data or displays a "no data available" message.
- **Root Cause:** Viva Insights may not be licensed or configured, data pipeline delay, or insufficient Copilot usage for analysis.
- **Resolution:**
  1. Verify Viva Insights licenses are assigned to the analysis population.
  2. Confirm Copilot has been active for at least 30 days (initial data requires history).
  3. Check that the Viva Insights data sources include Copilot interaction data.
  4. Verify the minimum group size is met for the selected population.

### Issue 2: Privacy Controls Too Restrictive for Analysis

- **Symptoms:** Analysts cannot access sufficient data granularity for meaningful Copilot impact analysis.
- **Root Cause:** Privacy settings (minimum group size, data access restrictions) may be more restrictive than necessary for analytical purposes.
- **Resolution:**
  1. Review the minimum group size setting — consider reducing to 10 if currently higher.
  2. Evaluate whether the analyst role has appropriate permissions.
  3. Consider creating a dedicated Viva Insights analyst role with appropriate access.
  4. If organizational policy requires high privacy thresholds, aggregate data manually from department-level reports.

### Issue 3: Inaccurate Time Savings Estimates

- **Symptoms:** Viva Insights reports time savings that seem unrealistically high or low compared to user feedback.
- **Root Cause:** Time savings algorithms use heuristic models that may not accurately reflect all types of Copilot usage.
- **Resolution:**
  1. Supplement Viva Insights time savings estimates with direct user surveys.
  2. Validate estimates against specific use cases with measurable time savings.
  3. Use the estimates as directional indicators rather than precise measurements.
  4. Document the methodology and limitations when presenting ROI data to leadership.

### Issue 4: Comparison Analysis Skewed by User Demographics

- **Symptoms:** Copilot vs. non-Copilot comparisons show misleading results because the groups have different job profiles.
- **Root Cause:** Copilot may be deployed first to specific roles that naturally have different collaboration patterns.
- **Resolution:**
  1. Use matched pair analysis — compare users with similar roles and departments.
  2. Control for department, role level, and tenure in the analysis.
  3. Use pre/post analysis for the same users rather than cross-group comparison.
  4. Document any demographic differences between groups in the analysis methodology.

## Diagnostic Steps

1. **Check Viva Insights access:** Navigate to insights.viva.office.com and verify access.
2. **Verify data freshness:** Check the last updated date on the Copilot dashboard.
3. **Review privacy settings:** Confirm minimum group size and data access configurations.
4. **Test data extraction:** Run the Graph API reports to verify data availability.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| High | No Viva Insights data available for governance reporting | IT Admin + Microsoft Support |
| Medium | Privacy settings preventing required analysis | Privacy officer + Viva admin |
| Medium | Inaccurate ROI reporting to leadership | Analytics team for methodology review |
| Low | Minor dashboard display issues | IT support |

## Related Resources

- [Control 4.5: Copilot Usage Analytics](../4.5/portal-walkthrough.md)
- [Control 4.7: Feedback and Telemetry Governance](../4.7/portal-walkthrough.md)
