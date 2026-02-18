# Control 1.6: Permission Model Audit — Portal Walkthrough

Step-by-step portal procedures for auditing the Microsoft 365 permission model to identify access risks before Copilot deployment.

## Prerequisites

- SharePoint Administrator and Entra ID Administrator roles
- Access to SharePoint Admin Center, Microsoft Entra admin center, and Microsoft Purview portal
- Microsoft 365 E5 or Entra ID P2 license for access reviews
- Inventory of high-sensitivity SharePoint sites and Teams

## Steps

### Step 1: Review SharePoint Site-Level Permissions

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Active Sites > [Select site] > Permissions

For each high-sensitivity site, review site-level permissions including:
- Site owners, members, and visitors groups
- Any "Everyone" or "Everyone except external users" permissions
- External sharing links and guest access grants
- Custom permission levels beyond the defaults

Document any permissions that are broader than the business need warrants.

### Step 2: Audit Entra ID Group Memberships

**Portal:** Microsoft Entra admin center
**Path:** Entra ID > Groups > All Groups > [Select group] > Members

Review membership of security groups and Microsoft 365 groups used for SharePoint and Teams access. Focus on groups that grant access to sensitive content:
- Identify groups with 100+ members that access confidential content
- Flag nested group structures that may grant unintended access
- Review dynamic group membership rules for accuracy

### Step 3: Configure Access Reviews

**Portal:** Microsoft Entra admin center
**Path:** Entra ID > Identity Governance > Access Reviews > New access review

Create recurring access reviews for groups that control access to sensitive content. Configure:
- Review scope: Members of groups with access to Confidential or Highly Confidential sites
- Reviewers: Group owners or designated business approvers
- Frequency: Quarterly for standard, monthly for highly sensitive
- Auto-apply results: Remove access for denied or non-responded reviews

### Step 4: Review Sharing Links and Anonymous Access

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Policies > Sharing

Review tenant-level sharing settings and site-level overrides. For FSI environments:
- Tenant default should be "Only people in your organization" or more restrictive
- Identify sites with sharing capability set above the tenant default
- Review active sharing links using the Sharing report

### Step 5: Assign DSPM for AI RBAC Roles

Microsoft Purview introduces dedicated roles for AI governance oversight. Assign these as part of the permission model configuration to maintain least-privilege access to AI governance data.

**Purview Data Security AI Viewer and AI Content Viewer:**

**Portal:** Microsoft Purview portal
**Path:** Purview portal > Settings > Roles and scopes > Role groups

1. Search for "Purview Data Security AI Viewer" in the role groups list
2. Select the role group and click **Edit**
3. Add compliance team members who need read-only access to DSPM for AI dashboards and AI observability metrics
4. Click **Save**

Repeat for "Purview Data Security AI Content Viewer" — add only investigation team members authorized to view prompt and response content. This role grants access to actual prompt/response data; restrict to personnel with documented authorization.

**AI Administrator (Microsoft Entra role):**

**Portal:** Microsoft Entra admin center
**Path:** Entra ID > Roles and administrators > AI Administrator

1. Click **AI Administrator** in the roles list
2. Click **Add assignments**
3. Search for and select the Copilot governance lead (the person responsible for managing Copilot DLP policies and AI service authorizations)
4. Click **Add**

Verify assignment: The AI Administrator role grants full management of Copilot DLP policies in the Microsoft 365 Admin Center without requiring full Purview Compliance Administrator rights.

### Step 6: Document Permission Audit Findings

Compile a permission audit report including:
- Count of sites with permissions broader than needed
- Groups with excessive membership for their content access level
- Sharing links requiring remediation
- DSPM role assignments and authorized personnel list
- Recommended remediation actions with priority and timeline

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Audit permissions on all sites containing sensitive data; remove "Everyone" access; assign Purview Data Security AI Viewer to compliance team |
| **Recommended** | Implement quarterly access reviews for all sensitive content groups; restrict tenant sharing to organization-only; assign AI Content Viewer to investigation team and AI Administrator to Copilot governance lead |
| **Regulated** | Monthly access reviews with auto-remediation; zero "Everyone" or anonymous access on any site; formal sign-off on all permission exceptions; quarterly access review of all AI-prefixed role assignments; formal documentation of AI Content Viewer authorization |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for bulk permission auditing
- See [Verification & Testing](verification-testing.md) to validate permission remediation
- Review Control 1.7 for SharePoint Advanced Management capabilities
