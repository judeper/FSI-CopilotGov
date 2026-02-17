# Control 4.10: Business Continuity and Disaster Recovery — Troubleshooting

Common issues and resolution steps for Copilot business continuity and disaster recovery.

## Common Issues

### Issue 1: No Fallback Procedures When Copilot Is Unavailable

- **Symptoms:** Business operations halt or significantly degrade when Copilot experiences an outage because users have no alternative workflows.
- **Root Cause:** Over-reliance on Copilot without documented fallback procedures, or fallback procedures exist but users are not trained on them.
- **Resolution:**
  1. Document manual fallback procedures for each Copilot-dependent business process.
  2. Conduct training sessions so users know how to operate without Copilot.
  3. Keep traditional tools and templates accessible as backups.
  4. Conduct periodic "Copilot-free" exercises to maintain manual skills.

### Issue 2: Service Health Notifications Not Reaching the Right People

- **Symptoms:** IT operations team is unaware of a Copilot service degradation until users report problems.
- **Root Cause:** Service health notification settings are misconfigured or notification recipients are outdated.
- **Resolution:**
  1. Review service health notification settings in the M365 Admin Center.
  2. Update notification recipients to include current IT operations and compliance contacts.
  3. Add a distribution group rather than individual emails for resilience.
  4. Implement API-based monitoring as a backup to email notifications.

### Issue 3: BCP Plan Does Not Address Copilot Dependencies

- **Symptoms:** During a BCP/DR test, the Copilot dependency is not addressed, leaving a gap in the continuity plan.
- **Root Cause:** The BCP plan was created before Copilot deployment and has not been updated.
- **Resolution:**
  1. Update the BCP plan to include a Copilot-specific appendix.
  2. Map Copilot dependencies to business process impact assessments.
  3. Define RTO and RPO for Copilot services.
  4. Include Copilot outage scenarios in the next BCP test cycle.

### Issue 4: Extended Outage Exceeding Acceptable Business Impact

- **Symptoms:** A prolonged Copilot outage causes business impact beyond the defined RTO tolerance.
- **Root Cause:** Microsoft service recovery is beyond organizational control, and fallback procedures may not sustain operations for extended periods.
- **Resolution:**
  1. Activate the extended outage communication plan.
  2. Implement additional manual resources to maintain business operations.
  3. Monitor Microsoft service health for restoration timeline updates.
  4. Document the business impact for post-incident review and BCP plan improvements.
  5. Evaluate if alternative AI services should be part of the DR strategy.

## Diagnostic Steps

1. **Check service status:** Run the service health script or check the M365 Admin Center.
2. **Review notification delivery:** Verify the operations team received recent service health notifications.
3. **Test fallback procedures:** Ask a business unit to demonstrate their Copilot fallback process.
4. **Review BCP plan currency:** Confirm the BCP plan includes Copilot and was updated within the last 12 months.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Extended outage impacting client-facing operations | CIO/CTO + Business leadership + Microsoft account team |
| High | BCP plan gaps discovered during actual incident | BCP coordinator + IT leadership |
| Medium | Service health monitoring failures | IT Operations — restore monitoring |
| Low | BCP plan update needed | BCP coordinator — schedule update |

## Related Resources

- [Control 4.9: Incident Reporting](../4.9/portal-walkthrough.md)
- [Control 4.11: Microsoft Sentinel Integration](../4.11/portal-walkthrough.md)
