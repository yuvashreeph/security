import numpy as np

def encrypt(text, key):
    text = text.upper().replace(" ", "")

    while len(text) % 3 != 0:
        text += "X"

    cipher = ""

    for i in range(0, len(text), 3):
        block = [ord(c) - ord('A') for c in text[i:i+3]]

        for row in range(3):
            value = sum(
                key[row][col] * block[col]
                for col in range(3)
            ) % 26

            cipher += chr(value + ord('A'))

    return cipher


def decrypt(cipher, key):
    det = int(round(np.linalg.det(key))) % 26

    inv_det = next(
        (i for i in range(1, 26) if (det*i) % 26 == 1),
        None
    )

    if inv_det is None:
        return "Invalid key"

    adj = np.round(
        np.linalg.inv(key) * np.linalg.det(key)
    ).astype(int)

    inv_key = (inv_det * adj) % 26
    text = ""

    for i in range(0, len(cipher), 3):
        block = [ord(c) - ord('A') for c in cipher[i:i+3]]

        for row in range(3):
            value = sum(
                inv_key[row][col] * block[col]
                for col in range(3)
            ) % 26

            text += chr(int(value) + ord('A'))

    return text


key = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

text = input("Enter plaintext: ")

cipher = encrypt(text, key)

print("Encrypted text:", cipher)
print("Decrypted text:", decrypt(cipher, key))


'''
### Algorithm: Hill Cipher (3 × 3 Matrix)

1. Start the program.
2. Import the NumPy library.
3. Define the encryption and decryption functions.
4. Read the plaintext and convert it to uppercase, removing spaces.
5. If the plaintext length is not divisible by 3, add `X` until it is divisible by 3.
6. Divide the plaintext into blocks of three letters.
7. Convert each letter into a number from 0 to 25.
8. Multiply each block by the key matrix modulo 26 to generate the ciphertext.
9. Display the encrypted text.
10. Calculate the determinant of the key matrix and find its modular inverse.
11. Calculate the inverse key matrix modulo 26. If the key is invalid, display an error message.
12. Divide the ciphertext into blocks of three letters and multiply each block by the inverse key matrix modulo 26.
13. Convert the resulting numbers back into letters and display the decrypted text.
14. Stop the program.
'''
