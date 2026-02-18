# Control 4.1: Copilot Admin Settings and Feature Management — Portal Walkthrough

Step-by-step portal configuration for managing Microsoft 365 Copilot administrative settings and feature controls through the Copilot Control System in the Microsoft 365 Admin Center.

## Prerequisites

- **Role:** Global Administrator, Copilot Administrator, or Microsoft 365 Service Administrator
- **License:** Microsoft 365 E5 with Copilot add-on
- **Access:** Microsoft 365 Admin Center (admin.microsoft.com)

## Steps

### Step 1: Access the Copilot Control System Overview Dashboard

**Portal:** Microsoft 365 Admin Center
**Path:** Copilot > Overview

1. Navigate to the Microsoft 365 Admin Center at admin.microsoft.com.
2. In the left navigation, select **Copilot** to expand the Copilot Control System section.
3. Select **Overview** to open the Copilot dashboard.
4. Review each dashboard section:
   - **License summary** — verify license assignments match the approved deployment list
   - **Security posture** — check for flagged gaps (sensitivity labels, DLP, Conditional Access)
   - **Usage analytics** — review adoption trends and feature engagement
   - **Recommended actions** — evaluate each recommendation before acting
5. Use the overview dashboard as the starting point for all Copilot governance activities — it provides links directly to relevant configuration areas.

### Step 2: Configure Baseline Security Mode

**Portal:** Microsoft 365 Admin Center
**Path:** Copilot > Settings > Security

1. From the Copilot Control System dashboard, navigate to **Copilot > Settings**.
2. Select the **Security** tab to access Baseline Security Mode settings.
3. Enable **Baseline Security Mode** to apply Microsoft's recommended security defaults.
4. Review the default settings applied:
   - Sensitivity label requirements for Copilot interactions
   - DLP policy defaults for Copilot data access
   - Conditional Access configuration for Copilot-licensed users
5. Document the baseline configuration in the configuration register.
6. For Recommended and Regulated tiers: note any customizations applied beyond the baseline and document the business justification.

### Step 3: Configure Feature Availability by User Group

**Portal:** Microsoft 365 Admin Center
**Path:** Copilot > Settings > Feature settings

1. From the Copilot section, navigate to **Settings > Feature settings**.
2. Review each Copilot feature and its current availability:
   - Copilot in Word, Excel, PowerPoint, Outlook, Teams
   - Microsoft 365 Copilot Chat
   - Copilot in Loop, OneNote, Whiteboard
3. For each feature, set availability by group:
   - **Pilot group** — initial rollout users for testing
   - **General availability group** — broader workforce access
   - **Excluded group** — users restricted from specific features (e.g., temporary workers, compliance-restricted roles)
4. Save configuration changes and document in the change register with approval reference.

### Step 4: Configure Data and Privacy Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Copilot > Settings > Data and privacy

1. From the Copilot section, navigate to **Settings > Data and privacy**.
2. Review and configure:
   - **Web grounding** — Enable or disable Copilot's ability to reference web content (recommended: Disabled for regulated environments)
   - **Plugin access** — Control which plugins are available to Copilot users
   - **Feedback collection** — Configure whether user feedback data is sent to Microsoft
3. For FSI environments, set data and privacy settings to the most restrictive options during initial deployment.

### Step 5: Configure Copilot License Assignment

**Portal:** Microsoft 365 Admin Center
**Path:** Billing > Licenses > Microsoft 365 Copilot

1. Review current license assignments.
2. Cross-reference against the license utilization summary from the Copilot > Overview dashboard.
3. Assign Copilot licenses only to approved user groups per the governance plan.
4. Remove licenses from users who have left the pilot group or no longer require access.
5. Document the license assignment policy and approval workflow.

### Step 6: Access Security Posture Details from Dashboard

**Portal:** Microsoft 365 Admin Center
**Path:** Copilot > Overview > Security posture links

1. From the Copilot > Overview dashboard, use the security posture section to navigate directly to:
   - **DSPM for AI** — review data exposure findings for Copilot grounding sources
   - **DLP policies** — verify Copilot surfaces are covered by data loss prevention policies
   - **Sensitivity labels** — confirm label coverage for documents and communications accessible to Copilot
2. Address any recommended actions flagged in the security posture section.
3. Document completion of recommended actions in the governance register.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Baseline Security Mode | Enabled | Enabled + customized | Enabled + fully customized |
| Web grounding | Enabled | Disabled | Disabled |
| Plugin access | All plugins | Approved plugins only | Approved plugins only |
| Feedback collection | Enabled | Organization-controlled | Disabled |
| Feature rollout | All at once | Phased by group | Phased with compliance review |
| Overview dashboard review | Quarterly | Monthly | Weekly |

## Regulatory Alignment

- **SOX Section 404** — Copilot > Overview dashboard provides centralized evidence of IT general controls governance and ongoing oversight
- **FFIEC Management Booklet** — Supports compliance with IT governance and change management requirements
- **OCC Heightened Standards** — Helps meet technology governance expectations for large institutions
- **NYDFS Cybersecurity Regulation** — Supports access control and technology governance requirements

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for administrative automation
- See [Verification & Testing](verification-testing.md) to validate configuration
