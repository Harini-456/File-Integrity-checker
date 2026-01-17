import hashlib
import os
import json

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()


def create_baseline(folder):
    baseline = {}

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            baseline[path] = calculate_hash(path)

    with open("baseline.json", "w") as f:
        json.dump(baseline, f, indent=4)

    print("[+] Baseline created successfully.")

def check_integrity(folder):
    with open("baseline.json", "r") as f:
        baseline = json.load(f)

    current_files = {}

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            current_files[path] = calculate_hash(path)

    # Check for modified or deleted files
    for file in baseline:
        if file not in current_files:
            print(f"[DELETED] {file}")
        elif baseline[file] != current_files[file]:
            print(f"[MODIFIED] {file}")

    # Check for new files
    for file in current_files:
        if file not in baseline:
            print(f"[NEW FILE] {file}")

def main():
    folder_to_monitor = "monitored folder"

    print("1. Create Baseline")
    print("2. Check Integrity")

    choice = input("Enter choice: ")

    if choice == "1":
        create_baseline(folder_to_monitor)
    elif choice == "2":
        check_integrity(folder_to_monitor)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
