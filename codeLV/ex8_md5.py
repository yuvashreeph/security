import hashlib
import json
from pathlib import Path
RECORD_FILE = "fims_record.json"
def generate_md5():
    text = input("\nEnter text string: ")
    print("MD5 Digest:", hashlib.md5(text.encode()).hexdigest())

def verify_integrity():
    text = input("\nEnter text message: ")
    expected = input("Enter expected MD5 digest: ").strip()
    actual = hashlib.md5(text.encode()).hexdigest()
    print("Matches!" if actual == expected else "Does Not Match!")

def avalanche_effect():
    str1 = input("\nEnter first string: ")
    str2 = input("Enter changed string: ")
    print("Digest 1:", hashlib.md5(str1.encode()).hexdigest())
    print("Digest 2:", hashlib.md5(str2.encode()).hexdigest())

def file_integrity_monitor():
    filename = input("\nEnter file path: ")
    record = json.loads(Path(RECORD_FILE).read_text()) if Path(RECORD_FILE).exists() else {}
    if not Path(filename).exists():
        print("Status: Missing File")
        return
    current_hash = hashlib.md5(Path(filename).read_bytes()).hexdigest()
    print("Current Checksum:", current_hash)
    if filename not in record:
        print("Status: New File")
    elif record[filename] == current_hash:
        print("Status: Not Modified")
    else:
        print("Status: Modified!")
    record[filename] = current_hash
    Path(RECORD_FILE).write_text(json.dumps(record, indent=4))

def compare_algorithms():
    text = input("\nEnter text: ").encode()
    print("MD5:    ", hashlib.md5(text).hexdigest())
    print("SHA-1:  ", hashlib.sha1(text).hexdigest())
    print("SHA-256:", hashlib.sha256(text).hexdigest())

while True:
    print("\n--- MENU ---")
    print("1. Generate MD5\n2. Verify Integrity\n3. Avalanche Effect\n4. FIMS File Check\n5. Compare Hashes\n6. Exit")
    choice = input("Choice (1-6): ").strip()
    if choice == "1": generate_md5()
    elif choice == "2": verify_integrity()
    elif choice == "3": avalanche_effect()
    elif choice == "4": file_integrity_monitor()
    elif choice == "5": compare_algorithms()
    elif choice == "6": break
    else: print("Invalid choice.")