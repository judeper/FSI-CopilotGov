# Control 1.15: SharePoint Permissions Drift Detection - PowerShell Setup

Automation workflow for capturing approved SharePoint permission baselines, detecting drift, and packaging reversion decisions for review.

## Prerequisites

- PowerShell 7+
- `PnP.PowerShell`
- `Microsoft.Graph`
- SharePoint Admin access and any Graph permissions your organization requires for alerting or reversion workflows
- Local checkout or reviewed copy of companion solution [17-sharepoint-permissions-drift](https://github.com/judeper/FSI-CopilotGov-Solutions/tree/main/solutions/17-sharepoint-permissions-drift)
- Approved baseline manifest and named approvers for the monitored sites

> **Important:** The companion solution is documentation-first. Validate credentials, notification routing, and reversion policy before production use.

## Script Flow

### Script 1: Validate configuration and prerequisites

```powershell
Set-Location C:\Repos\FSI-CopilotGov-Solutions\solutions\17-sharepoint-permissions-drift
pwsh .\scripts\Deploy-Solution.ps1 -ConfigurationTier regulated -TenantId <tenant-guid>
```

### Script 2: Capture the approved permissions baseline

```powershell
pwsh .\scripts\New-PermissionsBaseline.ps1 `
  -SiteUrls @("https://tenant.sharepoint.com/sites/wealth-advisory") `
  -OutputPath .\artifacts\baseline
```

### Script 3: Run the drift scan

```powershell
pwsh .\scripts\Invoke-DriftScan.ps1 `
  -BaselinePath .\artifacts\baseline `
  -OutputPath .\artifacts\drift
```

### Script 4: Package reversion or approval actions

```powershell
pwsh .\scripts\Invoke-DriftReversion.ps1 `
  -InputPath .\artifacts\drift\drift-report.json `
  -PolicyPath .\config\auto-revert-policy.json `
  -OutputPath .\artifacts\reversion
```

### Script 5: Export evidence

```powershell
pwsh .\scripts\Export-DriftEvidence.ps1 `
  -InputPath .\artifacts `
  -OutputPath .\artifacts\evidence
```

## Operational Guidance

| Task | Cadence | Notes |
|------|---------|-------|
| Baseline refresh | After approved structural change | Do not overwrite a baseline until the new state is approved |
| Drift scan | Monthly or more frequently for high-risk sites | Align to governance tier and change cadence |
| Evidence export | After each formal scan cycle | Keep with CAB, exception, or incident records |

## Next Steps

- Use [Verification & Testing](verification-testing.md) to confirm drift classification and evidence integrity.
- Keep [Troubleshooting](troubleshooting.md) available for baseline mismatches, alerting issues, and reversion problems.
- Pair recurring drift findings with access-recertification actions where appropriate.

*FSI Copilot Governance Framework v1.3 - April 2026*
