# Control 1.14: Item-Level Permission Scanning - Troubleshooting

Common issues and resolution steps for item-level permission scanning and approval-gated remediation.

## Common Issues

### Issue 1: PnP Authentication Fails During Item Enumeration

- **Symptoms:** `Connect-PnPOnline` fails or prompts repeatedly without creating output.
- **Resolution:** Confirm the tenant-specific app registration, verify the client ID, and rerun against a single test site.

### Issue 2: Scan Volume Is Too Large

- **Symptoms:** Long runtimes, throttling, or oversized exports.
- **Resolution:** Reduce scope to the highest-risk libraries first and split scans by business unit or site collection.

### Issue 3: Too Many Legitimate Exceptions Are Flagged

- **Symptoms:** The scored output contains many items with documented business exceptions.
- **Resolution:** Reconcile the scan manifest with the exception register before changing thresholds.

### Issue 4: Remediation Output Lacks Approval Context

- **Symptoms:** Findings are exported without owner or approver detail.
- **Resolution:** Update the manifest with site owner, business owner, and compliance approver, then rebuild the remediation package.

### Issue 5: Sensitivity Information Is Missing

- **Symptoms:** Items appear without the expected label or classification fields.
- **Resolution:** Validate sensitivity-label coverage with Control 1.5 and document any scoring assumptions used during triage.

## Diagnostic Steps

1. Review the scan manifest and confirm scope, owners, and approvers.
2. Validate PnP authentication against a single target site.
3. Inspect the raw scan output before running the scoring step.
4. Compare flagged items to known exception registers and site-owner feedback.
5. Confirm evidence export paths and write permissions.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Low | Isolated false positives or missing metadata | SharePoint admin or site owner |
| Medium | Repeated scoring anomalies or large scan gaps | Governance lead and solution owner |
| High | High-risk items cannot be packaged for approval | Compliance lead and SharePoint admin |
| Critical | Regulated-content exposure is confirmed and active | CISO, compliance officer, and incident-response lead |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Verification & Testing](verification-testing.md)

*FSI Copilot Governance Framework v1.3 - April 2026*
- Back to [Control 1.14](../../../controls/pillar-1-readiness/1.14-item-level-permission-scanning.md)
