# Phishing Incident Response Workflow

## Purpose

A concise analyst checklist for a suspected phishing report. Use alongside the full [Phishing Incident Response Playbook](phishing_incident_response_playbook.md). Follow local procedures and authorization requirements.

## 1. Intake
- [ ] Record reporter, affected user(s), report time, and case identifier.
- [ ] Preserve the original message and available headers.
- [ ] Capture sender, reply-to, subject, message ID, URLs, and attachment names.

## 2. Triage
- [ ] Check sender identity and domain.
- [ ] Review SPF, DKIM, and DMARC results where available.
- [ ] Identify urgency, impersonation, unusual requests, credential prompts, and attachment indicators.
- [ ] Analyze links and attachments only with approved tools.
- [ ] Record a classification and evidence-based rationale.

## 3. Scope and impact
- [ ] Identify recipients and message delivery scope using authorized telemetry.
- [ ] Determine whether users opened the message, clicked links, opened attachments, submitted credentials, or approved MFA prompts.
- [ ] Identify privileged or high-impact accounts.
- [ ] Mark unavailable telemetry and unresolved questions explicitly.

## 4. Containment decision
- [ ] Determine whether message quarantine or removal is warranted.
- [ ] Validate indicators before blocking senders, domains, or URLs.
- [ ] Coordinate credential resets and session revocation when exposure is suspected.
- [ ] Escalate account restrictions, endpoint isolation, or broader actions to the authorized owner.
- [ ] Record approvals, owners, timestamps, and expected operational impact.

## 5. Investigation and recovery
- [ ] Review sign-in and account activity for suspicious access.
- [ ] Check for relevant mailbox changes and follow-on activity.
- [ ] Coordinate remediation with IT/IAM and system owners.
- [ ] Confirm account recovery and monitoring ownership.

## 6. Closeout
- [ ] Document evidence, timeline, actions, decisions, and outcome.
- [ ] Notify affected users and stakeholders through approved channels.
- [ ] Record gaps and recommended improvements.
- [ ] Track follow-up actions to an owner and due date.

## Decision notes

- **No evidence of interaction:** Document what telemetry was checked and its limitations; do not assume no interaction if telemetry is unavailable.
- **Link clicked, no credential submission known:** Assess the destination and review relevant endpoint/browser and account telemetry as authorized.
- **Credentials or MFA approval may be exposed:** Escalate immediately to incident response and IAM/IT for account-protection actions.
- **Attachment executed or suspicious payload observed:** Initiate the applicable endpoint or malware-response process.
- **Widespread distribution or high-impact account:** Escalate to the incident lead and relevant stakeholders.

This checklist is a training aid, not proof of live incident execution.
