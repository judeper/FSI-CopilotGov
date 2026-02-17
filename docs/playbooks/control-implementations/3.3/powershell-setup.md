# Control 3.3: eDiscovery for Copilot-Generated Content — PowerShell Setup

Automation scripts for managing eDiscovery cases, searches, and holds that include Copilot-generated content.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement` (Security & Compliance PowerShell)
- **Permissions:** eDiscovery Manager or eDiscovery Administrator role
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
# Search for Copilot interactions across specified custodians
$searchName = "Copilot-Interactions-Search-$(Get-Date -Format 'yyyyMMdd')"
$custodians = @("user1@contoso.com", "user2@contoso.com")
$startDate = (Get-Date).AddMonths(-6).ToString("MM/dd/yyyy")
$endDate = (Get-Date).ToString("MM/dd/yyyy")

New-ComplianceSearch `
    -Name $searchName `
    -ExchangeLocation $custodians `
    -SharePointLocation "https://contoso.sharepoint.com/sites/finance" `
    -ContentMatchQuery "kind:microsoftcopilot AND date>=$startDate AND date<=$endDate" `
    -Description "Search for Copilot interactions in FSI custodian mailboxes"

# Start the search
Start-ComplianceSearch -Identity $searchName
Write-Host "Compliance search started: $searchName" -ForegroundColor Green
```

### Script 3: Place Custodians on Hold for Copilot Content

```powershell
# Create a hold policy to preserve Copilot content for specified custodians
$holdName = "FSI-Copilot-Content-Hold"
$custodians = @("user1@contoso.com", "user2@contoso.com")

New-CaseHoldPolicy `
    -Name $holdName `
    -Case "FSI-Copilot-Discovery-Template" `
    -ExchangeLocation $custodians `
    -SharePointLocation "All" `
    -Comment "Preservation hold for Copilot-generated content"

New-CaseHoldRule `
    -Name "$holdName-Rule" `
    -Policy $holdName `
    -ContentMatchQuery "kind:microsoftcopilot"

Write-Host "Custodian hold created for Copilot content" -ForegroundColor Green
```

### Script 4: Export Search Results Report

```powershell
# Check search status and export results summary
$searchName = "Copilot-Interactions-Search-$(Get-Date -Format 'yyyyMMdd')"

$searchStatus = Get-ComplianceSearch -Identity $searchName
Write-Host "Search Status: $($searchStatus.Status)"
Write-Host "Items Found: $($searchStatus.Items)"
Write-Host "Size (MB): $([math]::Round($searchStatus.Size / 1MB, 2))"

if ($searchStatus.Status -eq "Completed") {
    # Generate export action
    New-ComplianceSearchAction -SearchName $searchName -Export -Format FxStream
    Write-Host "Export initiated for search: $searchName" -ForegroundColor Green
}
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Review active cases | Weekly | Manual review |
| Hold status verification | Monthly | Script 3 (verify) |
| Search readiness test | Quarterly | Script 2 (test query) |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate eDiscovery operations
- See [Troubleshooting](troubleshooting.md) for common eDiscovery issues
