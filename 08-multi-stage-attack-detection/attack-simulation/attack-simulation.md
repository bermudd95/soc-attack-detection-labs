## Multi-Stage Attack Simulation

## Overview
this lab simulates a multi-stage attack aligned with real-world adversary behavior. Each step represents a specific MITRE ATT&CK technique and generates telemetry for detection and correlation. 

---

## Attack Chain Breakdown

### 1. Execution - PowerShell Command (T1059.001)

#### Command
```powershell
powershell -ExecutionPolicy Bypass -Command "whoami"
```

### 2. Defensive Evasion - Encoded PowerShell (T1059.001)

#### Command
```powershell id="nj0xy1"
powershell -enc SQBFAFgAIAAoACcAaABlAGwAbABvACcAKQA=
```

### 3. Persistence - Scheduled Task Creation (T1053)

#### Command
```powershell id="pbcm0i"
schtasks /create /tn "Updater" /tr "cmd.exe" /sc minute /mo 5
```

### 4. Credential Access / Brute Force Signal - Failed Logins (T1110)

#### Command 
```powershell id="jn6u2b"
runas /user:d4nny cmd
```

### 5. Command & Control - Network Request (T1071)

#### Command 
```powershell id="x3a5nl"
powershell -Command "Invoke-WebRequest http://g00gle.c0m"
```

---

## Attack Flow Summary
Execution -> Obfuscation -> Persistence -> Authentication Anomalies -> Network Activity
