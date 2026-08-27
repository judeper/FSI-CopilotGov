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
# Title alone is not enough — Severity and DetectionDetails are what make the report
# actionable, and Script 1b requires this exact set.
$incidentReportFields = @("Title", "Service", "RulesMatched", "Severity", "DetectionDetails")

# Conditions use the documented operator/groups/sensitivetypes syntax rather than a bare
# array of sensitive information types. Microsoft documents the groups shape and shows
# operator="Or" inside a group, but it does not document which operator a bare array
# implies — and that operator is the whole control: "Or" matches a prompt containing any
# one of these types, while "And" would only match a prompt containing all three at once.
# Stating it explicitly is also what makes it verifiable in Script 1b.
$lowVolumeNpiCondition = @{
    operator = "And"
    groups   = @(
        @{
            operator       = "Or"
            name           = "RegSP NPI types"
            sensitivetypes = @(
                @{ name = "U.S. Social Security Number (SSN)"; mincount = "1"; maxcount = "9" },
                @{ name = "Credit Card Number";                mincount = "1"; maxcount = "9" },
                @{ name = "U.S. Bank Account Number";          mincount = "1"; maxcount = "9" }
            )
        }
    )
}

$highVolumeNpiCondition = @{
    operator = "And"
    groups   = @(
        @{
            operator       = "Or"
            name           = "RegSP NPI types"
            sensitivetypes = @(
                @{ name = "U.S. Social Security Number (SSN)"; mincount = "10" },
                @{ name = "Credit Card Number";                mincount = "10" },
                @{ name = "U.S. Bank Account Number";          mincount = "10" }
            )
        }
    )
}

New-DlpCompliancePolicy `
    -Name $policyName `
    -Comment "Protects consumer financial information per SEC Reg S-P" `
    -Locations '[{"Workload":"Applications","Location":"470f2276-e011-4e9d-a6ec-20768be3a4b0","Inclusions":[{"Type":"Tenant","Identity":"All"}]}]' `
    -EnforcementPlanes @("CopilotExperiences") `
    -Mode Enable `
    -ErrorAction Stop

# Rule for low-volume NPI detection: user notification plus a medium-severity admin alert.
# NotifyUserType is set explicitly rather than left to the service default: the default is
# not documented, and Script 1b validates the notification target and channel exactly.
New-DlpComplianceRule `
    -Name "RegSP-LowVolume-NPI-Warn" `
    -Policy $policyName `
    -ContentContainsSensitiveInformation $lowVolumeNpiCondition `
    -NotifyUser Owner `
    -NotifyUserType "Email,PolicyTip" `
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
    -ContentContainsSensitiveInformation $highVolumeNpiCondition `
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

Run this before reporting the control as implemented. Every check throws on failure; the single
success line is printed only after all checks pass.

Microsoft documents that a `$null` or non-existent `Identity` value makes
`Get-DlpCompliancePolicy` (and `Get-DlpComplianceRule`) return **all** objects, so the script
first binds to exactly one case-sensitive name match and rejects any other count before it
validates anything. It then confirms, in order: `Mode=Enable`; exactly one Microsoft 365 Copilot
and Copilot Chat location entry scoped tenant-wide (`Type=Tenant` / `Identity=All`) with no
exclusions; `EnforcementPlanes=CopilotExperiences`; that each expected rule resolves to exactly
one name match **and** reports the validated policy as its parent; that each rule's condition
uses the documented `operator` / `groups` / `sensitivetypes` shape with **exactly one** group
whose operator is **`Or`** (an `And` group would only match a prompt carrying every NPI type at
once, so a prompt containing only Social Security numbers would slip past); each rule's
sensitive information type conditions and volume thresholds; that the low-volume rule restricts
nothing (no `RestrictAccess`, no `RestrictWebGrounding`, no `BlockAccess`) and notifies exactly
the configured target (`NotifyUser=Owner` and `NotifyUserType=Email,PolicyTip` — a
`SiteAdmin`-only value notifies an administrator and no one else, so it fails); that the
high-volume rule carries exactly one `ExcludeContentProcessing` restriction with the value
`Block` plus `RestrictWebGrounding`; and each rule's `GenerateAlert`, `GenerateIncidentReport`
(with the exact configured recipient set), `IncidentReportContent` (the exact configured field
set — a `Title`-only report, the documented `Default` set, or `All` all fail), and
`ReportSeverityLevel`.

Where a property is not exposed by the tenant's cmdlet build, or its value cannot be read
reliably, the script stops and tells you exactly what to verify by hand rather than silently
passing. That includes the condition operator: a rule created from a bare array of sensitive
information types does not state the operator between the types, so the script fails closed and
points at the portal instead of assuming `Or`. Configuration that is outside this control's
approved design — extra sensitive information types, extra `RestrictAccess` settings, extra
rules in the policy — is reported as a warning and is explicitly **not** validated here.

```powershell
$ErrorActionPreference = 'Stop'

# Expected configuration. Every check below is exact: change these values only when the
# approved policy design changes, and treat any deviation the script reports as unvalidated.
$policyName             = 'FSI-RegSP-Copilot-Privacy-Protection'
$copilotLocationGuid    = '470f2276-e011-4e9d-a6ec-20768be3a4b0'
$privacyAlertRecipients = @('privacy-officer@contoso.com', 'compliance-alerts@contoso.com')

# The exact notification target and channel Script 1 configures on the low-volume rule.
# 'SiteAdmin' is an administrator target: a rule that notifies only SiteAdmin produces no
# notification for the person who typed the prompt, so it is not this design.
$expectedNotifyUser     = @('Owner')
$expectedNotifyUserType = @('Email', 'PolicyTip')

# The exact incident-report field set Script 1 configures. Microsoft documents the full value
# list below; 'Default' is documented to expand to DocumentAuthor/MatchedItem/RulesMatched/
# Service/Title and to make any other value ignored, and 'All' is documented as usable only by
# itself and does not exclude OriginalContent — neither is this design.
$expectedIncidentReportContent  = @('Title', 'Service', 'RulesMatched', 'Severity', 'DetectionDetails')
$documentedIncidentReportFields = @(
    'All', 'Default', 'DetectionDetails', 'Detections', 'DocumentAuthor', 'DocumentLastModifier',
    'MatchedItem', 'OriginalContent', 'RulesMatched', 'Service', 'Severity', 'Title'
)
$documentedNotifyUserTypes = @('NotSet', 'Email', 'PolicyTip')

$expectedRules = [ordered]@{
    'RegSP-LowVolume-NPI-Warn' = @{
        Severity       = 'Medium'
        Restrict       = $false
        SensitiveTypes = @(
            @{ Name = 'U.S. Social Security Number (SSN)'; MinCount = 1; MaxCount = 9 },
            @{ Name = 'Credit Card Number';                MinCount = 1; MaxCount = 9 },
            @{ Name = 'U.S. Bank Account Number';          MinCount = 1; MaxCount = 9 }
        )
    }
    'RegSP-HighVolume-NPI-Block' = @{
        Severity       = 'High'
        Restrict       = $true
        SensitiveTypes = @(
            @{ Name = 'U.S. Social Security Number (SSN)'; MinCount = 10; MaxCount = $null },
            @{ Name = 'Credit Card Number';                MinCount = 10; MaxCount = $null },
            @{ Name = 'U.S. Bank Account Number';          MinCount = 10; MaxCount = $null }
        )
    }
}

$portalEvidence = "Record portal evidence instead: Microsoft Purview portal > Solutions > Data loss prevention > Policies > $policyName — policy status and scope, each rule's conditions and actions, and each rule's Incident reports section (severity, alert toggle, recipients)."

function Get-DlpMemberName {
    param($InputObject, [string]$Name)

    if ($null -eq $InputObject) { return $null }
    if ($InputObject -is [System.Collections.IDictionary]) {
        foreach ($key in $InputObject.Keys) {
            if (([string]$key) -ieq $Name) { return $key }
        }
        return $null
    }
    $property = $InputObject.PSObject.Properties[$Name]
    if ($null -ne $property) { return $property.Name }
    return $null
}

function Test-DlpMember {
    param($InputObject, [string]$Name)

    return ($null -ne (Get-DlpMemberName -InputObject $InputObject -Name $Name))
}

function Get-DlpMember {
    param($InputObject, [string]$Name)

    $key = Get-DlpMemberName -InputObject $InputObject -Name $Name
    if ($null -eq $key) { return $null }
    if ($InputObject -is [System.Collections.IDictionary]) { return $InputObject[$key] }
    return $InputObject.PSObject.Properties[$key].Value
}

function Get-RequiredDlpMember {
    param($InputObject, [string]$Name, [string]$Subject)

    if (-not (Test-DlpMember -InputObject $InputObject -Name $Name)) {
        throw "Fail closed: '$Subject' does not expose '$Name', so this check cannot be completed from cmdlet output and the control is NOT validated. $portalEvidence"
    }
    return (Get-DlpMember -InputObject $InputObject -Name $Name)
}

function ConvertTo-DlpBoolean {
    param($Value, [string]$Subject, [string]$Name)

    if ($null -eq $Value) { return $false }
    if ($Value -is [bool]) { return $Value }
    $text = ([string]$Value).Trim()
    if ($text -eq '') { return $false }
    if ($text -in @('true', '1')) { return $true }
    if ($text -in @('false', '0')) { return $false }
    throw "Fail closed: '$Subject' returned '$text' for '$Name', which cannot be read as a boolean. $portalEvidence"
}

function ConvertTo-DlpCount {
    param($Value, [string]$Subject, [string]$Name)

    if ($null -eq $Value) { return $null }
    $text = ([string]$Value).Trim()
    if ($text -eq '') { return $null }
    $parsed = 0
    if (-not [int]::TryParse($text, [ref]$parsed)) {
        throw "Fail closed: '$Subject' returned '$text' for '$Name', which is not a readable instance count. $portalEvidence"
    }
    return $parsed
}

function Get-DlpRecipientAddress {
    param($Value)

    $text = ([string]$Value).Trim()
    if ($text -eq '') { return $null }
    $address = [regex]::Match($text, '[^\s;,<>"]+@[^\s;,<>"]+')
    if ($address.Success) { return $address.Value.ToLowerInvariant() }
    return $text.ToLowerInvariant()
}

function Assert-DlpRecipient {
    param($Value, [string[]]$Expected, [string]$Subject, [string]$Name)

    $actual = @(@($Value) | ForEach-Object { Get-DlpRecipientAddress -Value $_ } | Where-Object { $_ })
    if ($actual.Count -eq 0) {
        throw "Fail closed: rule '$Subject' has no '$Name' recipients, so the notification this control promises is not produced. $portalEvidence"
    }
    $wanted     = @($Expected | ForEach-Object { Get-DlpRecipientAddress -Value $_ })
    $missing    = @($wanted | Where-Object { $actual -notcontains $_ })
    $unexpected = @($actual | Where-Object { $wanted -notcontains $_ })
    if ($missing.Count -gt 0 -or $unexpected.Count -gt 0) {
        throw "Fail closed: rule '$Subject' '$Name' recipients are [$($actual -join ', ')] but exactly [$($wanted -join ', ')] was expected (missing: [$($missing -join ', ')]; unexpected: [$($unexpected -join ', ')]). $portalEvidence"
    }
}

function Assert-DlpExactSet {
    param([string[]]$Actual, [string[]]$Expected, [string]$Subject, [string]$Name)

    $actualSet  = @($Actual   | ForEach-Object { ([string]$_).Trim().ToLowerInvariant() } | Where-Object { $_ } | Sort-Object -Unique)
    $wantedSet  = @($Expected | ForEach-Object { ([string]$_).Trim().ToLowerInvariant() } | Where-Object { $_ } | Sort-Object -Unique)
    $missing    = @($wantedSet | Where-Object { $actualSet -notcontains $_ })
    $unexpected = @($actualSet | Where-Object { $wantedSet -notcontains $_ })
    if ($missing.Count -gt 0 -or $unexpected.Count -gt 0) {
        throw "Fail closed: rule '$Subject' '$Name' is [$(@($Actual) -join ', ')] but exactly [$($Expected -join ', ')] was expected (missing: [$($missing -join ', ')]; unexpected: [$($unexpected -join ', ')]). $portalEvidence"
    }
}

function Get-DlpTokenList {
    param($Value)

    return @(
        @($Value) |
            Where-Object { $null -ne $_ } |
            ForEach-Object { ([string]$_) -split ',' } |
            ForEach-Object { $_.Trim() } |
            Where-Object { $_ -ne '' }
    )
}

# --- Condition structure -------------------------------------------------------------
# Microsoft documents the ContentContainsSensitiveInformation condition as an
# operator/groups/sensitivetypes structure. The operator inside a group is what decides
# whether the rule matches ANY of the listed NPI types or only a prompt that carries ALL of
# them, so it is read explicitly here instead of flattening the structure and assuming.
function Get-DlpConditionRoot {
    param($Value, [string]$Subject)

    $candidates = @()
    if (($Value -is [System.Collections.IEnumerable]) -and
        -not ($Value -is [System.Collections.IDictionary]) -and
        -not ($Value -is [string])) {
        $candidates = @($Value | Where-Object { $null -ne $_ })
    }
    else {
        $candidates = @($Value | Where-Object { $null -ne $_ })
    }

    $roots = @($candidates | Where-Object { Test-DlpMember -InputObject $_ -Name 'groups' })
    if ($roots.Count -ne 1) {
        throw "Fail closed: rule '$Subject' returned a ContentContainsSensitiveInformation value carrying $($roots.Count) documented condition container(s) ('groups'); exactly 1 is required. A condition built from a bare array of sensitive information types does not state the operator between those types, so this script cannot tell whether the rule matches any one NPI type or only a prompt containing all of them. Recreate the rule with the documented groups syntax shown in Script 1, or record portal evidence. $portalEvidence"
    }
    return $roots[0]
}

function Get-DlpConditionOperator {
    param($Node, [string]$Subject, [string]$Scope)

    if (-not (Test-DlpMember -InputObject $Node -Name 'operator')) {
        throw "Fail closed: rule '$Subject' does not expose the $Scope 'operator', so the logic joining its sensitive information type conditions cannot be confirmed from cmdlet output. $portalEvidence"
    }
    $operator = ([string](Get-DlpMember -InputObject $Node -Name 'operator')).Trim()
    if ($operator -ieq 'And' -or $operator -ieq 'Or') { return $operator }
    throw "Fail closed: rule '$Subject' returned $Scope operator '$operator'. Microsoft documents only 'And' and 'Or' for this key, so the condition logic cannot be read from cmdlet output. $portalEvidence"
}

function Get-DlpSensitiveTypeEntry {
    param($Node, [string]$Subject)

    foreach ($item in @($Node)) {
        if ($null -eq $item -or $item -is [string]) {
            throw "Fail closed: rule '$Subject' returned a sensitive information type entry that is not a readable object, so its name and instance counts cannot be checked. $portalEvidence"
        }
        $name = [string](Get-DlpMember -InputObject $item -Name 'name')
        if ([string]::IsNullOrWhiteSpace($name)) {
            throw "Fail closed: rule '$Subject' returned a sensitive information type entry with no readable 'name', so the condition cannot be checked. $portalEvidence"
        }
        [PSCustomObject]@{
            Name     = $name.Trim()
            MinCount = (Get-DlpMember -InputObject $item -Name 'mincount')
            MaxCount = (Get-DlpMember -InputObject $item -Name 'maxcount')
        }
    }
}

# --- Policy identity -----------------------------------------------------------------
# Microsoft documents that a $null or non-existent Identity value makes Get-DlpCompliancePolicy
# return *all* policies, so bind to exactly one exact-name match before checking anything.
$returnedPolicies = @(Get-DlpCompliancePolicy -Identity $policyName -ErrorAction Stop)
$policyMatches = @(
    foreach ($candidate in $returnedPolicies) {
        $candidateName = Get-RequiredDlpMember -InputObject $candidate -Name 'Name' -Subject 'a returned DLP policy object'
        if (([string]$candidateName) -ceq $policyName) { $candidate }
    }
)
if ($policyMatches.Count -ne 1) {
    throw "Fail closed: Get-DlpCompliancePolicy -Identity '$policyName' returned $($returnedPolicies.Count) object(s) with $($policyMatches.Count) exact name match(es); exactly 1 is required. A non-existent Identity value returns every policy in the tenant, so this result does not confirm the expected policy. $portalEvidence"
}
$policy = $policyMatches[0]

# --- Policy state and Copilot location -----------------------------------------------
$policyMode = Get-RequiredDlpMember -InputObject $policy -Name 'Mode' -Subject $policyName
if (([string]$policyMode) -ne 'Enable') {
    throw "Fail closed: '$policyName' is Mode=$policyMode. Expected Mode=Enable — simulation modes take no action on prompts."
}

$locationValue = Get-RequiredDlpMember -InputObject $policy -Name 'Locations' -Subject $policyName
$locationJson = @()
if ($locationValue -is [string]) {
    $locationJson = @($locationValue)
}
else {
    $locationJson = @(@($locationValue) | Where-Object { $_ -is [string] })
    if ($locationJson.Count -eq 0) {
        $locationJson = @(ConvertTo-Json -InputObject $locationValue -Depth 20)
    }
}

$locationEntries = @(
    foreach ($json in $locationJson) {
        if ([string]::IsNullOrWhiteSpace($json)) { continue }
        try { ConvertFrom-Json -InputObject $json }
        catch { throw "Fail closed: '$policyName' returned a Locations value that could not be parsed as JSON, so the policy scope cannot be confirmed. $portalEvidence" }
    }
)

$copilotLocation = @($locationEntries | Where-Object { ([string](Get-DlpMember -InputObject $_ -Name 'Location')) -ieq $copilotLocationGuid })
if ($copilotLocation.Count -ne 1) {
    throw "Fail closed: '$policyName' does not target exactly one Microsoft 365 Copilot and Copilot Chat location entry (GUID $copilotLocationGuid); $($copilotLocation.Count) matching entr(ies) were found. $portalEvidence"
}

$inclusions = @(Get-RequiredDlpMember -InputObject $copilotLocation[0] -Name 'Inclusions' -Subject "$policyName Copilot location")
$tenantInclusions = @($inclusions | Where-Object {
    (([string](Get-DlpMember -InputObject $_ -Name 'Type')) -ieq 'Tenant') -and
    (([string](Get-DlpMember -InputObject $_ -Name 'Identity')) -ieq 'All')
})
if ($inclusions.Count -eq 0 -or $tenantInclusions.Count -ne $inclusions.Count) {
    $scopeSummary = @($inclusions | ForEach-Object { "$(Get-DlpMember -InputObject $_ -Name 'Type'):$(Get-DlpMember -InputObject $_ -Name 'Identity')" }) -join ', '
    throw "Fail closed: '$policyName' is not scoped tenant-wide on the Copilot location. Inclusions are [$scopeSummary]; expected exactly Type=Tenant / Identity=All so that every Microsoft Copilot and Copilot Chat user is covered. If the narrower scope is a deliberate, approved deviation, record it and the uncovered users as documented evidence — this script does not validate it. $portalEvidence"
}

$exclusions = @(Get-DlpMember -InputObject $copilotLocation[0] -Name 'Exclusions')
$exclusions = @($exclusions | Where-Object { $null -ne $_ })
if ($exclusions.Count -gt 0) {
    $exclusionSummary = @($exclusions | ForEach-Object { "$(Get-DlpMember -InputObject $_ -Name 'Type'):$(Get-DlpMember -InputObject $_ -Name 'Identity')" }) -join ', '
    throw "Fail closed: '$policyName' excludes [$exclusionSummary] from the Copilot location, so the scope is not tenant-wide. Remove the exclusions or record the approved deviation as documented evidence. $portalEvidence"
}

$enforcementPlanes = @(Get-RequiredDlpMember -InputObject $policy -Name 'EnforcementPlanes' -Subject $policyName)
if ($enforcementPlanes -notcontains 'CopilotExperiences') {
    throw "Fail closed: '$policyName' does not set the Copilot enforcement plane (EnforcementPlanes=CopilotExperiences); found [$($enforcementPlanes -join ', ')]."
}

# --- Rules: identity, conditions, actions, alerts -------------------------------------
$policyIdentifiers = @(
    foreach ($identifierName in @('Name', 'Guid', 'ImmutableId', 'Id', 'Identity', 'ExchangeObjectId')) {
        $identifier = Get-DlpMember -InputObject $policy -Name $identifierName
        if ($null -ne $identifier -and -not [string]::IsNullOrWhiteSpace([string]$identifier)) { ([string]$identifier).Trim() }
    }
)

$returnedRules = @(Get-DlpComplianceRule -Policy $policyName -ErrorAction Stop)
$validatedRules = @()

foreach ($ruleName in $expectedRules.Keys) {
    $expected = $expectedRules[$ruleName]
    $ruleMatches = @(
        foreach ($candidate in $returnedRules) {
            $candidateName = Get-RequiredDlpMember -InputObject $candidate -Name 'Name' -Subject 'a returned DLP rule object'
            if (([string]$candidateName) -ceq $ruleName) { $candidate }
        }
    )
    if ($ruleMatches.Count -ne 1) {
        throw "Fail closed: expected rule '$ruleName' matched $($ruleMatches.Count) of the $($returnedRules.Count) returned rule(s); exactly 1 is required. $portalEvidence"
    }
    $rule = $ruleMatches[0]

    # Confirm the rule really belongs to the validated policy rather than to another policy
    # that a loose Identity/Policy resolution returned.
    $parentName = $null
    foreach ($parentProperty in @('ParentPolicyName', 'PolicyName', 'Policy', 'PolicyId')) {
        if (Test-DlpMember -InputObject $rule -Name $parentProperty) {
            $parentValue = Get-DlpMember -InputObject $rule -Name $parentProperty
            if ($null -ne $parentValue -and -not [string]::IsNullOrWhiteSpace([string]$parentValue)) {
                $parentName = ([string]$parentValue).Trim()
                break
            }
        }
    }
    if ($null -eq $parentName) {
        throw "Fail closed: rule '$ruleName' does not expose a parent policy property (ParentPolicyName / PolicyName / Policy / PolicyId), so its membership in '$policyName' cannot be confirmed. $portalEvidence"
    }
    if ($policyIdentifiers -notcontains $parentName) {
        throw "Fail closed: rule '$ruleName' reports parent policy '$parentName', which does not match '$policyName'. $portalEvidence"
    }

    $ruleDisabled = ConvertTo-DlpBoolean -Value (Get-RequiredDlpMember -InputObject $rule -Name 'Disabled' -Subject $ruleName) -Subject $ruleName -Name 'Disabled'
    if ($ruleDisabled) { throw "Fail closed: rule '$ruleName' is disabled." }

    # Conditions
    $conditionValue = Get-RequiredDlpMember -InputObject $rule -Name 'ContentContainsSensitiveInformation' -Subject $ruleName
    if ($conditionValue -is [string]) {
        throw "Fail closed: rule '$ruleName' returned its ContentContainsSensitiveInformation condition as raw text, which this script does not parse. $portalEvidence"
    }

    $conditionRoot = Get-DlpConditionRoot -Value $conditionValue -Subject $ruleName
    $rootOperator = Get-DlpConditionOperator -Node $conditionRoot -Subject $ruleName -Scope 'top-level'
    if ($rootOperator -ine 'And') {
        throw "Fail closed: rule '$ruleName' joins its condition groups with operator '$rootOperator'; the approved design is the documented 'And' top-level operator over a single group. $portalEvidence"
    }

    $conditionGroups = @(Get-DlpMember -InputObject $conditionRoot -Name 'groups' | Where-Object { $null -ne $_ })
    if ($conditionGroups.Count -ne 1) {
        throw "Fail closed: rule '$ruleName' carries $($conditionGroups.Count) condition group(s); the approved design is exactly 1 group holding the NPI sensitive information types. Extra or missing groups change what the rule matches and are not validated here. $portalEvidence"
    }
    $conditionGroup = $conditionGroups[0]

    $groupOperator = Get-DlpConditionOperator -Node $conditionGroup -Subject $ruleName -Scope 'condition group'
    if ($groupOperator -ine 'Or') {
        throw "Fail closed: rule '$ruleName' joins its sensitive information types with operator '$groupOperator'. With 'And' the rule matches only a prompt that carries every listed NPI type at the same time, so a prompt containing nothing but Social Security numbers would not match it. This control requires 'Or' so that any one of the NPI types triggers the rule on its own. $portalEvidence"
    }
    if (Test-DlpMember -InputObject $conditionGroup -Name 'groups') {
        throw "Fail closed: rule '$ruleName' nests further condition groups inside its NPI group, so the effective match logic is not the flat 'any one of these types' design this script validates. $portalEvidence"
    }
    if (-not (Test-DlpMember -InputObject $conditionGroup -Name 'sensitivetypes')) {
        throw "Fail closed: rule '$ruleName' condition group does not expose 'sensitivetypes', so the sensitive information types it matches cannot be confirmed from cmdlet output. $portalEvidence"
    }
    if (Test-DlpMember -InputObject $conditionGroup -Name 'labels') {
        Write-Warning "Rule '$ruleName' also carries a sensitivity label condition in the same group. That condition is outside this control's approved design and is not validated here; review it separately."
    }

    $actualTypes = @(Get-DlpSensitiveTypeEntry -Node (Get-DlpMember -InputObject $conditionGroup -Name 'sensitivetypes') -Subject $ruleName)
    foreach ($expectedType in $expected.SensitiveTypes) {
        $typeMatches = @($actualTypes | Where-Object { $_.Name -ieq $expectedType.Name })
        if ($typeMatches.Count -ne 1) {
            throw "Fail closed: rule '$ruleName' matched $($typeMatches.Count) condition entr(ies) for sensitive information type '$($expectedType.Name)'; exactly 1 is required. Found [$(@($actualTypes | ForEach-Object { $_.Name }) -join ', ')]. $portalEvidence"
        }
        $actualMin = ConvertTo-DlpCount -Value $typeMatches[0].MinCount -Subject $ruleName -Name "$($expectedType.Name) minCount"
        if ($actualMin -ne $expectedType.MinCount) {
            throw "Fail closed: rule '$ruleName' uses minCount=$actualMin for '$($expectedType.Name)'; expected $($expectedType.MinCount). The volume thresholds separate the warn rule from the restrict rule, so a mismatch changes what the control enforces."
        }
        $actualMax = ConvertTo-DlpCount -Value $typeMatches[0].MaxCount -Subject $ruleName -Name "$($expectedType.Name) maxCount"
        if ($null -eq $expectedType.MaxCount) {
            if ($null -ne $actualMax) {
                throw "Fail closed: rule '$ruleName' caps '$($expectedType.Name)' at maxCount=$actualMax; the high-volume rule is expected to have no upper bound, otherwise the largest disclosures fall outside it."
            }
        }
        elseif ($actualMax -ne $expectedType.MaxCount) {
            throw "Fail closed: rule '$ruleName' uses maxCount=$actualMax for '$($expectedType.Name)'; expected $($expectedType.MaxCount)."
        }
    }
    $extraTypes = @($actualTypes | Where-Object { $expected.SensitiveTypes.Name -notcontains $_.Name })
    if ($extraTypes.Count -gt 0) {
        Write-Warning "Rule '$ruleName' also matches [$(@($extraTypes | ForEach-Object { $_.Name }) -join ', ')]. Those conditions are outside this control's approved design and are not validated here; review them separately."
    }

    # Actions
    $restrictAccess = @(Get-DlpMember -InputObject $rule -Name 'RestrictAccess')
    $restrictAccess = @($restrictAccess | Where-Object { $null -ne $_ })
    $webGroundingValue = $null
    if (Test-DlpMember -InputObject $rule -Name 'RestrictWebGrounding') {
        $webGroundingValue = Get-DlpMember -InputObject $rule -Name 'RestrictWebGrounding'
    }
    $restrictsWebGrounding = ConvertTo-DlpBoolean -Value $webGroundingValue -Subject $ruleName -Name 'RestrictWebGrounding'
    $blocksAccess = ConvertTo-DlpBoolean -Value (Get-DlpMember -InputObject $rule -Name 'BlockAccess') -Subject $ruleName -Name 'BlockAccess'

    if ($expected.Restrict) {
        if (-not (Test-DlpMember -InputObject $rule -Name 'RestrictAccess')) {
            throw "Fail closed: rule '$ruleName' does not expose 'RestrictAccess', so its Copilot content-processing action cannot be confirmed. $portalEvidence"
        }
        $processingActions = @($restrictAccess | Where-Object { ([string](Get-DlpMember -InputObject $_ -Name 'setting')) -ieq 'ExcludeContentProcessing' })
        if ($processingActions.Count -ne 1) {
            throw "Fail closed: rule '$ruleName' carries $($processingActions.Count) 'ExcludeContentProcessing' restriction(s); exactly 1 is required so that Copilot prompt processing is restricted. $portalEvidence"
        }
        $processingValue = [string](Get-RequiredDlpMember -InputObject $processingActions[0] -Name 'value' -Subject "$ruleName ExcludeContentProcessing")
        if ($processingValue -ine 'Block') {
            throw "Fail closed: rule '$ruleName' sets ExcludeContentProcessing=$processingValue; expected Block. Any other value leaves high-volume NPI prompts unrestricted."
        }
        $otherActions = @($restrictAccess | Where-Object { ([string](Get-DlpMember -InputObject $_ -Name 'setting')) -ine 'ExcludeContentProcessing' })
        if ($otherActions.Count -gt 0) {
            Write-Warning "Rule '$ruleName' also carries RestrictAccess settings [$(@($otherActions | ForEach-Object { Get-DlpMember -InputObject $_ -Name 'setting' }) -join ', ')], which are outside this control's approved design and are not validated here."
        }
        if (-not (Test-DlpMember -InputObject $rule -Name 'RestrictWebGrounding')) {
            throw "Fail closed: rule '$ruleName' does not expose 'RestrictWebGrounding', so the web-grounding restriction cannot be confirmed. $portalEvidence"
        }
        if (-not $restrictsWebGrounding) {
            throw "Fail closed: rule '$ruleName' does not set RestrictWebGrounding, so high-volume NPI prompts can still be sent to web search grounding."
        }
    }
    else {
        if ($restrictAccess.Count -gt 0) {
            throw "Fail closed: rule '$ruleName' carries RestrictAccess settings [$(@($restrictAccess | ForEach-Object { "$(Get-DlpMember -InputObject $_ -Name 'setting')=$(Get-DlpMember -InputObject $_ -Name 'value')" }) -join ', ')]. The low-volume rule is designed to notify without restricting Copilot; a restriction here changes the documented user experience and is not validated by this script."
        }
        if ($restrictsWebGrounding) {
            throw "Fail closed: rule '$ruleName' sets RestrictWebGrounding. The low-volume rule is designed to notify without restricting Copilot."
        }
        if ($blocksAccess) {
            throw "Fail closed: rule '$ruleName' sets BlockAccess. The low-volume rule is designed to notify without restricting Copilot."
        }
        $notifyUser = @(Get-RequiredDlpMember -InputObject $rule -Name 'NotifyUser' -Subject $ruleName)
        $notifyUser = @($notifyUser | ForEach-Object { ([string]$_).Trim() } | Where-Object { $_ -ne '' })
        if ($notifyUser.Count -eq 0) {
            throw "Fail closed: rule '$ruleName' has no NotifyUser recipients, so the end-user notification this control expects for low-volume detections is not configured. $portalEvidence"
        }
        $endUserTargets = @($notifyUser | Where-Object { $_ -ine 'SiteAdmin' })
        if ($endUserTargets.Count -eq 0) {
            throw "Fail closed: rule '$ruleName' sets NotifyUser=[$($notifyUser -join ', ')]. SiteAdmin is an administrator target, so nothing reaches the person who typed the prompt and the low-volume rule notifies no user at all. Expected NotifyUser exactly [$($expectedNotifyUser -join ', ')]. $portalEvidence"
        }
        Assert-DlpExactSet -Actual $notifyUser -Expected $expectedNotifyUser -Subject $ruleName -Name 'NotifyUser'

        $notifyUserTypes = @(Get-DlpTokenList -Value (Get-RequiredDlpMember -InputObject $rule -Name 'NotifyUserType' -Subject $ruleName))
        if ($notifyUserTypes.Count -eq 0) {
            throw "Fail closed: rule '$ruleName' returned an empty NotifyUserType, so the notification channel cannot be confirmed. $portalEvidence"
        }
        $undocumentedTypes = @($notifyUserTypes | Where-Object { $documentedNotifyUserTypes -notcontains $_ })
        if ($undocumentedTypes.Count -gt 0) {
            throw "Fail closed: rule '$ruleName' returned NotifyUserType value(s) [$($undocumentedTypes -join ', ')] that are not in the documented set [$($documentedNotifyUserTypes -join ', ')], so the notification channel cannot be read from cmdlet output. $portalEvidence"
        }
        if ($notifyUserTypes -contains 'NotSet') {
            throw "Fail closed: rule '$ruleName' has NotifyUserType=NotSet, so no notification channel is selected and the notification this rule is designed to produce cannot be confirmed. $portalEvidence"
        }
        Assert-DlpExactSet -Actual $notifyUserTypes -Expected $expectedNotifyUserType -Subject $ruleName -Name 'NotifyUserType'
    }

    # Alerts, incident reports, severity, recipients
    Assert-DlpRecipient -Value (Get-RequiredDlpMember -InputObject $rule -Name 'GenerateAlert' -Subject $ruleName) -Expected $privacyAlertRecipients -Subject $ruleName -Name 'GenerateAlert'
    Assert-DlpRecipient -Value (Get-RequiredDlpMember -InputObject $rule -Name 'GenerateIncidentReport' -Subject $ruleName) -Expected $privacyAlertRecipients -Subject $ruleName -Name 'GenerateIncidentReport'

    $reportContent = @(Get-DlpTokenList -Value (Get-RequiredDlpMember -InputObject $rule -Name 'IncidentReportContent' -Subject $ruleName))
    if ($reportContent.Count -eq 0) {
        throw "Fail closed: rule '$ruleName' has no IncidentReportContent fields, so the incident report carries no detection detail. $portalEvidence"
    }
    $undocumentedFields = @($reportContent | Where-Object { $documentedIncidentReportFields -notcontains $_ })
    if ($undocumentedFields.Count -gt 0) {
        throw "Fail closed: rule '$ruleName' returned IncidentReportContent value(s) [$($undocumentedFields -join ', ')] that are not in the documented value list, so the report contents cannot be read from cmdlet output. $portalEvidence"
    }
    if ($reportContent -contains 'OriginalContent') {
        throw "Fail closed: rule '$ruleName' includes OriginalContent in its incident report, which copies detected NPI into notification email. Remove it, or record the approved exception as documented evidence."
    }
    if ($reportContent -contains 'All') {
        throw "Fail closed: rule '$ruleName' sets IncidentReportContent=All. Microsoft documents All as usable only by itself, and it does not exclude OriginalContent, so it cannot be relied on to keep detected NPI out of notification email. Expected exactly [$($expectedIncidentReportContent -join ', ')]. $portalEvidence"
    }
    if ($reportContent -contains 'Default') {
        throw "Fail closed: rule '$ruleName' sets IncidentReportContent=Default. Microsoft documents Default as DocumentAuthor, MatchedItem, RulesMatched, Service, and Title, and documents that any additional values used with it are ignored — so the report would carry neither Severity nor DetectionDetails. Expected exactly [$($expectedIncidentReportContent -join ', ')]. $portalEvidence"
    }
    Assert-DlpExactSet -Actual $reportContent -Expected $expectedIncidentReportContent -Subject $ruleName -Name 'IncidentReportContent'

    $severity = [string](Get-RequiredDlpMember -InputObject $rule -Name 'ReportSeverityLevel' -Subject $ruleName)
    if ($severity -ne $expected.Severity) {
        throw "Fail closed: rule '$ruleName' has ReportSeverityLevel=$severity; expected $($expected.Severity)."
    }

    $validatedRules += $ruleName
}

$unexpectedRules = @(
    foreach ($candidate in $returnedRules) {
        $candidateName = [string](Get-DlpMember -InputObject $candidate -Name 'Name')
        if ($expectedRules.Keys -notcontains $candidateName) { $candidateName }
    }
)
if ($unexpectedRules.Count -gt 0) {
    Write-Warning "'$policyName' also contains rule(s) [$($unexpectedRules -join ', ')] that are outside this control's approved design. They are not validated here; review them separately."
}

Write-Host "Verified: '$policyName' resolved to exactly one policy, is Mode=Enable, is scoped tenant-wide (Type=Tenant / Identity=All, no exclusions) on Copilot location $copilotLocationGuid with EnforcementPlanes=CopilotExperiences, and rules $($validatedRules -join ', ') are enabled with a single 'Or' sensitive information type condition group, their expected volume thresholds, restriction actions, notification target and channel, incident report fields ($($expectedIncidentReportContent -join ', ')), severity, and alert recipients ($($privacyAlertRecipients -join ', ')). Any warnings above cover configuration outside this control's design and are not validated." -ForegroundColor Green
```

> **Manual verification fallback:** If any check stops the script — including the "does not
> expose" and "cannot be read" messages — do not treat the control as validated. Open
> **Microsoft Purview portal > Solutions > Data loss prevention > Policies >
> FSI-RegSP-Copilot-Privacy-Protection**, confirm the policy status is on (not simulation),
> that its location is **Microsoft 365 Copilot and Copilot Chat** scoped to all users with no
> exclusions, that each rule's **Content contains** condition is grouped with **Any of these**
> (the portal wording for the `Or` group operator — **All of these** would require every NPI
> type in one prompt), that the low-volume rule notifies the user without any **Prevent Copilot
> from processing content** action, that the high-volume rule carries both **Processing
> prompts** and **Performing Web Searches** restrictions, and that each rule's **Incident
> reports** section shows the severity level, the admin-alert toggle, the recipients above, and
> the exact included fields (Title, Service, RulesMatched, Severity, DetectionDetails). Record
> the screenshots as the evidence instead of the script output.

> **Documented Copilot DLP limitations (read before relying on this control):** In the **Microsoft 365 Copilot and Copilot Chat** location, sensitive information type (SIT) enforcement evaluates **the text a user types into the prompt**. The two documented SIT actions are **Prevent Copilot from processing content > Processing prompts** and **> Performing Web Searches**. Microsoft does not document a DLP action that inspects or blocks the text of a **generated Copilot response**; sensitive data in responses can be *observed* after the fact (DSPM / Activity explorer **AI activities**, Audit, eDiscovery) but is not blocked by this control. DLP also can't scan the contents of files uploaded directly into a prompt — only typed prompt text is checked. SIT-based prompt blocking is in preview and rolling out. The sensitivity label condition covers emails sent on or after January 1, 2025; calendar invites and Admin units are not supported. Policy updates can take up to four hours to take effect in the Copilot experience.

### Script 2a: Copilot Interaction Audit Report (metadata only)

`RecordType CopilotInteraction` records the interaction itself; its `Operation` value is
`CopilotInteraction`. Do **not** pair this record type with a DLP operation name — DLP rule
matches are not carried on Copilot interaction records, so such a query returns nothing.

Microsoft documents that `Search-UnifiedAuditLog` returns a maximum of 100 results by default,
that `-SessionCommand ReturnLargeSet` with a **stable** `-SessionId` pages through a maximum of
50,000 results per session (5,000 records per page, unsorted), and that larger result sets have
to be split into narrower searches. A single call is therefore a sample, not a 30-day
population.

Paging to exhaustion is not by itself completeness. Microsoft documents `ReturnLargeSet` as
"optimized for search latency" and documents the `-HighCompleteness` switch (currently in
preview and not available in all organizations) as the option that "specifies completeness
instead performance in the results" — stating explicitly that **"If you don't use this switch,
the query runs faster but might have missing search results."** The collector below therefore
refuses to run at all unless the installed `Search-UnifiedAuditLog` exposes `-HighCompleteness`,
and passes it on every page. Microsoft does not document how `-HighCompleteness` interacts with
`-SessionCommand ReturnLargeSet`; if the combination is rejected by the service, the page call
throws and no count is printed.

The collector pages each one-day segment with one SessionId per segment, deduplicates on
`AuditData.Id`, and throws — instead of printing a count — whenever a page errors, a page of
records arrives without any of the documented progress signals (`ResultIndex`, `ResultCount`,
`AuditSearchRequestMetadata.moreRecordsAvailable`), paging stops making progress, a segment ends
while the service still reports more records available, a record cannot be deduplicated, or a
segment reaches the documented 50,000-result ceiling. A partial collection is never reported as
a complete count.

```powershell
$ErrorActionPreference = 'Stop'

# Collects every CopilotInteraction record in the window. Microsoft documents that
# Search-UnifiedAuditLog returns up to 100 records by default, that SessionCommand
# ReturnLargeSet with a stable SessionId pages through up to 50,000 results per session
# (max 5,000 records per page), that larger result sets must be split across narrower
# searches, and that without -HighCompleteness a query "runs faster but might have missing
# search results". Anything this function cannot page to exhaustion on a
# completeness-capable path is thrown, never returned as a partial evidence set.
function Get-PagedCopilotInteractionRecord {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [datetime]$StartDate,

        [Parameter(Mandatory)]
        [datetime]$EndDate,

        [timespan]$SegmentDuration = [timespan]::FromDays(1)
    )

    if ($EndDate -le $StartDate) {
        throw "EndDate must be later than StartDate."
    }
    if ($SegmentDuration -le [timespan]::Zero) {
        throw "SegmentDuration must be greater than zero."
    }

    # Completeness-capable path check. Microsoft documents that without -HighCompleteness the
    # query "runs faster but might have missing search results", so a build that cannot offer
    # the switch cannot produce an exhaustive population and must not pretend otherwise.
    $auditCommand = Get-Command -Name Search-UnifiedAuditLog -ErrorAction Stop
    if (-not $auditCommand.Parameters.ContainsKey('HighCompleteness')) {
        throw "Fail closed: the installed Search-UnifiedAuditLog does not expose -HighCompleteness, so results are returned on the performance-optimized path that Microsoft documents as possibly having missing search results. This collector cannot represent its output as a complete population. Update the ExchangeOnlineManagement module to a build that supports -HighCompleteness, or collect the evidence from Microsoft Purview portal > Solutions > Audit and record the search parameters and export as the evidence instead."
    }

    $records = [System.Collections.Generic.List[object]]::new()
    $seenRecordIds = [System.Collections.Generic.HashSet[string]]::new(
        [System.StringComparer]::OrdinalIgnoreCase
    )

    for ($segmentStart = $StartDate; $segmentStart -lt $EndDate; $segmentStart = $segmentEnd) {
        $segmentEnd = $segmentStart.Add($SegmentDuration)
        if ($segmentEnd -gt $EndDate) {
            $segmentEnd = $EndDate
        }

        # One stable SessionId per segment, and the same SessionCommand for every page of
        # that session — switching either mid-session silently truncates the results.
        $sessionId = "RegSPCopilotInteraction_$([guid]::NewGuid())"
        $pageNumber = 0
        $previousResultIndex = -1L
        $segmentResultCount = 0
        $segmentExhausted = $false
        $moreRecordsExpected = $false

        do {
            $pageNumber++
            if ($pageNumber -gt 100) {
                throw "Paging safety limit reached for $segmentStart to $segmentEnd (SessionId $sessionId); this run is not complete."
            }

            try {
                $page = @(
                    Search-UnifiedAuditLog `
                        -StartDate $segmentStart `
                        -EndDate $segmentEnd `
                        -RecordType CopilotInteraction `
                        -Operations "CopilotInteraction" `
                        -SessionId $sessionId `
                        -SessionCommand ReturnLargeSet `
                        -HighCompleteness `
                        -ResultSize 5000 `
                        -ErrorAction Stop
                )
            }
            catch {
                throw (
                    "Search-UnifiedAuditLog failed for segment $segmentStart to " +
                    "$segmentEnd on page $pageNumber (SessionId $sessionId). " +
                    "No evidence from this run should be treated as complete. " +
                    "Underlying error: $($_.Exception.Message)"
                )
            }

            if ($page.Count -eq 0) {
                if ($moreRecordsExpected) {
                    throw "Audit paging for $segmentStart to $segmentEnd (SessionId $sessionId) returned zero records on page $pageNumber after the service reported more records were available; the segment was truncated and this run is not complete."
                }
                $segmentExhausted = $true
                break
            }

            $segmentResultCount += $page.Count
            $newRecordCount = 0

            foreach ($record in $page) {
                $auditDataProperty = $record.PSObject.Properties['AuditData']
                if ($null -eq $auditDataProperty -or [string]::IsNullOrWhiteSpace([string]$auditDataProperty.Value)) {
                    throw "An audit record in segment $segmentStart to $segmentEnd has no AuditData; safe deduplication is not possible, so this run is not complete."
                }

                $auditData = ConvertFrom-Json -InputObject ([string]$auditDataProperty.Value)
                $idProperty = $auditData.PSObject.Properties['Id']
                $recordId = if ($null -ne $idProperty) { [string]$idProperty.Value } else { '' }
                if ([string]::IsNullOrWhiteSpace($recordId)) {
                    throw "An audit record in segment $segmentStart to $segmentEnd is missing AuditData.Id; safe deduplication is not possible, so this run is not complete."
                }

                if ($seenRecordIds.Add($recordId)) {
                    $records.Add(
                        [PSCustomObject]@{
                            Record    = $record
                            AuditData = $auditData
                        }
                    )
                    $newRecordCount++
                }
            }

            $lastResult = $page[-1]
            $resultIndexProperty = $lastResult.PSObject.Properties['ResultIndex']
            $resultCountProperty = $lastResult.PSObject.Properties['ResultCount']
            $hasResultIndex = $null -ne $resultIndexProperty -and
                -not [string]::IsNullOrWhiteSpace([string]$resultIndexProperty.Value)
            $hasResultCount = $null -ne $resultCountProperty -and
                -not [string]::IsNullOrWhiteSpace([string]$resultCountProperty.Value)

            if ($hasResultIndex) {
                $resultIndex = [long]$resultIndexProperty.Value
                if ($resultIndex -le $previousResultIndex -and $newRecordCount -eq 0) {
                    throw "Audit paging made no progress for $segmentStart to $segmentEnd (SessionId $sessionId); this run is not complete."
                }
                $previousResultIndex = $resultIndex
            }

            $metadataProperty = $lastResult.PSObject.Properties['AuditSearchRequestMetadata']
            $moreRecordsProperty = $null
            if ($null -ne $metadataProperty -and $null -ne $metadataProperty.Value) {
                $moreRecordsProperty = $metadataProperty.Value.PSObject.Properties['moreRecordsAvailable']
            }

            # Microsoft names ResultIndex, ResultCount, and
            # AuditSearchRequestMetadata.moreRecordsAvailable as the data to gauge progress
            # with. A page of records carrying none of them cannot be reasoned about, so the
            # run is failed rather than paged blindly until an empty page looks like the end.
            if ($null -eq $moreRecordsProperty -and -not ($hasResultIndex -and $hasResultCount)) {
                throw "Audit page $pageNumber for $segmentStart to $segmentEnd (SessionId $sessionId) returned records without any documented progress signal (AuditSearchRequestMetadata.moreRecordsAvailable, or both ResultIndex and ResultCount), so exhaustion cannot be established and this run is not complete."
            }

            if ($null -ne $moreRecordsProperty) {
                $segmentExhausted = -not [System.Convert]::ToBoolean($moreRecordsProperty.Value)
            }
            elseif ($hasResultIndex -and $hasResultCount) {
                $segmentExhausted = ([long]$resultIndexProperty.Value -eq [long]$resultCountProperty.Value)
            }
            $moreRecordsExpected = -not $segmentExhausted

            if (
                $segmentResultCount -ge 50000 -or
                ($hasResultCount -and [long]$resultCountProperty.Value -ge 50000)
            ) {
                throw (
                    "The $segmentStart to $segmentEnd segment reached the documented " +
                    "50,000-result ceiling for a Search-UnifiedAuditLog session. Rerun with a " +
                    "smaller -SegmentDuration (for example, [timespan]::FromHours(1)); this " +
                    "result cannot be represented as complete."
                )
            }

            if (-not $segmentExhausted -and $newRecordCount -eq 0) {
                throw "Audit paging returned only duplicate records for $segmentStart to $segmentEnd before reporting exhaustion; this run is not complete."
            }
        }
        while (-not $segmentExhausted)
    }

    return $records
}

$endDate   = (Get-Date).ToUniversalTime()
$startDate = $endDate.AddDays(-30)

$interactions = @(
    Get-PagedCopilotInteractionRecord -StartDate $startDate -EndDate $endDate
)

$report = @(
    foreach ($envelope in $interactions) {
        $record = $envelope.Record
        $data   = $envelope.AuditData
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
)

Write-Host "Copilot interactions audited from $($startDate.ToString('u')) to $($endDate.ToString('u')): $($report.Count)."
Write-Host "Every segment was collected with -HighCompleteness — the option Microsoft documents as prioritizing completeness over performance — and paged until the service's own documented signals reported exhaustion. The collector throws instead of returning a partial set, so this count is the population the audit service reported for the window, not a sample."
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

`Export-ActivityExplorerData` returns one page per call (`ResultData`, `LastPage`, `Watermark`),
and the watermark from a non-final page is passed back as the next call's `-PageCookie`. Writing
each page's `ResultData` string to the same file would concatenate several top-level JSON
documents — that is not a valid JSON file and `ConvertFrom-Json` (or any JSON parser) rejects it.
The script below deserializes every page and writes **one** JSON array of records, plus a
companion `.pages.json` file holding the per-page metadata (page number, record count,
watermark, last-page flag) so paging remains auditable. It throws instead of writing a file when
a page is missing a documented property, returns unreadable JSON or `LastPage`, or repeats a
watermark. Note that `-AsArray` is deliberately **not** used: `ConvertTo-Json -InputObject`
does not enumerate its argument, so an array passed to `-InputObject` is already serialized as a
JSON array and `-AsArray` would wrap it a second time, producing a nested `[[...]]` document
that no consumer of this evidence expects. Without `-AsArray`, zero records serialize to `[]`,
one record to `[{...}]`, and many records to a flat array.

```powershell
$ErrorActionPreference = 'Stop'

$start    = (Get-Date).AddDays(-30)
$end      = Get-Date
$stamp    = Get-Date -Format 'yyyyMMdd'
$outFile  = "RegSP_CopilotDlpMatches_$stamp.json"
$pageFile = "RegSP_CopilotDlpMatches_$stamp.pages.json"

$exportArgs = @{
    StartTime    = $start
    EndTime      = $end
    Filter1      = @("Workload", "Copilot")
    Filter2      = @("Activity", "DLPRuleMatch", "DLPRuleEnforce")
    OutputFormat = "Json"
    PageSize     = 5000
    ErrorAction  = "Stop"
}

$records        = [System.Collections.Generic.List[object]]::new()
$pageMetadata   = [System.Collections.Generic.List[object]]::new()
$seenWatermarks = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
$pageCookie     = $null
$pageNumber     = 0
$lastPage       = $false

do {
    $pageNumber++
    if ($pageNumber -gt 1000) {
        throw "Fail closed: Export-ActivityExplorerData paging safety limit reached after $pageNumber pages; this export is not complete."
    }

    try {
        if ($null -eq $pageCookie) {
            $page = Export-ActivityExplorerData @exportArgs
        }
        else {
            $page = Export-ActivityExplorerData @exportArgs -PageCookie $pageCookie
        }
    }
    catch {
        throw "Fail closed: Export-ActivityExplorerData failed on page $pageNumber. No file is written and nothing from this run is complete. Underlying error: $($_.Exception.Message)"
    }

    foreach ($name in @('ResultData', 'LastPage', 'Watermark')) {
        if (-not $page.PSObject.Properties[$name]) {
            throw "Fail closed: Export-ActivityExplorerData page $pageNumber did not return '$name'. Investigate Copilot DLP matches manually in the Microsoft Purview portal (Data loss prevention > Alerts, and Activity explorer > AI activities) instead of relying on this export."
        }
    }

    # Deserialize each page and keep the records, so the artifact is one JSON document
    # rather than several concatenated top-level JSON values.
    $pageRecords = @()
    $resultData = $page.ResultData
    if ($resultData -is [string]) {
        if (-not [string]::IsNullOrWhiteSpace($resultData)) {
            try { $parsedPage = ConvertFrom-Json -InputObject $resultData }
            catch { throw "Fail closed: page $pageNumber of the Activity Explorer export is not valid JSON, so the export cannot be aggregated. Underlying error: $($_.Exception.Message)" }
            if ($null -ne $parsedPage) { $pageRecords = @($parsedPage) }
        }
    }
    else {
        $pageRecords = @(@($resultData) | Where-Object { $null -ne $_ })
    }

    foreach ($record in $pageRecords) { $records.Add($record) }

    $lastPageValue = $page.LastPage
    if ($lastPageValue -is [bool]) {
        $lastPage = $lastPageValue
    }
    elseif ("$lastPageValue" -in @('True', 'False')) {
        $lastPage = [System.Convert]::ToBoolean("$lastPageValue")
    }
    else {
        throw "Fail closed: page $pageNumber returned LastPage='$lastPageValue', which cannot be read as a boolean, so exhaustion cannot be confirmed."
    }

    $watermark = [string]$page.Watermark
    $pageMetadata.Add([PSCustomObject]@{
        Page        = $pageNumber
        RecordCount = $pageRecords.Count
        LastPage    = $lastPage
        Watermark   = $watermark
    })

    if (-not $lastPage) {
        if ([string]::IsNullOrWhiteSpace($watermark)) {
            throw "Fail closed: page $pageNumber reports more data but returned no Watermark, so the remaining pages cannot be requested and this export is not complete."
        }
        if (-not $seenWatermarks.Add($watermark)) {
            throw "Fail closed: Export-ActivityExplorerData returned a repeated Watermark on page $pageNumber; paging is not progressing and this export is not complete."
        }
        $pageCookie = $watermark
    }
}
while (-not $lastPage)

$recordArray = $records.ToArray()

# No -AsArray here: ConvertTo-Json -InputObject does not enumerate its argument, so these
# arrays already serialize as JSON arrays ([] when empty, [{...}] for a single record).
# Adding -AsArray would wrap them again and emit a nested [[...]] document.
ConvertTo-Json -InputObject $recordArray -Depth 20 | Set-Content -Path $outFile -Encoding utf8
ConvertTo-Json -InputObject $pageMetadata.ToArray() -Depth 5 | Set-Content -Path $pageFile -Encoding utf8

Write-Host "Copilot DLP rule-match activity exported to $outFile — one JSON array holding $($recordArray.Count) record(s) aggregated from $pageNumber page(s) of the 30-day Activity Explorer window."
Write-Host "Per-page metadata (page number, record count, watermark, last-page flag) is in $pageFile."
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

Write-Host "`nUse Content explorer (classic) in the Purview portal to identify NPI locations." -ForegroundColor Yellow
Write-Host "Path: Microsoft Purview portal > Solutions > Data Lifecycle Management > Explorers > Content explorer."
Write-Host "Sensitive information type definitions: Microsoft Purview portal > Solutions > Information Protection > Classifiers > Sensitive info types."
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
