# Control 2.2: Sensitivity Labels and Copilot Content Classification — PowerShell Setup

Automation scripts for managing sensitivity label enforcement on Copilot content.

## Prerequisites

- Security & Compliance PowerShell (`ExchangeOnlineManagement`)
- Information Protection Administrator role
- Microsoft 365 E5 or E5 Compliance license

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
# Requires: PnP PowerShell

Import-Module PnP.PowerShell

$siteUrl = "https://<tenant>.sharepoint.com/sites/<sitename>"
Connect-PnPOnline -Url $siteUrl -Interactive

$items = Get-PnPListItem -List "Documents" -PageSize 500

$unlabeled = @()
foreach ($item in $items) {
    $label = $item.FieldValues["_ComplianceTag"]
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

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Label Policy Audit | Monthly | Verify policy settings remain correct |
| Label Usage Report | Weekly | Monitor label application patterns |
| Unlabeled Content Scan | Weekly | Identify gaps in label coverage |

## Next Steps

- See [Verification & Testing](verification-testing.md) for label enforcement validation
- See [Troubleshooting](troubleshooting.md) for label issues
