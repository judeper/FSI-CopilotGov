# Control 1.14: Item-Level Permission Scanning - Verification & Testing

Test cases and evidence collection for validating item-level permission scanning coverage, scoring, and remediation governance.

## Test Cases

### Test 1: Scan Scope Matches Approved Manifest

- **Objective:** Confirm the scan ran only against approved sites and libraries.
- **Expected Result:** Scan scope aligns to the approved manifest with no undocumented site expansion.
- **Evidence:** Approved manifest, run log, and output folder listing.

### Test 2: Uniquely Permissioned Items Are Detected

- **Objective:** Validate that the scan finds files or folders with broken inheritance or broad sharing.
- **Expected Result:** Known exceptions appear in the output with accurate item path and permission context.
- **Evidence:** Scan CSV excerpt and screenshot of the matching SharePoint permission view.

### Test 3: Risk Scoring Reflects FSI Priorities

- **Objective:** Confirm high-risk items are scored appropriately based on sharing type and data sensitivity.
- **Expected Result:** Risk tiers align with the documented thresholds and business expectations.
- **Evidence:** Risk-threshold configuration and scored report sample.

### Test 4: Approval Gate Output Is Complete

- **Objective:** Validate that remediation actions are packaged with the information needed for approval.
- **Expected Result:** Remediation artifacts are complete, reviewable, and approval-gated.
- **Evidence:** Remediation CSV or JSON and approval-routing notes.

### Test 5: Evidence Package Is Examination Ready

- **Objective:** Confirm evidence exports are complete and stored in the expected structure.
- **Expected Result:** Evidence artifacts are complete, named consistently, and retrievable for review.
- **Evidence:** Evidence package contents and retention location screenshot.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Scan manifest | Governance team | Markdown / CSV | Per retention policy |
| Item permission scan output | PowerShell | CSV | Per retention policy |
| Risk-scored report | PowerShell | CSV / JSON | Per retention policy |
| Remediation approval package | Governance workflow | CSV / PDF | 7 years for regulated evidence sets |
| Evidence export archive | PowerShell | ZIP / JSON | 7 years for regulated evidence sets |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Troubleshooting](troubleshooting.md)

*FSI Copilot Governance Framework v1.2.1 - March 2026*
