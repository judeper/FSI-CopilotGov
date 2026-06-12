# Control 4.15: Copilot Cowork Governance - PowerShell Setup

Automation workflow for capturing Cowork-related agent events, reconciling availability scope against the approved pilot group, and packaging preview-governance evidence. Cowork availability is managed in the admin center UI; this playbook focuses on evidence collection rather than configuration.

## Prerequisites

- PowerShell 7+
- `ExchangeOnlineManagement` for unified-audit-log queries
- `Microsoft.Graph` (AuditLog.Read.All, Group.Read.All) for group membership reconciliation
- M365 Global Reader (or equivalent least-privilege read role)
- Approved evidence-retention path
- An exported or documented record of the Cowork availability decision and approved pilot group

> **Important:** Cowork is a Frontier preview feature with no dedicated configuration cmdlets. Do not rely on undocumented Cowork-specific cmdlets. Validate the availability scope in the admin center UI and reconcile it with Purview Audit results before treating automated output as evidence.

## Script Flow

### Script 1: Capture Cowork-related agent audit events

```powershell
Connect-ExchangeOnline -ShowBanner:$false

$start = (Get-Date).AddDays(-30)
$end   = Get-Date

$agentOperations = @(
  'DeployedAgent',
  'RemovedAgent',
  'UpdatedAgent'
)

# Agent 365 management operations per https://learn.microsoft.com/purview/audit-log-activities#microsoft-365-admin-center-agent-management-activities
Search-UnifiedAuditLog -StartDate $start -EndDate $end `
  -Operations $agentOperations `
  -ResultSize 5000 |
  Where-Object { $_.AuditData -match 'Cowork' } |
  Export-Csv .\artifacts\4.15\cowork-agent-audit.csv -NoTypeInformation
```

### Script 2: Reconcile availability scope against the approved pilot group

```powershell
Connect-MgGraph -Scopes 'Group.Read.All'

# Source group from the documented availability decision.
$approvedGroupId = (Import-Csv .\config\cowork-availability-decision.csv).ApprovedGroupId | Select-Object -First 1

$members = Get-MgGroupMember -GroupId $approvedGroupId -All |
  Select-Object Id,
    @{n='Display';e={ $_.AdditionalProperties.displayName }},
    @{n='UserPrincipalName';e={ $_.AdditionalProperties.userPrincipalName }}

$members | Export-Csv .\artifacts\4.15\cowork-approved-members.csv -NoTypeInformation
```

### Script 3: Build a Cowork install activity report

```powershell
$audit = Import-Csv .\artifacts\4.15\cowork-agent-audit.csv

$audit |
  ForEach-Object {
    $data = $_.AuditData | ConvertFrom-Json
    [pscustomobject]@{
      CreationDate = $_.CreationDate
      UserIds      = $_.UserIds
      Operation    = $_.Operations
      AgentName    = $data.AgentName ?? $data.AppName
      AgentId      = $data.AgentId ?? $data.AppId
    }
  } |
  Export-Csv .\artifacts\4.15\cowork-install-activity.csv -NoTypeInformation
```

### Script 4: Flag installs outside the approved scope

```powershell
$activity = Import-Csv .\artifacts\4.15\cowork-install-activity.csv
# Reconcile on UPN: Search-UnifiedAuditLog emits UserIds as a UPN/email,
# so compare against the approved members' UserPrincipalName (not the GUID Id).
$approved = (Import-Csv .\artifacts\4.15\cowork-approved-members.csv).UserPrincipalName

$activity |
  Where-Object { $_.Operation -eq 'DeployedAgent' -and $approved -notcontains $_.UserIds } |
  Export-Csv .\artifacts\4.15\cowork-out-of-scope-installs.csv -NoTypeInformation
```

### Script 5: Package evidence

```powershell
$stamp = Get-Date -Format 'yyyyMMdd-HHmm'
Compress-Archive -Path .\artifacts\4.15\* `
  -DestinationPath ".\artifacts\4.15\cowork-governance-evidence-$stamp.zip"
```

## Operational Guidance

| Task | Cadence | Notes |
|------|---------|-------|
| Cowork audit pull | Weekly | Aligns with the supervisory review cadence during preview |
| Scope reconciliation | Monthly | Confirms installs stay within the approved pilot group |
| Out-of-scope install review | Monthly | Investigates installs outside the approved scope |
| Plugin inventory review | Monthly | Confirms available plugins match the approved inventory |
| Preview-change review | As released | Re-assesses availability decisions when Microsoft updates the preview |

## Next Steps

- Continue to [Verification & Testing](verification-testing.md) for availability, plugin, and audit-coverage validation.
- Reference [Troubleshooting](troubleshooting.md) for visibility, availability, and plugin issues.

*FSI Copilot Governance Framework v1.7.1 - April 2026*
- Back to [Control 4.15](../../../controls/pillar-4-operations/4.15-copilot-cowork-governance.md)
