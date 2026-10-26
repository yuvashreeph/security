
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

message = input("Enter plaintext: ")
key = input("Enter AES key (16, 24, or 32 characters): ").encode()
mode = input("Enter mode (ECB/CBC/CFB/OFB): ").upper()

if len(key) not in (16, 24, 32):
    raise ValueError("AES key must be 16, 24, or 32 bytes")

data = message.encode()
block = 16

if mode == "ECB":
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(data, block))
    decrypted = unpad(AES.new(key, AES.MODE_ECB).decrypt(encrypted), block)

elif mode == "CBC":
    iv = get_random_bytes(block)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    encrypted = cipher.encrypt(pad(data, block))
    decrypted = unpad(AES.new(key, AES.MODE_CBC, iv=iv).decrypt(encrypted), block)
    print("IV:", iv.hex())

elif mode == "CFB":
    iv = get_random_bytes(block)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=8)
    encrypted = cipher.encrypt(data)
    decrypted = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=8).decrypt(encrypted)
    print("IV:", iv.hex())

elif mode == "OFB":
    iv = get_random_bytes(block)
    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    encrypted = cipher.encrypt(data)
    decrypted = AES.new(key, AES.MODE_OFB, iv=iv).decrypt(encrypted)
    print("IV:", iv.hex())

else:
    raise ValueError("Invalid mode")

print("\nAlgorithm: AES")
print("Mode:", mode)
print("Plaintext:", message)
print("Ciphertext:", encrypted.hex())
print("Decrypted text:", decrypted.decode())
print("Match:", decrypted == data)
