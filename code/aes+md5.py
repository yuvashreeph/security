from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

key = b"1234567890123456"
iv = b"abcdefghijklmnop"

# Encryption
text = input("Enter message: ")
cipher = AES.new(key, AES.MODE_CBC, iv)
encrypted = cipher.encrypt(pad(text.encode(), 16))

# Generate MD5 hash
old_hash = hashlib.md5(encrypted).hexdigest()

print("Ciphertext:", encrypted.hex())
print("MD5 Hash:", old_hash)

# Check integrity before decryption
new_hash = hashlib.md5(encrypted).hexdigest()

if old_hash == new_hash:
    print("Integrity Verified")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), 16)

    print("Decrypted Message:", decrypted.decode())
else:
    print("Tampering Detected! Decryption Stopped.")
