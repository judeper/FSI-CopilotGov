# Control 2.13: Plugin and Graph Connector Security — PowerShell Setup

Automation scripts for managing plugin and Graph connector security.

## Prerequisites

- Microsoft Teams PowerShell module
- Microsoft Graph PowerShell SDK
- Teams Administrator and Global Administrator roles

## Scripts

### Script 1: Plugin and App Permissions Audit

```powershell
# Audit Teams app permissions and consent status
Import-Module Microsoft.Graph.Applications
Connect-MgGraph -Scopes "Application.Read.All","Directory.Read.All"

$apps = Get-MgServicePrincipal -All -Property "displayName,appId,oauth2PermissionScopes,appRoles"
$copilotApps = $apps | Where-Object { $_.Tags -contains "CopilotExtension" -or $_.DisplayName -match "Copilot|Plugin" }

$appReport = @()
foreach ($app in $copilotApps) {
    $grants = Get-MgServicePrincipalOauth2PermissionGrant -ServicePrincipalId $app.Id -ErrorAction SilentlyContinue
    $appReport += [PSCustomObject]@{
        Name         = $app.DisplayName
        AppId        = $app.AppId
        PermCount    = $grants.Count
        Permissions  = ($grants.Scope -join "; ")
    }
}

Write-Host "Copilot-related apps: $($appReport.Count)"
$appReport | Format-Table Name, PermCount -AutoSize
$appReport | Export-Csv "PluginPermissions_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Graph Connector Security Audit

```powershell
# Audit Graph connector configurations and access controls
Import-Module Microsoft.Graph.Search
Connect-MgGraph -Scopes "ExternalConnection.Read.All"

$connectors = Get-MgExternalConnection -All
$connReport = @()

foreach ($conn in $connectors) {
    $connReport += [PSCustomObject]@{
        Name        = $conn.Name
        Id          = $conn.Id
        State       = $conn.State
        Description = $conn.Description
    }
}

Write-Host "=== Graph Connector Security Audit ==="
Write-Host "Active connectors: $($connReport.Count)"
$connReport | Format-Table Name, State -AutoSize
$connReport | Export-Csv "ConnectorSecurity_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: App Consent Policy Verification

```powershell
# Verify app consent policies are restrictive
Import-Module Microsoft.Graph.Identity.SignIns
Connect-MgGraph -Scopes "Policy.Read.All"

$consentPolicy = Get-MgPolicyAuthorizationPolicy
Write-Host "=== App Consent Policy ==="
Write-Host "Default User Role Permissions:"
Write-Host "  Allow user consent: $($consentPolicy.DefaultUserRolePermissions.AllowedToCreateApps)"
Write-Host "  Consent policy: $($consentPolicy.DefaultUserRolePermissions.PermissionGrantPoliciesAssigned)"
Write-Host ""
Write-Host "Recommended: User consent disabled; admin consent required for all apps"
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Plugin Permission Audit | Monthly | Review plugin access scope |
| Connector Security Audit | Monthly | Verify connector configurations |
| Consent Policy Check | Quarterly | Verify consent restrictions active |

## Next Steps

- See [Verification & Testing](verification-testing.md) for plugin security validation
- See [Troubleshooting](troubleshooting.md) for plugin issues
