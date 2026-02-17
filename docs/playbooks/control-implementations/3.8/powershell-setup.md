# Control 3.8: Model Risk Management Alignment (OCC 2011-12 / SR 11-7) — PowerShell Setup

Automation scripts for monitoring Copilot model performance, generating model risk documentation, and tracking compliance with OCC/SR model risk management requirements.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`
- **Permissions:** Compliance Administrator, AuditLog.Read.All
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "AuditLog.Read.All", "Reports.Read.All"
```

## Scripts

### Script 1: Copilot User Feedback and Quality Metrics

```powershell
# Extract Copilot feedback signals for model performance monitoring
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$feedbackEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -Operations "CopilotFeedback" `
    -ResultSize 5000

$positive = ($feedbackEvents | Where-Object { $_.AuditData -like "*positive*" }).Count
$negative = ($feedbackEvents | Where-Object { $_.AuditData -like "*negative*" }).Count
$total = $feedbackEvents.Count

$metrics = [PSCustomObject]@{
    Period           = "Last 30 Days"
    TotalFeedback    = $total
    PositiveFeedback = $positive
    NegativeFeedback = $negative
    SatisfactionRate = if ($total -gt 0) { [math]::Round(($positive / $total) * 100, 1) } else { "N/A" }
}

$metrics | Format-List
$metrics | Export-Csv "CopilotModelMetrics_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Model performance metrics exported" -ForegroundColor Green
```

### Script 2: Copilot Usage Pattern Analysis

```powershell
# Analyze Copilot usage patterns for model risk monitoring
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$interactions = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

$patternAnalysis = $interactions | ForEach-Object {
    $data = $_.AuditData | ConvertFrom-Json
    [PSCustomObject]@{
        Date        = $_.CreationDate
        User        = $_.UserIds
        Application = $data.AppName
        Operation   = $_.Operations
    }
}

# Usage by application
$byApp = $patternAnalysis | Group-Object Application |
    Select-Object @{N='Application'; E={$_.Name}}, @{N='Count'; E={$_.Count}} |
    Sort-Object Count -Descending

Write-Host "Copilot Usage by Application (Last 30 Days):"
$byApp | Format-Table -AutoSize
$byApp | Export-Csv "CopilotUsageByApp_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Model Risk Assessment Documentation Generator

```powershell
# Generate model risk assessment documentation for OCC 2011-12
$assessmentDate = Get-Date -Format "yyyy-MM-dd"

$assessment = @"
# Model Risk Assessment — Microsoft 365 Copilot
## Assessment Date: $assessmentDate

### Model Information
- **Model Name:** Microsoft 365 Copilot (GPT-4 based)
- **Vendor:** Microsoft Corporation
- **Deployment:** Cloud-hosted SaaS (Microsoft Azure)
- **Risk Tier:** Tier 2 — Significant (AI-generated content used in business operations)

### Use Cases in Production
1. Document drafting and editing assistance
2. Email composition and response suggestions
3. Meeting summarization and action item extraction
4. Data analysis and presentation generation

### Controls Assessment
- Audit logging: IMPLEMENTED (Control 3.1)
- Data retention: IMPLEMENTED (Control 3.2)
- Communication compliance: IMPLEMENTED (Control 3.4)
- Supervisory oversight: IMPLEMENTED (Control 3.6)

### Risk Factors
- Output accuracy dependent on input data quality
- Potential for hallucinated or inaccurate content
- User reliance on AI-generated recommendations without verification

### Mitigations
- Human-in-the-loop review for all client-facing outputs
- Supervisory review for investment recommendations
- Regular performance monitoring via feedback metrics
"@

$assessment | Out-File "ModelRiskAssessment_Copilot_$assessmentDate.md" -Encoding UTF8
Write-Host "Model risk assessment generated" -ForegroundColor Green
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Model performance metrics | Monthly | Script 1 |
| Usage pattern analysis | Monthly | Script 2 |
| Model risk assessment update | Quarterly | Script 3 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate model risk controls
- See [Troubleshooting](troubleshooting.md) for monitoring issues
