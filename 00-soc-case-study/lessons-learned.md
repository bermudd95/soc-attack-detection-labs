# Lessons Learned

This section captures operational lessons from the simulated monitoring scenario. The observations are based on the alert descriptions and triage decisions supplied for the exercise, not on analysis of raw telemetry.

## 1. Correlate Authentication Events Before Confirming Compromise

**Scenario observation:** The timeline includes an SSH brute-force alert and a later successful SSH login following repeated failures.

**Lesson:** The sequence warrants escalation, but a relationship between the alerts should be confirmed by comparing source IP, username, destination host, and timestamps.

## 2. Use Context When Evaluating Administrative Execution

**Scenario observation:** The 09:27 PowerShell alert was closed as benign based on a known administrator account, an approved maintenance window, and an internal management host.

**Lesson:** Administrative context can help distinguish authorized activity from suspicious execution, but it should be validated using command details, process lineage, and an authoritative maintenance record.

## 3. Do Not Treat Internal Sources as Automatically Trusted

**Scenario observation:** The 09:44 failed-login alert was monitored because the source was identified as a known internal asset and the activity did not exceed the alert threshold.

**Lesson:** Internal origin and low event volume are contextual factors, not proof of benign behavior. Asset ownership, expected behavior, targeted accounts, and subsequent authentication results should also be considered.

## 4. Give Every Alert an Explicit Disposition

**Scenario observation:** The 10:22 repeated PowerShell alert appears in the timeline but has no documented triage outcome in the original materials.

**Lesson:** Each alert should have a recorded status, rationale, owner or escalation path, and follow-up requirement. Unresolved alerts should not be silently treated as benign.

## 5. Separate Confirmed Facts From Hypotheses

**Scenario observation:** The SSH sequence raises concern about possible account compromise, but the scenario does not include raw authentication records or post-login activity.

**Lesson:** Incident documentation should identify what is known, what is suspected, and what evidence is still needed. This prevents potential impact from being reported as confirmed compromise.

## Future Improvements

- Add validated correlation logic for failed SSH attempts followed by successful authentication.
- Document a consistent evidence checklist for authentication and endpoint alerts.
- Define a triage path for repeated PowerShell execution.
- Review alert thresholds against expected behavior while preserving visibility into suspicious activity.
- Standardize incident notes to capture evidence, confidence, decisions, and outstanding questions.
