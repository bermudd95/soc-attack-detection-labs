# End-to-End SOC Case Study: Alert Triage and Incident Response

## Project Overview

This project presents a **scenario-based SOC monitoring and incident response exercise**. It is designed to demonstrate how an analyst reviews security alerts, prioritizes suspicious activity, distinguishes potentially benign behavior from activity requiring escalation, and documents response recommendations.

The exercise uses a constructed scenario and summarized alert descriptions. It does not represent an investigation of a live environment, and no underlying production telemetry or retained lab logs are included. Findings and response actions are therefore limited to the information stated in the scenario.

## Scenario Summary

During a simulated monitoring shift, five alerts were presented across Linux authentication logs, general authentication logs, and Sysmon telemetry:

- An SSH brute-force attempt from an external IP address.
- PowerShell execution associated with routine administrative maintenance.
- Multiple failed logins associated with a known internal asset.
- A successful SSH login following repeated authentication failures.
- Repeated PowerShell commands requiring separate review.

The primary incident scenario concerns the successful SSH authentication following repeated failures. This sequence raises the possibility of credential compromise and warrants escalation. The available scenario information does not establish that the earlier SSH brute-force alert and later successful login involved the same source IP, account, or host. That relationship would need to be validated using authentication records in a real investigation.

## Objectives

1. Prioritize alerts based on severity, context, and potential impact.
2. Evaluate authentication activity for indicators of possible credential compromise.
3. Distinguish potentially authorized administrative activity from suspicious execution.
4. Identify what is known, what is assumed, and what additional evidence is required.
5. Recommend proportionate containment and investigation steps.
6. Document lessons that could improve alert correlation and detection quality.

## Skills Demonstrated

- Security alert triage and prioritization
- Authentication-event analysis and correlation concepts
- Escalation decision-making
- Evaluation of potentially benign administrative activity
- Incident documentation and response planning
- MITRE ATT&CK technique mapping, where supported by the scenario
- Identification of evidence gaps and detection improvements

## Project Files

| File | Purpose |
|---|---|
| `environment-and-scenario.md` | Defines the exercise, telemetry sources, scope, and limitations |
| `alert-timeline.md` | Summarizes the five simulated alerts in chronological order |
| `triage-decisions.md` | Documents the disposition and rationale for each alert |
| `evidence-analysis.md` | Separates scenario facts, analytical interpretation, and evidence still needed |
| `incident-report.md` | Records the suspected SSH incident and proposed response actions |
| `false-positives.md` | Explains the administrative PowerShell alert and benign-activity assessment |
| `lessons-learned.md` | Captures operational lessons from the exercise |
| `detection-improvements.md` | Recommends correlation, validation, and tuning improvements |

## Exercise Limitations

- The alerts and timeline are scenario inputs, not raw event records.
- No IP addresses, usernames, hostnames, command lines, event IDs, or authentication counts are provided beyond the descriptions in the scenario.
- No successful compromise, privilege escalation, persistence, lateral movement, or data access is confirmed.
- Containment and remediation steps are proposed response actions, not verified actions performed on a live system.

These limitations are intentional. The case study focuses on analyst reasoning and documentation without presenting simulated details as observed telemetry.
