# Alert Timeline

This timeline represents a simulated SOC monitoring shift with multiple alerts occurring over time.

| Time (UTC) | Alert Type | Severity | Source |
|----------|-----------|----------|--------|
| 09:12 | SSH Brute Force Attempt | Medium | Linux Auth Logs |
| 09:27 | PowerShell Execution Detected | Low | Sysmon |
| 09:44 | Multiple Failed Logins | Low | Authentication Logs |
| 10:05 | Successful SSH Login After Failures | High | Linux Auth Logs |
| 10:22 | Repeated PowerShell Commands | Medium | Sysmon |

---

Each alert was investigated independently and correlated where applicable.
