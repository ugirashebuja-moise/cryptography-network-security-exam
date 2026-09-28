# Integrated Situation Final Practical Project

**Module:** Cryptography & Network Security (ETTCS801)  
**Institution:** ULK Polytechnic Institute  
**Student ID:** 4202670018  
**Lecturer:** Isaac TUMWINE  

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

Run the Python utility using command-line arguments:

```powershell
# Display help and available options
python security_toolkit.py -h

# Encrypt a target file
python security_toolkit.py --encrypt sample.txt

# Decrypt an encrypted file
python security_toolkit.py --decrypt sample.txt.enc

# Generate SHA-256 integrity hash
python security_toolkit.py --hash sample.txt

# Verify file integrity against an expected hash
python security_toolkit.py --verify sample.txt <EXPECTED_HASH>
