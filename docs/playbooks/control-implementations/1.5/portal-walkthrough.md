# Control 1.5: Sensitivity Label Taxonomy Review — Portal Walkthrough

Step-by-step portal configuration for reviewing and optimizing the sensitivity label taxonomy for M365 Copilot readiness.

## Prerequisites

- Microsoft Purview Compliance Administrator or Information Protection Administrator role
- Microsoft 365 E5 or E5 Compliance license
- Current sensitivity label taxonomy documentation
- Governance committee input on classification requirements

## Steps

### Step 1: Inventory Current Label Taxonomy

**Portal:** Microsoft Purview
**Path:** Purview > Information Protection > Labels

Review the complete list of published sensitivity labels. Document each label's name, description, scope (files, emails, meetings, sites), protection settings (encryption, content marking, auto-labeling), and priority order.

Identify labels that may need adjustment for Copilot interactions — Copilot respects label protections, so the taxonomy must clearly delineate access boundaries.

### Step 2: Evaluate Label Hierarchy for Copilot

**Portal:** Microsoft Purview
**Path:** Purview > Information Protection > Labels > [Select parent label]

Review the label hierarchy structure. For FSI environments, a recommended minimum taxonomy includes:
- **Public** — Content safe for external distribution
- **General** — Internal content with no special restrictions
- **Confidential** — Business-sensitive content with access restrictions
- **Highly Confidential** — Regulated data with encryption and strict access controls

Verify sub-labels provide sufficient granularity for different business units and data types (e.g., "Confidential - Client Data", "Confidential - Financial Reports").

### Step 3: Review Label Policies and Scoping

**Portal:** Microsoft Purview
**Path:** Purview > Information Protection > Label Policies

Check which label policies are active and which user groups they target. Verify all Copilot-licensed users have access to the full label taxonomy through published policies.

Confirm default label settings — a default label helps meet the minimum labeling coverage target for Copilot readiness.

### Step 4: Validate Auto-Labeling Configuration

**Portal:** Microsoft Purview
**Path:** Purview > Information Protection > Auto-labeling

Review auto-labeling policies that detect and classify sensitive content types common in FSI (account numbers, SSNs, financial data). Auto-labeling helps achieve the 85% coverage target before Copilot deployment.

Verify policies are in enforcement mode rather than simulation mode.

### Step 5: Document Taxonomy Decisions

Record all taxonomy review decisions including any labels added, modified, or deprecated. Document the rationale for each decision and obtain governance committee approval.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Review and document current taxonomy; set default label to "General" |
| **Recommended** | Optimize taxonomy for Copilot with sub-labels for FSI data types; enable auto-labeling for top 10 sensitive information types |
| **Regulated** | Mandatory labeling policy; auto-labeling for all FSI-relevant sensitive information types; quarterly taxonomy review |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for label management automation
- See [Verification & Testing](verification-testing.md) to validate taxonomy coverage
- Review Control 2.2 for Copilot-specific sensitivity label enforcement
