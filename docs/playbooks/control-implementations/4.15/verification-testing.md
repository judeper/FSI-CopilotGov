# Control 4.15: Copilot Cowork Governance - Verification & Testing

Test cases and evidence collection for validating Frontier enrollment, availability scoping, deployment/pinning approvals, plugin governance, and supervision coverage for Microsoft 365 Copilot Cowork during preview.

## Test Cases

### Test 1: Availability Is Scoped, Not Default-All

- **Objective:** Confirm Cowork availability is set to an approved group (or blocked) rather than the default of all licensed users.
- **Expected Result:** The admin-center availability setting for Cowork matches the documented decision; only approved users see Cowork in the Agent Store.
- **Evidence:** Availability decision record and an admin-center screenshot or export.

### Test 2: Frontier Enrollment Is Documented

- **Objective:** Validate that tenant and admin Frontier enrollment is recorded.
- **Expected Result:** Enrollment status is captured in the register, and Cowork visibility in Agent management is consistent with that status.
- **Evidence:** Frontier enrollment record.

### Test 3: Installs Stay Within Approved Scope

- **Objective:** Confirm Cowork installs occur only within the approved pilot group.
- **Expected Result:** `cowork-out-of-scope-installs.csv` is empty after reconciliation; any exceptions have a documented approval.
- **Evidence:** Install activity report reconciled to approved-group membership.

### Test 4: Deployment and Pinning Have Approvals

- **Objective:** Validate that any deployment or pinning of Cowork is approved and scoped.
- **Expected Result:** Each deployment/pinning decision has an approval record naming the approver and target group.
- **Evidence:** Approval records reconciled to admin-center deployment/pinning configuration.

### Test 5: Plugin Inventory Matches Approved List

- **Objective:** Confirm plugins available to Cowork match the approved inventory.
- **Expected Result:** Available plugins and connector authentication match the approved-plugin inventory; unapproved plugins are not available.
- **Evidence:** Plugin inventory and the approved-plugin list.

### Test 6: Supervision and Audit Coverage Confirmed

- **Objective:** Validate that Cowork activity is visible to existing audit and supervision tooling.
- **Expected Result:** Cowork-related events appear in Purview audit pulls; any coverage gaps are documented with a remediation owner.
- **Evidence:** `cowork-agent-audit.csv` and the documented coverage assessment.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Availability decision record | Governance workspace | CSV / Markdown | Per retention policy |
| Frontier enrollment record | Governance workspace | PDF / Markdown | Per retention policy |
| Cowork audit extract | Unified audit log | CSV | 7 years for regulated evidence sets |
| Install activity report | PowerShell post-processing | CSV | Per retention policy |
| Deployment/pinning approvals | Governance workspace | PDF / Markdown | 7 years for regulated evidence sets |
| Approved-plugin inventory | Governance workspace | CSV / Markdown | Per retention policy |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Troubleshooting](troubleshooting.md)

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 4.15](../../../controls/pillar-4-operations/4.15-copilot-cowork-governance.md)
