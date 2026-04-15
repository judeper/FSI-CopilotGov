# Control 1.12: Training and Awareness Program — Troubleshooting

Common issues and resolution steps for the training and awareness program.

## Common Issues

### Issue 1: Low Training Completion Rates

- **Symptoms:** Training completion rates consistently below the 95% target, particularly in certain departments or roles
- **Root Cause:** Competing priorities, training perceived as irrelevant, insufficient time allocated for training, or lack of management enforcement.
- **Resolution:**
  1. Identify specific departments or roles with low completion and investigate root causes
  2. Shorten training modules where possible (target 20-30 minutes per module)
  3. Get management buy-in to enforce training completion deadlines
  4. Make training completion a gate for Copilot license activation
  5. Offer multiple delivery formats (self-paced, instructor-led, video, interactive)

### Issue 2: Training Content Quickly Becomes Outdated

- **Symptoms:** Users report that training screenshots, feature descriptions, or procedures do not match the current Copilot experience
- **Root Cause:** Microsoft updates Copilot frequently. Static training materials with specific UI screenshots become outdated within weeks.
- **Resolution:**
  1. Focus training on concepts and governance principles rather than specific UI paths
  2. Use Microsoft's official training resources for feature-specific content (kept current by Microsoft)
  3. Limit custom content to organization-specific policies and procedures
  4. Establish a monthly content review cycle for custom training materials
  5. Add version dates to all training content so users can identify currency

### Issue 3: Training Platform Integration Issues

- **Symptoms:** Training modules fail to load in Viva Learning, completion data does not sync with the LMS, or users cannot access assigned training
- **Root Cause:** Content source configuration issues, SCORM package compatibility problems, or synchronization delays between systems.
- **Resolution:**
  1. Verify content source configuration in Viva Learning admin settings
  2. Check SCORM package compatibility with the target LMS version
  3. For synchronization issues, review the sync schedule and force a manual sync
  4. Test the training module as a non-admin user to reproduce access issues
  5. Provide direct links to training content as a fallback for platform issues

### Issue 4: Users Completing Training Without Engagement

- **Symptoms:** High completion rates but low knowledge retention scores, or users report they "clicked through" training quickly
- **Root Cause:** Training modules may lack engagement mechanisms (quizzes, interactions) or may be too long, encouraging users to rush through.
- **Resolution:**
  1. Add knowledge check questions throughout the training (not just at the end)
  2. Require a minimum passing score on the assessment to mark training as complete
  3. Include scenario-based exercises relevant to the user's role
  4. Break long modules into shorter segments with mandatory engagement points
  5. Consider gamification elements or team-based learning challenges

### Issue 5: Difficulty Tracking Compliance Across Multiple Training Systems

- **Symptoms:** Different training modules are delivered through different platforms (LMS, Viva Learning, in-person), making consolidated compliance reporting difficult
- **Root Cause:** Fragmented training delivery architecture without a single source of truth for completion data.
- **Resolution:**
  1. Designate a single LMS as the authoritative training record
  2. Configure all training platforms to report completions back to the authoritative system
  3. Use PowerShell Script 1 as a reconciliation tool to cross-reference multiple data sources
  4. For in-person training, establish a manual completion recording process
  5. Consider consolidating all training delivery to a single platform

## Diagnostic Steps

1. **Check completion data:** Run Script 1 to assess current compliance state
2. **Review platform health:** Test training access as a standard user
3. **Survey learners:** Quick poll to identify access or content issues
4. **Verify tracking:** Cross-reference LMS data with manual attendance records
5. **Assess content:** Review training materials for accuracy and currency

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Individual user training access issues | IT Help Desk |
| **Medium** | Department-wide low completion rates | Department leadership and training team |
| **High** | Training platform outage affecting compliance tracking | IT Operations and LMS vendor |
| **Critical** | Training completion gate bypassed — unlicensed users accessing Copilot | CISO and License Administrator |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Training setup procedures
- [PowerShell Setup](powershell-setup.md) — Tracking automation
- [Verification & Testing](verification-testing.md) — Program validation
- Back to [Control 1.12](../../../controls/pillar-1-readiness/1.12-training-awareness.md)
