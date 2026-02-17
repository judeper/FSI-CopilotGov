# Control 4.4: Copilot in Viva Suite Governance — Portal Walkthrough

Step-by-step portal configuration for governing Copilot capabilities within the Microsoft Viva suite, including Viva Engage, Viva Learning, Viva Goals, and Viva Connections.

## Prerequisites

- **Role:** Global Administrator or Viva Administrator
- **License:** Microsoft 365 E5 with Copilot add-on, Microsoft Viva suite license
- **Access:** Microsoft 365 Admin Center, Viva Admin Center

## Steps

### Step 1: Configure Copilot in Viva Engage

**Portal:** Viva Engage Admin Center
**Path:** Governance and compliance > Copilot settings

1. Navigate to the Viva Engage admin settings.
2. Configure Copilot features for Engage:
   - Enable or disable Copilot-assisted post drafting
   - Control AI-powered conversation summaries
   - Set content moderation for AI-generated posts
3. For FSI environments, enable compliance monitoring on AI-assisted Engage posts.
4. Apply communication compliance policies to Viva Engage content.

### Step 2: Configure Copilot in Viva Learning

**Portal:** Viva Learning Admin Center
**Path:** Settings > Copilot

1. Review Copilot features in Viva Learning:
   - AI-recommended learning paths
   - Copilot-generated learning summaries
   - Skills assessment suggestions
2. Configure which learning content sources Copilot can reference.
3. Ensure Copilot learning recommendations align with firm compliance training requirements.
4. Verify mandatory compliance training is not bypassed by AI recommendations.

### Step 3: Configure Copilot in Viva Goals

**Portal:** Viva Goals Admin Center
**Path:** Settings > AI features

1. Review Copilot features in Viva Goals:
   - AI-assisted OKR drafting
   - Progress analysis and suggestions
   - Goal alignment recommendations
2. Configure data access controls to prevent Copilot from surfacing confidential performance data.
3. Set appropriate access boundaries so Copilot goal suggestions respect organizational hierarchies.

### Step 4: Configure Viva Connections Copilot Integration

**Portal:** SharePoint Admin Center / Viva Connections
**Path:** Viva Connections settings

1. Review how Copilot interacts with Viva Connections dashboard content.
2. Ensure Copilot does not surface restricted content on the employee dashboard.
3. Configure news and announcements handling by Copilot.
4. Verify sensitivity labels are respected when Copilot surfaces content in Viva Connections.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Engage AI moderation | Disabled | Enabled | Required |
| Learning AI recommendations | Enabled | Controlled | Controlled with compliance alignment |
| Goals AI features | Enabled | Enabled | Enabled with access controls |
| Connections content controls | Default | Sensitivity-aware | Sensitivity label enforced |

## Regulatory Alignment

- **FINRA Rule 3110** — Supports compliance with supervision of internal communications via Viva Engage
- **FFIEC Management Booklet** — Helps meet IT governance for enterprise collaboration platforms
- **EEOC/Employment law** — Supports governance of AI-generated goal and performance content

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for Viva governance automation
- See [Verification & Testing](verification-testing.md) to validate Viva Copilot controls
