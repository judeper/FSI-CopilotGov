# Control 4.4: Copilot in Viva Suite Governance — Verification & Testing

Test cases and evidence collection procedures for Copilot governance across the Microsoft Viva suite.

## Test Cases

### Test 1: Viva Engage Copilot Content Compliance

- **Objective:** Verify that Copilot-assisted Viva Engage posts are captured by communication compliance
- **Steps:**
  1. Use Copilot to draft a Viva Engage post as a test user.
  2. Publish the post to a monitored community.
  3. Verify the post appears in the Communication compliance review queue if it matches policy conditions.
  4. Confirm the post metadata identifies it as Copilot-assisted.
- **Expected Result:** Copilot-assisted Engage posts are captured by communication compliance policies.
- **Evidence:** Communication compliance review queue showing the Engage post.

### Test 2: Viva Learning Compliance Training Integrity

- **Objective:** Confirm that Copilot AI recommendations do not bypass mandatory compliance training
- **Steps:**
  1. Verify mandatory compliance training courses are configured in Viva Learning.
  2. Use Copilot to request learning recommendations.
  3. Confirm Copilot recommendations supplement but do not replace mandatory training.
  4. Verify completion tracking for mandatory training is independent of AI recommendations.
- **Expected Result:** Mandatory compliance training integrity is maintained alongside Copilot recommendations.
- **Evidence:** Training completion reports showing mandatory courses are tracked independently.

### Test 3: Viva Goals Data Boundary Enforcement

- **Objective:** Validate that Copilot in Viva Goals respects organizational data boundaries
- **Steps:**
  1. Create test goals in Viva Goals at different organizational levels.
  2. Use Copilot to request goal suggestions and progress analysis.
  3. Verify that Copilot only references data the user is authorized to access.
  4. Confirm that confidential executive goals are not surfaced to unauthorized users.
- **Expected Result:** Copilot respects organizational hierarchies and access controls in Viva Goals.
- **Evidence:** Test results showing data boundary enforcement.

### Test 4: Viva Connections Content Sensitivity

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
| Engage compliance test | Communication compliance | Screenshot | With control documentation |
| Learning compliance report | Viva Learning | CSV | With control documentation |
| Goals access test results | Viva Goals | Screenshot | With control documentation |
| Connections sensitivity test | Viva Connections | Screenshot | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FINRA 3110 | Supervision of internal communications | Supports monitoring of AI-assisted Viva Engage communications |
| FFIEC Management Booklet | IT governance | Helps meet governance requirements for enterprise collaboration AI |
| SOX 404 | Internal controls | Supports governance of AI tools affecting business processes |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for Viva Copilot issues
- Proceed to [Control 4.5](../4.5/portal-walkthrough.md) for usage analytics
