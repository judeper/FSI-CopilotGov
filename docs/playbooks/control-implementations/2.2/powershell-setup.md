# Control 2.2: Sensitivity Labels and Copilot Content Classification — PowerShell Setup

Automation scripts for managing sensitivity label enforcement on Copilot content.

## Prerequisites

Before running any scripts in this playbook, complete a one-time Entra ID app registration for PnP PowerShell. The shared multi-tenant PnP Management Shell Entra ID app was retired September 9, 2024. All PnP PowerShell automation now requires a tenant-specific app registration.

```powershell
# One-time setup: Register a tenant-specific app for PnP PowerShell
# Run this once per tenant before using any PnP PowerShell scripts below
Register-PnPEntraIDAppForInteractiveLogin `
    -ApplicationName "PnP Governance Shell - [YourOrg]" `
    -Tenant "yourorg.onmicrosoft.com" `
    -SharePointDelegated `
    -GraphDelegated `
    -Interactive
```

Save the returned Client ID. All `Connect-PnPOnline` calls must include `-ClientId <your-app-id>`.

**Additional prerequisites:**
- Security & Compliance PowerShell (`ExchangeOnlineManagement`)
- Information Protection Administrator role
- Microsoft 365 E5 or E5 Compliance license
- PnP PowerShell module (`PnP.PowerShell`)

## Scripts

### Script 1: Verify Label Policy Configuration for Copilot

```powershell
# Audit label policies for Copilot-relevant settings
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$policies = Get-LabelPolicy
foreach ($policy in $policies) {
    Write-Host "=== Policy: $($policy.Name) ==="
    Write-Host "  Enabled: $($policy.Enabled)"
    # NOTE: MandatoryLabelingEnabled, DefaultLabelId, and RequireDowngradeJustification
    # must be parsed from the $policy.Settings collection (a string array of key=value pairs),
    # not accessed as direct properties. Use: $policy.Settings | Where-Object { $_ -match 'MandatoryLabelingEnabled' }
    Write-Host "  Mandatory Labeling: $($policy.MandatoryLabelingEnabled)"
    Write-Host "  Default Label: $($policy.DefaultLabelId)"
    Write-Host "  Require Downgrade Justification: $($policy.RequireDowngradeJustification)"
    Write-Host "  Labels: $($policy.Labels -join ', ')"
    Write-Host ""
}
```

### Script 2: Label Usage Report on Recent Documents

```powershell
# Analyze label application on recently created or modified documents
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30).ToString("MM/dd/yyyy")
$endDate = (Get-Date).ToString("MM/dd/yyyy")

$labelEvents = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -RecordType "MipLabel" -ResultSize 5000

$labelReport = @()
foreach ($event in $labelEvents) {
    $data = $event.AuditData | ConvertFrom-Json
    $labelReport += [PSCustomObject]@{
        Date       = $event.CreationDate
        User       = $event.UserIds
        Operation  = $event.Operations
        LabelName  = $data.SensitivityLabelEventData.SensitivityLabelId
        FileName   = $data.ObjectId
        Justification = $data.SensitivityLabelEventData.JustificationText
    }
}

$labelChanges = ($labelReport | Where-Object Operation -match "Downgrade").Count
Write-Host "Label events in last 30 days: $($labelReport.Count)"
Write-Host "Label downgrades (with justification): $labelChanges"

$labelReport | Export-Csv "LabelUsage_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Unlabeled Content Detection

```powershell
# Identify documents without sensitivity labels in Copilot-accessible locations
# Requires: PnP PowerShell with custom app registration (see Prerequisites above)

Import-Module PnP.PowerShell

# Replace with your registered app's Client ID (from Register-PnPEntraIDAppForInteractiveLogin)
$appClientId = "<your-app-id>"
$siteUrl = "https://<tenant>.sharepoint.com/sites/<sitename>"

Connect-PnPOnline -Url $siteUrl -ClientId $appClientId -Interactive

$items = Get-PnPListItem -List "Documents" -PageSize 500

$unlabeled = @()
foreach ($item in $items) {
    $label = $item.FieldValues["_SensitivityLabelId"]
    if (-not $label) {
        $unlabeled += [PSCustomObject]@{
            FileName     = $item.FieldValues["FileLeafRef"]
            FilePath     = $item.FieldValues["FileRef"]
            CreatedBy    = $item.FieldValues["Author"].Email
            Modified     = $item.FieldValues["Modified"]
        }
    }
}

Write-Host "Unlabeled documents in site: $($unlabeled.Count) out of $($items.Count) total"
$unlabeled | Export-Csv "UnlabeledContent_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Scan Multiple Sites for Unlabeled Content

```powershell
# Scan multiple SharePoint sites for unlabeled documents
# Useful for large tenants with many Copilot-accessible sites
# Requires: PnP PowerShell with custom app registration (see Prerequisites above)

Import-Module PnP.PowerShell

# Replace with your registered app's Client ID
$appClientId = "<your-app-id>"

$siteUrls = @(
    "https://<tenant>.sharepoint.com/sites/<site1>",
    "https://<tenant>.sharepoint.com/sites/<site2>",
    "https://<tenant>.sharepoint.com/sites/<site3>"
)

$allUnlabeled = @()

foreach ($siteUrl in $siteUrls) {
    Connect-PnPOnline -Url $siteUrl -ClientId $appClientId -Interactive
    $items = Get-PnPListItem -List "Documents" -PageSize 500

    foreach ($item in $items) {
        $label = $item.FieldValues["_SensitivityLabelId"]
        if (-not $label) {
            $allUnlabeled += [PSCustomObject]@{
                Site         = $siteUrl
                FileName     = $item.FieldValues["FileLeafRef"]
                FilePath     = $item.FieldValues["FileRef"]
                CreatedBy    = $item.FieldValues["Author"].Email
                Modified     = $item.FieldValues["Modified"]
            }
        }
    }
    Write-Host "Processed: $siteUrl"
}

Write-Host "Total unlabeled documents across all sites: $($allUnlabeled.Count)"
$allUnlabeled | Export-Csv "UnlabeledContent_AllSites_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 5: Label Groups Migration Status Check

```powershell
# Check current label taxonomy structure and identify labels still in parent/child hierarchy
# Helps plan the migration to label groups (GA January 2026)
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$allLabels = Get-Label | Select-Object Name, DisplayName, Priority, ContentType, ParentId, IsParent

Write-Host "=== Sensitivity Label Taxonomy ==="
Write-Host "Total labels: $($allLabels.Count)"

$parentLabels = $allLabels | Where-Object { $_.IsParent -eq $true }
$childLabels = $allLabels | Where-Object { $_.ParentId -ne $null -and $_.ParentId -ne "" }
$standaloneLabels = $allLabels | Where-Object { $_.IsParent -ne $true -and ($_.ParentId -eq $null -or $_.ParentId -eq "") }

Write-Host "Parent labels (to be migrated to label groups): $($parentLabels.Count)"
Write-Host "Child/sub-labels: $($childLabels.Count)"
Write-Host "Standalone labels: $($standaloneLabels.Count)"

if ($parentLabels.Count -gt 0) {
    Write-Host ""
    Write-Host "=== Labels requiring label groups migration ==="
    $parentLabels | Format-Table Name, DisplayName, Priority
    Write-Host "Action: Navigate to Purview > Information Protection > Labels > Migrate sensitivity label scheme"
}

$allLabels | Export-Csv "LabelTaxonomy_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Label Policy Audit | Monthly | Verify policy settings remain correct |
| Label Usage Report | Weekly | Monitor label application patterns |
| Unlabeled Content Scan | Weekly | Identify gaps in label coverage |
| Label Groups Migration Check | Once / As needed | Track migration status until complete |

## Next Steps

- See [Verification & Testing](verification-testing.md) for label enforcement validation, including label groups and agent inheritance
- See [Troubleshooting](troubleshooting.md) for label issues including migration problems
- Back to [Control 2.2](../../../controls/pillar-2-security/2.2-sensitivity-labels-classification.md)
