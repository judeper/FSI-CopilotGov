# Control 2.12: External Sharing and Guest Access Governance — PowerShell Setup

Automation scripts for managing external sharing and guest access controls.

## Prerequisites

- SharePoint Online Management Shell
- Microsoft Graph PowerShell SDK
- SharePoint Admin and Global Reader roles

## Scripts

### Script 1: External Sharing Configuration Audit

```powershell
# Audit external sharing settings across all SharePoint sites
Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$sites = Get-SPOSite -Limit All -IncludePersonalSite $false
$sharingReport = @()

foreach ($site in $sites) {
    $detail = Get-SPOSite -Identity $site.Url -Detailed
    $sharingReport += [PSCustomObject]@{
        Url               = $site.Url
        Title             = $site.Title
        SharingCapability = $detail.SharingCapability
        SensitivityLabel  = $detail.SensitivityLabel
        ExternalSharingEnabled = ($detail.SharingCapability -ne "Disabled")
    }
}

$externalEnabled = ($sharingReport | Where-Object ExternalSharingEnabled).Count
Write-Host "Sites with external sharing enabled: $externalEnabled of $($sharingReport.Count)"
$sharingReport | Export-Csv "ExternalSharing_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Guest User Inventory and Activity Report

```powershell
# Inventory guest users and their last activity
Import-Module Microsoft.Graph.Users
Connect-MgGraph -Scopes "User.Read.All","AuditLog.Read.All"

$guests = Get-MgUser -Filter "userType eq 'Guest'" -All -Property "displayName,userPrincipalName,createdDateTime,signInActivity"

$guestReport = @()
foreach ($guest in $guests) {
    $lastSignIn = $guest.SignInActivity.LastSignInDateTime
    $guestReport += [PSCustomObject]@{
        DisplayName  = $guest.DisplayName
        UPN          = $guest.UserPrincipalName
        Created      = $guest.CreatedDateTime
        LastSignIn   = $lastSignIn
        DaysSinceSignIn = if ($lastSignIn) { ((Get-Date) - $lastSignIn).Days } else { 999 }
        IsStale      = ((-not $lastSignIn) -or ((Get-Date) - $lastSignIn).Days -gt 90)
    }
}

$stale = ($guestReport | Where-Object IsStale).Count
Write-Host "Guest users: $($guestReport.Count) | Stale (>90 days): $stale"
$guestReport | Export-Csv "GuestUsers_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Bulk Remove Stale Guest Accounts

```powershell
# Remove stale guest accounts (requires review before execution)
Import-Module Microsoft.Graph.Users
Connect-MgGraph -Scopes "User.ReadWrite.All"

$staleGuests = Import-Csv "GuestUsers_reviewed.csv" | Where-Object { $_.IsStale -eq "True" }
Write-Host "Stale guests to remove: $($staleGuests.Count)"
Write-Host "WARNING: Review the list before proceeding."

foreach ($guest in $staleGuests) {
    try {
        # Block sign-in first, then remove after grace period
        Update-MgUser -UserId $guest.UPN -AccountEnabled:$false
        Write-Host "Disabled: $($guest.UPN)"
    } catch {
        Write-Host "Failed: $($guest.UPN) - $($_.Exception.Message)" -ForegroundColor Red
    }
}
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| External Sharing Audit | Monthly | Verify sharing settings remain restrictive |
| Guest User Inventory | Monthly | Track and review guest accounts |
| Stale Guest Cleanup | Quarterly | Remove inactive guest accounts |

## Next Steps

- See [Verification & Testing](verification-testing.md) for sharing control validation
- See [Troubleshooting](troubleshooting.md) for sharing issues
- Back to [Control 2.12](../../../controls/pillar-2-security/2.12-external-sharing-governance.md)
