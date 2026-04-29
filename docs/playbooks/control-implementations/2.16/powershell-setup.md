# Control 2.16: Federated Copilot Connector and MCP Governance - PowerShell Setup

Automation workflow for inventorying federated connectors, capturing per-connector enablement state, and pulling invocation and authentication audit evidence.

## Prerequisites

- PowerShell 7+
- `Microsoft.Graph` (Application.Read.All, Directory.Read.All, AuditLog.Read.All)
- `ExchangeOnlineManagement` for unified-audit-log queries
- M365 Global Reader or equivalent least-privilege role
- Approved evidence-retention path

> **Important:** Federated connector and MCP surface APIs continue to evolve. Validate endpoint and operation names against the current Microsoft Learn references before automating.

## Script Flow

### Script 1: Inventory tenant connector posture

```powershell
Connect-MgGraph -Scopes "Application.Read.All","Directory.Read.All","AuditLog.Read.All" -NoWelcome

$connectors = Invoke-MgGraphRequest -Method GET `
  -Uri "https://graph.microsoft.com/beta/copilot/admin/connectors"

$connectors.value |
  Select-Object id, displayName, type, authenticationMode, defaultEnabled, scopedGroupIds |
  Export-Csv .\artifacts\2.16\connector-posture.csv -NoTypeInformation
```

### Script 2: Capture user-credential authentications to federated services

```powershell
$start = (Get-Date).AddDays(-30).ToString('o')

$signins = Invoke-MgGraphRequest -Method GET `
  -Uri "https://graph.microsoft.com/v1.0/auditLogs/signIns?`$filter=createdDateTime ge $start and clientAppUsed eq 'Other clients'"

$signins.value |
  Where-Object { $_.appDisplayName -match 'Notion|Canva|HubSpot|Linear|Google' } |
  Select-Object createdDateTime, userPrincipalName, appDisplayName, ipAddress |
  Export-Csv .\artifacts\2.16\federated-signins.csv -NoTypeInformation
```

### Script 3: Pull federated connector invocation audit events

```powershell
Connect-ExchangeOnline -ShowBanner:$false

$start = (Get-Date).AddDays(-30)
$end   = Get-Date

Search-UnifiedAuditLog -StartDate $start -EndDate $end `
  -RecordType CopilotInteraction `
  -Operations 'CopilotConnectorInvoked','CopilotConnectorAuthenticated','CopilotConnectorAuthorizationFailed' `
  -ResultSize 5000 |
  Export-Csv .\artifacts\2.16\connector-invocations.csv -NoTypeInformation
```

### Script 4: Snapshot scoped Entra groups per connector

```powershell
Import-Csv .\artifacts\2.16\connector-posture.csv |
  Where-Object { $_.scopedGroupIds } |
  ForEach-Object {
    $connector = $_.displayName
    foreach ($groupId in ($_.scopedGroupIds -split ';')) {
      Get-MgGroupMember -GroupId $groupId -All |
        Select-Object @{n='Connector';e={$connector}},
                      @{n='UPN';e={$_.AdditionalProperties.userPrincipalName}}
    }
  } | Export-Csv .\artifacts\2.16\connector-scope-membership.csv -NoTypeInformation
```

### Script 5: Package evidence

```powershell
$stamp = Get-Date -Format 'yyyyMMdd-HHmm'
Compress-Archive -Path .\artifacts\2.16\* `
  -DestinationPath ".\artifacts\2.16\federated-connector-evidence-$stamp.zip"
```

## Operational Guidance

| Task | Cadence | Notes |
|------|---------|-------|
| Connector posture snapshot | Monthly | Captures default-enabled changes Microsoft introduces |
| Sign-in and invocation audit pull | Weekly | Detects authentication patterns to unsanctioned services |
| Scoped-group membership reconciliation | Quarterly | Aligns scope to vendor-risk decisions |
| Vendor reassessment | Annually or per third-party policy | Per OCC Bulletin 2023-17 lifecycle expectations |

## Next Steps

- Continue to [Verification & Testing](verification-testing.md) for scope and DLP validation.
- Reference [Troubleshooting](troubleshooting.md) for inventory and audit issues.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 2.16](../../../controls/pillar-2-security/2.16-federated-connector-mcp-governance.md)
