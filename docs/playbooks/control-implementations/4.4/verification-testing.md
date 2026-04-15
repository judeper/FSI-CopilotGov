# Control 4.4: Copilot in Viva Suite Governance — Verification & Testing

Test cases and evidence collection procedures for Copilot governance across the Microsoft Viva suite.

## Test Cases

### Test 1: Copilot Chat Insights Data Availability

- **Objective:** Verify that Copilot Chat usage analytics are available in Viva Insights and respect privacy thresholds
- **Steps:**
  1. Navigate to the Viva Insights Advanced portal at `insights.viva.office.com`.
  2. Access **Analyst Workbench > Copilot Dashboard** and verify the Copilot Chat usage metrics tab is present.
  3. Confirm that department-level Copilot Chat adoption data is visible and shows aggregated metrics (not individual query content).
  4. Verify that departments with fewer users than the configured minimum group size show suppressed (no data) rather than individual-level data.
  5. Run Script 1 from the PowerShell Setup guide and confirm output matches the Viva Insights portal display.
- **Expected Result:** Copilot Chat insights are available at department level, individual query data is not accessible, and small departments are appropriately suppressed.
- **Evidence:** Screenshots of the Copilot Dashboard with department adoption data; Script 1 output CSV.

### Test 2: Engage-to-Teams Retention Policy Coverage

- **Objective:** Verify that Viva Engage content surfacing in Teams is captured by retention and compliance policies
- **Steps:**
  1. Identify a Viva Engage community that is connected to a Teams channel via the Engage-to-Teams integration.
  2. Post a test message in the Engage community using Copilot-assisted drafting.
  3. Verify the message appears in the connected Teams channel.
  4. In Microsoft Purview > eDiscovery, search for the test message using both Yammer and Teams location filters — confirm it appears in both locations.
  5. Run Script 4 from the PowerShell Setup guide and confirm retention policies exist for both Yammer and Teams locations.
- **Expected Result:** Engage content surfacing in Teams is captured by the organization's Teams retention policies and communication compliance policies.
- **Evidence:** eDiscovery search results showing message in both locations; Script 4 retention policy validation output.

### Test 3: Viva Engage Copilot Content Compliance

- **Objective:** Verify that Copilot-assisted Viva Engage posts are captured by communication compliance
- **Steps:**
  1. Use Copilot to draft a Viva Engage post as a test user.
  2. Publish the post to a monitored community.
  3. Verify the post appears in the Communication compliance review queue if it matches policy conditions.
  4. Confirm the post metadata identifies it as Copilot-assisted.
- **Expected Result:** Copilot-assisted Engage posts are captured by communication compliance policies.
- **Evidence:** Communication compliance review queue showing the Engage post.

### Test 4: Viva Learning Compliance Training Integrity

- **Objective:** Confirm that Copilot AI recommendations do not bypass mandatory compliance training
- **Steps:**
  1. Verify mandatory compliance training courses are configured in Viva Learning.
  2. Use Copilot to request learning recommendations.
  3. Confirm Copilot recommendations supplement but do not replace mandatory training.
  4. Verify completion tracking for mandatory training is independent of AI recommendations.
- **Expected Result:** Mandatory compliance training integrity is maintained alongside Copilot recommendations.
- **Evidence:** Training completion reports showing mandatory courses are tracked independently.

### Test 5: Viva Goals Data Boundary Enforcement

!!! warning "Retired"
    Viva Goals was retired December 31, 2025. This test case is no longer applicable.

- **Objective:** Validate that Copilot in Viva Goals respects organizational data boundaries
- **Steps:**
  1. Create test goals in Viva Goals at different organizational levels.
  2. Use Copilot to request goal suggestions and progress analysis.
  3. Verify that Copilot only references data the user is authorized to access.
  4. Confirm that confidential executive goals are not surfaced to unauthorized users.
- **Expected Result:** Copilot respects organizational hierarchies and access controls in Viva Goals.
- **Evidence:** Test results showing data boundary enforcement.

### Test 6: Viva Connections Content Sensitivity

- **Objective:** Verify that Copilot respects sensitivity labels when surfacing content in Viva Connections
- **Steps:**
  1. Create test news articles with different sensitivity labels.
  2. Access Viva Connections as a user and use Copilot to search for news.
  3. Verify that highly sensitive content is not surfaced to users without appropriate permissions.
  4. Confirm sensitivity label visual markings appear on surfaced content.
- **Expected Result:** Sensitivity labels are respected and content access is appropriately controlled.
- **Evidence:** Screenshots showing sensitivity-appropriate content surfacing.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Copilot Chat insights data availability | Viva Insights portal + Script 1 | Screenshot + CSV | With control documentation |
| Engage-to-Teams retention coverage | Purview eDiscovery + Script 4 | Screenshot + Script output | With control documentation |
| Engage compliance test | Communication compliance | Screenshot | With control documentation |
| Learning compliance report | Viva Learning | CSV | With control documentation |
| Goals access test results | Viva Goals | Screenshot | With control documentation |
| Connections sensitivity test | Viva Connections | Screenshot | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FINRA 3110 | Supervision of internal communications | Supports monitoring of AI-assisted Viva Engage communications, including content surfacing through Teams integration |
| FFIEC Management Booklet, Section II.C | IT risk monitoring — technology usage pattern oversight | Copilot Chat analytics in Viva Insights supports this monitoring expectation |
| SOX 404 | Internal controls | Supports governance of AI tools affecting business processes |
| EEOC AI Guidance | Non-discriminatory use of AI analytics | Privacy-protected Copilot Chat analytics help ensure individual query data is not used for employment decisions |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for Viva Copilot issues
- Proceed to [Control 4.5](../4.5/portal-walkthrough.md) for usage analytics
- Back to [Control 4.4](../../../controls/pillar-4-operations/4.4-viva-suite-governance.md)
