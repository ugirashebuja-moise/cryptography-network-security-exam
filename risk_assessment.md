# Risk Assessment Report

## 1. Assets, Vulnerabilities, and Consequences

| Asset | Vulnerability | Possible Consequences |
| :--- | :--- | :--- |
| **Student Records Server** | Guest network access to the server; weak staff passwords; outdated software. | Unauthorized access leading to confidentiality breaches, grade tampering, and system compromise. |
| **Transferred Student Files** | Unencrypted inter-campus file transfer protocols. | Interception (eavesdropping) or modification (Man-in-the-Middle attacks) of sensitive records in transit. |
| **Server Infrastructure & Services** | Unfiltered exposure to unfamiliar external IP addresses; unpatched software vulnerabilities. | Denial of Service (DoS) attacks, brute-force intrusions, and potential malware or ransomware infection. |

## 2. Risk Rankings

| Risk | Likelihood | Impact | Overall Rank | Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Unauthorized Access to Student Records** | High | High | **1 (Critical)** | Weak passwords combined with guest network access create an easily exploitable entry point for sensitive data theft or modification. |
| **Interception of In-Transit Files** | High | High | **2 (High)** | Transferring student data between campuses without encryption exposes data to packet sniffing and MitM alteration on shared links. |
| **External Intrusion via Outdated Software** | Medium | High | **3 (Medium)** | Known unpatched vulnerabilities and repeated external connection attempts present a severe threat, though perimeter filtering can quickly mitigate direct access. |

## 3. Recommended Controls

1. **Control for Risk 1 (Server Access):** Implement strict Network Segmentation (VLANs) to isolate the guest network, apply Access Control Lists (ACLs) blocking guest traffic to the server, and enforce Multi-Factor Authentication (MFA) along with strong password policies.
2. **Control for Risk 2 (In-Transit Data):** Mandate transport layer encryption (SFTP, HTTPS/TLS) for inter-campus transfers and use client-side file encryption (AES-256) prior to transmission.
3. **Control for Risk 3 (External Threats):** Deploy network firewall rules (`iptables`/`ufw`) to drop traffic from untrusted external IPs, establish an automated software patching schedule, and run an Intrusion Prevention System (e.g., Fail2ban).
