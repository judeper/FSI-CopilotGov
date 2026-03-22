# Control 1.14: Item-Level Permission Scanning - PowerShell Setup

Automation workflow for scanning uniquely permissioned SharePoint items and producing approval-gated remediation output.

## Prerequisites

- PowerShell 7+
- `PnP.PowerShell`
- `Microsoft.Graph`
- SharePoint Admin access to the target tenant
- Tenant-specific PnP app registration with the permissions your organization requires
- Local checkout or reviewed copy of companion solution [16-item-level-oversharing-scanner](https://github.com/judeper/FSI-CopilotGov-Solutions/tree/main/solutions/16-item-level-oversharing-scanner)

> **Important:** The companion solution is documentation-first. Validate tenant bindings, app registrations, and approval logic before production use.

## Script Flow

### Script 1: Validate configuration and generate a deployment manifest

```powershell
Set-Location C:\Repos\FSI-CopilotGov-Solutions\solutions\16-item-level-oversharing-scanner
pwsh .\scripts\Deploy-Solution.ps1 -ConfigurationTier recommended -TenantId <tenant-guid>
```

### Script 2: Enumerate item-level permissions

```powershell
pwsh .\scripts\Get-ItemLevelPermissions.ps1 `
  -SiteUrls @("https://tenant.sharepoint.com/sites/wealth-advisory") `
  -TenantUrl "https://tenant-admin.sharepoint.com" `
  -OutputPath .\artifacts\scan
```

### Script 3: Apply oversharing risk scoring

```powershell
pwsh .\scripts\Export-OversharedItems.ps1 `
  -InputPath .\artifacts\scan\item-permissions.csv `
  -OutputPath .\artifacts\scored
```

### Script 4: Generate approval-gated remediation actions

```powershell
pwsh .\scripts\Invoke-BulkRemediation.ps1 `
  -InputPath .\artifacts\scored\risk-scored-report.csv `
  -OutputPath .\artifacts\remediation `
  -TenantUrl "https://tenant-admin.sharepoint.com"
```

### Script 5: Export evidence

```powershell
pwsh .\scripts\Export-Evidence.ps1 -InputPath .\artifacts -OutputPath .\artifacts\evidence
```

## Operational Guidance

| Task | Cadence | Notes |
|------|---------|-------|
| Pilot scan | One-time per candidate site set | Start with a narrow scope to validate performance and false-positive rate |
| High-risk site scans | Monthly or more frequently | Align cadence to Control 1.2 and Control 1.15 monitoring |
| Evidence export | After each formal scan cycle | Store with the related approval records |

## Next Steps

- Use [Verification & Testing](verification-testing.md) to confirm the workflow is detecting the right items.
- Keep [Troubleshooting](troubleshooting.md) available for authentication, throttling, and scoring issues.
- Coordinate recurring scans with [Control 1.15: SharePoint Permissions Drift Detection](../../../controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md).

*FSI Copilot Governance Framework v1.2.1 - March 2026*
