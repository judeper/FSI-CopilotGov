# Pillar 2: Security & Protection

**Pillar Focus:** Protecting sensitive financial data and enforcing security boundaries across all Microsoft 365 Copilot surfaces.

**Controls:** 15
**Primary Admin Portals:** Microsoft Purview, Microsoft Entra, Microsoft Defender

---

## Overview

Pillar 2 addresses the security and data protection controls required to operate Microsoft 365 Copilot in regulated US financial services environments. These controls span data loss prevention, access governance, encryption, network security, and threat detection — all calibrated to the unique requirements of broker-dealers, registered investment advisers, banks, and insurance carriers.

Microsoft 365 Copilot introduces a new interaction surface that can access, summarize, and generate content across the entire Microsoft 365 tenant. Without appropriate security controls, Copilot can surface sensitive data to users who have technical permissions but should not have practical access (the "oversharing amplification" problem). Pillar 2 controls help prevent unauthorized data exposure, support compliance with GLBA safeguard requirements, and reduce the risk of regulatory findings during examinations.

Each control provides three governance levels — **Baseline**, **Recommended**, and **Regulated** — so organizations can implement protections proportional to their risk profile, examination frequency, and data sensitivity.

---

## Control Summary

| Control | Title | Key Regulatory Refs | Priority |
|---------|-------|---------------------|----------|
| [2.1](2.1-dlp-policies-for-copilot.md) | DLP Policies for M365 Copilot Interactions | FINRA 4511, SEC Reg S-P, GLBA 501(b), SOX 404 | Critical |
| [2.2](2.2-sensitivity-labels-classification.md) | Sensitivity Labels and Copilot Content Classification | GLBA 501(b), SOX 404 | Critical |
| [2.3](2.3-conditional-access-policies.md) | Conditional Access Policies for Copilot Workloads | GLBA 501(b), NYDFS Part 500, FFIEC | Critical |
| [2.4](2.4-information-barriers.md) | Information Barriers for Copilot (Chinese Wall) | SEC Rule 10b-5, FINRA 5280 | Critical |
| [2.5](2.5-data-minimization-grounding-scope.md) | Data Minimization and Grounding Scope | GLBA 501(b) | High |
| [2.6](2.6-web-search-controls.md) | Copilot Web Search and Web Grounding Controls | GLBA 501(b) | High |
| [2.7](2.7-data-residency.md) | Data Residency and Cross-Border Data Flow Governance | GLBA 501(b), GDPR, State Privacy Laws | High |
| [2.8](2.8-encryption.md) | Encryption (Data in Transit and at Rest) | GLBA 501(b), FFIEC, NYDFS Part 500 | Critical |
| [2.9](2.9-defender-cloud-apps.md) | Defender for Cloud Apps — Copilot Session Controls | GLBA 501(b), FFIEC | High |
| [2.10](2.10-insider-risk-detection.md) | Insider Risk Detection for Copilot Usage Patterns | GLBA 501(b), SOX 404, FINRA 3110 | High |
| [2.11](2.11-copilot-pages-security.md) | Copilot Pages Security and Sharing Controls | GLBA 501(b), FINRA 4511 | High |
| [2.12](2.12-external-sharing-governance.md) | External Sharing and Guest Access Governance | GLBA 501(b), SEC Reg S-P | High |
| [2.13](2.13-plugin-connector-security.md) | Plugin and Graph Connector Security Governance | GLBA 501(b), FFIEC | Medium |
| [2.14](2.14-declarative-agents-governance.md) | Declarative Agents from SharePoint — Creation and Sharing Governance | GLBA 501(b) | Medium |
| [2.15](2.15-network-security.md) | Network Security and Private Connectivity | NYDFS Part 500, FFIEC | Medium |

---

## Regulatory Mapping

The following regulations are addressed by Pillar 2 controls:

| Regulation | Section | Controls |
|------------|---------|----------|
| **GLBA** | 501(b) — Safeguards Rule | 2.1, 2.2, 2.3, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10, 2.11, 2.12, 2.13, 2.14 |
| **FINRA** | Rule 4511 — Books and Records | 2.1, 2.11 |
| **FINRA** | Rule 5280 — Trading Ahead of Research | 2.4 |
| **FINRA** | Rule 3110 — Supervision | 2.10 |
| **SEC** | Reg S-P — Privacy | 2.1, 2.12 |
| **SEC** | Rule 10b-5 — Fraud/Manipulation | 2.4 |
| **SOX** | Section 404 — Internal Controls | 2.1, 2.2, 2.10 |
| **NYDFS** | Part 500 — Cybersecurity | 2.3, 2.8, 2.15 |
| **FFIEC** | IT Examination Handbook | 2.3, 2.8, 2.9, 2.13, 2.15 |

---

## Implementation Approach

### Recommended Sequencing

1. **Foundation** (Controls 2.1-2.4): Deploy DLP, sensitivity labels, conditional access, and information barriers before enabling Copilot for any user group.
2. **Data Boundary** (Controls 2.5-2.8): Configure grounding scope, web search, data residency, and encryption to establish the data perimeter.
3. **Detection & Response** (Controls 2.9-2.10): Enable Defender for Cloud Apps session controls and insider risk detection for Copilot-specific monitoring.
4. **Collaboration Surfaces** (Controls 2.11-2.12): Secure Copilot Pages and external sharing before broad rollout.
5. **Extensibility** (Controls 2.13-2.15): Govern plugins, declarative agents, and network connectivity as the deployment matures.

### Dependencies

- Pillar 1 (Readiness & Assessment) should be substantially complete before implementing Pillar 2 controls.
- Controls 2.1 and 2.2 are foundational — most other Pillar 2 controls depend on sensitivity labels and DLP being in place.
- Control 2.4 (Information Barriers) is critical for any firm subject to Chinese Wall requirements and should be validated before Copilot pilot begins.

---

## Related Resources

- [Pillar 1: Readiness & Assessment](../pillar-1-readiness/index.md)
- [Pillar 3: Compliance & Audit](../pillar-3-compliance/index.md)
- [Pillar 4: Operations & Monitoring](../pillar-4-operations/index.md)
- [Microsoft 365 Copilot Security Documentation](https://learn.microsoft.com/microsoft-365-copilot/microsoft-365-copilot-privacy)
- [Microsoft Purview Data Security for AI](https://learn.microsoft.com/purview/ai-microsoft-purview)
