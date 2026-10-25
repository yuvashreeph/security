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