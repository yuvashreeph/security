
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
