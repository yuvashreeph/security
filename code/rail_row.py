import math

text = input("Enter plaintext: ").replace(" ", "").upper()
cols = int(input("Enter columns: "))

rows = math.ceil(len(text) / cols)
matrix = [['X'] * cols for _ in range(rows)]
k = 0

# Fill column-wise
for c in range(cols):
    for r in range(rows):
        if k < len(text):
            matrix[r][c] = text[k]
            k += 1

# Read row-wise
cipher = ""

for r in range(rows):
    for c in range(cols):
        cipher += matrix[r][c]

print("Ciphertext:", cipher)

# Decryption
matrix2 = [[''] * cols for _ in range(rows)]
k = 0

for r in range(rows):
    for c in range(cols):
        matrix2[r][c] = cipher[k]
        k += 1

plain = ""

for c in range(cols):
    for r in range(rows):
        plain += matrix2[r][c]

print("Decrypted:", plain.rstrip('X'))