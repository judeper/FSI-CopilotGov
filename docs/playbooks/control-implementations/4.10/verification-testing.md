# Control 4.10: Business Continuity and Disaster Recovery — Verification & Testing

Test cases and evidence collection procedures for Copilot business continuity and disaster recovery.

## Test Cases

### Test 1: Service Health Monitoring Validation

- **Objective:** Verify that service health monitoring detects and reports Copilot-related service issues
- **Steps:**
  1. Run the service health check script and review current status.
  2. Verify notification delivery by checking for recent advisory emails.
  3. Confirm the monitoring covers all Copilot dependency services.
  4. Test the API-based monitoring integration if configured.
- **Expected Result:** Service health monitoring is operational and notifications are delivered.
- **Evidence:** Service health report output and recent notification email samples.

### Test 2: Fallback Procedure Tabletop Exercise

- **Objective:** Validate that business units can operate without Copilot using documented fallback procedures
- **Steps:**
  1. Conduct a tabletop exercise simulating a Copilot service outage.
  2. Walk through each business process fallback procedure with the responsible teams.
  3. Verify teams know how to access fallback tools and procedures.
  4. Time the transition from normal operations to fallback mode.
- **Expected Result:** All business units can transition to fallback procedures within the defined RTO.
- **Evidence:** Tabletop exercise report with participant sign-off and timing results.

### Test 3: Communication Plan Execution

- **Objective:** Confirm the outage communication plan can be executed quickly and reaches all stakeholders
- **Steps:**
  1. Simulate an outage notification scenario.
  2. Send a test notification through the communication chain.
  3. Verify receipt by department heads and end user representatives.
  4. Measure time from incident detection to full communication delivery.
- **Expected Result:** Outage communication reaches all stakeholders within 30 minutes of detection.
- **Evidence:** Communication delivery timestamps and acknowledgment records.

### Test 4: Recovery Procedure Validation

- **Objective:** Verify that recovery from a Copilot outage restores normal operations correctly
- **Steps:**
  1. After a tabletop or actual outage, walk through the recovery procedure.
  2. Verify Copilot services are operational and accessible to users.
  3. Confirm that no data was lost or governance controls were impacted.
  4. Document any issues encountered during recovery.
- **Expected Result:** Recovery procedure restores full Copilot functionality with governance controls intact.
- **Evidence:** Recovery validation report with pre/post comparison of service status.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Service health reports | PowerShell/API | CSV | 1 year |
| Tabletop exercise report | BCP team | Document | 7 years |
| Communication test results | Email/Teams | Screenshot | With exercise report |
| Recovery validation | IT Operations | Document | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FFIEC BCP Booklet | Business continuity planning and testing | Supports compliance with BCP testing requirements for AI service dependencies |
| FINRA 4370 | Business continuity plan | Helps meet broker-dealer BCP requirements |
| OCC Heightened Standards | Technology resilience | Supports expectations for technology recovery capabilities |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for continuity issues
- Proceed to [Control 4.11](../4.11/portal-walkthrough.md) for Sentinel integration
