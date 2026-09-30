# Control 4.13: Copilot Extensibility and Agent Operations Governance — PowerShell Setup

Automation scripts for managing Copilot plugins, connectors, and related extensibility governance.

> **Tenant verification required:** Microsoft 365 agent, tool, and audit APIs continue to evolve. Treat the scripts below as supplemental evidence collection; current portal evidence from **Agents > Overview**, **All agents > Registry**, **Settings**, **Tools**, and **Settings > Integrated apps** remains required.

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

### Script 4: Microsoft 365 Copilot Plugin and Agent Interaction Evidence

```powershell
# Monitor Microsoft 365 Copilot interaction records and summarize plugin evidence.
# CopilotInteraction spans multiple Microsoft Copilot products, so use an
# AppIdentity allow-list and exclude Security Copilot from the evidence set.
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com -ShowBanner:$false

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

        $sessionId = "CopilotPluginEvidence_$([guid]::NewGuid())"
        $pageNumber = 0
        $previousResultIndex = -1L
        $segmentResultCount = 0
        $segmentExhausted = $false

        do {
            $pageNumber++
            if ($pageNumber -gt 100) {
                throw "Paging safety limit reached for $segmentStart to $segmentEnd."
            }

            try {
                $page = @(
                    Search-UnifiedAuditLog `
                        -StartDate $segmentStart `
                        -EndDate $segmentEnd `
                        -RecordType CopilotInteraction `
                        -Operations "CopilotInteraction" `
                        -SessionId $sessionId `
                        -SessionCommand ReturnLargeSet `
                        -ResultSize 5000 `
                        -ErrorAction Stop
                )
            }
            catch {
                throw (
                    "Search-UnifiedAuditLog failed for segment $segmentStart to " +
                    "$segmentEnd on page $pageNumber (SessionId $sessionId). " +
                    "No evidence from this run should be treated as complete. " +
                    "Underlying error: $($_.Exception.Message)"
                )
            }

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

$pluginEvidence = foreach ($envelope in $recordEnvelopes) {
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
            UserId          = $record.UserIds -join "; "
            Workload        = $auditData.Workload
            AppIdentity     = $auditData.AppIdentity
            AppHost         = $copilotEventData.AppHost
            AgentId         = $auditData.AgentId
            AgentName       = $auditData.AgentName
            PluginName      = $plugin.Name
            PluginId        = $plugin.ID
            PluginVersion   = $plugin.Version
        }
    }
}

Write-Host "Microsoft 365 Copilot Plugin Evidence (Last 30 Days):" -ForegroundColor Cyan
Write-Host "Total CopilotInteraction envelopes collected: $($recordEnvelopes.Count)"
Write-Host "Plugin rows before scoping filters: $($pluginEvidence.Count)"

$m365PluginEvidence = @($pluginEvidence | Where-Object EvidenceStatus -eq "Accepted")
$rejectedPluginEvidence = @($pluginEvidence | Where-Object EvidenceStatus -eq "Rejected")

Write-Host "In-scope M365 Copilot plugin rows: $($m365PluginEvidence.Count)"
Write-Host "Rejected rows: $($rejectedPluginEvidence.Count)"

if ($m365PluginEvidence.Count -gt 0) {
    $pluginSummary = $m365PluginEvidence | Group-Object PluginName |
        Select-Object @{N='Plugin'; E={$_.Name}}, @{N='ExecutionCount'; E={$_.Count}} |
        Sort-Object ExecutionCount -Descending

    $pluginSummary | Format-Table -AutoSize
    $m365PluginEvidence |
        Export-Csv "M365CopilotPluginUsage_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
}
else {
    Write-Warning "No in-scope Microsoft 365 Copilot plugin evidence matched the approved AppIdentity and plugin ID allow-lists."
}

if ($rejectedPluginEvidence.Count -gt 0) {
    $rejectedPluginEvidence |
        Export-Csv "RejectedCopilotPluginUsage_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
    Write-Warning "$($rejectedPluginEvidence.Count) plugin row(s) were excluded from the M365 Copilot evidence set; review the rejected export."
}
```

The Microsoft audit schema places `AISystemPlugin` and `AppHost` under `AuditData.CopilotEventData`, while fields such as `Workload`, `AppIdentity`, `AgentId`, and `AgentName` remain at the root of `AuditData`. Microsoft also documents `CopilotInteraction` as a cross-product record type that includes Microsoft 365 Copilot, Cowork, and Security Copilot, so `Workload = Copilot` is not a sufficient product boundary by itself. Filter by an approved `AppIdentity` allow-list and keep `Copilot.Security.SecurityCopilot` out of the Microsoft 365 Copilot evidence set.

`Search-UnifiedAuditLog` returns at most 5,000 records per call. Script 4 therefore reuses a stable `SessionId` with `SessionCommand ReturnLargeSet` until each one-hour segment is exhausted, deduplicates the immutable audit record ID across page and segment boundaries, and stops if any segment reaches the 50,000-record Exchange Online session limit. If that limit is hit, reduce `SegmentDuration` and rerun; do not treat the export as complete evidence.

If you also need administrative change evidence for plugin or agent governance, search the documented admin operations separately, for example: `CreatePlugin`, `UpdatePlugin`, `EnablePlugin`, `DisableCopilotPlugin`, `DeployedAgent`, `UpdatedAgent`, `RemovedAgent`, `BlockedAgent`, `UnblockedAgent`, `DeletedAgent`, and `UpdatedTenantSettings`. Microsoft documents `EnablePlugin` in more than one Copilot product context, and `UpdatedTenantSettings` (Agent settings) is a different operation from `UpdateTenantSettings` (Copilot setting changes), so scope exported records before treating them as Microsoft 365 Copilot evidence.

### Script 5: Agent tools / MCP request evidence checklist

```powershell
Write-Host "Collect this evidence from Microsoft 365 admin center > Agents > Tools:" -ForegroundColor Cyan
Write-Host "  - Available and Blocked tools / MCP servers"
Write-Host "  - Requests tab with approve/reject decision and requester"
Write-Host "  - Declared tools exposed by each BYO MCP server"
Write-Host "  - Microsoft Entra permission consent state"
Write-Host "  - Work IQ read/write setting, usage-based billing plan, and spending policy where Work IQ is enabled"
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Plugin inventory | Monthly | Script 1 |
| Graph connector review | Quarterly | Script 2 |
| Permission audit | Monthly | Script 3 |
| M365 Copilot plugin evidence review | Weekly | Script 4 |
| Agent tools / MCP request review | Monthly and after approvals | Script 5 evidence checklist |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate extensibility governance
- See [Troubleshooting](troubleshooting.md) for plugin governance issues
- Back to [Control 4.13](../../../controls/pillar-4-operations/4.13-extensibility-governance.md)
