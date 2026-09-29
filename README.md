# Integrated Situation Final Practical Project

**Module:** Cryptography & Network Security (ETTCS801)  
**Institution:** ULK Polytechnic Institute   

---

## Project Overview

This repository contains the practical security implementation and technical documentation addressing key vulnerabilities in student record management, host isolation, and access control.

---

## Project Structure

```text
.
├── security_toolkit.py                     # Python utility for AES/Fernet encryption/decryption & SHA-256 hashing
├── risk_assessment.md                      # Risk analysis, asset mapping, and priority ranking
├── filter_tests.md                         # iptables rule configuration and netcat empirical test logs
├── cryptography_network_security_exam.tex  # Main technical report source (LaTeX format)
├── cryptography_network_security_exam.pdf  # Compiled final technical report
└── README.md                               # Repository documentation and user guide
```

### 1. Cryptographic Toolkit (`security_toolkit.py`)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Imani-Anto/cryptography-network-security-exam.git](https://github.com/Imani-Anto/cryptography-network-security-exam.git)
   cd cryptography-network-security-exam
   ```
Install Dependencies:

```Bash
pip install cryptography
```
Running the Security Toolkit
```
Encrypt a file:
```

```Bash
python3 security_toolkit.py --encrypt sample.txt
```
Decrypt a file:
```Bash
python3 security_toolkit.py --decrypt sample.txt.enc
```
Calculate SHA-256 hash:

```Bash
python3 security_toolkit.py --hash sample.txt
```
Verify integrity against a hash:

```Bash
python3 security_toolkit.py --verify sample.txt <EXPECTED_SHA256_HASH>
```
## Reproducing Firewall Tests (iptables)
Apply the rules in filter_tests.md:

```Bash
sudo iptables -F
sudo iptables -P INPUT DROP
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -s 192.168.20.0/24 -j DROP
sudo iptables -A INPUT -s 192.168.10.0/24 -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j DROP
```
# Execute connection tests with netcat:

```Bash
# Permitted Staff connection
nc -zv -s 192.168.10.15 192.168.10.100 80

# Blocked Guest connection
nc -zv -w 3 -s 192.168.20.45 192.168.10.100 80
```
