# Pillar 3: Compliance & Audit

**Post-deployment compliance, regulatory record-keeping, and audit readiness controls for Microsoft 365 Copilot in financial services environments.**

---

## Overview

Pillar 3 establishes the compliance monitoring, regulatory record-keeping, and audit readiness posture required for operating Microsoft 365 Copilot in a regulated financial services environment. These 13 controls address the critical ongoing compliance activities that help reduce risk from inadequate audit trails, insufficient supervision, missing retention policies, and regulatory examination gaps.

Financial regulators expect that institutions maintain comprehensive records of AI-assisted activities, supervise the use of AI tools in client-facing communications, and demonstrate examination readiness. The controls in this pillar provide a structured approach to audit logging, data retention, eDiscovery, communication compliance, FINRA supervision, regulatory reporting, and evidence collection for Microsoft 365 Copilot.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](../../disclaimer.md).

---

## Why Compliance & Audit Matters for FSI

Microsoft 365 Copilot generates, assists with, and surfaces content across every major M365 workload. Every Copilot interaction that touches client data, financial records, or regulated communications creates a potential record-keeping and supervisory obligation. Compliance controls help organizations meet these obligations systematically rather than reactively.

Key regulatory drivers for compliance and audit:

- **FINRA 4511:** Requires member firms to make and preserve books and records as required under FINRA rules, the SEA, and the applicable SEA rules -- this extends to Copilot-assisted communications and generated content.
- **SEC 17a-3 / 17a-4:** Books-and-records rules that specify what records must be created, how long they must be retained, and the format requirements for electronic storage -- directly applicable to Copilot interaction logs and generated documents.
- **SOX 302/404:** Internal control requirements for financial reporting that extend to AI-assisted document generation and financial analysis workflows.
- **FINRA 3110/3120:** Supervisory obligations requiring written supervisory procedures, qualified supervision, and annual testing for all forms of communication -- including Copilot-assisted communications.
- **FINRA 2210:** Communications with the public rules that apply when Copilot drafts or assists with customer-facing materials.
- **OCC 2011-12 / SR 11-7:** Model risk management guidance applicable to Copilot as a vendor-provided AI model used in financial decision-making contexts.
- **GLBA / SEC Reg S-P:** Privacy of consumer financial information requirements that govern how Copilot accesses and processes nonpublic personal information.

---

## Controls Summary

| Control ID | Control Name | Description | Governance Level |
|------------|-------------|-------------|------------------|
| [3.1](3.1-copilot-audit-logging.md) | Copilot Interaction Audit Logging | Copilot-specific audit events in Purview Unified Audit Log, CopilotInteraction events, event schema, search queries, export, and retention of audit data | Baseline |
| [3.2](3.2-data-retention-policies.md) | Data Retention Policies for Copilot Interactions | Retention policies for Copilot chat history, Copilot Pages, Teams meeting transcripts, Exchange Copilot interactions, and preservation holds | Baseline |
| [3.3](3.3-ediscovery-copilot-content.md) | eDiscovery for Copilot-Generated Content | eDiscovery (Premium) searches for Copilot interactions, content search locations, legal holds, and export formats | Recommended |
| [3.4](3.4-communication-compliance.md) | Communication Compliance Monitoring | Communication compliance policies targeting Copilot-assisted communications, detecting regulatory violations, and review workflows | Recommended |
| [3.5](3.5-finra-2210-compliance.md) | FINRA Rule 2210 Compliance for Copilot-Drafted Communications | Content standards for customer-facing communications, pre-review requirements, supervisory approval workflows | Regulated |
| [3.6](3.6-supervision-oversight.md) | Supervision and Oversight (FINRA 3110 / SEC Reg BI) | Written supervisory procedures for Copilot usage, qualified supervisor assignment, ongoing supervision, annual testing | Regulated |
| [3.7](3.7-regulatory-reporting.md) | Regulatory Reporting | Compliance reporting obligations, automated report generation, evidence collection, CFPB UDAAP considerations | Recommended |
| [3.8](3.8-model-risk-management.md) | Model Risk Management Alignment (OCC 2011-12 / SR 11-7) | MRM framework for M365 Copilot, model inventory, validation, ongoing monitoring, fair lending considerations | Regulated |
| [3.9](3.9-ai-disclosure-transparency.md) | AI Disclosure, Transparency, and SEC Marketing Rule | AI disclosure requirements, transparency about Copilot usage, SEC Marketing Rule compliance, anti-AI-washing controls | Regulated |
| [3.10](3.10-sec-reg-sp-privacy.md) | SEC Reg S-P -- Privacy of Consumer Financial Information | Copilot access to consumer financial information, privacy notices, opt-out provisions, NPI safeguards | Regulated |
| [3.11](3.11-record-keeping.md) | Record Keeping and Books-and-Records Compliance | Comprehensive record keeping for Copilot interactions, WORM storage, metadata preservation, chain of custody | Baseline |
| [3.12](3.12-evidence-collection.md) | Evidence Collection and Audit Attestation | Evidence pack assembly for regulatory examinations, attestation workflows, control effectiveness documentation | Recommended |
| [3.13](3.13-ffiec-alignment.md) | FFIEC IT Examination Handbook Alignment | Mapping to FFIEC IT Examination Handbook booklets and FFIEC CAT cybersecurity assessment alignment | Recommended |

---

## Implementation Sequence

The recommended implementation order for Pillar 3 controls:

```
Phase 1: Foundation (Week 1-2)
+-- Control 3.1  Copilot Interaction Audit Logging
+-- Control 3.2  Data Retention Policies
+-- Control 3.11 Record Keeping and Books-and-Records

Phase 2: Discovery & Monitoring (Week 3-4)
+-- Control 3.3  eDiscovery for Copilot Content
+-- Control 3.4  Communication Compliance Monitoring
+-- Control 3.12 Evidence Collection and Attestation

Phase 3: Regulatory Controls (Week 5-6)
+-- Control 3.5  FINRA 2210 Compliance
+-- Control 3.6  Supervision and Oversight
+-- Control 3.7  Regulatory Reporting

Phase 4: Advanced Compliance (Week 7-8)
+-- Control 3.8  Model Risk Management
+-- Control 3.9  AI Disclosure and Transparency
+-- Control 3.10 SEC Reg S-P Privacy
+-- Control 3.13 FFIEC Alignment
```

---

## Dependencies

Pillar 3 controls depend on foundational work from Pillar 1 (Readiness) and Pillar 2 (Security), and feed into Pillar 4 (Operations):

| This Control | Depends On | Relationship |
|-------------|-----------|--------------|
| 3.1 Audit Logging | 1.9 License Planning | Audit (Premium) requires E5 or add-on licensing |
| 3.2 Retention Policies | 1.5 Sensitivity Labels | Retention labels align with sensitivity label taxonomy |
| 3.3 eDiscovery | 3.1 Audit Logging, 3.2 Retention | eDiscovery searches require audit data and retained content |
| 3.4 Communication Compliance | 2.x DLP Policies | Communication compliance leverages DLP sensitive info types |
| 3.5 FINRA 2210 | 3.4 Communication Compliance | 2210 monitoring builds on communication compliance policies |
| 3.6 Supervision | 3.4, 3.5 | Supervisory review depends on communication monitoring |
| 3.8 Model Risk | 1.10 Vendor Risk | MRM framework extends vendor risk management |
| 3.10 SEC Reg S-P | 2.x DLP, 1.6 Permission Audit | NPI protection depends on DLP and permission controls |

| This Control | Feeds Into | Relationship |
|-------------|-----------|--------------|
| 3.1 Audit Logging | 4.x Sentinel Monitoring | Audit events feed SIEM for operational monitoring |
| 3.7 Regulatory Reporting | 4.x Dashboards | Report data feeds operational dashboards |
| 3.12 Evidence Collection | All Pillars | Evidence packs reference controls from every pillar |

---

## Related Resources

- [Framework Overview](../../framework/index.md)
- [Pillar 1: Readiness & Assessment](../pillar-1-readiness/index.md)
- [Pillar 2: Security & Protection](../pillar-2-security/index.md)
- [Pillar 4: Operations & Monitoring](../pillar-4-operations/index.md)
- [Regulatory Mappings Reference](../../reference/regulatory-mappings.md)

---

*FSI Copilot Governance Framework v1.2.1 - March 2026*
