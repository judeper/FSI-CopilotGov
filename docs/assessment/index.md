# Governance Scorecard

The Governance Scorecard is an interactive self-assessment tool that helps financial-services organizations evaluate their implementation of the [FSI Copilot Governance Framework](../framework/index.md) across all 58 controls and four lifecycle pillars. It produces a personalized scorecard, gap analysis, and prioritized remediation roadmap.

!!! warning "Disclaimer"
    This tool supports governance readiness assessment. It does not constitute legal advice, is not a compliance certification, and should not be used as a substitute for professional compliance guidance. Organizations should verify these configurations meet their specific obligations under applicable regulations such as FINRA Rules 4511/3110/2210, SEC Rules 17a-3/17a-4, Reg S-P, Reg BI, SOX, GLBA, OCC guidelines, and FFIEC requirements.

**Scoring:** Yes (1.0) · Partial (0.5) · No (0.0) · N/A (excluded) — **RAG:** Green 80%+ · Amber 50–79% · Red <50% — All data stays in your browser.

<div id="assessment-app" class="assessment-container">
  <noscript>
    <div class="admonition warning">
      <p class="admonition-title">JavaScript Required</p>
      <p>The Governance Scorecard requires JavaScript to run.
      Please enable JavaScript in your browser to use this tool.</p>
    </div>
  </noscript>
  <div class="assessment-loading">
    <p>Loading assessment tool...</p>
  </div>
</div>

---

## About This Tool

### How It Works

1. **Scoping** — Select your target governance level (Baseline, Recommended, or Regulated) and organization profile
2. **Assess Controls** — Rate each control's implementation status (Yes / Partial / No / N/A); all controls must be answered before continuing to Results
3. **Drill-Down** — Refine gap-control scores with detailed verification checks and import completed delegated sections when applicable
4. **Results Dashboard** — View executive scorecard with per-level breakdowns, regulatory exposure, and remediation roadmap; if Drill-Down is incomplete, results remain preliminary
5. **Export** — Download the full assessment JSON for re-import or trend comparison, plus Excel, CSV, or print-to-PDF outputs for reporting

### Scoring Methodology

Each control is scored individually:

- **Yes** = 1.0 (fully implemented)
- **Partial** = 0.5 (refined by drill-down sub-questions)
- **No** = 0.0 (not implemented)
- **N/A** = excluded from scoring

Aggregate scores are calculated as: `score = sum(controlScores) / count(applicableControls) × 100`

**RAG thresholds:** Green (≥80%), Amber (50–79%), Red (below 50%)

#### Cumulative Target Level Model

The framework uses three cumulative governance levels — **Baseline ⊂ Recommended ⊂ Regulated** — meaning each level includes all requirements from the levels below it:

| Target Level | What Is Scored |
|---|---|
| **Baseline** | Baseline criteria only |
| **Recommended** | Baseline + Recommended criteria |
| **Regulated** | Baseline + Recommended + Regulated criteria |

When you select a target governance level, the scorecard evaluates all criteria at that level and every level below it. Scores are displayed per governance level up to your selected target, so you can see exactly where gaps exist at each tier. This helps organizations working toward a Regulated posture identify whether foundational Baseline requirements are met before addressing more advanced criteria.

#### Four Lifecycle Pillars

Scores are broken down across the four governance pillars:

1. **Pillar 1 — Readiness & Assessment** · Pre-deployment governance foundations
2. **Pillar 2 — Security & Protection** · Data protection, access control, and threat mitigation
3. **Pillar 3 — Compliance & Audit** · Regulatory alignment, retention, and audit readiness
4. **Pillar 4 — Operations & Monitoring** · Ongoing monitoring, incident response, and optimization

### Risk Priority

Gap controls are prioritized for remediation using:

`riskPriority = (1 - score) × regulatoryWeight × levelWeight`

- **Regulatory weight:** 3.0 (mapped to 4+ regulations), 2.0 (2–3 regulations), 1.0 (0–1 regulations)
- **Level weight:** Baseline gaps = 3.0 (most urgent), Recommended gaps = 2.0, Regulated gaps = 1.0

Baseline gaps are weighted highest because they represent foundational requirements. A Baseline gap in a control mapped to multiple regulations (e.g., FINRA Rule 4511(a), SEC Rule 17a-4) receives the highest remediation priority.

### Relevant Admin Roles

The scorecard identifies which administrator roles are responsible for each control area. Use canonical role names when assigning remediation tasks:

- **M365 Global Admin** — Tenant-wide configuration and service settings
- **Entra Global Admin** — Identity, access, and conditional-access policies
- **Purview Compliance Admin** — Retention, DLP, eDiscovery, and audit policies
- **SharePoint Admin** — Site-level permissions and sharing controls
- **Exchange Online Admin** — Mailbox policies and transport rules
- **Teams Admin** — Meeting, messaging, and app policies

### Collaboration

The governance lead can export role-specific sections as JSON files for relevant admins to complete independently during Drill-Down, then import completed sections back into the same assessment. If imported responses conflict with existing answers, the current assessment keeps the existing response so the governance lead can review the difference manually.

### Data Privacy

All assessment data stays in your browser. No data is sent to any server. Browser drafts are saved automatically on the current device as a convenience cache, while "Save to File" (JSON export) remains the primary artifact for sharing, re-import, and archival.
