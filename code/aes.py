from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = input("Enter key (16/24/32 characters): ").encode()
text = input("Enter plaintext: ").encode()

if len(key) not in (16, 24, 32):
    print("Key must be 16, 24, or 32 bytes")
    exit()

# 1. AES - ECB
cipher = AES.new(key, AES.MODE_ECB)
encrypted = cipher.encrypt(pad(text, 16))

decrypted = unpad(
    AES.new(key, AES.MODE_ECB).decrypt(encrypted), 16
)

print("\nECB Ciphertext:", encrypted.hex())
print("ECB Decrypted:", decrypted.decode())

# 2. AES - CBC
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
encrypted = cipher.encrypt(pad(text, 16))

decrypted = unpad(
    AES.new(key, AES.MODE_CBC, iv=iv).decrypt(encrypted), 16
)

print("\nCBC Ciphertext:", encrypted.hex())
print("CBC Decrypted:", decrypted.decode())

# 3. AES - CFB
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CFB, iv=iv)
encrypted = cipher.encrypt(text)

decrypted = AES.new(
    key, AES.MODE_CFB, iv=iv
).decrypt(encrypted)

print("\nCFB Ciphertext:", encrypted.hex())
print("CFB Decrypted:", decrypted.decode())

# 4. AES - OFB
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_OFB, iv=iv)
encrypted = cipher.encrypt(text)

decrypted = AES.new(
    key, AES.MODE_OFB, iv=iv
).decrypt(encrypted)

print("\nOFB Ciphertext:", encrypted.hex())
print("OFB Decrypted:", decrypted.decode())

# 5. AES - CTR
nonce = get_random_bytes(8)
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
encrypted = cipher.encrypt(text)

decrypted = AES.new(
    key, AES.MODE_CTR, nonce=nonce
).decrypt(encrypted)

print("\nCTR Ciphertext:", encrypted.hex())
print("CTR Decrypted:", decrypted.decode())

# 6. AES - GCM
nonce = get_random_bytes(12)
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
encrypted, tag = cipher.encrypt_and_digest(text)

cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
decrypted = cipher.decrypt_and_verify(encrypted, tag)

print("\nGCM Ciphertext:", encrypted.hex())
print("GCM Tag:", tag.hex())
print("GCM Decrypted:", decrypted.decode())


'''
### Algorithm: AES Encryption and Decryption

1. Start the program.
2. Import the AES module, padding functions, and random byte generator.
3. Read the AES key and plaintext from the user.
4. Check whether the key length is 16, 24, or 32 bytes. If invalid, display an error and stop.
5. Create an AES cipher using ECB mode. Pad the plaintext, encrypt it, decrypt the ciphertext, and remove the padding.
6. Create an AES cipher using CBC mode with a random IV. Encrypt and decrypt the padded plaintext.
7. Create an AES cipher using CFB mode with a random IV. Encrypt and decrypt the plaintext without padding.
8. Create an AES cipher using OFB mode with a random IV. Encrypt and decrypt the plaintext without padding.
9. Create an AES cipher using CTR mode with a random nonce. Encrypt and decrypt the plaintext without padding.
10. Create an AES cipher using GCM mode with a random nonce. Encrypt the plaintext and generate an authentication tag.
11. Decrypt the GCM ciphertext and verify the authentication tag to check data integrity.
12. Display the ciphertext and decrypted plaintext for all six modes. Display the GCM authentication tag.
13. Stop the program.
'''
