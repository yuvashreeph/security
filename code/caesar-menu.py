
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
