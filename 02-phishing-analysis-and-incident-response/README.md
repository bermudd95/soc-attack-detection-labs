# Phishing Analysis & Incident Response

## Overview
This consolidated project brings together a simulated phishing-email analysis, user-awareness guidance, and a structured incident-response playbook. It demonstrates how a security team can connect user reporting and email review with impact assessment, containment, investigation, recovery, and post-incident improvement.

## Project contents

| Path | Purpose |
|---|---|
| `phishing-analysis/sample_phishing_email.md` | Training example of a brand-impersonation and credential-reset lure, with analyst observations and evidence limitations |
| `security-awareness/phishing_awareness_guide.md` | Practical guidance for recognizing, handling, and reporting suspicious messages |
| `security-awareness/phishing_awareness_presentation.pptx` | Revised awareness presentation for employee training |
| `playbooks/phishing_incident_response_playbook.md` | Response phases, decision points, responsibilities, and documentation requirements |
| `playbooks/phishing_response_workflow.md` | Condensed analyst workflow for handling a reported message |

## Learning objectives
- Identify common phishing indicators, including sender mismatch, urgency, impersonation, and suspicious links.
- Distinguish observable message characteristics from assumptions about attacker infrastructure or user impact.
- Assess whether a message was delivered, opened, clicked, or used to submit credentials.
- Apply proportionate containment and account-remediation actions when authorized.
- Document findings, decisions, evidence, and follow-up actions.
- Communicate practical reporting guidance to end users.

## Scenario and evidence boundaries
The included email is a **simulated training artifact**. It uses a Gmail sender while claiming to be from Mastercard IT, and its displayed link points to a Wikipedia page. The link is not presented as a live malicious destination. No live phishing campaign, credential collection, inbox search, endpoint investigation, or account compromise is demonstrated by this project.

The playbook and workflow are **proposed training procedures**, not evidence that the listed actions were executed in a production environment. Actions such as message purging, sender/domain blocking, password resets, session revocation, and account disablement require the appropriate authorization, tooling, and organizational process.

## MITRE ATT&CK
This project discusses phishing as a social-engineering delivery method. A specific ATT&CK technique should be assigned only when the scenario and available evidence support it. The sample email alone does not establish that a user opened the message, clicked the link, submitted credentials, or that an attacker gained access. Accordingly, this package does not claim a confirmed compromise or a completed ATT&CK chain.

## Skills demonstrated
- Phishing email review and social-engineering indicator identification
- Security awareness content development
- Incident triage and impact-assessment planning
- Incident-response workflow design
- Evidence-conscious reporting and escalation
- Security communication and documentation

## Disclaimer
For educational and portfolio demonstration purposes only. The sample message is simulated; no live phishing activity or unauthorized access was performed.
