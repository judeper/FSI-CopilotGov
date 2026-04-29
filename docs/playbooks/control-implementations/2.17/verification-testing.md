# Control 2.17: Cross-Tenant Agent Federation - Verification & Testing

Test cases and evidence collection for validating cross-tenant trust scope, MCP attestation, multi-tenant publishing, supervisory observability, and termination integrity.

## Test Cases

### Test 1: Cross-Tenant Access Defaults Deny Inbound Agent Trust

- **Objective:** Confirm CTAP defaults deny inbound Agent ID trust unless an external tenant is explicitly added.
- **Expected Result:** Default policy excludes inbound Agent ID; only named external tenants appear in the partner list.
- **Evidence:** `ctap-default.json` and `ctap-partners.json` snapshots.

### Test 2: Each Trusted External Tenant Has a Vendor-Risk Decision

- **Objective:** Validate that every partner with inbound Agent ID trust corresponds to a [Control 1.10](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md) vendor-risk decision.
- **Expected Result:** Every partner is reconciled to an active vendor-risk record.
- **Evidence:** Partner list cross-referenced to the third-party register.

### Test 3: MCP Federated Servers Carry Signed Attestation

- **Objective:** Confirm each registered MCP federated server has a signed attestation covering operating tenant, provenance, data residency, and incident notification.
- **Expected Result:** Every server in `mcp-federated-servers.csv` shows `attestationStatus = signed` and matches the attestation record on file.
- **Evidence:** MCP inventory and the corresponding signed attestations.

### Test 4: Copilot Studio Publishing Targets Are Approved

- **Objective:** Validate that published agents authored by the firm are only available to receiving tenants on the approved publishing-target list.
- **Expected Result:** Published-agent target list matches the approved list; no unsanctioned tenants are listed.
- **Evidence:** Publishing-target export and the approval record.

### Test 5: Cross-Tenant Invocations Are Reconstructable

- **Objective:** Confirm cross-tenant invocations are observable for supervisory review.
- **Expected Result:** Audit entries identify caller identity, target external tenant, and the action taken for the review period.
- **Evidence:** `cross-tenant-audit.csv` for the period under review.

### Test 6: Termination Playbook Removes Residual Trust

- **Objective:** Validate that ending a cross-tenant relationship removes Entra trust, MCP registration, and Copilot Studio installation residuals.
- **Expected Result:** A controlled termination drill yields zero residual records for the test partner across all three patterns.
- **Evidence:** Termination drill report and final-state snapshots.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| CTAP default and partner snapshots | PowerShell / Graph | JSON | Per retention policy |
| Agent identity inventory | PowerShell / Graph | CSV | Per retention policy |
| MCP federated server inventory and attestations | PowerShell / Graph + governance workspace | CSV / PDF | 7 years for regulated evidence sets |
| Copilot Studio publishing-target list and approvals | Copilot Studio export | CSV / PDF | 7 years for regulated evidence sets |
| Cross-tenant invocation audit extract | Unified audit log | CSV | 7 years for regulated evidence sets |
| Termination drill report | Governance workspace | PDF / Markdown | Per retention policy |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Troubleshooting](troubleshooting.md)

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 2.17](../../../controls/pillar-2-security/2.17-cross-tenant-agent-federation.md)
