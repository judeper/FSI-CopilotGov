# Control 1.10: Vendor Risk Management for Microsoft AI Services — PowerShell Setup

Automation scripts for monitoring Microsoft AI service configuration and compliance posture.

## Prerequisites

- Microsoft Graph PowerShell SDK
- Global Reader role (minimum)
- Access to Microsoft 365 Message Center API

## Scripts

### Script 1: Tenant AI Service Configuration Report

```powershell
# Document current Microsoft AI service configuration for vendor risk records
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Beta.Reports
Import-Module Microsoft.Graph.Identity.DirectoryManagement

Connect-MgGraph -Scopes "Organization.Read.All","Policy.Read.All"

$org = Get-MgOrganization
$tenantConfig = @{
    TenantId          = $org.Id
    DisplayName       = $org.DisplayName
    DataLocation      = $org.CountryLetterCode
    AssessmentDate    = Get-Date -Format "yyyy-MM-dd"
    CopilotEnabled    = $true  # Verify via admin center
}

Write-Host "=== Tenant AI Service Configuration ==="
Write-Host "Tenant: $($tenantConfig.DisplayName)"
Write-Host "Data Location: $($tenantConfig.DataLocation)"
Write-Host "Assessment Date: $($tenantConfig.AssessmentDate)"

$tenantConfig | ConvertTo-Json | Out-File "VendorRiskConfig_$(Get-Date -Format 'yyyyMMdd').json"
```

### Script 2: Message Center AI-Related Updates Monitor

```powershell
# Check Microsoft 365 Message Center for AI-related service updates
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Devices.ServiceAnnouncement
Connect-MgGraph -Scopes "ServiceHealth.Read.All"

$messages = Get-MgServiceAnnouncementMessage -Top 100 |
    Where-Object {
        $_.Title -match "Copilot|AI|Machine Learning|Semantic Index" -or
        $_.Body.Content -match "Copilot|artificial intelligence"
    } |
    Sort-Object LastModifiedDateTime -Descending

$aiUpdates = @()
foreach ($msg in $messages) {
    $aiUpdates += [PSCustomObject]@{
        Id          = $msg.Id
        Title       = $msg.Title
        Category    = $msg.Category
        Severity    = $msg.Severity
        StartDate   = $msg.StartDateTime
        LastUpdated = $msg.LastModifiedDateTime
        ActionRequired = $msg.ActionRequiredByDateTime
    }
}

Write-Host "Found $($aiUpdates.Count) AI-related Message Center posts."
$aiUpdates | Format-Table Title, Severity, LastUpdated -AutoSize
$aiUpdates | Export-Csv "AIServiceUpdates_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Service Health Check for AI Workloads

```powershell
# Monitor service health for AI-related Microsoft 365 workloads
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Devices.ServiceAnnouncement
Connect-MgGraph -Scopes "ServiceHealth.Read.All"

$healthOverviews = Get-MgServiceAnnouncementHealthOverview
$aiWorkloads = $healthOverviews | Where-Object {
    $_.Service -match "Microsoft 365|SharePoint|Exchange|Teams|Purview"
}

Write-Host "=== AI Workload Service Health ==="
foreach ($workload in $aiWorkloads) {
    $status = if ($workload.Status -eq "ServiceOperational") { "Healthy" } else { $workload.Status }
    Write-Host "  $($workload.Service): $status"
}

$aiWorkloads | Select-Object Service, Status |
    Export-Csv "AIWorkloadHealth_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Message Center AI Updates | Weekly | Track service changes affecting AI governance |
| Service Health Check | Daily | Monitor AI workload availability |
| Configuration Snapshot | Monthly | Document AI service configuration for audit trail |
| Vendor Risk Reassessment | Semi-annually | Formal reassessment of Microsoft AI services |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate vendor risk processes
- See [Troubleshooting](troubleshooting.md) for vendor assessment issues
