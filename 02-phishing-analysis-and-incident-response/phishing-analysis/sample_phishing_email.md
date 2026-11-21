# Sample Phishing Email — Credential-Reset Lure

## Message

- **From:** `mastercardsIT@gmail.com`
- **To:** `employee@email.com`
- **Subject:** `URGENT! Password Reset Required!`

> Hello [Employee Name],
>
> During a routine audit, we noticed that your email account may have been compromised. We strongly recommend resetting your password immediately to reduce the risk of unauthorized access.
>
> Please click the link below to reset your password within the next hour, or your account will be temporarily locked:
>
> `https://en.wikipedia.org/wiki/Phishing`
>
> Regards,  
> Mastercard IT

## Analyst observations

| Indicator | Observation | Why it matters |
|---|---|---|
| Sender mismatch | The sender uses a public Gmail address while claiming to represent Mastercard IT | The sender domain does not establish an official corporate origin |
| Brand impersonation | The message claims to come from Mastercard IT | Attackers may borrow trusted brand names to increase credibility |
| Urgency | The recipient is given one hour to act | Time pressure can discourage careful verification |
| Threat of account lockout | The message warns that the account will be locked | A consequence is used to pressure the recipient into acting |
| Credential-reset pretext | The message asks the recipient to reset an account password | Password-reset themes can be used to direct users to credential-harvesting pages |
| Link mismatch in this sample | The supplied URL resolves to a Wikipedia page about phishing | This is a training placeholder, not evidence of a malicious landing page |

## Assessment

This is a **simulated phishing-awareness example** that illustrates brand impersonation, urgency, and a credential-reset pretext. The sender address is inconsistent with the claimed organization. However, the supplied URL is a Wikipedia page, not a demonstrated credential-harvesting destination.

The message alone does not establish that it was delivered to a real mailbox, that a recipient clicked the link, that credentials were submitted, or that an account was compromised.

## Recommended analyst checks

If this were a real user-reported message, an analyst would preserve the original message and review, as available and authorized:

1. Full email headers, including SPF, DKIM, and DMARC results.
2. The actual sender address, reply-to address, sending infrastructure, and authentication results.
3. The destination URL and any redirect chain, using approved analysis tools.
4. Message recipients and delivery scope.
5. Whether any recipient opened the message, clicked a link, downloaded an attachment, or submitted credentials.
6. Authentication and account activity for affected users if interaction or credential exposure is suspected.

## Handling guidance

Do not click the link or reply to the sender. Report the message using the organization's approved phishing-reporting process. Do not forward it in a way that strips headers or changes the original evidence unless the organization's procedure instructs you to do so.

## Evidence limitations

This file is a constructed training example. It contains no original email headers, message trace, URL reputation results, mailbox telemetry, authentication logs, or proof of user interaction.
