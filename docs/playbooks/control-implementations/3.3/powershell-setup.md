# Control 3.3: eDiscovery for Copilot-Generated Content — PowerShell Setup

Automation scripts for managing eDiscovery cases, searches, and holds that include Copilot-generated content. Case-management, search, and hold cmdlets remain useful for automation, but Copilot data source selection and cloud export steps should be completed in the Microsoft Purview portal or a validated eDiscovery API workflow.

> **Deprecation Notice:** Microsoft documents `New-ComplianceSearchAction -Export` examples and export parameters as functional only in on-premises Exchange after the May 2025 eDiscovery changes. Do not use `New-ComplianceSearchAction -Export` for cloud tenants; route exports through the Purview portal export/download experience, Microsoft Graph eDiscovery APIs, or another Microsoft-documented workflow validated for the tenant.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement` (Security & Compliance PowerShell)
- **Permissions:** eDiscovery Manager or eDiscovery Administrator role; Search And Purge is required only for approved AI-data deletion workflows
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
```

## Scripts

### Script 1: Create eDiscovery Case for Copilot Content

```powershell
# Create an eDiscovery (Premium) case for Copilot-related investigations
# Cases created via PowerShell are accessible from Microsoft Purview > eDiscovery > Cases
$caseName = "FSI-Copilot-Discovery-$(Get-Date -Format 'yyyyMMdd')"

New-ComplianceCase `
    -Name $caseName `
    -Description "eDiscovery case for Copilot interaction and content searches" `
    -CaseType AdvancedEdiscovery

# Add case members
Add-ComplianceCaseMember -Case $caseName -Member "compliance-team@contoso.com"
Write-Host "eDiscovery case created: $caseName" -ForegroundColor Green
```

### Script 2: Create Compliance Search for Copilot Interactions

```powershell
# Search for Microsoft 365 Copilot interactions across specified custodians.
# For the broadest portal search, use Item class > Copilot activity in the condition builder.
# Use itemclass KQL only after validating it in the tenant's current Purview experience.
$searchName = "Copilot-Interactions-Search-$(Get-Date -Format 'yyyyMMdd')"
$custodians = @("user1@contoso.com", "user2@contoso.com")
$startDate = (Get-Date).AddMonths(-6).ToString("MM/dd/yyyy")
$endDate = (Get-Date).ToString("MM/dd/yyyy")
$copilotQuery = "itemclass:IPM.SkypeTeams.Message.Copilot.* AND date>=$startDate AND date<=$endDate"

New-ComplianceSearch `
    -Name $searchName `
    -ExchangeLocation $custodians `
    -SharePointLocation "https://contoso.sharepoint.com/sites/finance" `
    -ContentMatchQuery $copilotQuery `
    -Description "Search for Microsoft 365 Copilot interactions in FSI custodian mailboxes"

Start-ComplianceSearch -Identity $searchName
Write-Host "Compliance search started: $searchName" -ForegroundColor Green
Write-Host "Portal follow-up: add Sources > Microsoft 365 Copilot interactions for case review and hold workflows." -ForegroundColor Yellow
```

### Script 3: Place Custodians on Hold for Copilot Content

```powershell
# Create a hold policy to preserve Copilot mailbox content for specified custodians.
# In the Purview portal, also add Sources > Microsoft 365 Copilot interactions to the case.
$holdName = "FSI-Copilot-Content-Hold"
$custodians = @("user1@contoso.com", "user2@contoso.com")
$copilotHoldQuery = "(itemclass:IPM.SkypeTeams.Message.Copilot.* OR itemclass:IPM.Contact)"

New-CaseHoldPolicy `
    -Name $holdName `
    -Case "FSI-Copilot-Discovery-Template" `
    -ExchangeLocation $custodians `
    -SharePointLocation "All" `
    -Comment "Preservation hold for Copilot interaction and memory content"

New-CaseHoldRule `
    -Name "$holdName-Rule" `
    -Policy $holdName `
    -ContentMatchQuery $copilotHoldQuery

Write-Host "Custodian mailbox hold created for Copilot content" -ForegroundColor Green
Write-Host "Portal follow-up: confirm Microsoft 365 Copilot interactions data source is on hold in the case." -ForegroundColor Yellow
```

### Script 4: Verify Cases Include the Copilot Interactions Data Source

```powershell
# List open cases that should be checked in the Purview portal for Copilot data source coverage.
# Manual portal check: eDiscovery > [case] > Sources > Microsoft 365 Copilot interactions.
$allCases = Get-ComplianceCase | Where-Object { $_.Status -ne "Closed" }

foreach ($case in $allCases) {
    Write-Host "Case: $($case.Name) | Created: $($case.CreatedDateTime) | Type: $($case.CaseType)"
    Write-Host "  --> Verify Sources include custodian Exchange mailboxes and Microsoft 365 Copilot interactions." -ForegroundColor Yellow
}
```

### Script 5: Review Search Status and Route Export

```powershell
# Check search status and provide cloud-safe export guidance.
# Do not run New-ComplianceSearchAction -Export for Microsoft 365 cloud tenants.
$searchName = "Copilot-Interactions-Search-$(Get-Date -Format 'yyyyMMdd')"

$searchStatus = Get-ComplianceSearch -Identity $searchName
Write-Host "Search Status: $($searchStatus.Status)"
Write-Host "Items Found: $($searchStatus.Items)"
Write-Host "Size (MB): $([math]::Round($searchStatus.Size / 1MB, 2))"

if ($searchStatus.Status -eq "Completed") {
    Write-Host "Search completed. Use a supported export workflow:" -ForegroundColor Green
    Write-Host "1. Purview portal > eDiscovery > Cases > open the case > Searches or Review sets."
    Write-Host "2. Add results to a review set when using eDiscovery (Premium)."
    Write-Host "3. Export from the portal or a validated eDiscovery API workflow."
    Write-Host "4. Validate requester format: PST, native files, redacted PDF, JSON, or another agreed format."
    Write-Host "5. Preserve export manifest, hashes, and handler identification for chain of custody."
}
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Review active cases | Weekly | Manual review + Script 4 for Copilot data source check |
| Hold status verification | Monthly | Script 3 plus portal verification of Microsoft 365 Copilot interactions hold |
| Search readiness test | Quarterly | Script 2 plus Item class > Copilot activity validation in the portal |
| Export workflow test | Quarterly | Script 5 plus portal/API export runbook validation |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate eDiscovery operations
- See [Troubleshooting](troubleshooting.md) for common eDiscovery issues
- Back to [Control 3.3](../../../controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md)
