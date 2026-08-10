# Control 2.13: Plugin and Graph Connector Security — PowerShell Setup

Automation scripts for managing plugin and Graph connector security.

## Prerequisites

- Microsoft Graph PowerShell SDK
- Microsoft Graph read permissions for applications, external connections, and policies
- Appropriate Microsoft Entra and Microsoft 365 administrator roles

## Scripts

### Script 1: Candidate Plugin and App OAuth Audit

```powershell
# Audit delegated OAuth grants for candidate plugin and agent service principals.
# Reconcile this best-effort result with the Agent Registry and Agent Tools inventory.
Import-Module Microsoft.Graph.Applications
Connect-MgGraph -Scopes "Application.Read.All","Directory.Read.All"

$apps = Get-MgServicePrincipal -All -Property "displayName,appId,oauth2PermissionScopes,appRoles"
$copilotApps = $apps | Where-Object {
    $_.Tags -contains "CopilotExtension" -or $_.DisplayName -match "Copilot|Plugin|Agent"
}

$appReport = @()
foreach ($app in $copilotApps) {
    $grants = Get-MgServicePrincipalOauth2PermissionGrant -ServicePrincipalId $app.Id -ErrorAction SilentlyContinue
    $scopes = @(
        $grants.Scope -split " " |
            Where-Object { $_ } |
            Sort-Object -Unique
    )
    $appReport += [PSCustomObject]@{
        Name         = $app.DisplayName
        AppId        = $app.AppId
        PermCount    = $scopes.Count
        Permissions  = ($scopes -join "; ")
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

This script inventories Microsoft Graph external connections. Verify each connection's access permissions separately under **Microsoft 365 Admin Center > Copilot > Connectors > Your Connections**; the Graph inventory is not proof that source ACLs are configured correctly.

### Script 3: App Consent Policy Verification

```powershell
# Verify user self-consent is disabled and the admin consent workflow is enabled
Import-Module Microsoft.Graph.Identity.SignIns
Connect-MgGraph -Scopes "Policy.Read.All"

$authorizationPolicy = Get-MgPolicyAuthorizationPolicy
$assignedPolicies = @(
    $authorizationPolicy.DefaultUserRolePermissions.PermissionGrantPoliciesAssigned
)
$selfConsentPolicies = @(
    $assignedPolicies |
        Where-Object { $_ -like "managePermissionGrantsForSelf.*" }
)
$ownedResourcePolicies = @(
    $assignedPolicies |
        Where-Object { $_ -like "managePermissionGrantsForOwnedResource.*" }
)
$adminConsentPolicy = Get-MgPolicyAdminConsentRequestPolicy

$result = [PSCustomObject]@{
    UserConsentDisabled        = ($selfConsentPolicies.Count -eq 0)
    AdminConsentWorkflowEnabled = $adminConsentPolicy.IsEnabled
    SelfConsentPolicies         = ($selfConsentPolicies -join "; ")
    OwnedResourcePolicies       = ($ownedResourcePolicies -join "; ")
}

$result | Format-List

if (-not $result.UserConsentDisabled) {
    Write-Warning "User consent remains enabled by a managePermissionGrantsForSelf policy."
}
if (-not $result.AdminConsentWorkflowEnabled) {
    Write-Warning "The admin consent request workflow is disabled."
}
```

`AllowedToCreateApps` controls whether users can register applications; it does not report whether users can grant OAuth consent. User consent is disabled only when no `managePermissionGrantsForSelf.*` policy is assigned to the default user role. Existing grants must be reviewed and revoked separately.

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Plugin Permission Audit | Monthly | Reconcile portal inventory and delegated OAuth scope |
| Connector Security Audit | Monthly | Verify connector configurations |
| Consent Policy Check | Quarterly | Verify self-consent is disabled and request workflow is active |

## Microsoft Guidance

- [Configure how users consent to applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=ms-powershell)
- [Configure the admin consent workflow](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-admin-consent-workflow)

## Next Steps

- See [Verification & Testing](verification-testing.md) for plugin security validation
- See [Troubleshooting](troubleshooting.md) for plugin issues
- Back to [Control 2.13](../../../controls/pillar-2-security/2.13-plugin-connector-security.md)
