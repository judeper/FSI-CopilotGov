# Control 1.9: License Planning and Assignment Strategy — Portal Walkthrough

Step-by-step portal configuration for planning and managing M365 Copilot license assignments aligned with governance requirements.

## Prerequisites

- License Administrator or Global Administrator role
- Microsoft 365 Admin Center access
- Approved Copilot deployment plan from governance committee
- User readiness assessment results from Control 1.1

## Steps

### Step 1: Inventory Current Licensing

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Billing > Licenses

Review current license inventory including:
- Microsoft 365 Copilot license count (purchased vs. assigned)
- Prerequisite licenses (M365 E3/E5, Office 365 E3/E5, Microsoft 365 F1/F3)
- Required add-ons (SharePoint Advanced Management, E5 Compliance, Entra ID P2)

Confirm all prerequisite licenses are assigned to users planned for Copilot deployment. Note which users are on Frontline (F1/F3) base licenses, as Copilot is available as an add-on for these SKUs.

### Step 2: Define License Assignment Groups

**Portal:** Microsoft Entra admin center
**Path:** Entra admin center > Groups > New Group

Create security groups for Copilot license management aligned with deployment phases:
- **Copilot-Pilot-Users** — Phase 1 pilot group (typically 50-100 users)
- **Copilot-Wave1-Users** — First expansion wave
- **Copilot-Wave2-Users** — Second expansion wave
- **Copilot-Frontline-Users** — Frontline workers (F1/F3 base) receiving the Copilot add-on
- **Copilot-Excluded-Users** — Users explicitly excluded from Copilot

Define group membership criteria based on department, role, readiness status, and governance approval.

### Step 3: Configure Group-Based License Assignment

**Portal:** Microsoft Entra admin center
**Path:** Entra admin center > Groups > [Select group] > Licenses > Assignments

Assign the Microsoft 365 Copilot license to the deployment group. Group-based licensing automates assignment and removal as users are added or removed from the group.

For Frontline users on F1/F3 base licenses, assign the Copilot add-on to the **Copilot-Frontline-Users** group. Confirm the F1 or F3 base license is present before assigning the Copilot add-on.

Verify the license assignment processes successfully with no errors.

### Step 4: Configure Pay-As-You-Go (PAYG) Copilot Chat

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Billing > Licenses (Azure billing linkage) or Azure portal > Cost Management

If deploying PAYG Copilot Chat ($0.01/message) for pilot users or occasional-access populations:

1. Verify PAYG Copilot Chat is enabled for the tenant in the Microsoft 365 Admin Center
2. Navigate to Azure portal > Cost Management to set up spend alerts and budget limits for PAYG usage
3. Configure per-department or per-user cost tracking to ensure PAYG spending is attributed correctly
4. Document which users are on the PAYG model vs. per-seat licensing in the deployment plan

**Note:** PAYG users do not require individual license assignment — any user with an appropriate base license can access Copilot Chat at the metered rate once PAYG is enabled. Apply governance policies to cover PAYG users the same as per-seat users.

### Step 5: Verify Prerequisite License Stack

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Users > Active Users > [Select user] > Licenses

For a sample of users in each deployment group, verify the complete license stack:
- Base license (M365 E3/E5 or F1/F3 for Frontline users)
- Copilot license (full seat or Frontline add-on as applicable)
- Any required add-on licenses (SAM, E5 Compliance, Entra ID P2)

Identify and resolve any license dependency gaps.

### Step 6: Document License Assignment Policy

Create a license assignment policy that documents:
- Criteria for Copilot license eligibility (per-seat vs. Frontline add-on vs. PAYG)
- Approval workflow for new license assignments
- Process for license reclamation from inactive users
- License cost tracking and budget allocation by department (including PAYG cost allocation)

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Group-based license assignment with documented deployment plan; PAYG acceptable for pilot groups (<50 users) with Azure spend limits configured |
| **Recommended** | Phased rollout with governance gates between waves; license reclamation policy for inactive users; per-seat licenses for regular users, PAYG for occasional/seasonal users; Frontline add-on documented with FSI use cases |
| **Regulated** | Governance committee approval required for each wave; documented business justification per user group; quarterly license utilization review; per-seat licenses required for users handling regulated data; PAYG limited to non-regulated use cases with documented justification |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for license management automation
- See [Verification & Testing](verification-testing.md) to validate license assignments
- Review Control 1.11 for Change Management planning aligned with license rollout
