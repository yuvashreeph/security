from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

message = input("Enter plaintext: ")
key = input("Enter DES key (8 characters): ").encode()
mode = input("Enter mode (ECB/CBC/CFB/OFB): ").upper()

if len(key) != 8:
    raise ValueError("DES key must be exactly 8 bytes")

data = message.encode()
block = 8

if mode == "ECB":
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted = cipher.encrypt(pad(data, block))
    decrypted = unpad(DES.new(key, DES.MODE_ECB).decrypt(encrypted), block)

elif mode == "CBC":
    iv = get_random_bytes(block)
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    encrypted = cipher.encrypt(pad(data, block))
    decrypted = unpad(DES.new(key, DES.MODE_CBC, iv=iv).decrypt(encrypted), block)
    print("IV:", iv.hex())

elif mode == "CFB":
    iv = get_random_bytes(block)
    cipher = DES.new(key, DES.MODE_CFB, iv=iv, segment_size=8)
    encrypted = cipher.encrypt(data)
    decrypted = DES.new(key, DES.MODE_CFB, iv=iv, segment_size=8).decrypt(encrypted)
    print("IV:", iv.hex())

elif mode == "OFB":
    iv = get_random_bytes(block)
    cipher = DES.new(key, DES.MODE_OFB, iv=iv)
    encrypted = cipher.encrypt(data)
    decrypted = DES.new(key, DES.MODE_OFB, iv=iv).decrypt(encrypted)
    print("IV:", iv.hex())

else:
    raise ValueError("Invalid mode")

print("\nAlgorithm: DES")
print("Mode:", mode)
print("Plaintext:", message)
print("Ciphertext:", encrypted.hex())
print("Decrypted text:", decrypted.decode())
print("Match:", decrypted == data)
