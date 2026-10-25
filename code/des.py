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