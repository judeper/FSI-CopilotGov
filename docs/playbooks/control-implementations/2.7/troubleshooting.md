# Control 2.7: Data Residency and Cross-Border Data Flow — Troubleshooting

Common issues and resolution steps for data residency controls.

## Common Issues

### Issue 1: Data Location Not Matching Expected Geography

- **Symptoms:** Admin Center shows data location in a different geography than expected based on the tenant's country
- **Root Cause:** Tenant was provisioned in a multi-national region, or the tenant was created before region-specific data centers were available.
- **Resolution:**
  1. Review the tenant creation date and original provisioning geography
  2. Check if Advanced Data Residency (ADR) is available for your region
  3. If ADR is available, evaluate migration to in-country data storage
  4. Document the current location and assess regulatory impact

### Issue 2: Cross-Border Data Access by Traveling Employees

- **Symptoms:** Employees traveling internationally access Copilot from foreign locations, creating cross-border data flow events
- **Root Cause:** Mobile workforce accessing cloud services from various countries is normal for global organizations.
- **Resolution:**
  1. Document the cross-border access as expected business activity
  2. Verify VPN usage policies for international travel (route through home country)
  3. Consider Conditional Access policies to restrict Copilot access from certain countries
  4. Maintain travel-based access records for compliance documentation

### Issue 3: Multi-Geo Configuration Complexity

- **Symptoms:** Users assigned to different data locations experience inconsistent Copilot behavior or content access
- **Root Cause:** Multi-Geo configurations create complexity in how content is stored and accessed across regions.
- **Resolution:**
  1. Verify each user's Preferred Data Location assignment is correct
  2. Review how Copilot handles cross-geo content references
  3. Simplify Multi-Geo assignments where possible
  4. Document known cross-geo behavior for user awareness

### Issue 4: Regulatory Requirements Conflicting with Service Architecture

- **Symptoms:** Regulatory requirements demand data remain in a specific jurisdiction, but Microsoft 365 architecture may process certain data operations in other locations
- **Root Cause:** Some Microsoft 365 services have global processing components that may not align with strict data localization requirements.
- **Resolution:**
  1. Review Microsoft's data residency commitments in the DPA and product terms
  2. Evaluate the EU Data Boundary or Advanced Data Residency add-ons
  3. Document any processing that occurs outside the required jurisdiction with legal justification
  4. Consult legal counsel on the adequacy of Microsoft's contractual commitments

## Diagnostic Steps

1. **Verify data location:** Admin Center > Settings > Org Settings > Data Location
2. **Check user assignments:** Run Script 2 for Multi-Geo user distribution
3. **Monitor access patterns:** Run Script 3 for cross-border access detection
4. **Review Microsoft commitments:** Check DPA and product terms for residency commitments
5. **Consult legal:** Verify compliance position with legal counsel

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Minor documentation gaps | Compliance team |
| **Medium** | Cross-border access patterns requiring review | Legal and Compliance |
| **High** | Data located in unexpected geography | Legal, CISO, and Microsoft account team |
| **Critical** | Regulatory violation due to data location | General Counsel, CRO, and executive management |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Residency verification steps
- [PowerShell Setup](powershell-setup.md) — Monitoring scripts
- [Verification & Testing](verification-testing.md) — Residency validation
