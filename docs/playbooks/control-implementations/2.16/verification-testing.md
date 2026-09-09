# Control 2.16: Federated Copilot Connector and MCP Governance - Verification & Testing

Test cases and evidence collection for validating federated connector inventory, scoping, authentication posture, DLP coverage, and vendor monitoring.

## Test Cases

### Test 1: Connector Inventory Matches the Approved Catalog

- **Objective:** Confirm the tenant-wide publisher-category posture and connector-specific access assignments match the firm's approved list.
- **Expected Result:** **Allowed agent types** matches the approved tenant posture; each connector available to users has a corresponding vendor-risk decision; every unapproved connector is scoped to **No users**.
- **Evidence:** Saved **Allowed agent types** settings, per-connector allowed-user and staged-rollout captures from **Copilot connectors > Your connections**, and `connector-posture.csv` cross-referenced to the third-party register.

### Test 2: Disabled Connectors Are Truly Unavailable to End Users

- **Objective:** Validate that connectors marked disabled cannot be invoked from Copilot.
- **Expected Result:** A controlled unapproved user cannot connect to or invoke the connector. The connector may remain visible to administrators, so administrative catalog visibility is not a pass/fail criterion.
- **Evidence:** Connector-specific **No users** or excluded-group setting plus a screenshot from a controlled unapproved account and the corresponding audit result showing no successful invocation.

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
| Tenant-wide publisher-category settings | M365 Admin Center > Agents > Settings > Allowed agent types | PDF / screenshot | Per retention policy |
| Connector allowed-user and staged-rollout settings | M365 Admin Center > Copilot connectors > Your connections | PDF / screenshot | Per retention policy |
| Supplemental connector inventory | PowerShell / Graph | CSV | Per retention policy |
| Controlled approved/unapproved user access test | Microsoft 365 Copilot | PDF / screenshot | Per retention policy |
| Federated sign-in record | PowerShell / Graph | CSV | Per retention policy |
| Connector invocation audit extract | Unified audit log | CSV | 7 years for regulated evidence sets |
| Scoped-group membership snapshot | PowerShell / Graph | CSV | Per retention policy |
| Vendor-risk decision per connector | Governance workspace | PDF / Markdown | Per retention policy |
| DLP test artifacts | Purview / Compliance portal | PDF / Markdown | Per retention policy |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Troubleshooting](troubleshooting.md)

*FSI Copilot Governance Framework v1.8.0 - July 2026*
- Back to [Control 2.16](../../../controls/pillar-2-security/2.16-federated-connector-mcp-governance.md)
