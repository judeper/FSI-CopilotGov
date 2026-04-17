# Teams Copilot Mode Governance — FINRA 3110 Supervision

Governance procedures for Microsoft Teams Copilot Mode (group chat with Copilot), addressing FINRA Rule 3110 supervision and FINRA Rule 4511 recordkeeping obligations.

!!! warning "Disclaimer"
    This playbook is provided for informational purposes only and does not constitute legal or regulatory advice. Consult legal counsel for specific compliance requirements.

---

## What Is Teams Copilot Mode?

Teams Copilot Mode transforms the Copilot 1:1 chat experience into a group collaboration experience where multiple users interact with Copilot together in a shared Teams conversation. This feature was announced at Microsoft Ignite 2025 and is in public preview.

**Key governance differences from standard Copilot Chat:**

| Characteristic | Standard Copilot Chat | Teams Copilot Mode |
|---------------|----------------------|-------------------|
| **Participants** | Single user + Copilot | Multiple users + Copilot |
| **Visibility** | User sees only their interactions | All participants see all interactions and responses |
| **Data grounding** | Based on individual user's Microsoft Graph access | May surface data accessible to any participant |
| **Record type** | Individual Copilot interaction | Group communication — potentially subject to FINRA 3110 |
| **Retention** | Microsoft Copilot experiences retention policy | Teams chat retention policy + Copilot experiences policy |

---

## FINRA 3110 Supervision Implications

### Why Teams Copilot Mode Requires Supervisory Attention

FINRA Rule 3110(b)(4) requires firms to establish written supervisory procedures for each type of business activity in which the firm engages. Teams Copilot Mode creates a new type of business communication where:

1. **Multiple registered representatives** may discuss client matters, investment recommendations, or market views with Copilot generating AI-assisted responses visible to all participants
2. **Copilot responses** in group context may incorporate data from multiple participants' Microsoft Graph access, potentially surfacing information that not all participants should see
3. **Group AI interactions** may constitute correspondence or retail communications under FINRA Rule 2210 depending on how the output is used

### Supervisory Procedures Checklist

| # | Procedure | FINRA Reference | Priority |
|---|-----------|-----------------|----------|
| 1 | Update written supervisory procedures (WSPs) to address Copilot Mode group interactions | FINRA Rule 3110(b)(4) | Required |
| 2 | Determine whether Copilot Mode interactions are captured by existing Communication Compliance policies | FINRA Rule 3110(b)(1) | Required |
| 3 | Verify retention policy coverage for Copilot Mode group chat content | FINRA Rule 4511(a) | Required |
| 4 | Assess whether Copilot Mode group responses are discoverable via Purview eDiscovery | FINRA Rule 8210 | Required |
| 5 | Evaluate whether Copilot Mode should be restricted for registered representatives via Teams policy | FINRA Rule 3110(a) | Recommended |
| 6 | Include Copilot Mode in annual FINRA 3120 supervisory testing program | FINRA Rule 3120 | Recommended |
| 7 | Train supervisors on Copilot Mode-specific review procedures | FINRA Rule 3110(a)(5) | Recommended |

---

## Configuration Recommendations

### Restricting Copilot Mode Access

For initial deployment, FSI organizations should consider restricting Copilot Mode to specific user groups:

1. **Evaluate per-user or per-group enablement** — Use Teams meeting/messaging policies to control Copilot Mode availability
2. **Exclude registered representatives initially** — Until supervisory procedures are updated and validated, consider excluding FINRA-registered individuals
3. **Pilot with non-client-facing groups** — Start with internal operations teams where communication compliance risk is lower

### Retention and Compliance Configuration

1. **Verify Teams chat retention** covers Copilot Mode conversations — these appear as Teams group chats
2. **Verify Communication Compliance policies** include Teams chat locations with Copilot Mode content in scope
3. **Test eDiscovery** to confirm Copilot Mode group chat content is searchable and exportable

---

## Verification Steps

| # | Step | Expected Result |
|---|------|-----------------|
| 1 | Search Purview audit log for Copilot Mode events | Copilot Mode group interactions appear as auditable events |
| 2 | Verify Copilot Mode content in eDiscovery | Group chat content with Copilot responses is discoverable |
| 3 | Confirm retention policy applies | Copilot Mode content is within scope of Teams chat retention policy |
| 4 | Test Communication Compliance coverage | Copilot Mode content triggers applicable compliance policies |
| 5 | Review WSP updates | Written supervisory procedures explicitly address Copilot Mode |

---

## Related Controls

- [3.4 Communication Compliance](../../controls/pillar-3-compliance/3.4-communication-compliance.md)
- [3.5 FINRA 2210 Compliance](../../controls/pillar-3-compliance/3.5-finra-2210-compliance.md)
- [3.6 Supervision and Oversight](../../controls/pillar-3-compliance/3.6-supervision-oversight.md)
- [4.2 Teams Meetings Governance](../../controls/pillar-4-operations/4.2-teams-meetings-governance.md)
- [3.2 Data Retention](../../controls/pillar-3-compliance/3.2-data-retention-policies.md)

---

*FSI Copilot Governance Framework v1.4 - April 2026*
