# Control 4.1: Copilot Admin Settings and Feature Management — Verification & Testing

Test cases and evidence collection procedures to validate Copilot administrative settings and feature controls.

## Test Cases

### Test 1: Feature Availability by Group

- **Objective:** Verify that Copilot features are only available to approved user groups
- **Steps:**
  1. Log in as a user in the approved Copilot group and verify Copilot is available in Word, Excel, and Teams.
  2. Log in as a user NOT in the approved group and verify Copilot is not available.
  3. Log in as a user in the excluded group and verify Copilot features are blocked.
  4. Document the results for each user test.
- **Expected Result:** Copilot features are available only to approved groups and blocked for excluded groups.
- **Evidence:** Screenshots showing feature availability for each test user type.

### Test 2: Web Grounding Configuration

- **Objective:** Confirm that web grounding is disabled for regulated environments
- **Steps:**
  1. Verify the web grounding setting in the M365 Admin Center shows "Disabled".
  2. As a Copilot user, attempt a query that would typically use web content.
  3. Verify that Copilot responses only use organizational data, not web sources.
  4. Check audit logs for any web grounding activity.
- **Expected Result:** Web grounding is disabled and Copilot does not reference web content.
- **Evidence:** Admin Center configuration screenshot and test query results.

### Test 3: Plugin Access Controls

- **Objective:** Validate that only approved plugins are accessible to Copilot users
- **Steps:**
  1. Review the plugin access settings in the M365 Admin Center.
  2. Verify the list of approved plugins matches the governance policy.
  3. As a test user, attempt to use an approved plugin and confirm it works.
  4. Verify that non-approved plugins are not visible or accessible.
- **Expected Result:** Only governance-approved plugins are available to Copilot users.
- **Evidence:** Plugin settings screenshot and test results.

### Test 4: License Assignment Accuracy

- **Objective:** Confirm that Copilot licenses are assigned only to approved users
- **Steps:**
  1. Run the license assignment report script.
  2. Cross-reference assigned users against the approved deployment list.
  3. Identify any unauthorized assignments (users with licenses who are not on the approved list).
  4. Identify any missing assignments (approved users without licenses).
- **Expected Result:** 100% alignment between license assignments and the approved deployment list.
- **Evidence:** License assignment comparison report.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Feature configuration | M365 Admin Center | Screenshot | With control documentation |
| Web grounding status | Admin Center | Screenshot | With control documentation |
| Plugin access settings | Admin Center | Screenshot | With control documentation |
| License assignment report | PowerShell | CSV | Monthly archive |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FFIEC Management Booklet | IT governance and access control | Supports compliance with technology governance and feature management |
| OCC Heightened Standards | Technology risk management | Helps meet expectations for centralized technology controls |
| NYDFS 23 NYCRR 500 | Access controls | Supports access control requirements for AI technology |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for configuration issues
- Proceed to [Control 4.2](../4.2/portal-walkthrough.md) for Teams Meetings governance
