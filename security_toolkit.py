#!/usr/bin/env python3
"""
Task 2: Encryption, Decryption, Integrity Verification, and Error Handling
"""

import os
import sys
import hashlib
from cryptography.fernet import Fernet, InvalidToken

KEY_FILE = "secret.key"
SAMPLE_RECORD_FILE = "sample_student_record.txt"


def load_or_generate_key() -> bytes:
    if os.path.exists(KEY_FILE):
        try:
            with open(KEY_FILE, "rb") as kf:
                key = kf.read().strip()
                if not key:
                    raise ValueError("Key file is empty.")
                return key
        except Exception as e:
            print(f"[-] Error reading key file '{KEY_FILE}': {e}")
            sys.exit(1)
    else:
        print(f"[*] Encryption key not found. Generating new key at '{KEY_FILE}'...")
        key = Fernet.generate_key()
        try:
            with open(KEY_FILE, "wb") as kf:
                kf.write(key)
            print(f"[!] IMPORTANT: Add '{KEY_FILE}' to your .gitignore to keep it outside the repository!")
            return key
        except Exception as e:
            print(f"[-] Failed to write key file: {e}")
            sys.exit(1)


# ==============================================================================
# 2a. ENCRYPTION FUNCTIONALITY 
# ==============================================================================
def encrypt_file(input_path: str, output_path: str, key: bytes) -> bool:
    print(f"\n--- [2a] Encrypting File: '{input_path}' ---")
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Source file '{input_path}' does not exist.")

        fernet = Fernet(key)
        with open(input_path, "rb") as f:
            plaintext = f.read()

        if len(plaintext) == 0:
            print("[!] Warning: Encrypting an empty file.")

        encrypted_data = fernet.encrypt(plaintext)

        with open(output_path, "wb") as f:
            f.write(encrypted_data)

        print(f"[+] File successfully encrypted.")
        print(f"[+] Output written to: '{output_path}'")
        return True

    except FileNotFoundError as fnf_err:
        print(f"[-] Error [2a]: {fnf_err}")
        return False
    except Exception as e:
        print(f"[-] Unexpected error during encryption: {e}")
        return False


# ==============================================================================
# 2b. DECRYPTION AND CONTENT VERIFICATION
# ==============================================================================
def decrypt_file(input_path: str, output_path: str, key: bytes, original_path: str = None) -> bool:
    print(f"\n--- [2b] Decrypting File: '{input_path}' ---")
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Encrypted file '{input_path}' does not exist.")

        fernet = Fernet(key)
        with open(input_path, "rb") as f:
            ciphertext = f.read()

        decrypted_data = fernet.decrypt(ciphertext)

        with open(output_path, "wb") as f:
            f.write(decrypted_data)

        print(f"[+] File successfully decrypted.")
        print(f"[+] Output saved to: '{output_path}'")

        if original_path and os.path.exists(original_path):
            with open(original_path, "rb") as orig_f:
                original_data = orig_f.read()

            if decrypted_data == original_data:
                print("[+] Content Match Verification: PASSED (Decrypted file perfectly matches original).")
            else:
                print("[!] Content Match Verification: FAILED (Decrypted file differs from original).")

        return True

    except FileNotFoundError as fnf_err:
        print(f"[-] Error [2b]: {fnf_err}")
        return False
    except InvalidToken:
        print("[-] Decryption Failed [2b]: Invalid encryption key or ciphertext has been tampered with.")
        return False
    except Exception as e:
        print(f"[-] Unexpected error during decryption: {e}")
        return False


def calculate_sha256(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Target file '{file_path}' does not exist.")
        
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


# ==============================================================================
# 2c. SHA-256 HASHING AND INTEGRITY DETECTION
# ==============================================================================
def detect_file_tampering(file_path: str, original_hash: str) -> bool:
    print(f"\n--- [2c] Calculating SHA-256 & Checking File Integrity ---")
    try:
        current_hash = calculate_sha256(file_path)
        print(f"[*] Baseline SHA-256 : {original_hash}")
        print(f"[*] Current SHA-256  : {current_hash}")

        if current_hash.lower() == original_hash.lower():
            print("[+] Integrity Check PASSED: File has NOT been modified.")
            return True
        else:
            print("[!] Integrity Check FAILED: ALERT! File modification/tampering detected!")
            return False

    except FileNotFoundError as fnf_err:
        print(f"[-] Error [2c]: {fnf_err}")
        return False
    except Exception as e:
        print(f"[-] Unexpected error during integrity check: {e}")
        return False


# ==============================================================================
# 2d. ERROR HANDLING AND INPUT VALIDATION
# ==============================================================================
def validate_cli_arguments(args: list) -> tuple:
    if len(args) < 2:
        return False, "No command provided."

    command = args[1].lower()
    script_name = "security_toolkit.py"

    if command in ["encrypt", "decrypt"]:
        if len(args) != 4:
            return False, f"Usage: python {script_name} {command} <input_file> <output_file>"
    elif command == "hash":
        if len(args) != 3:
            return False, f"Usage: python {script_name} hash <file_path>"
    elif command == "verify":
        if len(args) != 4:
            return False, f"Usage: python {script_name} verify <file_path> <expected_sha256>"
    elif command == "test":
        if len(args) != 2:
            return False, f"Usage: python {script_name} test"
    else:
        return False, f"Invalid command '{command}'."

    return True, "Valid"


def test_graceful_error_handling(key: bytes):
    print("\n--- [2d] Testing Graceful Error Handling & Input Validation ---")

    print("\n[*] Test Case 1: Encrypting a non-existent file")
    encrypt_file("missing_file.txt", "output.enc", key)

    print("\n[*] Test Case 2: Decrypting a non-existent file")
    decrypt_file("missing_file.enc", "output.txt", key)

    print("\n[*] Test Case 3: Decrypting using an invalid key")
    wrong_key = Fernet.generate_key()

    temp_src = "temp_test_rec.txt"
    temp_enc = "temp_test_rec.enc"
    temp_out = "temp_test_out.txt"

    with open(temp_src, "w") as f:
        f.write("Test Record")

    encrypt_file(temp_src, temp_enc, key)
    decrypt_file(temp_enc, temp_out, wrong_key)

    for f_path in [temp_src, temp_enc, temp_out]:
        if os.path.exists(f_path):
            os.remove(f_path)

    print("\n[*] Test Case 4: Checking SHA-256 integrity on a missing file")
    detect_file_tampering("ghost_file.txt", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")


def run_full_workflow():
    key = load_or_generate_key()

    if not os.path.exists(SAMPLE_RECORD_FILE):
        with open(SAMPLE_RECORD_FILE, "w") as f:
            f.write("StudentID: 20260001\nName: Jean Paul\nDepartment: Computer Science\nGPA: 3.85\n")
        print(f"[*] Created sample student record at '{SAMPLE_RECORD_FILE}'.")

    baseline_hash = calculate_sha256(SAMPLE_RECORD_FILE)
    print(f"[*] Baseline SHA-256 Hash: {baseline_hash}")

    encrypted_output = "student_record.enc"
    encrypt_file(SAMPLE_RECORD_FILE, encrypted_output, key)

    decrypted_output = "student_record_decrypted.txt"
    decrypt_file(encrypted_output, decrypted_output, key, original_path=SAMPLE_RECORD_FILE)

    detect_file_tampering(SAMPLE_RECORD_FILE, baseline_hash)

    print("\n[*] Simulating unauthorized file modification (tampering)...")
    tampered_file = "tampered_student_record.txt"
    with open(SAMPLE_RECORD_FILE, "r") as src, open(tampered_file, "w") as dst:
        dst.write(src.read() + "GPA Modified: 4.00\n")

    detect_file_tampering(tampered_file, baseline_hash)

    if os.path.exists(tampered_file):
        os.remove(tampered_file)

    test_graceful_error_handling(key)


if __name__ == "__main__":
    # Clean sys.argv from IPyKernel/Google Colab runtime flags (-f)
    clean_args = [arg for arg in sys.argv if not arg.startswith("-f") and not arg.endswith(".json")]

    if len(clean_args) <= 1:
        run_full_workflow()
    else:
        is_valid, msg = validate_cli_arguments(clean_args)
        if not is_valid:
            print(f"[-] CLI Error: {msg}")
            print("\nAvailable Commands:")
            print("  python security_toolkit.py                                   # Run full demonstration")
            print("  python security_toolkit.py encrypt <input_file> <out_file>   # Encrypt file")
            print("  python security_toolkit.py decrypt <input_file> <out_file>   # Decrypt file")
            print("  python security_toolkit.py hash <file_path>                  # Compute SHA-256")
            print("  python security_toolkit.py verify <file_path> <expected_hash># Verify Integrity")
            print("  python security_toolkit.py test                              # Run error handling tests")
            sys.exit(1)

        command = clean_args[1].lower()
        active_key = load_or_generate_key()

        if command == "encrypt":
            encrypt_file(clean_args[2], clean_args[3], active_key)
        elif command == "decrypt":
            decrypt_file(clean_args[2], clean_args[3], active_key)
        elif command == "hash":
            try:
                print(f"SHA-256 ({clean_args[2]}): {calculate_sha256(clean_args[2])}")
            except FileNotFoundError as e:
                print(f"[-] {e}")
        elif command == "verify":
            detect_file_tampering(clean_args[2], clean_args[3])
        elif command == "test":
            test_graceful_error_handling(active_key)
