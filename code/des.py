from Crypto.Cipher import DES, DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

text = input("Enter plaintext: ").encode() 

print("\n1. DES - ECB")
print("2. DES - CBC")
print("3. DES - CFB")
print("4. DES - OFB")
print("5. DES - CTR")
print("6. Triple DES - CBC")

choice = int(input("Choose mode: "))

if choice in [1, 2, 3, 4, 5]:
    key = input("Enter 8-byte DES key: ").encode()

    if len(key) != 8:
        print("Key must be exactly 8 bytes")
        exit()

    if choice == 1:
        cipher = DES.new(key, DES.MODE_ECB)
        encrypted = cipher.encrypt(pad(text, 8))

        decrypted = unpad(
            DES.new(key, DES.MODE_ECB).decrypt(encrypted), 8
        )

    elif choice == 2:
        iv = get_random_bytes(8)
        cipher = DES.new(key, DES.MODE_CBC, iv=iv)
        encrypted = cipher.encrypt(pad(text, 8))

        decrypted = unpad(
            DES.new(key, DES.MODE_CBC, iv=iv).decrypt(encrypted), 8
        )

        print("IV:", iv.hex())

    elif choice == 3:
        iv = get_random_bytes(8)
        cipher = DES.new(key, DES.MODE_CFB, iv=iv)
        encrypted = cipher.encrypt(text)

        decrypted = DES.new(
            key, DES.MODE_CFB, iv=iv
        ).decrypt(encrypted)

        print("IV:", iv.hex())

    elif choice == 4:
        iv = get_random_bytes(8)
        cipher = DES.new(key, DES.MODE_OFB, iv=iv)
        encrypted = cipher.encrypt(text)

        decrypted = DES.new(
            key, DES.MODE_OFB, iv=iv
        ).decrypt(encrypted)

        print("IV:", iv.hex())

    elif choice == 5:
        nonce = get_random_bytes(4)
        cipher = DES.new(key, DES.MODE_CTR, nonce=nonce)
        encrypted = cipher.encrypt(text)

        decrypted = DES.new(
            key, DES.MODE_CTR, nonce=nonce
        ).decrypt(encrypted)

        print("Nonce:", nonce.hex())

elif choice == 6:
    key = DES3.adjust_key_parity(get_random_bytes(24))
    iv = get_random_bytes(8)

    cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)
    encrypted = cipher.encrypt(pad(text, 8))

    decrypted = unpad(
        DES3.new(key, DES3.MODE_CBC, iv=iv).decrypt(encrypted), 8
    )

    print("Triple DES key:", key.hex())
    print("IV:", iv.hex())

else:
    print("Invalid choice")
    exit()

print("\nCiphertext:", encrypted.hex())
print("Decrypted text:", decrypted.decode())


'''

## Algorithm: DES and Triple DES Encryption and Decryption

1. Start the program.
2. Import the DES and Triple DES modules, padding functions, and random byte generator.
3. Read the plaintext from the user.
4. Display the available encryption modes: DES-ECB, DES-CBC, DES-CFB, DES-OFB, DES-CTR, and Triple DES-CBC.
5. Read the user's choice.
6. If the choice is between 1 and 5:
   - Read the DES key from the user.
   - Check whether the key is exactly 8 bytes long.
   - Generate a random IV or nonce for the selected mode, if required.
   - Create the DES cipher using the selected mode.
   - Apply padding for ECB and CBC modes.
   - Encrypt the plaintext.
   - Decrypt the ciphertext using the same key, mode, and IV or nonce.
   - Remove padding where required.
7. If the choice is 6:
   - Generate a random Triple DES key and adjust its parity.
   - Generate a random IV.
   - Create the Triple DES cipher using CBC mode.
   - Pad and encrypt the plaintext.
   - Decrypt the ciphertext and remove the padding.
8. If the choice is invalid, display an error message and stop.
9. Display the ciphertext in hexadecimal format.
10. Display the decrypted plaintext.
11. Stop the program.

'''
