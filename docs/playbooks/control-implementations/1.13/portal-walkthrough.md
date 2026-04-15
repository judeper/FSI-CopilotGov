# Control 1.13: Extensibility Readiness — Portal Walkthrough

Step-by-step portal procedures for assessing and governing Copilot extensibility features including plugins, connectors, and declarative agents.

## Prerequisites

- Microsoft 365 Admin Center access (Entra Global Admin or Teams Admin)
- Teams admin center access
- Understanding of planned Copilot extensibility use cases
- Governance committee input on extensibility policies

## Steps

### Step 1: Review Current Copilot Extensions

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Agents > Settings and Settings > Integrated apps

Review the current state of Copilot extensions in the tenant:
- Pre-built Microsoft plugins (Graph connectors, Microsoft apps)
- Third-party plugins available in the Teams app store
- Custom-built plugins and agents deployed by the organization
- Declarative agents created from SharePoint

Document which extensions are currently active and their data access scope.

### Step 2: Configure Extension Governance Policies

**Portal:** Teams admin center
**Path:** Teams Admin > Teams apps > Permission policies

Configure governance policies for Copilot extensions:
- Define which users can install third-party extensions
- Set approval workflows for new extension requests
- Block specific extensions that do not meet governance requirements
- Create an approved extensions allowlist for FSI compliance

### Step 3: Review Graph Connector Inventory

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Settings > Search & intelligence > Data sources

Review active Microsoft Graph connectors that bring external data into the Microsoft 365 search index and Copilot grounding:
- Identify each connector's data source and scope
- Review the data ingestion permissions and access controls
- Verify connector configurations align with data governance policies
- Document which connectors are approved for use with Copilot

### Step 4: Assess Custom Agent Development Readiness

**Portal:** Microsoft Copilot Studio
**Path:** copilotstudio.microsoft.com

Evaluate the organization's readiness for custom Copilot agent development:
- Review available Copilot Studio licenses and capabilities
- Assess developer team readiness and training needs
- Document governance requirements for custom agent development
- Define testing and approval processes for custom agents

### Step 5: Document Extensibility Governance Framework

Create the extensibility governance framework document covering:
- Extension approval criteria and process
- Data access review requirements for new extensions
- Testing requirements before production deployment
- Ongoing monitoring and review cadence
- Incident response procedures for extension-related issues

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Inventory current extensions; block all third-party extensions until governance review |
| **Recommended** | Implement extension approval workflow; maintain approved extension allowlist; quarterly review |
| **Regulated** | Formal extensibility governance framework with security review for each extension; data access impact assessment required; governance committee approval for all new extensions |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for extension management automation
- See [Verification & Testing](verification-testing.md) to validate extensibility controls
- Review Control 2.13 for Plugin and Graph Connector Security
- Back to [Control 1.13](../../../controls/pillar-1-readiness/1.13-extensibility-readiness.md)
