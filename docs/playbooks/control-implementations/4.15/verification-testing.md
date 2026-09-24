# Control 4.15: Copilot Cowork Governance - Verification & Testing

Test cases and evidence collection for validating access posture (Cowork-selecting spending policies and discovery), access-request handling, model controls and provider data-retention review, the Cowork Browsing tenant toggle, plugin and custom-skill inventory, consumption limits, and Purview/audit coverage for Microsoft 365 Copilot Cowork at general availability.

## Test Cases

### Test 1: Access Posture Matches the Approved Decision

- **Objective:** Confirm usage-based billing scope and the discovery setting match the documented pilot decision.
- **Expected Result:** The Cost management export lists only users/groups in the approved pilot; the discovery setting is off (or matches the approved posture), and both decisions are recorded with an approver.
- **Evidence:** Cost management billing-scope export, discovery-setting screenshot/export, and the access-posture decision record.

### Test 2: Access Requests Are Handled Under a Documented Workflow

- **Objective:** Validate that user access requests received when discovery is on are routed through a documented review.
- **Expected Result:** Each request has a reviewer, an outcome (approved or denied), and a policy, cost, and compliance basis recorded.
- **Evidence:** Access-request register.

### Test 3: Model Toggles Match Policy

- **Objective:** Confirm the Anthropic model family and any current model-specific controls match the documented decisions.
- **Expected Result:** Models with provider data-retention implications are disabled for regulated data unless provider data retention has been reviewed and approved for the intended use; the Anthropic-family control reflects the documented posture.
- **Evidence:** Copilot settings screenshots/exports for both toggles and the approval records.

### Test 4: Cowork Browsing Toggle Reflects Documented Review

- **Objective:** Validate that the **Cowork Browsing** tenant toggle is off, or is on only after a documented review of Conditional Access, DLP, browser management policy, and site allow/block/view-only rules.
- **Expected Result:** The toggle state matches the documented decision, and the browser-use review record references the relevant Edge, Conditional Access, and DLP policies.
- **Evidence:** Cowork Browsing toggle screenshot/export and the browser-use review record.

### Test 5: Cowork Users Stay Within the Approved Scope

- **Objective:** Confirm the users in Cowork-selecting spending policies remain within the approved pilot group, and no out-of-scope Cowork activity is observed.
- **Expected Result:** `cowork-out-of-scope-activity.csv` is empty after reconciliation; any exceptions have a documented approval.
- **Evidence:** Cost management billing-scope export reconciled to `cowork-approved-members.csv`, and the audit-derived activity report.

### Test 6: Plugin, Uploaded Package, and Custom Skill Inventory Matches Approvals

- **Objective:** Confirm plugins available to Cowork, uploaded plugin packages, and user-created/uploaded custom skills (with their sharing scope) match the approved inventory.
- **Expected Result:** Inventory matches; unapproved plugins, packages, or skills are removed or documented as exceptions.
- **Evidence:** Plugin inventory export, Customize > Plugins uploaded-package export, Customize > Skills export, and the approved inventory.

### Test 7: Consumption Limits Match the Approved Budget

- **Objective:** Validate that per-user or per-group consumption limits reflect the approved pilot budget and that consumption reporting is reviewed on cadence.
- **Expected Result:** Limits match the budget; consumption reporting shows model responses, tools/skills, image generation, and browser tasks trending within budget.
- **Evidence:** Consumption-limits export and the most recent consumption reporting review record.

### Test 8: Purview and Audit Coverage Confirmed

- **Objective:** Validate that Cowork is included in the tenant's Purview posture (per the Purview for Cowork guidance) and that browser task events appear in the unified audit log.
- **Expected Result:** Purview policies for Cowork match current Microsoft Learn coverage: audit, sensitivity labels, insider risk, communication compliance, eDiscovery, and data lifecycle management are documented for Cowork AI interactions; DLP is not listed as supported in the Purview for Cowork table as of this verification, while the M365 roadmap lists DLP expansion. Cowork events, including browser tasks, appear in unified-audit-log pulls or gaps have a documented owner and cadence.
- **Evidence:** Purview policy export, `cowork-audit.csv`, and the documented coverage assessment.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Access-posture decision record | Governance workspace | CSV / Markdown | Per retention policy |
| Cost management billing-scope export | M365 Admin Center > Copilot > Cost management > Configuration | CSV / PDF / PNG | Per retention policy |
| Discovery-setting state | M365 Admin Center > Copilot > Settings | PDF / PNG | Per retention policy |
| Access-request register | Governance workspace | CSV / Markdown | Per retention policy |
| Anthropic-family toggle export | M365 Admin Center > Copilot settings | PDF / PNG | Per retention policy |
| Current model-control and provider-retention evidence | M365 Admin Center > Copilot settings / current Microsoft Learn model guidance | PDF / PNG / Markdown | Per retention policy |
| Cowork Browsing toggle export | M365 Admin Center > Copilot > Settings > View All > Cowork settings | PDF / PNG | Per retention policy |
| Plugin inventory | M365 Admin Center > Integrated apps | CSV / PDF | Per retention policy |
| Uploaded plugin packages inventory | Cowork > Customize > Plugins | CSV / PDF / PNG | Per retention policy |
| Custom skills inventory | Cowork > Customize > Skills | CSV / PDF / PNG | Per retention policy |
| Consumption limits and reporting | M365 Admin Center > Copilot > Cost management > Configuration | CSV / PDF | Per retention policy |
| Cowork audit extract | Unified audit log | CSV | 7 years for regulated evidence sets |
| Out-of-scope activity report | PowerShell post-processing | CSV | Per retention policy |
| Purview policy coverage record | Governance workspace | PDF / Markdown | 7 years for regulated evidence sets |
| Approvals (billing, discovery, model, browser, plugins/skills, limits) | Governance workspace | PDF / Markdown | 7 years for regulated evidence sets |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Troubleshooting](troubleshooting.md)

*FSI Copilot Governance Framework v1.8.0 - July 2026*
- Back to [Control 4.15](../../../controls/pillar-4-operations/4.15-copilot-cowork-governance.md)
