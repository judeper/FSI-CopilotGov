# Control 2.14: Declarative Agents from SharePoint Governance — Verification & Testing

Test cases and evidence collection for validating declarative agent governance.

## Test Cases

### Test 1: Agent Creation Restriction

- **Objective:** Confirm agent creation is restricted to approved users
- **Steps:**
  1. As a standard Copilot user (not in the approved creators group), attempt to create a declarative agent
  2. Verify the creation is blocked or not available
  3. As an approved creator, verify agent creation is possible
- **Expected Result:** Only approved users can create declarative agents
- **Evidence:** Creation attempt screenshots from both user types

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

### Test 4: Agent Governance Documentation

- **Objective:** Verify all active agents have governance approval documentation
- **Steps:**
  1. Compile the inventory of active declarative agents
  2. Cross-reference each agent against governance approval records
  3. Verify each agent has documented purpose, data source review, and approval
  4. Flag any agents without proper governance documentation
- **Expected Result:** All active agents have complete governance documentation
- **Evidence:** Agent inventory with governance approval cross-reference

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
