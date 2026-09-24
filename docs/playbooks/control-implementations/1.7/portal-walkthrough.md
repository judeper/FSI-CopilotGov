# Control 1.7: SharePoint Advanced Management Readiness — Portal Walkthrough

Step-by-step portal configuration for enabling and validating SharePoint Advanced Management (SAM) capabilities that support Copilot governance.

## Prerequisites

- SharePoint Admin or Entra Global Admin role
- Microsoft Copilot license assigned to at least one user in the tenant for Copilot-supporting SAM features, or SharePoint Advanced Management add-on license
- Microsoft 365 E3 or E5 base license
- Understanding of current SharePoint governance requirements

## Steps

### Step 1: Verify SAM License Activation

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Billing > Licenses

Confirm that SAM capabilities are available for your tenant:

- **If your organization has Microsoft Copilot licenses:** Verify at least one assigned Copilot license and confirm the SAM features listed by Microsoft for Copilot deployment support are accessible in the SharePoint admin center.
- **If your organization does not have Copilot licenses:** Confirm that the SharePoint Advanced Management add-on is assigned to SharePoint Admins. Navigate to Admin Center > Billing > Licenses > SharePoint Advanced Management to verify assignment.

SAM enables critical governance features including Restricted Content Discovery, Restricted Access Control, site access reviews, data access governance reports, and site lifecycle management.

### Step 2: Enable Data Access Governance Reports

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Reports > Data access governance

Enable the data access governance reports that provide visibility into sharing patterns, permission grants, and content access across your SharePoint environment. These reports are foundational for Copilot governance.

Review available reports:
- **Snapshot reports:** site permissions across your organization, site permissions for users, sensitivity labels applied to files, and detailed Everyone/EEEU item reports where available
- **Activity reports:** sharing links and content shared with "Everyone except external users" over the last 28 days
- **Content Management Assessment:** use this SAM hub for oversharing, inactive/ownerless sites, broken inheritance, and governance recommendations

Schedule reports to run monthly at minimum. For Regulated institutions, configure continuous reporting and integrate into compliance dashboards.

### Step 3: Configure Restricted Content Discovery

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Sites > Active Sites > [Select site] > Settings

For sites that should be excluded from Copilot content discovery entirely:

1. Select the target site from the Active Sites list
2. Click **Settings**
3. Turn **Restrict content from Microsoft Copilot** on
4. Click **Save**
5. Verify the setting by testing Copilot queries from a licensed user — content from the site should no longer appear in Copilot responses

Prioritize RCD for: sites containing HR data, legal holds, M&A deal data rooms, regulatory examination materials, and any site that has not passed data hygiene review.

### Step 4: Configure Restricted Access Control

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Policies > Access control > Site-level access restriction, then SharePoint Admin > Sites > Active sites > [Select site] > Settings > Restricted site access

Restricted Access Control (RAC) enforces a hard access boundary, restricting SharePoint or OneDrive site access to users who both have site/content permission and belong to a designated Microsoft Entra security group or Microsoft 365 group.

1. Enable site-level access restriction for the organization under **Policies > Access control**
2. Select the target site from the Active Sites list
3. Click **Settings**
4. In **Restricted site access**, add up to 10 approved Microsoft Entra security groups or Microsoft 365 groups
5. Click **Save**
6. Verify by testing with a user who has a sharing link but is not in a configured group — access should be denied

Prioritize RAC for: sites containing NPI, MNPI, customer financial records, audit materials, and M&A deal rooms. RAC is complementary to RCD: use RCD to limit discovery in Copilot and organization-wide search, and RAC to enforce who can access the site at all. Configure shared and private channel sites separately.

### Step 5: Configure Site Lifecycle Policies

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Site lifecycle management

Set up site lifecycle policies to manage inactive sites that may contain stale data accessible to Copilot:
- Configure inactive site, ownership, or attestation policies
- Set notification cadence for site owners or admins
- Define enforcement or follow-up actions for unresponsive owners, including archive or remediation workflows where approved

### Step 6: Set Up Site Access Reviews

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Sites > [Select site] > Access review

Enable site-level access reviews for high-sensitivity sites. SAM access reviews allow site owners to periodically validate who has access to their content, complementing the tenant-level permission audit in Control 1.6.

Initiate access reviews on sites flagged by DAG reports as having broad sharing or excessive sharing link volume.

### Step 7: Configure Conditional Access for SharePoint

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Policies > Access control

Review SAM-enhanced access control policies including:
- Unmanaged device access restrictions
- Network location-based access policies
- App-enforced restrictions integration with Conditional Access

These policies affect how users interact with content that Copilot may surface.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Verify SAM availability through tenant Copilot licensing or add-on assignment. Enable data access governance reports. Run site permissions snapshot as pre-deployment baseline. |
| **Recommended** | Configure site lifecycle policies and enable access reviews for sensitive sites. Enable RCD for sites with highly sensitive data. Deploy RAC on top 10 most sensitive sites (NPI, MNPI, regulatory examination materials). |
| **Regulated** | Full SAM deployment with automated lifecycle management, mandatory quarterly access reviews for all regulated data sites, RCD for all uncertified sites, RAC on all NPI/MNPI sites with quarterly security group membership review, and integration with compliance dashboards. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for SAM automation
- See [Verification & Testing](verification-testing.md) to validate SAM configuration
- Review [Control 1.3: Restricted SharePoint Search](../../../controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md) for Restricted SharePoint Search (complementary to RCD for Copilot scope control)
- Back to [Control 1.7: SharePoint Advanced Management](../../../controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md)
