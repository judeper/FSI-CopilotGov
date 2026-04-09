# Control 2.14: Declarative Agents from SharePoint Governance — Verification & Testing

Test cases and evidence collection for validating agent access, sharing, Registry review, and SharePoint-backed knowledge governance.

## Test Cases

### Test 1: Agent Access and Creation Restriction

- **Objective:** Confirm agent access and agent creation are restricted to approved users
- **Steps:**
  1. As a standard Copilot user outside the approved scope, attempt to access and create agents.
  2. Verify the experience is blocked or not available.
  3. As an approved user, verify the intended access path is available.
- **Expected Result:** Only approved users can access or create governed agents.
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

- **Objective:** Confirm third-party model providers are disabled (default) or restricted to approved providers
- **Steps:**
  1. Navigate to M365 Admin Center > Copilot > Settings and verify the third-party model provider setting.
  2. If disabled (recommended default): document the setting and confirm it matches the governance policy.
  3. If enabled: verify a vendor risk assessment has been completed, document which providers are approved, and confirm data classification restrictions are in place.
  4. Test that agents cannot invoke unapproved model providers.
- **Expected Result:** Third-party model provider setting matches governance policy; unapproved providers are blocked.
- **Evidence:** Admin Center screenshot of the third-party model provider setting and governance policy document.

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
| OCC Model Risk Management | Model governance | Agent governance supports compliance with AI model governance requirements |
| FINRA Rule 3110 | Technology supervision | Agent oversight supports compliance with supervisory technology requirements |
| NIST AI RMF | GOVERN 1.1 — AI system governance | Formal agent governance supports compliance with AI governance requirements |
