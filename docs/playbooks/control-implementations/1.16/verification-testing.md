# Control 1.16: Copilot Tuning Governance - Verification & Testing

Test cases and evidence collection for validating tenant scoping, request-and-approval flow integrity, snapshot lifecycle, and tuned-agent supervision.

## Test Cases

### Test 1: Tuning Is Disabled by Default

- **Objective:** Confirm Copilot Tuning is disabled at the tenant level until an explicit policy decision enables it.
- **Expected Result:** Tenant configuration shows tuning disabled or scoped to a named Entra group only.
- **Evidence:** `tuning-config.json` snapshot and the documented policy decision.

### Test 2: Only Authorized Requesters Can Request Tuning

- **Objective:** Validate that Copilot Tuning is scoped to a named Entra group and not to all licensed users.
- **Expected Result:** The requester group membership matches the approved access list; non-members cannot initiate a tuning request.
- **Evidence:** Requester group export and a denial screenshot from a controlled non-member test account.

### Test 3: Approval Flow Produces a Reviewable Record

- **Objective:** Confirm every tuning request results in a discoverable approval or denial record.
- **Expected Result:** Approval and denial events appear in the unified audit log with requester, approver, business justification, and decision rationale.
- **Evidence:** Audit-log export from the standing review cycle and the approval record in the governance workspace.

### Test 4: Excluded Data Sources Are Not Used in Tuning

- **Objective:** Validate that SharePoint locations excluded from tuning scope are not present in any tuning job's data source list.
- **Expected Result:** Tuned-agent metadata only references approved sites; no exclusion-list site appears as a tuning source.
- **Evidence:** `tuned-agents.csv` cross-referenced to the documented exclusion list.

### Test 5: Snapshot Lifecycle Honors Agent Deletion

- **Objective:** Confirm that deleting a tuned agent triggers deletion of the associated SharePoint snapshots.
- **Expected Result:** Deletion event is logged and downstream reconciliation shows no orphaned snapshots tied to the deleted agent.
- **Evidence:** Audit-event extract for the deletion plus a snapshot reconciliation report.

### Test 6: Output Supervision Is Operating

- **Objective:** Validate the named supervisor reviews tuned-agent outputs on the documented cadence.
- **Expected Result:** Supervision attestations exist for the review period, with sampled outputs reviewed and any issues recorded.
- **Evidence:** Supervision log and sampled output review records.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Tenant tuning configuration snapshot | PowerShell / Graph | JSON | Per retention policy |
| Authorized requesters group export | PowerShell / Graph | CSV | Per retention policy |
| Tuning approval / denial audit extract | Unified audit log | CSV | 7 years for regulated evidence sets |
| Tuned-agent inventory | PowerShell / Graph | CSV | Per retention policy |
| Model card per tuned agent | Governance workspace | PDF / Markdown | 7 years for regulated evidence sets |
| Output supervision attestations | Governance workspace | PDF / Markdown | Per retention policy |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Troubleshooting](troubleshooting.md)

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 1.16](../../../controls/pillar-1-readiness/1.16-copilot-tuning-governance.md)
