# Control 2.12: External Sharing and Guest Access Governance — Portal Walkthrough

Step-by-step portal configuration for governing external sharing and guest access in the context of M365 Copilot.

## Prerequisites

- SharePoint Admin and Entra ID Administrator roles
- Microsoft 365 E5 or E3 with security add-ons
- External collaboration policy approved by governance committee

## Steps

### Step 1: Review Tenant-Level External Sharing Settings

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Policies > Sharing

Review and configure the tenant-level external sharing policy. For FSI environments, restrict sharing to prevent Copilot from surfacing content that has been shared externally without proper controls:
- Set tenant default to "Existing external users only" or "Only people in your organization"
- Disable anonymous sharing links organization-wide
- Configure sharing link expiration (maximum 30 days for FSI)

### Step 2: Configure Guest Access Policies in Entra ID

**Portal:** Entra ID Admin Center
**Path:** Entra ID > External Identities > External collaboration settings

Configure guest access restrictions:
- Guest user access: Set to "Limited access" (guests cannot enumerate directory)
- Guest invite restrictions: Only admins or specific roles can invite guests
- Collaboration restrictions: Define allowed or denied domains for external collaboration

These Entra external collaboration settings do not configure SharePoint/OneDrive guest-access expiration or delete guest accounts.

### Step 3: Configure SharePoint and OneDrive Guest-Access Expiration

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Policies > Sharing > More external sharing settings

- Configure **Guest access to a site or OneDrive will expire automatically after this many days**
- Document who reviews expiration notices and who may extend approved access
- Review site-level overrides under **Active sites > [Site] > Settings > More sharing settings**
- Inventory pre-existing direct or sharing-link access separately because the expiration policy applies only to access granted after the policy is enabled
- Inventory access through Microsoft 365 groups, security groups, and Teams separately because those membership-derived paths can survive SharePoint expiration

Microsoft's [guest-expiration guidance](https://support.microsoft.com/en-us/office/manage-guest-expiration-for-a-site-25bee24f-42ad-4ee8-8402-4186eed74dea) says the policy applies to guests using sharing links or direct site permissions granted after enablement. It does not alter or delete the Microsoft Entra B2B guest account, and Microsoft 365 group, security group, or Teams access can remain. Reconcile those access paths separately before treating an expired guest as removed.

### Step 4: Restrict Guest Access to Copilot-Accessible Content

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Active Sites > [Site] > Sharing

For sites in the Copilot grounding scope, verify external sharing is disabled or appropriately restricted. Guests should not have access to sites that Copilot uses for grounding responses unless explicitly approved.

### Step 5: Configure Conditional Access for Guest Users

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Protection > Conditional Access > Create Policy

Create a Conditional Access policy for guest users accessing content:
- Target: Guest and external users
- Grant: Require MFA, require terms of use acceptance
- Session: Limited session duration (4 hours maximum)

### Step 6: Set Up Guest Access Reviews

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Identity Governance > Access Reviews

Create recurring access reviews for guest users:
- Review scope: A selected Team or group, or an application, matching the access being reviewed
- Frequency: Monthly for sites with sensitive content
- Auto-apply: Remove access to the reviewed resource for denied or non-responded reviews
- Post-review reconciliation: Verify the guest has no surviving access through another Microsoft 365 group, security group, Team, application, direct permission, or sharing link

A denial in a Team, group, or application review removes access to that reviewed resource only; it must not by itself trigger a tenant-wide B2B guest-account block or deletion. If an account-level action is required, conduct a separate, dedicated guest-lifecycle review and first verify that all direct permissions, sharing links, Microsoft 365 group and security group memberships, Teams and SharePoint access, application assignments, and other active engagements are obsolete. Apply any approved account action through the tenant's guest-lifecycle procedure rather than treating the resource-review denial as a tenant-wide decision.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Disable anonymous sharing; restrict external sharing to existing guests; guest access reviews |
| **Recommended** | Organization-only sharing on Copilot-scoped sites; domain restrictions; monthly guest reviews |
| **Regulated** | External sharing disabled on all Copilot-accessible sites; guest accounts require governance approval; SharePoint/OneDrive access expiration plus separate Microsoft 365 group, security group, and Teams reconciliation; quarterly resource reviews; dedicated guest-lifecycle review before any tenant-wide account action |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for external sharing automation
- See [Verification & Testing](verification-testing.md) to validate sharing controls
- Back to [Control 2.12](../../../controls/pillar-2-security/2.12-external-sharing-governance.md)
