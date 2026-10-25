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