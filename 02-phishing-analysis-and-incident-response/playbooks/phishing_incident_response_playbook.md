# Phishing Incident Response Playbook

## 1. Purpose

This playbook defines a repeatable approach for handling suspected phishing messages, from intake through post-incident review. It is a training framework and should be adapted to the organization's approved policies, tools, authority boundaries, and escalation requirements.

## 2. Scope

Use this playbook for:
- User-reported suspicious emails.
- Email-security alerts involving suspected phishing.
- Suspected credential-harvesting messages.
- Reports of a user clicking a suspicious link, opening an attachment, submitting credentials, or approving an unexpected MFA prompt.

This playbook does not replace malware-response, account-compromise, privacy, legal, or law-enforcement procedures when those processes are required.

## 3. Roles and responsibilities

- **SOC analyst:** Intake, initial triage, evidence preservation, scope assessment, documentation, and escalation.
- **Incident responder:** Coordinates investigation and containment for confirmed or high-risk incidents.
- **IT / IAM:** Performs approved password resets, session revocation, account restrictions, and MFA remediation.
- **Email / messaging administrator:** Performs authorized message tracing, quarantine, purge, and sender/domain controls.
- **User / business contact:** Provides context about interaction with the message and follows security guidance.
- **Security awareness:** Supports targeted user education and broader awareness improvements.
- **Management / incident lead:** Makes or approves decisions according to incident severity and organizational policy.

## 4. Response phases

### Phase 1 — Intake and preservation
1. Record the report source, date/time received, reporter, and affected user(s).
2. Preserve the original message and available headers in accordance with evidence-handling procedures.
3. Record the subject, sender, reply-to address, URLs, attachment names, and message identifiers when available.
4. Avoid interacting with suspicious links or attachments outside approved analysis tooling.

**Output:** Initial case record and preserved message evidence.

### Phase 2 — Initial triage
1. Review the sender address, sending domain, reply-to field, and authentication results (SPF, DKIM, DMARC) where available.
2. Examine the message for impersonation, unusual requests, urgency, credential prompts, and unexpected attachments.
3. Inspect URLs and attachments using approved tools and procedures.
4. Classify the message as suspected phishing, benign, or inconclusive; document the rationale and confidence.
5. Escalate when the message appears targeted, widespread, or likely to involve credential exposure or malware.

**Output:** Triage decision, supporting indicators, and escalation rationale.

### Phase 3 — Impact and scope assessment
1. Determine the message's recipient and delivery scope using authorized email telemetry.
2. Establish whether recipients opened the message, clicked a link, downloaded an attachment, submitted credentials, or approved an MFA prompt.
3. Prioritize users based on access level, sensitivity of accessible systems, and evidence of interaction.
4. If credentials may have been exposed, coordinate with IAM/IT and incident response.
5. Record unknowns explicitly rather than treating missing telemetry as proof that no interaction occurred.

**Output:** Affected-user list, interaction status, impact assessment, and unresolved questions.

### Phase 4 — Containment
Select actions based on evidence, risk, and authorization:
- Quarantine or remove confirmed malicious messages from affected mailboxes.
- Block confirmed malicious URLs, sender addresses, or domains where appropriate.
- Reset credentials for users whose credentials may have been exposed.
- Revoke active sessions or refresh tokens when account compromise is suspected and the action is supported by organizational procedure.
- Restrict or disable an account only when warranted and approved.
- Coordinate endpoint isolation or malware response if an attachment or payload was executed.

Do not apply broad blocking or disablement solely because a message looks suspicious; validate indicators and consider operational impact.

**Output:** Recorded containment actions, approvals, timestamps, and residual risk.

### Phase 5 — Investigation and recovery
1. Review authentication and account activity for suspicious sign-ins, unfamiliar devices or locations, mailbox-rule changes, forwarding changes, and other relevant activity.
2. Determine whether additional activity occurred after any suspected credential exposure.
3. Coordinate remediation with IT/IAM and relevant system owners.
4. Restore access when the account is secured and the responsible team approves recovery.
5. Monitor affected accounts and systems for further suspicious activity.

**Output:** Investigation findings, remediation status, and monitoring plan.

### Phase 6 — Communication and closure
1. Notify affected users and relevant stakeholders through approved channels.
2. Provide clear instructions on required user actions and support contacts.
3. Document the incident timeline, evidence reviewed, decisions, approvals, actions, and outcome.
4. Identify gaps in email controls, detection, response procedures, or user awareness.
5. Recommend updates to filtering, reporting, training, or response procedures.
6. Close the case only when required actions are complete or remaining risks and owners are documented.

**Output:** Final incident record and lessons-learned actions.

## 5. Minimum case documentation

- Case identifier and report source.
- Date/time received and relevant event timestamps (with time zone).
- Sender, reply-to, subject, message ID, recipients, URLs, and attachment details as available.
- Evidence preserved and tools or data sources reviewed.
- Triage classification, confidence, and rationale.
- Recipient interaction status and impact assessment.
- Containment and recovery actions, owners, approvals, and timestamps.
- Stakeholder communications, escalation decisions, and final disposition.
- Outstanding questions, limitations, and lessons learned.

## 6. Escalation triggers

Escalate promptly when:
- A user submitted credentials or approved an unexpected MFA prompt.
- There is evidence of suspicious account access or mailbox changes.
- An attachment was executed or a payload may have run.
- Multiple users or business units are affected.
- A privileged or otherwise high-impact account is involved.
- The activity may involve sensitive data, regulatory obligations, or material business disruption.

## 7. Important limitations

This is a proposed educational playbook. It does not assert that any listed containment, investigation, or recovery action was performed in a live environment. Actual execution depends on organizational authority, approved tools, and incident-specific evidence.
