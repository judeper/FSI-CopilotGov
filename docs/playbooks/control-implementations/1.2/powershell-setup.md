# Control 1.2: SharePoint Oversharing Detection (DSPM for AI) — PowerShell Setup

Automation scripts for detecting, reporting, and remediating SharePoint oversharing at scale.

## Prerequisites

- SharePoint Online Management Shell (`Microsoft.Online.SharePoint.PowerShell`)
- Microsoft Graph PowerShell SDK (`Microsoft.Graph`)
- PnP PowerShell module (`PnP.PowerShell`) for detailed site analysis
- SharePoint Administrator or Global Administrator role

## Scripts

### Script 1: Tenant-Wide Oversharing Detection

```powershell
# Detect sites with oversharing risk based on sharing capability and content sensitivity
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell

Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$allSites = Get-SPOSite -Limit All -IncludePersonalSite $false
$oversharedSites = @()

foreach ($site in $allSites) {
    $detail = Get-SPOSite -Identity $site.Url -Detailed
    $riskLevel = "Low"

    if ($detail.SharingCapability -eq "ExternalUserAndGuestSharing") {
        $riskLevel = "Critical"
    } elseif ($detail.SharingCapability -eq "ExternalUserSharingOnly") {
        $riskLevel = "High"
    } elseif ($detail.SharingCapability -eq "ExistingExternalUserSharingOnly") {
        $riskLevel = "Medium"
    }

    if ($riskLevel -ne "Low") {
        $oversharedSites += [PSCustomObject]@{
            Url               = $site.Url
            Title             = $site.Title
            SharingCapability = $detail.SharingCapability
            RiskLevel         = $riskLevel
            Owner             = $detail.Owner
            LastModified      = $detail.LastContentModifiedDate
            StorageMB         = [math]::Round($detail.StorageUsageCurrent, 2)
        }
    }
}

Write-Host "Oversharing scan complete: $($oversharedSites.Count) sites flagged out of $($allSites.Count) total."
$oversharedSites | Export-Csv "OversharedSites_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Site-Level Permission Analysis

```powershell
# Deep permission analysis for a specific SharePoint site
# Requires: PnP PowerShell module

Import-Module PnP.PowerShell

$siteUrl = "https://<tenant>.sharepoint.com/sites/<sitename>"
Connect-PnPOnline -Url $siteUrl -Interactive

$web = Get-PnPWeb -Includes RoleAssignments
$uniquePermItems = Get-PnPListItem -List "Documents" -PageSize 500 |
    Where-Object { $_.HasUniqueRoleAssignments }

Write-Host "Items with unique permissions: $($uniquePermItems.Count)"

$permReport = @()
foreach ($item in $uniquePermItems) {
    $roleAssignments = Get-PnPProperty -ClientObject $item -Property RoleAssignments
    foreach ($ra in $roleAssignments) {
        $member = Get-PnPProperty -ClientObject $ra -Property Member
        $roles = Get-PnPProperty -ClientObject $ra -Property RoleDefinitionBindings
        $permReport += [PSCustomObject]@{
            ItemPath    = $item.FieldValues["FileRef"]
            Principal   = $member.Title
            PrincipalType = $member.PrincipalType
            Permissions = ($roles | Select-Object -ExpandProperty Name) -join "; "
        }
    }
}

$permReport | Export-Csv "SitePermissions_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Bulk Remediation — Restrict Overshared Sites

```powershell
# Bulk restrict sharing on flagged overshared sites
# Requires: SharePoint Online Management Shell
# WARNING: Review the overshared sites CSV before running remediation

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$flaggedSites = Import-Csv "OversharedSites_reviewed.csv"
$remediationLog = @()

foreach ($site in $flaggedSites) {
    try {
        Set-SPOSite -Identity $site.Url -SharingCapability "ExistingExternalUserSharingOnly"
        $remediationLog += [PSCustomObject]@{
            Url       = $site.Url
            Action    = "Restricted sharing"
            Status    = "Success"
            Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        }
    } catch {
        $remediationLog += [PSCustomObject]@{
            Url       = $site.Url
            Action    = "Restrict sharing"
            Status    = "Failed: $($_.Exception.Message)"
            Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        }
    }
}

$remediationLog | Export-Csv "RemediationLog_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Remediation complete. $($remediationLog.Where({$_.Status -eq 'Success'}).Count) sites restricted."
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Oversharing Detection Scan | Weekly | Identify new oversharing instances |
| Site Permission Analysis | Monthly | Deep audit of high-sensitivity sites |
| Remediation Verification | After each remediation cycle | Confirm restrictions applied successfully |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate detection accuracy
- See [Troubleshooting](troubleshooting.md) for script execution issues
