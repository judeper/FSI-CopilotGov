# Control 2.5: Data Minimization and Grounding Scope — Portal Walkthrough

Step-by-step portal configuration for limiting Copilot's data grounding scope to minimize unnecessary data exposure.

## Prerequisites

- Entra Global Admin or SharePoint Admin role
- Microsoft 365 Copilot licenses deployed
- SharePoint Advanced Management prerequisites met (required for Restricted Content Discovery)
- Data classification inventory completed (Control 1.1)
- Governance committee approval on grounding scope decisions

## Steps

### Step 1: Review Copilot Data Access Configuration

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Settings > Data access

Review the current Copilot data access configuration. Copilot grounds its responses on content the user has access to across Microsoft 365. Data minimization limits this scope to only what is necessary for the intended use cases.

### Step 2: Apply Restricted Content Discovery to High-Risk Sites

**Portal:** SharePoint admin center
**Path:** Sites > Active sites > [Site] > Settings > **Restrict content from Microsoft 365 Copilot**

Apply Restricted Content Discovery (RCD) as the primary mechanism for grounding scope limitation. RCD hides site content from organization-wide discovery experiences and Microsoft 365 Copilot discovery scenarios, and removes AI entry points such as the Copilot button, AI actions menus, and **Create pages with AI** on the site. It does not change permissions. RCD requires SharePoint Advanced Management availability and a Microsoft 365 Copilot license.

Restricted SharePoint Search (Control 1.3) is retiring — Microsoft blocks new enablement starting July 31, 2026 and directs organizations to RCD for content discoverability. Where RSS is already enabled, maintain the allow list while planning its retirement.

### Step 3: Configure Site-Level Access Restrictions

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Active Sites > [Site] > Permissions

For sites on the allowed list, further minimize the data scope by:
- Removing overly broad permissions (Control 1.6)
- Setting sharing to "Only people in your organization" or more restrictive
- Configuring site-level access policies for sensitive content repositories

### Step 4: Review and Restrict Copilot Features by Workload

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Settings

Disable Copilot features that are not needed for your deployment:
- Disable web grounding if not required (see Control 2.6)
- Review which Office applications have Copilot enabled
- Disable Copilot in workloads that handle sensitive data without proper controls

### Step 5: Document Data Minimization Decisions

Record all data minimization decisions including:
- Grounding scope (which content sources are included)
- Features disabled and rationale
- Data types excluded from Copilot access
- Review cadence and expansion criteria

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Apply RCD to high-risk sites to limit grounding scope; disable unnecessary Copilot features |
| **Recommended** | Granular site-level restrictions; feature-level controls per workload; quarterly scope review |
| **Regulated** | Formal data minimization policy; governance committee approval for scope expansion; continuous monitoring of grounding behavior |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for scope configuration automation
- See [Verification & Testing](verification-testing.md) to validate data minimization
- Review Control 2.6 for web search and web grounding controls
- Back to [Control 2.5](../../../controls/pillar-2-security/2.5-data-minimization-grounding-scope.md)
