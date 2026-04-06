# Control 4.6: Viva Insights — Copilot Impact Measurement — Portal Walkthrough

Step-by-step portal configuration for using Microsoft Viva Insights to measure the business impact of Copilot adoption and productivity outcomes.

## Prerequisites

- **Role:** Viva Insights Administrator, Entra Global Admin
- **License:** Microsoft Viva Insights, Microsoft 365 E5 with Copilot add-on
- **Access:** Viva Insights Advanced portal, Microsoft 365 Admin Center

## Steps

### Step 1: Enable Copilot Impact Dashboard in Viva Insights

**Portal:** Viva Insights Advanced
**Path:** Analyst experience > Copilot dashboard

1. Navigate to the Viva Insights advanced analyst experience.
2. Locate the Copilot impact dashboard (pre-built template).
3. Verify data sources are connected and populating:
   - Copilot interaction data
   - Collaboration patterns (meetings, email, chat)
   - Focus time metrics
4. Configure the dashboard date range and user scope.

### Step 2: Configure Privacy and Data Access Controls

**Portal:** Viva Insights Admin Center
**Path:** Settings > Privacy

1. Configure minimum group size for aggregated reports (minimum 10 users recommended for FSI).
2. Set data access controls:
   - Define who can view Copilot impact metrics (HR, management, compliance)
   - Restrict individual-level data to authorized roles only
   - Enable or disable manager-level insights
3. Configure data retention for Viva Insights analytics data.
4. Ensure employee privacy requirements are met per organizational policy.

### Step 3: Create Custom Copilot Impact Queries

**Portal:** Viva Insights Advanced
**Path:** Analyst experience > Custom queries

1. Create custom queries to measure Copilot-specific impact:
   - **Time savings:** Compare meeting duration and frequency pre/post Copilot adoption
   - **Email efficiency:** Measure email composition time and response rates
   - **Collaboration quality:** Analyze meeting attendance and engagement patterns
2. Set up comparison groups (Copilot users vs. non-Copilot users) for controlled analysis.
3. Schedule recurring queries for trend analysis.

### Step 4: Configure Executive Reporting Dashboard

**Portal:** Viva Insights / Power BI
**Path:** Analyst experience > Reports > Export to Power BI

1. Create an executive-level Copilot ROI dashboard with key metrics:
   - Estimated time saved per user per week
   - Meeting efficiency improvements
   - Email productivity gains
   - Document creation acceleration
2. Include cost-benefit analysis comparing Copilot license cost to productivity gains.
3. Set up automated report distribution to leadership.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Minimum aggregation group | 5 users | 10 users | 25 users |
| Individual-level data access | Open | Restricted | HR/Compliance only |
| Manager insights | Enabled | Selective | Disabled by default |
| Reporting frequency | Quarterly | Monthly | Monthly |

## Regulatory Alignment

- **FFIEC Management Booklet** — Supports compliance with IT investment governance and effectiveness monitoring
- **EEOC guidance** — Helps meet requirements for fair and non-discriminatory use of workplace analytics
- **GDPR/CCPA** — Supports privacy requirements for employee data analytics (where applicable)

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for insights automation
- See [Verification & Testing](verification-testing.md) to validate impact measurement
