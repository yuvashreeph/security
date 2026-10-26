def inverse_key(k):
    a, b = k[0]
    c, d = k[1]

    det = (a*d - b*c) % 26

    for x in range(26):
        if (det*x) % 26 == 1:
            inv = x
            break
    else:
        return None

    return [
        [(d*inv) % 26, (-b*inv) % 26],
        [(-c*inv) % 26, (a*inv) % 26]
    ]


def process(text):
    text = text.upper().replace(" ", "")

    if len(text) % 2:
        text += "X"

    return text


def encrypt(text, key):
    result = ""

    for i in range(0, len(text), 2):
        p1 = ord(text[i]) - 65
        p2 = ord(text[i+1]) - 65

        c1 = (key[0][0]*p1 + key[0][1]*p2) % 26
        c2 = (key[1][0]*p1 + key[1][1]*p2) % 26

        result += chr(c1+65)
        result += chr(c2+65)

    return result


def decrypt(text, key):
    result = ""

    for i in range(0, len(text), 2):
        c1 = ord(text[i]) - 65
        c2 = ord(text[i+1]) - 65

        p1 = (key[0][0]*c1 + key[0][1]*c2) % 26
        p2 = (key[1][0]*c1 + key[1][1]*c2) % 26

        result += chr(p1+65)
        result += chr(p2+65)

    return result


key = [
    list(map(int, input("Row 1: ").split())),
    list(map(int, input("Row 2: ").split()))
]

text = process(input("Enter plaintext: "))
inv = inverse_key(key)

if inv is None:
    print("Key is not invertible")
else:
    cipher = encrypt(text, key)
    print("Ciphertext:", cipher)
    print("Decrypted:", decrypt(cipher, inv))


'''
### Algorithm: Hill Cipher Encryption and Decryption

1. Start the program.
2. Define a function to calculate the inverse of the \\(2 \times 2\\) key matrix modulo 26.
3. Read the key matrix from the user.
4. Read the plaintext, convert it to uppercase, and remove spaces.
5. If the plaintext length is odd, add the letter `X` at the end.
6. Calculate the determinant of the key matrix and find its modular inverse.
7. If the key matrix is not invertible, display an error message and stop.
8. Divide the plaintext into pairs of letters.
9. Convert each pair into numbers and multiply it by the key matrix modulo 26 to obtain the ciphertext.
10. Display the encrypted ciphertext.
11. Decrypt the ciphertext using the inverse key matrix modulo 26.
12. Display the decrypted plaintext.
13. Stop the program.
'''
