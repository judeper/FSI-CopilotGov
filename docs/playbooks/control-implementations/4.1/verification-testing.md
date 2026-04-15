# Control 4.1: Copilot Admin Settings and Feature Management — Verification & Testing

Test cases and evidence collection procedures to validate Copilot administrative settings across Copilot, Agents, Cloud Policy, and billing controls.

## Test Cases

### Test 1: Copilot Overview Accessibility

- **Objective:** Verify designated reviewers can access the Copilot overview dashboard
- **Steps:**
  1. Navigate to **M365 Admin Center > Copilot > Overview**.
  2. Confirm overview content is populated and recent.
  3. Capture evidence of who performed the review.
- **Expected Result:** Dashboard accessible to approved admins or reviewers.
- **Evidence:** Screenshot of the overview page and review log entry.

### Test 2: Copilot Settings Baseline Review

- **Objective:** Confirm Copilot settings are documented across the current tab model
- **Steps:**
  1. Open **Copilot > Settings**.
  2. Review **User access**, **Data access**, **Copilot actions**, and **Other settings**.
  3. Compare the current configuration with the approved baseline.
- **Expected Result:** No undocumented deviations from the approved configuration.
- **Evidence:** Settings screenshots and baseline comparison notes.

### Test 3: Web Search Configuration

- **Objective:** Confirm web search matches the approved FSI posture
- **Steps:**
  1. Open **Copilot > Settings > Data access**.
  2. Verify the web search setting is configured as approved.
  3. If disabled, run a prompt that would normally use public web content and confirm no web-grounded response is returned.
- **Expected Result:** Web search posture matches policy.
- **Evidence:** Setting screenshot and user test result.

### Test 4: Agent Governance Settings

- **Objective:** Confirm agents are governed according to approved policy
- **Steps:**
  1. Open **Agents > Settings**.
  2. Review allowed agent types, sharing, and user access.
  3. Validate the visible configuration against the approved governance baseline.
- **Expected Result:** Agent settings align with documented governance decisions.
- **Evidence:** Screenshots from agent settings and the governance register.

### Test 5: Copilot Pages / Notebooks Policy Scope

- **Objective:** Confirm Cloud Policy scope is correct
- **Steps:**
  1. Open the Microsoft 365 Cloud Policy service.
  2. Review **Create and view Copilot Pages and Copilot Notebooks**.
  3. Confirm the policy targets only the intended user population.
- **Expected Result:** Cloud Policy scope matches the approved rollout group.
- **Evidence:** Policy screenshot and group assignment evidence.

### Test 6: Billing and Self-Service Controls

- **Objective:** Confirm cost-enablement controls are governed
- **Steps:**
  1. Review **Settings > Org settings > Self-service trials and purchases**.
  2. Review **Billing > Pay-as-you-go services**.
  3. Confirm any active billing policy or self-service exception is documented and approved.
- **Expected Result:** Billing-related Copilot controls match policy.
- **Evidence:** Screenshots and approval references.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Copilot overview review | M365 Admin Center > Copilot > Overview | Screenshot | With control documentation |
| Copilot settings baseline | M365 Admin Center > Copilot > Settings | Screenshot / notes | With control documentation |
| Agent settings review | M365 Admin Center > Agents > Settings | Screenshot | With control documentation |
| Cloud Policy scope | Microsoft 365 Cloud Policy service | Screenshot | With control documentation |
| Billing and self-service posture | M365 Admin Center | Screenshot | With control documentation |
| License assignment report | PowerShell | CSV | Monthly archive |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SOX Section 404 | IT general controls for financial reporting systems | Supports evidence of governed Copilot configuration and change review |
| FFIEC Management Booklet | IT governance and access control | Supports centralized administration and least-privilege review |
| 12 CFR part 30, appendix D (OCC Heightened Standards) | Technology risk management | Helps document ongoing control of AI feature rollout and spend pathways |
| NYDFS 23 NYCRR 500 | Access controls | Supports use of limited administrator roles and documented access decisions |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for configuration issues
- Proceed to [Control 4.2](../4.2/portal-walkthrough.md) for Teams Meetings governance
- Back to [Control 4.1](../../../controls/pillar-4-operations/4.1-admin-settings-feature-management.md)
