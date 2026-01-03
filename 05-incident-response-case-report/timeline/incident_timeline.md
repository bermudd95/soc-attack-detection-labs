# Incident Timeline

| Time (Local) | Event | Source | Notes |
|-------------|------|--------|------|
| 10:14:02 | Encoded PowerShell executed | Sysmon Event ID 1 | Suspicious command-line execution |
| 10:15:10 | certutil invoked | Sysmon Event ID 1 | LOLBin usage to download external resource |
| 10:15:11 | Network connection established | Sysmon Event ID 3 | Outbound connection observed |
