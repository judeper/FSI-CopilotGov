# Control 1.3: Restricted SharePoint Search and Restricted Content Discovery — Portal Walkthrough

Step-by-step portal configuration for implementing Restricted SharePoint Search (RSS) and Restricted Content Discovery (RCD) as scope-limiting controls while SharePoint permissions, labels, RBAC, and DLP mature.

## Prerequisites

- SharePoint Admin role
- SharePoint Advanced Management (SAM) license — included with Microsoft 365 Copilot licenses at no additional cost; standalone SAM add-on required for tenants without Copilot licenses
- List of approved SharePoint sites for Copilot grounding (for RSS)
- List of sites to exclude from Copilot discovery (for RCD)
- Governance committee approval on the allowed sites list and exclusion list

## RSS and RCD: Choose Your Approach

| Use Case | Tool | When |
|----------|------|------|
| Temporary positive-list while permissions are reviewed | RSS | Initial deployment and regulated onboarding; not a long-term security boundary |
| Targeted suppression from tenant-wide discovery | RCD | Known-sensitive sites that should be hidden from Copilot and tenant-wide search experiences |
| Layered transition control | RSS + RCD | Combined approach while durable Purview, SAM, RBAC, label, and DLP controls mature |

## Steps

### Step 1: Enable Restricted SharePoint Search (RSS)

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Settings > Search > Restricted SharePoint Search

Navigate to search settings and locate the Restricted SharePoint Search toggle. Enable RSS to temporarily limit SharePoint search and Microsoft 365 Copilot grounding to an allow-list of up to 100 sites while permissions are audited.

RSS does not change user permissions and is not a security boundary. Microsoft notes that RSS does not provide complete exclusion: if a user recently accessed a site or the site was shared with that user in Teams or Outlook, that site can still appear in search results or Copilot responses even when it is not on the allowed list.

### Step 2: Configure Restricted Content Discovery (RCD) for Specific Sites

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Sites > Active sites > [site name] > Settings

RCD can be used independently of RSS or alongside it. For each site you want to exclude from Copilot discovery:

1. Navigate to the site in Active sites
2. Open the site Settings panel
3. Enable "Restrict content from Microsoft 365 Copilot"
4. Save the setting

RCD is a stronger site-level discovery control than RSS because it hides the site from Microsoft 365 Copilot and tenant-wide search experiences such as SharePoint home, Office.com, Bing, and Delve where applicable. It still does not change existing site permissions: users with direct permissions can open content in SharePoint, and files they own or recently interacted with can still appear.

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

Review the complete allowed sites list. Verify each site has been reviewed for appropriate permissions and sensitivity labels. Document the list with business justification for each included site and note that RSS exceptions can occur for recently accessed or Teams/Outlook-shared sites.

**For RCD exclusion:**
Review RCD-enabled sites by checking the settings panel for each site. Maintain a separate governance log documenting which sites have RCD enabled and why. When testing, use accounts that do not own, recently access, or receive direct shares to the site so exceptions are visible rather than mistaken for configuration failure.

### Step 5: Verify Copilot Data Access Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Settings

Verify that Copilot data access settings reflect the RSS configuration. Copilot grounding should be scoped primarily to the allowed list when RSS is enabled, with documented exceptions for recent access or Teams/Outlook sharing.

### Step 6: Communicate Changes to Users

Document the RSS and/or RCD configuration and communicate to Copilot users that search results and Copilot responses may be limited to approved content sources during the transition. Set expectations that direct SharePoint permissions still control access and that some previously searchable content may no longer appear in tenant-wide results.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Enable RCD for known high-risk sites as a simpler starting point. If deploying RSS, treat it as temporary and start with a conservative initial allowed list of fully vetted sites |
| **Recommended** | Implement RSS with quarterly review of the allowed sites list by governance committee, track known RSS exceptions, and apply RCD to sites with sensitive content not yet fully remediated |
| **Regulated** | Manage RSS and RCD through formal change control. Require data hygiene certification before additions to the RSS allowed list, apply RCD as a targeted discovery control for residual sensitive content, and maintain an audit trail of all changes |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for scripted RSS and RCD management
- See [Verification & Testing](verification-testing.md) to validate search restrictions
- Review [Control 1.2: SharePoint Oversharing Detection](../../../controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md) for DSPM oversharing detection as a complementary control
- Back to [Control 1.3: Restricted SharePoint Search](../../../controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md)
