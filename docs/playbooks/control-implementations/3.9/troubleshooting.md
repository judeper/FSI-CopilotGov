# Control 3.9: AI Disclosure, Transparency, and SEC Marketing Rule — Troubleshooting

Common issues and resolution steps for AI disclosure and transparency controls.

## Common Issues

### Issue 1: Sensitivity Label Content Markings Not Appearing

- **Symptoms:** The AI-Assisted Content label is applied but header/footer markings are not visible in the document.
- **Root Cause:** Content marking settings may not be enabled in the label policy, or the application does not support content markings.
- **Resolution:**
  1. Verify the label configuration includes content marking: `Get-Label -Identity "AI-Assisted-Content" | Select *Marking*`
  2. Confirm the label policy is published and distributed: check `DistributionStatus`.
  3. Ensure the user is running a supported version of Office that renders content markings.
  4. Test in Word desktop (full support) before testing in web or mobile apps.

### Issue 2: DLP Policy Not Detecting Copilot-Assisted Content

- **Symptoms:** External emails drafted with Copilot assistance are sent without AI disclosure and are not blocked by DLP.
- **Root Cause:** The DLP rule conditions may not correctly identify Copilot-assisted content, or the sensitivity label is not being automatically applied.
- **Resolution:**
  1. Verify the DLP policy is enabled and distributed.
  2. Check that the DLP rule conditions correctly reference the AI-Assisted Content label or Copilot metadata.
  3. Consider implementing auto-labeling to apply the AI-Assisted Content label to Copilot-generated content automatically.
  4. As an interim measure, rely on user training and communication compliance review for detection.

### Issue 3: Users Bypassing AI Disclosure Requirements

- **Symptoms:** Users override DLP policy tips and send undisclosed AI-assisted content externally.
- **Root Cause:** DLP policy is set to "Block with override" allowing users to bypass, or users are not trained on disclosure requirements.
- **Resolution:**
  1. Review override justifications in the DLP incident reports.
  2. If overrides are excessive, change the policy action from "Block with override" to "Block" for high-risk groups.
  3. Conduct targeted training for teams with high override rates.
  4. Add override usage to supervisory reporting for compliance review.

### Issue 4: SEC Marketing Rule Classification Inaccurate

- **Symptoms:** Non-marketing content is being flagged as requiring SEC Marketing Rule review, or actual marketing content is missed.
- **Root Cause:** Detection conditions may be too broad or too narrow, or user groups are not correctly scoped.
- **Resolution:**
  1. Review the policy scope to ensure only marketing and client-facing teams are targeted.
  2. Refine keyword lists to distinguish marketing language from general business communication.
  3. Add exclusion conditions for internal communications and non-client content.
  4. Consider using trainable classifiers specifically trained on the firm's marketing content.

## Diagnostic Steps

1. **Check label deployment:** `Get-LabelPolicy | Select Name, Enabled, DistributionStatus`
2. **Review DLP incidents:** `Get-DlpDetailReport -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date)`
3. **Verify content markings:** Open a labeled document and check for header/footer visibility.
4. **Test DLP enforcement:** Send a test email to an external address without disclosure language.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Undisclosed AI content reaching clients at scale | Chief Compliance Officer + Marketing compliance |
| High | DLP enforcement failing to block non-compliant content | IT security + Compliance team |
| Medium | High override rate on DLP policies | Compliance team — training and policy review |
| Low | Minor label formatting issues | IT support for Office configuration |

## Related Resources

- [Control 3.5: FINRA Rule 2210 Compliance](../3.5/portal-walkthrough.md)
- [Control 3.10: SEC Reg S-P Privacy](../3.10/portal-walkthrough.md)
