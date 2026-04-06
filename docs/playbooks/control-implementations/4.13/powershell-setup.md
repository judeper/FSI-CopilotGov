# Control 4.13: Copilot Extensibility and Agent Operations Governance — PowerShell Setup

Automation scripts for managing Copilot plugins, connectors, and related extensibility governance.

## Prerequisites

- **Modules:** `Microsoft.Graph`, `ExchangeOnlineManagement`
- **Permissions:** Application Administrator, Entra Global Admin
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "Application.Read.All", "AppCatalog.ReadWrite.All", "AuditLog.Read.All"
```

## Scripts

### Script 1: Copilot Plugin and App Inventory

```powershell
# Generate an inventory of all apps and plugins available to Copilot
$apps = Get-MgServicePrincipal -All | Where-Object {
    $_.Tags -contains "CopilotExtension" -or
    $_.Tags -contains "TeamsApp" -or
    $_.AppDisplayName -like "*Copilot*"
}

$inventory = $apps | ForEach-Object {
    [PSCustomObject]@{
        AppName        = $_.AppDisplayName
        AppId          = $_.AppId
        Publisher      = $_.PublisherName
        CreatedDate    = $_.CreatedDateTime
        Permissions    = ($_.Oauth2PermissionScopes | Select-Object -First 3 -ExpandProperty Value) -join ", "
        ConsentType    = if ($_.AppOwnerOrganizationId -eq $null) { "Microsoft" } else { "Third-Party" }
    }
}

Write-Host "Copilot Plugin and App Inventory:" -ForegroundColor Cyan
$inventory | Format-Table AppName, Publisher, ConsentType -AutoSize
$inventory | Export-Csv "CopilotPluginInventory_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Total plugins: $($inventory.Count)" -ForegroundColor Green
```

### Script 2: Graph Connector Inventory and Risk Assessment

```powershell
# Inventory Graph connectors and assess data sensitivity
$connectors = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/external/connections" `
    -OutputType PSObject

if ($connectors.value) {
    $connectorReport = $connectors.value | ForEach-Object {
        [PSCustomObject]@{
            ConnectorName  = $_.name
            ConnectorId    = $_.id
            State          = $_.state
            Description    = $_.description
        }
    }

    Write-Host "Graph Connector Inventory:" -ForegroundColor Cyan
    $connectorReport | Format-Table -AutoSize
    $connectorReport | Export-Csv "GraphConnectors_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
} else {
    Write-Host "No Graph connectors configured" -ForegroundColor Yellow
}
```

### Script 3: Plugin Consent and Permission Audit

```powershell
# Audit app consent and permissions for Copilot-related applications
$appConsents = Get-MgOauth2PermissionGrant -All | Where-Object {
    $_.ConsentType -eq "AllPrincipals"
}

$consentReport = foreach ($consent in $appConsents) {
    $sp = Get-MgServicePrincipal -ServicePrincipalId $consent.ClientId -ErrorAction SilentlyContinue
    if ($sp) {
        [PSCustomObject]@{
            AppName       = $sp.AppDisplayName
            ConsentType   = $consent.ConsentType
            Scope         = $consent.Scope
            ResourceId    = $consent.ResourceId
            GrantedDate   = $consent.StartDateTime
        }
    }
}

Write-Host "Organization-Wide App Consent Audit:" -ForegroundColor Cyan
$consentReport | Where-Object { $_.Scope -like "*ReadWrite*" -or $_.Scope -like "*FullControl*" } |
    Format-Table AppName, Scope, GrantedDate -AutoSize

$highRisk = $consentReport | Where-Object { $_.Scope -like "*ReadWrite*" -or $_.Scope -like "*FullControl*" }
if ($highRisk) {
    Write-Warning "$($highRisk.Count) apps have broad read-write or full control permissions"
}

$consentReport | Export-Csv "AppConsentAudit_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Plugin Usage Monitoring

```powershell
# Monitor plugin usage within Copilot interactions
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$pluginEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "CopilotPluginRun" `
    -ResultSize 5000

Write-Host "Copilot Plugin Usage (Last 30 Days):" -ForegroundColor Cyan
Write-Host "Total plugin execution events: $($pluginEvents.Count)"

if ($pluginEvents.Count -gt 0) {
    $pluginSummary = $pluginEvents | Group-Object {
        ($_.AuditData | ConvertFrom-Json).PluginName
    } | Select-Object @{N='Plugin'; E={$_.Name}}, @{N='ExecutionCount'; E={$_.Count}} |
        Sort-Object ExecutionCount -Descending

    $pluginSummary | Format-Table -AutoSize
    $pluginSummary | Export-Csv "PluginUsage_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
}
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Plugin inventory | Monthly | Script 1 |
| Graph connector review | Quarterly | Script 2 |
| Permission audit | Monthly | Script 3 |
| Plugin usage monitoring | Weekly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate extensibility governance
- See [Troubleshooting](troubleshooting.md) for plugin governance issues
