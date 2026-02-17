# Control 1.7: SharePoint Advanced Management Readiness — Portal Walkthrough

Step-by-step portal configuration for enabling and validating SharePoint Advanced Management (SAM) capabilities that support Copilot governance.

## Prerequisites

- SharePoint Administrator or Global Administrator role
- SharePoint Advanced Management add-on license
- Microsoft 365 E3 or E5 base license
- Understanding of current SharePoint governance requirements

## Steps

### Step 1: Verify SAM License Activation

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Billing > Licenses > SharePoint Advanced Management

Confirm that SharePoint Advanced Management licenses are provisioned in your tenant. SAM enables critical governance features including Restricted SharePoint Search, site access reviews, data access governance reports, and site lifecycle management.

Verify the license count matches the number of SharePoint sites requiring advanced governance.

### Step 2: Enable Data Access Governance Reports

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Reports > Data access governance

Enable the data access governance reports that provide visibility into sharing patterns, permission grants, and content access across your SharePoint environment. These reports are foundational for Copilot governance.

Review available reports:
- Sharing links report — tracks all active sharing links by type
- Sites shared with "Everyone except external users" — identifies broad access
- Sensitivity label report — shows label coverage across sites
- Oversharing baseline — identifies sites with content access risk

### Step 3: Configure Site Lifecycle Policies

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Policies > Site lifecycle management

Set up site lifecycle policies to manage inactive sites that may contain stale data accessible to Copilot:
- Configure inactivity threshold (recommended: 180 days for FSI)
- Set notification cadence for site owners
- Define actions for unresponsive owners (archive, restrict, delete)

### Step 4: Set Up Site Access Reviews

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Sites > [Select site] > Access review

Enable site-level access reviews for high-sensitivity sites. SAM access reviews allow site owners to periodically validate who has access to their content, complementing the tenant-level permission audit in Control 1.6.

### Step 5: Configure Conditional Access for SharePoint

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
| **Baseline** | Activate SAM and enable data access governance reports |
| **Recommended** | Configure site lifecycle policies and enable access reviews for sensitive sites |
| **Regulated** | Full SAM deployment with automated lifecycle management, mandatory access reviews, and integration with Conditional Access policies |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for SAM automation
- See [Verification & Testing](verification-testing.md) to validate SAM configuration
- Review Control 1.3 for Restricted SharePoint Search (enabled by SAM)
