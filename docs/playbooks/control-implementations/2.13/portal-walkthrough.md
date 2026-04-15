# Control 2.13: Plugin and Graph Connector Security — Portal Walkthrough

Step-by-step portal configuration for securing Copilot plugins and Microsoft Graph connectors.

## Prerequisites

- Teams Administrator and Entra Global Admin roles
- Microsoft 365 Admin Center and Teams Admin Center access
- Plugin security review process approved by governance committee

## Steps

### Step 1: Inventory Active Plugins and Connectors

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Agents > All agents and Settings > Integrated apps

Review all active Copilot extensions including Microsoft first-party plugins, third-party plugins, and custom-built plugins. Document each plugin's data access scope, publisher, and certification status.

### Step 2: Configure Plugin Permission Policies

**Portal:** Microsoft Teams Admin Center
**Path:** Teams Admin > Teams Apps > Permission Policies

Create restrictive permission policies for Copilot plugins:
- Block all third-party apps by default
- Create an allowlist of approved plugins
- Assign the restrictive policy to all Copilot users
- Create a separate policy for the IT team to evaluate new plugins

### Step 3: Review Graph Connector Security

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Settings > Search & Intelligence > Data Sources

For each active Graph connector, review security:
- Authentication method (certificate, secret, managed identity)
- Data ingestion permissions and scope
- Access control list (ACL) mapping for ingested content
- Data refresh schedule and error handling

### Step 4: Configure Consent and Approval Workflows

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Enterprise Applications > Consent and Permissions

Configure app consent policies to control how plugins request permissions:
- Disable user consent for new applications
- Require admin consent for all plugin permission requests
- Set up admin consent workflow for user requests

### Step 5: Document Plugin Security Standards

Create plugin security standards document covering:
- Required security certifications for approved plugins
- Data access review requirements before approval
- Plugin testing procedures (security scan, data flow analysis)
- Periodic review cadence for approved plugins

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Block all third-party plugins; admin consent required; document approved list |
| **Recommended** | Security review process for new plugins; Graph connector ACL verification; quarterly plugin review |
| **Regulated** | Formal plugin security assessment per OWASP; third-party security certification required; monthly review with governance approval |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for plugin management automation
- See [Verification & Testing](verification-testing.md) to validate plugin security
- Review Control 1.13 for Extensibility Readiness
- Back to [Control 2.13](../../../controls/pillar-2-security/2.13-plugin-connector-security.md)
