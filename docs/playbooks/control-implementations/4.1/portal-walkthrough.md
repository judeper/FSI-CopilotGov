# Control 4.1: Copilot Admin Settings and Feature Management — Portal Walkthrough

Step-by-step portal configuration for managing Microsoft 365 Copilot administrative settings and feature controls across the organization.

## Prerequisites

- **Role:** Global Administrator or Microsoft 365 Service Administrator
- **License:** Microsoft 365 E5 with Copilot add-on
- **Access:** Microsoft 365 Admin Center

## Steps

### Step 1: Access Copilot Admin Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Copilot

1. Navigate to the Microsoft 365 Admin Center.
2. Go to **Settings > Copilot** to access the centralized Copilot configuration page.
3. Review the current feature enablement status for each Copilot capability.

### Step 2: Configure Feature Availability by User Group

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Copilot > Feature settings

1. Review each Copilot feature and its current availability:
   - Copilot in Word, Excel, PowerPoint, Outlook, Teams
   - Microsoft 365 Copilot Chat
   - Copilot in Loop, OneNote, Whiteboard
2. For each feature, set availability by group:
   - **Pilot group** — initial rollout users for testing
   - **General availability group** — broader workforce access
   - **Excluded group** — users restricted from specific features (e.g., temporary workers, compliance-restricted roles)
3. Save configuration changes.

### Step 3: Configure Data and Privacy Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Copilot > Data and privacy

1. Review and configure:
   - **Web grounding** — Enable or disable Copilot's ability to reference web content (recommended: Disabled for regulated environments)
   - **Plugin access** — Control which plugins are available to Copilot users
   - **Feedback collection** — Configure whether user feedback data is sent to Microsoft
2. For FSI environments, set data and privacy settings to the most restrictive options during initial deployment.

### Step 4: Configure Copilot License Assignment

**Portal:** Microsoft 365 Admin Center
**Path:** Billing > Licenses > Microsoft 365 Copilot

1. Review current license assignments.
2. Assign Copilot licenses only to approved user groups per the governance plan.
3. Remove licenses from users who have left the pilot group or no longer require access.
4. Document the license assignment policy and approval workflow.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Web grounding | Enabled | Disabled | Disabled |
| Plugin access | All plugins | Approved plugins only | Approved plugins only |
| Feedback collection | Enabled | Organization-controlled | Disabled |
| Feature rollout | All at once | Phased by group | Phased with compliance review |

## Regulatory Alignment

- **FFIEC Management Booklet** — Supports compliance with IT governance and change management requirements
- **OCC Heightened Standards** — Helps meet technology governance expectations for large institutions
- **NYDFS Cybersecurity Regulation** — Supports access control and technology governance requirements

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for administrative automation
- See [Verification & Testing](verification-testing.md) to validate configuration
