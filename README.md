# File Integrity Checker

This project is a Python-based File Integrity Checker used to monitor changes in files by calculating and comparing cryptographic hash values (SHA-256).

## Features
- Detects file modifications
- Detects new file additions
- Detects file deletions
- Uses SHA-256 hashing

## How It Works
1. Create a baseline by generating hash values for all files.
2. Store hashes securely in a baseline file.
3. Recalculate hashes and compare with the baseline to detect changes.

## Technologies Used
- Python
- hashlib
- os
- json

## Usage
Run the script and choose:
- Option 1: Create Baseline
- Option 2: Check Integrity
