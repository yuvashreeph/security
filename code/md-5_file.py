import hashlib
import os
import json

# 1. Generate MD5 hash
text = input("Enter text: ")
md5_hash = hashlib.md5(text.encode()).hexdigest()

print("\nMD5 Hash:", md5_hash)
print("Length:", len(md5_hash))

# 2. Verify message integrity
old_hash = input("\nEnter previous MD5 hash: ")
new_hash = hashlib.md5(text.encode()).hexdigest()

if old_hash.lower() == new_hash:
    print("Message is not modified")
else:
    print("Message is modified")

# 3. Avalanche effect
text1 = input("\nEnter first string: ")
text2 = input("Enter similar string: ")

h1 = hashlib.md5(text1.encode()).hexdigest()
h2 = hashlib.md5(text2.encode()).hexdigest()

print("Hash 1:", h1)
print("Hash 2:", h2)

b1 = bin(int(h1, 16))[2:].zfill(128)
b2 = bin(int(h2, 16))[2:].zfill(128)

changed = sum(x != y for x, y in zip(b1, b2))
print("Bits changed:", changed, "/ 128")

# 4. File MD5 checksum
path = input("\nEnter file path: ")

if os.path.isfile(path):
    with open(path, "rb") as f:
        data = f.read()

    print("File MD5:", hashlib.md5(data).hexdigest())
else:
    print("File not found")

# 5. Compare hash algorithms
text = input("\nEnter text to compare hashes: ").encode()

print("MD5   :", hashlib.md5(text).hexdigest())
print("SHA-1 :", hashlib.sha1(text).hexdigest())
print("SHA-256:", hashlib.sha256(text).hexdigest())

# 6. File integrity monitoring
db_file = "checksums.json"

if os.path.exists(db_file):
    with open(db_file, "r") as f:
        database = json.load(f)
else:
    database = {}

path = input("\nEnter file path to monitor: ")

if os.path.isfile(path):
    with open(path, "rb") as f:
        current_hash = hashlib.md5(f.read()).hexdigest()

    if path not in database:
        database[path] = current_hash

        with open(db_file, "w") as f:
            json.dump(database, f, indent=2)

        print("Checksum saved successfully")

    elif database[path] == current_hash:
        print("File is UNCHANGED")

    else:
        print("File is MODIFIED")
else:
    print("File not found")

'''

### Algorithm: MD5 Hashing and File Integrity Verification

1. Start the program.
2. Import the `hashlib`, `os`, and `json` modules.
3. Read the text from the user and calculate its MD5 hash.
4. Display the MD5 hash and its length.
5. Read the previous MD5 hash and compare it with the newly calculated hash to check message integrity.
6. Read two similar strings, calculate their MD5 hashes, and display both hashes.
7. Convert the hashes into binary and count the number of bits that differ to demonstrate the avalanche effect.
8. Read a file path and check whether the file exists.
9. If the file exists, calculate and display its MD5 checksum; otherwise, display an error message.
10. Calculate and display the MD5, SHA-1, and SHA-256 hashes of the input text.
11. Load the saved file checksums from `checksums.json`, if available.
12. Calculate the current MD5 checksum of the selected file.
13. If the file is new, save its checksum; otherwise, compare it with the saved checksum to identify whether the file is unchanged or modified.
14. Display the appropriate result.
15. Stop the program.

Note: MD5 is suitable for this educational experiment, but SHA-256 is recommended for security-sensitive integrity verification.

'''
