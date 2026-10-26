import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

n = p * q
phi = (p - 1) * (q - 1)

for e in range(2, phi):
    if gcd(e, phi) == 1:
        break

d = mod_inverse(e, phi)

print("\nPublic Key:", (e, n))
print("Private Key:", (d, n))

message = int(input("\nEnter message as an integer: "))

if message >= n:
    print("Message must be smaller than n.")
    exit()

# Encryption
ciphertext = pow(message, e, n)
print("Encrypted message:", ciphertext)

# Decryption
decrypted = pow(ciphertext, d, n)
print("Decrypted message:", decrypted)


'''
## Algorithm: RSA Encryption and Decryption

1. Start the program.
2. Define a function to calculate the GCD of two numbers.
3. Define a function to find the modular inverse of `e` with respect to \\(\phi\\).
4. Read two prime numbers, `p` and `q`, from the user.
5. Calculate \\(n = p \times q\\).
6. Calculate \\(\phi(n) = (p-1)(q-1)\\).
7. Find a public exponent `e` such that \\(\gcd(e,\phi(n)) = 1\\).
8. Calculate the private exponent `d` such that \\((d \times e) \bmod \phi(n) = 1\\).
9. Display the public key \\((e,n)\\) and private key \\((d,n)\\).
10. Read the message as an integer and check that it is smaller than `n`.
11. Encrypt the message using \\(C = M^e \bmod n\\).
12. Decrypt the ciphertext using \\(M = C^d \bmod n\\).
13. Display the encrypted and decrypted messages.
14. Stop the program.
'''
