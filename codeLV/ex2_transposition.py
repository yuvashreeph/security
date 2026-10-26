import math

def create_matrix(text, cols):
    text = text.upper().replace(" ", "")
    orig_len = len(text)
    rows = math.ceil(orig_len / cols)
    padded_text = text.ljust(rows * cols, 'X')
    mat = [['X' for _ in range(cols)] for _ in range(rows)]
    return padded_text, mat, orig_len, rows

def display(mat):
    for row in mat:
        print(" ".join(row))

def row_encrypt(text, cols):
    text, mat, orig_len, rows = create_matrix(text, cols)
    k = 0
    for c in range(cols):
        for r in range(rows):
            mat[r][c] = text[k]
            k += 1
    cipher = ""
    for r in range(rows):
        for c in range(cols):
            cipher += mat[r][c]    
    return cipher, mat, orig_len

def row_decrypt(cipher, cols, orig_len):
    rows = len(cipher) // cols
    mat = [['X' for _ in range(cols)] for _ in range(rows)]
    k = 0
    for r in range(rows):
        for c in range(cols):
            mat[r][c] = cipher[k]
            k += 1
    text = ""
    for c in range(cols):
        for r in range(rows):
            text += mat[r][c]
            
    return text[:orig_len]

def column_encrypt(text, cols):
    text, mat, orig_len, rows = create_matrix(text, cols)
    k = 0
    for r in range(rows):
        for c in range(cols):
            mat[r][c] = text[k]
            k += 1
    cipher = ""
    for c in range(cols):
        for r in range(rows):
            cipher += mat[r][c]      
    return cipher, mat, orig_len

def column_decrypt(cipher, cols, orig_len):
    rows = len(cipher) // cols
    mat = [['X' for _ in range(cols)] for _ in range(rows)]
    k = 0
    for c in range(cols):
        for r in range(rows):
            mat[r][c] = cipher[k]
            k += 1
    text = ""
    for r in range(rows):
        for c in range(cols):
            text += mat[r][c]   
    return text[:orig_len]

plain = input("Enter plaintext: ")
cols = int(input("Enter number of columns: "))

# Run Row Major
rc, rmat, r_len = row_encrypt(plain, cols)
print("\n--- Row Major ---")
print("Matrix:")
display(rmat)
print("Ciphertext:", rc)
print("Decrypted :", row_decrypt(rc, cols, r_len))

# Run Column Major
cc, cmat, c_len = column_encrypt(plain, cols)
print("\n--- Column Major ---")
print("Matrix:")
display(cmat)
print("Ciphertext:", cc)
print("Decrypted :", column_decrypt(cc, cols, c_len))