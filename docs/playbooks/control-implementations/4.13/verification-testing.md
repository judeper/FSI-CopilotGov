# Control 4.13: Copilot Extensibility Governance (Plugin Lifecycle) — Verification & Testing

Test cases and evidence collection procedures for Copilot extensibility governance and plugin lifecycle management.

## Test Cases

### Test 1: User Consent Blocking

- **Objective:** Verify that users cannot self-consent to new Copilot plugins without admin approval
- **Steps:**
  1. Log in as a standard Copilot user.
  2. Attempt to add or enable a third-party plugin that is not in the approved catalog.
  3. Verify the request is blocked and the user is directed to the request workflow.
  4. Confirm the admin team receives the request notification.
- **Expected Result:** User consent is blocked and the request is routed through the approval workflow.
- **Evidence:** Screenshots showing the blocked consent attempt and admin notification.

### Test 2: Plugin Approval Workflow

- **Objective:** Validate the end-to-end plugin approval workflow
- **Steps:**
  1. Submit a test plugin request through the user request workflow.
  2. Walk through the three-level approval chain (IT, Compliance, Business).
  3. Verify each approver receives the request with the Plugin Risk Assessment.
  4. Complete the approval and verify the plugin is made available.
- **Expected Result:** Plugin approval workflow completes through all levels with documented approvals.
- **Evidence:** Approval workflow records showing each approval level.

### Test 3: Plugin Access Control by Group

- **Objective:** Confirm that plugin access is correctly restricted by user group
- **Steps:**
  1. Configure a plugin to be available only to a specific user group.
  2. Log in as a user in the approved group and verify plugin access.
  3. Log in as a user outside the approved group and verify the plugin is not available.
  4. Change group membership and verify access updates accordingly.
- **Expected Result:** Plugin access follows group membership restrictions.
- **Evidence:** Screenshots showing plugin availability per group membership.

### Test 4: Graph Connector Data Sensitivity Assessment

- **Objective:** Verify that Graph connectors exposing data to Copilot have been assessed for sensitivity
- **Steps:**
  1. Run the Graph connector inventory script.
  2. For each connector, verify a data sensitivity assessment is on file.
  3. Confirm appropriate access controls are applied to connector data.
  4. Verify sensitivity labels are applied to connector content where applicable.
- **Expected Result:** All Graph connectors have documented sensitivity assessments and appropriate controls.
- **Evidence:** Connector inventory with sensitivity assessment completion status.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Plugin inventory | PowerShell | CSV | Monthly archive |
| Approval workflow records | Microsoft 365 admin center | Screenshot/Export | 7 years |
| Permission audit | PowerShell | CSV | Monthly archive |
| Connector sensitivity assessments | Assessment documents | PDF | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FFIEC Development Booklet | Third-party software governance | Supports compliance with software acquisition and deployment governance |
| OCC Bulletin 2013-29 (Third-Party Relationships) | Vendor risk management | Helps meet third-party risk management for plugin providers |
| NYDFS 23 NYCRR 500 | Third-party security assessment | Supports security assessment of third-party service providers |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for plugin governance issues
- Return to [Pillar 4 Overview](../../index.md) for the complete control listing
