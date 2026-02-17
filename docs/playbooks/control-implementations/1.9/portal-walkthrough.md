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
- Prerequisite licenses (M365 E3/E5, Office 365 E3/E5)
- Required add-ons (SharePoint Advanced Management, E5 Compliance, Entra ID P2)

Confirm all prerequisite licenses are assigned to users planned for Copilot deployment.

### Step 2: Define License Assignment Groups

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Groups > New Group

Create security groups for Copilot license management aligned with deployment phases:
- **Copilot-Pilot-Users** — Phase 1 pilot group (typically 50-100 users)
- **Copilot-Wave1-Users** — First expansion wave
- **Copilot-Wave2-Users** — Second expansion wave
- **Copilot-Excluded-Users** — Users explicitly excluded from Copilot

Define group membership criteria based on department, role, readiness status, and governance approval.

### Step 3: Configure Group-Based License Assignment

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Groups > [Select group] > Licenses > Assignments

Assign the Microsoft 365 Copilot license to the deployment group. Group-based licensing automates assignment and removal as users are added or removed from the group.

Verify the license assignment processes successfully with no errors.

### Step 4: Verify Prerequisite License Stack

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Users > Active Users > [Select user] > Licenses

For a sample of users in each deployment group, verify the complete license stack:
- Base license (M365 E3 or E5)
- Copilot license
- Any required add-on licenses (SAM, E5 Compliance, Entra ID P2)

Identify and resolve any license dependency gaps.

### Step 5: Document License Assignment Policy

Create a license assignment policy that documents:
- Criteria for Copilot license eligibility
- Approval workflow for new license assignments
- Process for license reclamation from inactive users
- License cost tracking and budget allocation by department

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Group-based license assignment with documented deployment plan |
| **Recommended** | Phased rollout with governance gates between waves; license reclamation policy for inactive users |
| **Regulated** | Governance committee approval required for each wave; documented business justification per user group; quarterly license utilization review |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for license management automation
- See [Verification & Testing](verification-testing.md) to validate license assignments
- Review Control 1.11 for Change Management planning aligned with license rollout
