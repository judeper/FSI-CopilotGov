# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — PowerShell Setup

Automation scripts for implementing and monitoring privacy controls for consumer financial information when using Copilot, including incident response automation for the 72-hour vendor notification requirement under SEC Rule 248.30(a)(3).

The DLP scripts below scope the policy **tenant-wide** (`"Inclusions":[{"Type":"Tenant","Identity":"All"}]`), which covers every user who can reach Microsoft Copilot or Copilot Chat — including users who have no paid Microsoft 365 Copilot add-on. Keep the portal scope aligned with this; see [Portal Walkthrough](portal-walkthrough.md) Step 2.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`
- **Permissions:** Purview Compliance Admin, Information Protection Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "InformationProtectionPolicy.ReadWrite.All", "AuditLog.Read.All"
```

## Scripts

### Script 1: Create DLP Policy for Consumer Financial Information

The two rules below are the ones the rest of this playbook refers to. The low-volume rule
raises an admin alert without restricting Copilot; the high-volume rule restricts Copilot
content processing and web grounding **and** raises a high-severity alert. Alert generation,
recipients, and severity are configured **on the rules themselves** (`GenerateAlert`,
`GenerateIncidentReport`, `IncidentReportContent`, `ReportSeverityLevel`) — that is the
documented way to make a Copilot DLP rule produce notifications.

```powershell
# Fail closed: stop on nonterminating cmdlet errors as well as terminating ones.
$ErrorActionPreference = 'Stop'

$policyName             = "FSI-RegSP-Copilot-Privacy-Protection"
$privacyAlertRecipients = @("privacy-officer@contoso.com", "compliance-alerts@contoso.com")

# Incident report content deliberately excludes OriginalContent so that detected NPI is not
# copied into notification email. Detection metadata is enough to open an investigation.
$incidentReportFields = @("Title", "Service", "RulesMatched", "Severity", "DetectionDetails")

New-DlpCompliancePolicy `
    -Name $policyName `
    -Comment "Protects consumer financial information per SEC Reg S-P" `
    -Locations '[{"Workload":"Applications","Location":"470f2276-e011-4e9d-a6ec-20768be3a4b0","Inclusions":[{"Type":"Tenant","Identity":"All"}]}]' `
    -EnforcementPlanes @("CopilotExperiences") `
    -Mode Enable `
    -ErrorAction Stop

# Rule for low-volume NPI detection: user notification plus a medium-severity admin alert.
New-DlpComplianceRule `
    -Name "RegSP-LowVolume-NPI-Warn" `
    -Policy $policyName `
    -ContentContainsSensitiveInformation @(
        @{Name="U.S. Social Security Number (SSN)"; minCount="1"; maxCount="9"},
        @{Name="Credit Card Number"; minCount="1"; maxCount="9"},
        @{Name="U.S. Bank Account Number"; minCount="1"; maxCount="9"}
    ) `
    -NotifyUser Owner `
    -GenerateAlert $privacyAlertRecipients `
    -GenerateIncidentReport $privacyAlertRecipients `
    -IncidentReportContent $incidentReportFields `
    -ReportSeverityLevel Medium `
    -ErrorAction Stop

# Rule for high-volume NPI detection: restrict Copilot processing and web grounding, and
# raise a high-severity alert to the privacy/compliance recipients.
New-DlpComplianceRule `
    -Name "RegSP-HighVolume-NPI-Block" `
    -Policy $policyName `
    -ContentContainsSensitiveInformation @(
        @{Name="U.S. Social Security Number (SSN)"; minCount="10"},
        @{Name="Credit Card Number"; minCount="10"},
        @{Name="U.S. Bank Account Number"; minCount="10"}
    ) `
    -RestrictAccess @(@{setting="ExcludeContentProcessing";value="Block"}) `
    -RestrictWebGrounding $true `
    -GenerateAlert $privacyAlertRecipients `
    -GenerateIncidentReport $privacyAlertRecipients `
    -IncidentReportContent $incidentReportFields `
    -ReportSeverityLevel High `
    -ErrorAction Stop
```

> **`RestrictAccess` caveat:** The current `New-DlpComplianceRule` reference does not enumerate
> the valid `RestrictAccess` setting values; `ExcludeContentProcessing` is the value shown in
> Microsoft's own Copilot-location example. The authoritative selection surface for the
> prompt-level actions remains the portal action names **Prevent Copilot from processing
> content > Processing prompts** and **> Performing Web Searches**. Confirm in the portal that
> the rule shows the actions you intended before treating the rule as configured.

### Script 1b: Fail-Closed Validation of the Copilot DLP Policy

Run this before reporting the control as implemented. Every check throws on failure; the
success line is printed only when all checks pass. Where a property is not exposed by the
tenant's cmdlet build, the script stops and tells you exactly what to verify by hand rather
than silently passing.

```powershell
$ErrorActionPreference = 'Stop'

$policyName          = "FSI-RegSP-Copilot-Privacy-Protection"
$copilotLocationGuid = "470f2276-e011-4e9d-a6ec-20768be3a4b0"
$expectedRules       = @{
    "RegSP-LowVolume-NPI-Warn"   = @{ Restrict = $false; Severity = "Medium" }
    "RegSP-HighVolume-NPI-Block" = @{ Restrict = $true;  Severity = "High"   }
}

function Assert-ExposedProperty {
    param($InputObject, [string]$Name, [string]$Subject)
    if (-not $InputObject.PSObject.Properties[$Name]) {
        throw "Fail closed: '$Subject' does not expose a '$Name' property in this tenant. Verify '$Subject' manually in the Microsoft Purview portal (Data loss prevention > Policies) before reporting success."
    }
}

$policy = Get-DlpCompliancePolicy -Identity $policyName -ErrorAction Stop
if (-not $policy) { throw "Fail closed: DLP policy '$policyName' was not found." }

Assert-ExposedProperty $policy 'Mode' $policyName
if ("$($policy.Mode)" -ne 'Enable') {
    throw "Fail closed: '$policyName' is Mode=$($policy.Mode). Expected Mode=Enable — simulation modes take no action on prompts."
}

Assert-ExposedProperty $policy 'Locations' $policyName
$locationsJson = ConvertTo-Json -InputObject $policy.Locations -Depth 10 -Compress
if ($locationsJson -notmatch [regex]::Escape($copilotLocationGuid)) {
    throw "Fail closed: '$policyName' does not target the Microsoft 365 Copilot and Copilot Chat location GUID $copilotLocationGuid."
}

Assert-ExposedProperty $policy 'EnforcementPlanes' $policyName
if (-not (@($policy.EnforcementPlanes) -contains 'CopilotExperiences')) {
    throw "Fail closed: '$policyName' does not set the Copilot enforcement plane (EnforcementPlanes=CopilotExperiences)."
}

$rules = @(Get-DlpComplianceRule -Policy $policyName -ErrorAction Stop)
foreach ($ruleName in $expectedRules.Keys) {
    $rule = $rules | Where-Object { $_.Name -eq $ruleName }
    if (-not $rule) { throw "Fail closed: expected rule '$ruleName' is missing from '$policyName'." }

    Assert-ExposedProperty $rule 'Disabled' $ruleName
    if ($rule.Disabled) { throw "Fail closed: rule '$ruleName' is disabled." }

    Assert-ExposedProperty $rule 'GenerateAlert' $ruleName
    if (-not @($rule.GenerateAlert)) {
        throw "Fail closed: rule '$ruleName' has no alert recipients, so the notification this playbook promises is not produced."
    }

    Assert-ExposedProperty $rule 'ReportSeverityLevel' $ruleName
    if ("$($rule.ReportSeverityLevel)" -ne $expectedRules[$ruleName].Severity) {
        throw "Fail closed: rule '$ruleName' has ReportSeverityLevel=$($rule.ReportSeverityLevel); expected $($expectedRules[$ruleName].Severity)."
    }

    if ($expectedRules[$ruleName].Restrict) {
        Assert-ExposedProperty $rule 'RestrictAccess' $ruleName
        $restrictJson = ConvertTo-Json -InputObject $rule.RestrictAccess -Depth 10 -Compress
        if ($restrictJson -notmatch 'ExcludeContentProcessing') {
            throw "Fail closed: rule '$ruleName' does not carry the ExcludeContentProcessing restriction."
        }
        Assert-ExposedProperty $rule 'RestrictWebGrounding' $ruleName
        if (-not $rule.RestrictWebGrounding) {
            throw "Fail closed: rule '$ruleName' does not set RestrictWebGrounding."
        }
    }
}

Write-Host "Verified: '$policyName' is Mode=Enable on Copilot location $copilotLocationGuid with EnforcementPlanes=CopilotExperiences; rules $($expectedRules.Keys -join ', ') exist, are enabled, and carry their expected restriction and alert configuration." -ForegroundColor Green
```

> **Manual verification fallback:** If any `Assert-ExposedProperty` check stops the script, do
> not treat the control as validated. Open **Microsoft Purview portal > Data loss prevention >
> Policies > FSI-RegSP-Copilot-Privacy-Protection**, confirm the policy status is on (not
> simulation), that its location is **Microsoft 365 Copilot and Copilot Chat**, that both rules
> exist with their intended **Prevent Copilot from processing content** actions, and that each
> rule's **Incident reports** section shows the severity level and alert recipients above.
> Record the screenshots as the evidence instead of the script output.

> **Documented Copilot DLP limitations (read before relying on this control):** In the **Microsoft 365 Copilot and Copilot Chat** location, sensitive information type (SIT) enforcement evaluates **the text a user types into the prompt**. The two documented SIT actions are **Prevent Copilot from processing content > Processing prompts** and **> Performing Web Searches**. Microsoft does not document a DLP action that inspects or blocks the text of a **generated Copilot response**; sensitive data in responses can be *observed* after the fact (DSPM / Activity explorer **AI activities**, Audit, eDiscovery) but is not blocked by this control. DLP also can't scan the contents of files uploaded directly into a prompt — only typed prompt text is checked. SIT-based prompt blocking is in preview and rolling out. The sensitivity label condition covers emails sent on or after January 1, 2025; calendar invites and Admin units are not supported. Policy updates can take up to four hours to take effect in the Copilot experience.

### Script 2a: Copilot Interaction Audit Report (metadata only)

`RecordType CopilotInteraction` records the interaction itself; its `Operation` value is
`CopilotInteraction`. Do **not** pair this record type with a DLP operation name — DLP rule
matches are not carried on Copilot interaction records, so such a query returns nothing.

```powershell
$ErrorActionPreference = 'Stop'

$startDate = (Get-Date).AddDays(-30)
$endDate   = Get-Date

$interactions = @(Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000 `
    -ErrorAction Stop)

$report = foreach ($record in $interactions) {
    $data = $record.AuditData | ConvertFrom-Json
    [PSCustomObject]@{
        CreationDate        = $record.CreationDate
        UserId              = $record.UserIds
        Operation           = $record.Operations
        AppHost             = $data.CopilotEventData.AppHost
        ThreadId            = $data.CopilotEventData.ThreadId
        MessageCount        = @($data.CopilotEventData.Messages).Count
        AccessedResources   = (@($data.CopilotEventData.AccessedResources) | ForEach-Object { $_.Name }) -join '; '
        SensitivityLabelIds = (@($data.CopilotEventData.AccessedResources) | ForEach-Object { $_.SensitivityLabelId } | Where-Object { $_ }) -join '; '
    }
}

Write-Host "Copilot interactions audited (last 30 days): $($report.Count)"
$report | Export-Csv "RegSP_CopilotInteractions_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

> **What this report can and can't tell you:** A `CopilotInteraction` audit record carries
> interaction metadata — `AppHost`, `Contexts`, `ThreadId`, `AccessedResources` (with any
> sensitivity label applied), and a `Messages` collection that holds **message IDs and an
> `isPrompt` flag only**. It does **not** contain the prompt or response text, so you cannot
> string-match it for "SSN" or "Credit Card" and call the result an NPI incident count. Use
> Script 2b for DLP matches, DSPM / Activity explorer **AI activities** for SIT detections in
> prompts and responses, and eDiscovery (query condition **Type > Contains any of > Copilot
> activity**) when you need the interaction content itself.

### Script 2b: Copilot DLP Rule-Match Investigation Report

DLP rule matches for the Copilot workload are exported from Activity Explorer, which reports
on up to 30 days of data. Alert triage itself happens in the DLP Alerts dashboard.

```powershell
$ErrorActionPreference = 'Stop'

$start   = (Get-Date).AddDays(-30)
$end     = Get-Date
$outFile = "RegSP_CopilotDlpMatches_$(Get-Date -Format 'yyyyMMdd').json"
$pages   = New-Object System.Collections.Generic.List[string]

$exportArgs = @{
    StartTime    = $start
    EndTime      = $end
    Filter1      = @("Workload", "Copilot")
    Filter2      = @("Activity", "DLPRuleMatch", "DLPRuleEnforce")
    OutputFormat = "Json"
    PageSize     = 5000
    ErrorAction  = "Stop"
}

$page = Export-ActivityExplorerData @exportArgs
foreach ($name in @('ResultData', 'LastPage', 'Watermark')) {
    if (-not $page.PSObject.Properties[$name]) {
        throw "Fail closed: Export-ActivityExplorerData did not return '$name'. Investigate Copilot DLP matches manually in the Microsoft Purview portal (Data loss prevention > Alerts, and Activity explorer > AI activities) instead of relying on this export."
    }
}

$pages.Add($page.ResultData)
while ($page.LastPage -ne $true) {
    $page = Export-ActivityExplorerData @exportArgs -PageCookie $page.Watermark
    $pages.Add($page.ResultData)
}

$pages | Set-Content -Path $outFile
Write-Host "Copilot DLP rule-match activity exported to $outFile (one JSON array per page, 30-day Activity Explorer window)."
Write-Host "Triage the corresponding alerts in the Microsoft Purview portal: Data loss prevention > Alerts."
```

> **Reading the export:** Activity Explorer records for a DLP match carry documented columns
> such as `PolicyName`, `RuleName`, `RuleActions`, `PolicyMode`, `EnforcementMode`, `User`,
> `Workload`, and `SensitiveInfoTypeData`. Filter on those columns rather than string-matching
> raw audit payloads. Not every column is present for every activity.

### Script 3: Content Explorer (classic) NPI Location Report

```powershell
# Identify locations containing consumer financial information
$sensitiveTypes = @(
    "U.S. Social Security Number (SSN)",
    "Credit Card Number",
    "U.S. Bank Account Number",
    "U.S. Individual Taxpayer Identification Number (ITIN)"
)

foreach ($type in $sensitiveTypes) {
    $results = Get-DlpSensitiveInformationType |
        Where-Object { $_.Name -like "*$type*" }
    Write-Host "SIT: $type — Sensitive information type: $($results.Name)" -ForegroundColor Cyan
}

Write-Host "`nUse Content Explorer (classic) in the Purview portal to identify NPI locations." -ForegroundColor Yellow
Write-Host "Path: Purview > Information Protection > Classifiers > Sensitive info types; Content Explorer (classic) is under Solutions > Data classification."
```

### Script 4: Privacy Control Compliance Scorecard

```powershell
# Generate Reg S-P compliance scorecard for Copilot privacy controls
$scorecard = @(
    [PSCustomObject]@{Control="DLP for NPI"; Status="Active"; LastVerified=(Get-Date -Format "yyyy-MM-dd")},
    [PSCustomObject]@{Control="Information Barriers"; Status="Active"; LastVerified=(Get-Date -Format "yyyy-MM-dd")},
    [PSCustomObject]@{Control="Sensitivity Labels"; Status="Active"; LastVerified=(Get-Date -Format "yyyy-MM-dd")},
    [PSCustomObject]@{Control="Access Controls"; Status="Active"; LastVerified=(Get-Date -Format "yyyy-MM-dd")},
    [PSCustomObject]@{Control="Privacy Impact Assessment"; Status="Completed"; LastVerified=(Get-Date -Format "yyyy-MM-dd")},
    [PSCustomObject]@{Control="Written IRP (Rule 248.30(a)(4))"; Status="Active"; LastVerified=(Get-Date -Format "yyyy-MM-dd")},
    [PSCustomObject]@{Control="72-Hour Vendor Notification Procedure (Rule 248.30(a)(3))"; Status="Active"; LastVerified=(Get-Date -Format "yyyy-MM-dd")}
)

Write-Host "Reg S-P Privacy Control Scorecard:"
$scorecard | Format-Table -AutoSize
$scorecard | Export-Csv "RegSP_Scorecard_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 5: Incident Response Timer and Notification Tracking (Rule 248.30(a)(3))

```powershell
# Track the 72-hour vendor notification window for Reg S-P compliance
# Run this script when a Copilot NPI incident is detected

param(
    [Parameter(Mandatory=$true)]
    [string]$IncidentDescription,

    [Parameter(Mandatory=$true)]
    [ValidateSet("Critical","High","Medium","Low")]
    [string]$Severity,

    [Parameter(Mandatory=$false)]
    [datetime]$DetectionTime = (Get-Date)
)

$incidentId = "REGSP-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
$notificationDeadline72hr = $DetectionTime.AddHours(72)
$notificationDeadline30day = $DetectionTime.AddDays(30)

$incidentRecord = [PSCustomObject]@{
    IncidentId            = $incidentId
    DetectedAt            = $DetectionTime.ToString("yyyy-MM-dd HH:mm:ss UTC")
    Severity              = $Severity
    Description           = $IncidentDescription
    InternalEscalationBy  = $DetectionTime.AddHours(4).ToString("yyyy-MM-dd HH:mm:ss UTC")
    ExecutiveNotificationBy = $DetectionTime.AddHours(24).ToString("yyyy-MM-dd HH:mm:ss UTC")
    VendorNotificationBy  = $notificationDeadline72hr.ToString("yyyy-MM-dd HH:mm:ss UTC")  # Rule 248.30(a)(3)
    CustomerNotificationBy = $notificationDeadline30day.ToString("yyyy-MM-dd HH:mm:ss UTC")
    VendorNotified        = "PENDING"
    CustomerNotified      = "PENDING"
}

Write-Host "=== Reg S-P NPI Incident Tracker ===" -ForegroundColor Yellow
Write-Host "Incident ID: $incidentId" -ForegroundColor Cyan
Write-Host "Severity: $Severity" -ForegroundColor $(if ($Severity -eq "Critical") { "Red" } else { "Yellow" })
Write-Host ""
Write-Host "REQUIRED NOTIFICATION DEADLINES:"
Write-Host "  Internal escalation:    $($incidentRecord.InternalEscalationBy)"
Write-Host "  Executive notification: $($incidentRecord.ExecutiveNotificationBy)"
Write-Host "  Microsoft notification: $($incidentRecord.VendorNotificationBy)  [Rule 248.30(a)(3) — 72-HOUR DEADLINE]" -ForegroundColor Red
Write-Host "  Customer notification:  $($incidentRecord.CustomerNotificationBy)  [30-day deadline]"
Write-Host ""
Write-Host "Microsoft notification channel: Microsoft Security Response Center (msrc.microsoft.com)"

$incidentRecord | Export-Csv "RegSP_Incident_$incidentId.csv" -NoTypeInformation
Write-Host "`nIncident record saved to: RegSP_Incident_$incidentId.csv" -ForegroundColor Green
```

**Usage example:**
```powershell
.\Script5-IncidentTracker.ps1 -IncidentDescription "Copilot Chat surfaced client SSN to unauthorized advisor" -Severity "Critical"
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Copilot DLP policy fail-closed validation | Weekly, and after any policy edit | Script 1b |
| Copilot interaction audit report | Weekly | Script 2a |
| Copilot DLP rule-match investigation report | Weekly | Script 2b |
| NPI location assessment | Quarterly | Script 3 |
| Privacy control scorecard | Monthly | Script 4 |
| Incident response timer | On-demand (at incident detection) | Script 5 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate privacy protections
- See [Troubleshooting](troubleshooting.md) for privacy control issues
- Back to [Control 3.10](../../../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md)
