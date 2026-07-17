# Control 4.5: Copilot Usage Analytics and Adoption Reporting — PowerShell Setup

Conservative automation for proving that Microsoft 365 Copilot usage-detail reporting is reachable and exportable from a live tenant.

## Verification Boundary (Read First)

This runbook verifies **access + exportability** of usage-detail records only. It does **not** establish:

- dashboard interpretation quality
- adoption effectiveness
- regulatory sufficiency by itself
- complete user coverage

## Current First-Party Microsoft Graph Surfaces

| Surface | Documented Endpoint / Cmdlet | Notes |
|---|---|---|
| Legacy Graph beta report API | `GET https://graph.microsoft.com/beta/reports/getMicrosoft365CopilotUsageUserDetail(period='D7')?$format=application/json` | Supports `$format` (`application/json` or `text/csv`), returns JSON (`200`) or CSV redirect (`302` + `Location`) |
| Copilot report root (beta) | `GET https://graph.microsoft.com/beta/copilot/reports/getMicrosoft365CopilotUsageUserDetail(period='D7',version='v1')` | Newer path segment; preview response is JSON (`200`) |
| Documented Graph PowerShell beta cmdlet | `Get-MgBetaReportMicrosoft365CopilotUsageUserDetail -Period D7 -Format application/json -OutFile <path>` | Module: `Microsoft.Graph.Beta.Reports` |

## Prerequisites

- **PowerShell:** 7.x
- **Modules:** `Microsoft.Graph.Authentication`, `Microsoft.Graph.Beta.Reports`
- **Permission support (per Microsoft Graph docs):**
  - Delegated (work/school): `Reports.Read.All`
  - Application: `Reports.Read.All`
  - Delegated personal Microsoft account: not supported
- **Delegated role requirement:** assign a supported Microsoft Entra admin role (for example: Company Administrator, AI Administrator, Exchange Administrator, SharePoint Administrator, Lync Administrator, Teams Service Administrator, Teams Communications Administrator, or Reports Reader).
- **Availability caveat:** this API is documented as available in Microsoft Graph global service only.

## Parameter and Behavior Notes

- `period` is required for this method.
- Supported period values on the legacy endpoint/cmdlet: `D7`, `D30`, `D90`, `D180`, `ALL`.
- No `date` parameter is documented for this usage-detail method; treat date-filter attempts as out of scope for Control 4.5 verification.
- Beta APIs are subject to change and are not supported for production applications.
- Unlicensed Copilot Chat usage data is not returned by this API.

## Script: Conservative Verification (Fail Closed)

```powershell
Import-Module Microsoft.Graph.Authentication
Import-Module Microsoft.Graph.Beta.Reports

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$period = 'D7'
$outFile = Join-Path $PWD ("copilot-usage-beta-{0}.json" -f (Get-Date -Format 'yyyyMMddHHmmss'))

Connect-MgGraph -Scopes 'Reports.Read.All'

try {
    Get-MgBetaReportMicrosoft365CopilotUsageUserDetail `
        -Period $period `
        -Format 'application/json' `
        -OutFile $outFile | Out-Null

    if (-not (Test-Path $outFile)) {
        throw "Fail closed: expected export file was not created."
    }

    $payload = Get-Content -Raw -Path $outFile | ConvertFrom-Json
    $records = @($payload.value)

    if ($records.Count -lt 1) {
        throw "Fail closed: API call succeeded but returned zero usage-detail records."
    }

    [PSCustomObject]@{
        Period = $period
        RecordCount = $records.Count
        ReportRefreshDate = $records[0].reportRefreshDate
        SampleUser = $records[0].userPrincipalName
        OutputFile = $outFile
    } | Format-List
}
catch {
    if ($_.Exception.Message -match '429|TooManyRequests|Retry-After') {
        throw "Fail closed: throttled by Microsoft Graph. Follow Retry-After guidance and rerun."
    }
    throw
}
finally {
    Disconnect-MgGraph -ErrorAction SilentlyContinue
}
```

## Optional REST Probe (CSV Redirect Behavior)

Use this only when you need explicit evidence of the documented `302` redirect behavior.

```powershell
Connect-MgGraph -Scopes 'Reports.Read.All'
Invoke-MgGraphRequest -Method GET `
  -Uri "https://graph.microsoft.com/beta/reports/getMicrosoft365CopilotUsageUserDetail(period='D7')?`$format=text/csv" `
  -SkipHttpErrorCheck
Disconnect-MgGraph
```

Expected behavior: `302 Found` with a short-lived preauthenticated URL in the `Location` header.

## Required Evidence Artifacts

- Command transcript (including period value and timestamp)
- Export artifact (`*.json` or `*.csv`)
- Record count result (`>=1` for pass)
- Permission/role evidence for the identity used
- Any throttling events and retry actions

## References

- [Graph beta: reportRoot getMicrosoft365CopilotUsageUserDetail](https://learn.microsoft.com/en-us/graph/api/reportroot-getmicrosoft365copilotusageuserdetail?view=graph-rest-beta)
- [Copilot report root API](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/admin-settings/reports/copilotreportroot-getmicrosoft365copilotusageuserdetail)
- [Get-MgBetaReportMicrosoft365CopilotUsageUserDetail](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.beta.reports/get-mgbetareportmicrosoft365copilotusageuserdetail?view=graph-powershell-beta)
- [Authorization for Microsoft 365 usage-report APIs](https://learn.microsoft.com/en-us/graph/reportroot-authorization)
- [Microsoft Graph throttling guidance](https://learn.microsoft.com/en-us/graph/throttling)

## Next Steps

- Run [Verification & Testing](verification-testing.md)
- See [Troubleshooting](troubleshooting.md) for common failures
- Back to [Control 4.5](../../../controls/pillar-4-operations/4.5-usage-analytics.md)
