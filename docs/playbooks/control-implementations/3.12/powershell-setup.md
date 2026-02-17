# Control 3.12: Evidence Collection and Audit Attestation — PowerShell Setup

Automation scripts for collecting governance evidence, generating attestation reports, and assembling audit evidence packs.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`
- **Permissions:** Compliance Administrator, AuditLog.Read.All
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "AuditLog.Read.All", "Policy.Read.All"
```

## Scripts

### Script 1: Automated Evidence Pack Generator

```powershell
# Generate a comprehensive evidence pack for Copilot governance controls
$evidenceDate = Get-Date -Format "yyyyMMdd"
$evidencePath = "EvidencePack_$evidenceDate"
New-Item -ItemType Directory -Path $evidencePath -Force | Out-Null

# Collect audit log configuration evidence
$auditConfig = Get-AdminAuditLogConfig | Select-Object UnifiedAuditLogIngestionEnabled
$auditConfig | Out-File "$evidencePath/AuditLogConfig.txt"

# Collect retention policy evidence
$retentionPolicies = Get-RetentionCompliancePolicy | Where-Object { $_.Name -like "*Copilot*" -or $_.Name -like "*FSI*" }
$retentionPolicies | Format-List | Out-File "$evidencePath/RetentionPolicies.txt"

# Collect DLP policy evidence
$dlpPolicies = Get-DlpCompliancePolicy | Where-Object { $_.Name -like "*Copilot*" -or $_.Name -like "*FSI*" }
$dlpPolicies | Format-List | Out-File "$evidencePath/DLPPolicies.txt"

# Collect sensitivity label evidence
$labels = Get-Label | Where-Object { $_.Name -like "*AI*" -or $_.Name -like "*Copilot*" }
$labels | Format-List | Out-File "$evidencePath/SensitivityLabels.txt"

Write-Host "Evidence pack generated at: $evidencePath" -ForegroundColor Green
Get-ChildItem $evidencePath | Format-Table Name, Length -AutoSize
```

### Script 2: Control Attestation Status Report

```powershell
# Generate attestation status report for all Copilot governance controls
$controls = @(
    @{ID="3.1"; Name="Audit Logging"; Owner="IT Security"; LastAttested=""},
    @{ID="3.2"; Name="Data Retention"; Owner="Records Mgmt"; LastAttested=""},
    @{ID="3.3"; Name="eDiscovery"; Owner="Legal/Compliance"; LastAttested=""},
    @{ID="3.4"; Name="Comm Compliance"; Owner="Compliance"; LastAttested=""},
    @{ID="3.5"; Name="FINRA 2210"; Owner="Compliance"; LastAttested=""},
    @{ID="3.6"; Name="Supervision"; Owner="Compliance"; LastAttested=""},
    @{ID="3.7"; Name="Reg Reporting"; Owner="Compliance"; LastAttested=""},
    @{ID="3.8"; Name="Model Risk Mgmt"; Owner="Risk Mgmt"; LastAttested=""},
    @{ID="3.9"; Name="AI Disclosure"; Owner="Compliance"; LastAttested=""},
    @{ID="3.10"; Name="Reg S-P Privacy"; Owner="Privacy"; LastAttested=""},
    @{ID="3.11"; Name="Record Keeping"; Owner="Records Mgmt"; LastAttested=""},
    @{ID="3.12"; Name="Evidence Collection"; Owner="Audit"; LastAttested=""},
    @{ID="3.13"; Name="FFIEC Alignment"; Owner="Compliance"; LastAttested=""}
)

$attestationReport = $controls | ForEach-Object {
    [PSCustomObject]@{
        ControlID     = $_.ID
        ControlName   = $_.Name
        Owner         = $_.Owner
        LastAttested  = $_.LastAttested
        NextDue       = (Get-Date).AddMonths(3).ToString("yyyy-MM-dd")
        Status        = if ($_.LastAttested) { "Current" } else { "Pending" }
    }
}

$attestationReport | Format-Table -AutoSize
$attestationReport | Export-Csv "AttestationStatus_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Audit Log Evidence Extraction

```powershell
# Extract audit log evidence for a specific control and time period
param(
    [string]$ControlArea = "CopilotInteraction",
    [int]$DaysBack = 90
)

$startDate = (Get-Date).AddDays(-$DaysBack)
$endDate = Get-Date

$evidence = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType $ControlArea `
    -ResultSize 5000

$evidenceSummary = [PSCustomObject]@{
    ControlArea    = $ControlArea
    Period         = "$($startDate.ToString('yyyy-MM-dd')) to $($endDate.ToString('yyyy-MM-dd'))"
    TotalRecords   = $evidence.Count
    UniqueUsers    = ($evidence | Select-Object -Unique UserIds).Count
    ExportDate     = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
}

$evidenceSummary | Format-List
$evidence | Export-Csv "AuditEvidence_${ControlArea}_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Evidence Freshness Audit

```powershell
# Check evidence freshness to identify stale evidence requiring updates
$evidenceItems = @(
    @{Name="Audit Log Config"; MaxAgeDays=90; LastCollected="2026-01-15"},
    @{Name="Retention Policies"; MaxAgeDays=90; LastCollected="2026-01-15"},
    @{Name="DLP Policies"; MaxAgeDays=90; LastCollected="2026-01-15"},
    @{Name="Communication Compliance"; MaxAgeDays=90; LastCollected="2026-01-15"},
    @{Name="Supervisory Reviews"; MaxAgeDays=30; LastCollected="2026-02-01"}
)

$freshnessReport = $evidenceItems | ForEach-Object {
    $lastDate = [DateTime]$_.LastCollected
    $ageDays = ((Get-Date) - $lastDate).Days
    [PSCustomObject]@{
        EvidenceItem   = $_.Name
        LastCollected  = $_.LastCollected
        AgeDays        = $ageDays
        MaxAgeDays     = $_.MaxAgeDays
        Status         = if ($ageDays -le $_.MaxAgeDays) { "Current" } else { "STALE" }
    }
}

$freshnessReport | Format-Table -AutoSize
$staleItems = $freshnessReport | Where-Object { $_.Status -eq "STALE" }
if ($staleItems) { Write-Warning "$($staleItems.Count) evidence items require refresh" }
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Evidence pack generation | Quarterly | Script 1 |
| Attestation status report | Monthly | Script 2 |
| Audit log evidence extraction | Monthly | Script 3 |
| Evidence freshness audit | Weekly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate evidence completeness
- See [Troubleshooting](troubleshooting.md) for evidence collection issues
