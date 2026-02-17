# Control 2.5: Data Minimization and Grounding Scope — Portal Walkthrough

Step-by-step portal configuration for limiting Copilot's data grounding scope to minimize unnecessary data exposure.

## Prerequisites

- Global Administrator or SharePoint Administrator role
- Microsoft 365 Copilot licenses deployed
- Data classification inventory completed (Control 1.1)
- Governance committee approval on grounding scope decisions

## Steps

### Step 1: Review Copilot Data Access Configuration

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Settings > Microsoft 365 Copilot > Data Access

Review the current Copilot data access configuration. Copilot grounds its responses on content the user has access to across Microsoft 365. Data minimization limits this scope to only what is necessary for the intended use cases.

### Step 2: Implement Restricted SharePoint Search

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Settings > Search > Restricted SharePoint Search

Enable Restricted SharePoint Search (Control 1.3) as the primary mechanism for grounding scope limitation. This restricts Copilot to only reference content from approved sites on the allowed list, reducing the grounding scope to vetted content sources.

### Step 3: Configure Site-Level Access Restrictions

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Active Sites > [Site] > Permissions

For sites on the allowed list, further minimize the data scope by:
- Removing overly broad permissions (Control 1.6)
- Setting sharing to "Only people in your organization" or more restrictive
- Configuring site-level access policies for sensitive content repositories

### Step 4: Review and Restrict Copilot Features by Workload

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Settings > Microsoft 365 Copilot > Settings

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
| **Baseline** | Enable RSS to limit grounding scope; disable unnecessary Copilot features |
| **Recommended** | Granular site-level restrictions; feature-level controls per workload; quarterly scope review |
| **Regulated** | Formal data minimization policy; governance committee approval for scope expansion; continuous monitoring of grounding behavior |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for scope configuration automation
- See [Verification & Testing](verification-testing.md) to validate data minimization
- Review Control 2.6 for web search and web grounding controls
