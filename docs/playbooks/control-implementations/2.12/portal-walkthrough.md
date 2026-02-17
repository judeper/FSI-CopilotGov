# Control 2.12: External Sharing and Guest Access Governance — Portal Walkthrough

Step-by-step portal configuration for governing external sharing and guest access in the context of M365 Copilot.

## Prerequisites

- SharePoint Administrator and Entra ID Administrator roles
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
- Guest access expiration: Configure automatic expiration for guest accounts

### Step 3: Restrict Guest Access to Copilot-Accessible Content

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Active Sites > [Site] > Sharing

For sites in the Copilot grounding scope, verify external sharing is disabled or appropriately restricted. Guests should not have access to sites that Copilot uses for grounding responses unless explicitly approved.

### Step 4: Configure Conditional Access for Guest Users

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Protection > Conditional Access > Create Policy

Create a Conditional Access policy for guest users accessing content:
- Target: Guest and external users
- Grant: Require MFA, require terms of use acceptance
- Session: Limited session duration (4 hours maximum)

### Step 5: Set Up Guest Access Reviews

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Identity Governance > Access Reviews

Create recurring access reviews for guest users:
- Review scope: All guest users with access to SharePoint or Teams
- Frequency: Monthly for sites with sensitive content
- Auto-apply: Remove access for denied or non-responded reviews

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Disable anonymous sharing; restrict external sharing to existing guests; guest access reviews |
| **Recommended** | Organization-only sharing on Copilot-scoped sites; domain restrictions; monthly guest reviews |
| **Regulated** | External sharing disabled on all Copilot-accessible sites; guest accounts require governance approval; automated expiration and quarterly reviews |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for external sharing automation
- See [Verification & Testing](verification-testing.md) to validate sharing controls
