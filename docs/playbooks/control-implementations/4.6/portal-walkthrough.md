# Control 4.6: Viva Insights — Copilot Impact Measurement — Portal Walkthrough

Step-by-step portal configuration for using Microsoft Viva Insights to measure the business impact of Copilot adoption and productivity outcomes.

## Prerequisites

- **Role:** Viva Insights Administrator or authorized dashboard viewer; M365 Global Admin for tenant reporting and access management
- **License:** Microsoft 365 or Office 365 business/enterprise subscription with an active Exchange Online account. A paid Viva Insights license or Microsoft 365 Copilot license is not required to view the dashboard, but analyzed Copilot populations and enhanced features depend on assigned Copilot or Viva Insights license counts.
- **Access:** Viva Insights web app, Microsoft 365 admin center

## Steps

### Step 1: Open the Microsoft Copilot Dashboard in Viva Insights

**Portal:** Viva Insights web app
**Path:** Left navigation > Copilot Dashboard

1. Navigate to the Viva Insights web app and select **Copilot Dashboard** from the left navigation.
2. Validate feature availability against the tenant's assigned license counts:
   - At least one assigned Copilot license starts Copilot Dashboard data processing and includes Microsoft 365 Copilot adoption insights.
   - At least 50 assigned Copilot licenses or 50 assigned Viva Insights licenses unlocks richer team/manager views, agent-related insights, benchmarks, intelligent summaries, delegation support, and survey data where available.
3. Compare dashboard metrics with Microsoft 365 admin center **Reports > Microsoft 365 Copilot Usage** for tenant-level adoption reporting.
4. Verify data sources are connected and populating:
   - Copilot interaction data
   - Collaboration patterns (meetings, email, chat)
   - Focus time metrics
5. Configure the dashboard date range and user scope. Dashboard readiness, adoption, and impact data reflects the previous 28 days and can lag by up to six days.

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

**Portal:** Viva Insights advanced insights (where licensed)
**Path:** Advanced insights > Custom queries

1. Create custom queries to measure Copilot-specific impact:
   - **Time savings:** Compare meeting duration and frequency pre/post Copilot adoption
   - **Email efficiency:** Measure email composition time and response rates
   - **Collaboration quality:** Analyze meeting attendance and engagement patterns
2. Set up comparison groups (Copilot users vs. non-Copilot users) for controlled analysis.
3. Schedule recurring queries for trend analysis.

### Step 4: Configure Executive Reporting Dashboard

**Portal:** Viva Insights advanced insights / Power BI (where licensed)
**Path:** Reports or Power BI export

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
- Back to [Control 4.6](../../../controls/pillar-4-operations/4.6-viva-insights-measurement.md)
