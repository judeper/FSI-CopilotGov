# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Verification & Testing

Test cases and evidence collection procedures to validate privacy controls for consumer financial information in Copilot interactions, including the incident response program requirements from the Reg S-P amendments proposed in 2023 and adopted by the SEC in May 2024 (Release No. 34-100155).

## Test Cases

### Test 1: DLP Detection of NPI in Copilot Prompts and Policy Configuration Verification

- **Objective:** Verify that DLP policies detect nonpublic personal information **entered as Copilot prompt text**, and that the exact expected policy is enabled on the Copilot location and enforcement plane with both expected rules and their alert configuration
- **Steps:**
  1. Using a test account, **type** test SSN and account number data directly into a Copilot prompt. Do not attach the test data as an uploaded file — uploaded file contents are not scanned by this control, so a file-based test proves nothing.
  2. Submit the prompt and observe whether Copilot processing is restricted.
  3. Verify that the DLP policy tip appears warning about NPI content. During the SIT-in-prompts preview, user messaging in Word, Excel, and PowerPoint may not clearly attribute the block to organizational policy; the prompt is still restricted.
  4. Run the fail-closed verification. This is the same validator as [PowerShell Setup — Script 1b](powershell-setup.md), with the session connect line added. Every check throws; the single success line prints only if all checks pass. It resolves exactly one case-sensitive policy-name match before validating anything (a `$null` or non-existent `Identity` value makes `Get-DlpCompliancePolicy` return every policy in the tenant), and it verifies tenant-wide Copilot scope, the enforcement plane, each rule's identity and parent policy, its conditions and volume thresholds, the low-volume rule's nonrestricting behavior, the high-volume rule's exact `ExcludeContentProcessing=Block` and `RestrictWebGrounding` actions, and each rule's `GenerateAlert`, `GenerateIncidentReport`, `IncidentReportContent`, `ReportSeverityLevel`, and recipients:
     ```powershell
     $ErrorActionPreference = 'Stop'
     Connect-IPPSSession -ErrorAction Stop

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
  5. Confirm that high-volume NPI **in prompt text** triggers the documented Copilot content-processing restriction.
- **Expected Result:** DLP detects NPI typed into the prompt, displays policy tips or restricts Copilot processing, and the verification script prints its single success line with no exception raised.
- **Evidence:** Screenshots of DLP policy tips/content-processing restrictions; PowerShell transcript showing the verification success line; if any check stopped the script, the portal screenshots described in the throw message instead.

> **Documented Copilot DLP limitations (read before relying on this control):** In the **Microsoft 365 Copilot and Copilot Chat** location, sensitive information type (SIT) enforcement evaluates **the text a user types into the prompt**. The two documented SIT actions are **Prevent Copilot from processing content > Processing prompts** and **> Performing Web Searches**. Microsoft does not document a DLP action that inspects or blocks the text of a **generated Copilot response**; sensitive data in responses can be *observed* after the fact (DSPM / Activity explorer **AI activities**, Audit, eDiscovery) but is not blocked by this control. DLP also can't scan the contents of files uploaded directly into a prompt — only typed prompt text is checked. SIT-based prompt blocking is in preview and rolling out. The sensitivity label condition covers emails sent on or after January 1, 2025; calendar invites and Admin units are not supported. Policy updates can take up to four hours to take effect in the Copilot experience.

### Test 2: Information Barrier Enforcement

- **Objective:** Confirm that information barriers prevent Copilot from surfacing NPI across business unit boundaries
- **Steps:**
  1. Create test documents containing consumer financial data in a restricted segment's SharePoint site.
  2. Have a user from a different segment use Copilot to search for or reference that content.
  3. Verify that Copilot does not surface the restricted content in its responses.
- **Expected Result:** Information barriers prevent cross-segment NPI exposure through Copilot.
- **Evidence:** Copilot response showing no restricted content surfaced.

### Test 3: Sensitivity Label Protection for NPI Documents

- **Objective:** Validate that documents containing NPI are protected with appropriate sensitivity labels
- **Steps:**
  1. Create a document containing consumer financial data.
  2. Apply or verify auto-application of the appropriate sensitivity label.
  3. Confirm the label enforces encryption and access restrictions.
  4. Test that Copilot interactions with the document respect label protections.
- **Expected Result:** NPI documents are labeled, encrypted, and Copilot respects label-based access controls.
- **Evidence:** Document properties showing label and encryption status.

### Test 4: Incident Response Program Verification (Rule 248.30(a)(4))

- **Objective:** Verify that the written incident response program covers Copilot-related NPI incidents and includes the required notification procedures
- **Steps:**
  1. Review the firm's written incident response program (IRP) for Copilot NPI coverage.
  2. Confirm the IRP is written (not informal) and includes: Copilot-specific incident scenarios, severity classification, escalation paths, containment steps, and notification procedures.
  3. Verify the 72-hour Microsoft notification procedure is documented (SEC Rule 248.30(a)(3)): confirm Microsoft notification channel, contact information, and notification template are accessible.
  4. Verify the 30-day customer notification timeline is documented.
  5. Confirm a named individual is responsible for executing the Microsoft notification within the 72-hour window.
- **Expected Result:** Written IRP exists, covers Copilot scenarios, and documents both the 72-hour vendor notification and 30-day customer notification procedures.
- **Evidence:** IRP document with Copilot section; 72-hour notification procedure documentation; responsible party assignment.

### Test 5: Incident Response Simulation — NPI Exposure via Copilot

- **Objective:** Simulate a Copilot NPI exposure event to test the incident response program and verify the 72-hour notification window is achievable
- **Steps:**
  1. Run a tabletop exercise scenario: "Copilot Chat surfaced client account numbers to a user without appropriate permissions due to a permission misconfiguration. The exposure was detected via a DLP alert."
  2. Walk through the IRP steps: detection confirmation → severity classification → internal escalation (4 hours) → executive notification (24 hours) → Microsoft notification preparation (72-hour deadline).
  3. Time the exercise — confirm that the 72-hour notification to Microsoft could be executed within the required window.
  4. Identify any gaps in the notification chain (e.g., unavailable contacts, missing notification templates).
  5. Document exercise outcomes and any remediation items.
- **Expected Result:** Tabletop exercise completed with documented outcome; notification chain is achievable within the 72-hour and 30-day windows; gaps identified and assigned for remediation.
- **Evidence:** Exercise facilitation notes and outcome documentation; gap remediation log.

### Test 6: Privacy Incident Response Alert Workflow

- **Objective:** Verify that NPI-related DLP rule matches produce the alert and email notification the control promises, and that the alert can be investigated end to end
- **Steps:**
  1. Confirm the alert is defined **on the rule**: in Microsoft Purview > Data loss prevention > Policies > FSI-RegSP-Copilot-Privacy-Protection, open each rule and confirm the **Incident reports** section shows the alert toggle on, the expected severity level (Medium / High), and the Privacy Officer plus compliance team as email alert recipients. The PowerShell equivalent is the `GenerateAlert`, `GenerateIncidentReport`, and `ReportSeverityLevel` check in Test 1.
  2. Trigger a DLP rule match by typing consumer financial test data into a Copilot prompt (test environment).
  3. Verify the alert appears on the DLP Alerts dashboard (Microsoft Purview > Data loss prevention > Alerts).
  4. Confirm the compliance team and Privacy Officer received the alert email generated by the rule.
  5. Cross-check the match in Activity explorer **AI activities** (Workload `Copilot`, activity `DLPRuleMatch` / `DLPRuleEnforce`) and confirm the `PolicyName` and `RuleName` match the expected rule.
  6. Walk through the incident investigation and resolution process in Purview.
- **Expected Result:** The rule's own alert configuration produces a dashboard alert and an email to the configured recipients; the match is visible in Activity explorer with the expected policy and rule names.
- **Evidence:** Screenshot of the rule's **Incident reports** configuration; DLP alert detail; notification email header (redacted); Activity explorer export row.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| DLP policy and rule configuration (including Incident reports) | Purview portal | Screenshot | With control documentation |
| Fail-closed policy verification output | Security & Compliance PowerShell transcript | Text | With control documentation |
| Copilot interaction audit records (metadata) | Unified audit log (`RecordType CopilotInteraction`) | CSV export | 7 years |
| Copilot DLP rule-match records | Activity explorer / DSPM **AI activities** (`Export-ActivityExplorerData`) | JSON or CSV export | 7 years |
| DLP alerts | Purview > Data loss prevention > Alerts | Screenshot / export | 7 years |
| Information barrier test results | Copilot response | Screenshot | With control documentation |
| Privacy impact assessment | Assessment document | PDF | 7 years |
| Written IRP with Copilot section | IRP document | PDF | 7 years (updated annually) |
| 72-hour notification procedure | IRP or standalone document | PDF | 7 years |
| Tabletop exercise documentation | Exercise records | PDF | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SEC Reg S-P Rule 248.30(a)(3) | 72-hour vendor notification for unauthorized NPI access | Test 4 and 5 verify documented procedure and achievable window |
| SEC Reg S-P Rule 248.30(a)(4) | Written incident response program | Test 4 verifies existence and completeness of written IRP |
| SEC Reg S-P Rule 30 | Safeguard customer records | Supports compliance with NPI safeguarding in AI interactions |
| GLBA Title V | Financial privacy | Helps meet privacy requirements for consumer financial information |
| GLBA §501(b) | Safeguards provision for NPI | Supports requirements for protecting customer information at banks and broker-dealers (statutory basis for SEC Reg S-P safeguards; the FTC Safeguards Rule is a separate implementing regulation outside SEC jurisdiction) |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for privacy control issues
- Proceed to [Control 3.11](../3.11/portal-walkthrough.md) for record keeping compliance
- Back to [Control 3.10](../../../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md)
