# Control 2.6: Copilot Web Search and Web Grounding Controls — Verification & Testing

Test cases and evidence collection for validating web search and grounding controls.

## Test Cases

### Test 1: Web Search Disabled Verification

- **Objective:** Confirm web search is disabled for Copilot users
- **Steps:**
  1. Verify the **Allow web search in Copilot** Cloud Policy is configured to off in the Microsoft 365 Apps admin center (`https://config.office.com` > Customization > Policy Management), and confirm the policy exists rather than relying on the unconfigured default
  2. As a Copilot user, ask a question about a current event not in organizational data
  3. Verify Copilot does not return web-sourced content, and that the **Web content** toggle is turned off and dimmed for the user
  4. Verify Copilot indicates it can only reference organizational data
- **Expected Result:** Copilot does not use web search; responses based only on organizational data
- **Evidence:** Cloud Policy configuration screenshot and Copilot response showing no web content

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

### Test 4: Graph Beta Tenant-Level Setting Evidence

- **Objective:** Corroborate the Cloud Policy state with the public Graph beta `microsoft.copilot.allowwebsearch` setting without assuming an undocumented value map
- **Steps:**
  1. Run Script 1 to query `GET https://graph.microsoft.com/beta/copilot/admin/policySettings/microsoft.copilot.allowwebsearch`
  2. Record the returned raw `value` and `policyId`
  3. Compare the raw value to the visible **Allow web search in Copilot** Cloud Policy option in `https://config.office.com`
  4. Document the tenant-observed mapping as evidence; do not reuse it as a public 0/1/2 mapping unless Microsoft publishes one
- **Expected Result:** The Graph beta tenant-level setting corroborates the Cloud Policy UI, or the discrepancy is documented and escalated
- **Evidence:** Graph response JSON plus Cloud Policy screenshot

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Web search Cloud Policy configuration screenshot | PNG | Compliance evidence repository | 7 years |
| Graph beta `microsoft.copilot.allowwebsearch` response | JSON | Compliance evidence repository | 7 years |
| Web search test results | PDF | Compliance evidence repository | 7 years |
| Web search audit log report | CSV | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 2210 | Communications accuracy | Disabling web search helps prevent unverified external data in AI communications |
| SEC Regulation Best Interest | Reasonable basis for recommendations | Controlling web grounding supports compliance with recommendation basis requirements |
| NIST AI RMF | MEASURE 2.6 — AI system trustworthiness | Grounding controls support AI response trustworthiness |
- Back to [Control 2.6](../../../controls/pillar-2-security/2.6-web-search-controls.md)
