# Executive Summary

A board-level overview of Microsoft 365 Copilot governance for US financial services organizations.

---

## The M365 Copilot Opportunity and Risk

Microsoft 365 Copilot embeds generative AI directly into the applications your workforce uses daily -- Word, Excel, Outlook, Teams, SharePoint, and more. For financial services institutions, this represents both a significant productivity opportunity and a governance challenge that requires structured oversight.

**Key Business Drivers:**

- Enhanced employee productivity across document creation, email composition, data analysis, and meeting management
- Faster information discovery across the Microsoft 365 tenant
- Improved customer communication drafting and review workflows
- Competitive positioning in AI-augmented financial services operations

**Key Risk Considerations:**

- Discovery amplification: Copilot surfaces content users already have access to, but at unprecedented speed and scale
- Copilot-drafted customer communications may require supervisory review under FINRA Rule 2210
- Web search grounding may introduce external data into regulated workflows
- Audit and retention requirements apply to Copilot interactions in regulated contexts
- Existing oversharing and permission sprawl are magnified, not introduced, by Copilot

---

## Top 10 M365 Copilot Risks for Financial Services

| Rank | Risk | Impact | Key Mitigating Controls |
|------|------|--------|------------------------|
| 1 | **Oversharing Amplification** | Copilot surfaces sensitive content users technically can access but should not routinely see, exposing PII, deal data, or compensation information at scale | 1.1, 1.2, 1.3 |
| 2 | **Copilot-Drafted Customer Communications** | AI-generated emails, letters, or proposals sent to clients without adequate supervisory review may violate FINRA Rule 2210 or create misleading statements | 3.5, 3.6 |
| 3 | **Inadequate Audit Trail** | Copilot interactions not captured, retained, or searchable for regulatory examination, undermining FINRA 4511 and SEC 17a-4 obligations | 3.1, 3.2, 3.3 |
| 4 | **Web Search Data Leakage** | Copilot web grounding sends tenant context to Bing, potentially exposing confidential terms or client names in search queries | 2.7, 4.2 |
| 5 | **Sensitivity Label Gaps** | Unlabeled or mislabeled content is treated as accessible by Copilot, resulting in confidential data surfacing in AI-generated responses | 2.2, 2.3 |
| 6 | **Meeting Transcription Exposure** | Teams meeting transcriptions indexed by Copilot expose spoken content (including off-the-record remarks) to anyone with meeting access | 1.5, 3.2, 4.6 |
| 7 | **Copilot Pages Data Sprawl** | Copilot Pages create new collaborative content outside traditional governance boundaries, potentially duplicating regulated data without retention controls | 3.2, 4.8 |
| 8 | **Hallucination in Regulated Contexts** | Copilot generates plausible but incorrect financial data, regulatory citations, or client information that enters official documents | 3.5, 3.7 |
| 9 | **Plugin and Connector Data Exposure** | Graph connectors and plugins extend Copilot's data reach beyond M365, potentially grounding responses in unvetted or unclassified external data | 2.8, 4.10 |
| 10 | **Insufficient Access Governance for Semantic Index** | The Semantic Index indexes all content accessible to the user; without regular access reviews, stale permissions create an expanding attack surface | 1.2, 1.4, 1.6 |

---

## Regulatory Landscape Summary

### Primary US Financial Regulations

| Regulation | Issuer | Copilot Relevance | Framework Coverage |
|------------|--------|-------------------|-------------------|
| **FINRA Rule 4511** | FINRA | Books and records for Copilot interactions and outputs | Controls 3.1, 3.2, 3.11 |
| **FINRA Rule 3110** | FINRA | Supervision of Copilot-assisted activities and outputs | Controls 3.6, 3.4 |
| **FINRA Rule 2210** | FINRA | Copilot-drafted customer communications review | Control 3.5 |
| **SEC Rule 17a-3/4** | SEC | Recordkeeping for Copilot-generated content | Controls 3.11, 3.3 |
| **SEC Reg S-P** | SEC | Privacy of consumer financial information accessed by Copilot | Control 3.10 |
| **SEC Reg BI** | SEC | Supervision and best interest when Copilot assists recommendations | Control 3.6 |
| **SOX 302/404** | Congress | Internal controls over financial data accessed by Copilot | Controls 3.1, 1.3 |
| **GLBA 501(b)** | FTC | Safeguards for customer information surfaced by Copilot | Controls 2.1, 2.2 |
| **OCC 2011-12 / SR 11-7** | OCC/Fed | Model risk management considerations for AI-assisted decisions | Control 3.8 |
| **CFPB UDAAP** | CFPB | Unfair/deceptive practices in Copilot-assisted customer interactions | Control 3.7 |
| **FFIEC IT Handbook** | FFIEC | IT examination alignment for AI tools | Control 3.13 |
| **Interagency AI Guidance (2023)** | OCC/Fed/FDIC | Vendor risk management for AI services | Control 1.10 |

### Regulatory Heatmap by Governance Level

| Regulation | Baseline | Recommended | Regulated |
|------------|----------|-------------|-----------|
| FINRA 4511 | Basic audit logging | Extended retention | Full 6-year retention with eDiscovery |
| FINRA 3110 | Awareness training | Supervisory sampling | Comprehensive supervision program |
| FINRA 2210 | User guidance | Pre-send review workflows | Automated communication compliance |
| SEC 17a-3/4 | Basic retention | Searchable archives | WORM-compliant, examination-ready |
| SEC Reg S-P | Default permissions | Oversharing remediation | Full access governance program |
| SEC Reg BI | N/A | Supervisory controls | Best interest documentation |
| SOX 302/404 | Basic access controls | Segregation of duties | Full ICFR integration |
| GLBA 501(b) | DLP baseline | Sensitivity labels | Comprehensive safeguards |
| OCC 2011-12 / SR 11-7 | N/A | Awareness documentation | Formal MRM alignment |

**Note:** "Baseline" represents minimum viable governance. Organizations subject to specific regulations should target "Recommended" or "Regulated" levels for those requirements. Consult legal counsel for your specific obligations.

---

## Governance Model Summary

### Four Pillars

```
+-------------------+-------------------+-------------------+-------------------+
|     PILLAR 1      |     PILLAR 2      |     PILLAR 3      |     PILLAR 4      |
|    Readiness &    |    Security &     |   Compliance &    |   Operations &    |
|    Assessment     |    Protection     |      Audit        |    Monitoring     |
|   (15 controls)   |   (15 controls)   |   (13 controls)   |   (13 controls)   |
+-------------------+-------------------+-------------------+-------------------+
| Data hygiene,     | DLP, labels,      | Audit logging,    | Feature toggles,  |
| oversharing,      | conditional       | retention,        | analytics, cost,  |
| permissions,      | access, barriers, | eDiscovery,       | incident response, |
| licensing         | Defender          | FINRA, SEC        | BC/DR, Sentinel   |
+-------------------+-------------------+-------------------+-------------------+
```

**56 Total Controls** across four lifecycle pillars addressing readiness, security, compliance, and operations for M365 Copilot governance.

### Three Governance Levels

| Level | Risk Posture | Typical Use | Control Coverage |
|-------|--------------|-------------|------------------|
| **Baseline** | Minimum viable governance | Initial Copilot deployment, low-risk environments | ~30 controls |
| **Recommended** | Best-practice governance | Most production environments | ~45 controls |
| **Regulated** | Examination-ready governance | FINRA/SEC-regulated, high-risk environments | All 56 controls |

---

## High-Level RACI

| Activity | AI Gov Lead | Compliance | CISO | Legal | Board |
|----------|-------------|------------|------|-------|-------|
| Framework ownership | **A** | C | C | I | I |
| Copilot deployment approval | R | **A** | C | C | I |
| Security policy configuration | C | C | **A** | I | I |
| Regulatory alignment validation | C | **A** | C | C | I |
| Incident escalation (material) | R | R | R | C | **A** |
| Annual governance review | R | **A** | C | C | A |
| Oversharing remediation | R | C | **A** | I | I |
| Copilot feature toggle decisions | **A** | C | C | I | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

See [Operating Model](operating-model.md) for complete RACI matrices.

---

## Key Governance Metrics

### Board-Level KPIs

| Metric | Target | Measurement Frequency |
|--------|--------|----------------------|
| Oversharing sites remediated (of identified) | 100% before Copilot expansion | Monthly |
| Copilot interactions with audit logging | 100% | Monthly |
| Critical control implementation rate | 100% for applicable level | Quarterly |
| Regulatory examination findings (Copilot-related) | 0 critical | Annual |
| Mean time to remediation (critical Copilot issue) | < 7 days | Per incident |
| Communication compliance review rate | Per supervisory plan | Monthly |

### Operational Metrics

| Metric | Baseline Target | Regulated Target |
|--------|-----------------|------------------|
| Sensitivity label coverage (files) | 80% | 95%+ |
| Audit log completeness | 99% | 99.9% |
| DLP policy violation response SLA | 48 hours | 4 hours |
| Copilot license utilization | Tracked | Tracked with cost optimization |
| Access review completion rate | 90% | 100% |

---

## Investment Requirements

### Technology Investment

| Component | Purpose | Licensing |
|-----------|---------|-----------|
| Microsoft 365 E5 (or E3 + add-ons) | Core platform, compliance features (Purview, Defender) | Required |
| Microsoft 365 Copilot licenses | Per-user Copilot access | Required |
| Microsoft Purview | Data governance, audit, eDiscovery, communication compliance | Included in E5 |
| Microsoft Entra ID P2 | Conditional access, access reviews, identity governance | Included in E5 |
| Microsoft Sentinel | Advanced security monitoring, analytics | Optional (Regulated recommended) |
| SharePoint Advanced Management | Restricted SharePoint Search, access governance reports | Recommended |

### Organizational Investment

| Role | Responsibility | FTE Estimate |
|------|----------------|--------------|
| AI Governance Lead / Copilot Program Manager | Framework ownership, committee chair, feature management | 0.5-1.0 FTE |
| M365 / Purview Admin | Technical control implementation, audit configuration | 0.25-0.5 FTE |
| Compliance Analyst | Monitoring, communication review, reporting | 0.25-0.5 FTE |
| SharePoint Admin | Oversharing remediation, site access governance | 0.25-0.5 FTE |

**Note:** FTE estimates scale with tenant size, number of Copilot users, and regulatory complexity.

---

## Implementation Roadmap Summary

### Phase 0: Foundation (Days 0-30)

- Conduct oversharing assessment and remediate high-risk SharePoint sites
- Establish Copilot Governance Committee and charter
- Implement core controls: audit logging (3.1), DLP baseline (2.1), sensitivity labels (2.2)
- Configure Copilot feature toggles for pilot scope
- Complete baseline governance training

### Phase 1: Pilot (Days 30-60)

- Deploy Copilot to controlled pilot group (50-200 users)
- Enable communication compliance monitoring (3.4, 3.5)
- Implement supervisory review workflows (3.6)
- Configure retention policies for Copilot interactions (3.2)
- Conduct first governance review

### Phase 2: Expansion (Days 60-90)

- Broader Copilot deployment based on pilot learnings
- Implement advanced controls: information barriers (2.6), Defender for Cloud Apps (2.9)
- Enable eDiscovery for Copilot content (3.3)
- Validate examination readiness
- Achieve steady-state governance operations

See [Adoption Roadmap](adoption-roadmap.md) for detailed implementation guidance.

---

## Examination Readiness

### Key Artifacts for Examiners

| Artifact | Source | Retention |
|----------|--------|-----------|
| Copilot interaction audit logs | Purview Audit (Copilot activities) | Per retention matrix (3 years communications, 6 years financial records; supports SEC 17a-4, FINRA 4511) |
| Supervisory review records | Communication compliance | 6 years (supports FINRA 3110, SEC 17a-4) |
| Governance committee minutes | SharePoint Compliance Library | 7 years (SOX 802) |
| Copilot deployment approval records | Governance committee | 7 years (SOX 802) |
| DLP policy configuration and violations | Purview | 3 years minimum |
| Training records | HR/LMS system | 7 years (SOX 802) |
| Incident reports (Copilot-related) | Incident management system | 7 years (SOX 802) |

### Examination Response Process

1. Receive information request from examiner
2. Compliance Officer coordinates response with AI Governance Lead
3. AI Governance Lead provides technical artifacts (audit logs, configuration evidence)
4. Legal reviews before submission
5. Document all interactions and responses

---

## Questions for Board Discussion

1. **Risk Appetite:** What level of Copilot-related risk is acceptable? Should Copilot be available to all licensed users or restricted by role/department?
2. **Oversharing Posture:** Has the organization assessed and remediated oversharing before Copilot deployment? What is the timeline for completing this work?
3. **Supervisory Model:** How will the organization supervise Copilot-drafted customer communications under FINRA Rule 2210?
4. **Investment:** Are current technology and staffing investments adequate for Copilot governance?
5. **Metrics:** What Copilot governance metrics should be reported to the board quarterly?
6. **Web Search:** Should Copilot web search be enabled, restricted, or disabled for regulated users?
7. **Expansion Criteria:** What success criteria must be met before expanding Copilot beyond the pilot group?

---

## Next Steps for Executives

1. **Review** this summary and [Governance Fundamentals](governance-fundamentals.md)
2. **Approve** Copilot Governance Committee charter and membership
3. **Fund** oversharing assessment and remediation as a pre-deployment prerequisite
4. **Allocate** resources per [Adoption Roadmap](adoption-roadmap.md)
5. **Establish** board reporting cadence for Copilot governance metrics
6. **Schedule** annual governance review participation

---

## Disclaimer

This framework provides governance guidance and does not constitute legal, regulatory, or compliance advice. Organizations should validate all controls against their specific regulatory obligations and consult legal counsel for regulatory interpretation.

---

*FSI Copilot Governance Framework v1.1 - February 2026*
