# Control 4.5: Copilot Usage Analytics and Adoption Reporting — Portal Walkthrough

Step-by-step portal configuration for establishing usage analytics and adoption reporting capabilities for Microsoft 365 Copilot across the organization.

## Prerequisites

- **Role:** Entra Global Admin, Reports Reader, or Usage Summary Reports Reader
- **License:** Microsoft 365 E5 with Copilot add-on
- **Access:** Microsoft 365 Admin Center

## Steps

### Step 1: Access Copilot Usage Dashboard

**Portal:** Microsoft 365 Admin Center
**Path:** Reports > Usage > Microsoft 365 Copilot

1. Navigate to Reports > Usage in the Admin Center.
2. Select the **Microsoft 365 Copilot** report.
3. Review the dashboard metrics:
   - Enabled users vs. active users
   - Usage by application (Word, Excel, PowerPoint, Outlook, Teams)
   - Feature adoption trends over 7, 30, and 180 days
   - Active user percentage by department

### Step 2: Configure Report Privacy Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Org settings > Reports

1. Navigate to Settings > Org settings > Reports.
2. Configure privacy settings for usage data:
   - **Show identifiable user information** — Disable for general reports, enable only for compliance-authorized viewers
   - **Make report data available to the Microsoft Graph** — Enable for programmatic access
3. For FSI compliance, maintain the ability to identify individual users for supervisory purposes while restricting general access.

### Step 3: Set Up Custom Adoption Reports

**Portal:** Microsoft 365 Admin Center
**Path:** Reports > Usage > Copilot > Download report

1. Download the detailed Copilot usage report for custom analysis.
2. Create custom views filtered by:
   - Business unit / department
   - User role (front office, back office, compliance)
   - Feature type (drafting, summarizing, analyzing)
   - Geographic location
3. Establish baseline adoption metrics for each deployment wave.

### Step 4: Configure Adoption Tracking Metrics

**Portal:** Microsoft 365 Admin Center / Power BI
**Path:** Reports > Adoption Score

1. Review the Microsoft Adoption Score for Copilot-related categories.
2. Define target adoption KPIs:
   - Active Copilot users as a percentage of licensed users (target: 80%+)
   - Average interactions per user per week
   - Feature breadth (number of apps with active Copilot usage per user)
3. Set up a recurring adoption review cadence (monthly for leadership, weekly for deployment team).
4. Create Power BI dashboards for detailed adoption analytics if needed.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Usage report access | Admin only | Admin + compliance team | Restricted role-based access |
| User identification | Anonymized | Identifiable for compliance | Identifiable with audit trail |
| Reporting frequency | Monthly | Weekly | Weekly with daily alerts |
| Adoption target (active/licensed) | 50% | 70% | 80% |

## Regulatory Alignment

- **FFIEC Management Booklet** — Supports compliance with IT investment governance and monitoring
- **OCC Heightened Standards** — Helps meet technology utilization and governance expectations
- **SOX Section 404** — Supports internal controls over IT asset management

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for usage reporting automation
- See [Verification & Testing](verification-testing.md) to validate analytics accuracy
