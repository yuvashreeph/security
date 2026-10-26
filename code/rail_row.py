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


'''
### Algorithm: Columnar Transposition Cipher Encryption and Decryption

1. Start the program.
2. Read the plaintext and number of columns from the user.
3. Convert the plaintext to uppercase and remove spaces.
4. Calculate the number of rows required to store the plaintext.
5. Create a matrix and fill empty positions with `X`.
6. Fill the matrix column by column using the plaintext.
7. Read the matrix row by row to generate the ciphertext.
8. Display the encrypted ciphertext.
9. Create a new matrix and fill it row by row using the ciphertext.
10. Read the new matrix column by column to recover the plaintext.
11. Remove trailing `X` characters and display the decrypted text.
12. Stop the program.
'''
