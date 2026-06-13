# Control 4.15: Copilot Cowork Governance - Troubleshooting

Common issues and resolution steps for governing Microsoft 365 Copilot Cowork during its Frontier preview.

## Common Issues

### Issue 1: Cowork Not Visible in Agent Management

- **Symptoms:** Cowork does not appear in the admin center under Copilot > Agents.
- **Resolution:** Confirm the administering account is enrolled in the Frontier preview program (Copilot > Settings > Frontier). Cowork is available only to Frontier-enrolled tenants and admins.

### Issue 2: Cowork Available to All Users by Default

- **Symptoms:** Users outside the approved pilot can discover and install Cowork.
- **Resolution:** In Copilot > Agents > All agents > Cowork, change availability from the default of all users to **Available to specific users or groups** scoped to the approved security group. Record the decision and approver.

### Issue 3: Installs Outside the Approved Scope

- **Symptoms:** `cowork-out-of-scope-installs.csv` is non-empty.
- **Resolution:** Verify the availability scope matches the approved group, investigate how out-of-scope users gained access, and document the exception or remediate the scope.

### Issue 4: Unapproved Plugin Available to Cowork

- **Symptoms:** A plugin not on the approved inventory is usable in Cowork.
- **Resolution:** Restrict the plugin through the admin plugin controls, reconcile the inventory, and route the plugin through extensibility governance under [Control 4.13](../../../controls/pillar-4-operations/4.13-extensibility-governance.md).

### Issue 5: Cowork Activity Missing from Audit

- **Symptoms:** Expected Cowork events do not appear in Purview audit pulls.
- **Resolution:** Confirm unified audit logging is enabled and that the operation set in the PowerShell setup matches current Microsoft references. Re-run the pull, and document any preview-related coverage gap with a remediation owner.

### Issue 6: Deployment Installed Cowork for Unintended Users

- **Symptoms:** Cowork appears for users who were not in the intended deployment scope.
- **Resolution:** Review the **Deploy to** scope, recognizing that deployment accepts users' permissions on their behalf. Re-scope or remove the deployment, and capture a corrected approval record.

## Diagnostic Steps

1. Confirm Frontier enrollment for the tenant and admin account.
2. Reconcile the availability scope against the approved pilot group.
3. Re-run the install activity report and review out-of-scope installs.
4. Reconcile the available plugin list against the approved inventory.
5. Validate audit coverage against current Microsoft references.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Low | Documentation gap or single out-of-scope install | Governance analyst |
| Medium | Availability scope drift or unapproved plugin available | Governance lead and M365 admin |
| High | Cowork enabled for a regulated population without supervisory review | Compliance lead and M365 admin |
| Critical | Agentic Cowork action against regulated data outside approved governance | CISO, compliance officer, incident-response lead |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Verification & Testing](verification-testing.md)

*FSI Copilot Governance Framework v1.7.1 - April 2026*
- Back to [Control 4.15](../../../controls/pillar-4-operations/4.15-copilot-cowork-governance.md)
