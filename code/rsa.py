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


'''
### Algorithm: RSA Encryption and Decryption

1. Start the program.
2. Import the RSA and PKCS1-OAEP modules.
3. Generate an RSA key pair consisting of a public key and a private key.
4. Display the public key and private key.
5. Read the plaintext from the user and convert it into bytes.
6. Encrypt the plaintext using the public key and PKCS1-OAEP padding.
7. Display the ciphertext in hexadecimal format.
8. Decrypt the ciphertext using the private key.
9. Convert the decrypted bytes into text and display the plaintext.
10. Compare the decrypted plaintext with the original plaintext.
11. If both match, display "Verification Successful"; otherwise, display "Verification Failed".
12. Stop the program.
'''
