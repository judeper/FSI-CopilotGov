# Control 1.16: Copilot Tuning Governance - Troubleshooting

Common issues and resolution steps for Copilot Tuning enablement, request flow, scoping, snapshot lifecycle, and supervision.

## Common Issues

### Issue 1: Copilot Tuning Settings Are Not Visible in the Admin Center

- **Symptoms:** The Copilot Tuning configuration surface does not appear, or the option is greyed out.
- **Resolution:** Confirm the tenant meets the 5,000-license eligibility threshold and that the signed-in admin holds the required Copilot or M365 administrator role. If both are satisfied, verify the feature has rolled out to the tenant region.

### Issue 2: Tuning Requests Reach Users Outside the Approved Group

- **Symptoms:** Users not in the authorized requester group see the tuning request entry point.
- **Resolution:** Re-scope tuning to the Entra security group rather than relying on tenant-wide enablement, then validate by signing in as a controlled out-of-group test account.

### Issue 3: Approval Flow Lacks a Reviewable Record

- **Symptoms:** Audit queries return no approval or denial entries for known tuning requests.
- **Resolution:** Verify unified audit logging is enabled and that the operation set in Script 3 of the PowerShell setup matches the audit operations active in the tenant. Add any newly published operations and rerun.

### Issue 4: Excluded SharePoint Site Appears in a Tuned Agent's Data Sources

- **Symptoms:** Reconciliation shows a tuned agent referencing a site on the documented exclusion list.
- **Resolution:** Quarantine the tuned agent, capture an evidence snapshot, and route through the deprecation workflow. Re-validate the site-exclusion configuration before any retraining.

### Issue 5: Orphan Snapshots After Agent Deletion

- **Symptoms:** Snapshot inventory still references a deleted tuned agent.
- **Resolution:** Open a Microsoft support case to confirm snapshot lifecycle behavior, then retain the evidence package and reconciliation report until the orphan is cleared.

### Issue 6: Output Supervision Cadence Is Slipping

- **Symptoms:** Supervision attestations are missing for one or more review periods.
- **Resolution:** Reassign the named supervisor, document the gap, and require backfilled sampling before the next review cycle.

## Diagnostic Steps

1. Validate eligibility, role assignments, and feature availability.
2. Confirm tuning is scoped via Entra group rather than tenant-wide.
3. Cross-check tuned-agent data sources to the documented exclusion list.
4. Re-run the audit-log extract for the latest review window.
5. Review supervision attestations for completeness across the period.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Low | Documentation gap or single missed attestation | Governance analyst |
| Medium | Approval-flow record missing or supervisor unavailable | Governance lead and model risk owner |
| High | Tuned agent uses excluded data, or orphan snapshots persist | Compliance lead, model risk owner, M365 admin |
| Critical | Confirmed exposure of regulated data in tuned-agent training scope | CISO, compliance officer, incident-response lead |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Verification & Testing](verification-testing.md)

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 1.16](../../../controls/pillar-1-readiness/1.16-copilot-tuning-governance.md)
