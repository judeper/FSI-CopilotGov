# Control 4.1: Copilot Admin Settings and Feature Management — Verification & Testing

Test cases and evidence collection procedures to validate Copilot Control System administrative settings and feature controls.

## Test Cases

### Test 1: Copilot Overview Dashboard Accessibility

- **Objective:** Verify that the MAC > Copilot > Overview dashboard is accessible and displays current governance posture
- **Steps:**
  1. Navigate to M365 Admin Center > Copilot > Overview.
  2. Confirm the license utilization summary section displays current assignment data.
  3. Confirm the security posture section is visible and shows current status.
  4. Confirm the recommended actions section is populated (if applicable).
  5. Verify that the security posture links to DSPM for AI, DLP policies, and sensitivity label coverage work correctly.
- **Expected Result:** Dashboard accessible; all four dashboard sections (licenses, security, analytics, recommended actions) visible and populated.
- **Evidence:** Screenshots of the Copilot > Overview dashboard showing all sections.

### Test 2: Baseline Security Mode Verification

- **Objective:** Confirm that Baseline Security Mode is enabled and settings are documented
- **Steps:**
  1. Navigate to M365 Admin Center > Copilot > Settings > Security.
  2. Verify Baseline Security Mode shows as enabled.
  3. Review the list of defaults applied by Baseline Security Mode.
  4. Confirm that any customizations applied beyond the baseline are documented in the configuration register.
  5. For Regulated tier: verify deviation documentation exists for any settings that differ from the Microsoft baseline.
- **Expected Result:** Baseline Security Mode enabled; customizations documented.
- **Evidence:** Screenshot of Baseline Security Mode status; configuration register entry.

### Test 3: Feature Availability by Group

- **Objective:** Verify that Copilot features are only available to approved user groups
- **Steps:**
  1. Log in as a user in the approved Copilot group and verify Copilot is available in Word, Excel, and Teams.
  2. Log in as a user NOT in the approved group and verify Copilot is not available.
  3. Log in as a user in the excluded group and verify Copilot features are blocked.
  4. Document the results for each user test.
- **Expected Result:** Copilot features are available only to approved groups and blocked for excluded groups.
- **Evidence:** Screenshots showing feature availability for each test user type.

### Test 4: Web Grounding Configuration

- **Objective:** Confirm that web grounding is disabled for regulated environments
- **Steps:**
  1. Verify the web grounding setting in M365 Admin Center > Copilot > Settings shows "Disabled".
  2. As a Copilot user, attempt a query that would typically use web content.
  3. Verify that Copilot responses only use organizational data, not web sources.
  4. Check audit logs for any web grounding activity.
- **Expected Result:** Web grounding is disabled and Copilot does not reference web content.
- **Evidence:** Admin Center configuration screenshot and test query results.

### Test 5: Copilot for Admins Availability

- **Objective:** Verify Copilot for Admins is accessible and that changes made through it follow the standard change management workflow
- **Steps:**
  1. As a Copilot Administrator, navigate to M365 Admin Center and verify the Copilot for Admins interface is available.
  2. Use Copilot for Admins to query current Copilot policy state.
  3. Verify that any configuration recommendation generated requires a separate change approval before implementation.
  4. Confirm the change management workflow documentation covers Copilot for Admins-assisted changes.
- **Expected Result:** Copilot for Admins accessible; no changes implemented without CAB approval.
- **Evidence:** Screenshot confirming Copilot for Admins availability; change management process documentation.

### Test 6: License Assignment Accuracy

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
| Copilot overview dashboard | MAC > Copilot > Overview | Screenshot | With control documentation |
| Baseline Security Mode status | MAC > Copilot > Settings | Screenshot | With control documentation |
| Feature configuration | MAC > Copilot > Settings | Screenshot | With control documentation |
| Web grounding status | Admin Center | Screenshot | With control documentation |
| Plugin access settings | Admin Center | Screenshot | With control documentation |
| License assignment report | PowerShell | CSV | Monthly archive |
| Copilot for Admins availability | MAC admin interface | Screenshot | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SOX Section 404 | IT general controls for financial reporting systems | Copilot Control System dashboard provides centralized evidence of ongoing governance oversight |
| FFIEC Management Booklet | IT governance and access control | Supports compliance with technology governance and feature management |
| OCC Heightened Standards | Technology risk management | Helps meet expectations for centralized technology controls |
| NYDFS 23 NYCRR 500 | Access controls | Supports access control requirements for AI technology |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for configuration issues
- Proceed to [Control 4.2](../4.2/portal-walkthrough.md) for Teams Meetings governance
