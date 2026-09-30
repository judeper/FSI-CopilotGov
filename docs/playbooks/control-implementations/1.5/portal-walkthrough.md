# Control 1.5: Sensitivity Label Taxonomy Review — Portal Walkthrough

Step-by-step portal configuration for reviewing and optimizing the sensitivity label taxonomy for M365 Copilot readiness.

## Prerequisites

- Purview Compliance Admin or Information Protection Admin role
- Microsoft 365 E5 or E5 Compliance license
- Current sensitivity label taxonomy documentation
- Governance committee input on classification requirements

## Steps

### Step 1: Inventory Current Label Taxonomy

**Portal:** Microsoft Purview portal
**Path:** Solutions > Information Protection > Sensitivity labels

Review the complete list of published sensitivity labels. Document each label's name, description, scope (files, emails, meetings, sites), protection settings (encryption, content marking, auto-labeling), and priority order.

Identify labels that may need adjustment for Copilot interactions — Copilot respects label protections, so the taxonomy must clearly delineate access boundaries.

### Step 2: Evaluate Label Hierarchy for Copilot

**Portal:** Microsoft Purview portal
**Path:** Solutions > Information Protection > Sensitivity labels

Review the label hierarchy structure. Microsoft is transitioning from the legacy parent/child hierarchy to **label groups** as the modern scheme, so first determine whether your tenant is still using parent labels or has the **Migrate to the modern label scheme** banner available. For FSI environments, a recommended minimum taxonomy includes:
- **Public** — Content safe for external distribution
- **General** — Internal content with no special restrictions
- **Confidential** — Business-sensitive content with access restrictions
- **Highly Confidential** — Regulated data with encryption and strict access controls

Verify sublabels or labels within each label group provide sufficient granularity for different business units and data types (for example, "Confidential - Client Data", "Confidential - Financial Reports").

### Step 3: Review Label Policies and Scoping

**Portal:** Microsoft Purview portal
**Path:** Solutions > Information Protection > Publishing policies

Check which label policies are active and which user groups they target. Verify all Copilot-licensed users have access to the full label taxonomy through published policies.

Confirm default label settings. A default label from a label policy helps prevent unlabeled new content, but it does **not** override an existing label. If a SharePoint document library needs to raise lower-priority labels or apply its library default to existing files, that uses the separate document-library default-label feature and, for preexisting files at rest, the dedicated auto-labeling policy.

### Step 4: Validate Auto-Labeling Configuration

**Portal:** Microsoft Purview portal
**Path:** Solutions > Information Protection > Policies > Auto-labeling policies

Review auto-labeling policies that detect and classify sensitive content types common in FSI (account numbers, SSNs, financial data). Auto-labeling helps achieve the governance-level coverage targets (>50% Baseline, >75% Recommended, >90% Regulated) before Copilot deployment.

For each policy, confirm the current phase:
- **Simulation mode** has completed and the results were reviewed
- **Coverage by simulation context** is available after the policy is turned on
- The **Labeled items** tab has been checked, including the **Failed** view for SharePoint and OneDrive files

If the organization already uses **default sensitivity labels for SharePoint document libraries**, determine whether a separate auto-labeling policy is needed to apply those library defaults to existing files that were already at rest before the default label was configured.

### Step 5: Document Taxonomy Decisions

Record all taxonomy review decisions including any labels added, modified, or deprecated. Document the rationale for each decision and obtain governance committee approval.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Review and document current taxonomy; set default label to "General"; enable mandatory labeling policy |
| **Recommended** | Optimize taxonomy for Copilot with sub-labels for FSI data types; enable auto-labeling for top 10 sensitive information types |
| **Regulated** | Auto-labeling for all FSI-relevant sensitive information types; quarterly taxonomy review |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for label management automation
- See [Verification & Testing](verification-testing.md) to validate taxonomy coverage
- Review Control 2.2 for Copilot-specific sensitivity label enforcement
- Back to [Control 1.5: Sensitivity Label Taxonomy Review](../../../controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md)
