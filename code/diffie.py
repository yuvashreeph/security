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