# Alert Triage Decisions

## Alert 1: SSH Brute Force Attempt
**Severity:** Medium  
**Decision:** Escalated  

**Rationale:**
- High volume of failed SSH logins from a single IP
- Pattern consistent with automated brute-force behavior
- Risk of credential compromise

---

## Alert 2: PowerShell Execution
**Severity:** Low  
**Decision:** Closed as Benign  

**Rationale:**
- Command execution matched known administrative behavior
- Originated from an internal management host
- No additional suspicious indicators observed

---

## Alert 3: Multiple Failed Logins
**Severity:** Low  
**Decision:** Monitored  

**Rationale:**
- Failed logins did not exceed alert threshold
- Source IP matched known internal asset
- No evidence of automation

---

## Alert 4: Successful SSH Login After Failures
**Severity:** High  
**Decision:** Escalated to Incident  

**Rationale:**
- Successful authentication following repeated failures
- Potential credential compromise
- Required immediate response and containment
