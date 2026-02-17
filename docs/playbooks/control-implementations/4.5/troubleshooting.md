# Control 4.5: Copilot Usage Analytics and Adoption Reporting — Troubleshooting

Common issues and resolution steps for Copilot usage analytics and adoption reporting.

## Common Issues

### Issue 1: Usage Reports Showing Zero or Stale Data

- **Symptoms:** Copilot usage reports show no data or data that has not updated in several days.
- **Root Cause:** Reporting data pipeline may have a delay of up to 48 hours, or the tenant may have a reporting configuration issue.
- **Resolution:**
  1. Allow 48 hours for new activity to appear in usage reports.
  2. Verify the reports service is healthy in the M365 Admin Center under Service Health.
  3. Check if usage data is available via the Graph API as an alternative.
  4. If data remains stale beyond 72 hours, contact Microsoft support.

### Issue 2: Licensed Users Not Showing in Reports

- **Symptoms:** Users with confirmed Copilot licenses do not appear in the usage report at all.
- **Root Cause:** License was recently assigned and the reporting system has not yet indexed the user, or the license assignment failed silently.
- **Resolution:**
  1. Verify the license assignment in Admin Center > Users > Active users.
  2. Allow up to 48 hours after license assignment for the user to appear in reports.
  3. Check if the user has signed in and used a Copilot feature since license assignment.
  4. If the user has been licensed for more than 48 hours and still does not appear, reassign the license.

### Issue 3: Graph API Reports Returning Errors

- **Symptoms:** PowerShell scripts using the Graph API return authentication or permission errors when accessing usage reports.
- **Root Cause:** Insufficient permissions, expired tokens, or API endpoint changes.
- **Resolution:**
  1. Verify the service principal has `Reports.Read.All` permission.
  2. Re-authenticate: `Disconnect-MgGraph && Connect-MgGraph -Scopes "Reports.Read.All"`
  3. Check for Microsoft Graph API deprecation notices for the reports endpoint.
  4. Update the Microsoft.Graph PowerShell module to the latest version.

### Issue 4: Adoption Rate Calculation Discrepancies

- **Symptoms:** Different reporting methods (Admin Center dashboard, Graph API, PowerShell) show different adoption rates.
- **Root Cause:** Each reporting method may use different definitions of "active" or different time period calculations.
- **Resolution:**
  1. Standardize on a single reporting method for official KPI tracking.
  2. Document the definition of "active" used by each method.
  3. When comparing, ensure the same time period and user scope are applied.
  4. Use Graph API data as the authoritative source for programmatic comparisons.

## Diagnostic Steps

1. **Check service health:** Verify Microsoft 365 reports service status.
2. **Test Graph API access:** `Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/reports"`
3. **Verify permissions:** `Get-MgContext | Select Scopes`
4. **Manual data check:** Compare 5 known users against the downloaded usage report.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | No usage data available for regulatory reporting | IT Admin + Microsoft Support |
| High | Report data significantly inaccurate | IT Admin — investigate data pipeline |
| Medium | API access issues | IT Support — permissions and connectivity |
| Low | Minor reporting delays | Monitor and report at next cycle |

## Related Resources

- [Control 4.1: Copilot Admin Settings](../4.1/portal-walkthrough.md)
- [Control 4.6: Viva Insights Copilot Measurement](../4.6/portal-walkthrough.md)
