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