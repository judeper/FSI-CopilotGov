# Control 2.13: Plugin and Graph Connector Security — PowerShell Setup

Automation scripts for managing plugin and Graph connector security.

## Prerequisites

- PowerShell 7.x
- Microsoft Graph PowerShell SDK for Scripts 1–3
- Exchange Online PowerShell module (`ExchangeOnlineManagement`) for Script 4
- Microsoft Graph read permissions for applications, external connections, and policies
- The **View-Only Audit Logs** or **Audit Logs** role in Exchange Online for `Search-UnifiedAuditLog`
- Appropriate Microsoft Entra and Microsoft 365 administrator roles

Install the required modules once:

```powershell
Install-Module Microsoft.Graph -Scope CurrentUser
Install-Module ExchangeOnlineManagement -Scope CurrentUser
```

Scripts 1–3 connect to Microsoft Graph with their required scopes. Before running Script 4, connect to Exchange Online and verify that unified audit log ingestion is enabled:

```powershell
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -ShowBanner:$false
Get-AdminAuditLogConfig | Select-Object UnifiedAuditLogIngestionEnabled
```

## Scripts

### Script 1: Candidate Plugin and App OAuth Audit

```powershell
# Audit delegated OAuth grants for candidate plugin and agent service principals.
# Reconcile this best-effort result with the Agent Registry and Agent Tools inventory.
Import-Module Microsoft.Graph.Applications
Connect-MgGraph -Scopes "Application.Read.All","Directory.Read.All"

$apps = Get-MgServicePrincipal -All -Property "id,displayName,appId,tags,oauth2PermissionScopes,appRoles"
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

### Script 4: Microsoft 365 Copilot Plugin Usage Evidence

```powershell
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -ShowBanner:$false

# Populate exact values from the approved agent and plugin inventory.
# Microsoft documents values such as Copilot.MicrosoftCopilot.BizChat and
# Copilot.Studio.<app-id>; do not add Copilot.Security.SecurityCopilot.
$approvedAppIdentities = @(
    # "Copilot.MicrosoftCopilot.BizChat"
    # "Copilot.Studio.<approved-app-id>"
)
$approvedPluginIds = @(
    # "<approved-plugin-id>"
)

if ($approvedAppIdentities.Count -eq 0 -or $approvedPluginIds.Count -eq 0) {
    throw "Populate the approved AppIdentity and plugin ID allow-lists before collecting evidence."
}

function Get-PagedCopilotAuditRecord {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [datetime]$StartDate,

        [Parameter(Mandatory)]
        [datetime]$EndDate,

        [timespan]$SegmentDuration = [timespan]::FromHours(1)
    )

    if ($EndDate -le $StartDate) {
        throw "EndDate must be later than StartDate."
    }
    if ($SegmentDuration -le [timespan]::Zero) {
        throw "SegmentDuration must be greater than zero."
    }

    $records = [System.Collections.Generic.List[object]]::new()
    $seenRecordIds = [System.Collections.Generic.HashSet[string]]::new(
        [System.StringComparer]::OrdinalIgnoreCase
    )

    for ($segmentStart = $StartDate; $segmentStart -lt $EndDate; $segmentStart = $segmentEnd) {
        $segmentEnd = $segmentStart.Add($SegmentDuration)
        if ($segmentEnd -gt $EndDate) {
            $segmentEnd = $EndDate
        }

        $sessionId = "CopilotPluginAudit_$([guid]::NewGuid())"
        $pageNumber = 0
        $previousResultIndex = -1L
        $segmentResultCount = 0
        $segmentExhausted = $false

        do {
            $pageNumber++
            if ($pageNumber -gt 100) {
                throw "Paging safety limit reached for $segmentStart to $segmentEnd."
            }

            $page = @(
                Search-UnifiedAuditLog `
                    -StartDate $segmentStart `
                    -EndDate $segmentEnd `
                    -RecordType CopilotInteraction `
                    -Operations "CopilotInteraction" `
                    -SessionId $sessionId `
                    -SessionCommand ReturnLargeSet `
                    -ResultSize 5000
            )

            if ($page.Count -eq 0) {
                $segmentExhausted = $true
                break
            }

            $segmentResultCount += $page.Count
            $newRecordCount = 0

            foreach ($record in $page) {
                $auditData = $record.AuditData | ConvertFrom-Json
                $recordId = [string]$auditData.Id
                if ([string]::IsNullOrWhiteSpace($recordId)) {
                    throw "An audit record is missing AuditData.Id; safe deduplication is not possible."
                }

                if ($seenRecordIds.Add($recordId)) {
                    $records.Add(
                        [PSCustomObject]@{
                            Record    = $record
                            AuditData = $auditData
                        }
                    )
                    $newRecordCount++
                }
            }

            $lastResult = $page[-1]
            $hasResultIndex = $null -ne $lastResult.ResultIndex -and
                -not [string]::IsNullOrWhiteSpace([string]$lastResult.ResultIndex)
            $hasResultCount = $null -ne $lastResult.ResultCount -and
                -not [string]::IsNullOrWhiteSpace([string]$lastResult.ResultCount)

            if ($hasResultIndex) {
                $resultIndex = [long]$lastResult.ResultIndex
                if ($resultIndex -le $previousResultIndex -and $newRecordCount -eq 0) {
                    throw "Audit paging made no progress for $segmentStart to $segmentEnd."
                }
                $previousResultIndex = $resultIndex
            }

            $moreRecordsProperty = $lastResult.AuditSearchRequestMetadata.PSObject.Properties[
                "moreRecordsAvailable"
            ]
            if ($null -ne $moreRecordsProperty) {
                $segmentExhausted = -not [System.Convert]::ToBoolean(
                    $moreRecordsProperty.Value
                )
            }
            elseif ($hasResultIndex -and $hasResultCount) {
                $segmentExhausted = (
                    [long]$lastResult.ResultIndex -eq [long]$lastResult.ResultCount
                )
            }

            if (
                $segmentResultCount -ge 50000 -or
                ($hasResultCount -and [long]$lastResult.ResultCount -ge 50000)
            ) {
                throw (
                    "The $segmentStart to $segmentEnd segment reached the Exchange Online " +
                    "50,000-record session limit. Reduce SegmentDuration and rerun; this " +
                    "result cannot be represented as complete."
                )
            }

            if (-not $segmentExhausted -and $newRecordCount -eq 0) {
                throw "Audit paging returned only duplicate records before reporting exhaustion."
            }
        }
        while (-not $segmentExhausted)
    }

    return $records
}

$endDate = (Get-Date).ToUniversalTime()
$startDate = $endDate.AddDays(-30)
$recordEnvelopes = @(
    Get-PagedCopilotAuditRecord -StartDate $startDate -EndDate $endDate
)

$pluginUsageRows = @(
    foreach ($envelope in $recordEnvelopes) {
        $record = $envelope.Record
        $auditData = $envelope.AuditData
        $copilotEventData = $auditData.CopilotEventData

        foreach ($plugin in @($copilotEventData.AISystemPlugin)) {
            if ($null -eq $plugin) {
                continue
            }

            $rejectionReasons = @()
            if ($auditData.Workload -ne "Copilot") {
                $rejectionReasons += "Unexpected workload"
            }
            if (([string]$auditData.AppIdentity) -like "Copilot.Security.*") {
                $rejectionReasons += "Security Copilot is out of scope"
            }
            elseif ($approvedAppIdentities -notcontains [string]$auditData.AppIdentity) {
                $rejectionReasons += "AppIdentity is not approved"
            }
            if ($approvedPluginIds -notcontains [string]$plugin.ID) {
                $rejectionReasons += "Plugin ID is not approved"
            }

            [PSCustomObject]@{
                EvidenceStatus  = if ($rejectionReasons.Count -eq 0) { "Accepted" } else { "Rejected" }
                RejectionReason = $rejectionReasons -join "; "
                CreationDate    = $record.CreationDate
                UserId           = $record.UserIds -join "; "
                Workload         = $auditData.Workload
                AppIdentity      = $auditData.AppIdentity
                AppHost          = $copilotEventData.AppHost
                AgentId          = $auditData.AgentId
                AgentName        = $auditData.AgentName
                PluginName       = $plugin.Name
                PluginId         = $plugin.ID
                PluginVersion    = $plugin.Version
            }
        }
    }
)

$m365PluginUsage = @($pluginUsageRows | Where-Object EvidenceStatus -eq "Accepted")
$rejectedPluginUsage = @($pluginUsageRows | Where-Object EvidenceStatus -eq "Rejected")

$m365PluginUsage |
    Export-Csv "M365CopilotPluginUsage_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
$rejectedPluginUsage |
    Export-Csv "RejectedCopilotPluginUsage_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation

if ($rejectedPluginUsage.Count -gt 0) {
    Write-Warning "$($rejectedPluginUsage.Count) plugin record(s) were excluded from M365 evidence; review the rejected export."
}
```

The Microsoft audit schema places `AISystemPlugin` and `AppHost` inside `AuditData.CopilotEventData`; the script keeps root-level fields such as `Workload` and `AppIdentity` separate. The Microsoft audit catalog lists `EnablePlugin` for both Microsoft 365 Copilot administration and Security Copilot platform management, so this script does not use that overloaded operation. `CopilotInteraction` also spans multiple Microsoft Copilot products, and `Workload = Copilot` is not a sufficient product boundary. Microsoft's [audit examples](https://learn.microsoft.com/en-us/purview/audit-copilot#example-copilot-scenarios-for-user-activities) show distinct `AppIdentity` values for Microsoft Copilot and Security Copilot, and Microsoft directs administrators to export records and filter that property offline. This script additionally requires an exact `CopilotEventData.AISystemPlugin.ID` match. Unknown identities and `Copilot.Security.SecurityCopilot` therefore fail closed into a separate rejected export instead of entering the Microsoft 365 Copilot evidence set.

`Search-UnifiedAuditLog` returns at most 5,000 records per call. Script 4 reuses a stable `SessionId` with `SessionCommand ReturnLargeSet` until each one-hour segment is exhausted, and deduplicates the immutable audit record ID across page and segment boundaries. Exchange Online limits a `ReturnLargeSet` session to 50,000 records. If any segment reaches that limit, the script stops instead of claiming a complete result; reduce `SegmentDuration` (for example, to 15 minutes) and rerun. For high-volume, recurring ingestion, use the Office 365 Management Activity API rather than treating this cmdlet as a guaranteed bulk-export interface.

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Plugin Permission Audit | Monthly | Reconcile portal inventory and delegated OAuth scope |
| Connector Security Audit | Monthly | Verify connector configurations |
| Consent Policy Check | Quarterly | Verify self-consent is disabled and request workflow is active |
| M365 Copilot Plugin Usage Audit | Monthly | Filter interaction telemetry by approved application and plugin IDs |

## Microsoft Guidance

- [Configure how users consent to applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=ms-powershell)
- [Configure the admin consent workflow](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-admin-consent-workflow)
- [Audit logs for Copilot and AI applications](https://learn.microsoft.com/en-us/purview/audit-copilot)
- [Use a PowerShell script to search the audit log](https://learn.microsoft.com/en-us/purview/audit-log-search-script)
- [Connect to Exchange Online PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-online-powershell)
- [Microsoft 365 audit log activities](https://learn.microsoft.com/en-us/purview/audit-log-activities)

## Next Steps

- See [Verification & Testing](verification-testing.md) for plugin security validation
- See [Troubleshooting](troubleshooting.md) for plugin issues
- Back to [Control 2.13](../../../controls/pillar-2-security/2.13-plugin-connector-security.md)
