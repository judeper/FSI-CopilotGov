# Control 3.9: AI Disclosure, Transparency, and SEC Marketing Rule — PowerShell Setup

Automation scripts for enforcing AI disclosure requirements and monitoring transparency compliance for Copilot-generated content.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`
- **Permissions:** Compliance Administrator, Information Protection Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "AuditLog.Read.All", "InformationProtectionPolicy.Read"
```

## Scripts

### Script 1: Create AI-Assisted Content Sensitivity Label

```powershell
# Create a sensitivity label for AI-assisted content disclosure
New-Label `
    -DisplayName "AI-Assisted Content" `
    -Name "AI-Assisted-Content" `
    -Tooltip "Content drafted with or substantially assisted by Microsoft 365 Copilot" `
    -Comment "SEC Marketing Rule and AI transparency compliance label" `
    -ApplyContentMarkingHeaderEnabled $true `
    -ApplyContentMarkingHeaderText "AI-Assisted Content — Review Before Distribution" `
    -ApplyContentMarkingFooterEnabled $true `
    -ApplyContentMarkingFooterText "This content was generated with AI assistance and requires human review per firm policy."

# Publish the label
New-LabelPolicy `
    -Name "AI-Disclosure-Label-Policy" `
    -Labels "AI-Assisted-Content" `
    -ExchangeLocation "All" `
    -Comment "Publishes AI-Assisted Content label to all users"

Write-Host "AI-Assisted Content label created and published" -ForegroundColor Green
```

### Script 2: Create DLP Policy for AI Disclosure Enforcement

```powershell
# Create DLP policy requiring AI disclosure on external communications
New-DlpCompliancePolicy `
    -Name "FSI-AI-Disclosure-Enforcement" `
    -Comment "Requires AI disclosure on Copilot-assisted external communications" `
    -ExchangeLocation "All" `
    -SharePointLocation "All" `
    -Mode Enable

New-DlpComplianceRule `
    -Name "Block-Undisclosed-AI-Content-External" `
    -Policy "FSI-AI-Disclosure-Enforcement" `
    -ContentContainsSensitiveInformation @{Name="AI-Assisted-Content-Pattern"} `
    -ExceptIfContentContainsWords @("AI assistance", "AI-assisted", "generated with AI") `
    -BlockAccess $true `
    -BlockAccessScope SpecificExternalUsers `
    -NotifyUser Owner `
    -NotifyUserType Sender

Write-Host "AI disclosure DLP policy created" -ForegroundColor Green
```

### Script 3: Audit AI Disclosure Compliance

```powershell
# Report on AI disclosure compliance for outbound Copilot-assisted communications
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$copilotEmails = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

$dlpMatches = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType DLP `
    -ResultSize 5000

$report = [PSCustomObject]@{
    Period                      = "Last 30 Days"
    TotalCopilotInteractions    = $copilotEmails.Count
    DLPBlocksForMissingDisclosure = ($dlpMatches | Where-Object { $_.AuditData -like "*AI-Disclosure*" }).Count
    ComplianceRate              = "Calculated after DLP analysis"
}

$report | Format-List
$report | Export-Csv "AIDisclosureCompliance_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Generate SEC Marketing Rule Compliance Report

```powershell
# Report for SEC Marketing Rule compliance on AI-generated marketing content
$startDate = (Get-Date).AddDays(-90)
$endDate = Get-Date

$marketingReviews = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "SupervisionPolicyMatch" `
    -ResultSize 5000

$secMatches = $marketingReviews | Where-Object {
    $_.AuditData -like "*MarketingRule*" -or $_.AuditData -like "*AI-Disclosure*"
}

Write-Host "SEC Marketing Rule Compliance Report (Last 90 Days):"
Write-Host "Total marketing content reviews: $($secMatches.Count)"

$secMatches | Select-Object CreationDate, UserIds, Operations |
    Export-Csv "SECMarketingRule_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| AI disclosure compliance audit | Monthly | Script 3 |
| SEC Marketing Rule report | Quarterly | Script 4 |
| Label policy review | Quarterly | Script 1 (verify) |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate disclosure controls
- See [Troubleshooting](troubleshooting.md) for disclosure enforcement issues
