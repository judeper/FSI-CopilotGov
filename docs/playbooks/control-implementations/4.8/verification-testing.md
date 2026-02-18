# Control 4.8: Cost Allocation and License Optimization — Verification & Testing

Test cases and evidence collection procedures for Copilot cost allocation and license optimization.

## Test Cases

### Test 1: PAYG Billing Accuracy Verification

- **Objective:** Verify that PAYG Copilot Chat charges in Azure Commerce accurately reflect actual usage and are reconcilable to internal records
- **Steps:**
  1. Run Script 1 from the PowerShell Setup guide to retrieve PAYG billing data from Azure Commerce for the current month.
  2. Compare the total PAYG charges with the estimated message count ($0.01/message): verify the calculation is consistent with usage data from the Microsoft 365 usage report.
  3. Download the Azure invoice from **Azure Portal > Cost Management + Billing > Invoices** and confirm the PAYG Copilot Chat line item matches Script 1 output.
  4. Verify department tag assignment is correct: confirm each PAYG charge routes to the correct cost center via Azure cost tags.
  5. Reconcile the total PAYG cost against the department budget cap to confirm no budget was exceeded without alerting.
- **Expected Result:** PAYG billing data in Azure Commerce matches usage estimates, reconciles to the invoice, and routes to correct cost centers via tags.
- **Evidence:** Script 1 output CSV; Azure invoice screenshot showing PAYG line items; Azure Cost Management tag report.

### Test 2: Budget Cap Enforcement Verification

- **Objective:** Confirm that PAYG budget caps alert appropriately before spending limits are reached
- **Steps:**
  1. Navigate to **Azure Portal > Cost Management > Budgets** and review active budget configurations for PAYG Copilot Chat.
  2. Verify each department with PAYG enabled has a budget configured with both 80% and 100% alert thresholds.
  3. Confirm alert recipients are set to the department head and IT finance owner (as configured in Step 1b of the portal walkthrough).
  4. Test alert delivery: if a budget was previously reached in the current month, confirm an alert was received. If not, verify the alert email routing by reviewing the budget alert configuration.
  5. Run Script 2 from the PowerShell Setup guide to review budget configuration programmatically.
- **Expected Result:** Budget caps are in place for all PAYG-enabled departments with correct alert thresholds and recipients.
- **Evidence:** Screenshot of Azure Budget configurations; alert notification records or email confirmation.

### Test 3: PAYG Cost Allocation Verification

- **Objective:** Verify that PAYG costs are correctly allocated to departments via Azure cost management tags
- **Steps:**
  1. In **Azure Portal > Cost Management > Cost analysis**, filter by the Copilot Chat service and group by department tag.
  2. Verify that costs appear attributed to the expected departments based on user group membership.
  3. Identify any "Untagged" costs and investigate their source — untagged PAYG usage indicates a tag governance gap.
  4. Compare the cost allocation output with the internal finance cost center mapping to confirm alignment.
- **Expected Result:** PAYG costs are fully tagged and allocated to correct cost centers; no significant untagged charges.
- **Evidence:** Azure Cost Management cost analysis export grouped by department tag; comparison with finance cost center report.

### Test 4: License Inventory Accuracy

- **Objective:** Verify that the license inventory report matches the actual license state in the tenant
- **Steps:**
  1. Run the license inventory script.
  2. Compare the script output with the M365 Admin Center Billing > Licenses page.
  3. Verify total purchased, assigned, and available counts match.
  4. Confirm the per-user cost matches the contracted price.
- **Expected Result:** Script output matches Admin Center data exactly.
- **Evidence:** Side-by-side comparison of script output and Admin Center screenshot.

### Test 5: Group-Based License Assignment

- **Objective:** Confirm that group-based licensing correctly assigns and removes licenses
- **Steps:**
  1. Add a test user to a Copilot license group.
  2. Wait for the license to be assigned (up to 24 hours).
  3. Verify the user has a Copilot license in their profile.
  4. Remove the user from the group and verify the license is removed.
- **Expected Result:** Licenses are automatically assigned and removed based on group membership.
- **Evidence:** Screenshots showing group membership change and license status.

### Test 6: Chargeback Report Accuracy

- **Objective:** Validate that department chargeback calculations correctly allocate costs
- **Steps:**
  1. Run the department chargeback report.
  2. Manually verify 3 departments by counting their licensed users.
  3. Confirm the cost calculation uses the correct per-user rate.
  4. Verify the total across all departments equals the total license cost.
- **Expected Result:** Chargeback allocations are mathematically correct and total matches overall spend.
- **Evidence:** Chargeback report with manual verification notes.

### Test 7: Underutilization Detection Accuracy

- **Objective:** Confirm that inactive license detection correctly identifies underutilized licenses
- **Steps:**
  1. Run the underutilization detection script.
  2. Manually verify 5 identified inactive users actually have no recent activity.
  3. Cross-reference with the M365 usage report for the same period.
  4. Confirm no active users are incorrectly flagged as inactive.
- **Expected Result:** Detection correctly identifies truly inactive users with no false positives.
- **Evidence:** Verification report comparing detection results with usage data.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| PAYG billing accuracy report | Script 1 + Azure invoice | CSV + Screenshot | Monthly archive; 7-year for regulated |
| Budget cap configuration | Azure Portal + Script 2 | Screenshot + Script output | With control documentation |
| PAYG cost allocation by department | Azure Cost Management export | CSV | Monthly archive |
| License inventory | PowerShell/Admin Center | CSV | Monthly archive |
| Chargeback report (per-seat) | Script 5 | CSV | Monthly archive |
| Underutilization report | Script 6 | CSV | Monthly archive |
| Group licensing config | Entra Admin Center | Screenshot | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SOX Section 404 (15 U.S.C. § 7262) | IT general controls over financial reporting — material technology expenditure authorization | PAYG budget authorization controls and per-seat license tracking fulfill IT asset management control requirements |
| FFIEC Management Booklet, Section II.D | IT investment governance — cost-benefit analysis and ongoing cost monitoring | Per-seat vs. PAYG comparison documentation and monthly PAYG billing reconciliation directly satisfy this expectation |
| OCC Heightened Standards (12 CFR Part 30, Appendix D) | Operational risk governance framework — technology cost management | Budget caps, anomaly detection, and monthly PAYG reporting demonstrate responsive cost governance |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for licensing issues
- Proceed to [Control 4.9](../4.9/portal-walkthrough.md) for incident reporting
