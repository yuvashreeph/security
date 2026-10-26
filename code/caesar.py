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

'''
### Algorithm: Caesar Cipher Encryption, Decryption and Brute Force

1. Start the program.
2. Define an encryption function that accepts the plaintext and key.
3. Initialize an empty string to store the result and calculate the key modulo 26.
4. Read the plaintext and key from the user.
5. Encrypt the plaintext by shifting each alphabet forward by the key, preserving uppercase and lowercase letters.
6. Display the encrypted text.
7. Decrypt the ciphertext by shifting the letters backward using the negative key.
8. Display the decrypted text.
9. Perform brute force by trying all 26 possible keys from 0 to 25.
10. Display the decrypted text for each key.
11. Stop the program.
'''
