
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


while True:
    print("\n--- Caesar Cipher ---")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Brute Force")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter plaintext: ")
        key = int(input("Enter key: "))
        print("Encrypted:", encrypt(text, key))

    elif choice == "2":
        text = input("Enter ciphertext: ")
        key = int(input("Enter key: "))
        print("Decrypted:", encrypt(text, -key))

    elif choice == "3":
        text = input("Enter ciphertext: ")

        for k in range(26):
            print(k, ":", encrypt(text, -k))

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")


'''
### Algorithm: Caesar Cipher

1. Start the program.
2. Define an encryption function that accepts the text and key.
3. Read the user's choice from the menu: Encryption, Decryption, Brute Force, or Exit.
4. For Encryption:
   - Read the plaintext and key.
   - Shift each alphabet by the given key and preserve uppercase and lowercase letters.
   - Keep spaces, numbers, and special characters unchanged.
   - Display the encrypted text.
5. For Decryption:
   - Read the ciphertext and key.
   - Shift each alphabet backward by the key.
   - Display the decrypted text.
6. For Brute Force:
   - Read the ciphertext.
   - Try all 26 possible keys from 0 to 25.
   - Display the decrypted text for each key.
7. If the user selects Exit, terminate the program.
8. If the choice is invalid, display an error message.
9. Repeat the menu until the user selects Exit.
10. Stop.
'''
