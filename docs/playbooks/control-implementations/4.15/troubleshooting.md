# Control 4.15: Copilot Cowork Governance - Troubleshooting

Common issues and resolution steps for governing Microsoft 365 Copilot Cowork after its June 2026 general availability, including access gating (usage-based billing + discovery), model toggles, local browser use, plugin and Customize-page extensibility, and consumption limits.

## Common Issues

### Issue 1: Users Cannot Access Cowork

- **Symptoms:** Users in the pilot cannot open or use Cowork.
- **Resolution:** In **M365 Admin Center > Copilot > Cost management**, confirm that usage-based billing is enabled for the users or groups in scope and that a spending policy is configured. Cowork access is gated on usage-based billing setup; discovery alone does not grant access.

### Issue 2: Cowork Is Not Visible to Any Users

- **Symptoms:** Users report Cowork is not surfaced in Microsoft 365 Copilot.
- **Resolution:** Check whether the intended access posture is billing-only (targeted users only) or billing + discovery (broader awareness with request flow). If broad discovery is intended, turn on **M365 Admin Center > Copilot > Settings > AI experiences enabled by usage-based billing**. If discovery is deliberately off, communicate the pilot scope to users so they understand why Cowork is not visible.

### Issue 3: Unexpected Access Requests

- **Symptoms:** Admins receive Cowork access requests from users outside the approved pilot.
- **Resolution:** If discovery is on tenant-wide, users without billing enabled can request access from within Cowork. Route each request through the documented review workflow (policy, cost, compliance) before enabling billing for the requester. If request volume is unmanageable, consider turning discovery off and re-communicating the pilot scope.

### Issue 4: Cowork Activity from Users Outside the Approved Scope

- **Symptoms:** `cowork-out-of-scope-activity.csv` is non-empty.
- **Resolution:** Compare the users with activity against the Cost management billing-scope export. If billing was enabled for a user outside the approved pilot, verify the approval basis or remove the user from scope. If billing scope is correct but out-of-scope users still appear, re-run the audit pull and confirm that the reconciliation input is current.

### Issue 5: Claude Fable 5 (Preview) Enabled Without Retention Review

- **Symptoms:** The **Claude Fable 5 (Preview)** model is on in **M365 Admin Center > Copilot settings**, but the provider data-retention posture has not been reviewed and approved.
- **Resolution:** Turn Fable 5 (Preview) off. Fable 5 (Preview) requires the model provider to retain prompts and responses; do not enable it until legal, privacy, and compliance have reviewed the retention terms and approved the use for the intended data classes. Cowork displays a banner while Fable 5 is selected — treat that banner as an in-product reminder, not a substitute for governance.

### Issue 6: Anthropic Model Family Was Disabled Without Coordination

- **Symptoms:** Pilot users report their Cowork model choices have narrowed unexpectedly.
- **Resolution:** In **M365 Admin Center > Copilot settings**, check whether the Anthropic model family toggle was disabled. Coordinate with the change register — if the change was intentional, communicate the remaining model choices (for example, GPT 5.5) to the pilot; if unintentional, restore the previous state and document the incident.

### Issue 7: Cowork Browsing Is Enabled Without a Documented Review

- **Symptoms:** The **Cowork Browsing** toggle is on but no browser-use review record exists.
- **Resolution:** Turn the toggle off, complete a documented review that references the tenant's Conditional Access, Microsoft Purview DLP, browser management policy, and any site allow/block/view-only rules that should apply, then re-enable if approved. Local browser use is a preview feature at the time of last verification.

### Issue 8: Browser Task Fails or Is Blocked

- **Symptoms:** A Cowork browser task cannot complete, or Cowork reports the site is blocked.
- **Resolution:** Because browser tasks run in the user's local Microsoft Edge, they inherit web filtering, Conditional Access, DLP, and browser management policy. Verify that Edge is installed and up to date, that the user is signed in to Edge with the same work/school account used for Cowork, and that no policy is blocking the target site or action. If the block is intentional, the failure is expected; document the outcome.

### Issue 9: Unapproved Plugin or Uploaded Package Available to Cowork

- **Symptoms:** A plugin, uploaded plugin package, or shared custom skill not on the approved inventory is usable in Cowork.
- **Resolution:** Restrict the plugin through the admin plugin controls, remove the uploaded package or skill (or restrict its sharing scope) from **Cowork > Customize**, reconcile the inventory, and route the item through extensibility governance under [Control 4.13](../../../controls/pillar-4-operations/4.13-extensibility-governance.md).

### Issue 10: Consumption Trending Over Budget

- **Symptoms:** Consumption reporting in **Copilot > Cost management** shows spend on track to exceed the approved budget.
- **Resolution:** Review per-user or per-group consumption limits, tighten them where appropriate, and identify the activity classes driving spend (model responses, tools/skills, image generation, browser tasks). Communicate limit changes to the pilot and record the decision.

### Issue 11: Cowork Activity Missing from Audit

- **Symptoms:** Expected Cowork events do not appear in Purview audit pulls.
- **Resolution:** Confirm unified audit logging is enabled tenant-wide, and re-run the audit pull with a wider operation set and the Cowork filter. Because Microsoft's audit-log-activities reference evolves, re-verify the operation list against current documentation. Document any preview-related coverage gap with a remediation owner. For browser task events specifically, confirm that browser use is enabled and that at least one browser task has been attempted in the reporting window.

## Diagnostic Steps

1. Confirm the intended access posture (billing scope, discovery on/off) against **Copilot > Cost management** and **Copilot > Settings > AI experiences enabled by usage-based billing**.
2. Confirm model toggle state under **Copilot settings** (Anthropic family, Fable 5 (Preview)).
3. Confirm the **Cowork Browsing** toggle state under **Copilot > Settings > View All > Cowork settings**.
4. Reconcile Cowork users against the approved pilot group.
5. Re-run the audit pull and review out-of-scope activity.
6. Reconcile the plugin, uploaded-package, and custom-skill inventory against approvals.
7. Review consumption reporting and per-user/per-group limits.
8. Validate Purview coverage against the Purview for Cowork guidance.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Low | Documentation gap, single out-of-scope activity, or single access-request delay | Governance analyst |
| Medium | Access-posture drift, model-toggle drift (including unreviewed Fable 5 (Preview) enablement), browser-toggle drift, or unapproved plugin/package/skill available | Governance lead and M365 admin |
| High | Cowork enabled for a regulated population without supervisory review, or consumption significantly exceeding the approved budget | Compliance lead and M365 admin |
| Critical | Agentic Cowork action (including browser use) against regulated data outside approved governance, or model with provider data retention used on regulated data without approval | CISO, compliance officer, incident-response lead |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Verification & Testing](verification-testing.md)

*FSI Copilot Governance Framework v1.7.1 - July 2026*
- Back to [Control 4.15](../../../controls/pillar-4-operations/4.15-copilot-cowork-governance.md)
