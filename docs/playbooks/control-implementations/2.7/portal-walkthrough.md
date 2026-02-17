# Control 2.7: Data Residency and Cross-Border Data Flow — Portal Walkthrough

Step-by-step portal procedures for verifying and configuring data residency controls for M365 Copilot processing.

## Prerequisites

- Global Administrator role
- Microsoft 365 Admin Center access
- Understanding of organizational data residency requirements
- Legal and compliance input on cross-border data flow obligations

## Steps

### Step 1: Verify Tenant Data Location

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Settings > Org Settings > Organization profile > Data location

Review the tenant's data residency configuration. Microsoft 365 stores data at rest in the geography associated with the tenant's provisioning country. Verify the data location for each workload (Exchange, SharePoint, Teams).

### Step 2: Review Copilot Data Processing Location

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Settings > Microsoft 365 Copilot > Data Processing

Review where Copilot processes prompts and generates responses. Microsoft processes Copilot interactions within the tenant's data boundary. Verify this configuration meets your regulatory data residency requirements.

Document the data processing locations for each Copilot workload.

### Step 3: Evaluate Microsoft EU Data Boundary or Advanced Data Residency

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Settings > Org Settings > Data Residency

If your organization requires strict data residency, evaluate:
- **EU Data Boundary:** For organizations subject to EU data regulations
- **Advanced Data Residency (ADR):** For organizations requiring in-country data processing
- **Multi-Geo:** For organizations with data residency requirements across multiple regions

Document which residency options are active and their scope.

### Step 4: Assess Cross-Border Data Flow Risks

Document cross-border data flow scenarios specific to Copilot:
- User in one region accessing content stored in another region
- Copilot processing requests that reference multi-region content
- Third-party plugins that may route data through external services
- Microsoft support access and data handling during support incidents

### Step 5: Document Data Residency Compliance Position

Create a data residency compliance document that includes:
- Tenant data location for each workload
- Copilot processing location confirmation
- Any cross-border data flow exceptions and justifications
- Legal basis for any cross-border transfers (SCCs, BCRs, adequacy decisions)
- Review cadence for data residency compliance

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Verify and document tenant data location; confirm Copilot processing geography |
| **Recommended** | Evaluate Advanced Data Residency for in-geography processing; document cross-border flows |
| **Regulated** | Advanced Data Residency or EU Data Boundary enabled; formal cross-border transfer documentation; legal review of processing locations |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for residency verification automation
- See [Verification & Testing](verification-testing.md) to validate residency controls
- Review Control 2.8 for encryption controls that complement data residency
