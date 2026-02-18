# Control 3.5: FINRA Rule 2210 Compliance for Copilot-Drafted Communications — Troubleshooting

Common issues and resolution steps for FINRA 2210 compliance monitoring of Copilot-drafted communications.

## Common Issues

### Issue 1: Copilot-Drafted Content Bypassing Detection

- **Symptoms:** Known non-compliant Copilot-drafted communications are not flagged by the policy.
- **Root Cause:** Detection rules may not cover the specific language patterns Copilot generates, or the Copilot interaction channel is not included in the policy scope.
- **Resolution:**
  1. Review the undetected communication to identify the specific language used.
  2. Add the language pattern to the keyword dictionary or sensitive information type.
  3. Verify the policy includes Copilot interactions as a supervised location.
  4. Consider expanding trainable classifier training data to include Copilot-style language.

### Issue 2: Excessive Review Volume from Copilot-Generated Content

- **Symptoms:** The review queue is overwhelmed with Copilot-drafted items, many of which are false positives.
- **Root Cause:** Copilot may generate language patterns that trigger broad keyword matches even when the content is compliant.
- **Resolution:**
  1. Analyze the top false positive patterns from Copilot-generated content.
  2. Add exclusion rules for common Copilot phrasing that is flagged incorrectly.
  3. Adjust confidence thresholds for sensitive information types.
  4. Implement a tiered review process with automated resolution for low-confidence matches.

### Issue 3: Pre-Send Review Blocking Legitimate Communications

- **Symptoms:** Compliant client communications are being held in supervisory review, causing delivery delays and client complaints.
- **Root Cause:** Pre-send review criteria are too broad, capturing compliant communications alongside non-compliant ones.
- **Resolution:**
  1. Review the held communications to identify false positive patterns.
  2. Narrow the pre-send review scope to high-confidence matches only.
  3. Create an expedited review lane for time-sensitive communications.
  4. Consider allowing low-risk communications to proceed with post-send review instead.

### Issue 4: FINRA Category Misclassification

- **Symptoms:** Communications are classified under the wrong FINRA 2210 category (e.g., correspondence classified as retail communication).
- **Root Cause:** Recipient count detection may not properly account for distribution lists, or institutional vs. retail classification is based on incomplete data.
- **Resolution:**
  1. Verify distribution list expansion is correctly calculating recipient counts.
  2. Update the institutional investor classification criteria in the policy.
  3. Ensure CRM integration is providing accurate client classification data.
  4. Implement manual override capabilities for reviewers to correct misclassifications.

### Issue 5: AI Washing Detection False Positives (Legitimate Copilot Capability Descriptions)

- **Symptoms:** Compliant communications that legitimately describe what Copilot does — such as "Microsoft 365 Copilot assists our team in drafting communications" — are being flagged as AI washing violations.
- **Root Cause:** AI washing keyword policies may be too broad, catching factual, balanced descriptions of Copilot's role alongside the unsubstantiated promotional claims the policy is intended to target. The distinction is between accurate, limited descriptions of AI assistance (compliant) and promissory or capability-exaggerating claims (non-compliant under FINRA Rule 2210(d)(1)(A) and the Investment Advisers Act Section 206).
- **Resolution:**
  1. Review the falsely flagged communications and identify the specific triggering phrases.
  2. Add exclusion refinements for factual, balanced AI descriptions — for example, exclude phrases like "Copilot assists" or "AI helps draft" when not paired with outcome guarantees.
  3. Narrow keyword patterns to focus on promissory or absolute language (e.g., "guarantees", "eliminates risk", "always", "certain to") rather than simply the presence of "AI" or "Copilot" terms.
  4. Conduct quarterly review of AI washing detection accuracy using a labeled test set of 20+ communications — both compliant AI descriptions and genuinely non-compliant AI washing claims.
  5. Document the refined keyword policy in the firm's written supervisory procedures so reviewers understand the distinction between acceptable AI transparency and prohibited AI washing.

## Diagnostic Steps

1. **Check policy health:** Navigate to Communication compliance > Policies and verify status.
2. **Review match patterns:** Analyze the last 50 matches to identify common triggers and false positive rates.
3. **Verify user scope:** Confirm all registered representatives with Copilot access are in the supervised group.
4. **Test detection rules:** Send a test communication with known prohibited language to verify detection.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Non-compliant communications reaching clients undetected | Chief Compliance Officer + FINRA reporting review |
| High | Pre-send review failures causing systematic delivery delays | Compliance team + IT for policy optimization |
| Medium | Detection accuracy below target thresholds | Schedule policy tuning session |
| Low | Minor classification inconsistencies | Document and address in quarterly review |

## Related Resources

- [Control 3.4: Communication Compliance Monitoring](../3.4/portal-walkthrough.md)
- [Control 3.6: Supervision and Oversight](../3.6/portal-walkthrough.md)
- [FINRA Rule 2210 reference](https://www.finra.org/rules-guidance/rulebooks/finra-rules/2210)
