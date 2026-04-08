# Control 2.14: Declarative Agents from SharePoint Governance — PowerShell Setup

Automation scripts for managing and monitoring declarative Copilot agents.

## Prerequisites

- SharePoint Online Management Shell
- Microsoft Graph PowerShell SDK
- SharePoint Admin role

## Scripts

### Script 1: Declarative Agent Inventory

```powershell
# Inventory declarative agents and their data sources
# Note: Agent management APIs may be in preview
# NOTE: This script provides guidance only. For actual agent enumeration, use the Graph API: GET /beta/appCatalogs/agents/packages
Import-Module Microsoft.Graph.Search
Connect-MgGraph -Scopes "Sites.Read.All"

Write-Host "=== Declarative Agent Inventory ==="
Write-Host ""
Write-Host "Declarative agent enumeration may require admin portal review."
Write-Host "Check: Admin Center > Agents > Settings"
Write-Host ""
Write-Host "For each active agent, document:"
Write-Host "  - Agent name and purpose"
Write-Host "  - Data source (SharePoint site/library URL)"
Write-Host "  - Creator and creation date"
Write-Host "  - Sharing scope (individual, team, organization)"
Write-Host "  - Governance approval status"
```

### Script 2: Agent Source Site Security Verification

```powershell
# Verify security posture of sites used as agent data sources
Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$agentSources = Import-Csv "AgentDataSources.csv"  # CSV with Url column
$secReport = @()

foreach ($source in $agentSources) {
    $site = Get-SPOSite -Identity $source.Url -Detailed -ErrorAction SilentlyContinue
    if ($site) {
        $secReport += [PSCustomObject]@{
            Url               = $source.Url
            Title             = $site.Title
            SharingCapability = $site.SharingCapability
            SensitivityLabel  = $site.SensitivityLabel
            ConditionalAccess = $site.ConditionalAccessPolicy
            Owner             = $site.Owner
            IsSecure = (
                $site.SharingCapability -eq "Disabled" -or
                $site.SharingCapability -eq "ExistingExternalUserSharingOnly"
            ) -and ($null -ne $site.SensitivityLabel)
        }
    }
}

$secure = ($secReport | Where-Object IsSecure).Count
Write-Host "Agent source sites: $($secReport.Count) | Secure: $secure"
$secReport | Format-Table Url, SharingCapability, SensitivityLabel, IsSecure -AutoSize
$secReport | Export-Csv "AgentSourceSecurity_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Monitor Agent Activity in Audit Logs

```powershell
# Track declarative agent usage and creation events
Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30).ToString("MM/dd/yyyy")
$endDate = (Get-Date).ToString("MM/dd/yyyy")

$agentEvents = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -FreeText "DeclarativeAgent" -ResultSize 1000

Write-Host "Declarative agent events (last 30 days): $($agentEvents.Count)"
foreach ($event in $agentEvents) {
    Write-Host "  $($event.CreationDate) | $($event.UserIds) | $($event.Operations)"
}

$agentEvents | Export-Csv "AgentActivity_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Agent Inventory | Monthly | Track active agents and their data sources |
| Source Site Security Check | Monthly | Verify agent data sources remain secure |
| Agent Activity Monitoring | Weekly | Track agent creation and usage |

## Next Steps

- See [Verification & Testing](verification-testing.md) for agent governance validation
- See [Troubleshooting](troubleshooting.md) for agent issues
