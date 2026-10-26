p = int(input("Enter prime number p: "))
g = int(input("Enter primitive root g: "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

A = pow(g, a, p)
B = pow(g, b, p)

secret_alice = pow(B, a, p)
secret_bob = pow(A, b, p)

print("\nAlice's public key:", A)
print("Bob's public key:", B)
print("Shared secret calculated by Alice:", secret_alice)
print("Shared secret calculated by Bob:", secret_bob)
print("Keys match:", secret_alice == secret_bob)