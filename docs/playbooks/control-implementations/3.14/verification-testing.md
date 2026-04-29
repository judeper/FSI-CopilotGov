# Control 3.14: Copilot Pages and Notebooks Retention and Provenance - Verification & Testing

Test cases and evidence collection for validating retention scope, branch and embed lineage capture, eDiscovery integration, and attestation completeness.

## Test Cases

### Test 1: Retention Policies Cover All Artifact Storage Locations

- **Objective:** Confirm tenant retention policies scope Loop workspaces, Notebook locations, and Loop-component-hosting SharePoint sites.
- **Expected Result:** Every inventoried storage location is associated with an active retention policy meeting the documented minimum retention.
- **Evidence:** Inventory CSVs reconciled to the retention policy scope export.

### Test 2: Pages Branch Events Are Captured and Linked

- **Objective:** Validate that branching a Page produces an audit event and a lineage record linking child to parent.
- **Expected Result:** A controlled branch generates a `CopilotPageBranched` audit entry that the lineage report links to the parent Page.
- **Evidence:** `pages-branch-lineage.csv` and the test-branch screenshot.

### Test 3: Notebook Edits Are Logged at the Page Level

- **Objective:** Confirm OneNote edits in supervisory or compliance Notebooks are captured.
- **Expected Result:** Edits to in-scope sections appear in the lifecycle audit extract with user, timestamp, and target identity.
- **Evidence:** Audit-event extract for the in-scope Notebook sections.

### Test 4: Loop Component Embeddings Are Tracked Across Hosts

- **Objective:** Validate that embedding the same Loop component in multiple hosts produces a host-reference map.
- **Expected Result:** A controlled embed yields entries in `loop-embed-map.csv` for each host, and a removal yields the corresponding `LoopComponentRemoved` entry.
- **Evidence:** Embed map and the controlled-test transcript.

### Test 5: eDiscovery Hold Preserves Branched and Embedded Content

- **Objective:** Confirm a legal hold under [Control 3.11](../../../controls/pillar-3-compliance/3.11-record-keeping.md) preserves branched Pages and embedded Loop components, not only the parent.
- **Expected Result:** Held set includes the parent Page, the branched Page, the Loop component, and the host references.
- **Evidence:** Hold export and the corresponding inventory.

### Test 6: Quarterly Attestation Is Complete and Reviewed

- **Objective:** Validate the Regulated-tier attestation that branch events have been captured and reconciled.
- **Expected Result:** Attestation shows zero unaccounted branches for the period and is signed by the named reviewer.
- **Evidence:** Attestation record with reviewer signature.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Storage inventory snapshots | PowerShell / Graph | CSV | Per retention policy |
| Lifecycle audit extract | Unified audit log | CSV | 7 years for regulated evidence sets |
| Pages branch lineage report | PowerShell post-processing | CSV | 7 years for regulated evidence sets |
| Loop component embed map | PowerShell post-processing | CSV | 7 years for regulated evidence sets |
| eDiscovery hold export | Purview | CSV / PDF | Per legal hold policy |
| Quarterly attestation record | Governance workspace | PDF / Markdown | 7 years for regulated evidence sets |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Troubleshooting](troubleshooting.md)

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 3.14](../../../controls/pillar-3-compliance/3.14-copilot-pages-notebooks-retention.md)
