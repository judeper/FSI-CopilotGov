# Control 1.15: SharePoint Permissions Drift Detection - Verification & Testing

Test cases and evidence collection for validating baseline integrity, drift detection accuracy, and approval-gated reversion.

## Test Cases

### Test 1: Baseline Snapshot Matches the Approved State

- **Objective:** Confirm the stored baseline reflects the approved permissions state for the monitored site set.
- **Expected Result:** The baseline is complete, approved, and traceable to a governance decision.
- **Evidence:** Baseline snapshot, approval record, and sampled permission screenshots.

### Test 2: Known Drift Scenario Is Detected

- **Objective:** Validate that the workflow flags a deliberate permission change.
- **Expected Result:** Drift output reflects the changed state accurately and classifies it consistently.
- **Evidence:** Drift report and screenshot of the changed permission state.

### Test 3: Approved Change Windows Are Handled Correctly

- **Objective:** Confirm expected changes are documented and not treated as unexplained drift.
- **Expected Result:** Approved changes are distinguishable from unauthorized drift.
- **Evidence:** CAB or exception record and corresponding drift output.

### Test 4: Reversion Workflow Preserves Approval Control

- **Objective:** Validate that reversion actions are either approval-gated or follow the documented policy.
- **Expected Result:** Reversion outputs align to the approved auto-revert policy and governance model.
- **Evidence:** Reversion package and approval-routing record.

### Test 5: Evidence Package Supports Audit Review

- **Objective:** Confirm drift artifacts can be retrieved for an audit or examination request.
- **Expected Result:** Evidence is complete, reviewable, and retained with the related approvals.
- **Evidence:** Exported evidence package and retention-path confirmation.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Approved baseline snapshot | PowerShell | JSON / CSV | Per retention policy |
| Drift report | PowerShell | JSON / CSV | Per retention policy |
| Approved change reference | CAB / ticketing system | PDF / screenshot | Per retention policy |
| Reversion approval package | Governance workflow | JSON / PDF | 7 years for regulated evidence sets |
| Evidence export archive | PowerShell | ZIP / JSON | 7 years for regulated evidence sets |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Troubleshooting](troubleshooting.md)

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 1.15](../../../controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md)
