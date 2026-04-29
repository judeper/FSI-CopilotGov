# Control 1.16: Copilot Tuning Governance - PowerShell Setup

Automation workflow for capturing Copilot Tuning configuration, request-and-approval activity, and tuned-agent inventory evidence.

## Prerequisites

- PowerShell 7+
- `Microsoft.Graph` (Reports.Read.All, AuditLog.Read.All)
- `ExchangeOnlineManagement` for unified-audit-log queries
- M365 Global Reader or equivalent least-privilege role for evidence collection
- Approved evidence-retention path

> **Important:** Tuning configuration and approval-flow surfaces evolve as Copilot Tuning rolls out. Validate cmdlet availability against the M365 Admin Center current state before automating.

## Script Flow

### Script 1: Capture tenant tuning configuration

```powershell
Connect-MgGraph -Scopes "Reports.Read.All","AuditLog.Read.All" -NoWelcome

$config = Invoke-MgGraphRequest -Method GET `
  -Uri "https://graph.microsoft.com/beta/copilot/admin/settings"

$config | ConvertTo-Json -Depth 8 |
  Out-File .\artifacts\1.16\tuning-config.json
```

### Script 2: List tuned agents

```powershell
$agents = Invoke-MgGraphRequest -Method GET `
  -Uri "https://graph.microsoft.com/beta/copilot/agents?`$filter=type eq 'tuned'"

$agents.value |
  Select-Object id, displayName, owner, createdDateTime, dataSources |
  Export-Csv .\artifacts\1.16\tuned-agents.csv -NoTypeInformation
```

### Script 3: Pull tuning approval and snapshot audit events

```powershell
Connect-ExchangeOnline -ShowBanner:$false

$start = (Get-Date).AddDays(-30)
$end   = Get-Date

Search-UnifiedAuditLog -StartDate $start -EndDate $end `
  -RecordType CopilotInteraction `
  -Operations 'CopilotTuningRequest','CopilotTuningApproval','CopilotTuningJobStarted','CopilotTuningSnapshotCreated','CopilotTuningAgentDeleted' `
  -ResultSize 5000 |
  Export-Csv .\artifacts\1.16\tuning-audit.csv -NoTypeInformation
```

### Script 4: Snapshot the authorized requesters group

```powershell
$groupId = '<entra-group-object-id-for-tuning-requesters>'

Get-MgGroupMember -GroupId $groupId -All |
  Select-Object Id, @{n='UPN';e={$_.AdditionalProperties.userPrincipalName}} |
  Export-Csv .\artifacts\1.16\tuning-requesters.csv -NoTypeInformation
```

### Script 5: Package evidence

```powershell
$stamp = Get-Date -Format 'yyyyMMdd-HHmm'
Compress-Archive -Path .\artifacts\1.16\* `
  -DestinationPath ".\artifacts\1.16\tuning-evidence-$stamp.zip"
```

## Operational Guidance

| Task | Cadence | Notes |
|------|---------|-------|
| Re-snapshot tuning configuration | Monthly | Captures changes to enablement scope or open-source model policy |
| Audit pull | Weekly | Aligns with the standing tuning approval review cadence |
| Tuned-agent inventory reconciliation | Quarterly | Reconciles live agents to the model risk register |
| Evidence archive | After every approval cycle | Supports examination response |

## Next Steps

- Continue to [Verification & Testing](verification-testing.md) to validate evidence captures.
- Reference [Troubleshooting](troubleshooting.md) for cmdlet errors or empty audit results.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 1.16](../../../controls/pillar-1-readiness/1.16-copilot-tuning-governance.md)
