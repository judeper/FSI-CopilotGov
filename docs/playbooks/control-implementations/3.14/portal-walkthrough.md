# Control 3.14: Copilot Pages and Notebooks Retention and Provenance - Portal Walkthrough

Step-by-step governance workflow for inventorying Copilot Pages, OneNote Notebooks, and Loop component storage; scoping retention policies; and capturing branch, embed, and lineage evidence.

## Prerequisites

- [Control 3.2 Data Retention Policies](../../../controls/pillar-3-compliance/3.2-data-retention-policies.md) tenant-wide retention baseline is in place.
- [Control 3.1 Audit Logging](../../../controls/pillar-3-compliance/3.1-copilot-audit-logging.md) unified audit logging is enabled.
- [Control 3.11 Record Keeping](../../../controls/pillar-3-compliance/3.11-record-keeping.md) eDiscovery and legal hold workflow is documented.
- Named retention owner for each artifact type and an evidence retention path.

## Access Paths

| Portal | Path | Why it matters |
|--------|------|----------------|
| Microsoft Purview portal | Solutions > Data Lifecycle Management > Retention policies | Scopes retention across Loop workspaces, OneDrive, SharePoint, Exchange |
| Microsoft Purview portal | Solutions > Audit | Captures Pages branch, Notebook edit, and Loop component lifecycle events |
| SharePoint Admin Center | Sites > Active sites | Identifies Notebook and Loop workspace storage locations |
| Microsoft Loop app | Workspaces | Validates Pages and Loop component storage in scope |

## Steps

### Step 1: Inventory artifact storage locations

Enumerate Loop workspaces (Pages and Loop components), OneNote Notebooks, and the OneDrive / SharePoint / Exchange locations that host them. Without a complete inventory, retention scoping risks gaps that examiners will identify.

### Step 2: Validate retention scope per artifact type

Confirm the tenant retention policy covers Loop workspaces, Notebook storage locations, and the SharePoint sites hosting embedded Loop components. Flat retention is necessary but is not sufficient for branch and embed lineage — see Step 4.

### Step 3: Enable lifecycle audit operations

Verify unified audit logging captures Pages branch events (create, branch, edit, delete), Notebook edits, and Loop component lifecycle events (create, embed, edit, delete). These events feed the lineage trail described in [Control 3.14](../../../controls/pillar-3-compliance/3.14-copilot-pages-notebooks-retention.md).

### Step 4: Establish branch-aware and embed-aware lineage capture

For Pages, design the retention process so each branch is preserved as an independent retained item with a recorded link to its parent. For Loop components, capture the host references each time a component is embedded or unembedded so cross-host lineage can be reconstructed.

### Step 5: Wire artifacts into eDiscovery and legal hold

Confirm Pages, Notebooks, and Loop components can be searched and held under [Control 3.11](../../../controls/pillar-3-compliance/3.11-record-keeping.md). Validate that holds preserve branched Pages and embedded Loop components, not only the parent location.

### Step 6: Schedule periodic attestation

Schedule a quarterly attestation that branch events for in-scope Pages have been captured and that no branch is unaccounted for. The attestation forms the core evidence artifact for the Regulated tier.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Include all three artifact types in tenant retention policies and enable lifecycle audit operations. |
| **Recommended** | Apply branch-aware retention for Pages and section-aware scoping for Notebooks used in supervisory or compliance workflows. |
| **Regulated** | All Recommended controls plus: examiner-ready evidence pack of all in-scope artifact versions for a sampling period, and quarterly attestation of branch and embed lineage completeness. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) to inventory storage and pull lifecycle audit evidence.
- Use [Verification & Testing](verification-testing.md) to validate retention scope and lineage capture.
- Keep [Troubleshooting](troubleshooting.md) available for branch, embed, and hold issues.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 3.14](../../../controls/pillar-3-compliance/3.14-copilot-pages-notebooks-retention.md)
