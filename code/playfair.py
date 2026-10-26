def make_matrix(key):
    key = key.upper().replace("J", "I")
    chars = []

    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in chars:
            chars.append(ch)

    return [chars[i:i+5] for i in range(0, 25, 5)]


def pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def prepare(text):
    text = text.upper().replace("J", "I")
    text = "".join(c for c in text if c.isalpha())
    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 == len(text):
            result += a + "X"
            break

        b = text[i + 1]

        if a == b:
            result += a + "X"
            i += 1
        else:
            result += a + b
            i += 2

    return result


def encrypt(text, matrix):
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = pos(matrix, a)
        r2, c2 = pos(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1+1) % 5]
            result += matrix[r2][(c2+1) % 5]
        elif c1 == c2:
            result += matrix[(r1+1) % 5][c1]
            result += matrix[(r2+1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


def decrypt(text, matrix):
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = pos(matrix, a)
        r2, c2 = pos(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1-1) % 5]
            result += matrix[r2][(c2-1) % 5]
        elif c1 == c2:
            result += matrix[(r1-1) % 5][c1]
            result += matrix[(r2-1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter key: ")
text = input("Enter plaintext: ")

matrix = make_matrix(key)

for row in matrix:
    print(row)

text = prepare(text)
cipher = encrypt(text, matrix)

print("Ciphertext:", cipher)
print("Decrypted:", decrypt(cipher, matrix))


'''
### Algorithm: Playfair Cipher Encryption and Decryption

1. Start the program.
2. Read the key from the user.
3. Convert the key to uppercase, replace `J` with `I`, and remove duplicate letters.
4. Create a \\(5 \times 5\\) key matrix using the key and remaining alphabet letters.
5. Read the plaintext, convert it to uppercase, replace `J` with `I`, and remove spaces and special characters.
6. Divide the plaintext into pairs of letters. Insert `X` between repeated letters in a pair and add `X` if the final letter has no pair.
7. Encrypt each pair using these rules:
   - Same row: Replace each letter with the letter to its right.
   - Same column: Replace each letter with the letter below it.
   - Different row and column: Replace each letter with the letter in the same row and the other letter's column.
8. Display the encrypted ciphertext.
9. Decrypt the ciphertext using the reverse rules:
   - Same row: Move one position to the left.
   - Same column: Move one position upward.
   - Different row and column: Apply the rectangle rule.
10. Display the decrypted text.
11. Stop the program.
'''
