# Control 3.9: AI Disclosure, Transparency, and SEC Marketing Rule — PowerShell Setup

Automation scripts for enforcing AI disclosure requirements and monitoring transparency compliance for Copilot-generated content.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`
- **Permissions:** Purview Compliance Admin, Information Protection Admin
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "AuditLog.Read.All"
```

## Scripts

### Script 1: Create AI-Assisted Content Sensitivity Label

```powershell
# Create a sensitivity label for AI-assisted content disclosure
# Requires Connect-IPPSSession (Security & Compliance PowerShell)

New-Label `
    -DisplayName "AI-Assisted Content" `
    -Name "AI-Assisted-Content" `
    -Tooltip "Content created with or substantially assisted by Microsoft 365 Copilot" `
    -Comment "Supports SEC Marketing Rule (Rule 206(4)-1) and AI transparency requirements" `
    -ApplyContentMarkingHeaderEnabled $true `
    -ApplyContentMarkingHeaderText "AI-Assisted Content — Review Required Before Distribution" `
    -ApplyContentMarkingFooterEnabled $true `
    -ApplyContentMarkingFooterText "This content was generated with AI assistance. Review per firm policy before external distribution."

# Publish label to all Exchange users
New-LabelPolicy `
    -Name "AI-Disclosure-Label-Policy" `
    -Labels "AI-Assisted-Content" `
    -ExchangeLocation All `
    -Comment "Publishes AI-Assisted Content label for disclosure compliance"

Write-Host "AI-Assisted Content label created and published" -ForegroundColor Green
Write-Host "Label propagation may take up to 24 hours across all workloads" -ForegroundColor Yellow
```

### Script 2: Create DLP Policy for AI Disclosure Enforcement

```powershell
# Create DLP policy detecting NPI in content shared externally from Copilot workloads
# Covers SharePoint, OneDrive, Exchange, and Teams locations
# Requires Connect-IPPSSession (Security & Compliance PowerShell)

New-DlpCompliancePolicy -Name "FSI-AIDisclosure-DLP" `
    -SharePointLocation All `
    -OneDriveLocation All `
    -ExchangeLocation All `
    -TeamsLocation All `
    -Mode Enable `
    -Comment "Detects NPI in AI-generated content shared externally — FSI regulatory requirement"

# Rule using built-in SITs with external-sharing scope
New-DlpComplianceRule -Name "FSI-AIDisclosure-ExternalShare-Rule" `
    -Policy "FSI-AIDisclosure-DLP" `
    -ContentContainsSensitiveInformation @(
        @{Name="U.S. Social Security Number (SSN)"; minCount=1},
        @{Name="ABA Routing Number"; minCount=1},
        @{Name="U.S. Bank Account Number"; minCount=1},
        @{Name="Credit Card Number"; minCount=1}
    ) `
    -AccessScope NotInOrganization `
    -BlockAccess $true `
    -BlockAccessScope All `
    -NotifyUser @("compliance@contoso.com") `
    -GenerateIncidentReport "SiteAdmin" `
    -IncidentReportContent @("Title","Severity","MachineTranslatedMessages","RulesMatched","Detections") `
    -NotifyEmailCustomText "AI-generated content containing NPI detected in external share. Reg S-P review required." `
    -Severity High `
    -Comment "Block external sharing of NPI from Copilot-generated content"

Write-Host "AI disclosure DLP policy created with real SIT detection" -ForegroundColor Green
```

### Script 3: Audit Copilot Interactions for Disclosure Review

```powershell
# Export Copilot interactions and DLP matches for AI disclosure compliance review
# Combines CopilotInteraction audit records with DLP incident data
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

# Copilot interaction audit records
$copilotEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

# DLP incidents from Unified Audit Log
$dlpEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType DlpAll `
    -ResultSize 5000

# Parse DLP events and filter to AI disclosure policy matches
$dlpMatches = $dlpEvents | ForEach-Object {
    $data = $_.AuditData | ConvertFrom-Json
    [PSCustomObject]@{
        Date       = $_.CreationDate
        User       = $_.UserIds
        PolicyName = $data.PolicyDetails.PolicyName
        RuleMatch  = $data.PolicyDetails.Rules.RuleName
        Action     = $data.Actions
    }
} | Where-Object { $_.PolicyName -match "AIDisclosure|FSI" }

$report = [PSCustomObject]@{
    Period                 = "$($startDate.ToString('yyyy-MM-dd')) to $($endDate.ToString('yyyy-MM-dd'))"
    TotalCopilotEvents     = $copilotEvents.Count
    UniqueCopilotUsers     = ($copilotEvents | Select-Object -ExpandProperty UserIds -Unique).Count
    DLPBlocksForDisclosure = $dlpMatches.Count
}

$report | Format-List
$dlpMatches | Export-Csv "AIDisclosureDLP_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Disclosure compliance report exported" -ForegroundColor Green
```

### Script 4: SEC Marketing Rule Compliance Report

```powershell
# Report on communication compliance policy matches for SEC Marketing Rule review
# Queries supervision events from Unified Audit Log with structured parsing
$startDate = (Get-Date).AddDays(-90)
$endDate = Get-Date

# Supervision policy match and review action events
$supervisionEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "SupervisionPolicyMatch","SupervisionReviewAction" `
    -ResultSize 5000

# Parse structured audit data for each event
$parsed = $supervisionEvents | ForEach-Object {
    $data = $_.AuditData | ConvertFrom-Json
    [PSCustomObject]@{
        Date        = $_.CreationDate
        User        = $_.UserIds
        Operation   = $_.Operations
        PolicyName  = $data.PolicyMatchInfo.PolicyName
        RuleMatched = $data.PolicyMatchInfo.RuleName
        ItemClass   = $data.PolicyMatchInfo.ItemClass
    }
}

Write-Host "SEC Marketing Rule Compliance Report (Last 90 Days):" -ForegroundColor Cyan
Write-Host "  Supervision policy matches: $($parsed.Count)"
Write-Host "  Unique users flagged: $(($parsed | Select-Object -ExpandProperty User -Unique).Count)"

$parsed | Export-Csv "SECMarketingRule_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Report exported to SECMarketingRule_$(Get-Date -Format 'yyyyMMdd').csv" -ForegroundColor Green
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| AI disclosure compliance audit | Monthly | Script 3 |
| SEC Marketing Rule report | Quarterly | Script 4 |
| Label policy review | Quarterly | Script 1 (verify) |

## Limitations

- No native M365 sensitive information type (SIT) exists for "AI-generated content" as a class — disclosure enforcement relies on SIT matches combined with sensitivity label conditions or trainable classifiers
- Sensitivity label auto-application for AI-generated content requires E5 or E5 Compliance license
- `New-Label` and `New-LabelPolicy` changes can take up to 24 hours to propagate to all workloads
- Communication compliance review workflows (approve, escalate, resolve) are portal-only — PowerShell retrieves policy match events but not reviewer actions taken in the Purview portal
- SEC Marketing Rule (Rule 206(4)-1) interpretation varies by firm — organizations should verify that DLP and label configurations meet their specific compliance obligations

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate disclosure controls
- See [Troubleshooting](troubleshooting.md) for disclosure enforcement issues
