# Phishing Incident Response Playbook

## Overview
This project documents a practical phishing incident response playbook designed to guide SOC analysts through identification, containment, and recovery steps following a phishing event.

The playbook emphasizes consistency, speed, and clarity during response operations.

---

## Scope
This playbook applies to:
- Reported phishing emails
- Suspected credential harvesting attempts
- User-reported suspicious messages

---

## Phase 1: Identification
- Review reported email headers and content
- Identify indicators such as:
  - Urgent language
  - Brand impersonation
  - Malicious or shortened links
- Determine if credentials were submitted

---

## Phase 2: Containment
- Block malicious sender domains and URLs
- Remove phishing emails from user inboxes if possible
- Reset affected user credentials
- Revoke active sessions

---

## Phase 3: Eradication
- Identify additional users who received the same email
- Search for similar messages across mail logs
- Validate that no persistence mechanisms exist

---

## Phase 4: Recovery
- Restore account access after credential resets
- Confirm MFA enforcement
- Monitor affected accounts for abnormal activity

---

## Phase 5: Lessons Learned
- Document timeline and response actions
- Identify gaps in detection or user awareness
- Update email filtering and response procedures

---

## Roles & Responsibilities
- SOC Analyst: Triage and investigation
- Incident Responder: Containment and recovery
- IT / IAM Teams: Account remediation
- Security Awareness: User education follow-up

---

## Disclaimer
This playbook is a simulated response framework for training and educational purposes.
