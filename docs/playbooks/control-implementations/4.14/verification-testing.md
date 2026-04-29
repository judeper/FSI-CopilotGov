# Control 4.14: Copilot Studio Agent Lifecycle Governance - Verification & Testing

Test cases and evidence collection for validating intake clearance, stage transitions, publishing approvals, version history, and deprecation integrity.

## Test Cases

### Test 1: Authoring Begins Only After Intake Clearance

- **Objective:** Confirm every agent in authoring has a recorded Control 1.10 intake decision.
- **Expected Result:** Agent register entries cite a current intake decision identifier; agents lacking one are blocked from authoring.
- **Evidence:** Agent register and the linked intake decisions.

### Test 2: Testing Is a Gate Before Publishing

- **Objective:** Validate that publishing requires a passing test result.
- **Expected Result:** A controlled agent with failing tests cannot be published; the publishing approver record references the test result.
- **Evidence:** Test plan, results, and the publishing approval record.

### Test 3: Publishing Approval Workflow Is Operating

- **Objective:** Confirm publishing produces an approval record with named approver.
- **Expected Result:** Each `CopilotStudioAgentPublished` audit event has a corresponding approval record with named approver and audience scope.
- **Evidence:** `agent-lifecycle-audit.csv` reconciled to publishing approval records.

### Test 4: Versioning Policy Captures Every Change

- **Objective:** Validate that subsequent changes generate version entries with change-log content.
- **Expected Result:** `agent-version-history.csv` shows a version entry for each in-period change; orphan changes are flagged.
- **Evidence:** Version history report and source change log.

### Test 5: Register Reconciles to Live Inventory

- **Objective:** Confirm the agent register matches the live inventory.
- **Expected Result:** `unregistered-published-agents.csv` and `register-only-agents.csv` are empty after reconciliation.
- **Evidence:** Reconciliation outputs from the PowerShell setup.

### Test 6: Deprecation Playbook Removes Runtime Access

- **Objective:** Validate that deprecated agents are removed from runtime surfaces.
- **Expected Result:** A controlled deprecation drill yields a final retirement record, no remaining audience scope, and no further runtime invocations after the cutover.
- **Evidence:** Deprecation drill report and post-deprecation audit extract.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Agent register | Governance workspace | CSV / Markdown | Per retention policy |
| Live agent inventory | PowerShell / Power Platform admin | CSV | Per retention policy |
| Lifecycle audit extract | Unified audit log | CSV | 7 years for regulated evidence sets |
| Version history report | PowerShell post-processing | CSV | 7 years for regulated evidence sets |
| Publishing approval records | Governance workspace | PDF / Markdown | 7 years for regulated evidence sets |
| Deprecation drill report | Governance workspace | PDF / Markdown | Per retention policy |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Troubleshooting](troubleshooting.md)

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 4.14](../../../controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md)
