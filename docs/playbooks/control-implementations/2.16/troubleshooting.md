# Control 2.16: Federated Copilot Connector and MCP Governance - Troubleshooting

Common issues and resolution steps for federated connector inventory, scoping, authentication patterns, audit visibility, and DLP coverage.

## Common Issues

### Issue 1: New Federated Connectors Appear Without Notice

- **Symptoms:** Inventory pulls reveal connectors that were not previously approved.
- **Resolution:** Treat the new connector as un-vetted; restrict it to no users until [Control 1.10](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md) clears the vendor. Subscribe to the M365 message center for advance notice of upcoming connector rollouts.

### Issue 2: Users Authenticate Personal Accounts to a Connector

- **Symptoms:** Sign-in records show non-corporate identities completing OAuth to a federated service.
- **Resolution:** Update Acceptable Use guidance, communicate the policy, and apply conditional-access controls that restrict OAuth to firm-managed identities for regulated populations.

### Issue 3: Audit Events Are Missing

- **Symptoms:** Invocation audit pull returns zero rows for known connector activity.
- **Resolution:** Verify unified audit logging is enabled and that the operations list in the PowerShell setup matches the operations published by Microsoft for the tenant. Add any newly published operations and rerun.

### Issue 4: DLP Does Not Trigger on a Federated Response

- **Symptoms:** A controlled test response containing a known DLP keyword surfaced through a federated connector but did not raise an alert.
- **Resolution:** Confirm the DLP policy includes Copilot interactions in scope. Federated connector content is evaluated at the response layer; policies scoped only to email or SharePoint will not match Copilot responses.

### Issue 5: A Vendor Reassessment Is Overdue

- **Symptoms:** The third-party register shows a vendor reassessment past its scheduled date.
- **Resolution:** Restrict the connector to no users until the reassessment completes, capture the temporary restriction in the evidence workspace, and reinstate after sign-off.

## Diagnostic Steps

1. Snapshot the current connector posture and compare to the prior baseline.
2. Pull federated sign-in records for the review period and filter for non-corporate identities.
3. Cross-check audit-log operations against the published Microsoft operation set.
4. Run a controlled DLP test prompt against the connector returning a known keyword.
5. Reconcile scoped-group membership against the access-decision record.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Low | Inventory delta or documentation gap | Governance analyst |
| Medium | Personal-account authentication detected on a regulated workstream | Compliance lead and identity admin |
| High | Connector enabled without vendor-risk decision, or DLP coverage gap confirmed | CISO delegate, compliance lead, M365 admin |
| Critical | Confirmed exposure of customer NPI through a federated connector path | CISO, compliance officer, incident-response lead |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Verification & Testing](verification-testing.md)

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 2.16](../../../controls/pillar-2-security/2.16-federated-connector-mcp-governance.md)
