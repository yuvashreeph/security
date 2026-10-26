p = int(input("Enter prime p: "))
g = int(input("Enter primitive root g: "))

a = int(input("Enter Alice private key: "))
b = int(input("Enter Bob private key: "))

# Calculate public keys
A = pow(g, a, p)
B = pow(g, b, p)

# Calculate shared keys
KA = pow(B, a, p)
KB = pow(A, b, p)

print("Alice public key:", A)
print("Bob public key:", B)

print("Alice shared key:", KA)
print("Bob shared key:", KB)

if KA == KB:
    print("Shared key is same")
else:
    print("Error")


'''
### Algorithm: Diffie–Hellman Key Exchange

1. Start the program.
2. Read the prime number \\(p\\) and primitive root \\(g\\).
3. Read Alice's private key \\(a\\) and Bob's private key \\(b\\).
4. Calculate Alice's public key using \\(A = g^a \bmod p\\).
5. Calculate Bob's public key using \\(B = g^b \bmod p\\).
6. Calculate Alice's shared key using \\(K_A = B^a \bmod p\\).
7. Calculate Bob's shared key using \\(K_B = A^b \bmod p\\).
8. Display both public keys and shared keys.
9. Compare the shared keys. If they are equal, display "Shared key is same"; otherwise, display "Error".
10. Stop the program.
'''
