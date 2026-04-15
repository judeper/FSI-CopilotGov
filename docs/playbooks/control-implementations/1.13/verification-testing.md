# Control 1.13: Extensibility Readiness — Verification & Testing

Test cases and evidence collection for validating Copilot extensibility governance.

## Test Cases

### Test 1: Extension Inventory Completeness

- **Objective:** Verify all active Copilot extensions are documented and approved
- **Steps:**
  1. Run PowerShell Script 1 to generate the current app inventory
  2. Run Script 2 to list active Graph connectors
  3. Cross-reference against the approved extensions list
  4. Identify any unauthorized or undocumented extensions
- **Expected Result:** All active extensions are documented in the approved list
- **Evidence:** Extension inventory with approval status annotations

### Test 2: Extension Governance Policy Enforcement

- **Objective:** Confirm governance policies prevent unauthorized extension installation
- **Steps:**
  1. As a standard user, attempt to install a third-party Teams app that is not on the approved list
  2. Verify the installation is blocked by the permission policy
  3. Verify the appropriate error message is displayed
  4. Confirm the blocked attempt is logged
- **Expected Result:** Unauthorized extension installation is blocked by policy
- **Evidence:** Screenshot of blocked installation attempt and audit log entry

### Test 3: Graph Connector Data Access Review

- **Objective:** Verify each Graph connector's data access scope is appropriate
- **Steps:**
  1. For each active Graph connector, review the data source and access permissions
  2. Verify the connector only ingests data that is approved for Copilot grounding
  3. Confirm access controls on ingested content align with the data classification
  4. Verify connector configurations have governance approval documentation
- **Expected Result:** All Graph connectors have appropriate, documented data access scopes
- **Evidence:** Connector configuration review with governance approval records

### Test 4: Extension Approval Workflow Validation

- **Objective:** Verify the extension approval process works as designed
- **Steps:**
  1. Submit a test extension approval request through the documented process
  2. Verify the request routes to the correct reviewers
  3. Confirm the security review and data access assessment steps are executed
  4. Verify the approval or rejection is documented and communicated
- **Expected Result:** Approval workflow functions correctly with all review steps completed
- **Evidence:** Test approval request with workflow step documentation

### Test 5: Custom Agent Governance Compliance

- **Objective:** Verify custom-built agents meet governance requirements
- **Steps:**
  1. Identify any custom agents deployed via Copilot Studio
  2. Review each agent's data source configuration and access scope
  3. Verify each agent has passed the required security review
  4. Confirm each agent has governance committee approval
- **Expected Result:** All custom agents comply with governance requirements
- **Evidence:** Agent configuration review with approval documentation

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Extension inventory | CSV | Compliance evidence repository | 7 years |
| Governance policy configuration | Screenshot/PDF | Compliance evidence repository | 7 years |
| Graph connector review records | PDF | Compliance evidence repository | 7 years |
| Approval workflow documentation | PDF | Governance document repository | 7 years |
| Custom agent review records | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory systems and WSPs | Extension governance supports compliance with technology oversight requirements |
| OCC Heightened Standards | IT risk management | Extension approval process supports compliance with IT risk management standards |
| NIST CSF | PR.IP-1 Baseline configuration | Extension governance establishes and maintains baseline configurations |
| NIST AI RMF | MAP 5 — AI system components | Extension inventory maps AI system component dependencies |
- Back to [Control 1.13](../../../controls/pillar-1-readiness/1.13-extensibility-readiness.md)
