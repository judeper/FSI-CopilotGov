# Phase 4: Pillar Updates — Compliance and Operations - Context

**Gathered:** 2026-02-17
**Status:** Ready for planning

<domain>
## Phase Boundary

Update 19 controls across Pillars 3 and 4 (controls 3.1–3.11 and 4.1–4.8) to reflect current regulatory developments, expanded audit schemas, unified eDiscovery, agentic AI supervision requirements, and new billing models. Framework scope remains Microsoft 365 Copilot and Microsoft 365 Copilot Chat — other Copilot surfaces (Studio, Security, Fabric) are out of scope.

</domain>

<decisions>
## Implementation Decisions

### Regulatory Citation Style
- Section number + brief context (one sentence) for all regulatory citations — e.g., "SEC Rule 17a-4(f) requires broker-dealers to preserve electronic communications in non-rewritable format"
- SEC v. Delphia/Global Predictions enforcement action: use a dedicated "Enforcement Precedent" callout box pattern with 2-3 sentences on what happened and what it means for AI governance claims
- When multiple related regulations appear in one control (e.g., 17a-4 + off-channel fines + mobile recordkeeping), use unified narrative threading them together rather than separate sub-sections
- Forward-looking guidance (FINRA 2026 Report, SEC 2026 exam priorities): use anticipatory framing — "institutions should prepare now" tone, not treating as enacted rules but signaling forthcoming expectations

### Framework Scope for Expanded Purview Tools
- When a Purview compliance tool (Communication Compliance, etc.) expands coverage to surfaces outside our scope (Copilot Studio, Security Copilot, Fabric Copilot): briefly note the expansion exists, then keep all guidance focused on M365 Copilot and Copilot Chat
- Pattern: "Communication Compliance now covers [expanded list]; for M365 Copilot deployments, configure as follows..."

### Agentic AI Framing
- Adopt Microsoft's new "Copilot Control System" branding where they use it, referencing old name once for continuity — same pattern as Phase 2 terminology corrections
- For FINRA 2026 agentic supervision: frame around M365 Copilot agents (Teams channel agents, declarative agents), not custom Copilot Studio agents. Claude decides specific framing based on what the FINRA guidance says and how it maps to M365 Copilot capabilities
- New subsection threshold: same as Phase 3 (3-paragraph threshold for new subsections; otherwise integrate into existing sections)

### Teams Default Change (SC-4)
- Compliance-critical callout box: dedicated warning for the EnabledWithTranscript → Enabled change (March 2026). Position as must-act item for regulated firms — "ACTION REQUIRED" level framing
- Include specific Teams PowerShell cmdlet to enforce transcript retention directly in the control document (not deferred to playbook)
- Date-specific framing: "Effective March 2026, Microsoft changed the default..." — anchored to specific date, provides clear timeline context
- Claude decides which recordkeeping regulations to cite in the callout based on control context and regulatory mapping

### Plan Grouping and Structure
- Playbook updates bundled with control updates (same plan) when a control update changes portal paths or procedures — keeps control + playbook in sync
- Verification gate: same rigor as Phase 3. Grep-based checks for SC-1, SC-2, SC-4. For SC-3 (citation specificity), sampling approach — spot-check 3-4 controls for section numbers

### Claude's Discretion
- Plan grouping: Claude groups requirements based on file dependencies and natural clustering
- Wave structure: Claude picks based on inter-plan dependencies
- Agent supervision framing: Claude decides how to map FINRA 2026 guidance to M365 Copilot agent capabilities
- Regulatory citations for Teams callout: Claude selects most relevant from SEC 17a-4, FINRA 3110, FINRA 4511, and off-channel enforcement context

</decisions>

<specifics>
## Specific Ideas

- Enforcement Precedent box for SEC v. Delphia — distinct visual pattern to differentiate case law from statutory regulations
- Anticipatory framing for forward-looking guidance creates a clear tonal distinction from enacted rules
- Teams transcript change callout should include PowerShell remediation inline, not just policy description
- Scope guardrail: other Copilot surfaces (Studio, Security, Fabric) are mentioned as awareness only, never implementation guidance

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 04-pillar-compliance-operations*
*Context gathered: 2026-02-17*
