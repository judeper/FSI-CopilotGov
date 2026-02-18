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

### Issue 4: Model Inventory Classification Debate — Tier Assignment

- **Symptoms:** Internal model risk management team and business stakeholders disagree on the appropriate risk tier for Copilot (Tier 1 vs. Tier 2 vs. Tier 3), particularly when Copilot usage spans both internal productivity and limited client-facing activities.
- **Root Cause:** AI-generated content tools do not fit neatly into traditional model tiering frameworks designed for quantitative financial models. Use cases may span multiple risk levels.
- **Resolution:**
  1. Apply the higher tier when use cases span multiple risk levels — if any approved use case involves client-facing activities or lending workflows, do not classify as Tier 3.
  2. Reference OCC Bulletin 2011-12 and SR 11-7 on the materiality of model outputs for tier determination. The key question: could Copilot outputs in the approved use cases directly influence decisions affecting clients or regulated activities?
  3. Document the full approved use-case register before tier assignment — tier follows use cases, not general capability.
  4. Seek guidance from the firm's model risk management committee and document the outcome.
  5. If Copilot usage evolves to include higher-risk activities, update the tier and associated governance promptly.

### Issue 5: Proportionality Determination for Mid-Size Institutions

- **Symptoms:** A mid-size institution (not a community bank, but not a large complex organization) is uncertain whether OCC Bulletin 2025-26 proportionality applies and what MRM tier to select.
- **Root Cause:** OCC Bulletin 2025-26 was written with community banks in mind, but the proportionality principle applies more broadly. Mid-size institutions may have legitimate grounds for a simplified MRM approach depending on Copilot usage scope.
- **Resolution:**
  1. Assess the actual risk profile: what use cases are approved, what is the volume and materiality of Copilot-assisted decisions, and what is the institution's overall complexity? Proportionality should reflect actual risk, not just asset size.
  2. Document the proportionality analysis in writing — even if the institution is not a community bank, a documented and reasoned proportionality determination is defensible in an examination.
  3. If Copilot is used only for internal productivity (meeting summaries, document drafting, research support) with no direct client impact, a simplified MRM approach aligned with OCC Bulletin 2025-26 proportionality is supportable. Cite the bulletin and the usage scope limitation in the model inventory.
  4. If examiners challenge the proportionality determination, present the documented rationale — the quality of the documentation matters as much as the tier selected.
  5. For institutions uncertain about the correct approach: consult with outside counsel or regulatory advisory specialists familiar with OCC model risk management examination practice.

### Issue 6: Copilot Model Status Under SR 11-7 Disputed

- **Symptoms:** An examiner or internal legal team questions whether M365 Copilot meets the SR 11-7 definition of a "model," creating uncertainty about whether any MRM framework is required.
- **Root Cause:** SR 11-7 defines models as quantitative methods applying "statistical, economic, financial, or mathematical theories, techniques, and assumptions." Copilot is an LLM — not a traditional quantitative model — and there is genuine ambiguity about how the definition applies.
- **Resolution:**
  1. The consensus regulatory and industry view is to treat Copilot as a model subject to MRM (at some tier), rather than arguing it falls outside the definition. This is the safer compliance posture.
  2. Document the model status determination in the inventory: "M365 Copilot is classified as a vendor-provided general-purpose LLM. It straddles the SR 11-7 model definition. The institution has elected to include it in the model inventory at [Tier X] as a prudent governance approach, consistent with the 2023 Interagency Guidance on AI."
  3. Reference the 2023 Interagency AI Guidance, which confirms that existing risk management frameworks (including MRM) apply to AI technologies.
  4. Avoid the position that Copilot requires no governance — this is the posture most likely to draw examiner scrutiny.

## Diagnostic Steps

1. **Review model inventory:** Verify all required fields are populated and current, including tier classification with documented rationale.
2. **Check performance metrics:** Run the feedback and quality metrics scripts to confirm data availability.
3. **Validate vendor docs:** Verify that all Microsoft documentation is current and accessible.
4. **Assess monitoring coverage:** Confirm that performance monitoring covers all approved Copilot use cases.
5. **Review proportionality documentation:** Confirm that community banks or mid-size institutions applying a simplified MRM approach have documented rationale citing OCC Bulletin 2025-26.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | OCC/Fed examination finding on model risk | Chief Risk Officer + Model Risk Committee |
| High | Model validation overdue by more than 30 days | Model Risk Management team lead |
| High | Tier classification dispute with examiner | Chief Risk Officer + outside counsel |
| Medium | Performance metrics showing degradation trend | Model owner + IT monitoring team |
| Medium | Proportionality determination challenged | Model Risk Committee + compliance officer |
| Low | Documentation updates needed | Assign to model owner for next update cycle |

## Related Resources

- [Control 3.7: Regulatory Reporting](../3.7/portal-walkthrough.md)
- [Control 3.9: AI Disclosure and Transparency](../3.9/portal-walkthrough.md)
- [OCC Bulletin 2011-12](https://www.occ.gov/news-issuances/bulletins/2011/bulletin-2011-12.html)
- [OCC Bulletin 2025-26 (Community Bank MRM Proportionality)](https://www.occ.gov/news-issuances/bulletins/2025/bulletin-2025-26.html)
