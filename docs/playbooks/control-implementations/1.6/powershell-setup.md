# Control 1.6: Permission Model Audit — PowerShell Setup

Automation scripts for comprehensive permission model auditing across Microsoft 365.

## Prerequisites

### Required Modules

- SharePoint Online Management Shell
- PnP PowerShell (see custom app registration below)
- Microsoft Graph PowerShell SDK
- Exchange Online Management module for mailbox permissions

### PnP PowerShell: Custom App Registration Required

The shared multi-tenant PnP Management Shell Entra ID app was retired on September 9, 2024. All PnP PowerShell scripts now require a tenant-specific Entra ID app registration. Complete this one-time setup before running any PnP scripts in this playbook.

```powershell
# One-time setup: Register a tenant-specific app for PnP PowerShell
Register-PnPEntraIDAppForInteractiveLogin `
    -ApplicationName "PnP Governance Shell - [YourOrg]" `
    -Tenant "yourorg.onmicrosoft.com" `
    -SharePointApplicationPermissions "Sites.FullControl.All" `
    -GraphApplicationPermissions "Sites.Read.All" `
    -Interactive
```

Save the returned Client ID — you will need it for all `Connect-PnPOnline` calls in this playbook. Store the Client ID in your organization's secrets management system (e.g., Azure Key Vault) for team use.

### Required Roles

- SharePoint Admin and Global Reader roles (for SPO and Graph scripts)
- Exchange Administrator role (for Exchange scripts)

## Scripts

### Script 1: Tenant-Wide Site Permission Audit

```powershell
# Audit permissions across all SharePoint sites
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$sites = Get-SPOSite -Limit All -IncludePersonalSite $false
$permReport = @()

foreach ($site in $sites) {
    $detail = Get-SPOSite -Identity $site.Url -Detailed
    $siteGroups = Get-SPOSiteGroup -Site $site.Url -ErrorAction SilentlyContinue

    $everyoneAccess = $siteGroups | Where-Object {
        # NOTE: Replace $detail.HubSiteId with your tenant GUID. Get via: (Get-MgOrganization).Id
        $_.Users -contains "c:0-.f|rolemanager|spo-grid-all-users/$($detail.HubSiteId)" -or
        $_.LoginName -match "Everyone"
    }

    $permReport += [PSCustomObject]@{
        Url               = $site.Url
        Title             = $site.Title
        SharingCapability = $detail.SharingCapability
        SensitivityLabel  = $detail.SensitivityLabel
        GroupCount        = $siteGroups.Count
        HasEveryoneAccess = ($null -ne $everyoneAccess)
        Owner             = $detail.Owner
    }
}

$riskyCount = ($permReport | Where-Object { $_.HasEveryoneAccess -or $_.SharingCapability -eq "ExternalUserAndGuestSharing" }).Count
Write-Host "Permission audit complete. $riskyCount sites with elevated risk out of $($permReport.Count) total."
$permReport | Export-Csv "PermissionAudit_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Large Group Membership Audit

```powershell
# Identify large security groups that may grant excessive access
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Groups
Connect-MgGraph -Scopes "Group.Read.All","GroupMember.Read.All"

$groups = Get-MgGroup -All -Property "DisplayName,Id,MembershipRule,GroupTypes,SecurityEnabled"
$largeGroups = @()

foreach ($group in $groups) {
    $memberCount = (Get-MgGroupMember -GroupId $group.Id -All).Count
    if ($memberCount -gt 50) {
        $largeGroups += [PSCustomObject]@{
            GroupName    = $group.DisplayName
            GroupId      = $group.Id
            MemberCount  = $memberCount
            IsDynamic    = ($group.GroupTypes -contains "DynamicMembership")
            IsSecurityGroup = $group.SecurityEnabled
        }
    }
}

$largeGroups | Sort-Object MemberCount -Descending | Format-Table GroupName, MemberCount, IsDynamic -AutoSize
$largeGroups | Export-Csv "LargeGroups_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Found $($largeGroups.Count) groups with more than 50 members."
```

### Script 3: Sharing Links Inventory

```powershell
# Enumerate active sharing links across high-priority sites
# Requires: PnP PowerShell with custom app registration (see Prerequisites)

Import-Module PnP.PowerShell

$targetSites = Import-Csv "HighPrioritySites.csv"
$sharingReport = @()
$clientId = "<your-app-id>"  # Client ID from Register-PnPEntraIDAppForInteractiveLogin

foreach ($site in $targetSites) {
    Connect-PnPOnline -Url $site.Url -ClientId $clientId -Interactive
    $items = Get-PnPListItem -List "Documents" -PageSize 500

    foreach ($item in $items) {
        $sharingInfo = Get-PnPFileSharingLink -FileUrl $item.FieldValues["FileRef"] -ErrorAction SilentlyContinue
        if ($sharingInfo) {
            foreach ($link in $sharingInfo) {
                $sharingReport += [PSCustomObject]@{
                    Site     = $site.Url
                    FilePath = $item.FieldValues["FileRef"]
                    LinkType = $link.LinkKind
                    Scope    = $link.Scope
                    Created  = $link.CreatedDateTime
                    Expiration = $link.ExpirationDateTime
                }
            }
        }
    }
    Disconnect-PnPOnline
}

$sharingReport | Export-Csv "SharingLinks_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Found $($sharingReport.Count) active sharing links across $($targetSites.Count) sites."
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Site Permission Audit | Monthly | Detect permission drift and new risk areas |
| Large Group Review | Quarterly | Identify groups that need access review |
| Sharing Link Inventory | Monthly | Track and manage active sharing links |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate audit findings
- See [Troubleshooting](troubleshooting.md) for script execution issues
- Back to [Control 1.6: Permission Model Audit](../../../controls/pillar-1-readiness/1.6-permission-model-audit.md)
