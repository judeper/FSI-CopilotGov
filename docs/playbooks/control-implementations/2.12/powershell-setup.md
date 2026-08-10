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

### Script 2: SharePoint and OneDrive Guest-Access Expiration Audit

```powershell
# Review the tenant-level resource-access expiration setting
$tenant = Get-SPOTenant
$tenant | Select-Object ExternalUserExpirationRequired, ExternalUserExpireInDays

# Example: configure 90-day expiration for eligible direct and sharing-link access
Set-SPOTenant -ExternalUserExpirationRequired $true -ExternalUserExpireInDays 90
```

Microsoft's [guest-expiration guidance](https://support.microsoft.com/en-us/office/manage-guest-expiration-for-a-site-25bee24f-42ad-4ee8-8402-4186eed74dea) limits this policy to sharing-link access and direct site permissions granted after enablement. It does not alter or delete the Microsoft Entra B2B guest account. Pre-existing access and access through Microsoft 365 groups, security groups, or Teams can remain and must be separately reconciled.

### Script 3: Guest User Inventory and Activity Report

```powershell
# Inventory guest users and their last activity
Import-Module Microsoft.Graph.Users
Connect-MgGraph -Scopes "User.Read.All","AuditLog.Read.All"

$guests = Get-MgUser -Filter "userType eq 'Guest'" -All -Property "id,displayName,userPrincipalName,createdDateTime,signInActivity"

$guestReport = @()
foreach ($guest in $guests) {
    $lastSignIn = $guest.SignInActivity.LastSignInDateTime
    $guestReport += [PSCustomObject]@{
        Id           = $guest.Id
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

This inventory reports identities, not every access path. For each expiration or stale-access candidate, use [`Get-MgUserTransitiveMemberOf -UserId <guest-object-id> -All`](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users/get-mgusertransitivememberof) and the Teams inventory to identify Microsoft 365 group, security group, and Teams membership, then reconcile each membership against the approved engagement.

### Script 4: Export Stale Guest Candidates for Access Review

```powershell
# Prepare candidates for a governed access review; this script does not delete accounts
$staleGuests = Import-Csv "GuestUsers_reviewed.csv" | Where-Object { $_.IsStale -eq "True" }
Write-Host "Stale guest candidates for review: $($staleGuests.Count)"
$staleGuests | Export-Csv "GuestAccessReviewCandidates_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

The candidate report is not an account-deletion or complete-access-removal mechanism. Reconcile direct permissions, sharing links, Microsoft 365 groups, security groups, Teams, and application assignments separately. Automatic tenant-account deletion requires a specifically configured Entra access review for **Select Teams + groups** with auto-apply enabled, nonresponse set to remove access, and the denied-guest action set to **Block user from signing-in for 30 days, then remove user from the tenant**. That deletion option is unavailable for **All Microsoft 365 groups with guest users** reviews.

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| External Sharing Audit | Monthly | Verify sharing settings remain restrictive |
| Guest-Access Expiration Audit | Monthly | Verify eligible direct/link expiration and reconcile surviving group, security-group, and Teams access |
| Guest User Inventory | Monthly | Track and review guest accounts |
| Stale Guest Access Review | Quarterly | Reconcile candidates through the approved access-review process |

## Next Steps

- See [Verification & Testing](verification-testing.md) for sharing control validation
- See [Troubleshooting](troubleshooting.md) for sharing issues
- Back to [Control 2.12](../../../controls/pillar-2-security/2.12-external-sharing-governance.md)
