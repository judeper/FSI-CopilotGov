# Control 2.14: Declarative Agents from SharePoint Governance — Verification & Testing

Test cases and evidence collection for validating agent access, sharing, Registry review, and SharePoint-backed knowledge governance.

## Test Cases

### Test 1: Agent Access, Installation, and Publishing Restrictions

- **Objective:** Confirm agent access, installation, and broad publishing are restricted to approved users or groups where the tenant exposes controls
- **Steps:**
  1. As a standard Copilot user outside the approved scope, attempt to access, install, and broadly share or publish agents through the available tenant surfaces.
  2. Verify the access/install/publishing experience is blocked or not available according to the configured control.
  3. As an approved user, verify the intended access path is available.
  4. Separately record whether the tenant exposes a direct creation restriction for the specific authoring surface; do not infer creation blocking from **User access**, which governs consumption.
- **Expected Result:** Only approved users can access, install, or broadly publish governed agents through the tenant's available controls; any authoring-surface creation restrictions are explicitly verified.
- **Evidence:** Screenshots from both user types.

### Test 2: Agent Data Source Security

- **Objective:** Verify all active agent data sources meet security requirements
- **Steps:**
  1. Run Script 2 to check source site security posture
  2. Verify all sources have sensitivity labels applied
  3. Verify sharing is appropriately restricted on all source sites
  4. Confirm no oversharing exists on agent source sites
- **Expected Result:** All agent data sources meet minimum security requirements
- **Evidence:** Source site security report

### Test 3: Agent Scope Limitation

- **Objective:** Confirm agents only access content within their defined scope
- **Steps:**
  1. Select an active declarative agent with a specific site scope
  2. Ask the agent a question that would require content outside its scope
  3. Verify the agent only responds with content from its defined data source
  4. Verify no content leakage from other sites
- **Expected Result:** Agent responses limited to defined content scope
- **Evidence:** Agent interaction showing scope enforcement

### Test 4: Registry, Agent 365, and Governance Documentation

- **Objective:** Verify all active agents have Registry visibility, Agent 365 inventory coverage, ownership, Entra Agent ID (where applicable), and governance approval documentation
- **Steps:**
  1. Compile the inventory of active agents from the Registry, Agent 365 dashboard, or equivalent export.
  2. Cross-reference each agent against governance approval records
  3. Verify each agent has documented purpose, owner, data source review, and approval
  4. For Recommended/Regulated tiers: verify agents have an Entra Agent ID assigned
  5. Flag any agents without proper governance documentation or owner assignment
- **Expected Result:** All active agents have complete governance documentation and ownership; Entra Agent IDs assigned at Recommended/Regulated tiers.
- **Evidence:** Agent inventory with governance approval cross-reference and Entra Agent ID assignments.

### Test 5: Third-Party Model Provider Policy

- **Objective:** Confirm any tenant-exposed third-party model-provider setting is disabled or restricted to approved providers
- **Steps:**
  1. Navigate to the current M365 Admin Center / Copilot / Agent settings surfaces and verify whether a third-party model-provider setting or equivalent control is present.
  2. If present and disabled: document the setting and confirm it matches the governance policy.
  3. If present and enabled: verify a vendor risk assessment has been completed, document which providers are approved, and confirm data-classification restrictions are in place.
  4. If not present: record "not available in tenant" with date and reviewer rather than treating the absence as a disabled default.
  5. Test that agents cannot invoke unapproved model providers where a test path exists.
- **Expected Result:** Any tenant-exposed third-party model-provider setting matches governance policy; unapproved providers are blocked or the setting is recorded as unavailable in the tenant.
- **Evidence:** Admin Center screenshot of the setting or absence, governance policy document, and any invocation test.

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Agent inventory | CSV | Compliance evidence repository | 7 years |
| Source site security report | CSV | Compliance evidence repository | 7 years |
| Agent scope test results | PDF | Compliance evidence repository | 7 years |
| Governance approval records | PDF | Governance document repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| OCC model-risk governance | Model governance | Potential internal mapping for firm/counsel review; agent governance can provide evidence for the firm's AI governance process |
| FINRA Rule 3110 | Technology supervision | Potential supervisory-system mapping for firm/counsel review; agent oversight can support documented technology supervision |
| NIST AI RMF | GOVERN 1.1 — AI system governance | Voluntary framework mapping; formal agent governance can provide AI governance evidence |
- Back to [Control 2.14](../../../controls/pillar-2-security/2.14-declarative-agents-governance.md)
