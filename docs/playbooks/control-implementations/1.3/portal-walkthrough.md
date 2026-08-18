# Control 1.3: Restricted SharePoint Search and Restricted Content Discovery — Portal Walkthrough

Step-by-step portal configuration for implementing Restricted SharePoint Search (RSS) and Restricted Content Discovery (RCD) as scope-limiting controls while SharePoint permissions, labels, RBAC, and DLP mature.

## Prerequisites

- SharePoint Admin role
- SharePoint Advanced Management (SAM) license — included with Microsoft 365 Copilot licenses at no additional cost; standalone SAM add-on required for tenants without Copilot licenses
- List of approved SharePoint sites for Copilot grounding (for RSS)
- List of sites to exclude from Copilot discovery (for RCD)
- Governance committee approval on the allowed sites list and exclusion list

## RSS and RCD: Choose Your Approach

!!! warning "RSS is retiring"
    Restricted SharePoint Search (RSS) is retiring. Microsoft has blocked new enablement from July 31, 2026. For new Copilot deployments, use Restricted Content Discovery (RCD) as the primary discoverability control. Organizations with existing RSS configurations should plan migration to RCD.

| Use Case | Tool | When |
|----------|------|------|
| **New deployment** — temporary per-site restriction while permissions are reviewed | **RCD** | All new Copilot deployments; RCD is the current recommended control |
| **Existing RSS deployment** — migrate positive-list posture to per-site exclusions | **RCD migration from RSS** | Plan RCD for all sites requiring discovery restriction; disable RSS when RCD is validated |
| Targeted suppression from tenant-wide discovery | RCD | Known-sensitive sites that should be hidden from Copilot and tenant-wide search experiences |
| Layered transition control (existing RSS deployments only) | RSS + RCD (legacy) | Combined approach during RSS migration period while durable Purview, SAM, RBAC, label, and DLP controls mature |

## Steps

### Step 1: Enable Restricted Content Discovery (RCD) for Specific Sites (Current Path)

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Sites > Active sites > [site name] > Settings

RCD is the current discoverability control for new Copilot deployments. For each site you want to exclude from Copilot discovery:

1. Navigate to the site in Active sites
2. Open the site Settings panel
3. Enable "Restrict content from Microsoft 365 Copilot"
4. Select **Save**

RCD is a stronger site-level discovery control than RSS. It hides the site from Microsoft 365 Copilot and tenant-wide search experiences such as SharePoint home, Office.com, Bing, and Delve where applicable. It also removes AI-powered entry points from the site (Copilot button, AI action menus, Create pages with AI). RCD still does not change existing site permissions: users with direct permissions can open content in SharePoint, and files they own or recently interacted with can still appear.

### Step 2: Enable Restricted SharePoint Search (RSS) — Existing Configurations Only

!!! warning "RSS is retiring"
    RSS new enablement is blocked from July 31, 2026. Step 2 applies **only** to organizations managing an existing RSS configuration enabled before that date.

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Settings > Search > Restricted SharePoint Search

For organizations with existing RSS configurations, the setting remains accessible for management and for disabling during migration to RCD. Navigate to search settings to review current RSS status.

RSS does not change user permissions and is not a security boundary. Microsoft notes that RSS does not provide complete exclusion: if a user recently accessed a site or the site was shared with that user in Teams or Outlook, that site can still appear in search results or Copilot responses even when it is not on the allowed list.

### Step 3: Build the RCD Governance Log and (for legacy) RSS Allowed Sites List

**For RCD (current path):**
Maintain a governance log for each site with RCD applied. For each site, document:
- Site URL and name
- Justification for discovery restriction (e.g., permissions review pending, sensitive content not yet labeled)
- Date applied and review date
- Owner responsible for site remediation

**For RSS (existing deployments only):**
**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Settings > Search > Restricted SharePoint Search > Manage allowed sites

If managing an existing RSS configuration, review and maintain the allowed list based on governance committee approval. Organizations migrating from RSS should plan to transition allowed-list exclusions to per-site RCD before disabling RSS.

### Step 4: Verify Site Inclusion and Exclusion

**For RCD:**
Review RCD-enabled sites by checking the settings panel for each site or by running the tenant-wide monitoring report. Maintain the governance log documenting which sites have RCD enabled and why. When testing, use accounts that do not own, recently access, or receive direct shares to the site so exceptions are visible rather than mistaken for configuration failure.

**For RSS (existing deployments only):**
**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Settings > Search > Restricted SharePoint Search > View allowed sites

Review the complete allowed sites list. Verify each site has been reviewed for appropriate permissions and sensitivity labels. Document the list with business justification for each included site and note that RSS exceptions can occur for recently accessed or Teams/Outlook-shared sites.

### Step 5: Verify Copilot Data Access Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Settings

Verify that Copilot data access settings reflect the expected governance configuration. For RCD-based deployments, confirm Copilot does not surface content from RCD-excluded sites. For existing RSS configurations, Copilot grounding should be scoped primarily to the allowed list, with documented exceptions for recent access or Teams/Outlook sharing.

### Step 6: Communicate Changes to Users

Document the RCD and/or RSS configuration and communicate to Copilot users that search results and Copilot responses may be limited for specific sites. Set expectations that direct SharePoint permissions still control access and that some previously discoverable content may no longer appear in tenant-wide results. For organizations migrating from RSS, communicate the expected change in Copilot behavior when RSS is disabled.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Enable RCD for known high-risk sites. RSS cannot be newly enabled; if an existing RSS configuration is in place, plan migration to RCD |
| **Recommended** | Apply RCD to all sites with unreviewed permissions or unresolved sensitivity labels. If migrating from RSS, complete transition to RCD with quarterly review of the RCD governance log. Track known RCD exceptions |
| **Regulated** | Manage RCD through formal change control. Apply RCD to all sites that have not passed data hygiene certification. Maintain an audit trail of all RCD changes with justification records in Purview audit logs. For existing RSS: complete migration with compliance sign-off; update the regulatory examination file |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for scripted RSS and RCD management
- See [Verification & Testing](verification-testing.md) to validate search restrictions
- Review [Control 1.2: SharePoint Oversharing Detection](../../../controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md) for DSPM oversharing detection as a complementary control
- Back to [Control 1.3: Restricted SharePoint Search](../../../controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md)
