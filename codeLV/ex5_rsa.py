from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto.Hash import SHA256

key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

def test_oaep(message_bytes):
    print("\n--- Method 1: RSA-OAEP (Standard & Secure) ---")
    cipher = PKCS1_OAEP.new(public_key, hashAlgo=SHA256)
    encrypted = cipher.encrypt(message_bytes)
    decrypted = PKCS1_OAEP.new(private_key, hashAlgo=SHA256).decrypt(encrypted)
    print("Ciphertext (Hex):", encrypted.hex())
    print("Decrypted Text:", decrypted.decode())
    print("Verification Match:", decrypted == message_bytes)

def test_v1_5(message_bytes):
    print("\n--- Method 2: PKCS#1 v1.5 Padding (Legacy) ---")
    cipher = PKCS1_v1_5.new(public_key)
    encrypted = cipher.encrypt(message_bytes)
    sentinel = b"Decryption failed"
    decrypted = PKCS1_v1_5.new(private_key).decrypt(encrypted, sentinel)
    print("Ciphertext (Hex):", encrypted.hex())
    print("Decrypted Text:", decrypted.decode())
    print("Verification Match:", decrypted == message_bytes)

def test_raw(message_bytes):
    print("\n--- Method 3: Raw / Textbook RSA (No Padding) ---")
    msg_int = int.from_bytes(message_bytes, byteorder='big')
    if msg_int >= public_key.n:
        print("Error: Message is too large for raw RSA encryption.")
        return
    encrypted_int = pow(msg_int, public_key.e, public_key.n)
    decrypted_int = pow(encrypted_int, private_key.d, private_key.n)
    decrypted_bytes = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, byteorder='big')
    print("Ciphertext (Integer):", encrypted_int)
    print("Decrypted Text:", decrypted_bytes.decode())
    print("Verification Match:", decrypted_bytes == message_bytes)

while True:
    message = input("Enter new plaintext message: ").encode('utf-8')
    print("\n=========== RSA IMPLEMENTATION MODES ===========")
    print("1. Run RSA-OAEP (Recommended)")
    print("2. Run PKCS#1 v1.5 Padding")
    print("3. Run Raw RSA (No Padding)")
    print("4. Exit")
    choice = input("Enter your choice (1-6): ").strip()
    if choice == "1":
        test_oaep(message)
    elif choice == "2":
        test_v1_5(message)
    elif choice == "3":
        test_raw(message)
    elif choice == "4":
        print("Exiting...")
        break