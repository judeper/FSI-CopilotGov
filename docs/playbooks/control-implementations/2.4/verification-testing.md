# Control 2.4: Information Barriers for Copilot (Chinese Wall) — Verification & Testing

Test cases and evidence collection for validating Information Barrier enforcement with Copilot.

## Test Cases

### Test 1: Barrier Enforcement in Teams Communication

- **Objective:** Verify users in blocked segments cannot communicate via Teams
- **Steps:**
  1. Identify test users in the Investment Banking and Research segments
  2. As the IB user, attempt to start a Teams chat with the Research user
  3. Verify the chat is blocked with an appropriate message
  4. Verify the block event is logged
- **Expected Result:** Communication blocked with clear policy notification
- **Evidence:** Screenshot of block notification and audit log

### Test 2: Copilot Content Grounding Barrier

- **Objective:** Verify Copilot does not ground responses on content from blocked segments
- **Steps:**
  1. Create unique test content accessible only within the Research segment
  2. As an Investment Banking user, ask Copilot a question that would require the Research content
  3. Verify Copilot does not reference or include Research segment content
  4. As a Research user, verify the same Copilot query does return the content
- **Expected Result:** Copilot respects barrier boundaries in content grounding
- **Evidence:** Copilot responses from both segments showing barrier enforcement

### Test 3: SharePoint Barrier Enforcement

- **Objective:** Confirm barriers prevent cross-segment content discovery in SharePoint
- **Steps:**
  1. Verify a SharePoint site owned by the Research segment is not searchable by IB users
  2. Perform a SharePoint search as an IB user for content known to be in Research sites
  3. Verify no results from Research segment sites appear
- **Expected Result:** SharePoint search respects barrier boundaries
- **Evidence:** Search result screenshots from barred user

### Test 4: Barrier Exception Validation

- **Objective:** Verify approved barrier exceptions function correctly
- **Steps:**
  1. Configure a documented exception (e.g., Compliance team can access both segments)
  2. As a Compliance team member, verify access to both IB and Research content
  3. Verify the exception is limited to the approved scope
  4. Confirm exception documentation is current with governance approval
- **Expected Result:** Exceptions work as configured with proper documentation
- **Evidence:** Exception configuration and access verification

### Test 5: Channel Agent IB Coverage Verification

- **Objective:** Confirm Channel Agent deployments comply with the IB gap compensating controls
- **Steps:**
  1. Enumerate all active Channel Agent deployments: navigate to Microsoft 365 Admin Center > Agents > All agents / Registry or Microsoft Teams Admin Center > Teams apps
  2. For each Channel Agent, retrieve the channels where it is deployed
  3. Review the membership of each channel where Channel Agent is deployed
  4. Confirm no channel with an active Channel Agent has members from IB-separated segments
  5. Verify the Channel Agent IB limitation is documented in the firm's supervisory procedures
  6. If sensitivity labels are applied as a compensating control, confirm labeled content in IB-adjacent channels is not accessible via Channel Agent
- **Expected Result:** No Channel Agent is deployed in a channel containing members from IB-separated segments; IB limitation is documented in supervisory procedures
- **Evidence:** Channel Agent deployment list; channel membership review; supervisory procedure documentation

### Test 6: IB Coverage Matrix Completeness

- **Objective:** Verify the IB coverage matrix reflects the actual enforcement status of all Copilot surfaces
- **Steps:**
  1. For each Copilot surface in the control's coverage matrix, perform a functional test from a user in one IB segment to access content from a barrier-separated segment
  2. Confirm Microsoft 365 Copilot Chat, Word, Excel, PowerPoint, Outlook, and Teams Copilot (meeting summaries) all enforce barriers as documented
  3. Confirm Channel Agent does NOT enforce barriers (expected behavior per documented limitation)
  4. Document test results against the coverage matrix
- **Expected Result:** All standard Copilot surfaces enforce IB; Channel Agent gap is confirmed and documented
- **Evidence:** Functional test results for each Copilot surface

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Barrier policy configuration | CSV | Compliance evidence repository | 7 years |
| Barrier enforcement test results | PDF with screenshots | Compliance evidence repository | 7 years |
| Copilot barrier test results | PDF | Compliance evidence repository | 7 years |
| Exception documentation and approval | PDF | Governance document repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 5280 | Information barriers for trading | Barriers support compliance with trading information wall requirements |
| SEC Regulation FD | Fair disclosure requirements | Information barriers help prevent selective disclosure through AI |
| Securities Exchange Act Section 15(f) | Chinese Wall requirements | Barriers support compliance with broker-dealer Chinese Wall obligations |
| MiFID II | Conflict of interest management | Information barriers support compliance with conflict management requirements |
- Back to [Control 2.4](../../../controls/pillar-2-security/2.4-information-barriers.md)
