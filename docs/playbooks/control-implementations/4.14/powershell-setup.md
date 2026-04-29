# Control 4.14: Copilot Studio Agent Lifecycle Governance - PowerShell Setup

Automation workflow for inventorying Copilot Studio agents across environments, capturing publishing and version events, and packaging lifecycle evidence.

## Prerequisites

- PowerShell 7+
- `Microsoft.Graph` (AuditLog.Read.All)
- `Microsoft.PowerApps.Administration.PowerShell` for Copilot Studio environment / agent inventory
- `ExchangeOnlineManagement` for unified-audit-log queries
- Power Platform Administrator (read-only) and M365 Global Reader (or equivalent)
- Approved evidence-retention path

> **Important:** Copilot Studio agent operations exposed through Power Platform admin cmdlets continue to evolve. Validate cmdlet availability before automating.

## Script Flow

### Script 1: Inventory Copilot Studio environments and agents

```powershell
Add-PowerAppsAccount

$environments = Get-AdminPowerAppEnvironment

$agents = foreach ($env in $environments) {
  Get-AdminPowerAppCopilot -EnvironmentName $env.EnvironmentName -ErrorAction SilentlyContinue |
    Select-Object @{n='EnvironmentName';e={$env.DisplayName}},
                  @{n='EnvironmentType';e={$env.EnvironmentType}},
                  Name, DisplayName, Owner, CreatedTime, LastModifiedTime, LifecycleStage
}

$agents | Export-Csv .\artifacts\4.14\copilot-studio-agents.csv -NoTypeInformation
```

### Script 2: Pull publishing, version, and lifecycle audit events

```powershell
Connect-ExchangeOnline -ShowBanner:$false

$start = (Get-Date).AddDays(-30)
$end   = Get-Date

Search-UnifiedAuditLog -StartDate $start -EndDate $end `
  -Operations 'CopilotStudioAgentCreated','CopilotStudioAgentPublished','CopilotStudioAgentVersionPublished','CopilotStudioAgentDeprecated','CopilotStudioAgentDeleted','CopilotStudioApprovalRecorded' `
  -ResultSize 5000 |
  Export-Csv .\artifacts\4.14\agent-lifecycle-audit.csv -NoTypeInformation
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

### Script 4: Build a per-agent version history

```powershell
$audit = Import-Csv .\artifacts\4.14\agent-lifecycle-audit.csv

$audit |
  Where-Object { $_.Operations -in @('CopilotStudioAgentPublished','CopilotStudioAgentVersionPublished') } |
  Select-Object CreationDate, UserIds,
                @{n='AgentName';e={ ($_.AuditData | ConvertFrom-Json).AgentName }},
                @{n='Version';e={   ($_.AuditData | ConvertFrom-Json).Version   }},
                @{n='Approver';e={  ($_.AuditData | ConvertFrom-Json).Approver  }} |
  Export-Csv .\artifacts\4.14\agent-version-history.csv -NoTypeInformation
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
| Version-history report | Quarterly | Feeds the lifecycle attestation |
| Deprecation drill | Annually | Validates the end-of-life playbook |

## Next Steps

- Continue to [Verification & Testing](verification-testing.md) for stage transition and deprecation validation.
- Reference [Troubleshooting](troubleshooting.md) for register, approval, and deprecation issues.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 4.14](../../../controls/pillar-4-operations/4.14-copilot-studio-agent-lifecycle.md)
