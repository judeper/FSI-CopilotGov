# Control 4.11: Microsoft Sentinel Integration for Copilot Events — Portal Walkthrough

Step-by-step portal configuration for integrating Microsoft 365 Copilot events into Microsoft Sentinel for advanced security monitoring, threat detection, and compliance analytics.

## Prerequisites

- **Role:** Security Administrator, Sentinel Contributor
- **License:** Microsoft 365 E5, Microsoft Sentinel
- **Access:** Azure Portal (Sentinel workspace), Microsoft Purview

## Steps

### Step 1: Connect Microsoft 365 Data Connector in Sentinel

**Portal:** Azure Portal
**Path:** Microsoft Sentinel > Data connectors > Microsoft 365

1. Navigate to the Sentinel workspace in the Azure Portal.
2. Go to **Data connectors** and locate the **Microsoft 365** connector.
3. Click **Open connector page** and enable the following data types:
   - Exchange Online audit logs
   - SharePoint Online audit logs
   - Teams audit logs
4. Verify the connector status shows "Connected" and data is flowing.

### Step 2: Enable Microsoft Purview Connector for Copilot Events

**Portal:** Azure Portal
**Path:** Microsoft Sentinel > Data connectors > Microsoft Purview (Preview)

1. Locate the **Microsoft Purview** data connector.
2. Enable the connector to ingest Copilot-specific audit events.
3. Configure the data types to include:
   - CopilotInteraction events
   - DLP events related to Copilot
   - Communication compliance events
4. Verify Copilot events are appearing in the Sentinel logs.

### Step 3: Create Copilot-Specific Analytics Rules

**Portal:** Azure Portal
**Path:** Microsoft Sentinel > Analytics > Create rule

1. Create analytics rules for Copilot security monitoring:
   - **Unusual Copilot access pattern** — Detect Copilot usage from unusual locations or devices
   - **High-volume data extraction via Copilot** — Detect potential data exfiltration through excessive Copilot queries
   - **Copilot access to sensitive content** — Alert when Copilot interactions involve highly classified content
   - **After-hours Copilot usage** — Detect Copilot usage outside normal business hours
2. Set severity levels and configure automated response actions.
3. Map each rule to MITRE ATT&CK techniques where applicable.

### Step 4: Create Copilot Monitoring Workbook

**Portal:** Azure Portal
**Path:** Microsoft Sentinel > Workbooks > Add workbook

1. Create a workbook titled "Copilot Security and Governance Dashboard".
2. Add the following visualizations:
   - Copilot event volume over time
   - Top Copilot users by interaction count
   - DLP incidents related to Copilot
   - Geographic distribution of Copilot usage
   - Anomaly detection alerts
3. Share the workbook with the security operations and compliance teams.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Sentinel data connectors | M365 only | M365 + Purview | M365 + Purview + Custom |
| Analytics rules | Default | Copilot-specific rules | Custom rules + ML detection |
| Workbook dashboards | None | Copilot dashboard | Real-time SOC dashboard |
| Incident auto-response | Manual | Semi-automated | Automated for high-severity |

## Regulatory Alignment

- **FFIEC IT Handbook** — Supports compliance with continuous monitoring and threat detection requirements
- **NYDFS 23 NYCRR 500** — Helps meet continuous monitoring and event logging requirements
- **PCI DSS** — Supports security monitoring requirements (if applicable to card data environments)

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for Sentinel configuration automation
- See [Verification & Testing](verification-testing.md) to validate Sentinel integration
- Back to [Control 4.11](../../../controls/pillar-4-operations/4.11-sentinel-integration.md)
