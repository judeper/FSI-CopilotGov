# Control 4.6: Viva Insights — Copilot Impact Measurement — Verification & Testing

Test cases and evidence collection procedures for Copilot impact measurement using Viva Insights.

## Test Cases

### Test 1: Dashboard Data Population

- **Objective:** Verify that the Copilot impact dashboard in Viva Insights is populated with current data
- **Steps:**
  1. Access the Viva Insights Copilot impact dashboard.
  2. Verify data is current (within the last 7 days).
  3. Confirm key metrics are populated: active users, interaction counts, time savings estimates.
  4. Verify data covers all business units with Copilot deployments.
- **Expected Result:** Dashboard shows current data across all deployed business units.
- **Evidence:** Dashboard screenshot with data freshness timestamps.

### Test 2: Privacy Controls Enforcement

- **Objective:** Confirm that privacy controls prevent exposure of individual-level data to unauthorized viewers
- **Steps:**
  1. Log in as a non-authorized user (e.g., department manager without Insights access).
  2. Attempt to access individual-level Copilot usage data.
  3. Verify access is denied or data is aggregated below the minimum group size.
  4. Log in as an authorized analyst and verify individual data is accessible.
- **Expected Result:** Privacy controls correctly restrict individual data access per configuration.
- **Evidence:** Access attempt results showing correct enforcement.

### Test 3: Comparison Group Accuracy

- **Objective:** Validate that Copilot vs. non-Copilot user comparisons use correct group definitions
- **Steps:**
  1. Run the comparison analysis script.
  2. Verify the Copilot user group matches the actual license assignment list.
  3. Confirm no users are miscategorized (licensed but inactive, unlicensed but counted).
  4. Cross-reference group counts with the license report from Control 4.5.
- **Expected Result:** Comparison groups accurately reflect Copilot licensing and usage status.
- **Evidence:** Group membership comparison report.

### Test 4: ROI Calculation Validation

- **Objective:** Verify that ROI estimates use reasonable assumptions and accurate data inputs
- **Steps:**
  1. Run the ROI estimation report script.
  2. Review the assumptions (time saved, labor cost) against organizational benchmarks.
  3. Cross-reference active user counts with the usage analytics report.
  4. Validate the mathematical calculations in the ROI formula.
- **Expected Result:** ROI calculations use accurate data and documented assumptions.
- **Evidence:** ROI report with assumption documentation and calculation verification.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Copilot impact dashboard | Viva Insights | Screenshot | Monthly archive |
| Privacy configuration | Viva Insights Admin | Screenshot | With control documentation |
| Comparison analysis | PowerShell | CSV | Monthly archive |
| ROI report | Custom calculation | Spreadsheet | Quarterly archive |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FFIEC Management Booklet | IT investment effectiveness | Supports compliance with technology ROI measurement |
| OCC Heightened Standards | Technology governance | Helps meet expectations for measuring AI technology impact |
| SOX 404 | IT asset management | Supports governance of IT investment outcomes |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for Viva Insights issues
- Proceed to [Control 4.7](../4.7/portal-walkthrough.md) for feedback and telemetry governance
