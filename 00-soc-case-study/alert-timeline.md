# Alert Timeline

This timeline summarizes five alerts in a constructed SOC monitoring scenario. The entries are alert-level descriptions, not raw event records.

| Time (UTC) | Alert | Severity | Telemetry source | Scenario context |
|---|---|---|---|---|
| 09:12 | SSH brute-force attempt | Medium | Linux authentication logs | High-volume failed SSH logins from a single external IP address, according to the triage notes |
| 09:27 | PowerShell execution detected | Low | Sysmon | Later assessed as routine administrative maintenance |
| 09:44 | Multiple failed logins | Low | Authentication logs | Triage notes identify the source as a known internal asset; activity did not exceed the alert threshold |
| 10:05 | Successful SSH login after failures | High | Linux authentication logs | Escalated as a suspected account compromise because successful authentication followed repeated failures |
| 10:22 | Repeated PowerShell commands | Medium | Sysmon | Separate alert; the original scenario does not document its investigation or disposition |

## Correlation Notes

The 09:12 SSH brute-force alert and the 10:05 successful SSH login are both relevant to the suspected SSH incident. However, the scenario does not provide the source IP, username, or destination host needed to confirm that they are part of the same activity sequence. The relationship should therefore be treated as a correlation hypothesis, not an established fact.

The 09:44 failed-login alert is described as originating from a known internal asset. The scenario does not establish that it is related to the external SSH activity.

The 09:27 and 10:22 PowerShell alerts are Sysmon-based endpoint alerts. They should be evaluated separately from the SSH incident unless additional evidence establishes a relationship. The 10:22 alert has no documented disposition in the original scenario and remains unresolved in this case study.

## Timeline Limitations

No exact IP addresses, hostnames, usernames, event IDs, command lines, or raw timestamps beyond the summarized alert times were supplied. The timeline should not be interpreted as a complete forensic event sequence.
