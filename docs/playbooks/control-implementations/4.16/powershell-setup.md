# Control 4.16: Microsoft Scout Governance - PowerShell Setup

Automation workflow for reconciling the three Scout admin gates, capturing Intune endpoint-policy assignment as evidence, inspecting Windows ADMX policy on managed devices, pulling the subset of Scout-related activity visible to Purview audit, and packaging preview-governance evidence. Scout configuration itself is managed through the Microsoft 365 admin center, Intune, and GitHub — this playbook focuses on evidence collection.

## Prerequisites

- PowerShell 7+
- `Microsoft.Graph` (permissions: `DeviceManagementConfiguration.Read.All`, `DeviceManagementApps.Read.All`, `Group.Read.All`, `User.Read.All`, `Directory.Read.All`) for Intune device-configuration inspection, group reconciliation, and Microsoft 365 Copilot license assignment reads
- `ExchangeOnlineManagement` for unified-audit-log queries (Scout-related admin events flow through admin-agent management operations)
- On the local Windows device being sampled: rights to read `HKLM` policy hives
- M365 Global Reader (or equivalent least-privilege read role) for the tenant surfaces
- GitHub administrator access to the linked GitHub organization or enterprise for entitlement reconciliation (out-of-band; use the GitHub UI or `gh` CLI — no PowerShell module invocation is included here)
- Approved evidence-retention path
- A documented record of the approved pilot group, endpoint-policy assignment target, and the two per-user license prerequisites (active Microsoft 365 Copilot license per Control 1.9, GitHub Copilot Business or Enterprise entitlement)

> **Important:** Scout is a Frontier preview capability with **no dedicated Scout PowerShell service module**. Do not rely on invented or undocumented Scout-specific cmdlets. Validate configuration in the Microsoft 365 admin center, Intune, and GitHub UIs and reconcile results with the evidence pulled below. Re-verify audit operation names and Intune configuration schemas against current Microsoft documentation before treating output as evidence.

## Script Flow

### Script 1: Inventory Intune device configuration profiles that carry Scout policy

The Windows Scout policy is deployed as an imported ADMX / group-policy configuration; the macOS Scout policy is deployed as a custom device configuration profile using a `.mobileconfig`. Both are visible through Microsoft Graph device-management endpoints.

```powershell
Connect-MgGraph -Scopes 'DeviceManagementConfiguration.Read.All','Group.Read.All' -NoWelcome

# Windows imported ADMX / group policy configurations
$gpConfigs = Get-MgDeviceManagementGroupPolicyConfiguration -All |
  Select-Object Id, DisplayName, Description, CreatedDateTime, LastModifiedDateTime

$gpConfigs |
  Where-Object { $_.DisplayName -match 'Scout' -or $_.Description -match 'Scout' } |
  Export-Csv .\artifacts\4.16\scout-intune-windows-policies.csv -NoTypeInformation

# macOS custom configuration profiles (and any other device configurations)
# Filter server-side to reduce payload
$macConfigs = Get-MgDeviceManagementDeviceConfiguration -All |
  Where-Object { $_.DisplayName -match 'Scout' -or $_.Description -match 'Scout' } |
  Select-Object Id, DisplayName, Description,
    @{n='Type';e={ $_.AdditionalProperties.'@odata.type' }},
    CreatedDateTime, LastModifiedDateTime

$macConfigs | Export-Csv .\artifacts\4.16\scout-intune-macos-profiles.csv -NoTypeInformation
```

### Script 2: Capture assignment scope for each Scout policy

Confirms that Scout endpoint policy is targeted only to the approved pilot device group.

```powershell
$targets = @()

foreach ($cfg in (Import-Csv .\artifacts\4.16\scout-intune-windows-policies.csv)) {
  $assignments = Get-MgDeviceManagementGroupPolicyConfigurationAssignment `
    -GroupPolicyConfigurationId $cfg.Id -All
  foreach ($a in $assignments) {
    $targets += [pscustomobject]@{
      PolicyType   = 'Windows (GroupPolicyConfiguration)'
      PolicyId     = $cfg.Id
      PolicyName   = $cfg.DisplayName
      TargetType   = $a.Target.AdditionalProperties.'@odata.type'
      TargetGroup  = $a.Target.AdditionalProperties.groupId
    }
  }
}

foreach ($cfg in (Import-Csv .\artifacts\4.16\scout-intune-macos-profiles.csv)) {
  $assignments = Get-MgDeviceManagementDeviceConfigurationAssignment `
    -DeviceConfigurationId $cfg.Id -All
  foreach ($a in $assignments) {
    $targets += [pscustomobject]@{
      PolicyType   = 'macOS (DeviceConfiguration)'
      PolicyId     = $cfg.Id
      PolicyName   = $cfg.DisplayName
      TargetType   = $a.Target.AdditionalProperties.'@odata.type'
      TargetGroup  = $a.Target.AdditionalProperties.groupId
    }
  }
}

$targets | Export-Csv .\artifacts\4.16\scout-intune-assignments.csv -NoTypeInformation
```

### Script 3: Reconcile endpoint-policy assignment against the approved pilot group

```powershell
# Source approved group from the documented decision
$approvedGroupId = (Import-Csv .\config\scout-pilot-decision.csv).ApprovedDeviceGroupId |
  Select-Object -First 1

$assignments = Import-Csv .\artifacts\4.16\scout-intune-assignments.csv
$outOfScope  = $assignments | Where-Object { $_.TargetGroup -and $_.TargetGroup -ne $approvedGroupId }

$outOfScope | Export-Csv .\artifacts\4.16\scout-intune-out-of-scope-assignments.csv -NoTypeInformation
```

### Script 4: Inspect the local Windows ADMX-backed policy values on a sampled device

Read-only inspection. Microsoft's [Manage admin controls in Intune for Microsoft Scout](https://learn.microsoft.com/microsoft-scout/manage-group-policy) documents the Scout Windows ADMX policy as device-scoped and stored under `HKLM\SOFTWARE\Policies\Scout`. The **Allow Microsoft Scout Frontier access** capability (from [Set up Microsoft Scout with Intune](https://learn.microsoft.com/microsoft-scout/admin-intune-setup)) is the sign-in gate; the other documented values give admins policy-level control over MCP servers, permission types, models, providers, Heartbeat, Automations, workspace scoping, browser egress, and forced approval prompts. Verify names against the current article before treating output as evidence. Do not write to policy hives from this playbook.

```powershell
# Documented ADMX admin controls under HKLM\SOFTWARE\Policies\Scout.
# Verify names/types against current Microsoft documentation before treating as evidence:
#   https://learn.microsoft.com/microsoft-scout/manage-group-policy
$scoutPolicyPath = 'HKLM:\SOFTWARE\Policies\Scout'
$scoutDwordValues = @(
  'PolicyVersion',
  'ForcePrompt',
  'DisableHeartbeat',
  'DisableWorkflows',
  'RestrictToWorkspace'
)
$scoutStringValues = @(
  'DisabledServers',
  'DisabledPermissions',
  'DisabledModels',
  'DisabledProviders',
  'BrowserEgressBlockedOrigins'
)

# Frontier-access ADMX capability from admin-intune-setup (sign-in gate).
$frontierValue = 'AllowScoutFrontierAccess'

$sample = [ordered]@{
  PSPath                    = $scoutPolicyPath
  KeyPresent                = (Test-Path $scoutPolicyPath)
  $frontierValue            = $null
}
foreach ($v in ($scoutDwordValues + $scoutStringValues)) { $sample[$v] = $null }

if ($sample.KeyPresent) {
  $props = Get-ItemProperty -Path $scoutPolicyPath -ErrorAction SilentlyContinue
  foreach ($name in @($frontierValue) + $scoutDwordValues + $scoutStringValues) {
    if ($props.PSObject.Properties.Name -contains $name) {
      $sample[$name] = $props.$name
    }
  }
} else {
  Write-Warning 'No Scout policy key found at HKLM\SOFTWARE\Policies\Scout. Verify the ADMX namespace and settings in current Microsoft documentation and update this script.'
}

[pscustomobject]$sample |
  Export-Csv .\artifacts\4.16\scout-local-policy-sample.csv -NoTypeInformation
```

> On macOS, evidence for the equivalent profile is captured with `profiles show -type configuration` and by exporting the deployed `.mobileconfig` from Intune. Where an equivalent macOS payload key exists for any of the Windows ADMX admin controls above, confirm the specific key against current Microsoft documentation before treating output as evidence. Both are out-of-band relative to this PowerShell workflow.

### Script 4b: Reconcile pilot users against active Microsoft 365 Copilot license assignment

Microsoft's [Get started with Microsoft Scout](https://learn.microsoft.com/microsoft-scout/get-started) lists an active Microsoft 365 Copilot license as a per-user prerequisite. Reconcile pilot users against license assignment (also relevant to [Control 1.9](../../../controls/pillar-1-readiness/1.9-license-planning.md)).

```powershell
Connect-MgGraph -Scopes 'User.Read.All','Directory.Read.All','Group.Read.All' -NoWelcome

# Substitute the current Microsoft 365 Copilot license SKU part number from your tenant.
# Verify against the current Microsoft 365 Copilot licensing documentation before use.
$copilotSkuPartNumber = 'Microsoft_365_Copilot'
$copilotSku = Get-MgSubscribedSku -All |
  Where-Object { $_.SkuPartNumber -eq $copilotSkuPartNumber }

if (-not $copilotSku) {
  Write-Warning "SKU '$copilotSkuPartNumber' not found in Get-MgSubscribedSku. Verify the Copilot SKU part number in the Microsoft 365 admin center and update this script."
}

$approvedPilotGroupId = (Import-Csv .\config\scout-pilot-decision.csv).ApprovedUserGroupId |
  Select-Object -First 1

$pilotUsers = Get-MgGroupMember -GroupId $approvedPilotGroupId -All

$licenseReport = foreach ($m in $pilotUsers) {
  $u = Get-MgUser -UserId $m.Id -Property 'id,userPrincipalName,assignedLicenses'
  [pscustomobject]@{
    UserPrincipalName    = $u.UserPrincipalName
    UserId               = $u.Id
    HasM365CopilotLicense = if ($copilotSku) {
      [bool]($u.AssignedLicenses | Where-Object { $_.SkuId -eq $copilotSku.SkuId })
    } else { 'Unknown' }
  }
}

$licenseReport |
  Export-Csv .\artifacts\4.16\scout-m365-copilot-license-reconciliation.csv -NoTypeInformation
```

### Script 5: Pull the subset of Scout-related activity visible to Purview audit

Scout activity that flows through M365 (for example, Copilot admin surfaces or Frontier-related admin events) is visible through the unified audit log; local shell execution, MCP output, automation instructions, and third-party inference are **not** captured by Purview and must be sourced from endpoint tooling (out of scope of this script).

```powershell
Connect-ExchangeOnline -ShowBanner:$false

$start = (Get-Date).AddDays(-30)
$end   = Get-Date

# Admin-agent management operations — verify against current audit-log activity reference.
$agentOperations = @(
  'DeployedAgent',
  'RemovedAgent',
  'UpdatedAgent'
)

Search-UnifiedAuditLog -StartDate $start -EndDate $end `
  -Operations $agentOperations `
  -ResultSize 5000 |
  Where-Object { $_.AuditData -match 'Scout' -or $_.AuditData -match 'Frontier' } |
  Export-Csv .\artifacts\4.16\scout-m365-audit-subset.csv -NoTypeInformation
```

### Script 6: Package evidence and record known unsupported coverage

```powershell
# Record a manifest of Scout evidence gaps that this collection intentionally does not cover.
@'
Scout evidence gaps (Frontier preview):
- Local shell command execution logs — sourced from endpoint tooling, not Purview.
- Automation instructions stored on the endpoint — outside the M365 DPA.
- MCP server output stored on the endpoint — outside the M365 DPA.
- Third-party inference request/response content — outside M365 residency, retention, label enforcement, and eDiscovery.
- Sensitivity-label inheritance on Scout-generated or modified content — not reliably inherited.
GitHub Copilot Business/Enterprise entitlement reconciliation is captured out-of-band from the GitHub administration surface.
'@ | Set-Content -Encoding UTF8 .\artifacts\4.16\scout-evidence-gaps.txt

$stamp = Get-Date -Format 'yyyyMMdd-HHmm'
Compress-Archive -Path .\artifacts\4.16\* `
  -DestinationPath ".\artifacts\4.16\scout-governance-evidence-$stamp.zip"
```

## Operational Guidance

| Task | Cadence | Notes |
|------|---------|-------|
| Intune policy + assignment export | Monthly | Confirms endpoint policy (including documented ADMX admin controls under `HKLM\SOFTWARE\Policies\Scout`) stays scoped to the approved pilot device group |
| Local ADMX policy spot-check | Monthly (rotating device sample) | Confirms the **Allow Microsoft Scout Frontier access** capability and the documented admin controls actually applied on managed devices; verify names against current [Microsoft documentation](https://learn.microsoft.com/microsoft-scout/manage-group-policy) |
| Microsoft 365 Copilot license reconciliation | Monthly | Confirms pilot users hold an active Microsoft 365 Copilot license (per Control 1.9) — one of Scout's per-user prerequisites |
| GitHub Copilot entitlement reconciliation | Monthly | Out-of-band from GitHub administration; documents the GitHub Copilot Business/Enterprise entitlement gate |
| Admin-attestation record review | Quarterly | Confirms Microsoft's Frontier organization sign-up (attestation) gate remains valid and named admins are still authorized |
| Installation-privilege deployment review | Quarterly | Confirms the Scout installer deployment pattern (system-context managed deployment, just-in-time elevation, or documented exception) remains in force so end users are not granted standing local Administrator rights |
| MCP-server inventory review | Monthly | Confirms configured MCP servers match the approved inventory; where the ADMX `DisabledServers` setting is used, confirm the policy value matches the inventory decision |
| Permission-mode review | Monthly | Confirms shell default posture (with `ForcePrompt` where applied), autonomous-mode posture, and unattended-automation posture (with `DisableWorkflows` where applied) match the approved decisions |
| Provider/model exclusion review | Quarterly | Confirms `DisabledProviders` and `DisabledModels` ADMX values match the third-party inference exclusion decision |
| M365 audit pull (Scout subset) | Weekly | Aligns with the pilot supervisory review cadence |
| Preview-change review | As released | Re-assesses each gate — and the documented ADMX admin controls — when Microsoft updates the Scout preview |
| Evidence-gap manifest refresh | Quarterly | Confirms the documented list of unsupported platform evidence remains current |

## Next Steps

- Continue to [Verification & Testing](verification-testing.md) for gate, permission, MCP, and boundary-coverage validation.
- Reference [Troubleshooting](troubleshooting.md) for entitlement, endpoint-policy, attestation, MCP, and boundary-related issues.

*FSI Copilot Governance Framework — Control 4.16 (Microsoft Scout, Frontier preview) · Last Verified 2026-07-10*
- Back to [Control 4.16](../../../controls/pillar-4-operations/4.16-microsoft-scout-governance.md)
