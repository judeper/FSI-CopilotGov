# Control 4.13: Copilot Extensibility Governance (Plugin Lifecycle) — Portal Walkthrough

Step-by-step portal configuration for governing the lifecycle of Copilot plugins, Graph connectors, and declarative agents including approval, deployment, monitoring, and retirement.

## Prerequisites

- **Role:** Global Administrator, Teams Administrator
- **License:** Microsoft 365 E5 with Copilot add-on
- **Access:** Microsoft 365 Admin Center, Teams Admin Center

## Steps

### Step 1: Configure Integrated Apps Governance

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Integrated apps

1. Navigate to the Integrated apps settings.
2. Review the current list of deployed apps and plugins.
3. Configure the app governance settings:
   - **User consent settings** — Block user consent; require admin approval for all apps
   - **App catalog** — Curate the list of approved apps available to Copilot users
   - **Third-party app access** — Restrict to a pre-approved list for FSI environments
4. Document the approved plugin catalog with business justification for each.

### Step 2: Establish Plugin Approval Workflow

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Integrated apps > User requests

1. Enable the user request workflow for new app/plugin requests.
2. Configure the approval chain:
   - First-level: IT team reviews technical requirements and security posture
   - Second-level: Compliance team reviews regulatory and data protection impact
   - Third-level: Business owner confirms business justification
3. Set SLA for approval decisions (5 business days recommended).
4. Create a standardized Plugin Risk Assessment template.

### Step 3: Configure Copilot Plugin Access Controls

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Copilot > Plugins

1. Navigate to the Copilot plugin settings.
2. Configure plugin availability:
   - **First-party Microsoft plugins** — Enable approved plugins, disable non-essential ones
   - **Third-party plugins** — Block all or allow only from the approved list
   - **Custom plugins (line-of-business)** — Enable with governance controls
3. Set plugin access by user group (not all users need all plugins).
4. Document which plugins are approved and for which user groups.

### Step 4: Configure Graph Connector Governance

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Search & intelligence > Data sources

1. Review existing Microsoft Graph connectors.
2. Evaluate each connector for data sensitivity:
   - What data does the connector expose to Copilot?
   - Are there access control restrictions on the connected data?
   - Does the connector data include regulated content?
3. Apply sensitivity labels to Graph connector content where applicable.
4. Document the connector inventory with data classification and access controls.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| User consent for plugins | Allowed | Admin-only consent | Admin-only with compliance review |
| Third-party plugins | Allowed | Pre-approved list | Pre-approved with security assessment |
| Custom plugins | Unrestricted | Governed | Governed with code review |
| Graph connector review | Ad hoc | Annual | Semi-annual with data classification |

## Regulatory Alignment

- **FFIEC Development Booklet** — Supports compliance with third-party software governance requirements
- **OCC Third-Party Risk** — Helps meet vendor risk management for plugin providers
- **NYDFS 23 NYCRR 500** — Supports third-party service provider security assessment requirements

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for plugin governance automation
- See [Verification & Testing](verification-testing.md) to validate extensibility controls
