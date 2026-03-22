# Control 4.8: Cost Allocation and License Optimization — Verification & Testing

Test cases and evidence collection procedures for Copilot cost allocation and license optimization.

## Test Cases

### Test 1: PAYG Billing Accuracy Verification

- **Objective:** Verify that PAYG Copilot charges are tied to the correct billing policy and reconciled to internal records
- **Steps:**
  1. Run Script 1 from the PowerShell Setup guide to retrieve PAYG billing data from Azure Commerce for the current month.
  2. Review the billing policy configuration in **Billing > Pay-as-you-go services** and confirm the intended users or groups are covered.
  3. Download the Azure invoice or cost export and confirm the PAYG Copilot line item matches Script 1 output.
  4. Reconcile the total PAYG cost to the internal cost owner or department assigned to the billing policy.
  5. Confirm the connected service and policy coverage match the approved scope.
- **Expected Result:** PAYG billing data matches the billing-policy scope, reconciles to invoice or cost-management records, and is attributable to the correct cost owner.
- **Evidence:** Script 1 output CSV; billing policy screenshot; invoice or Cost Management export.

### Test 2: Budget and Notification Verification

- **Objective:** Confirm that PAYG billing policies have budgets and notification routing configured appropriately
- **Steps:**
  1. Navigate to **Billing > Pay-as-you-go services** and review the active billing policies.
  2. Verify each active billing policy has a budget configured.
  3. Confirm alert recipients are set to the approved business and IT finance owners.
  4. If prior notifications exist, confirm they were received and handled appropriately.
  5. Run Script 2 from the PowerShell Setup guide to review budget configuration programmatically.
- **Expected Result:** Budgets and notification routing are in place for all active billing policies.
- **Evidence:** Screenshot of billing policy settings or budget configuration; notification records or email confirmation.

### Test 3: PAYG Cost Allocation Verification

- **Objective:** Verify that PAYG costs are correctly allocated to departments or cost owners through billing policy governance
- **Steps:**
  1. In **Cost Management**, filter by the Copilot service covered by PAYG.
  2. Compare the costs with the billing policy owner and covered user or group list.
  3. Identify any costs that cannot be mapped to an approved billing policy and investigate their source.
  4. Compare the output with the internal finance cost center mapping to confirm alignment.
- **Expected Result:** PAYG costs are attributable to approved billing policies and mapped to the correct cost owners.
- **Evidence:** Cost Management export; billing policy inventory; comparison with finance cost center report.

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
| Billing policy and budget configuration | Admin Center + Script 2 | Screenshot + Script output | With control documentation |
| PAYG cost allocation by department | Cost Management export + billing policy inventory | CSV | Monthly archive |
| License inventory | PowerShell/Admin Center | CSV | Monthly archive |
| Chargeback report (per-seat) | Script 5 | CSV | Monthly archive |
| Underutilization report | Script 6 | CSV | Monthly archive |
| Group licensing config | Entra Admin Center | Screenshot | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SOX Section 404 (15 U.S.C. § 7262) | IT general controls over financial reporting — material technology expenditure authorization | PAYG budget authorization controls, billing-policy review, and per-seat license tracking support IT asset management control requirements |
| FFIEC Management Booklet, Section II.D | IT investment governance — cost-benefit analysis and ongoing cost monitoring | Per-seat versus PAYG documentation and monthly billing review help satisfy this expectation |
| OCC Heightened Standards (12 CFR Part 30, Appendix D) | Operational risk governance framework — technology cost management | Billing-policy review, anomaly detection, and monthly PAYG reporting demonstrate responsive cost governance |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for licensing issues
- Proceed to [Control 4.9](../4.9/portal-walkthrough.md) for incident reporting
