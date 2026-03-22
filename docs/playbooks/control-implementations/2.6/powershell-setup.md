# Control 2.6: Copilot Web Search and Web Grounding Controls — PowerShell Setup

Automation scripts for managing Copilot web search and grounding controls.

## Prerequisites

- Microsoft Graph PowerShell SDK
- Global Administrator role
- Microsoft 365 Admin Center API access

## Scripts

### Script 1: Check Web Search Configuration

```powershell
# Verify Copilot web search configuration
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Beta.Identity.DirectoryManagement
Connect-MgGraph -Scopes "Policy.Read.All","Organization.Read.All"

# Check tenant Copilot settings
$org = Get-MgOrganization
Write-Host "=== Copilot Web Search Configuration ==="
Write-Host "Tenant: $($org.DisplayName)"
Write-Host ""
Write-Host "NOTE: Web search toggle is managed via Microsoft 365 Admin Center."
Write-Host "Verify at: Admin Center > Copilot > Settings > Data access > Web search"
Write-Host ""
Write-Host "Recommended FSI setting: DISABLED for all users"
```

### Script 2: Audit Web-Related Plugin Access

```powershell
# Audit Teams apps and plugins that access web content
# Requires: Microsoft Teams PowerShell module

Import-Module MicrosoftTeams
Connect-MicrosoftTeams

$apps = Get-TeamsApp | Where-Object {
    $_.DisplayName -match "Web|Browse|Search|Internet|Bing"
}

$webApps = @()
foreach ($app in $apps) {
    $webApps += [PSCustomObject]@{
        Name          = $app.DisplayName
        AppId         = $app.Id
        Publisher     = $app.Publisher
        Distribution  = $app.DistributionMethod
    }
}

Write-Host "=== Web-Related Apps/Plugins ==="
if ($webApps.Count -gt 0) {
    $webApps | Format-Table Name, Publisher, Distribution -AutoSize
} else {
    Write-Host "No web-related apps detected."
}
$webApps | Export-Csv "WebPlugins_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Monitor for Web Search Usage in Audit Logs

```powershell
# Search audit logs for web search activity in Copilot
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30).ToString("MM/dd/yyyy")
$endDate = (Get-Date).ToString("MM/dd/yyyy")

$webSearchEvents = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -RecordType "CopilotInteraction" -ResultSize 5000

$webGrounded = @()
foreach ($event in $webSearchEvents) {
    $data = $event.AuditData | ConvertFrom-Json
    if ($data.CopilotEventData.WebSearchUsed -eq $true) {
        $webGrounded += [PSCustomObject]@{
            Date     = $event.CreationDate
            User     = $event.UserIds
            Activity = $event.Operations
        }
    }
}

Write-Host "Web-grounded Copilot interactions (last 30 days): $($webGrounded.Count)"
if ($webGrounded.Count -gt 0) {
    Write-Host "WARNING: Web search activity detected. Review governance policy."
    $webGrounded | Export-Csv "WebSearchUsage_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
}
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Web Search Config Check | Weekly | Verify web search remains disabled |
| Web Plugin Audit | Monthly | Detect new web-accessing plugins |
| Web Search Usage Monitor | Weekly | Alert on any web search activity |

## Next Steps

- See [Verification & Testing](verification-testing.md) for web control validation
- See [Troubleshooting](troubleshooting.md) for web control issues
