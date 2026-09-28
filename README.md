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
