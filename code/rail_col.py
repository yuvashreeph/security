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


'''
### Algorithm: Transposition Cipher Encryption and Decryption

1. Start the program.
2. Read the plaintext and number of columns from the user.
3. Convert the plaintext to uppercase and remove spaces.
4. Calculate the number of rows required to store the plaintext.
5. Create a matrix with the specified number of rows and columns, filling empty positions with `X`.
6. Fill the matrix row by row using the plaintext.
7. Read the matrix column by column to generate the ciphertext.
8. Display the encrypted ciphertext.
9. Create an empty matrix for decryption.
10. Fill the matrix column by column using the ciphertext.
11. Read the matrix row by row to recover the plaintext.
12. Remove trailing `X` characters and display the decrypted text.
13. Stop the program.
'''
