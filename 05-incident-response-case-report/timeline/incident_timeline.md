# Incident Timeline

| Time (Local) | Event | Source | Notes |
|-------------|------|--------|------|
| 10:24:35 | Encoded PowerShell executed | Sysmon Event ID 1 | Suspicious command-line execution |
| 10:22:23 | certutil invoked | Sysmon Event ID 1 | LOLBin usage to download external resource |
| 10:27:30 | Network connection established | Sysmon Event ID 3 | Outbound connection observed |
