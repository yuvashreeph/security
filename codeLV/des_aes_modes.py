from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_decrypt_demo(algorithm, mode_name, message, key):
    data = message.encode("utf-8")
    BlockCipher = DES if algorithm == "DES" else AES
    block = BlockCipher.block_size

    if mode_name == "ECB":
        cipher = BlockCipher.new(key, BlockCipher.MODE_ECB)
        encrypted = cipher.encrypt(pad(data, block))
        recovered = unpad(cipher.decrypt(encrypted), block)

    elif mode_name == "CBC":
        iv = get_random_bytes(block)
        cipher = BlockCipher.new(key, BlockCipher.MODE_CBC, iv=iv)
        encrypted = cipher.encrypt(pad(data, block))
        recovered = unpad(BlockCipher.new(key, BlockCipher.MODE_CBC, iv=iv).decrypt(encrypted), block)
        print("IV (hex):", iv.hex())

    elif mode_name in ("CFB", "OFB"):
        iv = get_random_bytes(block)
        mode = BlockCipher.MODE_CFB if mode_name == "CFB" else BlockCipher.MODE_OFB
        cipher = BlockCipher.new(key, mode, iv=iv, segment_size=8) if mode_name == "CFB" else BlockCipher.new(key, mode, iv=iv)
        encrypted = cipher.encrypt(data)  # no padding for stream-like modes
        decipher = BlockCipher.new(key, mode, iv=iv, segment_size=8) if mode_name == "CFB" else BlockCipher.new(key, mode, iv=iv)
        recovered = decipher.decrypt(encrypted)
        print("IV (hex):", iv.hex())

    elif mode_name == "CTR":
        nonce = get_random_bytes(block - 4)
        cipher = BlockCipher.new(key, BlockCipher.MODE_CTR, nonce=nonce)
        encrypted = cipher.encrypt(data)
        recovered = BlockCipher.new(key, BlockCipher.MODE_CTR, nonce=nonce).decrypt(encrypted)
        print("Nonce (hex):", nonce.hex())

    elif mode_name == "EAX":
        cipher = BlockCipher.new(key, BlockCipher.MODE_EAX)
        encrypted, tag = cipher.encrypt_and_digest(data)
        decipher = BlockCipher.new(key, BlockCipher.MODE_EAX, nonce=cipher.nonce)
        recovered = decipher.decrypt_and_verify(encrypted, tag)
        print("Nonce (hex):", cipher.nonce.hex())
        print("Authentication tag (hex):", tag.hex())

    else:
        raise ValueError("Mode must be ECB, CBC, CFB, OFB, CTR, or EAX.")

    print("Algorithm:", algorithm, "| Mode:", mode_name)
    print("Plaintext:", message)
    print("Ciphertext (hex):", encrypted.hex())
    print("Decrypted:", recovered.decode("utf-8"))
    print("Match:", recovered == data)

algorithm = input("Algorithm (DES/AES): ").strip().upper()
mode = input("Mode (ECB/CBC/CFB/OFB/CTR/EAX): ").strip().upper()
message = input("Plaintext: ")

if algorithm == "DES":
    key_text = input("DES key (exactly 8 ASCII bytes): ")
    key = key_text.encode("utf-8")
    if len(key) != 8: raise ValueError("DES key must be exactly 8 bytes.")
elif algorithm == "AES":
    key_text = input("AES key (16, 24, or 32 ASCII bytes): ")
    key = key_text.encode("utf-8")
    if len(key) not in (16,24,32): raise ValueError("AES key must be 16, 24, or 32 bytes.")
else:
    raise ValueError("Choose DES or AES.")
encrypt_decrypt_demo(algorithm, mode, message, key)
