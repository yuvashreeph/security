import math
import hashlib

# Check whether a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Check RSA parameters
def check_rsa(p, q, e):
    phi = (p - 1) * (q - 1)
    return (is_prime(p) and is_prime(q) and p != q
            and 1 < e < phi and math.gcd(e, phi) == 1)

# Given values
p = 61
q = 53
e = 17
M = 88

if check_rsa(p, q, e):
    # Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)

    print("--- RSA Encryption and Decryption ---")
    print("n =", n)
    print("Phi(n) =", phi)
    print("GCD =", math.gcd(e, phi))

    # Calculate private key d
    d = 1
    while (e * d) % phi != 1:
        d += 1

    print("Public Key:", (e, n))
    print("Private Key:", (d, n))

    # RSA Encryption
    C = pow(M, e, n)
    print("Ciphertext:", C)

    # RSA Decryption
    recovered = pow(C, d, n)
    print("Decrypted Message:", recovered)

    # Calculate MD5 hash of recovered message
    md5_hash = hashlib.md5(
        str(recovered).encode()
    ).hexdigest()
    print("\nMD5 Hash:", md5_hash)

    # Convert hash to a number
    hash_number = int(md5_hash, 16)

    # Sign the hash using RSA private key
    signature = pow(hash_number, d, n)
    print("Digital Signature:", signature)

    # Verify the RSA signature
    verified_hash = pow(signature, e, n)

    if verified_hash == hash_number % n:
        print("RSA Signature: VALID")
    else:
        print("RSA Signature: INVALID")

    # MD5 message integrity verification
    print("\n--- MD5 Hashing and Verification ---")

    message = input("Enter a message: ")
    original_hash = hashlib.md5(
        message.encode()
    ).hexdigest()
    print("Original MD5 Hash:", original_hash)

    check_message = input("Enter message to verify: ")
    check_hash = hashlib.md5(
        check_message.encode()
    ).hexdigest()
    print("Verification MD5 Hash:", check_hash)

    if original_hash == check_hash:
        print("MD5 Verification: Message is unchanged")
    else:
        print("MD5 Verification: Message is modified")

else:
    print("Invalid RSA parameters")

'''
## Algorithm: RSA Digital Signature and MD5 Message Integrity Verification

1. Start the program.
2. Import the required modules for mathematical operations and MD5 hashing.
3. Define a function to check whether a number is prime.
4. Define a function to validate the RSA parameters \\(p\\), \\(q\\), and \\(e\\).
5. Initialize the values \\(p=61\\), \\(q=53\\), \\(e=17\\), and message \\(M=88\\).
6. Check whether the RSA parameters are valid.
7. Calculate \\(n=p\times q\\) and \\(\phi(n)=(p-1)(q-1)\\).
8. Find the private key exponent \\(d\\) such that \\((e\times d)\bmod\phi(n)=1\\).
9. Display the public and private keys.
10. Encrypt the message using \\(C=M^e\bmod n\\) and decrypt it using \\(M=C^d\bmod n\\).
11. Calculate the MD5 hash of the recovered message and convert the hash into a number.
12. Generate a digital signature by encrypting the hash number with the RSA private key.
13. Verify the signature using the RSA public key and display whether it is valid.
14. Read an original message and calculate its MD5 hash.
15. Read the message to be verified and calculate its MD5 hash.
16. Compare both hashes and display whether the message is unchanged or modified.
17. If the RSA parameters are invalid, display an error message.
18. Stop the program.
'''
