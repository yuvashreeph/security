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