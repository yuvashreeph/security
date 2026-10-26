from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# 1. Generate RSA keys
key = RSA.generate(2048)
public_key = key.publickey()

print("RSA keys generated successfully")

# 2. Sign a message
message = input("\nEnter message: ")

hash_value = SHA256.new(message.encode())
signature = pkcs1_15.new(key).sign(hash_value)

print("SHA-256 Hash:", hash_value.hexdigest())
print("Digital Signature:", signature.hex())

# 3. Verify the signature
try:
    pkcs1_15.new(public_key).verify(
        SHA256.new(message.encode()), signature
    )
    print("Signature VALID")

except (ValueError, TypeError):
    print("Signature INVALID")

# 4. Demonstrate message tampering
modified = input("\nEnter modified message: ")

try:
    pkcs1_15.new(public_key).verify(
        SHA256.new(modified.encode()), signature
    )
    print("Modified message: Signature VALID")

except (ValueError, TypeError):
    print("Modified message: Signature INVALID")

# 5. Alice and Bob email example
alice = RSA.generate(2048)
bob = RSA.generate(2048)

email_message = input("\nAlice's e-mail message: ")

# Alice signs using her private key
email_signature = pkcs1_15.new(alice).sign(
    SHA256.new(email_message.encode())
)

print("Alice's signature:", email_signature.hex()[:64], "...")

# Bob verifies using Alice's public key
try:
    pkcs1_15.new(alice.publickey()).verify(
        SHA256.new(email_message.encode()), email_signature
    )
    print("Bob: E-mail signature VALID")

except (ValueError, TypeError):
    print("Bob: E-mail signature INVALID")

# Test modified email
tampered_email = email_message + " (tampered)"

try:
    pkcs1_15.new(alice.publickey()).verify(
        SHA256.new(tampered_email.encode()), email_signature
    )
    print("Tampered e-mail: VALID")

except (ValueError, TypeError):
    print("Tampered e-mail: INVALID")

print("Digital Signature Experiment Completed")



'''

from Crypto.PublicKey import RSA
from Crypto.Signature import pss 
from Crypto.Hash import SHA256 

key = RSA.generate(2048)
priv = key
publ = key.publickey()

msg = input("Enter message: ")
h = SHA256.new(msg.encode())
sign = pss.new(priv).sign(h)

try:
    pss.new(publ).verify(SHA256.new(msg.encode()), sign)
except(ValueError, TypeError):
    print("Invalid")
    
'''


'''
### Algorithm: RSA Digital Signature using SHA-256

1. Start the program.
2. Import the RSA, digital signature, and SHA-256 modules.
3. Generate an RSA public key and private key.
4. Read the message from the user.
5. Calculate the SHA-256 hash of the message.
6. Sign the hash using the sender's private key.
7. Display the hash and digital signature.
8. Verify the signature using the public key.
9. If verification succeeds, display "Signature VALID"; otherwise, display "Signature INVALID".
10. Read a modified message and verify its signature.
11. Display whether the modified message's signature is valid or invalid.
12. Generate RSA key pairs for Alice and Bob.
13. Read Alice's email message and sign it using Alice's private key.
14. Verify the email signature using Alice's public key.
15. Modify the email and verify it again to demonstrate tampering detection.
16. Display the experiment completion message.
17. Stop the program.
'''
