# Control 1.3: Restricted SharePoint Search and Restricted Content Discovery — Portal Walkthrough

Step-by-step portal configuration for implementing Restricted SharePoint Search (RSS) and Restricted Content Discovery (RCD) to limit Copilot's grounding scope to approved sites.

## Prerequisites

- SharePoint Administrator role
- SharePoint Advanced Management (SAM) license — included with Microsoft 365 Copilot licenses at no additional cost; standalone SAM add-on required for tenants without Copilot licenses
- List of approved SharePoint sites for Copilot grounding (for RSS)
- List of sites to exclude from Copilot discovery (for RCD)
- Governance committee approval on the allowed sites list and exclusion list

## RSS and RCD: Choose Your Approach

| Use Case | Tool | When |
|----------|------|------|
| Strict positive-list (only approved sites in Copilot) | RSS | Initial deployment, regulated environments |
| Surgical exclusion of specific sites | RCD | Targeted exclusion of known-sensitive sites |
| Defense-in-depth | RSS + RCD | Combined approach for maximum control |

## Steps

### Step 1: Enable Restricted SharePoint Search (RSS)

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Settings > Search > Restricted SharePoint Search

Navigate to search settings and locate the Restricted SharePoint Search toggle. Enable RSS to switch from the default "search everywhere" model to an allow-list-based model.

When enabled, SharePoint search and Microsoft 365 Copilot will only surface content from sites explicitly added to the allowed list. All other sites are excluded from search results and Copilot grounding.

### Step 2: Configure Restricted Content Discovery (RCD) for Specific Sites

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Sites > Active sites > [site name] > Settings

RCD can be used independently of RSS or alongside it. For each site you want to exclude from Copilot discovery:

1. Navigate to the site in Active sites
2. Open the site Settings panel
3. Enable "Restrict content org-wide search"
4. Save the setting

RCD excludes the site from Copilot discovery while leaving direct user access unchanged. Users with permissions can still navigate to and use the site — only Copilot's ability to discover and surface the site's content is restricted.

### Step 3: Build the RSS Allowed Sites List

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Settings > Search > Restricted SharePoint Search > Manage allowed sites

Add sites to the allowed list based on governance committee approval. Consider including:
- Departmental collaboration sites with proper access controls
- Policy and procedure document libraries
- Approved knowledge bases and reference materials

Exclude sites containing sensitive data that has not been properly classified or where permissions have not been validated.

### Step 4: Verify Site Inclusion and Exclusion

**For RSS allowed list:**
**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Settings > Search > Restricted SharePoint Search > View allowed sites

Review the complete allowed sites list. Verify each site has been reviewed for appropriate permissions and sensitivity labels. Document the list with business justification for each included site.

**For RCD exclusion:**
Review RCD-enabled sites by checking the settings panel for each site. Maintain a separate governance log documenting which sites have RCD enabled and why.

### Step 5: Verify Copilot Data Access Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Settings

Verify that Copilot data access settings reflect the RSS configuration. Copilot should only ground responses on content from allowed sites when RSS is enabled.

### Step 6: Communicate Changes to Users

Document the RSS and/or RCD configuration and communicate to Copilot users that search results and Copilot responses will be limited to approved content sources. Set expectations that some previously searchable content may no longer appear in results.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Enable RCD for known high-risk sites as a simpler starting point. If deploying RSS, start with a conservative initial allowed list of fully vetted sites |
| **Recommended** | Implement RSS with quarterly review of the allowed sites list by governance committee. Apply RCD to sites with sensitive content not yet fully remediated |
| **Regulated** | Enable RSS with formal change control process for any additions to the allowed list. Apply RCD as supplementary control for any sites with residual sensitive content. Maintain audit trail of all changes to both RSS and RCD configurations |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for scripted RSS and RCD management
- See [Verification & Testing](verification-testing.md) to validate search restrictions
- Review Control 1.2 for DSPM oversharing detection as a complementary control
