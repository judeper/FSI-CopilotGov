# Control 4.14: Copilot Studio Agent Lifecycle Governance - Troubleshooting

Common issues and resolution steps for intake-to-deprecation lifecycle governance of Copilot Studio agents.

## Common Issues

### Issue 1: Agent Authored Without Intake Clearance

- **Symptoms:** A new agent appears in inventory with no linked Control 1.10 intake decision.
- **Resolution:** Suspend the agent in dev/test, route through intake, and only resume authoring after a current decision is recorded in the agent register.

### Issue 2: Publishing Occurred Without Test Sign-Off

- **Symptoms:** Publishing audit entry exists with no linked test results or approval record.
- **Resolution:** Treat as a control gap. Roll back the publish, complete testing, and re-run the publishing approval workflow with a documented post-mortem.

### Issue 3: Version Entry Missing for a Known Change

- **Symptoms:** Change-log shows a modification with no `CopilotStudioAgentVersionPublished` audit entry.
- **Resolution:** Verify unified audit logging is enabled and that the operation set in the PowerShell setup matches the operations Microsoft has published. Add and rerun. Document the gap.

### Issue 4: Register Drift Between Live Inventory and Agent Register

- **Symptoms:** `unregistered-published-agents.csv` or `register-only-agents.csv` is non-empty.
- **Resolution:** For unregistered live agents, suspend audience scope and route through intake retroactively. For register-only entries, confirm decommissioning and update the register with the final retirement record.

### Issue 5: Deprecation Did Not Remove Runtime Access

- **Symptoms:** Audit pull shows invocations of an agent after its deprecation date.
- **Resolution:** Re-run the deprecation playbook end-to-end, validate audience scope removal, capture final-state evidence, and update the playbook to capture the missed step.

### Issue 6: Lifecycle Attestation Missing for an Agent

- **Symptoms:** Periodic attestation report flags one or more agents without an in-period review record.
- **Resolution:** Reassign the named owner, complete the attestation, and document the cause of the gap.

## Diagnostic Steps

1. Reconcile live inventory to the agent register.
2. Validate audit operation coverage against current Microsoft references.
3. Re-run a controlled publishing flow and confirm test, approval, and audit linkage.
4. Re-run a controlled deprecation flow and confirm runtime removal.
5. Validate attestation completeness across the period.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Low | Documentation gap or single missed attestation | Governance analyst |
| Medium | Register drift or version-entry gap | Governance lead and Copilot Studio admin |
| High | Publishing without intake or test sign-off, or deprecation residual access | Compliance lead, M365 admin, Power Platform admin |
| Critical | Unregistered agent invoked against regulated data | CISO, compliance officer, incident-response lead |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Verification & Testing](verification-testing.md)

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 4.14](../../../controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md)
