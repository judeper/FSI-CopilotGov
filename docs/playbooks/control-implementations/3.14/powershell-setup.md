# Control 3.14: Copilot Pages and Notebooks Retention and Provenance - PowerShell Setup

Automation workflow for inventorying Loop workspaces, Notebook locations, and Loop component hosts; pulling lifecycle audit events; and packaging lineage evidence.

## Prerequisites

- PowerShell 7+
- `Microsoft.Graph` (Sites.Read.All, Files.Read.All, AuditLog.Read.All)
- `ExchangeOnlineManagement` for unified-audit-log queries
- M365 Global Reader and Purview Compliance Reader (or equivalent)
- Approved evidence-retention path

> **Important:** Microsoft documents Copilot Pages and Copilot Notebooks audit data under the Loop application identity and file-extension evidence, not under a separate Copilot Pages/Notebooks application filter. Do not assume fixed operation names such as `CopilotPageBranched` or `LoopComponentEmbedded` unless the names are visible in the tenant or current Microsoft documentation.

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

### Script 2: Pull Pages, Notebook, and Loop container/file audit evidence

```powershell
Connect-ExchangeOnline -ShowBanner:$false

$start = (Get-Date).AddDays(-30)
$end   = Get-Date
$loopApplicationIds = @(
  'a187e399-0c36-4b98-8f04-1edc167a0996',
  '0922ef46-e1b9-4f7e-9134-9ad00547eb41'
)

$rawAudit = foreach ($keyword in @('page','loop','loot','fluid') + $loopApplicationIds) {
  Search-UnifiedAuditLog -StartDate $start -EndDate $end `
    -FreeText $keyword `
    -ResultSize 5000
}

$rawAudit |
  Select-Object CreationDate, UserIds, Operations, AuditData |
  Export-Csv .\artifacts\3.14\artifact-lifecycle-audit-raw.csv -NoTypeInformation
```

### Script 3: Build a Page/Notebook lineage reconciliation report

```powershell
$audit = Import-Csv .\artifacts\3.14\artifact-lifecycle-audit-raw.csv

$audit | ForEach-Object {
  $data = $_.AuditData | ConvertFrom-Json
  if ($data.SourceFileExtension -in @('page','loop','pod','fluid')) {
    [PSCustomObject]@{
      CreationDate        = $_.CreationDate
      UserIds             = $_.UserIds
      Operation           = $_.Operations
      SourceFileExtension = $data.SourceFileExtension
      SourceFileName      = $data.SourceFileName
      SiteUrl             = $data.SiteUrl
      ObjectId            = $data.ObjectId
      ListItemUniqueId    = $data.ListItemUniqueId
    }
  }
} | Export-Csv .\artifacts\3.14\lineage-reconciliation-input.csv -NoTypeInformation
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

*FSI Copilot Governance Framework v1.8.0 - July 2026*
- Back to [Control 3.14](../../../controls/pillar-3-compliance/3.14-copilot-pages-notebooks-retention.md)
