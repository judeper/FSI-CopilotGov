# Control 3.14: Copilot Pages and Notebooks Retention and Provenance - Troubleshooting

Common issues and resolution steps for retention scope, branch and embed lineage capture, eDiscovery, and attestation.

## Common Issues

### Issue 1: New Loop Workspace Falls Outside Retention Scope

- **Symptoms:** Inventory reveals a Loop workspace not covered by the tenant retention policy.
- **Resolution:** Update the retention policy to include the workspace's storage location, then capture an evidence snapshot showing the workspace is now in scope.

### Issue 2: Pages Branch Audit Events Are Missing

- **Symptoms:** Controlled branch tests do not appear in the lifecycle audit extract.
- **Resolution:** Verify unified audit logging is enabled and that `CopilotPageBranched` (and any successor operation Microsoft has published) is included in the operation set. Add and rerun.

### Issue 3: Notebook Section Retention Is Coarser Than Required

- **Symptoms:** A Notebook with mixed-purpose sections is governed by a single retention period, leaving sensitive sections under-retained.
- **Resolution:** Move sensitive sections into a dedicated Notebook scoped to the longer retention policy, and update the documentation.

### Issue 4: Loop Component Hosts Cannot Be Reconstructed

- **Symptoms:** Embed map is incomplete or shows components without hosts.
- **Resolution:** Validate the operation set includes `LoopComponentEmbedded` and `LoopComponentRemoved`. Re-run for the period, and document any gap before the operation was active.

### Issue 5: Hold Captures Parent but Not Branched Page

- **Symptoms:** eDiscovery hold export omits a branched Page that should be preserved.
- **Resolution:** Update the hold scope to follow the branch lineage, validate against the branch lineage report, and re-issue the hold.

### Issue 6: Quarterly Attestation Cannot Reconcile Unexplained Branches

- **Symptoms:** Attestation review identifies branches that the lineage report cannot match to a parent.
- **Resolution:** Document the unmatched branches, expand the lineage report to capture the gap source, and remediate before the next attestation cycle.

## Diagnostic Steps

1. Re-run the storage inventory and reconcile to retention policy scope.
2. Validate audit operation coverage against current Microsoft references.
3. Run a controlled branch and embed test and confirm both appear in the extracts.
4. Re-issue a controlled hold and confirm scope captures branches and embeds.
5. Reconcile the quarterly attestation against the branch lineage report.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Low | Documentation gap or minor reconciliation mismatch | Governance analyst |
| Medium | Audit operation gap or incomplete embed map | Governance lead and Purview admin |
| High | Hold scope misses branched or embedded artifacts, or retention scope gap on regulated content | Compliance lead and eDiscovery owner |
| Critical | Required record under SEC Rule 17a-4 cannot be produced | Compliance officer, CISO, eDiscovery owner |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Verification & Testing](verification-testing.md)

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 3.14](../../../controls/pillar-3-compliance/3.14-copilot-pages-notebooks-retention.md)
