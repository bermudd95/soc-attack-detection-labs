## Sysmon Detection Analysis

### Event Observed
- Event ID: 1 (Process Creation)
- Process: powershell.exe
- Command Line: Encoded PowerShell execution
- User Context: Standard user

### Analyst Assessment
Encoded PowerShell execution is commonly used by attackers to obfuscate
commands and evade detection. While this activity was simulated in a controlled
environment, it would warrant further investigation in a production setting.

### MITRE ATT&CK Mapping
- T1059.001 – PowerShell
- T1027 – Obfuscated Files or Information
