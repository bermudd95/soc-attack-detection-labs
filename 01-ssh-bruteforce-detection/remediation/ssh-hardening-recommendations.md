# SSH Hardening and Remediation Recommendations

## Context

The lab demonstrated successful password discovery for the Ubuntu account `bob_victim` through dictionary-based SSH password guessing. The recommendations below address the credential weakness and reduce exposure to repeated authentication attempts.

These are proposed controls; the original project materials do not confirm that they were implemented.

## Immediate response

1. **Reset the affected credential.** Replace the discovered password with a unique, strong credential. Do not reuse the lab password.
2. **Review account access.** Confirm whether the account requires SSH access and restrict or disable it if it is not needed.
3. **Review authentication records.** Identify failed and successful events, source addresses, timestamps, and any subsequent sessions.
4. **Inspect SSH trust material.** Review `authorized_keys` and account configuration for unrecognized keys or changes.
5. **Review post-authentication activity.** If session or audit telemetry exists, examine commands, privilege changes, new accounts, modified files, and persistence indicators.

## Preventive controls

### Strong authentication

- Enforce unique, sufficiently strong passwords where password authentication remains enabled.
- Prefer SSH public-key authentication with securely managed keys where appropriate.
- Consider multi-factor authentication for administrative access.
- Remove or disable unused accounts and stale credentials.

### Reduce SSH exposure

- Restrict SSH access to approved management networks or VPN paths.
- Use host firewalls or security groups to limit permitted source addresses.
- Disable direct remote login for privileged accounts where operationally appropriate.
- Keep the SSH server and operating system patched.

### Reduce password-guessing opportunities

- Consider rate-limiting or intrusion-prevention controls, such as carefully configured fail2ban, where suitable.
- Monitor authentication failures and successful logins.
- Alert on repeated failures and on suspicious success-after-failure sequences.
- Review exceptions and allowlists regularly; do not trust an address solely because it is internal.

## Verification

After changes, verify that:

- The old credential no longer authenticates.
- Only approved users and sources can reach SSH.
- The intended authentication method is enforced.
- Authentication events are logged and centrally retained where possible.
- Detection alerts fire during a controlled, authorized test.

## Operational caution

Do not disable password authentication or change SSH access controls remotely without confirming an alternative administrative access path. Validate configuration changes in a controlled manner to avoid locking administrators out of the host.
