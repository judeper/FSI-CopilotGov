# Control 3.7: Regulatory Reporting — Troubleshooting

Common issues and resolution steps for regulatory reporting incorporating Copilot governance data.

## Common Issues

### Issue 1: Report Data Discrepancies Between Sources

- **Symptoms:** Copilot interaction counts in the regulatory report differ from the Communication compliance dashboard or audit log totals.
- **Root Cause:** Different data sources may have varying refresh cycles, or query parameters may not align precisely across sources.
- **Resolution:**
  1. Standardize the date range and time zone across all report queries.
  2. Use UTC timestamps consistently in audit log searches.
  3. Account for audit log ingestion latency (up to 24 hours) by setting the report cutoff 48 hours before generation.
  4. Document known variance sources and acceptable thresholds in the report methodology section.

### Issue 2: Audit Log Search Returning Incomplete Data

- **Symptoms:** Audit log queries hit the 5,000-record limit, resulting in incomplete data for the reporting period.
- **Root Cause:** High-volume Copilot usage generates more records than a single search can return.
- **Resolution:**
  1. Implement paginated search using `SessionCommand ReturnLargeSet`.
  2. Split queries by date range (weekly intervals) and aggregate results.
  3. Use the Microsoft Graph API for large-scale audit data retrieval.
  4. Consider implementing a data warehouse for regulatory reporting data.

### Issue 3: Report Template Missing Required Regulatory Fields

- **Symptoms:** Regulatory submission is returned or flagged by the regulator for missing required data fields.
- **Root Cause:** Report template was not updated to reflect changes in regulatory requirements, or new AI-specific reporting fields were added.
- **Resolution:**
  1. Review the latest regulatory guidance for reporting requirements.
  2. Update report templates to include all required fields.
  3. Implement a template review process triggered by regulatory updates.
  4. Subscribe to FINRA, SEC, and OCC regulatory update notifications.

### Issue 4: Report Generation Scripts Failing

- **Symptoms:** PowerShell automation scripts fail with authentication errors, timeout errors, or module incompatibilities.
- **Root Cause:** Authentication tokens may have expired, module versions may be incompatible, or service connectivity issues.
- **Resolution:**
  1. Verify authentication credentials and re-authenticate to all required services.
  2. Update PowerShell modules to the latest stable versions.
  3. Increase timeout values for large audit log queries.
  4. Implement error handling and retry logic in report generation scripts.
  5. Test scripts in a non-production environment before regulatory report generation.

## Diagnostic Steps

1. **Verify data source connectivity:** Test connections to each data source used in reporting.
2. **Check audit log availability:** Confirm audit logs are available for the full reporting period.
3. **Validate query parameters:** Review search queries for correct date ranges, record types, and filters.
4. **Test report generation:** Run the full report generation pipeline with a limited date range.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Regulatory submission deadline at risk | Chief Compliance Officer + IT leadership |
| High | Data accuracy issues in submitted report | Compliance team — correction and resubmission |
| Medium | Report generation delays | IT support — script and connectivity troubleshooting |
| Low | Minor formatting or presentation issues | Address in next reporting cycle |

## Related Resources

- [Control 3.1: Copilot Interaction Audit Logging](../3.1/portal-walkthrough.md)
- [Control 3.6: Supervision and Oversight](../3.6/portal-walkthrough.md)
- [Control 3.12: Evidence Collection](../3.12/portal-walkthrough.md)
- Back to [Control 3.7](../../../controls/pillar-3-compliance/3.7-regulatory-reporting.md)
