# Control 4.8: Cost Allocation and License Optimization — Verification & Testing

Test cases and evidence collection procedures for Copilot cost allocation and license optimization.

## Test Cases

### Test 1: License Inventory Accuracy

- **Objective:** Verify that the license inventory report matches the actual license state in the tenant
- **Steps:**
  1. Run the license inventory script.
  2. Compare the script output with the M365 Admin Center Billing > Licenses page.
  3. Verify total purchased, assigned, and available counts match.
  4. Confirm the per-user cost matches the contracted price.
- **Expected Result:** Script output matches Admin Center data exactly.
- **Evidence:** Side-by-side comparison of script output and Admin Center screenshot.

### Test 2: Group-Based License Assignment

- **Objective:** Confirm that group-based licensing correctly assigns and removes licenses
- **Steps:**
  1. Add a test user to a Copilot license group.
  2. Wait for the license to be assigned (up to 24 hours).
  3. Verify the user has a Copilot license in their profile.
  4. Remove the user from the group and verify the license is removed.
- **Expected Result:** Licenses are automatically assigned and removed based on group membership.
- **Evidence:** Screenshots showing group membership change and license status.

### Test 3: Chargeback Report Accuracy

- **Objective:** Validate that department chargeback calculations correctly allocate costs
- **Steps:**
  1. Run the department chargeback report.
  2. Manually verify 3 departments by counting their licensed users.
  3. Confirm the cost calculation uses the correct per-user rate.
  4. Verify the total across all departments equals the total license cost.
- **Expected Result:** Chargeback allocations are mathematically correct and total matches overall spend.
- **Evidence:** Chargeback report with manual verification notes.

### Test 4: Underutilization Detection Accuracy

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
| License inventory | PowerShell/Admin Center | CSV | Monthly archive |
| Chargeback report | PowerShell | CSV | Monthly archive |
| Underutilization report | PowerShell | CSV | Monthly archive |
| Group licensing config | Entra Admin Center | Screenshot | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SOX 404 | IT asset management controls | Supports compliance with IT asset tracking and cost controls |
| FFIEC Management Booklet | IT investment governance | Helps meet technology cost management requirements |
| OCC Heightened Standards | Resource governance | Supports expectations for technology resource optimization |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for licensing issues
- Proceed to [Control 4.9](../4.9/portal-walkthrough.md) for incident reporting
