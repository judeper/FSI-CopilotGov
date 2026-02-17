# Control 4.5: Copilot Usage Analytics and Adoption Reporting — Verification & Testing

Test cases and evidence collection procedures for Copilot usage analytics and adoption reporting.

## Test Cases

### Test 1: Usage Dashboard Data Accuracy

- **Objective:** Verify that Copilot usage dashboard data accurately reflects actual usage
- **Steps:**
  1. Have 5 test users perform known Copilot interactions across different applications.
  2. Wait 48 hours for reporting data to update.
  3. Check the M365 Admin Center Copilot usage report for the test users.
  4. Verify the reported activity matches the known test interactions.
- **Expected Result:** Dashboard accurately reflects the test users' Copilot activity within 48 hours.
- **Evidence:** Comparison of known test activity with dashboard-reported data.

### Test 2: Report Privacy Controls

- **Objective:** Confirm that usage report privacy settings are correctly configured
- **Steps:**
  1. Log in as a Reports Reader role user and access the Copilot usage report.
  2. Verify that user-identifiable information is shown or hidden per the configured privacy settings.
  3. Log in as a compliance administrator and verify they can access identifiable data.
  4. Confirm the audit log records who accessed user-identifiable usage reports.
- **Expected Result:** Privacy settings correctly control visibility of identifiable data per role.
- **Evidence:** Screenshots showing different data visibility for different roles.

### Test 3: Adoption KPI Tracking

- **Objective:** Validate that adoption KPIs are accurately calculated and tracked over time
- **Steps:**
  1. Run the adoption report scripts for 7-day, 30-day, and 90-day periods.
  2. Verify the active user count is consistent across data sources.
  3. Confirm the adoption rate calculation is correct (active / licensed * 100).
  4. Compare with the M365 Admin Center dashboard for consistency.
- **Expected Result:** KPI calculations are accurate and consistent across reporting methods.
- **Evidence:** KPI comparison report showing calculated values from multiple sources.

### Test 4: Department-Level Reporting Accuracy

- **Objective:** Confirm department-level adoption reports correctly aggregate user data
- **Steps:**
  1. Run the department-level adoption report script.
  2. Manually verify 3 departments by cross-referencing user lists and activity.
  3. Confirm department assignments match Azure AD department attributes.
  4. Verify totals sum correctly across all departments.
- **Expected Result:** Department adoption data is accurately aggregated from individual user data.
- **Evidence:** Department report with manual verification notes.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Usage dashboard screenshot | M365 Admin Center | Screenshot | Monthly archive |
| Adoption report | PowerShell/Graph | CSV | Monthly archive |
| Privacy settings config | Admin Center | Screenshot | With control documentation |
| KPI tracking log | Custom report | Spreadsheet | 1 year |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FFIEC Management Booklet | IT investment monitoring | Supports compliance with technology utilization tracking |
| OCC Heightened Standards | Technology governance | Helps meet expectations for AI technology adoption oversight |
| SOX 404 | Internal control over IT assets | Supports IT asset management and utilization controls |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for analytics issues
- Proceed to [Control 4.6](../4.6/portal-walkthrough.md) for Viva Insights Copilot measurement
