# Control 4.11: Microsoft Sentinel Integration for Copilot Events — Portal Walkthrough

Step-by-step portal configuration for integrating Microsoft 365 Copilot events into Microsoft Sentinel for advanced security monitoring, threat detection, and compliance analytics.

## Prerequisites

- **Role:** Security Administrator, Sentinel Contributor
- **License:** Microsoft 365 E5, Microsoft Sentinel
- **Access:** Microsoft Defender portal (primary Sentinel workspace experience), Azure portal (legacy transition), Microsoft Purview

!!! note "Microsoft Defender portal transition"
    Microsoft Learn states Microsoft Sentinel is generally available in the Microsoft Defender portal and that Azure portal support for Sentinel ends after March 31, 2027. Use the Defender portal (`https://security.microsoft.com`) as the recommended FSI operating path for unified incident management; retain Azure portal paths only for legacy workspaces during transition.

## Steps

### Step 1: Connect Microsoft 365 Data Connector in Sentinel

**Portal:** Microsoft Defender portal (recommended primary path)
**Path:** Microsoft Sentinel > Configuration > Data connectors > Microsoft 365
**Legacy Azure path:** Azure portal > Microsoft Sentinel > Data connectors > Microsoft 365

1. In the Microsoft Defender portal (`https://security.microsoft.com`), open **Microsoft Sentinel** and select the target workspace.
2. Go to **Configuration > Data connectors** and locate the **Microsoft 365** connector.
3. Click **Open connector page** and enable the following data types:
   - Exchange Online audit logs
   - SharePoint Online audit logs
   - Teams audit logs
4. Verify the connector status shows "Connected" and data is flowing.
5. For workspaces not yet transitioned, use the legacy Azure portal path until migration is complete.

### Step 2: Enable Microsoft Copilot Connector (Preview)

**Portal:** Microsoft Defender portal (recommended primary path)
**Path:** Microsoft Sentinel > Configuration > Data connectors > Microsoft Copilot (Preview)
**Legacy Azure path:** Azure portal > Microsoft Sentinel > Data connectors > Microsoft Copilot (Preview)

1. In **Microsoft Sentinel > Configuration > Data connectors**, locate **Microsoft Copilot (Preview)**.
2. Enable the connector for the target workspace.
3. Validate the table schema in Logs:
   - `CopilotActivity | getschema`
4. Validate ingestion with the documented filter:
   - `CopilotActivity | where RecordType == "CopilotInteraction" | take 10`
5. If zero rows are returned, treat that as a gap indicator and verify connector state, RBAC permissions, and ingestion delay.

### Step 3: Create Copilot-Specific Analytics Rules

**Portal:** Microsoft Defender portal (recommended primary path)
**Path:** Microsoft Sentinel > Configuration > Analytics
**Related paths:** Microsoft Sentinel > Configuration > Automation; Microsoft Sentinel > Configuration > Watchlists
**Legacy Azure path:** Azure portal > Microsoft Sentinel > Analytics

1. Create analytics rules for Copilot security monitoring:
   - **Unusual Copilot access pattern** — Detect Copilot usage from unusual locations or devices
   - **High-volume data extraction via Copilot** — Detect potential data exfiltration through excessive Copilot queries
   - **Copilot access to sensitive content** — Alert when Copilot interactions involve highly classified content
   - **After-hours Copilot usage** — Detect Copilot usage outside normal business hours
2. Set severity levels and configure automated response actions with **Microsoft Sentinel > Configuration > Automation** where appropriate.
3. Use **Microsoft Sentinel > Configuration > Watchlists** to reference high-value assets, service accounts, or restricted data sets in rules where applicable.
4. Map each rule to MITRE ATT&CK techniques where applicable.

### Step 4: Create Copilot Monitoring Workbook

**Portal:** Microsoft Defender portal (recommended primary path)
**Path:** Microsoft Sentinel > Threat management > Workbooks
**Related hunting paths:** Microsoft Sentinel > Threat management > Hunting; Investigation & response > Hunting > Advanced hunting
**Legacy Azure path:** Azure portal > Microsoft Sentinel > Workbooks

1. Create a workbook titled "Copilot Security and Governance Dashboard".
2. Add the following visualizations:
   - Copilot event volume over time
   - Top Copilot users by interaction count
   - DLP incidents related to Copilot
   - Geographic distribution of Copilot usage
   - Anomaly detection alerts
3. Use **Threat management > Hunting** or **Advanced hunting** to validate KQL queries that support the workbook and related investigations.
4. Share the workbook with the security operations and compliance teams.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Sentinel data connectors | M365 + Copilot (Preview) | M365 + Copilot (Preview) + Purview | M365 + Copilot (Preview) + Purview + custom sources |
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
