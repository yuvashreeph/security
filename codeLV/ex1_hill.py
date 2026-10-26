from math import gcd

def inverse_mod(a, m=26):
    a %= m
    for x in range(1, m):
        if (a*x) % m == 1:
            return x
    raise ValueError("Determinant has no inverse modulo 26; choose another key.")

def hill(text, key, decrypt=False):
    text = ''.join(c for c in text.upper() if c.isalpha())
    text = text.replace('J','I')
    if len(text) % 2: text += 'X'
    a,b = key[0]
    c,d = key[1]
    det = (a*d - b*c) % 26
    if gcd(det, 26) != 1:
        raise ValueError("Key matrix must have determinant coprime to 26.")
    if decrypt:
        invdet = inverse_mod(det)
        # inverse = inv(det) * [[d,-b],[-c,a]] mod 26
        key = [[invdet*d % 26, invdet*(-b) % 26],
               [invdet*(-c) % 26, invdet*a % 26]]
    out = []
    for i in range(0, len(text), 2):
        x,y = ord(text[i])-65, ord(text[i+1])-65
        out.extend([(key[0][0]*x + key[0][1]*y) % 26,
                    (key[1][0]*x + key[1][1]*y) % 26])
    return ''.join(chr(n+65) for n in out)

key = []
print("Enter 2x2 key matrix values (integers):")
for i in range(2):
    key.append([int(x) for x in input(f"Row {i+1}, two values separated by space: ").split()])
message = input("Plaintext: ")
cipher = hill(message, key)
plain = hill(cipher, key, decrypt=True)
print("Ciphertext:", cipher)
print("Decrypted (padded/cleaned input):", plain)
