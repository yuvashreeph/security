def caesar(text, shift):
    result = []
    shift %= 26
    for ch in text:
        if 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        elif 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(ch)
    return ''.join(result)

message = input("Enter message: ")
key = int(input("Enter shift key: "))
cipher = caesar(message, key)
plain = caesar(cipher, -key)
print("Plaintext :", message)
print("Ciphertext:", cipher)
print("Decrypted :", plain)
