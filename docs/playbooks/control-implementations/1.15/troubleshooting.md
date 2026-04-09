# Control 1.15: SharePoint Permissions Drift Detection - Troubleshooting

Common issues and resolution steps for permissions-baseline capture, drift scanning, and approval-gated reversion.

## Common Issues

### Issue 1: Baseline Snapshot Is Incomplete

- **Symptoms:** Expected groups, sharing settings, or libraries are missing from the baseline output.
- **Resolution:** Review the baseline manifest, confirm all in-scope sites are listed, and re-capture the baseline only after the approved state is confirmed.

### Issue 2: Approved Changes Are Repeatedly Flagged as Drift

- **Symptoms:** Findings keep recurring for changes that were approved through CAB or exception workflow.
- **Resolution:** Map approved changes to the baseline refresh process and record the approval identifier alongside the drift finding.

### Issue 3: Drift Severity Is Too High or Too Low

- **Symptoms:** Group membership changes or sharing-setting changes are classified inconsistently.
- **Resolution:** Review the policy or risk model with compliance and SharePoint operations before changing thresholds.

### Issue 4: Reversion Package Cannot Be Actioned

- **Symptoms:** Reversion output exists, but the organization cannot determine who should approve or execute it.
- **Resolution:** Update the site inventory with named owners and approvers, then rebuild the approval package.

### Issue 5: Alerting or Notifications Are Missing

- **Symptoms:** Drift findings are written to output, but no stakeholders are notified.
- **Resolution:** Validate notification routing, test the alert path with a controlled sample finding, and document fallback escalation steps.

## Diagnostic Steps

1. Validate the approved baseline manifest and capture date.
2. Review the latest drift report for repeated or unexplained findings.
3. Compare flagged changes to CAB, exception, or incident records.
4. Inspect the auto-revert or approval policy for severity mismatches.
5. Test the notification path with a controlled sample finding.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Low | Minor baseline mismatch or documentation gap | SharePoint admin or governance analyst |
| Medium | Repeated false drift or missing change references | Governance lead and CAB owner |
| High | High-risk drift cannot be triaged or approved | Compliance lead and SharePoint admin |
| Critical | Unauthorized expansion of access to regulated or privileged content | CISO, compliance officer, and incident-response lead |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md)
- [PowerShell Setup](powershell-setup.md)
- [Verification & Testing](verification-testing.md)

*FSI Copilot Governance Framework v1.3 - April 2026*
