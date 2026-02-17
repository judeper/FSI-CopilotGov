# Control 3.8: Model Risk Management Alignment (OCC 2011-12 / SR 11-7) — Troubleshooting

Common issues and resolution steps for model risk management compliance related to Copilot.

## Common Issues

### Issue 1: Model Inventory Entry Incomplete or Outdated

- **Symptoms:** OCC examiners flag the Copilot model inventory entry as lacking required fields or containing stale information.
- **Root Cause:** Model inventory was not updated after Copilot feature updates, or initial entry used incomplete documentation.
- **Resolution:**
  1. Review the latest Microsoft Copilot AI documentation from the Service Trust Portal.
  2. Update all model inventory fields with current information.
  3. Establish a trigger-based update process tied to Microsoft's Copilot release cycle.
  4. Assign a dedicated model owner responsible for ongoing inventory maintenance.

### Issue 2: Insufficient Performance Monitoring Data

- **Symptoms:** Model validation reviewers report that performance metrics are too limited to assess model quality effectively.
- **Root Cause:** Feedback collection may be limited by low user engagement, or the audit log may not capture all relevant quality indicators.
- **Resolution:**
  1. Encourage Copilot users to provide feedback (thumbs up/down) on responses.
  2. Supplement audit log data with direct user surveys conducted quarterly.
  3. Implement structured output quality reviews by sampling Copilot-generated content.
  4. Consider deploying additional monitoring through Viva Insights Copilot metrics.

### Issue 3: Vendor Documentation Not Available from Microsoft

- **Symptoms:** Required third-party risk documentation (SOC reports, AI assessments) is delayed or unavailable from Microsoft.
- **Root Cause:** Microsoft's reporting cycle may not align with the firm's assessment schedule, or access to the Service Trust Portal may be restricted.
- **Resolution:**
  1. Verify Service Trust Portal access for the compliance team.
  2. Contact the Microsoft account team to request documentation availability timelines.
  3. Use alternative evidence such as Microsoft's published AI principles and compliance certifications as interim documentation.
  4. Document the gap and timeline in the vendor risk assessment.

### Issue 4: Risk Tier Classification Disputed

- **Symptoms:** Internal model risk management team and business stakeholders disagree on the appropriate risk tier for Copilot.
- **Root Cause:** AI-generated content tools do not fit neatly into traditional model tiering frameworks designed for quantitative financial models.
- **Resolution:**
  1. Reference OCC and Fed guidance on AI/ML model classification.
  2. Consider the materiality of Copilot outputs on business decisions and client-facing activities.
  3. Apply the higher tier when use cases span multiple risk levels.
  4. Document the rationale for the selected tier in the model inventory.
  5. Seek guidance from the firm's model risk management committee.

## Diagnostic Steps

1. **Review model inventory:** Verify all required fields are populated and current.
2. **Check performance metrics:** Run the feedback and quality metrics scripts to confirm data availability.
3. **Validate vendor docs:** Verify that all Microsoft documentation is current and accessible.
4. **Assess monitoring coverage:** Confirm that performance monitoring covers all Copilot use cases.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | OCC/Fed examination finding on model risk | Chief Risk Officer + Model Risk Committee |
| High | Model validation overdue by more than 30 days | Model Risk Management team lead |
| Medium | Performance metrics showing degradation trend | Model owner + IT monitoring team |
| Low | Documentation updates needed | Assign to model owner for next update cycle |

## Related Resources

- [Control 3.7: Regulatory Reporting](../3.7/portal-walkthrough.md)
- [Control 3.9: AI Disclosure and Transparency](../3.9/portal-walkthrough.md)
- [OCC Bulletin 2011-12](https://www.occ.gov/news-issuances/bulletins/2011/bulletin-2011-12.html)
