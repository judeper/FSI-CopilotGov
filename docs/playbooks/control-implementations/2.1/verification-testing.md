# Control 2.1: DLP Policies for Microsoft 365 Copilot Interactions — Verification & Testing

Test cases and evidence collection for the supported Microsoft 365 Copilot and Copilot Chat DLP condition/action patterns. Prompt blocking is in preview and rolling out; confirm tenant availability before running that test.

## Test Cases

### Test 1: Policy and Rule Configuration

- **Objective:** Confirm applicable Copilot DLP rules are in the approved mode and use the dedicated location.
- **Steps:**
  1. Run Script 2 in the [PowerShell Setup](powershell-setup.md).
  2. Verify the policy uses the `CopilotExperiences` enforcement plane.
  3. Verify `Locations` contains `470f2276-e011-4e9d-a6ec-20768be3a4b0`.
  4. Confirm all other policy locations are disabled.
  5. Confirm label-exclusion, prompt-blocking, web-search, and any tenant-available external-email rules match the approved design.
  6. If the Microsoft-deployed default simulation policy is present, review its status and match data.
- **Expected Result:** Applicable rules and location configuration match the approved design.
- **Evidence:** Policy/rule output and portal configuration screenshots.

### Test 2: Label-Based Source Exclusion

- **Objective:** Verify Copilot doesn't process content from a file with a matching sensitivity label.
- **Steps:**
  1. Upload a test document labeled **Highly Confidential** to a SharePoint site accessible to a test user. If using email, send it on or after January 1, 2025; calendar invites aren't supported.
  2. Ask Copilot to summarize or reference the test document.
  3. Verify the response doesn't use the document's content.
  4. Record whether the document remains visible as a citation; this is supported behavior.
  5. Confirm a policy tip appears if configured and review the applicable DLP alert or DSPM AI activity.
  6. Clean up test data.
- **Expected Result:** Labeled content isn't processed; a citation can remain.
- **Evidence:** Response screenshot, policy configuration, and applicable alert/activity record.

### Test 3: SIT-Based Typed-Prompt Blocking

- **Objective:** Verify the preview rule blocks a response when typed prompt text matches a configured SIT.
- **Precondition:** The **Processing prompts** action is available in the tenant.
- **Steps:**
  1. Type an approved synthetic SSN pattern directly into a Copilot prompt.
  2. Verify Copilot doesn't process the request or produce a response.
  3. Verify the configured policy tip appears.
  4. Review the applicable DLP alert or DSPM AI activity.
- **Expected Result:** A matching typed prompt is blocked before grounding.
- **Evidence:** Blocked-prompt screenshot and applicable alert/activity record.

#### Direct-Upload Limitation Test

1. Upload a file containing the same synthetic SIT value without typing the value into the prompt.
2. Record that Copilot DLP doesn't scan the uploaded file's contents for the prompt/web SIT rule.
3. Verify source permissions and sensitivity labels address this path.

### Test 4: SIT-Based External Web-Search Restriction

- **Objective:** Verify a matching typed prompt doesn't use external web search.
- **Steps:**
  1. Confirm **Allow web search in Copilot** is enabled for the test user so the rule can be observed.
  2. Submit a benign prompt requiring current public information and confirm a web citation appears.
  3. Submit an approved synthetic prompt that matches the configured SIT.
  4. Confirm no external web search or web citation is used.
  5. If an approved internal source is available, confirm internal Microsoft 365 grounding can continue.
- **Expected Result:** The matching prompt doesn't use external web search; permitted internal grounding can continue.
- **Evidence:** Before/after screenshots and applicable alert/activity record.

### Test 4a: External-Email Exclusion

- **Objective:** Verify the preview sender-domain rule excludes matching external email.
- **Precondition:** The **Email is received from > External users** action is available and configured.
- **Steps:**
  1. Send a synthetic email from a domain outside the tenant's accepted domains.
  2. Ask Copilot to summarize or reason over that email.
  3. Confirm the email isn't used for grounding or summarization and doesn't appear as a citation.
  4. Confirm the user can still access the email itself and that permitted internal sources remain available.
- **Expected Result:** The external email is excluded based on sender-domain metadata; its body isn't inspected by the condition.
- **Evidence:** Sender/accepted-domain evidence, Copilot result, and applicable alert/activity record.

### Test 5: Combined Supported Actions

- **Objective:** Validate supported rules without assuming general output-SIT scanning.
- **Steps:**
  1. Reference a document carrying a matching sensitivity label and type a synthetic SIT value into the prompt.
  2. If prompt blocking is available, verify the typed-prompt rule acts before grounding.
  3. Remove the typed SIT and repeat the request.
  4. Verify the sensitivity-label rule excludes source content from processing; a citation can remain.
- **Expected Result:** Each supported action operates at its documented enforcement point.
- **Evidence:** Screenshots and applicable DLP/DSPM records for each path.

### Test 6: Endpoint/Browser DLP as a Separate Control

- **Objective:** Verify an independently configured Endpoint/browser DLP policy for an approved browser activity.
- **Steps:**
  1. Confirm the current Endpoint DLP documentation supports the selected browser, activity, device platform, and file type.
  2. Run an approved synthetic-data test for that activity.
  3. Verify the Endpoint DLP rule triggers and its event is recorded.
  4. Don't attribute the result to the Copilot policy location.
- **Expected Result:** The separate Endpoint/browser control behaves as currently documented.
- **Evidence:** Endpoint DLP configuration and event record.

### Test 6a: Adaptive Scoping for SharePoint DLP

- **Objective:** Verify a separate SharePoint DLP policy uses an approved adaptive scope for grounding sources.
- **Steps:**
  1. Configure an adaptive scope targeting a test SharePoint site property.
  2. Attach the adaptive scope to a DLP policy covering the SharePoint location.
  3. Verify the policy includes and excludes the test site as its property changes.
  4. Keep this evidence separate from the Copilot-location policy.
- **Expected Result:** SharePoint scoping follows the approved adaptive-scope rule.
- **Evidence:** SharePoint DLP configuration and match data.

### Test 7: Notifications and Alerts

- **Objective:** Confirm configured policy tips and alerts appear for a supported Copilot rule.
- **Steps:**
  1. Enable user notifications and alerts on a test rule.
  2. Trigger the rule with approved synthetic data.
  3. Confirm the policy tip or blocked-action message appears.
  4. Confirm the alert appears under **Purview > Data Loss Prevention > Alerts**.
  5. Confirm the applicable event appears under **Solutions > DSPM > Discover > Activity explorer > AI activities**.
- **Expected Result:** Configured notifications and alerts are available for investigation.
- **Evidence:** User message, DLP alert, and applicable AI activity screenshots.

### Test 8: False-Positive Assessment

- **Objective:** Evaluate match quality for each applicable rule.
- **Steps:**
  1. Export policy match evidence from the applicable Purview DLP/DSPM view.
  2. Review the institution-approved sample and classify matches.
  3. Calculate the false-positive rate per rule.
  4. Tune SIT patterns or confidence thresholds under the approved change process.
- **Expected Result:** Results meet institution-defined acceptance criteria.
- **Evidence:** Match classification and approval record.

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Copilot DLP policy and rule configuration | CSV/JSON/screenshots | Compliance evidence repository | Per approved schedule |
| Label-source-exclusion results | PDF with screenshots | Compliance evidence repository | Per approved schedule |
| Typed-prompt test and preview-availability record | PDF with screenshots | Compliance evidence repository | Per approved schedule |
| Web-search restriction results | PDF with screenshots | Compliance evidence repository | Per approved schedule |
| External-email exclusion test, where available | PDF with screenshots | Compliance evidence repository | Per approved schedule |
| Direct-upload limitation test | PDF with screenshots | Compliance evidence repository | Per approved schedule |
| DLP alerts and DSPM AI activities | CSV/screenshots | Compliance evidence repository | Per approved schedule |
| False-positive analysis | PDF | Compliance evidence repository | Per approved schedule |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| SEC Regulation S-P (17 CFR §248, amended Dec 3, 2025) | Customer NPI safeguards covering AI interaction surfaces | SIT rules can restrict typed prompts and external web search; sensitivity-label rules can exclude labeled source content from processing |
| FINRA Rule 3110 | Supervisory data controls | Supported DLP rules support compliance with supervisory requirements for data protection in AI interactions |
| GLBA §501(b) | Technical safeguards | Supported DLP rules provide controls for labeled source processing and typed-prompt paths |
| PCI DSS | Cardholder data protection | SIT rules can restrict typed card data in prompts or external web search; sensitivity-label rules can exclude labeled source content |

- Back to [Control 2.1](../../../controls/pillar-2-security/2.1-dlp-policies-for-copilot.md)
