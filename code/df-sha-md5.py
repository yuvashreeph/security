
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


'''
### Algorithm: Diffie–Hellman Key Exchange with MD5 and SHA-256

1. Start the program.
2. Import the `hashlib` module.
3. Initialize the public values \\(p\\) and \\(g\\), and the private keys of users A and B.
4. Calculate the public key of A using \\(K_A = g^a \bmod p\\).
5. Calculate the public key of B using \\(K_B = g^b \bmod p\\).
6. Calculate the shared secret key for A using \\(K_A^{shared} = K_B^a \bmod p\\).
7. Calculate the shared secret key for B using \\(K_B^{shared} = K_A^b \bmod p\\).
8. Compare both shared keys. If they match, display a success message.
9. Convert the shared key into a string.
10. Calculate and display the MD5 hash of the shared key string.
11. Calculate and display the SHA-256 hash of the shared key string.
12. If the shared keys do not match, display an error message.
13. Stop the program.
'''
