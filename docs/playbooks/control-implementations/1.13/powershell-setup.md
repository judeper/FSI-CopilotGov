# Control 1.13: Extensibility Readiness — PowerShell Setup

Automation scripts for managing and monitoring Copilot extensibility components.

## Prerequisites

- Microsoft Graph PowerShell SDK
- Microsoft Teams PowerShell module (`MicrosoftTeams`)
- Entra Global Admin or Teams Admin role

## Scripts

### Script 1: Teams App and Extension Inventory

```powershell
# Inventory all Teams apps including Copilot extensions
# Requires: Microsoft Teams PowerShell module

Import-Module MicrosoftTeams
Connect-MicrosoftTeams

$apps = Get-TeamsApp
$appReport = @()

foreach ($app in $apps) {
    $appReport += [PSCustomObject]@{
        DisplayName    = $app.DisplayName
        AppId          = $app.Id
        ExternalId     = $app.ExternalId
        DistributionMethod = $app.DistributionMethod
        Publisher      = $app.Publisher
    }
}

$thirdParty = ($appReport | Where-Object DistributionMethod -eq "Store").Count
$custom = ($appReport | Where-Object DistributionMethod -eq "Organization").Count

Write-Host "=== Teams App Inventory ==="
Write-Host "Total apps: $($appReport.Count)"
Write-Host "Third-party (Store): $thirdParty"
Write-Host "Custom (Organization): $custom"

$appReport | Export-Csv "TeamsAppInventory_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Graph Connector Status Report

```powershell
# Report on Microsoft Graph connector configurations
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Search
Connect-MgGraph -Scopes "ExternalConnection.Read.All"

$connections = Get-MgExternalConnection -All
$connectorReport = @()

foreach ($conn in $connections) {
    $connectorReport += [PSCustomObject]@{
        Name        = $conn.Name
        Id          = $conn.Id
        Description = $conn.Description
        State       = $conn.State
        ConnectorId = $conn.ConnectorId
    }
}

Write-Host "=== Graph Connector Status ==="
Write-Host "Total connectors: $($connectorReport.Count)"
$connectorReport | Format-Table Name, State, ConnectorId -AutoSize
$connectorReport | Export-Csv "GraphConnectors_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Teams App Permission Policies Audit

```powershell
# Audit Teams app permission policies affecting Copilot extensions
# Requires: Microsoft Teams PowerShell module

Import-Module MicrosoftTeams
Connect-MicrosoftTeams

$policies = Get-CsTeamsAppPermissionPolicy

$policyReport = @()
foreach ($policy in $policies) {
    $policyReport += [PSCustomObject]@{
        PolicyName        = $policy.Identity
        GlobalCatalogApps = $policy.DefaultCatalogAppsType
        PrivateCatalogApps = $policy.PrivateCatalogAppsType
        ThirdPartyApps    = $policy.GlobalCatalogAppsType
    }
}

Write-Host "=== App Permission Policies ==="
$policyReport | Format-Table PolicyName, ThirdPartyApps, PrivateCatalogApps -AutoSize
$policyReport | Export-Csv "AppPermPolicies_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Extension Change Detection

```powershell
# Detect changes in Teams app installations since last scan
# Requires: Previous inventory file and Microsoft Teams module

Import-Module MicrosoftTeams
Connect-MicrosoftTeams

$currentApps = Get-TeamsApp | Select-Object DisplayName, Id, DistributionMethod
$previousFile = Get-ChildItem "TeamsAppInventory_*.csv" | Sort-Object LastWriteTime -Descending | Select-Object -First 1

if ($previousFile) {
    $previousApps = Import-Csv $previousFile.FullName
    $previousIds = $previousApps.AppId

    $newApps = $currentApps | Where-Object { $_.Id -notin $previousIds }
    if ($newApps) {
        Write-Host "=== New Apps Detected ===" -ForegroundColor Yellow
        $newApps | Format-Table DisplayName, DistributionMethod -AutoSize
    } else {
        Write-Host "No new apps detected since last scan."
    }
} else {
    Write-Host "No previous inventory found. Run Script 1 first to establish baseline."
}
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| App Inventory | Weekly | Detect new extensions |
| Graph Connector Status | Monthly | Monitor connector health and configuration |
| Permission Policy Audit | Quarterly | Verify governance policies are enforced |
| Change Detection | Weekly | Alert on unauthorized extension installations |

## Next Steps

- See [Verification & Testing](verification-testing.md) for extensibility governance validation
- See [Troubleshooting](troubleshooting.md) for extension management issues
- Back to [Control 1.13](../../../controls/pillar-1-readiness/1.13-extensibility-readiness.md)
