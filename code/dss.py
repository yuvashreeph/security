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
