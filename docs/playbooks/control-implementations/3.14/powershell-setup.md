# Control 3.14: Copilot Pages and Notebooks Retention and Provenance - PowerShell Setup

Automation workflow for inventorying Loop workspaces, Notebook locations, and Loop component hosts; pulling lifecycle audit events; and packaging lineage evidence.

## Prerequisites

- PowerShell 7+
- `Microsoft.Graph` (Sites.Read.All, Files.Read.All, AuditLog.Read.All)
- `ExchangeOnlineManagement` for unified-audit-log queries
- M365 Global Reader and Purview Compliance Reader (or equivalent)
- Approved evidence-retention path

> **Important:** Pages branch and Loop component embed events depend on operations that Microsoft continues to publish. Validate operation names against the current Microsoft Learn references before automating.

## Script Flow

### Script 1: Inventory Loop workspaces and Notebook locations

```powershell
Connect-MgGraph -Scopes "Sites.Read.All","Files.Read.All","AuditLog.Read.All" -NoWelcome

$workspaces = Invoke-MgGraphRequest -Method GET `
  -Uri "https://graph.microsoft.com/beta/loop/workspaces"

$workspaces.value |
  Select-Object id, displayName, webUrl, ownerUpn, createdDateTime |
  Export-Csv .\artifacts\3.14\loop-workspaces.csv -NoTypeInformation

$notebooks = Invoke-MgGraphRequest -Method GET `
  -Uri "https://graph.microsoft.com/v1.0/sites?`$search=`"OneNote`""

$notebooks.value |
  Select-Object id, displayName, webUrl |
  Export-Csv .\artifacts\3.14\notebook-sites.csv -NoTypeInformation
```

### Script 2: Pull Pages, Notebook, and Loop lifecycle audit events

```powershell
Connect-ExchangeOnline -ShowBanner:$false

$start = (Get-Date).AddDays(-30)
$end   = Get-Date

Search-UnifiedAuditLog -StartDate $start -EndDate $end `
  -Operations 'CopilotPageCreated','CopilotPageBranched','CopilotPageEdited','CopilotPageDeleted','OneNotePageEdited','LoopComponentCreated','LoopComponentEmbedded','LoopComponentEdited','LoopComponentRemoved' `
  -ResultSize 5000 |
  Export-Csv .\artifacts\3.14\artifact-lifecycle-audit.csv -NoTypeInformation
```

### Script 3: Build a Pages branch lineage report

```powershell
$audit = Import-Csv .\artifacts\3.14\artifact-lifecycle-audit.csv

$audit |
  Where-Object { $_.Operations -eq 'CopilotPageBranched' } |
  Select-Object CreationDate, UserIds,
                @{n='ParentPageId';e={ ($_.AuditData | ConvertFrom-Json).ParentPageId }},
                @{n='ChildPageId';e={  ($_.AuditData | ConvertFrom-Json).ChildPageId  }} |
  Export-Csv .\artifacts\3.14\pages-branch-lineage.csv -NoTypeInformation
```

### Script 4: Build a Loop component embed map

```powershell
$audit |
  Where-Object { $_.Operations -in @('LoopComponentEmbedded','LoopComponentRemoved') } |
  Select-Object CreationDate, Operations, UserIds,
                @{n='ComponentId';e={ ($_.AuditData | ConvertFrom-Json).ComponentId }},
                @{n='HostType';e={    ($_.AuditData | ConvertFrom-Json).HostType    }},
                @{n='HostUri';e={     ($_.AuditData | ConvertFrom-Json).HostUri     }} |
  Export-Csv .\artifacts\3.14\loop-embed-map.csv -NoTypeInformation
```

### Script 5: Package evidence

```powershell
$stamp = Get-Date -Format 'yyyyMMdd-HHmm'
Compress-Archive -Path .\artifacts\3.14\* `
  -DestinationPath ".\artifacts\3.14\artifact-lineage-evidence-$stamp.zip"
```

## Operational Guidance

| Task | Cadence | Notes |
|------|---------|-------|
| Storage inventory snapshot | Monthly | Detects new workspaces or Notebook sites that should be in retention scope |
| Lifecycle audit pull | Weekly | Aligns with the supervisory review cadence |
| Pages branch lineage report | Quarterly | Feeds the Regulated-tier attestation |
| Loop embed map | Quarterly | Detects host references that may surface live content |
| Evidence archive | Monthly | Supports examination response |

## Next Steps

- Continue to [Verification & Testing](verification-testing.md) for retention and lineage validation.
- Reference [Troubleshooting](troubleshooting.md) for branch, embed, or hold issues.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 3.14](../../../controls/pillar-3-compliance/3.14-copilot-pages-notebooks-retention.md)
