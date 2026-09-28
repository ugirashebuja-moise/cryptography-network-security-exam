# Cryptography & Network Security Project report

## Overview
This repository contains the security deliverables for the ULK Polytechnic Institute cryptography and network security assessment. It includes a Python file encryption/decryption and integrity verification toolkit, network traffic filtering rule sets, risk assessment documentation, and an overall technical report in LaTeX.

---

## 1. Project Directory Structure

```text
cryptography-network-security-exam/
├── README.md                   # Project overview, structure, installation, and run guide
├── risk_assessment.md          # Task 1: Assets, vulnerabilities, risk rankings, & controls
├── security_toolkit.py         # Task 2: Python script for encryption, decryption, and SHA-256 hashing
├── firewall_rules.sh           # Task 3: Shell script containing iptables traffic filtering rules
├── filter_tests.md             # Task 3: Commands, expected outcomes, and actual test results
├── report.tex                  # Task 5: Complete LaTeX source for technical report
├── report.pdf                  # Task 5: Compiled PDF technical report
├── sample_student_record.txt   # Sample data file generated for demonstration
└── .gitignore                  # Git ignore file excluding secret keys and transient files
# File Security Toolkit

A Python utility for file encryption, decryption, SHA-256 integrity verification, and tamper detection using AES-128 via the `cryptography` (Fernet) library.

---

## Features

- **Symmetric Encryption & Decryption**: Secure files using Fernet (AES-128 in CBC mode with HMAC-SHA256 authentication).
- **Integrity Verification**: Calculate and compare SHA-256 hashes to detect unauthorized file tampering.
- **CLI & Automated Workflow**: Run as a command-line utility or execute an automated test/demo workflow.
- **Robust Error Handling**: Handles missing files, invalid encryption keys, and empty files gracefully.

---

## Prerequisites & Installation

### 1. Requirements
- Python 3.8 or higher
- `pip` (Python package installer)

### 2. Install Dependencies
Install the required `cryptography` library:

```bash
pip install cryptography
