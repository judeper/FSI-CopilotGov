# State-Level AI Laws: Multi-State Compliance Matrix

Compliance considerations for state-level AI legislation applicable to Microsoft 365 Copilot deployments in financial services organizations operating across multiple US states.

!!! warning "Disclaimer"
    This module is provided for informational purposes only and does not constitute legal or regulatory advice. State AI legislation is evolving rapidly — consult legal counsel for current compliance requirements.

---

!!! info "Educational Reference"
    This matrix is a simplified educational reference. State AI legislation evolves rapidly — consult current sources and legal counsel.

## Overview

As of 2026, several US states have enacted or are advancing AI-specific legislation that may apply to financial institutions using Microsoft 365 Copilot. FSI organizations operating across state lines must assess compliance obligations in each jurisdiction where they operate.

This module supplements the framework's federal regulatory mappings (FINRA, SEC, OCC, FFIEC) with state-level AI governance considerations.

---

## Key State AI Laws

### Colorado AI Act (SB 24-205, amended by SB 25B-004)

**Effective date:** June 30, 2026
**Status:** Enacted, amended

For detailed Colorado-specific guidance, see [Colorado AI Act Readiness](colorado-ai-act-readiness.md).

**Key requirements for FSI Copilot deployments:**

- Deployers of "high-risk AI systems" must implement risk management programs
- Impact assessments required before deployment
- Consumer notification when AI is used in consequential decisions
- Annual review of AI systems for algorithmic discrimination

**Applicable controls:** [3.8 Model Risk Management](../../controls/pillar-3-compliance/3.8-model-risk-management.md), [3.9 AI Disclosure](../../controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md)

### Texas Responsible AI Governance Act (HB 1709)

**Effective date:** September 1, 2025
**Status:** Enacted
**Topic:** AI governance and transparency requirements for deployers of high-risk AI systems.

**Applicable controls:** [3.8 Model Risk Management](../../controls/pillar-3-compliance/3.8-model-risk-management.md), [3.9 AI Disclosure](../../controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md), [3.12 Evidence Collection](../../controls/pillar-3-compliance/3.12-evidence-collection.md)

### Utah Artificial Intelligence Policy Act (SB 149)

**Effective date:** May 1, 2024
**Status:** Enacted, in effect
**Topic:** AI disclosure requirements and prohibition on deceptive AI practices in regulated transactions.

**Applicable controls:** [3.9 AI Disclosure](../../controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md)

### Illinois AI Legislation

**Illinois Artificial Intelligence Video Interview Act (820 ILCS 42)**
**Effective date:** January 1, 2020 (already in effect)
**Status:** Enacted, in effect
**Topic:** Consent and notification requirements for AI-assisted video interviews.

**Illinois Employee AI Act (HB 3773)**
**Effective date:** January 1, 2026
**Status:** Enacted
**Topic:** Notice and disparate-impact testing requirements for AI used in employment decisions.

**Applicable controls:** [3.9 AI Disclosure](../../controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md), [4.4 Viva Suite Governance](../../controls/pillar-4-operations/4.4-viva-suite-governance.md)

### California AI Legislation

**California AB 2013 (AI Transparency Act)**
**Effective date:** January 1, 2026
**Status:** Enacted
**Topic:** Transparency disclosure requirements for AI-generated content and system capabilities.

**California SB 1047 (Safe and Secure Innovation for Frontier AI Models Act)**
**Status:** **Vetoed** by Governor Newsom, September 2024

**Applicable controls:** [3.9 AI Disclosure](../../controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md)

### New York City Local Law 144

**Effective date:** July 5, 2023
**Status:** Enacted, in effect
**Topic:** Requirements for automated employment decision tools (AEDTs), including bias audits and candidate notification.

**Applicable controls:** [3.9 AI Disclosure](../../controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md), [3.8 Model Risk Management](../../controls/pillar-3-compliance/3.8-model-risk-management.md)

---

## Multi-State Compliance Matrix

| Requirement | Colorado | Texas | Utah | Illinois (Video) | Illinois (HB 3773) | California (AB 2013) | NYC (LL 144) |
|------------|:--------:|:-----:|:----:|:--------:|:--------:|:--------:|:--------:|
| Risk management program | Required | Required | N/A | N/A | N/A | N/A | N/A |
| Impact assessment | Required | Required | N/A | N/A | N/A | N/A | Required (bias audit) |
| Consumer/employee notification | Required | Required | Required | Required (video) | Required | N/A | Required |
| Algorithmic discrimination review | Required | Recommended | N/A | N/A | Required (disparate impact testing) | N/A | Required (annual audit) |
| Transparency disclosures | Required | Required | N/A | N/A | N/A | Required | Required |
| Record keeping | Required | Required | N/A | Required (video) | Required | N/A | Required (audit results) |
| Effective date | June 30, 2026 | Sept 1, 2025 | May 1, 2024 | Jan 1, 2020 | Jan 1, 2026 | Jan 1, 2026 | July 5, 2023 |

!!! note "Vetoed and Pending Proposals"
    Several state AI bills have been vetoed or remain pending — notably **California SB 1047**, vetoed in September 2024. These do not impose current obligations but may inform future legislation. Monitor developments through your firm's regulatory monitoring program (Control 4.12).

---

## Recommended Actions for Multi-State FSI Organizations

1. **Jurisdiction mapping** — Identify all states where the organization operates, has customers, or has employees, and map applicable AI legislation
2. **Use-case inventory** — Catalog all Copilot use cases that involve consequential decisions (lending, insurance underwriting, employment, client recommendations) and assess state-by-state applicability
3. **Impact assessment program** — Implement a unified AI impact assessment process that satisfies the most stringent state requirements (currently Colorado)
4. **Disclosure framework** — Create a standard disclosure template for AI-assisted interactions that meets all applicable state notification requirements
5. **Documentation** — Maintain state-specific compliance evidence in the regulatory examination file per [Control 3.12 — Evidence Collection](../../controls/pillar-3-compliance/3.12-evidence-collection.md)
6. **Legal monitoring** — Establish a process to monitor state AI legislation developments, as additional states are expected to enact AI-specific laws in 2026–2027

---

## Related Controls

- [3.8 Model Risk Management](../../controls/pillar-3-compliance/3.8-model-risk-management.md) — SR 26-2 / OCC Bulletin 2026-13 (April 2026; excludes generative AI), continuing to apply SR 11-7 / OCC Bulletin 2011-12 principles to Copilot. See also [SR 26-2 / OCC 2026-13 Readiness](sr-26-2-occ-2026-13-readiness.md).
- [3.9 AI Disclosure and Transparency](../../controls/pillar-3-compliance/3.9-ai-disclosure-transparency.md) — Federal disclosure requirements
- [3.12 Evidence Collection](../../controls/pillar-3-compliance/3.12-evidence-collection.md) — Examination readiness documentation
- [3.10 SEC Reg S-P Privacy](../../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md) — Federal privacy framework
- [Colorado AI Act Readiness](colorado-ai-act-readiness.md) — Detailed Colorado guidance
- [SR 26-2 / OCC 2026-13 Readiness](sr-26-2-occ-2026-13-readiness.md) — Model-risk transition guidance

---

*FSI Copilot Governance Framework v1.8.0 - July 2026*
