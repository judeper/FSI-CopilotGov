# Control 3.11: Record Keeping and Books-and-Records Compliance — PowerShell Setup

Automation scripts for implementing and managing records management for Copilot-generated content, including Preservation Lock configuration for the audit-trail alternative path under SEC Rule 17a-4(f)(2)(ii)(A) and retention label deployment for regulatory records.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`
- **Permissions:** Records Management Administrator, Compliance Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
```

## Scripts

### Script 1: Create Regulatory Record Retention Labels

```powershell
# Create retention labels for books-and-records compliance
# These labels, when applied, mark items as regulatory records (immutable for SEC 17a-4 audit-trail alternative)
$labels = @(
    @{Name="SEC-17a4-Business-Communication-6yr"; Duration=2190; Description="SEC 17a-4 business communication records — 6 year retention"},
    @{Name="FINRA-4511-Client-Record-7yr"; Duration=2555; Description="FINRA 4511 client correspondence — 7 year retention"},
    @{Name="Investment-Recommendation-Record-7yr"; Duration=2555; Description="Investment recommendation records — 7 year retention"},
    @{Name="Marketing-Material-Record-3yr"; Duration=1095; Description="Marketing material records — 3 year retention"}
)

foreach ($label in $labels) {
    New-ComplianceTag `
        -Name $label.Name `
        -Comment $label.Description `
        -RetentionAction KeepAndDelete `
        -RetentionDuration $label.Duration `
        -RetentionType CreationAgeInDays `
        -IsRecordLabel $true `
        -Regulatory $true

    Write-Host "Created regulatory record label: $($label.Name)" -ForegroundColor Green
}
```

### Script 2: Publish Retention Labels to All Locations

```powershell
# Publish all regulatory record labels to relevant locations
$labelNames = @(
    "SEC-17a4-Business-Communication-6yr",
    "FINRA-4511-Client-Record-7yr",
    "Investment-Recommendation-Record-7yr",
    "Marketing-Material-Record-3yr"
)

New-RetentionCompliancePolicy `
    -Name "FSI-Regulatory-Record-Labels" `
    -RetentionComplianceTag $labelNames `
    -ExchangeLocation "All" `
    -SharePointLocation "All" `
    -OneDriveLocation "All" `
    -ModernGroupLocation "All" `
    -Enabled $true

Write-Host "Regulatory record labels published to all locations" -ForegroundColor Green
```

### Script 3: Enable Preservation Lock on Critical Policies

```powershell
# Enable Preservation Lock for SEC 17a-4(f) WORM compliance or audit-trail alternative (Rule 17a-4(f)(2)(ii)(A))
# Preservation Lock makes the retention policy irreversible — required for both compliance paths
#
# IMPORTANT: Preservation Lock is IRREVERSIBLE.
# After locking:
# - The retention period cannot be shortened
# - The policy cannot be disabled or deleted
# - Additional locations can be added, but existing settings cannot be reduced
# - Even Global Administrators cannot reverse this action
#
# Only apply after the policy has been fully validated and approved.
$policyName = "FSI-Regulatory-Record-Labels"

Write-Warning "Preservation Lock is IRREVERSIBLE. The policy cannot be shortened or disabled after locking."
Write-Warning "This lock is required for the SEC Rule 17a-4(f)(2)(ii)(A) audit-trail alternative compliance path."
Write-Host "Policy to lock: $policyName" -ForegroundColor Yellow
Write-Host ""
Write-Host "Prerequisites before locking:"
Write-Host "  1. Verify all label configurations are correct"
Write-Host "  2. Verify retention durations are accurate"
Write-Host "  3. Obtain written approval from Records Management lead and Legal"
Write-Host "  4. Document the lock in the compliance record"
Write-Host ""
$confirm = Read-Host "Type 'CONFIRM-LOCK' to enable Preservation Lock (this is irreversible)"

if ($confirm -eq "CONFIRM-LOCK") {
    Set-RetentionCompliancePolicy `
        -Identity $policyName `
        -RestrictiveRetention $true

    $lockDate = Get-Date -Format "yyyy-MM-dd HH:mm:ss UTC"
    Write-Host "Preservation Lock ENABLED on '$policyName' at $lockDate" -ForegroundColor Red
    Write-Host "Document this action: Policy '$policyName' locked on $lockDate" -ForegroundColor Yellow
    Write-Host "This lock supports the SEC Rule 17a-4(f)(2)(ii)(A) audit-trail alternative compliance path" -ForegroundColor Cyan
} else {
    Write-Host "Preservation Lock NOT enabled — operation cancelled" -ForegroundColor Yellow
}
```

### Script 4: Verify Preservation Lock Status

```powershell
# Verify Preservation Lock status on all FSI retention policies
# Run regularly to confirm WORM / audit-trail alternative posture
$policies = Get-RetentionCompliancePolicy | Where-Object { $_.Name -like "*FSI*" -or $_.Name -like "*Record*" -or $_.Name -like "*Regulatory*" }

$report = foreach ($policy in $policies) {
    $rules = Get-RetentionComplianceRule -Policy $policy.Name -ErrorAction SilentlyContinue
    [PSCustomObject]@{
        PolicyName           = $policy.Name
        Enabled              = $policy.Enabled
        RestrictiveRetention = $policy.RestrictiveRetention  # TRUE = Preservation Lock enabled
        RetentionDays        = $rules.RetentionDuration
        IsRegulatory         = $rules.Regulatory
        DistributionStatus   = $policy.DistributionStatus
        LockStatus           = if ($policy.RestrictiveRetention) { "LOCKED - Audit-Trail Alt. Active" } else { "Unlocked" }
    }
}

Write-Host "=== Retention Policy Preservation Lock Status ==="
$report | Format-Table PolicyName, LockStatus, Enabled, DistributionStatus -AutoSize
Write-Host ""
Write-Host "Policies with Preservation Lock (RestrictiveRetention = True) support the"
Write-Host "SEC Rule 17a-4(f)(2)(ii)(A) audit-trail alternative compliance path."

$report | Export-Csv "RetentionPolicy_LockStatus_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Lock status report exported" -ForegroundColor Green
```

### Script 5: Verify Audit Trail Coverage for Regulatory Records

```powershell
# Verify that the audit trail captures required events for the Rule 17a-4(f)(2)(ii)(A) audit-trail alternative
# The audit trail must log all modifications, deletions, and access events for regulatory records
param(
    [int]$DaysBack = 7
)

$startDate = (Get-Date).AddDays(-$DaysBack)
$endDate = Get-Date

Write-Host "Searching audit log for regulatory record events (last $DaysBack days)..." -ForegroundColor Cyan

# Check for record status changes (items declared as regulatory records)
$recordDeclarations = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "RecordStatusChanged" `
    -ResultSize 100

# Check for blocked deletion/modification attempts on regulatory records
$blockedAttempts = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "ComplianceRecordChanged", "FileSensitivityLabelChanged" `
    -ResultSize 100

Write-Host ""
Write-Host "=== Audit Trail Coverage Report ==="
Write-Host "Regulatory record declarations (last $DaysBack days): $($recordDeclarations.Count)"
Write-Host "Compliance record change events (last $DaysBack days): $($blockedAttempts.Count)"
Write-Host ""

if ($recordDeclarations.Count -gt 0) {
    Write-Host "Audit trail IS capturing regulatory record events." -ForegroundColor Green
    Write-Host "This supports the SEC Rule 17a-4(f)(2)(ii)(A) audit-trail alternative compliance path."
} else {
    Write-Host "WARNING: No regulatory record events found in last $DaysBack days." -ForegroundColor Yellow
    Write-Host "Verify that regulatory record labels are being applied to Copilot content."
    Write-Host "If labels are applied but not appearing in audit, check audit log policy retention settings."
}

# Export audit trail evidence
$auditEvidence = @(
    $recordDeclarations | Select-Object CreationDate, UserIds, Operations, AuditData
    $blockedAttempts | Select-Object CreationDate, UserIds, Operations, AuditData
)
$auditEvidence | Export-Csv "AuditTrailEvidence_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Audit trail evidence exported for compliance documentation" -ForegroundColor Green
```

### Script 6: Records Management Compliance Report

```powershell
# Generate a report of records management status across the tenant
$policies = Get-RetentionCompliancePolicy | Where-Object { $_.Name -like "*FSI*" -or $_.Name -like "*Record*" }

$report = foreach ($policy in $policies) {
    $rules = Get-RetentionComplianceRule -Policy $policy.Name
    [PSCustomObject]@{
        PolicyName           = $policy.Name
        Enabled              = $policy.Enabled
        RestrictiveRetention = $policy.RestrictiveRetention
        RetentionDays        = $rules.RetentionDuration
        IsRegulatory         = $rules.Regulatory
        DistributionStatus   = $policy.DistributionStatus
    }
}

Write-Host "Records Management Policy Report:"
$report | Format-Table -AutoSize
$report | Export-Csv "RecordsManagement_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Label deployment verification | Monthly | Script 6 |
| New label creation | As needed | Script 1 |
| Preservation Lock review | Monthly | Script 4 |
| Audit trail coverage check | Monthly | Script 5 |
| Policy compliance report | Quarterly | Script 6 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate records management
- See [Troubleshooting](troubleshooting.md) for records management issues
