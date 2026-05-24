# SR 26-2 / OCC Bulletin 2026-13: Model-Risk Transition Readiness

Guidance for FSI organizations navigating the April 2026 interagency model-risk management updates and the explicit generative AI exclusion.

!!! warning "Disclaimer"
    This module is provided for informational purposes only and does not constitute legal or regulatory advice. The regulatory interpretation of SR 26-2 and OCC Bulletin 2026-13 is evolving — consult legal counsel and your primary regulator for institution-specific guidance.

---

## Background

In April 2026, the Federal Reserve Board issued **SR 26-2** and the OCC issued **OCC Bulletin 2026-13**, updating the interagency framework for model risk management. These issuances supersede the prior guidance:

- **SR 11-7** (Federal Reserve, April 2011) — Guidance on Model Risk Management
- **OCC Bulletin 2011-12** (OCC, April 2011) — Sound Practices for Model Risk Management

### The Generative AI Exclusion

SR 26-2 and OCC Bulletin 2026-13 **explicitly exclude generative AI and agentic AI systems** from the updated model-risk framework. The exclusion acknowledges that generative AI presents fundamentally different risk characteristics — non-deterministic outputs, emergent behavior, and the absence of traditional model validation techniques — that require separate regulatory treatment.

**What this means for Copilot governance:**

- Microsoft 365 Copilot, as a generative AI system, is **not governed by SR 26-2 / OCC 2026-13**
- The prior guidance (SR 11-7 / OCC Bulletin 2011-12) remains the **most recent applicable interagency guidance** for generative AI model-risk management
- Organizations should continue applying SR 11-7 / OCC 2011-12 principles to their Copilot deployments until separate generative AI guidance is issued
- The exclusion does not mean generative AI is unregulated — it means the agencies have deferred comprehensive guidance to a future issuance

!!! info "Regulatory Timeline"
    The interagency agencies have indicated that separate generative AI model-risk guidance is under development. FSI organizations should monitor Federal Reserve, OCC, and FDIC communications for the forthcoming generative AI framework. Until that guidance is issued, SR 11-7 / OCC 2011-12 principles remain the applicable standard.

---

## Impact Assessment: What Changes and What Does Not

### What SR 26-2 / OCC 2026-13 Changes (for Traditional Models)

| Area | Prior (SR 11-7 / OCC 2011-12) | Updated (SR 26-2 / OCC 2026-13) |
|------|-------------------------------|----------------------------------|
| **Scope** | Models used for decision-making, financial reporting, regulatory compliance | Same, but with explicit exclusions for generative AI and agentic AI |
| **Validation requirements** | Effective challenge, independent validation | Enhanced validation frequency and documentation requirements |
| **Board oversight** | General board awareness | Strengthened board reporting and accountability requirements |
| **Third-party model risk** | General vendor risk | More detailed third-party model due diligence and ongoing monitoring |
| **Inventory requirements** | Model inventory recommended | Model inventory mandated with specific metadata fields |

### What Does NOT Change for Copilot (Generative AI Remains Under SR 11-7 / OCC 2011-12)

| Copilot Governance Area | Applicable Guidance | Framework Control |
|------------------------|--------------------|--------------------|
| Model inventory — documenting Copilot in the firm's AI system inventory | SR 11-7 / OCC 2011-12 principles (interim) | [Control 3.8](../../controls/pillar-3-compliance/3.8-model-risk-management.md) |
| Output validation — establishing review procedures for Copilot-generated content | SR 11-7 / OCC 2011-12 principles (interim) | [Control 3.8](../../controls/pillar-3-compliance/3.8-model-risk-management.md), [Control 3.5](../../controls/pillar-3-compliance/3.5-finra-2210-compliance.md) |
| Ongoing monitoring — tracking Copilot behavior and output quality | SR 11-7 / OCC 2011-12 principles (interim) | [Control 4.5](../../controls/pillar-4-operations/4.5-usage-analytics.md) |
| Vendor risk — Microsoft as the model provider | SR 11-7 / OCC 2011-12 + OCC Bulletin 2023-17 (third-party risk) | [Control 1.10](../../controls/pillar-1-readiness/1.10-vendor-risk-management.md) |
| Board reporting — generative AI risk reporting | SR 11-7 / OCC 2011-12 principles (interim) | [Control 3.8](../../controls/pillar-3-compliance/3.8-model-risk-management.md) |
| Third-party model governance — Anthropic, xAI | SR 11-7 / OCC 2011-12 + OCC Bulletin 2023-17 | [Control 3.8a](../../controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md) |

---

## Readiness Checklist

Organizations should complete the following steps to maintain model-risk compliance during the transition period.

### Step 1: Classify AI Systems by Applicable Guidance

Separate the firm's AI/model inventory into two categories:

| Category | Applicable Guidance | Action Required |
|----------|--------------------|--------------------|
| **Traditional models** (credit scoring, pricing, fraud detection, AML, valuation) | SR 26-2 / OCC 2026-13 | Update model-risk policies and validation procedures to meet the new requirements |
| **Generative and agentic AI** (Microsoft 365 Copilot, Copilot Studio agents, third-party LLMs) | SR 11-7 / OCC 2011-12 (interim) | Continue applying current model-risk principles; prepare for future generative AI guidance |

### Step 2: Update Model-Risk Policies

- Revise the firm's model-risk management policy to reference SR 26-2 / OCC 2026-13 for traditional models
- Add an explicit section documenting the generative AI exclusion and the interim application of SR 11-7 / OCC 2011-12 principles to Copilot and other generative AI tools
- Document the rationale for the classification decision in examination-ready format

### Step 3: Review Model Inventory Documentation

- Verify that Microsoft 365 Copilot is documented in the firm's model or AI system inventory
- Confirm the inventory entry references SR 11-7 / OCC 2011-12 as the applicable guidance (not SR 26-2)
- Document any Copilot Tuning deployments with tuning corpus metadata, snapshot versions, and approval chains
- Include third-party model providers (Anthropic, xAI) if enabled, with data flow documentation

### Step 4: Prepare for Forthcoming Generative AI Guidance

- Establish a monitoring process for Federal Reserve, OCC, and FDIC communications regarding generative AI model-risk guidance
- Identify the team responsible for analyzing and implementing new generative AI guidance when issued
- Consider whether current Copilot governance controls (this framework) provide a defensible baseline that demonstrates proactive risk management
- Document the firm's position: "We are applying SR 11-7 / OCC 2011-12 principles as interim guidance pending separate generative AI issuance"

### Step 5: Examination Readiness

Prepare documentation that demonstrates:

1. **Awareness** — The firm is aware of SR 26-2 / OCC 2026-13 and the explicit generative AI exclusion
2. **Classification** — The firm has classified its AI systems and applied the correct guidance to each category
3. **Interim framework** — The firm continues to apply SR 11-7 / OCC 2011-12 principles to Copilot and generative AI systems as interim guidance
4. **Monitoring posture** — The firm is actively monitoring for forthcoming generative AI-specific guidance
5. **Controls in place** — The firm has implemented governance controls for Copilot (this framework) that demonstrate proactive model-risk management

---

## Examiner Talking Points

When discussing Copilot model-risk governance during regulatory examinations:

- "We classify Microsoft 365 Copilot as a generative AI system, which is explicitly excluded from SR 26-2 / OCC 2026-13. We continue to apply SR 11-7 / OCC Bulletin 2011-12 principles as the most recent applicable interagency guidance for generative AI model risk."
- "Our Copilot deployment is documented in our AI system inventory with risk assessment, output validation procedures, and ongoing monitoring — consistent with the SR 11-7 / OCC 2011-12 framework."
- "We are monitoring Federal Reserve, OCC, and FDIC communications for the forthcoming generative AI model-risk guidance and have identified the team responsible for implementation when it is issued."
- "For third-party model providers enabled within Copilot (Anthropic, xAI), we apply both SR 11-7 / OCC 2011-12 model-risk principles and OCC Bulletin 2023-17 third-party risk management requirements."

---

## Related Controls and Resources

- [Control 3.8 — Model Risk Management](../../controls/pillar-3-compliance/3.8-model-risk-management.md) — Primary control for Copilot model-risk governance
- [Control 3.8a — Generative AI Model Governance](../../controls/pillar-3-compliance/3.8a-generative-ai-model-governance.md) — Third-party model provider governance
- [Control 1.10 — Vendor Risk Management](../../controls/pillar-1-readiness/1.10-vendor-risk-management.md) — Microsoft and third-party vendor risk
- [State AI Laws Compliance Matrix](state-ai-laws-compliance-matrix.md) — State-level AI legislation
- [Regulatory Mappings](../../reference/regulatory-mappings.md) — Federal regulatory control mappings

---

*FSI Copilot Governance Framework v1.4.0 - April 2026*
