
import hashlib

# Public values
p = 23
g = 5

# Private keys
a = 6
b = 15

# Calculate public keys
KA = pow(g, a, p)
KB = pow(g, b, p)

print("Public Key of A:", KA)
print("Public Key of B:", KB)

# Calculate shared secret key
keyA = pow(KB, a, p)
keyB = pow(KA, b, p)

print("Shared Key of A:", keyA)
print("Shared Key of B:", keyB)

if keyA == keyB:
    print("Shared Key Matched")

    # Convert shared key to string
    key_string = str(keyA)
    print("Shared Key String:", key_string)

    # MD5 hash
    md5_hash = hashlib.md5(key_string.encode()).hexdigest()
    print("MD5 Hash:", md5_hash)

    # SHA-256 hash
    sha_hash = hashlib.sha256(key_string.encode()).hexdigest()
    print("SHA-256 Hash:", sha_hash)
else:
    print("Shared Key Not Matched")
