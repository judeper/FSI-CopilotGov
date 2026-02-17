# Control 2.15: Network Security and Private Connectivity — PowerShell Setup

Automation scripts for verifying and monitoring network security for Copilot connectivity.

## Prerequisites

- Microsoft Graph PowerShell SDK
- Azure PowerShell module (for Private Link verification)
- Network Administrator role

## Scripts

### Script 1: Microsoft 365 Endpoint Connectivity Test

```powershell
# Test connectivity to critical Microsoft 365 Copilot endpoints
# Requires: Network access from the test machine

$endpoints = @(
    @{ Name = "SharePoint Online"; URL = "<tenant>.sharepoint.com"; Port = 443 },
    @{ Name = "Exchange Online"; URL = "outlook.office365.com"; Port = 443 },
    @{ Name = "Teams"; URL = "teams.microsoft.com"; Port = 443 },
    @{ Name = "Graph API"; URL = "graph.microsoft.com"; Port = 443 },
    @{ Name = "Copilot Service"; URL = "substrate.office.com"; Port = 443 }
)

$results = @()
foreach ($ep in $endpoints) {
    $test = Test-NetConnection -ComputerName $ep.URL -Port $ep.Port -WarningAction SilentlyContinue
    $results += [PSCustomObject]@{
        Endpoint     = $ep.Name
        URL          = $ep.URL
        Port         = $ep.Port
        Reachable    = $test.TcpTestSucceeded
        LatencyMs    = $test.PingReplyDetails.RoundtripTime
        RemoteAddress = $test.RemoteAddress
    }
}

Write-Host "=== M365 Copilot Endpoint Connectivity ==="
$results | Format-Table Endpoint, Reachable, LatencyMs -AutoSize
$results | Export-Csv "EndpointConnectivity_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation

$failures = ($results | Where-Object { -not $_.Reachable }).Count
if ($failures -gt 0) {
    Write-Host "WARNING: $failures endpoints unreachable!" -ForegroundColor Red
}
```

### Script 2: Azure Private Link Status Check

```powershell
# Verify Azure Private Link configuration for M365 (if deployed)
# Requires: Azure PowerShell module

Import-Module Az.Network
Connect-AzAccount

$privateEndpoints = Get-AzPrivateEndpoint | Where-Object {
    $_.PrivateLinkServiceConnections.GroupIds -match "sharePoint|exchange"
}

if ($privateEndpoints.Count -gt 0) {
    Write-Host "=== Azure Private Link Status ==="
    foreach ($pe in $privateEndpoints) {
        Write-Host "Name: $($pe.Name)"
        Write-Host "  Status: $($pe.ProvisioningState)"
        Write-Host "  Subnet: $($pe.Subnet.Id)"
        Write-Host "  Connection: $($pe.PrivateLinkServiceConnections.PrivateLinkServiceConnectionState.Status)"
        Write-Host ""
    }
} else {
    Write-Host "No Azure Private Link endpoints configured for Microsoft 365."
    Write-Host "Private Link is optional but recommended for regulated FSI environments."
}
```

### Script 3: Named Location Configuration Audit

```powershell
# Audit Conditional Access named locations for network security
Import-Module Microsoft.Graph.Identity.SignIns
Connect-MgGraph -Scopes "Policy.Read.All"

$locations = Get-MgIdentityConditionalAccessNamedLocation
$locationReport = @()

foreach ($loc in $locations) {
    $type = $loc.AdditionalProperties["@odata.type"]
    $trusted = $loc.AdditionalProperties["isTrusted"]
    $locationReport += [PSCustomObject]@{
        Name      = $loc.DisplayName
        Type      = $type
        IsTrusted = $trusted
        Created   = $loc.CreatedDateTime
        Modified  = $loc.ModifiedDateTime
    }
}

Write-Host "=== Named Locations for Network Security ==="
$locationReport | Format-Table Name, Type, IsTrusted -AutoSize
$locationReport | Export-Csv "NamedLocations_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Endpoint Connectivity Test | Daily | Verify Copilot endpoint accessibility |
| Private Link Status Check | Weekly | Monitor Private Link health |
| Named Location Audit | Quarterly | Verify network location definitions |

## Next Steps

- See [Verification & Testing](verification-testing.md) for network validation
- See [Troubleshooting](troubleshooting.md) for network issues
