# Baseline hardening checklist

Use this as a starting point for personal devices, small teams, or as a prompt for an organization's formal control review. Prefer supported vendor settings and documented changes. Mark controls **done**, **not applicable**, or **needs follow-up** and record an owner for follow-up items.

## 1. Accounts and credentials

- [ ] Use a unique password for every account; store them in a reputable password manager.
- [ ] Turn on MFA for email, password manager, financial, administrator, and cloud accounts. Prefer passkeys or security keys where supported; otherwise use an authenticator app over SMS when practical.
- [ ] Protect recovery email, phone numbers, backup codes, and account-recovery questions. Store recovery codes securely and separately from the account they recover.
- [ ] Review active sessions, trusted devices, connected apps, app passwords, and forwarding rules. Revoke anything unrecognized or no longer needed.
- [ ] Remove stale accounts and access promptly when people leave or roles change.
- [ ] Use separate standard and administrator accounts where supported. Do routine work without elevated privileges.
- [ ] Never share passwords or MFA codes in chat, email, or with an unsolicited caller. Verify unusual requests through a known, independent channel.

## 2. Endpoints

- [ ] Enable automatic security updates for the operating system, browsers, and commonly used applications.
- [ ] Replace unsupported operating systems and devices; establish an owner and replacement date for anything that cannot be updated.
- [ ] Enable the built-in firewall and reputable endpoint protection; investigate alerts rather than dismissing them reflexively.
- [ ] Use device encryption and a strong screen lock. Configure automatic screen locking and secure boot where available.
- [ ] Install software only from trusted vendor or platform sources. Remove software and browser extensions that are not needed.
- [ ] Keep backups of important data. Keep at least one backup protected from routine modification and test restoring files periodically.
- [ ] Report lost devices quickly; use the supported device-lock or remote-wipe process when appropriate.

## 3. Browsers and web use

- [ ] Keep browsers updated and use supported browsers.
- [ ] Remove unused extensions; review requested permissions before installation and periodically afterward.
- [ ] Use a password manager's domain matching and autofill behavior to help spot lookalike login pages.
- [ ] Treat unexpected links, attachments, QR codes, and login prompts as untrusted. Navigate to services using a saved bookmark or known address.
- [ ] Do not bypass certificate warnings. A warning can indicate a misconfiguration, captive portal, or interception; stop and verify using a trusted route.
- [ ] Avoid entering credentials after following an unsolicited link. Verify the request independently.

## 4. Email and phishing resilience

- [ ] Enable the email provider's available spam, impersonation, and attachment protections.
- [ ] Require MFA on email and restrict who can change recovery information and forwarding settings.
- [ ] Treat urgency, secrecy, payment changes, credential requests, and unexpected MFA prompts as reasons to verify independently.
- [ ] Report suspicious messages using the organization's established process; do not forward sensitive messages to personal accounts.
- [ ] If a link was opened or credentials entered, report it promptly. Early reporting is more useful than blame.
- [ ] For organizations operating a mail domain, configure SPF, DKIM, and DMARC using provider guidance and monitor reports before tightening enforcement.

## 5. Cloud and SaaS accounts

- [ ] Require MFA, especially for administrators and billing/security owners.
- [ ] Use named accounts, role-based access, and least privilege; avoid shared administrator accounts and long-lived keys.
- [ ] Review administrators, service accounts, OAuth grants, API keys, access tokens, and external sharing on a schedule.
- [ ] Prefer short-lived credentials and managed identities where the provider supports them. Store necessary secrets in an approved secrets manager, never in source code or tickets.
- [ ] Turn on audit logs and security alerts, protect them from routine deletion, and know who reviews them.
- [ ] Set billing alerts and review public exposure, storage sharing, network rules, and backup coverage.
- [ ] Document a safe process to revoke sessions, keys, tokens, and integrations during an incident.

## 6. Home and small-office Wi-Fi

- [ ] Use the strongest current mode supported by all required devices (for example, WPA3-Personal where supported, otherwise WPA2-AES); avoid obsolete protocols and mixed modes when feasible.
- [ ] Change default router administrator credentials and use a unique Wi-Fi passphrase.
- [ ] Install router firmware updates; replace equipment that no longer receives security updates.
- [ ] Disable remote administration and convenience features you do not use. Review vendor guidance before changing unfamiliar settings.
- [ ] Use a guest network for visitors and less-trusted devices when supported. Keep router administration limited to trusted devices.
- [ ] Review the router's connected-device list and authentication/security logs when investigating an unfamiliar device. Device names and MAC addresses can be spoofed, so treat them as clues, not proof of identity.

## 7. Preparation and recovery

- [ ] Know who to contact for IT, security, cloud, email, and internet-provider support.
- [ ] Keep an inventory of important accounts, devices, owners, and recovery contacts without storing secrets in the inventory.
- [ ] Know how to disable an account, revoke sessions, isolate a device, and contact the provider.
- [ ] Keep incident notes with timestamps and time zones. Preserve relevant logs and messages before making changes when it is safe to do so.
- [ ] Test restoring backups and document what was learned.
- [ ] Review this checklist at least annually and after major changes or incidents.

## If you suspect compromise

1. If there is active harm, contact your security/IT team or provider immediately. Use a known-clean device for sensitive account actions.
2. Preserve relevant alerts, messages, timestamps, and logs. Avoid wiping or resetting a suspected device before getting appropriate advice, unless necessary to stop ongoing harm.
3. Contain through trusted administrative channels: revoke sessions/tokens, disable affected accounts, or isolate affected devices as appropriate.
4. Change affected credentials from a known-clean device, starting with email and identity-provider accounts; review recovery methods and MFA registrations.
5. Follow the [incident response playbook](incident-response.md) to scope impact, remediate, and recover.
