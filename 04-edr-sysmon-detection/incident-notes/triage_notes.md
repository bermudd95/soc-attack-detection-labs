## Incident Triage Notes

**Alert Type:** Suspicious PowerShell Execution  
**Severity:** Medium  
**Host:** Windows 11 Endpoint  
**Status:** Closed – Benign Activity (Lab Simulation)

### Actions Taken
- Reviewed Sysmon Event ID 1
- Validated command-line execution
- Confirmed activity was user-initiated in lab environment

### Recommendations
- Monitor for repeated encoded PowerShell executions
- Alert on PowerShell launched from non-standard parent processes
