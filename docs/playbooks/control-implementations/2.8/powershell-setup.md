# Control 2.8: Encryption (Data in Transit and at Rest) — PowerShell Setup

Automation scripts for verifying and monitoring encryption controls.

## Prerequisites

- Exchange Online Management module
- Security & Compliance PowerShell
- Global Reader or Security Administrator role

## Scripts

### Script 1: TLS Enforcement Verification

```powershell
# Verify TLS configuration for Exchange Online
# Requires: Exchange Online Management

Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline

$connectors = Get-InboundConnector
$outConnectors = Get-OutboundConnector

Write-Host "=== TLS Enforcement Status ==="
Write-Host "`nInbound Connectors:"
foreach ($conn in $connectors) {
    Write-Host "  $($conn.Name): RequireTls=$($conn.RequireTls) TlsSenderCertificateName=$($conn.TlsSenderCertificateName)"
}

Write-Host "`nOutbound Connectors:"
foreach ($conn in $outConnectors) {
    Write-Host "  $($conn.Name): TlsSettings=$($conn.TlsSettings) TlsDomain=$($conn.TlsDomain)"
}

# Check organization-level TLS
$orgConfig = Get-TransportConfig
Write-Host "`nOrganization TLS: TLSReceiveDomainSecureList=$($orgConfig.TLSReceiveDomainSecureList)"
```

### Script 2: Customer Key Status Check

```powershell
# Check Customer Key deployment status
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline

$deks = Get-DataEncryptionPolicy -ErrorAction SilentlyContinue

if ($deks) {
    Write-Host "=== Customer Key Status ==="
    foreach ($dek in $deks) {
        Write-Host "Policy: $($dek.Name)"
        Write-Host "  State: $($dek.State)"
        Write-Host "  Enabled: $($dek.Enabled)"
        Write-Host "  KeyVaultUrl1: $($dek.AzureKeyVaultUrl1)"
        Write-Host "  KeyVaultUrl2: $($dek.AzureKeyVaultUrl2)"
        Write-Host ""
    }
} else {
    Write-Host "Customer Key: Not configured (using Microsoft-managed keys)"
}
```

### Script 3: Encryption-Enabled Label Inventory

```powershell
# Inventory sensitivity labels with encryption settings
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$labels = Get-Label | Where-Object { $_.EncryptionEnabled -eq $true }

$encLabels = @()
foreach ($label in $labels) {
    $encLabels += [PSCustomObject]@{
        DisplayName        = $label.DisplayName
        Priority           = $label.Priority
        EncryptionEnabled  = $label.EncryptionEnabled
        EncryptionProtectionType = $label.EncryptionProtectionType
        EncryptionContentExpiredOnDateInDaysOrNever = $label.EncryptionContentExpiredOnDateInDaysOrNever
    }
}

Write-Host "=== Encryption-Enabled Labels ==="
Write-Host "Total labels with encryption: $($encLabels.Count)"
$encLabels | Format-Table DisplayName, Priority, EncryptionProtectionType -AutoSize
$encLabels | Export-Csv "EncryptionLabels_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| TLS Enforcement Check | Monthly | Verify TLS configuration integrity |
| Customer Key Health | Weekly | Monitor key vault and DEP status |
| Encryption Label Audit | Quarterly | Review encryption label configuration |

## Next Steps

- See [Verification & Testing](verification-testing.md) for encryption validation
- See [Troubleshooting](troubleshooting.md) for encryption issues
- Back to [Control 2.8](../../../controls/pillar-2-security/2.8-encryption.md)
