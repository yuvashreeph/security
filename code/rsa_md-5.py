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

# Check RSA validity
def check_rsa(p, q, e):
    phi = (p - 1) * (q - 1)
    return (is_prime(p) and is_prime(q) and p != q
            and 1 < e < phi and math.gcd(e, phi) == 1)

# Given values
p = 61
q = 53
e = 17
M = 88

if not check_rsa(p, q, e):
    print("Invalid RSA parameters")
else:
    # Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)

    print("n =", n)
    print("Phi(n) =", phi)
    print("GCD =", math.gcd(e, phi))

    # Calculate private key
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

# MD5 calculation and verification
print("\n--- MD5 Hashing and Verification ---")

message = input("Enter a message: ")

# Calculate original MD5 hash
original_hash = hashlib.md5(message.encode()).hexdigest()
print("Original MD5 Hash:", original_hash)

# Verify the same message
check_message = input("Enter message to verify: ")
check_hash = hashlib.md5(check_message.encode()).hexdigest()

print("Verification MD5 Hash:", check_hash)

if original_hash == check_hash:
    print("MD5 Verification: Message is unchanged")
else:
    print("MD5 Verification: Message is modified")