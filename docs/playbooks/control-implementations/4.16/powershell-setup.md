# Control 4.16: Microsoft Scout Governance - PowerShell Setup

Automation workflow for reconciling the three Scout admin gates, capturing Intune endpoint-policy assignment as evidence, inspecting Windows ADMX policy on managed devices, pulling the subset of Scout-related activity visible to Purview audit, and packaging preview-governance evidence. Scout configuration itself is managed through the Microsoft 365 admin center, Intune, and GitHub — this playbook focuses on evidence collection.

## Prerequisites

- PowerShell 7+
- `Microsoft.Graph` (permissions: `DeviceManagementConfiguration.Read.All`, `DeviceManagementApps.Read.All`, `Group.Read.All`) for Intune device-configuration inspection and group reconciliation
- `ExchangeOnlineManagement` for unified-audit-log queries (Scout-related admin events flow through admin-agent management operations)
- On the local Windows device being sampled: rights to read `HKLM` policy hives
- M365 Global Reader (or equivalent least-privilege read role) for the tenant surfaces
- GitHub administrator access to the linked GitHub organization or enterprise for entitlement reconciliation (out-of-band; use the GitHub UI or `gh` CLI — no PowerShell module invocation is included here)
- Approved evidence-retention path
- A documented record of the approved pilot group, endpoint-policy assignment target, and GitHub Copilot entitlement list

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

### Script 4: Inspect the local Windows ADMX-backed policy value on a sampled device

Read-only inspection. The Scout Windows ADMX is documented to expose `AllowScoutFrontierAccess`. Registry paths for policy-backed settings resolve under the `HKLM\SOFTWARE\Policies` hive; the exact subkey should be verified against the current Scout ADMX. Do not write to policy hives from this playbook.

```powershell
# Adjust the subkey path to match the Scout ADMX namespace verified from current Microsoft docs.
$candidates = @(
  'HKLM:\SOFTWARE\Policies\Scout'
)

$found = @()
foreach ($path in $candidates) {
  if (Test-Path $path) {
    $found += Get-ItemProperty -Path $path |
      Select-Object PSPath,
        @{n='AllowScoutFrontierAccess';e={ $_.AllowScoutFrontierAccess }}
  }
}

if (-not $found) {
  Write-Warning 'No Scout policy key found under the sampled paths. Verify the ADMX namespace in current Microsoft documentation and update this script.'
}

$found | Export-Csv .\artifacts\4.16\scout-local-policy-sample.csv -NoTypeInformation
```

> On macOS, evidence for the equivalent profile is captured with `profiles show -type configuration` and by exporting the deployed `.mobileconfig` from Intune. Both are out-of-band relative to this PowerShell workflow.

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
| Intune policy + assignment export | Monthly | Confirms endpoint policy stays scoped to the approved pilot device group |
| Local ADMX policy spot-check | Monthly (rotating device sample) | Confirms the policy actually applied on managed devices; verify ADMX namespace against current docs |
| GitHub Copilot entitlement reconciliation | Monthly | Out-of-band from GitHub administration; documents the third gate |
| Admin-attestation record review | Quarterly | Confirms the attestation gate remains valid and named admins are still authorized |
| MCP-server inventory review | Monthly | Confirms configured MCP servers match the approved inventory |
| Permission-mode review | Monthly | Confirms shell default posture, autonomous-mode posture, and unattended-automation posture match the approved decisions |
| M365 audit pull (Scout subset) | Weekly | Aligns with the pilot supervisory review cadence |
| Preview-change review | As released | Re-assesses each gate when Microsoft updates the Scout preview |
| Evidence-gap manifest refresh | Quarterly | Confirms the documented list of unsupported platform evidence remains current |

## Next Steps

- Continue to [Verification & Testing](verification-testing.md) for gate, permission, MCP, and boundary-coverage validation.
- Reference [Troubleshooting](troubleshooting.md) for entitlement, endpoint-policy, attestation, MCP, and boundary-related issues.

*FSI Copilot Governance Framework — Control 4.16 (Microsoft Scout, Frontier preview) · Last Verified 2026-07-10*
- Back to [Control 4.16](../../../controls/pillar-4-operations/4.16-microsoft-scout-governance.md)
