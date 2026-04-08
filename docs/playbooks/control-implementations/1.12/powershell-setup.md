# Control 1.12: Training and Awareness Program — PowerShell Setup

Automation scripts for tracking training completion and managing awareness program distribution.

## Prerequisites

- Microsoft Graph PowerShell SDK
- Global Reader or User Administrator role
- Training completion data from LMS (CSV export)

## Scripts

### Script 1: Training Completion Compliance Report

```powershell
# Cross-reference Copilot-licensed users with training completion records
# Requires: Microsoft Graph SDK + LMS export

Import-Module Microsoft.Graph.Users
Import-Module Microsoft.Graph.Identity.DirectoryManagement
Connect-MgGraph -Scopes "User.Read.All","Organization.Read.All"

# Import training completion data from LMS
$trainingCompleted = Import-Csv "TrainingCompletions.csv"  # Expected columns: UPN, CompletionDate, Module
$completedUPNs = $trainingCompleted | Select-Object -ExpandProperty UPN -Unique

# Get Copilot licensed users
$copilotSku = Get-MgSubscribedSku | Where-Object { $_.SkuPartNumber -match "Microsoft_365_Copilot" }
$allUsers = Get-MgUser -All -Property "displayName,userPrincipalName,department,assignedLicenses"

$licensedUsers = $allUsers | Where-Object {
    $_.AssignedLicenses.SkuId -contains $copilotSku.SkuId
}

$complianceReport = @()
foreach ($user in $licensedUsers) {
    $hasTraining = $completedUPNs -contains $user.UserPrincipalName
    $complianceReport += [PSCustomObject]@{
        DisplayName       = $user.DisplayName
        UPN               = $user.UserPrincipalName
        Department        = $user.Department
        TrainingCompleted = $hasTraining
        CompletionDate    = if ($hasTraining) {
            ($trainingCompleted | Where-Object UPN -eq $user.UserPrincipalName | Select-Object -First 1).CompletionDate
        } else { "Not completed" }
    }
}

$compliant = ($complianceReport | Where-Object TrainingCompleted).Count
$total = $complianceReport.Count
if ($total -eq 0) { Write-Warning "No Copilot-licensed users found."; return }
$rate = [math]::Round(($compliant / $total) * 100, 1)

Write-Host "=== Training Compliance Report ==="
Write-Host "Copilot users: $total"
Write-Host "Training completed: $compliant ($rate%)"
Write-Host "Training not completed: $($total - $compliant)"

$complianceReport | Export-Csv "TrainingCompliance_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Send Training Reminder Notifications

```powershell
# Generate list of users needing training reminders
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Users
Connect-MgGraph -Scopes "User.Read.All","Mail.Send"

$nonCompliant = Import-Csv "TrainingCompliance_$(Get-Date -Format 'yyyyMMdd').csv" |
    Where-Object { $_.TrainingCompleted -eq "False" }

Write-Host "Users requiring training reminders: $($nonCompliant.Count)"

# Export reminder list for email distribution
$reminderList = $nonCompliant | Select-Object DisplayName, UPN, Department
$reminderList | Export-Csv "TrainingReminders_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation

# Generate department-level summary for managers
$deptReminders = $nonCompliant | Group-Object Department | ForEach-Object {
    [PSCustomObject]@{
        Department   = $_.Name
        PendingCount = $_.Count
    }
} | Sort-Object PendingCount -Descending

Write-Host "`n=== Departments with Pending Training ==="
$deptReminders | Format-Table Department, PendingCount -AutoSize
```

### Script 3: Training Program Metrics Dashboard Data

```powershell
# Generate metrics for training program dashboard
# Requires: LMS export data

$completions = Import-Csv "TrainingCompletions.csv"

# Module completion analysis
$moduleStats = $completions | Group-Object Module | ForEach-Object {
    [PSCustomObject]@{
        Module          = $_.Name
        Completions     = $_.Count
        AvgDaysToComplete = [math]::Round(($_.Group | ForEach-Object {
            ((Get-Date $_.CompletionDate) - (Get-Date $_.AssignedDate)).Days
        } | Measure-Object -Average).Average, 1)
    }
}

Write-Host "=== Training Module Metrics ==="
$moduleStats | Format-Table Module, Completions, AvgDaysToComplete -AutoSize
$moduleStats | Export-Csv "TrainingMetrics_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Training Compliance Report | Weekly | Track completion rates |
| Training Reminders | Weekly | Notify non-compliant users |
| Metrics Dashboard Update | Monthly | Report training program health |

## Next Steps

- See [Verification & Testing](verification-testing.md) for program validation
- See [Troubleshooting](troubleshooting.md) for training delivery issues
