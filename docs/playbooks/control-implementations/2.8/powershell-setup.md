# Control 2.8: Encryption (Data in Transit and at Rest) — PowerShell Setup

Use these procedures to collect **manual evidence** for Control 2.8. There is no Microsoft Graph tenant property that proves tenant-wide Microsoft 365 encryption. In particular, organization notification email or phone properties are not encryption evidence and must not be imported as such.

The procedures distinguish actual endpoint handshakes from connector configuration and Customer Key state. Each evidence item has a limited scope; retain that scope with the output.

## Prerequisites

- PowerShell 7 or later for the negotiated TLS handshake procedure.
- ExchangeOnlineManagement for Exchange connector and data encryption policy review.
- Az.Accounts and Az.KeyVault for Customer Key vault/HSM configuration review.
- `M365CustomerKeyOnboarding` for Customer Key Onboarding Service validation.
- Read access appropriate to each target. Customer Key operations run through Exchange Online PowerShell, and Azure review needs access to each stated subscription.

!!! warning "No fabricated tenant-wide result"
    A TCP reachability check and an application protocol preference do not show the protocol or cipher suite actually negotiated with a Microsoft 365 service. An Exchange connector export applies only to the connector's configured mail-flow path.

## Script 1: Capture actual negotiated TLS handshakes

This procedure performs a real TLS handshake, validates the server certificate using the platform defaults, and records the negotiated protocol and cipher suite. Select the endpoints from the organization’s approved Microsoft 365/Copilot endpoint inventory; the examples are representative HTTPS endpoints, not a declaration of universal service coverage.

```powershell
function Get-NegotiatedTlsEvidence {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$HostName,

        [ValidateRange(1, 65535)]
        [int]$Port = 443
    )

    $client = [System.Net.Sockets.TcpClient]::new()
    $ssl = $null
    $certificate = $null

    try {
        $client.Connect($HostName, $Port)
        # No permissive callback: certificate validation remains enabled.
        $ssl = [System.Net.Security.SslStream]::new($client.GetStream(), $false)
        $options = [System.Net.Security.SslClientAuthenticationOptions]::new()
        $options.TargetHost = $HostName
        # Ask the local TLS stack to negotiate normally, then record the result.
        $options.EnabledSslProtocols = [System.Security.Authentication.SslProtocols]::None
        $options.CertificateRevocationCheckMode = `
            [System.Security.Cryptography.X509Certificates.X509RevocationMode]::Online
        $ssl.AuthenticateAsClient($options)

        if ($ssl.SslProtocol -notin @(
            [System.Security.Authentication.SslProtocols]::Tls12,
            [System.Security.Authentication.SslProtocols]::Tls13
        )) {
            throw "Unexpected negotiated protocol: $($ssl.SslProtocol)"
        }

        $certificate = [System.Security.Cryptography.X509Certificates.X509Certificate2]::new(
            $ssl.RemoteCertificate
        )
        [pscustomobject]@{
            TimestampUtc          = [DateTime]::UtcNow.ToString('o')
            HostName              = $HostName
            Port                  = $Port
            NegotiatedProtocol    = $ssl.SslProtocol.ToString()
            NegotiatedCipherSuite = $ssl.NegotiatedCipherSuite.ToString()
            CertificateSubject    = $certificate.Subject
            CertificateIssuer     = $certificate.Issuer
            CertificateNotAfter   = $certificate.NotAfter.ToUniversalTime().ToString('o')
        }
    }
    finally {
        if ($null -ne $certificate) { $certificate.Dispose() }
        if ($null -ne $ssl) { $ssl.Dispose() }
        $client.Dispose()
    }
}

$targets = @(
    'www.office.com',
    'outlook.office365.com',
    'login.microsoftonline.com'
)

$results = foreach ($target in $targets) {
    Get-NegotiatedTlsEvidence -HostName $target
}

$evidencePath = Join-Path $HOME (
    'M365-TlsHandshake-{0}.json' -f (Get-Date -Format 'yyyyMMdd-HHmmss')
)
$results | ConvertTo-Json -Depth 3 | Set-Content -Path $evidencePath -Encoding utf8
$results | Format-Table -AutoSize
Write-Host "Saved negotiated handshake evidence to $evidencePath"
```

Record the endpoint list, client/network location, timestamp, protocol, cipher suite, and certificate result. A TLS 1.3 result demonstrates negotiated support for that endpoint and client at that time; a TLS 1.2 result remains valid baseline evidence and does not establish that TLS 1.3 is unavailable elsewhere.

## Script 2: Export narrowly scoped Exchange connector and SMTP AUTH evidence

Use this only if the tenant has partner, hybrid, forced-TLS, or mutual-TLS mail-flow connectors. It does not verify the TLS version of Microsoft 365 Copilot HTTPS traffic.

```powershell
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline

$connectorEvidence = [ordered]@{
    CollectedUtc = [DateTime]::UtcNow.ToString('o')
    LegacySmtpAuthTlsException = Get-TransportConfig |
        Select-Object AllowLegacyTLSClients
    InboundConnectors = @(
        Get-InboundConnector | Select-Object `
            Name, Enabled, ConnectorType, RequireTls, `
            TlsSenderCertificateName, SenderDomains
    )
    OutboundConnectors = @(
        Get-OutboundConnector | Select-Object `
            Name, Enabled, ConnectorType, TlsSettings, `
            TlsDomain, SmartHosts, UseMXRecord
    )
}

$connectorEvidence | ConvertTo-Json -Depth 6
```

`AllowLegacyTLSClients` is relevant only to the opt-in Exchange Online legacy SMTP AUTH endpoint. Document an approved exception and retirement plan if it is enabled; it is not evidence for general Microsoft 365 TLS policy.

## Script 3: Review Customer Key policy and onboarding state

Use Customer Key onboarding state for the applicable scenario rather than treating a Graph organization object as key-management evidence. `Validate` makes no environment changes; do not use `Enable` until the validation result is successful and the change is approved.

```powershell
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline

# DEP state is useful where a DEP is already deployed.
Get-DataEncryptionPolicy |
    Select-Object Name, State, DataEncryptionPolicyType, AzureKeyIDs |
    Format-List

# Review a retained Customer Key Onboarding Service request.
Import-Module M365CustomerKeyOnboarding
$request = Get-CustomerKeyOnboardingRequest `
    -OrganizationID '<tenant-guid>' `
    -RequestID '<onboarding-request-guid>'

$request | Format-List ID, CreatedDate, ValidationResult, EnablementResult
$request.PassedValidations
$request.FailedValidations
```

For Microsoft 365 Copilot interactions, the Multi-workload DEP (`MDEP`) is the Customer Key scenario documented to include those interactions. Use the workload-specific process for Exchange mailbox or SharePoint/OneDrive scenarios.

## Script 4: Provision and verify one Premium vault per paid subscription

This is a provisioning template, not a read-only evidence query. Run it only through the approved change process. It intentionally fails if the two entries reuse a subscription. A single subscription containing two vaults is not a compliant Customer Key pair.

```powershell
Import-Module Az.Accounts
Import-Module Az.KeyVault

$vaults = @(
    [pscustomobject]@{
        SubscriptionId = '<paid-subscription-1-guid>'
        ResourceGroup  = 'rg-customer-key-1'
        VaultName      = 'ckm365vault01'
        Location       = 'EastUS'
        KeyName        = 'm365-customer-key'
    },
    [pscustomobject]@{
        SubscriptionId = '<paid-subscription-2-guid>'
        ResourceGroup  = 'rg-customer-key-2'
        VaultName      = 'ckm365vault02'
        Location       = 'WestUS'
        KeyName        = 'm365-customer-key'
    }
)

if ($vaults.Count -ne 2 -or @($vaults.SubscriptionId | Select-Object -Unique).Count -ne 2) {
    throw 'Customer Key requires two distinct paid Azure subscriptions.'
}

foreach ($vaultSpec in $vaults) {
    Set-AzContext -SubscriptionId $vaultSpec.SubscriptionId | Out-Null
    if ((Get-AzContext).Subscription.Id -ne $vaultSpec.SubscriptionId) {
        throw "Could not select subscription $($vaultSpec.SubscriptionId)."
    }

    New-AzResourceGroup -Name $vaultSpec.ResourceGroup `
        -Location $vaultSpec.Location -Force | Out-Null
    New-AzKeyVault -Name $vaultSpec.VaultName `
        -ResourceGroupName $vaultSpec.ResourceGroup `
        -Location $vaultSpec.Location `
        -Sku Premium `
        -SoftDeleteRetentionInDays 90 `
        -EnablePurgeProtection | Out-Null
    Add-AzKeyVaultKey -VaultName $vaultSpec.VaultName `
        -Name $vaultSpec.KeyName -Destination HSM | Out-Null
}

# Collect the configuration evidence after provisioning.
$vaultEvidence = foreach ($vaultSpec in $vaults) {
    Set-AzContext -SubscriptionId $vaultSpec.SubscriptionId | Out-Null
    $vault = Get-AzKeyVault -VaultName $vaultSpec.VaultName
    $key = Get-AzKeyVaultKey -VaultName $vaultSpec.VaultName -Name $vaultSpec.KeyName

    [pscustomobject]@{
        SubscriptionId           = (Get-AzContext).Subscription.Id
        VaultName                = $vault.VaultName
        Sku                      = $vault.Sku.Name
        SoftDeleteRetentionDays  = $vault.SoftDeleteRetentionInDays
        PurgeProtectionEnabled   = $vault.EnablePurgeProtection
        KeyId                    = $key.Id
        KeyType                  = $key.Key.Kty
        KeyExpires               = $key.Expires
    }
}
$vaultEvidence | Format-List
```

Customer Key requires 90-day recovery configuration and purge protection for Azure Key Vault. Managed HSM has soft delete enabled by default but requires purge protection at creation. Use one Managed HSM per paid subscription when that configuration is selected. If Azure Key Vault is used for Multiple Workloads, Exchange, and SharePoint/OneDrive, create a separate vault pair for each workload scenario as Microsoft documents.

## Script 5: Inventory encrypted sensitivity labels

This inventory supports label review but does not prove a user’s effective EXTRACT rights or every Copilot surface outcome. Pair it with the test matrix in [Verification & Testing](verification-testing.md).

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$labels = Get-Label | Where-Object { $_.EncryptionEnabled -eq $true }
$labels |
    Select-Object DisplayName, Priority, EncryptionEnabled, `
        EncryptionProtectionType, EncryptionContentExpiredOnDateInDaysOrNever |
    Format-Table -AutoSize
```

## Review Cadence

| Evidence | Suggested cadence | Scope |
|---|---|---|
| Negotiated endpoint handshake | Monthly and after material endpoint/proxy changes | Representative approved endpoint/client pairs |
| Connector and SMTP AUTH exception export | Monthly and after connector changes | Configured Exchange mail-flow paths only |
| Customer Key policy/onboarding and key configuration | Weekly when deployed; after key changes | Applicable Customer Key scenario |
| Sensitivity-label scenario tests | Quarterly and after label/DLP/Edge/connector changes | Effective-user and source/surface behavior |

## Next Steps

- See [Verification & Testing](verification-testing.md) for expected evidence and exception tests.
- See [Troubleshooting](troubleshooting.md) for failed onboarding, TLS, and encryption-surface diagnostics.
- Back to [Control 2.8](../../../controls/pillar-2-security/2.8-encryption.md).
