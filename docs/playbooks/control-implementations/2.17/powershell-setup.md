# Control 2.17: Cross-Tenant Agent Federation - PowerShell Setup

Automation workflow for inventorying cross-tenant Agent ID trust, MCP federated server registrations, Copilot Studio multi-tenant publishing, and the corresponding audit evidence.

## Prerequisites

- PowerShell 7+
- `Microsoft.Graph` (Policy.Read.All, Application.Read.All, Directory.Read.All, AuditLog.Read.All)
- `ExchangeOnlineManagement` for unified-audit-log queries
- M365 Global Reader and Identity Reader (or equivalent)
- Approved evidence-retention path

> **Important:** Cross-tenant agent federation surfaces are evolving. Validate endpoints and operation names against the current Microsoft Learn references before automating.

## Script Flow

### Script 1: Snapshot cross-tenant access settings

```powershell
Connect-MgGraph -Scopes "Policy.Read.All","Directory.Read.All","Application.Read.All","AuditLog.Read.All" -NoWelcome

$default = Invoke-MgGraphRequest -Method GET `
  -Uri "https://graph.microsoft.com/v1.0/policies/crossTenantAccessPolicy/default"

$partners = Invoke-MgGraphRequest -Method GET `
  -Uri "https://graph.microsoft.com/v1.0/policies/crossTenantAccessPolicy/partners"

$default  | ConvertTo-Json -Depth 8 | Out-File .\artifacts\2.17\ctap-default.json
$partners | ConvertTo-Json -Depth 8 | Out-File .\artifacts\2.17\ctap-partners.json
```

### Script 2: Inventory workload identities used as agent identities

```powershell
$apps = Invoke-MgGraphRequest -Method GET `
  -Uri "https://graph.microsoft.com/v1.0/applications?`$select=id,appId,displayName,signInAudience,tags"

$apps.value |
  Where-Object { $_.tags -contains 'AgentId' -or $_.signInAudience -ne 'AzureADMyOrg' } |
  Select-Object id, appId, displayName, signInAudience, @{n='Tags';e={$_.tags -join ';'}} |
  Export-Csv .\artifacts\2.17\agent-identities.csv -NoTypeInformation
```

### Script 3: Inventory MCP federated server registrations

```powershell
$mcp = Invoke-MgGraphRequest -Method GET `
  -Uri "https://graph.microsoft.com/beta/copilot/admin/connectors?`$filter=type eq 'mcpFederatedServer'"

$mcp.value |
  Select-Object id, displayName, operatingTenant, attestationStatus, dataResidency, registeredBy |
  Export-Csv .\artifacts\2.17\mcp-federated-servers.csv -NoTypeInformation
```

### Script 4: Pull cross-tenant invocation and trust-grant audit events

```powershell
Connect-ExchangeOnline -ShowBanner:$false

$start = (Get-Date).AddDays(-30)
$end   = Get-Date

Search-UnifiedAuditLog -StartDate $start -EndDate $end `
  -Operations 'CrossTenantAgentInvoked','CrossTenantTrustGranted','CrossTenantTrustRevoked','MCPFederatedServerRegistered','MCPFederatedServerRevoked','CopilotStudioAgentInstalled','CopilotStudioAgentUninstalled' `
  -ResultSize 5000 |
  Export-Csv .\artifacts\2.17\cross-tenant-audit.csv -NoTypeInformation
```

### Script 5: Package evidence

```powershell
$stamp = Get-Date -Format 'yyyyMMdd-HHmm'
Compress-Archive -Path .\artifacts\2.17\* `
  -DestinationPath ".\artifacts\2.17\cross-tenant-evidence-$stamp.zip"
```

## Operational Guidance

| Task | Cadence | Notes |
|------|---------|-------|
| CTAP and partner snapshot | Monthly | Detects drift in cross-tenant trust scope |
| Agent identity and MCP inventory | Monthly | Aligns with the third-party register |
| Audit pull | Weekly | Supports supervisory observability |
| Termination playbook drill | Annually | Validates clean-up procedures |

## Next Steps

- Continue to [Verification & Testing](verification-testing.md) for trust scope and termination validation.
- Reference [Troubleshooting](troubleshooting.md) for attestation or publishing issues.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 2.17](../../../controls/pillar-2-security/2.17-cross-tenant-agent-federation.md)
