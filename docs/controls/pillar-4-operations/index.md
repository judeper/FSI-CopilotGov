# Pillar 4: Operations & Monitoring

**Pillar Focus:** Operational governance, ongoing monitoring, and lifecycle management of Microsoft 365 Copilot in financial services environments.

**Controls:** 13
**Primary Admin Portals:** M365 Admin Center, Microsoft Sentinel, Microsoft Viva Insights, Teams Admin Center

---

## Overview

Pillar 4 addresses the operational governance and ongoing monitoring controls required to sustain responsible Microsoft 365 Copilot usage in regulated US financial services environments. While Pillars 1-3 focus on readiness, security, and compliance foundations, Pillar 4 addresses what happens after deployment: how the institution manages Copilot settings, monitors usage, handles incidents, governs costs, and adapts to continuous feature changes.

Financial regulators expect that institutions do not merely deploy technology controls -- they demonstrate ongoing operational effectiveness. Sarbanes-Oxley §§302/404 requires evidence of control monitoring, the FFIEC expects continuous risk management, and FINRA Rule 3110 requires supervisory systems that adapt to the firm's evolving business model. Pillar 4 controls provide the operational backbone that transforms static policies into living governance.

These controls span five operational domains: administrative management (Controls 4.1-4.4), analytics and measurement (Controls 4.5-4.8), incident and resilience management (Controls 4.9-4.10), security monitoring (Control 4.11), and lifecycle governance (Controls 4.12-4.13).

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](../../disclaimer.md).

---

## Why Operations & Monitoring Matters for FSI

Deploying Microsoft 365 Copilot is not a one-time event -- it is the beginning of an ongoing governance obligation. Copilot surfaces evolve continuously as Microsoft releases new features, updates AI models, and expands capabilities. Without operational governance, the institution's security and compliance posture may degrade over time as new features bypass existing controls, usage patterns shift, and organizational changes affect access boundaries.

Key regulatory drivers for operational governance:

- **Sarbanes-Oxley §§302/404:** Requires ongoing monitoring and testing of internal controls, not just initial implementation. Copilot governance controls must be demonstrably effective throughout the reporting period.
- **FFIEC IT Examination Handbook:** Expects institutions to maintain change management, incident response, business continuity, and vendor management programs that cover all deployed technology, including AI services.
- **FINRA Rule 3110 (supervisory systems and WSPs):** Requires supervisory systems that are periodically reviewed and updated. As Copilot usage expands, supervisory coverage must scale accordingly.
- **GLBA §501(b):** Requires administrative, technical, and physical safeguards -- which must be maintained and monitored, not just established.
- **OCC Heightened Standards:** Expects large banks to maintain effective and current risk management frameworks, including for AI technology risks.

---

## Control Summary

| Control | Title | Key Regulatory Refs | Priority |
|---------|-------|---------------------|----------|
| [4.1](4.1-admin-settings-feature-management.md) | Copilot Admin Settings and Feature Management | Sarbanes-Oxley §§302/404, FFIEC | Critical |
| [4.2](4.2-teams-meetings-governance.md) | Copilot in Teams Meetings Governance | FINRA 3110, FINRA 4511, SEC 17a-4 | Critical |
| [4.3](4.3-teams-phone-queues.md) | Copilot in Teams Phone and Queues Governance | FINRA 3110, FINRA 4511 | High |
| [4.4](4.4-viva-suite-governance.md) | Copilot in Viva Suite Governance | GLBA §501(b), Labor Regulations | Medium |
| [4.5](4.5-usage-analytics.md) | Copilot Usage Analytics and Adoption Reporting | Sarbanes-Oxley §§302/404, FFIEC | High |
| [4.6](4.6-viva-insights-measurement.md) | Microsoft Viva Insights and Copilot Analytics Impact Measurement | Internal Governance | Medium |
| [4.7](4.7-feedback-telemetry.md) | Copilot Feedback and Telemetry Data Governance | GLBA §501(b), Privacy Regulations | Medium |
| [4.8](4.8-cost-allocation.md) | Cost Allocation and License Optimization | Sarbanes-Oxley §§302/404, FFIEC | Medium |
| [4.9](4.9-incident-reporting.md) | Incident Reporting and Root Cause Analysis | FINRA 4530, GLBA §501(b), NYDFS 500.17 | Critical |
| [4.10](4.10-business-continuity.md) | Business Continuity and Disaster Recovery for Copilot Dependency | FFIEC BC/DR, OCC, FINRA 4370 | High |
| [4.11](4.11-sentinel-integration.md) | Microsoft Sentinel Integration for Copilot Events | FFIEC, Sarbanes-Oxley §§302/404, NYDFS 500 | High |
| [4.12](4.12-change-management-rollouts.md) | Change Management for Copilot Feature Rollouts | Sarbanes-Oxley §§302/404, FFIEC | High |
| [4.13](4.13-extensibility-governance.md) | Copilot Extensibility and Agent Operations Governance | GLBA §501(b), FFIEC, OCC | High |

---

## Regulatory Mapping

The following regulations are addressed by Pillar 4 controls:

| Regulation | Section | Controls |
|------------|---------|----------|
| **SOX** | Section 404 -- Internal Controls | 4.1, 4.5, 4.6, 4.8, 4.11, 4.12, 4.13 |
| **FFIEC** | IT Examination Handbook | 4.1, 4.5, 4.8, 4.10, 4.11, 4.12, 4.13 |
| **FINRA** | Rule 3110 -- Supervision | 4.2, 4.3 |
| **FINRA** | Rule 4511 -- Books and Records | 4.2, 4.3 |
| **FINRA** | Rule 4370 -- Business Continuity Plans | 4.10 |
| **FINRA** | Rule 4530 -- Reporting Requirements | 4.9 |
| **SEC** | Rule 17a-4 -- Retention | 4.2 |
| **GLBA** | 501(b) -- Safeguards Rule | 4.3, 4.4, 4.7, 4.9, 4.11, 4.13 |
| **NYDFS** | Part 500 -- Cybersecurity | 4.9, 4.11 |
| **OCC** | Heightened Standards / 12 CFR 30 | 4.9, 4.10, 4.13 |

---

## Implementation Approach

### Recommended Sequencing

```
Phase 1: Administrative Foundation (Week 1-2)
├── Control 4.1  Copilot Admin Settings and Feature Management
├── Control 4.12 Change Management for Feature Rollouts
└── Control 4.5  Usage Analytics and Adoption Reporting

Phase 2: Communication Governance (Week 3-4)
├── Control 4.2  Teams Meetings Governance
├── Control 4.3  Teams Phone and Queues Governance
└── Control 4.7  Feedback and Telemetry Data Governance

Phase 3: Security Monitoring (Week 5-6)
├── Control 4.11 Microsoft Sentinel Integration
├── Control 4.9  Incident Reporting and Root Cause Analysis
└── Control 4.10 Business Continuity and Disaster Recovery

Phase 4: Optimization and Lifecycle (Week 7-8)
├── Control 4.4  Viva Suite Governance
├── Control 4.6  Viva Insights Impact Measurement
├── Control 4.8  Cost Allocation and License Optimization
└── Control 4.13 Extensibility Governance
```

### Dependencies

- Pillar 1 (Readiness & Assessment), Pillar 2 (Security & Protection), and Pillar 3 (Compliance & Audit) should be substantially complete before implementing Pillar 4 controls.
- Control 4.1 (Admin Settings) is foundational -- most other Pillar 4 controls depend on having a documented configuration baseline.
- Control 4.11 (Sentinel) depends on Pillar 2 security controls (DLP, information barriers, sensitivity labels) being in place to generate meaningful security events.
- Control 4.12 (Change Management) should be established before broad Copilot deployment to capture feature changes from the start.
- Control 4.13 (Extensibility Governance) builds on Control 1.13 (Extensibility Readiness) and Control 2.13 (Plugin Security).

### Cross-Pillar Dependencies

| This Control | Depends On | Relationship |
|-------------|-----------|--------------|
| 4.2 Teams Meetings | 2.x DLP, 3.x Communication Compliance | Meeting content requires DLP and supervisory controls |
| 4.5 Usage Analytics | 1.9 License Planning | Analytics require license assignment data |
| 4.9 Incident Reporting | 2.x Security Controls | Incidents detected by Pillar 2 security mechanisms |
| 4.11 Sentinel | 2.x DLP, IB, Labels | Sentinel monitors events generated by Pillar 2 controls |
| 4.12 Change Management | 4.1 Admin Settings | Changes assessed against admin settings baseline |
| 4.13 Extensibility | 1.13 Readiness, 2.13 Security | Lifecycle governance builds on readiness and security assessment |

---

## Related Resources

- [Pillar 1: Readiness & Assessment](../pillar-1-readiness/index.md)
- [Pillar 2: Security & Protection](../pillar-2-security/index.md)
- [Pillar 3: Compliance & Audit](../pillar-3-compliance/index.md)
- [Microsoft 365 Admin Center](https://admin.microsoft.com)
- [Microsoft Sentinel Documentation](https://learn.microsoft.com/azure/sentinel/overview)
- [Microsoft Viva Insights](https://learn.microsoft.com/viva/insights/)
- [Framework Executive Summary](../../framework/index.md)

---

*FSI Copilot Governance Framework v1.3 - April 2026*
