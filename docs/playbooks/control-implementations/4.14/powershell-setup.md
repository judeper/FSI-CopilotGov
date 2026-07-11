# Control 4.14: Copilot Studio Agent Lifecycle Governance - PowerShell Setup

Automation workflow for inventorying Copilot Studio agents across environments, capturing publishing and version events, and packaging lifecycle evidence.

## Prerequisites

- PowerShell 7+
- `Microsoft.Graph` (AuditLog.Read.All)
- `Microsoft.PowerApps.Administration.PowerShell` for Power Platform environment inventory
- `ExchangeOnlineManagement` for unified-audit-log queries
- Power Platform Administrator (read-only) and M365 Global Reader (or equivalent)
- Approved evidence-retention path
- Tenant-approved Copilot Studio agent inventory export or API source

> **Important:** Do not rely on undocumented Copilot-specific Power Platform cmdlets for evidence collection. Validate the inventory source in your tenant and reconcile it with Purview Audit results before automating.

## Script Flow

### Script 1: Inventory Copilot Studio environments and agents

```powershell
Add-PowerAppsAccount

$environments = Get-AdminPowerAppEnvironment |
  Select-Object EnvironmentName, DisplayName, EnvironmentType

$environments | Export-Csv .\artifacts\4.14\power-platform-environments.csv -NoTypeInformation

# Source this file from a tenant-approved Copilot Studio export, CMDB, or validated API.
# Required columns: EnvironmentName, EnvironmentType, Name, DisplayName, Owner,
# CreatedTime, LastModifiedTime, LifecycleStage.
$agents = Import-Csv .\config\copilot-studio-agent-inventory.csv

$agents |
  Select-Object EnvironmentName, EnvironmentType, Name, DisplayName, Owner,
                CreatedTime, LastModifiedTime, LifecycleStage |
  Export-Csv .\artifacts\4.14\copilot-studio-agents.csv -NoTypeInformation
```

### Script 2: Pull publishing, version, and lifecycle audit events

```powershell
Connect-ExchangeOnline -ShowBanner:$false

$start = (Get-Date).AddDays(-30)
$end   = Get-Date

$copilotStudioOperations = @(
  'BotComponentUpdate',
  'BotComponentDelete',
  'BotUpdateOperation-BotPublish',
  'EnvironmentVariableUpdate'
)

# Copilot Studio events do not carry a dedicated MicrosoftCopilotStudio RecordType;
# constrain by -Operations per https://learn.microsoft.com/microsoft-copilot-studio/admin-logging-copilot-studio
Search-UnifiedAuditLog -StartDate $start -EndDate $end `
  -Operations $copilotStudioOperations `
  -ResultSize 5000 |
  Export-Csv .\artifacts\4.14\agent-lifecycle-audit.csv -NoTypeInformation

# Agent 365 management operations per https://learn.microsoft.com/purview/audit-log-activities#microsoft-365-admin-center-agent-management-activities
$agent365Operations = @('DeployedAgent','RemovedAgent','UpdatedAgent')

Search-UnifiedAuditLog -StartDate $start -EndDate $end `
  -Operations $agent365Operations `
  -ResultSize 5000 |
  Export-Csv .\artifacts\4.14\agent-365-admin-audit.csv -NoTypeInformation
```

### Script 3: Reconcile published agents against the register

```powershell
$register = Import-Csv .\config\agent-register.csv
$live     = Import-Csv .\artifacts\4.14\copilot-studio-agents.csv

$live |
  Where-Object { $register.Name -notcontains $_.Name -and $_.LifecycleStage -eq 'Published' } |
  Export-Csv .\artifacts\4.14\unregistered-published-agents.csv -NoTypeInformation

$register |
  Where-Object { $_.LifecycleStage -ne 'Deprecated' -and $live.Name -notcontains $_.Name } |
  Export-Csv .\artifacts\4.14\register-only-agents.csv -NoTypeInformation
```

### Script 4: Build a per-agent change history

```powershell
$audit = Import-Csv .\artifacts\4.14\agent-lifecycle-audit.csv

$audit |
  Where-Object { $_.Operations -in @('BotUpdateOperation-BotPublish','BotComponentUpdate','EnvironmentVariableUpdate') } |
  ForEach-Object {
    $data = $_.AuditData | ConvertFrom-Json
    [pscustomobject]@{
      CreationDate = $_.CreationDate
      UserIds      = $_.UserIds
      Operation    = $_.Operations
      AgentName    = $data.AgentName ?? $data.BotName ?? $data.BotSchemaName
      AgentId      = $data.AgentId ?? $data.BotId
      Component    = $data.BotComponentSchemaName ?? $data.BotComponentType
    }
  } |
  Export-Csv .\artifacts\4.14\agent-change-history.csv -NoTypeInformation
```

### Script 5: Package evidence

```powershell
$stamp = Get-Date -Format 'yyyyMMdd-HHmm'
Compress-Archive -Path .\artifacts\4.14\* `
  -DestinationPath ".\artifacts\4.14\agent-lifecycle-evidence-$stamp.zip"
```

## Operational Guidance

| Task | Cadence | Notes |
|------|---------|-------|
| Agent inventory snapshot | Monthly | Detects new agents and stage transitions |
| Lifecycle audit pull | Weekly | Aligns with the supervisory review cadence |
| Register reconciliation | Monthly | Identifies unregistered published agents and stale register entries |
| Change-history report | Quarterly | Feeds the lifecycle attestation |
| Deprecation drill | Annually | Validates the end-of-life playbook |

## Next Steps

- Continue to [Verification & Testing](verification-testing.md) for stage transition and deprecation validation.
- Reference [Troubleshooting](troubleshooting.md) for register, approval, and deprecation issues.

*FSI Copilot Governance Framework v1.8.0 - July 2026*
- Back to [Control 4.14](../../../controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md)
