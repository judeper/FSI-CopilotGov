# Control 2.6: Copilot Web Search and Web Grounding Controls — Verification & Testing

Test cases and evidence collection for validating web search and grounding controls.

## Test Cases

### Test 1: Web Search Disabled Verification

- **Objective:** Confirm web search is disabled for Copilot users
- **Steps:**
  1. Verify web search is toggled off in Admin Center > Copilot > Web Search
  2. As a Copilot user, ask a question about a current event not in organizational data
  3. Verify Copilot does not return web-sourced content
  4. Verify Copilot indicates it can only reference organizational data
- **Expected Result:** Copilot does not use web search; responses based only on organizational data
- **Evidence:** Admin Center screenshot and Copilot response showing no web content

### Test 2: Web Plugin Block Verification

- **Objective:** Confirm web-accessing plugins are blocked by policy
- **Steps:**
  1. Run Script 2 to identify web-related plugins
  2. As a standard user, verify web plugins are not available
  3. Attempt to install a web-browsing plugin and verify it is blocked
- **Expected Result:** Web-accessing plugins are blocked by governance policy
- **Evidence:** Plugin block confirmation

### Test 3: Web Search Activity Monitoring

- **Objective:** Verify monitoring detects any web search usage
- **Steps:**
  1. Run Script 3 to check for web search activity in audit logs
  2. Verify zero web search events (if disabled)
  3. If events are found, investigate whether they occurred before the disable date
- **Expected Result:** Zero web search events after policy enforcement date
- **Evidence:** Audit log report showing no web search activity

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Web search configuration screenshot | PNG | Compliance evidence repository | 7 years |
| Web search test results | PDF | Compliance evidence repository | 7 years |
| Web search audit log report | CSV | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 2210 | Communications accuracy | Disabling web search helps prevent unverified external data in AI communications |
| SEC Regulation Best Interest | Reasonable basis for recommendations | Controlling web grounding supports compliance with recommendation basis requirements |
| NIST AI RMF | MEASURE 2.6 — AI system trustworthiness | Grounding controls support AI response trustworthiness |
- Back to [Control 2.6](../../../controls/pillar-2-security/2.6-web-search-controls.md)
