# Control 2.17: Cross-Tenant Agent Federation - Troubleshooting

Common issues and resolution steps for cross-tenant Agent ID trust, MCP attestation, multi-tenant publishing, supervisory observability, and termination.

## Common Issues

### Issue 1: Inbound Agent Trust From an Unapproved Tenant

- **Symptoms:** CTAP partner list shows an external tenant that has not been cleared under [Control 1.10](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md).
- **Resolution:** Suspend the partner, snapshot the configuration, and route through vendor-risk review before reinstating.

### Issue 2: MCP Federated Server Lacks Signed Attestation

- **Symptoms:** A registered MCP server reports `attestationStatus` other than `signed`.
- **Resolution:** Treat the registration as un-attested; restrict invocations and require the operating tenant to provide a signed attestation before further use.

### Issue 3: Copilot Studio Agent Reaches an Unsanctioned Tenant

- **Symptoms:** Publishing-target export shows a receiving tenant not on the approved list.
- **Resolution:** Remove the unsanctioned target from the publishing list, capture an evidence snapshot, and confirm the receiving tenant has uninstalled the agent.

### Issue 4: Supervisory Reconstruction Misses Cross-Tenant Activity

- **Symptoms:** Supervision review cannot reconstruct an invocation involving an external tenant.
- **Resolution:** Validate that unified audit logging is enabled and that the cross-tenant operation set in the PowerShell setup matches the operations Microsoft has published. Add any newly published operations and rerun.

### Issue 5: Residual Trust After Relationship Termination

- **Symptoms:** Termination drill or post-termination review finds residual Entra trust, MCP registration, or Copilot Studio installation.
- **Resolution:** Execute the termination playbook end-to-end, document each removal, and update the playbook to capture the missed step.

### Issue 6: Data-Residency Attestation Conflicts With Cross-Tenant Path

- **Symptoms:** External tenant's signed attestation lists processing regions outside the firm's approved data-residency boundary.
- **Resolution:** Suspend the trust pending compliance review; do not reinstate without an updated attestation or a documented exception approved by the data-residency owner.

## Diagnostic Steps

1. Snapshot CTAP defaults and partner list; reconcile to the third-party register.
2. Cross-check MCP attestation status against the on-file attestations.
3. Reconcile publishing-target lists against the approved receiving-tenant list.
4. Re-run the cross-tenant audit pull and validate operation coverage.
5. Execute the termination playbook against a controlled test partner.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Low | Documentation gap in cross-tenant inventory | Governance analyst |
| Medium | Un-attested MCP server or unsanctioned publishing target | Identity admin and compliance lead |
| High | Confirmed inbound Agent trust to unapproved tenant, or supervisory-reconstruction gap | CISO delegate, compliance lead, M365 admin |
| Critical | Customer NPI confirmed flowing to or from an unapproved external tenant | CISO, compliance officer, incident-response lead |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Verification & Testing](verification-testing.md)

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 2.17](../../../controls/pillar-2-security/2.17-cross-tenant-agent-federation.md)
