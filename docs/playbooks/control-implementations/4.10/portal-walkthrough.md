# Control 4.10: Business Continuity and Disaster Recovery — Portal Walkthrough

Step-by-step portal configuration for establishing business continuity and disaster recovery procedures addressing Copilot service dependencies in financial services environments.

## Prerequisites

- **Role:** Entra Global Admin, IT Infrastructure Manager
- **License:** Microsoft 365 E5 with Copilot add-on
- **Access:** Microsoft 365 Admin Center, Service Health Dashboard

## Steps

### Step 1: Document Copilot Service Dependencies

**Portal:** Microsoft 365 Admin Center
**Path:** Health > Service health

1. Map Copilot service dependencies across the Microsoft 365 stack:
   - Azure OpenAI Service (core AI processing)
   - Microsoft Graph (organizational data access)
   - SharePoint Online (content grounding)
   - Exchange Online (email interactions)
   - Teams (meeting and chat interactions)
2. Document the dependency chain and single points of failure.
3. Identify which business processes have become dependent on Copilot.

### Step 2: Configure Service Health Monitoring

**Portal:** Microsoft 365 Admin Center
**Path:** Health > Service health > Preferences

1. Configure service health notifications:
   - Subscribe to Copilot-related service advisories and incidents
   - Add the IT operations team and compliance team as notification recipients
   - Enable notifications for all severity levels
2. Create a monitoring dashboard for Copilot service dependencies.
3. Set up Microsoft 365 Service Health API integration for automated monitoring.

### Step 3: Develop Copilot-Specific BCP Procedures

**Portal:** Internal business continuity documentation
**Path:** BCP/DR plan appendix for AI services

1. Document fallback procedures for each Copilot-dependent business process:
   - Document drafting without Copilot — return to manual processes
   - Meeting management without Copilot — manual note-taking protocols
   - Email management without Copilot — standard email practices
   - Data analysis without Copilot — traditional analytics tools
2. Define Recovery Time Objective (RTO) and Recovery Point Objective (RPO) for Copilot services.
3. Assign BCP coordinators for each business unit.

### Step 4: Establish Communication Plan for Copilot Outages

**Portal:** Internal communications system
**Path:** Incident communication templates

1. Create communication templates for different outage scenarios:
   - Planned maintenance — advance notice to affected users
   - Unplanned partial outage — status update and workaround guidance
   - Extended outage — fallback procedure activation notice
2. Define the communication chain: IT Operations -> Department heads -> End users.
3. Establish a status page or Teams channel for real-time outage updates.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Service health monitoring | Email alerts | Real-time API monitoring | Automated with dashboards |
| BCP procedures for Copilot | None | Documented fallbacks | Tested fallbacks |
| DR testing frequency | Annual | Semi-annual | Quarterly |
| Communication templates | Ad hoc | Pre-defined | Pre-defined with approval chain |

## Regulatory Alignment

- **FFIEC BCP Booklet** — Supports compliance with business continuity planning requirements for technology dependencies
- **12 CFR part 30, appendix D (OCC Heightened Standards)** — Helps meet expectations for technology resilience and recovery
- **FINRA Rule 4370** — Supports business continuity plan requirements for broker-dealers

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for service monitoring automation
- See [Verification & Testing](verification-testing.md) to validate BCP/DR procedures
- Back to [Control 4.10](../../../controls/pillar-4-operations/4.10-business-continuity.md)
