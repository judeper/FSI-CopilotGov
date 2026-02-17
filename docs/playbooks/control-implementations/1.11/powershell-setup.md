# Control 1.11: Change Management and Adoption Planning — PowerShell Setup

Automation scripts for tracking Copilot adoption metrics and deployment progress.

## Prerequisites

- Microsoft Graph PowerShell SDK
- Global Reader or Reports Reader role
- Microsoft 365 Copilot licenses deployed

## Scripts

### Script 1: Copilot Adoption Metrics Report

```powershell
# Generate Copilot adoption metrics across the organization
# Requires: Microsoft Graph SDK with Reports.Read.All

Import-Module Microsoft.Graph.Reports
Import-Module Microsoft.Graph.Users

Connect-MgGraph -Scopes "Reports.Read.All","User.Read.All"

# Get Copilot usage data
$copilotUsage = Get-MgReportM365AppUserDetail -Period "D30" -OutFile "CopilotRawUsage.csv"

# Generate adoption summary from licensed users
$copilotSku = Get-MgSubscribedSku | Where-Object { $_.SkuPartNumber -match "Microsoft_365_Copilot" }
$allUsers = Get-MgUser -All -Property "displayName,userPrincipalName,department,assignedLicenses,signInActivity"

$licensedUsers = $allUsers | Where-Object {
    $_.AssignedLicenses.SkuId -contains $copilotSku.SkuId
}

$adoptionReport = @()
foreach ($user in $licensedUsers) {
    $lastSignIn = $user.SignInActivity.LastSignInDateTime
    $adoptionReport += [PSCustomObject]@{
        DisplayName  = $user.DisplayName
        Department   = $user.Department
        LastSignIn   = $lastSignIn
        IsActive     = ($lastSignIn -gt (Get-Date).AddDays(-7))
    }
}

$totalLicensed = $adoptionReport.Count
$activeUsers = ($adoptionReport | Where-Object IsActive).Count
$adoptionRate = if ($totalLicensed -gt 0) { [math]::Round(($activeUsers / $totalLicensed) * 100, 1) } else { 0 }

Write-Host "=== Copilot Adoption Summary ==="
Write-Host "Licensed users: $totalLicensed"
Write-Host "Active users (7-day): $activeUsers"
Write-Host "Adoption rate: $adoptionRate%"

$adoptionReport | Export-Csv "CopilotAdoption_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Department-Level Adoption Breakdown

```powershell
# Break down Copilot adoption by department
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Users
Connect-MgGraph -Scopes "User.Read.All"

$adoptionData = Import-Csv "CopilotAdoption_$(Get-Date -Format 'yyyyMMdd').csv"

$deptSummary = $adoptionData | Group-Object Department | ForEach-Object {
    $active = ($_.Group | Where-Object { $_.IsActive -eq "True" }).Count
    [PSCustomObject]@{
        Department    = $_.Name
        TotalLicensed = $_.Count
        ActiveUsers   = $active
        AdoptionRate  = [math]::Round(($active / $_.Count) * 100, 1)
    }
} | Sort-Object AdoptionRate -Descending

Write-Host "=== Department Adoption Rates ==="
$deptSummary | Format-Table Department, TotalLicensed, ActiveUsers, AdoptionRate -AutoSize
$deptSummary | Export-Csv "DeptAdoption_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Deployment Wave Progress Tracker

```powershell
# Track deployment progress by wave group
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Groups
Import-Module Microsoft.Graph.Users
Connect-MgGraph -Scopes "Group.Read.All","User.Read.All","Reports.Read.All"

$waveGroups = @("Copilot-Pilot-Users", "Copilot-Wave1-Users", "Copilot-Wave2-Users")
$waveReport = @()

foreach ($groupName in $waveGroups) {
    $group = Get-MgGroup -Filter "displayName eq '$groupName'" -ErrorAction SilentlyContinue
    if ($group) {
        $members = Get-MgGroupMember -GroupId $group.Id -All
        $waveReport += [PSCustomObject]@{
            Wave        = $groupName
            MemberCount = $members.Count
            Status      = if ($members.Count -gt 0) { "Active" } else { "Not Started" }
        }
    }
}

Write-Host "=== Deployment Wave Progress ==="
$waveReport | Format-Table Wave, MemberCount, Status -AutoSize
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Adoption Metrics Report | Weekly | Track adoption progress |
| Department Breakdown | Monthly | Identify departments needing adoption support |
| Wave Progress Tracker | After each wave deployment | Monitor wave completion |

## Next Steps

- See [Verification & Testing](verification-testing.md) for adoption validation
- See [Troubleshooting](troubleshooting.md) for adoption issues
