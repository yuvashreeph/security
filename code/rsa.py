from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

private_key = key
public_key = key.publickey()

print("Public Key:\n", public_key.export_key().decode())
print("Private Key:\n", private_key.export_key().decode())

plaintext = input("Enter Plaintext: ").encode()

# Encrypt using public key
ciphertext = PKCS1_OAEP.new(public_key).encrypt(plaintext)
print("\nCiphertext (hex):", ciphertext.hex())

# Decrypt using private key
decrypted = PKCS1_OAEP.new(private_key).decrypt(ciphertext)

print("Decrypted Plaintext:", decrypted.decode())

if decrypted == plaintext:
    print("Verification Successful")
else:
    print("Verification Failed")