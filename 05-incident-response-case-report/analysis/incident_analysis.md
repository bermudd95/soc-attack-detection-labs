# Incident Analysis

## Summary
Endpoint telemetry identified suspicious PowerShell execution using encoded
commands, followed by the use of certutil to access an external resource.

## Indicators Observed
- Encoded PowerShell command execution
- LOLBin usage (certutil)
- Outbound network activity

## Assessment
Encoded PowerShell and LOLBin usage are common attacker techniques used to
obfuscate malicious activity and bypass detection controls. In this case,
analysis confirmed the activity was initiated by the user in a controlled
lab environment.

## MITRE ATT&CK Mapping
- T1059.001 – PowerShell
- T1027 – Obfuscated Files or Information
- T1218 – Signed Binary Proxy Execution
