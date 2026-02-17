# Control 3.13: FFIEC IT Examination Handbook Alignment — PowerShell Setup

Automation scripts for generating FFIEC-aligned evidence, assessment reports, and examination preparation data.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`
- **Permissions:** Compliance Administrator, AuditLog.Read.All
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "AuditLog.Read.All", "Policy.Read.All", "Directory.Read.All"
```

## Scripts

### Script 1: FFIEC Audit Booklet Evidence Collection

```powershell
# Collect evidence aligned with FFIEC Audit Booklet requirements
$evidenceDate = Get-Date -Format "yyyyMMdd"
$outputPath = "FFIEC_Audit_Evidence_$evidenceDate"
New-Item -ItemType Directory -Path $outputPath -Force | Out-Null

# Audit log configuration
$auditConfig = Get-AdminAuditLogConfig
$auditConfig | Format-List | Out-File "$outputPath/AuditLogConfiguration.txt"

# Audit retention policies
$retentionPolicies = Get-UnifiedAuditLogRetentionPolicy
$retentionPolicies | Format-List | Out-File "$outputPath/AuditRetentionPolicies.txt"

# Administrative changes in the last 90 days
$adminChanges = Search-UnifiedAuditLog `
    -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) `
    -RecordType AzureActiveDirectory `
    -Operations "Update policy", "Set-AdminAuditLogConfig" `
    -ResultSize 5000

$adminChanges | Export-Csv "$outputPath/AdminChanges_90Days.csv" -NoTypeInformation

Write-Host "FFIEC Audit booklet evidence collected at: $outputPath" -ForegroundColor Green
```

### Script 2: FFIEC Information Security Booklet Compliance Check

```powershell
# Verify security controls aligned with FFIEC Information Security booklet
$securityChecks = @()

# Check DLP policies
$dlpPolicies = Get-DlpCompliancePolicy
$securityChecks += [PSCustomObject]@{
    Category = "Data Protection"
    Control  = "DLP Policies"
    Status   = if ($dlpPolicies.Count -gt 0) { "Implemented ($($dlpPolicies.Count) policies)" } else { "NOT CONFIGURED" }
}

# Check retention policies
$retentionPolicies = Get-RetentionCompliancePolicy
$securityChecks += [PSCustomObject]@{
    Category = "Data Retention"
    Control  = "Retention Policies"
    Status   = if ($retentionPolicies.Count -gt 0) { "Implemented ($($retentionPolicies.Count) policies)" } else { "NOT CONFIGURED" }
}

# Check sensitivity labels
$labels = Get-Label
$securityChecks += [PSCustomObject]@{
    Category = "Classification"
    Control  = "Sensitivity Labels"
    Status   = if ($labels.Count -gt 0) { "Implemented ($($labels.Count) labels)" } else { "NOT CONFIGURED" }
}

Write-Host "`nFFIEC Information Security Compliance Check:" -ForegroundColor Cyan
$securityChecks | Format-Table -AutoSize
$securityChecks | Export-Csv "FFIEC_SecurityCheck_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: FFIEC Management Booklet — Governance Documentation

```powershell
# Generate governance documentation aligned with FFIEC Management booklet
$governanceReport = @"
# FFIEC Management Booklet — Copilot AI Governance Report
## Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss UTC")

### IT Governance Structure
- **AI Governance Committee:** [Document committee membership and charter]
- **Copilot Policy Owner:** Compliance Administrator
- **Risk Assessment Owner:** Model Risk Management
- **Operational Owner:** IT Operations

### Risk Management
- **Risk Assessment Methodology:** OCC 2011-12 aligned model risk framework
- **Risk Rating:** Medium — supervised AI assistant with governance controls
- **Last Assessment Date:** $(Get-Date -Format "yyyy-MM-dd")
- **Next Assessment Due:** $((Get-Date).AddMonths(6).ToString("yyyy-MM-dd"))

### Control Framework
- Pillar 1: Readiness and Assessment (13 controls) — IMPLEMENTED
- Pillar 2: Security and Protection (15 controls) — IMPLEMENTED
- Pillar 3: Compliance and Audit (13 controls) — IMPLEMENTED
- Pillar 4: Operations and Monitoring (13 controls) — IMPLEMENTED
"@

$governanceReport | Out-File "FFIEC_GovernanceReport_$(Get-Date -Format 'yyyyMMdd').md" -Encoding UTF8
Write-Host "FFIEC governance report generated" -ForegroundColor Green
```

### Script 4: Examination Readiness Scorecard

```powershell
# Generate FFIEC examination readiness scorecard
$booklets = @(
    @{Booklet="Audit"; Controls="3.1, 3.12"; EvidenceStatus="Current"; ReadinessLevel="Examination Ready"},
    @{Booklet="Information Security"; Controls="2.1-2.15"; EvidenceStatus="Current"; ReadinessLevel="Examination Ready"},
    @{Booklet="Management"; Controls="3.6, 3.8"; EvidenceStatus="Current"; ReadinessLevel="Examination Ready"},
    @{Booklet="Operations"; Controls="4.1-4.13"; EvidenceStatus="Current"; ReadinessLevel="Examination Ready"},
    @{Booklet="Development/Acquisition"; Controls="1.13"; EvidenceStatus="Current"; ReadinessLevel="Examination Ready"}
)

$scorecard = $booklets | ForEach-Object {
    [PSCustomObject]@{
        FFIECBooklet   = $_.Booklet
        MappedControls = $_.Controls
        EvidenceStatus = $_.EvidenceStatus
        ReadinessLevel = $_.ReadinessLevel
        LastReviewed   = (Get-Date -Format "yyyy-MM-dd")
    }
}

Write-Host "FFIEC Examination Readiness Scorecard:"
$scorecard | Format-Table -AutoSize
$scorecard | Export-Csv "FFIEC_ReadinessScorecard_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Audit booklet evidence collection | Quarterly | Script 1 |
| Security compliance check | Monthly | Script 2 |
| Governance documentation update | Semi-annually | Script 3 |
| Readiness scorecard | Monthly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate FFIEC alignment
- See [Troubleshooting](troubleshooting.md) for examination preparation issues
