# Control 3.5: FINRA Rule 2210 Compliance for Copilot-Drafted Communications — PowerShell Setup

Automation scripts for monitoring, reporting, and managing FINRA 2210 compliance for Copilot-assisted communications.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`
- **Permissions:** Compliance Administrator or Communication Compliance Admin
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "Mail.Read", "AuditLog.Read.All"
```

## Scripts

### Script 1: Create Custom Sensitive Information Type for Prohibited Language

```powershell
# Create a custom SIT for FINRA 2210 prohibited language patterns
$prohibitedPatterns = @(
    "guaranteed return", "risk-free", "assured performance",
    "no possibility of loss", "certain to increase", "will achieve",
    "cannot lose", "safe investment", "sure thing",
    "always profitable", "zero risk", "assured outcome"
)

$xmlContent = @"
<?xml version="1.0" encoding="utf-8"?>
<RulePackage xmlns="http://schemas.microsoft.com/office/2011/mce">
  <RulePack id="$(New-Guid)">
    <Version major="1" minor="0" build="0" revision="0"/>
    <Publisher id="$(New-Guid)"/>
  </RulePack>
  <Rules>
    <Entity id="$(New-Guid)" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
        <Any minMatches="1">
$(foreach ($pattern in $prohibitedPatterns) { "          <Match idRef=`"keyword_$($pattern.Replace(' ','_'))`" />`n" })
        </Any>
      </Pattern>
    </Entity>
  </Rules>
</RulePackage>
"@

$xmlContent | Out-File "FINRA2210_ProhibitedLanguage.xml" -Encoding UTF8
New-DlpSensitiveInformationTypeRulePackage -FileData ([System.IO.File]::ReadAllBytes("FINRA2210_ProhibitedLanguage.xml"))
Write-Host "FINRA 2210 prohibited language SIT created" -ForegroundColor Green
```

### Script 2: Report on FINRA 2210 Policy Matches

```powershell
# Generate a report of FINRA 2210 policy matches from the audit log
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$matches = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "SupervisionPolicyMatch" `
    -ResultSize 5000

$finraMatches = $matches | Where-Object {
    ($_ | ConvertFrom-Json).PolicyName -like "*FINRA*2210*"
}

$report = $finraMatches | ForEach-Object {
    $data = $_.AuditData | ConvertFrom-Json
    [PSCustomObject]@{
        Date       = $_.CreationDate
        User       = $_.UserIds
        PolicyName = $data.PolicyName
        Action     = $data.ActionType
        Channel    = $data.CommunicationChannel
    }
}

$report | Export-Csv "FINRA2210_Matches_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "FINRA 2210 report exported: $($report.Count) matches" -ForegroundColor Green
```

### Script 3: Identify Copilot Users Without FINRA 2210 Policy Coverage

```powershell
# Find Copilot-licensed users who are not in the FINRA 2210 supervision scope
$copilotUsers = Get-MgUser -Filter "assignedLicenses/any(x:x/skuId eq 'copilot-sku-id')" -All |
    Select-Object UserPrincipalName, DisplayName

# Compare against supervised user group
$supervisedGroup = Get-MgGroupMember -GroupId "supervision-group-id" -All |
    Select-Object -ExpandProperty AdditionalProperties

$unsupervised = $copilotUsers | Where-Object {
    $_.UserPrincipalName -notin $supervisedGroup.userPrincipalName
}

Write-Host "Copilot users NOT covered by FINRA 2210 policy:"
$unsupervised | Format-Table DisplayName, UserPrincipalName -AutoSize
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| FINRA 2210 match report | Weekly | Script 2 |
| Coverage gap analysis | Monthly | Script 3 |
| Prohibited language SIT review | Quarterly | Script 1 (update) |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate FINRA 2210 detection
- See [Troubleshooting](troubleshooting.md) for policy tuning guidance
