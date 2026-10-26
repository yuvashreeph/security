def make_matrix(keyword):
    keyword = ''.join(ch for ch in keyword.upper() if ch.isalpha()).replace('J', 'I')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J omitted
    letters = []
    for ch in keyword + alphabet:
        if ch in alphabet and ch not in letters:
            letters.append(ch)
    return [letters[i:i+5] for i in range(0, 25, 5)]

def prepare(text):
    text = ''.join(ch for ch in text.upper() if ch.isalpha()).replace('J', 'I')
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        if i + 1 == len(text):
            b = 'X'
            i += 1
        elif text[i+1] == a:
            b = 'X'
            i += 1            # leave repeated character for next pair
        else:
            b = text[i+1]
            i += 2
        pairs.append(a+b)
    return ''.join(pairs)

def transform(text, matrix, decrypt=False):
    pos = {matrix[r][c]:(r,c) for r in range(5) for c in range(5)}
    out = []
    step = -1 if decrypt else 1
    for i in range(0, len(text), 2):
        a,b = text[i], text[i+1]
        r1,c1 = pos[a]; r2,c2 = pos[b]
        if r1 == r2:             # same row
            out += [matrix[r1][(c1+step)%5], matrix[r2][(c2+step)%5]]
        elif c1 == c2:           # same column
            out += [matrix[(r1+step)%5][c1], matrix[(r2+step)%5][c2]]
        else:                    # rectangle: swap columns
            out += [matrix[r1][c2], matrix[r2][c1]]
    return ''.join(out)

keyword = input("Keyword: ")
message = input("Plaintext: ")
square = make_matrix(keyword)
print("Key matrix:")
for row in square: print(' '.join(row))
prepared = prepare(message)
cipher = transform(prepared, square)
recovered = transform(cipher, square, decrypt=True)
print("Prepared plaintext:", prepared)
print("Ciphertext:", cipher)
print("Decrypted prepared text:", recovered)
