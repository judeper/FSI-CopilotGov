# Control 2.13: Plugin and Graph Connector Security — Verification & Testing

Test cases and evidence collection for validating plugin and connector security.

## Test Cases

### Test 1: External Agent and Unapproved Tool Block Verification

- **Objective:** Confirm external agents and unapproved plugin tools are blocked by default
- **Steps:**
  1. Confirm the external-publisher setting under **Microsoft 365 Admin Center > Agents > Settings > Allowed agent types**
  2. As a standard Copilot user, attempt to install an external partner agent or use an agent with an unapproved plugin
  3. Capture the policy or portal denial and export the corresponding Agent Registry or Agent Tools scope
- **Expected Result:** The external agent or unapproved tool is unavailable to the user
- **Evidence:** Agent setting, tool scope, and block notification. Do not use an operation-only `EnablePlugin` search as proof of Microsoft 365 Copilot state.

### Test 2: Admin Consent Enforcement

- **Objective:** Verify user consent is disabled and admin consent is required
- **Steps:**
  1. Run Script 3 and confirm `UserConsentDisabled` and `AdminConsentWorkflowEnabled` are both `True`
  2. As a standard user, access an app requiring consent — verify admin consent is required
  3. Submit an admin consent request and verify it routes correctly
  4. Review existing grants separately and confirm unauthorized grants have been revoked
- **Expected Result:** Users cannot self-consent; the request reaches an authorized reviewer; no unauthorized legacy grant remains
- **Evidence:** Script 3 output, request-workflow record, and existing-grant review

### Test 3: Graph Connector ACL Verification

- **Objective:** Confirm Graph connector ACLs correctly restrict content access
- **Steps:**
  1. Under **Microsoft 365 Admin Center > Copilot > Connectors > Your Connections**, verify each connection's access permission
  2. Test with a user who should not have access — verify content is not returned by Copilot
  3. Test with an authorized user — verify content is returned
- **Expected Result:** Connections configured for source ACLs show **Only people with access to this data source**, and access tests match the source system
- **Evidence:** Access test results for authorized and unauthorized users

### Test 4: Microsoft 365 Plugin Usage Evidence Boundary

- **Objective:** Confirm plugin usage evidence cannot include Security Copilot or an unapproved application or plugin
- **Steps:**
  1. Populate Script 4 with exact `AppIdentity` and `AISystemPlugin.ID` values from the approved inventory
  2. Invoke an approved plugin from an approved Microsoft 365 Copilot host
  3. Run Script 4 after audit ingestion completes
  4. Confirm every output row has `Workload = Copilot`, an exact approved `AppIdentity`, and an exact approved plugin ID
  5. Confirm `Copilot.Security.SecurityCopilot`, unknown application identities, and unapproved plugin IDs do not appear; retain rejected values separately for investigation
- **Expected Result:** The evidence set contains only inventory-matched Microsoft 365 Copilot plugin usage
- **Evidence:** Script 4 CSV, the application and plugin allow-lists used for the run, and the matching approval records

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Plugin permission audit | CSV | Compliance evidence repository | 7 years |
| Workload-scoped plugin usage audit | CSV plus application/plugin allow-lists | Compliance evidence repository | 7 years |
| Connector security audit | CSV | Compliance evidence repository | 7 years |
| Consent policy verification | PowerShell output and workflow record | Compliance evidence repository | 7 years |
| ACL test results | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| 12 CFR part 30, appendix D (OCC Heightened Standards) | Third-party risk management | Plugin security supports compliance with third-party technology risk requirements |
| FINRA Rule 3110 | Technology oversight | Plugin governance supports compliance with supervisory technology controls |
| NIST CSF | PR.IP-1 Baseline configuration | Plugin restrictions help establish and maintain secure baseline configurations |
- Back to [Control 2.13](../../../controls/pillar-2-security/2.13-plugin-connector-security.md)
