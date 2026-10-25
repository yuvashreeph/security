def encrypt(text, key):
    result = ""
    key = key % 26

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            result += ch

    return result


text = input("Enter plaintext: ")
key = int(input("Enter key: "))

cipher = encrypt(text, key)

print("Encrypted:", cipher)
print("Decrypted:", encrypt(cipher, -key))

print("\nBrute Force:")
for k in range(26):
    print(k, encrypt(cipher, -k))