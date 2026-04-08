# Control 4.4: Copilot in Viva Suite Governance — Portal Walkthrough

Step-by-step portal configuration for governing Copilot capabilities within the Microsoft Viva suite, including Viva Insights (with Copilot Chat analytics), Viva Engage (with Teams integration), Viva Learning, Viva Goals, and Viva Connections.

## Prerequisites

- **Role:** Entra Global Admin or Viva Administrator
- **License:** Microsoft 365 E5 with Copilot add-on, Microsoft Viva suite license (Viva Insights P2 or Viva Suite for Copilot Chat analytics)
- **Access:** Microsoft 365 Admin Center, Viva Admin Center, Microsoft Purview

## Steps

### Step 1: Configure Viva Insights Copilot Chat Analytics

**Portal:** Viva Insights Admin Center (Advanced)
**Path:** Advanced Insights > Analyst Settings > Copilot analytics

1. Navigate to the Viva Insights Advanced portal at `insights.viva.office.com`.
2. Select **Analyst Settings** in the left navigation.
3. Under **Copilot analytics**, enable Copilot Chat usage reporting:
   - Toggle **Copilot Chat insights** to **On**
   - Confirm that the minimum group size configured in privacy settings (Step 1 of the control setup) applies to Copilot Chat data
4. Configure department-level analytics dashboards:
   - Navigate to **Analyst Workbench > Copilot Dashboard**
   - Under **View by**, select the organizational attributes to display (department, role level)
   - Assign analyst access to business unit leaders who need visibility into their department's Copilot Chat adoption
5. Review available Copilot Chat metrics:
   - **Adoption rate:** Percentage of licensed users actively using Copilot Chat within the reporting period
   - **Interaction frequency:** Average Copilot Chat interactions per active user per week
   - **Feature engagement:** Breakdown of Copilot Chat usage patterns by function (file summarization, drafting assistance, search)
6. Verify privacy protections are active:
   - Confirm that no individual-level Copilot Chat query data is accessible via the analyst interface
   - Confirm that departments below the minimum group size threshold show suppressed (not visible) data

### Step 2: Configure Copilot in Viva Engage and Teams Integration

**Portal:** Viva Engage Admin Center
**Path:** Governance and compliance > Copilot settings

1. Navigate to the Viva Engage admin settings.
2. Configure Copilot features for Engage:
   - Enable or disable Copilot-assisted post drafting
   - Control AI-powered conversation summaries
   - Set content moderation for AI-generated posts
3. For FSI environments, enable compliance monitoring on AI-assisted Engage posts.
4. Apply communication compliance policies to Viva Engage content.
5. Configure the Engage-to-Teams integration compliance perimeter:
   - Navigate to **Microsoft Purview > Communication Compliance**
   - Open the relevant supervision policy covering Viva Engage communities
   - Verify the policy scope includes both "Yammer messages" and "Teams messages" locations — this ensures Engage content that surfaces in Teams is captured regardless of where it appears
   - Navigate to **Microsoft Purview > Data Lifecycle Management**
   - Open the Teams retention policy and confirm its scope includes Teams channels that receive surfaced Engage content
6. For communities covering regulated business topics (market commentary, investment strategy, client matters):
   - Connect those Engage communities to Teams channels using the Viva Engage community-to-Teams channel integration
   - Confirm that surfacing in Teams channels automatically applies Teams retention and supervision policies to the Engage content

### Step 3: Configure Copilot in Viva Learning

**Portal:** Viva Learning Admin Center
**Path:** Settings > Copilot

1. Review Copilot features in Viva Learning:
   - AI-recommended learning paths
   - Copilot-generated learning summaries
   - Skills assessment suggestions
2. Configure which learning content sources Copilot can reference.
3. Ensure Copilot learning recommendations align with firm compliance training requirements.
4. Verify mandatory compliance training is not bypassed by AI recommendations.

### Step 4: Configure Copilot in Viva Goals

!!! warning "Viva Goals Retired"
    Microsoft Viva Goals was retired on December 31, 2025. Organizations that used Viva Goals should verify data has been exported. No further configuration is needed.

### Step 5: Configure Viva Connections Copilot Integration

**Portal:** SharePoint admin center / Viva Connections
**Path:** Viva Connections settings

1. Review how Copilot interacts with Viva Connections dashboard content.
2. Ensure Copilot does not surface restricted content on the employee dashboard.
3. Configure news and announcements handling by Copilot.
4. Verify sensitivity labels are respected when Copilot surfaces content in Viva Connections.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Copilot Chat usage reporting | Enable org-level reporting | Enable department-level dashboards | Enable with anomaly detection alerts |
| Engage-to-Teams compliance coverage | Verify Teams retention applies | Confirm CC policies cover both locations | Quarterly review of Engage-to-Teams scope |
| Engage AI moderation | Disabled | Enabled | Required |
| Learning AI recommendations | Enabled | Controlled | Controlled with compliance alignment |
| Goals AI features | Enabled | Enabled | Enabled with access controls |
| Connections content controls | Default | Sensitivity-aware | Sensitivity label enforced |

## Regulatory Alignment

- **FINRA Rule 3110** — Supports compliance with supervision of internal communications via Viva Engage, including content surfacing through the Engage-to-Teams integration
- **FFIEC Management Booklet, Section II.C** — Copilot Chat analytics in Viva Insights directly support IT risk monitoring expectations for AI technology usage patterns
- **EEOC/Employment law** — Supports governance of AI-generated goal and performance content; Copilot Chat analytics must not be used for individual performance evaluation

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for Viva governance automation
- See [Verification & Testing](verification-testing.md) to validate Viva Copilot controls
