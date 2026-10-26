
import math
import hashlib
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Check RSA validity
def check_rsa(p, q, e):
    phi = (p - 1) * (q - 1)
    return (is_prime(p) and is_prime(q) and p != q
            and 1 < e < phi and math.gcd(e, phi) == 1)

# Given RSA values
p = 61
q = 53
e = 17
M = 88

if check_rsa(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)

    print("--- RSA Encryption and Decryption ---")
    print("n =", n)
    print("Phi(n) =", phi)
    print("GCD =", math.gcd(e, phi))

    # Calculate private exponent
    d = 1
    while (e * d) % phi != 1:
        d += 1

    print("RSA Public Key:", (e, n))
    print("RSA Private Key:", (d, n))

    # Encrypt and decrypt
    C = pow(M, e, n)
    print("Ciphertext:", C)

    recovered = pow(C, d, n)
    print("Decrypted Message:", recovered)

    # SHA-256 hash of recovered message
    sha_hash = hashlib.sha256(str(recovered).encode()).hexdigest()
    print("\nSHA-256 Hash:", sha_hash)

    # Convert hash into a number
    hash_number = int(sha_hash, 16)
    print("Hash Number:", hash_number)

    # RSA signature using private key
    signature = pow(hash_number, d, n)
    print("RSA Digital Signature:", signature)

    # Verify RSA signature using public key
    verified_hash = pow(signature, e, n)

    if verified_hash == hash_number % n:
        print("RSA Signature: VALID")
    else:
        print("RSA Signature: INVALID")

else:
    print("Invalid RSA parameters")

# DSS digital signature using SHA-256
print("\n--- DSS Digital Signature using SHA-256 ---")

# Generate DSA key pair
key = DSA.generate(2048)
public_key = key.publickey()

message = input("Enter message to sign: ")

# Calculate SHA-256 hash
hash_value = SHA256.new(message.encode())
print("SHA-256 Hash:", hash_value.hexdigest())

# Sign using DSA private key
signer = DSS.new(key, 'fips-186-3')
dss_signature = signer.sign(hash_value)
print("DSS Signature:", dss_signature.hex())

# Verify using DSA public key
verifier = DSS.new(public_key, 'fips-186-3')

try:
    verifier.verify(SHA256.new(message.encode()), dss_signature)
    print("DSS Verification: Signature VALID")
except ValueError:
    print("DSS Verification: Signature INVALID")

# Verify a modified message
modified = input("Enter message to verify: ")

try:
    verifier.verify(SHA256.new(modified.encode()), dss_signature)
    print("Modified Message: Signature VALID")
except ValueError:
    print("Modified Message: Signature INVALID")

'''
### Algorithm: RSA and DSS Digital Signature using SHA-256

1. Start the program.
2. Import the required modules for RSA, DSA, SHA-256 hashing, and digital signatures.
3. Define functions to check prime numbers and validate RSA parameters.
4. Initialize the RSA values \\(p\\), \\(q\\), \\(e\\), and message \\(M\\).
5. Calculate \\(n = p \times q\\) and \\(\phi(n) = (p-1)(q-1)\\).
6. Calculate the private exponent \\(d\\) such that \\((e \times d) \bmod \phi(n) = 1\\).
7. Encrypt the message using the RSA public key and decrypt it using the private key.
8. Calculate the SHA-256 hash of the decrypted message and convert it into a number.
9. Generate an RSA digital signature using the private key and verify it using the public key.
10. Generate a DSA key pair and read a message from the user.
11. Calculate the SHA-256 hash of the message and sign it using the DSA private key.
12. Verify the DSA signature using the public key and display whether it is valid.
13. Read a modified message and verify its signature to detect message changes.
14. Display the verification result for the modified message.
15. Stop the program.

Note: The RSA signature portion is a simplified educational demonstration and is not secure for real-world use.

'''
