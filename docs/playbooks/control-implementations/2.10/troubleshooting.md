# Control 2.10: Insider Risk Detection for Copilot Usage — Troubleshooting

Common issues and resolution steps for insider risk detection.

## Common Issues

### Issue 1: No Copilot-Specific Indicators Available

- **Symptoms:** Insider Risk Management settings do not show Copilot-specific indicators
- **Root Cause:** Copilot-specific indicators may require specific licensing or may be in staged rollout.
- **Resolution:**
  1. Verify Microsoft 365 E5 Compliance licensing is active
  2. Check the Microsoft 365 roadmap for Copilot insider risk indicator availability
  3. Use general data access and DLP-based indicators as alternatives
  4. Configure custom indicators using Copilot audit log events

### Issue 2: High Volume of Low-Quality Alerts

- **Symptoms:** Insider risk generates many alerts for routine Copilot usage, overwhelming investigators
- **Root Cause:** Risk thresholds may be too sensitive, or the baseline for normal Copilot usage has not been properly established.
- **Resolution:**
  1. Allow 2-4 weeks for the system to establish behavioral baselines
  2. Adjust risk level thresholds upward to reduce noise
  3. Use priority user groups to focus detection on higher-risk roles
  4. Implement alert filtering to separate low-confidence from high-confidence signals

### Issue 3: Insider Risk Data Not Correlating with Copilot Events

- **Symptoms:** Insider risk alerts do not include Copilot-specific context or activity details
- **Root Cause:** Audit log data for Copilot may not be fully integrated with the insider risk management data pipeline.
- **Resolution:**
  1. Verify audit logging is enabled for Copilot interactions
  2. Check that the Copilot audit record type is included in the insider risk data sources
  3. Use supplementary monitoring (Script 2) to correlate Copilot usage with risk signals
  4. Configure SIEM integration to provide additional correlation context

### Issue 4: Legal Concerns About Employee Monitoring

- **Symptoms:** Legal or HR team raises concerns about the scope of insider risk monitoring for Copilot
- **Root Cause:** Employee monitoring requires careful balancing of security needs with privacy rights and employment law compliance.
- **Resolution:**
  1. Enable pseudonymization to protect employee identity until investigation threshold
  2. Document the legal basis for monitoring (e.g., regulatory obligation, acceptable use policy)
  3. Obtain legal counsel review of the insider risk program scope
  4. Communicate monitoring expectations through the acceptable use policy and training
  5. Limit investigator access to the minimum necessary for triage

## Diagnostic Steps

1. **Check policy status:** Run Script 1 to verify policies are active
2. **Review indicators:** Purview > Insider Risk > Settings > Indicators
3. **Test detection:** Generate test activity and monitor for risk signals
4. **Review audit logs:** Verify Copilot events appear in the unified audit log
5. **Check privacy settings:** Verify pseudonymization is properly configured

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Alert tuning needed | Insider risk management team |
| **Medium** | Indicators not detecting expected patterns | Security Operations and Microsoft support |
| **High** | True positive insider risk alert on sensitive data | CISO, Legal, and HR per investigation procedures |
| **Critical** | Active data exfiltration detected via Copilot | Incident response team immediately |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Insider risk configuration
- [PowerShell Setup](powershell-setup.md) — Monitoring scripts
- [Verification & Testing](verification-testing.md) — Detection validation
