# Control 2.16: Federated Copilot Connector and MCP Governance - Verification & Testing

Test cases and evidence collection for validating federated connector inventory, scoping, authentication posture, DLP coverage, and vendor monitoring.

## Test Cases

### Test 1: Connector Inventory Matches the Approved Catalog

- **Objective:** Confirm the live federated connector catalog matches the firm's approved list.
- **Expected Result:** Each enabled connector has a corresponding vendor-risk decision; no unapproved connector is enabled.
- **Evidence:** `connector-posture.csv` cross-referenced to the third-party register.

### Test 2: Disabled Connectors Are Truly Unavailable to End Users

- **Objective:** Validate that connectors marked disabled cannot be invoked from Copilot.
- **Expected Result:** A controlled test prompt does not return content from a disabled connector; the connector does not appear in the user's connectors list.
- **Evidence:** Screenshot from a controlled test account and the corresponding audit entry showing no invocation.

### Test 3: Personal-Account Authentication Is Restricted Where Required

- **Objective:** Confirm the Acceptable Use posture on personal-account authentication is enforced for regulated workstreams.
- **Expected Result:** Sign-in records show only firm-managed identities authenticating to in-scope connectors, or out-of-scope authentications are detected and routed to compliance.
- **Evidence:** `federated-signins.csv` and any compliance routing records.

### Test 4: DLP Evaluates Federated Connector Responses

- **Objective:** Validate that DLP policies covering Copilot interactions also evaluate federated connector responses surfaced in those interactions.
- **Expected Result:** A controlled prompt that pulls a sensitive-keyword response from a federated connector triggers the expected DLP policy tip or block.
- **Evidence:** DLP alert record and Copilot interaction transcript.

### Test 5: Invocation Audit Trail Supports Reconstruction

- **Objective:** Confirm audit events allow reconstruction of who invoked which connector with what target.
- **Expected Result:** Audit entries identify user, connector, target service, and timestamp for the review window.
- **Evidence:** `connector-invocations.csv` for the period under review.

### Test 6: Scope Membership Aligns to Vendor Risk Decisions

- **Objective:** Validate that group membership for scoped connectors matches the vendor-risk-approved population.
- **Expected Result:** No out-of-scope users appear in the scoped Entra group, and no in-scope user is missing.
- **Evidence:** `connector-scope-membership.csv` reconciled to the access-decision record.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Connector posture snapshot | PowerShell / Graph | CSV | Per retention policy |
| Federated sign-in record | PowerShell / Graph | CSV | Per retention policy |
| Connector invocation audit extract | Unified audit log | CSV | 7 years for regulated evidence sets |
| Scoped-group membership snapshot | PowerShell / Graph | CSV | Per retention policy |
| Vendor-risk decision per connector | Governance workspace | PDF / Markdown | Per retention policy |
| DLP test artifacts | Purview / Compliance portal | PDF / Markdown | Per retention policy |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Troubleshooting](troubleshooting.md)

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 2.16](../../../controls/pillar-2-security/2.16-federated-connector-mcp-governance.md)
