import math

text = input("Enter plaintext: ").replace(" ", "").upper()
cols = int(input("Enter columns: "))

rows = math.ceil(len(text) / cols)
matrix = [['X'] * cols for _ in range(rows)]
k = 0

# Fill row-wise
for r in range(rows):
    for c in range(cols):
        if k < len(text):
            matrix[r][c] = text[k]
            k += 1

# Read column-wise
cipher = ""

for c in range(cols):
    for r in range(rows):
        cipher += matrix[r][c]

print("Ciphertext:", cipher)

# Decryption
matrix2 = [[''] * cols for _ in range(rows)]
k = 0

for c in range(cols):
    for r in range(rows):
        matrix2[r][c] = cipher[k]
        k += 1

plain = ""

for r in range(rows):
    for c in range(cols):
        plain += matrix2[r][c]

print("Decrypted:", plain.rstrip('X'))