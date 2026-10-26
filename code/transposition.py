import math

def show(m):
    for row in m:
        print(" ".join(row))

# Type A: Fill column-wise, read row-wise
def enc_A(pt, cols):
    pt = pt.replace(" ", "").upper()
    rows = math.ceil(len(pt) / cols)

    m = [['X'] * cols for _ in range(rows)]
    k = 0

    for c in range(cols):
        for r in range(rows):
            if k < len(pt):
                m[r][c] = pt[k]
                k += 1

    print("Grid:")
    show(m)

    return "".join("".join(row) for row in m)


def dec_A(ct, cols):
    rows = len(ct) // cols
    m = [
        list(ct[r * cols:(r + 1) * cols])
        for r in range(rows)
    ]

    return "".join(
        m[r][c] for c in range(cols) for r in range(rows)
    ).rstrip('X')


# Type B: Fill row-wise, read column-wise
def enc_B(pt, cols):
    pt = pt.replace(" ", "").upper()

    while len(pt) % cols != 0:
        pt += 'X'

    print("Padded plaintext:", pt)

    rows = len(pt) // cols
    m = [
        list(pt[r * cols:(r + 1) * cols])
        for r in range(rows)
    ]

    print("Grid:")
    show(m)

    return "".join(
        m[r][c] for c in range(cols) for r in range(rows)
    )


def dec_B(ct, cols):
    rows = len(ct) // cols
    m = [[''] * cols for _ in range(rows)]
    k = 0

    for c in range(cols):
        for r in range(rows):
            m[r][c] = ct[k]
            k += 1

    return "".join("".join(row) for row in m)


text = input("Enter plaintext: ")
cols = int(input("Enter number of columns: "))

cipher_A = enc_A(text, cols)
print("Type A Ciphertext:", cipher_A)
print("Type A Decrypted:", dec_A(cipher_A, cols))

cipher_B = enc_B(text, cols)
print("Type B Ciphertext:", cipher_B)
print("Type B Decrypted:", dec_B(cipher_B, cols))


'''

## Algorithm: Columnar Transposition Cipher (Type A and Type B)

1. Start the program and import the `math` module.
2. Read the plaintext and the number of columns from the user.
3. Remove spaces from the plaintext and convert it to uppercase.
4. Type A Encryption:
   - Calculate the number of rows required.
   - Create a grid filled with `X`.
   - Fill the grid column-wise with the plaintext.
   - Read the grid row-wise to generate the ciphertext.
5. Type A Decryption:
   - Arrange the ciphertext row-wise into a grid.
   - Read the grid column-wise to recover the plaintext.
   - Remove trailing `X` characters.
6. Display the Type A ciphertext and decrypted message.
7. Type B Encryption:
   - Add `X` characters until the plaintext length is divisible by the number of columns.
   - Fill the grid row-wise with the padded plaintext.
   - Read the grid column-wise to generate the ciphertext.
8. Type B Decryption:
   - Create an empty grid with the required rows and columns.
   - Fill the grid column-wise using the ciphertext.
   - Read the grid row-wise to recover the plaintext.
9. Display the Type B ciphertext and decrypted message.
10. Stop the program.
'''
