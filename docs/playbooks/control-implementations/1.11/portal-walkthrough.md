# Control 1.11: Change Management and Adoption Planning — Portal Walkthrough

Step-by-step portal procedures for establishing change management and adoption plans for Microsoft 365 Copilot deployment.

## Prerequisites

- Microsoft 365 Admin Center access (Entra Global Admin or Service Administrator)
- Microsoft Viva Insights license (optional, for adoption tracking)
- Organizational change management framework or methodology
- Executive sponsor and change management lead identified

## Steps

### Step 1: Configure Copilot Deployment Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Overview / Settings > User access

Review and configure deployment settings that affect the user experience:
- Enable or disable Copilot features by workload (Word, Excel, PowerPoint, Teams, Outlook)
- Configure the Copilot welcome experience for new users
- Set up the Copilot adoption hub for self-service resources

Document which features are enabled for each deployment wave.

### Step 2: Set Up Adoption Tracking in Viva Insights

**Portal:** Microsoft Viva Insights
**Path:** Viva Insights > Organization Insights > Copilot Dashboard

If Viva Insights is available, configure the Copilot adoption dashboard to track:
- Active Copilot users by department and role
- Feature utilization rates across workloads
- Copilot interaction frequency and patterns
- Productivity impact metrics

Set baseline measurements before pilot deployment begins.

### Step 3: Create Communication Plan in Admin Center

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Settings > Org Settings > Communication preferences

Configure organizational communication channels for Copilot deployment announcements:
- Message Center post notifications for IT administrators
- Organizational messages for end users (if enabled)
- Custom notification settings for Copilot-related updates

### Step 4: Configure Feedback Channels

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Settings > Org Settings > User owned apps and services

Enable or configure feedback mechanisms for Copilot users:
- Microsoft feedback integration within Office apps
- Custom feedback forms for governance-specific concerns
- Escalation paths for data security concerns observed in Copilot

### Step 5: Document Change Management Plan

Create the formal change management plan including:
- Stakeholder analysis and communication matrix
- Training schedule aligned with deployment waves
- Resistance management strategies for common FSI concerns
- Success metrics and measurement plan
- Post-deployment support model

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Document change management plan with stakeholder analysis and communication schedule |
| **Recommended** | Implement adoption tracking with Viva Insights; establish feedback loops and support channels |
| **Regulated** | Formal OCM methodology with executive sponsorship; documented resistance management for compliance-sensitive roles; post-deployment effectiveness assessment |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for adoption reporting automation
- See [Verification & Testing](verification-testing.md) to validate change management effectiveness
- Review Control 1.12 for Training and Awareness Program details
- Back to [Control 1.11](../../../controls/pillar-1-readiness/1.11-change-management-adoption.md)
