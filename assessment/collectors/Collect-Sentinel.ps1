<#
.SYNOPSIS
    Collects Microsoft Sentinel / Log Analytics configuration data for the FSI-CopilotGov assessment engine.

.DESCRIPTION
    Validates Sentinel workspace existence, enumerates data connectors (Office 365,
    Microsoft Defender for Cloud Apps, Microsoft Copilot where visible), and runs a
    KQL audit query against CopilotActivity to confirm Copilot interaction audit
    records are queryable in the last 7 days.

    Outputs a structured JSON file (sentinel.json) consumed by the assessment engine.

    Pattern references:
      - Set-InactivityTimeout.ps1 — Azure token acquisition (Get-AzAccessToken)
      - Invoke-SharingAudit.ps1 — REST API invocation patterns
      - Invoke-HardeningBaselineCheck.ps1 — multi-control baseline check structure

.PARAMETER TenantId
    Mandatory. Microsoft Entra tenant ID.

.PARAMETER AuthMode
    Mandatory. Authentication mode: Interactive or ServicePrincipal.

.PARAMETER ClientId
    Optional. Application (client) ID for service principal authentication.

.PARAMETER ClientSecret
    Optional. Client secret as SecureString for service principal authentication.

.PARAMETER OutputDir
    Mandatory. Root output directory. Collected JSON is written to $OutputDir\collected\sentinel.json.

.PARAMETER SubscriptionId
    Mandatory. Azure subscription ID containing the Sentinel workspace.

.PARAMETER ResourceGroup
    Mandatory. Resource group name containing the Sentinel workspace.

.PARAMETER WorkspaceName
    Mandatory. Log Analytics workspace name.

.OUTPUTS
    sentinel.json — JSON file with workspace details, data connectors, and KQL audit check results.

.NOTES
    Part of the FSI-CopilotGov Assessment Engine — Sentinel Collector. (Engine lineage ported from FSI-AgentGov v1.4.)
    Requires Az.OperationalInsights module.
    Exit codes: 0 = success, 1 = partial failure (some sections null), 2 = total failure.
    Version: 1.0.0
#>

#Requires -Version 7.0

[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$TenantId,

    [Parameter(Mandatory)]
    [ValidateSet('Interactive', 'ServicePrincipal')]
    [string]$AuthMode,

    [Parameter()]
    [string]$ClientId,

    [Parameter()]
    [securestring]$ClientSecret,

    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$OutputDir,

    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$SubscriptionId,

    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$ResourceGroup,

    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$WorkspaceName
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
. (Join-Path $PSScriptRoot 'Collect-Sentinel.CopilotActivity.ps1')

# ─── Initialise ──────────────────────────────────────────────────────
$warnings = [System.Collections.Generic.List[string]]::new()
$collectedDir = Join-Path $OutputDir 'collected'
if (-not (Test-Path $collectedDir)) {
    New-Item -ItemType Directory -Path $collectedDir -Force | Out-Null
}
$outputFile = Join-Path $collectedDir 'sentinel.json'

# ─── Module Import ───────────────────────────────────────────────────
Import-Module Az.OperationalInsights -ErrorAction Stop
Write-Verbose "Loaded Az.OperationalInsights module."

# ─── Authentication ──────────────────────────────────────────────────
# Pattern: Set-InactivityTimeout.ps1 — Connect-AzAccount for token acquisition
Write-Verbose "Authenticating to Azure in $AuthMode mode..."

if ($AuthMode -eq 'Interactive') {
    Connect-AzAccount -TenantId $TenantId -SubscriptionId $SubscriptionId -ErrorAction Stop
}
else {
    if (-not $ClientId -or -not $ClientSecret) {
        throw "ServicePrincipal auth requires -ClientId and -ClientSecret parameters."
    }
    $credential = [System.Management.Automation.PSCredential]::new($ClientId, $ClientSecret)
    Connect-AzAccount -TenantId $TenantId -SubscriptionId $SubscriptionId `
        -ServicePrincipal -Credential $credential -ErrorAction Stop
}

# Set active subscription context
Set-AzContext -SubscriptionId $SubscriptionId -ErrorAction Stop | Out-Null
Write-Verbose "Azure authentication successful. Subscription: $SubscriptionId"

# ═══════════════════════════════════════════════════════════════════════
# Section 1: Workspace Existence and Configuration
# Supports: Control 3.1 (Audit Logging), SIEM workspace validation
# ═══════════════════════════════════════════════════════════════════════
$workspaceInfo = $null
try {
    Write-Verbose "Section 1: Validating Sentinel workspace existence..."
    $workspace = Get-AzOperationalInsightsWorkspace `
        -ResourceGroupName $ResourceGroup `
        -Name $WorkspaceName `
        -ErrorAction Stop

    $workspaceInfo = [PSCustomObject]@{
        WorkspaceId       = $workspace.CustomerId
        ResourceId        = $workspace.ResourceId
        Name              = $workspace.Name
        Location          = $workspace.Location
        ProvisioningState = $workspace.ProvisioningState
        Sku               = $workspace.Sku
        RetentionInDays   = $workspace.RetentionInDays
        WorkspaceCapping  = $workspace.WorkspaceCapping
    }
    Write-Verbose "  Workspace '$WorkspaceName' found. State: $($workspace.ProvisioningState), SKU: $($workspace.Sku)"
}
catch {
    $warnings.Add("Section 1 (Workspace) failed: $($_.Exception.Message)")
    Write-Warning $warnings[-1]
}

# ═══════════════════════════════════════════════════════════════════════
# Section 2: Data Connectors
# Supports: Control 3.1 (Audit Ingestion) — verify Office 365 and Defender for Cloud Apps connectors
# Pattern: Invoke-HardeningBaselineCheck.ps1 — baseline item enumeration
# ═══════════════════════════════════════════════════════════════════════
$dataConnectors = $null
try {
    Write-Verbose "Section 2: Enumerating Sentinel data connectors..."

    # Use Azure REST API for Sentinel data connectors (more reliable than Get-AzOperationalInsightsDataSource
    # for Sentinel-specific connectors like Office365 and Defender for Cloud Apps (kind: MicrosoftCloudAppSecurity))
    $connectorApiUri = "https://management.azure.com/subscriptions/$SubscriptionId" +
        "/resourceGroups/$ResourceGroup" +
        "/providers/Microsoft.OperationalInsights/workspaces/$WorkspaceName" +
        "/providers/Microsoft.SecurityInsights/dataConnectors?api-version=2023-02-01"

    # Acquire ARM token
    # Pattern: Set-InactivityTimeout.ps1 — Get-AzAccessToken for resource-specific tokens
    $armToken = $null
    try {
        $armTokenResult = Get-AzAccessToken -ResourceUrl "https://management.azure.com" -ErrorAction Stop
        if ($armTokenResult.Token -is [securestring]) {
            $armToken = $armTokenResult.Token | ConvertFrom-SecureString -AsPlainText
        }
        else {
            $armToken = $armTokenResult.Token
        }
    }
    catch {
        throw "Failed to acquire ARM token: $($_.Exception.Message)"
    }

    $headers = @{
        Authorization  = "Bearer $armToken"
        'Content-Type' = 'application/json'
    }
    $connectorResponse = Invoke-RestMethod -Uri $connectorApiUri -Method GET -Headers $headers -ErrorAction Stop

    $dataConnectors = [PSCustomObject]@{
        TotalConnectors         = if ($connectorResponse.value) { $connectorResponse.value.Count } else { 0 }
        ConnectorSummary        = if ($connectorResponse.value) {
            $connectorResponse.value | ForEach-Object {
                [PSCustomObject]@{
                    Id        = $_.id
                    Name      = $_.name
                    Kind      = $_.kind
                    Etag      = $_.etag
                }
            }
        }
        else { @() }
        Office365Enabled        = $false
        McasEnabled             = $false
        CopilotConnectorDetected = $false
    }

    if ($connectorResponse.value) {
        $dataConnectors.Office365Enabled = ($connectorResponse.value | Where-Object { $_.kind -eq 'Office365' }).Count -gt 0
        $dataConnectors.McasEnabled = ($connectorResponse.value | Where-Object { $_.kind -eq 'MicrosoftCloudAppSecurity' }).Count -gt 0
        $dataConnectors.CopilotConnectorDetected = (
            $connectorResponse.value | Where-Object {
                ($_.kind -match 'copilot') -or
                ($_.name -match 'copilot') -or
                ($_.id -match 'copilot')
            }
        ).Count -gt 0

        if (-not $dataConnectors.Office365Enabled) {
            $warnings.Add("Section 2: Office365 data connector is NOT enabled in workspace '$WorkspaceName'.")
            Write-Warning $warnings[-1]
        }
        if (-not $dataConnectors.McasEnabled) {
            $warnings.Add("Section 2: MicrosoftCloudAppSecurity data connector is NOT enabled in workspace '$WorkspaceName'.")
            Write-Warning $warnings[-1]
        }
        if (-not $dataConnectors.CopilotConnectorDetected) {
            $warnings.Add("Section 2: No data connector with a Copilot name/kind signature was detected. Verify the Microsoft Copilot connector (preview) is enabled in Sentinel.")
            Write-Warning $warnings[-1]
        }
    }
    Write-Verbose "  Data connectors enumerated. Office365=$($dataConnectors.Office365Enabled), MCAS=$($dataConnectors.McasEnabled), CopilotConnectorDetected=$($dataConnectors.CopilotConnectorDetected)"
}
catch {
    $warnings.Add("Section 2 (Data Connectors) failed: $($_.Exception.Message)")
    Write-Warning $warnings[-1]
}

# ═══════════════════════════════════════════════════════════════════════
# Section 3: KQL Audit Check — Copilot Interaction Records
# Supports: Control 4.11 (Sentinel integration) and supplemental 3.1 audit evidence
# ═══════════════════════════════════════════════════════════════════════
$kqlAuditCheck = $null
try {
    Write-Verbose "Section 3: Running KQL audit check for CopilotInteraction records..."

    if ($workspaceInfo) {
        $schemaQuery = Get-CopilotActivitySchemaQuery
        $kqlQuery = Get-CopilotActivityDataQuery
        $requiredColumns = @(Get-CopilotActivityRequiredColumns)
        $collectionCaveat = 'CopilotActivity is populated by the Microsoft Copilot data connector (preview). Use RecordType == "CopilotInteraction" for collection evidence. OfficeActivity is not equivalent proof for Copilot interaction coverage and must not be used as a substitute.'
        $kqlAuditCheck = [PSCustomObject]@{
            Table            = 'CopilotActivity'
            RecordTypeFilter = 'CopilotInteraction'
            SchemaQuery      = $schemaQuery
            Query            = $kqlQuery
            QueryTimeRange   = '7 days'
            ExecutedAt       = (Get-Date -Format 'o')
            RequiredColumns  = $requiredColumns
            AvailableColumns = @()
            MissingColumns   = @()
            RecordCount      = 0
            HasRecords       = $false
            Status           = 'query_failure'
            TableAvailable   = $false
            SampleRows       = @()
            QueryError       = $null
            CollectionCaveat = $collectionCaveat
        }

        try {
            $schemaResult = Invoke-AzOperationalInsightsQuery `
                -WorkspaceId $workspaceInfo.WorkspaceId `
                -Query $schemaQuery `
                -ErrorAction Stop

            $availableColumns = @(Get-CopilotActivitySchemaColumnNames -SchemaRows $schemaResult.Results)
            $missingColumns = @(Get-CopilotActivityMissingColumns -AvailableColumns $availableColumns)
            $kqlAuditCheck.AvailableColumns = $availableColumns
            $kqlAuditCheck.MissingColumns = $missingColumns

            if ($missingColumns.Count -gt 0) {
                $kqlAuditCheck.Status = 'schema_mismatch'
                $kqlAuditCheck.QueryError = "CopilotActivity schema missing expected column(s): $($missingColumns -join ', ')"
                $warnings.Add("Section 3: CopilotActivity schema mismatch. Missing expected column(s): $($missingColumns -join ', '). Treat collection as failed-closed until schema is verified.")
                Write-Warning $warnings[-1]
            }
            else {
                $kqlAuditCheck.TableAvailable = $true

                try {
                    $queryResult = Invoke-AzOperationalInsightsQuery `
                        -WorkspaceId $workspaceInfo.WorkspaceId `
                        -Query $kqlQuery `
                        -ErrorAction Stop

                    $rows = @($queryResult.Results)
                    $recordCount = $rows.Count
                    $kqlAuditCheck.RecordCount = $recordCount
                    $kqlAuditCheck.HasRecords = ($recordCount -gt 0)
                    $kqlAuditCheck.Status = Get-CopilotActivityAssessmentStatus -RowCount $recordCount
                    $kqlAuditCheck.SampleRows = @($rows | Select-Object -First 5)

                    if ($recordCount -eq 0) {
                        $warnings.Add("Section 3: CopilotActivity query returned zero CopilotInteraction records in the last 7 days. This is a fail-closed evidence gap (not equivalent to proof via OfficeActivity). Verify connector state, ingestion timing, and query permissions.")
                        Write-Warning $warnings[-1]
                    }
                    else {
                        Write-Verbose "  Found $recordCount CopilotInteraction record(s) in CopilotActivity over the last 7 days."
                    }
                }
                catch {
                    $queryError = $_.Exception.Message
                    $queryStatus = Get-CopilotActivityFailureStatus -Message $queryError
                    $kqlAuditCheck.Status = $queryStatus
                    $kqlAuditCheck.QueryError = $queryError
                    $warnings.Add("Section 3: CopilotActivity data query failed ($queryStatus): $queryError")
                    Write-Warning $warnings[-1]
                }
            }
        }
        catch {
            $schemaError = $_.Exception.Message
            $schemaStatus = Get-CopilotActivityFailureStatus -Message $schemaError
            $kqlAuditCheck.Status = $schemaStatus
            $kqlAuditCheck.QueryError = $schemaError
            if ($schemaStatus -eq 'table_or_connector_unavailable') {
                $warnings.Add("Section 3: CopilotActivity table unavailable. Verify the Microsoft Copilot connector (preview) is enabled for this workspace. OfficeActivity is not an equivalent fallback for CopilotInteraction evidence.")
            }
            else {
                $warnings.Add("Section 3: CopilotActivity schema query failed ($schemaStatus): $schemaError")
            }
            Write-Warning $warnings[-1]
        }
    }
    else {
        $kqlAuditCheck = [PSCustomObject]@{
            Table            = 'CopilotActivity'
            RecordTypeFilter = 'CopilotInteraction'
            SchemaQuery      = Get-CopilotActivitySchemaQuery
            Query            = Get-CopilotActivityDataQuery
            QueryTimeRange   = '7 days'
            ExecutedAt       = (Get-Date -Format 'o')
            RequiredColumns  = @(Get-CopilotActivityRequiredColumns)
            AvailableColumns = @()
            MissingColumns   = @()
            RecordCount      = 0
            HasRecords       = $false
            Status           = 'workspace_unavailable'
            TableAvailable   = $false
            SampleRows       = @()
            QueryError       = 'Workspace information unavailable.'
            CollectionCaveat = 'CopilotActivity is collected through the Microsoft Copilot connector (preview). OfficeActivity is not an equivalent fallback for CopilotInteraction evidence.'
        }
        $warnings.Add("Section 3 (KQL Audit): Workspace info unavailable; CopilotActivity query not attempted.")
        Write-Warning $warnings[-1]
    }
}
catch {
    $warnings.Add("Section 3 (KQL Audit) failed: $($_.Exception.Message)")
    Write-Warning $warnings[-1]
}

# ═══════════════════════════════════════════════════════════════════════
# Build Output
# ═══════════════════════════════════════════════════════════════════════
$result = [ordered]@{
    workspace         = $workspaceInfo
    data_connectors   = $dataConnectors
    kql_audit_check   = $kqlAuditCheck
    _metadata       = [ordered]@{
        collector       = 'Collect-Sentinel'
        timestamp       = (Get-Date -Format 'o')
        tenant_id       = $TenantId
        subscription_id = $SubscriptionId
        resource_group  = $ResourceGroup
        workspace_name  = $WorkspaceName
        warnings        = @($warnings)
    }
}

$json = $result | ConvertTo-Json -Depth 10
$json | Out-File -FilePath $outputFile -Encoding utf8
Write-Verbose "Output written to $outputFile"

# ─── Exit Code ───────────────────────────────────────────────────────
$sectionValues = @($workspaceInfo, $dataConnectors, $kqlAuditCheck)
$nullSections = @($sectionValues | Where-Object { $null -eq $_ })
$failedClosedStatuses = @(
    'table_or_connector_unavailable',
    'permission_failure',
    'query_failure',
    'schema_mismatch',
    'workspace_unavailable'
)
$kqlFailedClosed = $false
if ($kqlAuditCheck -and $kqlAuditCheck.PSObject.Properties['Status']) {
    $kqlFailedClosed = $failedClosedStatuses -contains [string]$kqlAuditCheck.Status
}

if ($nullSections.Count -eq $sectionValues.Count) {
    Write-Error "All sections failed to collect data. See warnings for details."
    exit 2
}
elseif ($nullSections.Count -gt 0 -or $kqlFailedClosed) {
    Write-Warning "Partial collection: $($nullSections.Count)/$($sectionValues.Count) sections returned null."
    if ($kqlFailedClosed) {
        Write-Warning "Section 3 failed-closed with status '$($kqlAuditCheck.Status)'."
    }
    exit 1
}
else {
    Write-Verbose "All sections collected successfully."
    exit 0
}
