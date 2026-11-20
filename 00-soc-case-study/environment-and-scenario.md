# Environment and Scenario

## Exercise Type

This is a scenario-based SOC exercise. It uses constructed alert descriptions to model a monitoring shift and an investigation decision process. It is not a production incident, and the project does not include retained raw logs or a deployed lab environment for these events.

## Scenario Objective

Evaluate a set of security alerts, determine which require escalation, identify potentially benign activity, and develop a defensible response plan for a suspected SSH account compromise.

## Telemetry Sources Referenced

| Source | Scenario use | Available detail |
|---|---|---|
| Linux authentication logs | SSH brute-force attempt and successful SSH login after failures | Alert descriptions only; no raw log entries |
| Authentication logs | Multiple failed logins | Alert description only; source described as a known internal asset in the triage notes |
| Sysmon | PowerShell execution and repeated PowerShell commands | Alert descriptions only; no event IDs, process details, or command lines |

## Simulated Monitoring Timeline

The exercise covers five alerts between 09:12 and 10:22 UTC. Refer to `alert-timeline.md` for the chronological summary and `triage-decisions.md` for the documented dispositions.

## Scenario Facts

The following details are explicitly present in the original scenario materials:

- An SSH brute-force alert was generated at 09:12 UTC and described as high-volume failed SSH logins from a single external IP address.
- A PowerShell execution alert was generated at 09:27 UTC and was assessed as routine administrative maintenance.
- Multiple failed logins were reported at 09:44 UTC; the triage notes describe the source as a known internal asset and state that the alert threshold was not exceeded.
- A successful SSH login following repeated failures was reported at 10:05 UTC and escalated as a suspected incident.
- Repeated PowerShell commands were reported at 10:22 UTC. The original materials do not provide a triage disposition or supporting details for this alert.
- The original incident report identifies an external IP address as the origin of the suspected SSH activity, but does not provide the address or establish whether it matches the 09:12 source.

## Analytical Assumptions and Unknowns

The scenario suggests possible credential compromise, but does not prove that an account was compromised. The following details are not available and must not be invented:

- Source IP addresses and whether the SSH alerts share a source.
- Affected hostnames, usernames, and authentication methods.
- Number and timing of individual failed authentication attempts.
- Whether the successful SSH login used the same account and host targeted by the failures.
- The command lines, parent processes, user context, and Sysmon event IDs for either PowerShell alert.
- Whether any post-authentication activity, privilege escalation, persistence, lateral movement, or data access occurred.
- Whether any proposed containment action was actually carried out or validated.

## Scope

This case study evaluates alert triage, investigative reasoning, escalation, and response planning. It does not claim forensic confirmation, malware analysis, host isolation validation, or remediation verification.
