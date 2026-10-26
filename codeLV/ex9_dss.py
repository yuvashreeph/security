from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

private_key = None
public_key = None

def generate_keys():
    global private_key, public_key
    print("\nGenerating 2048-bit RSA Key Pair...")
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    print("Keys generated and stored in memory successfully!")

def sign_message():
    if not private_key:
        print("Error: Generate keys first")
        return
    message = input("Enter message to sign: ").encode()
    h = SHA256.new(message)
    signature = pkcs1_15.new(private_key).sign(h)
    print("\n--- Signing Output ---")
    print("Original message:", message.decode())
    print("SHA-256 Digest:", h.hexdigest())
    print("Digital Signature (Hex):", signature.hex())

def verify_message():
    if not public_key:
        print("Error: Generate keys first")
        return
    message = input("Enter received message: ").encode()
    sig_hex = input("Enter signature hex: ").strip()
    
    try:
        h = SHA256.new(message)
        pkcs1_15.new(public_key).verify(h, bytes.fromhex(sig_hex))
        print("\nStatus: Signature VALID (Authentic & Untampered)")
    except (ValueError, TypeError):
        print("\nStatus: Signature INVALID (Modified or Incorrect)")

def tamper_demo():
    if not private_key:
        print("Error: Generate keys first")
        return
    original = input("Enter original message: ")
    h = SHA256.new(original.encode())
    signature = pkcs1_15.new(private_key).sign(h)
    tampered = original + " [TAMPERED]"
    print("\nOriginal:", original)
    print("Tampered in transit:", tampered)
    
    try:
        pkcs1_15.new(public_key).verify(SHA256.new(tampered.encode()), signature)
        print("Status: VALID")
    except (ValueError, TypeError):
        print("\nStatus: FAILED / INVALID (Integrity check caught the change!)")

def email_simulation():
    global private_key, public_key
    if not private_key:
        key = RSA.generate(2048)   # Auto-generate keys if missing for convenience
        private_key = key
        public_key = key.publickey()  
    print("\n==========================================")
    print("      ALICE & BOB SECURE E-MAIL SIMULATION")
    print("==========================================")
    msg = input("Alice, enter message for Bob: ").encode()
    # 1. Hash & Sign
    h = SHA256.new(msg)
    sig = pkcs1_15.new(private_key).sign(h)
    print("1. Alice hashes message and signs with private key.")
    # 2. Transmission & Normal Verification
    print("2. Transmitting message + signature to Bob...")
    try:
        pkcs1_15.new(public_key).verify(SHA256.new(msg), sig)
        print("3. Bob's Verification: [ VALID ] (Sender is authentic)")
    except:
        print("3. Bob's Verification: [ INVALID ]")   
    # 3. Tampering Simulation
    altered = msg + b" [HACKED]"
    print(f"4. Interceptor alters message to: \"{altered.decode()}\"")
    try:
        pkcs1_15.new(public_key).verify(SHA256.new(altered), sig)
        print("5. Tampered Verification: [ VALID ]")
    except:
        print("5. Tampered Verification: [ INVALID / FAILED ]")
    print("==========================================")

while True:
    print("\n=========== DIGITAL SIGNATURE SYSTEM ===========")
    print("1. Generate Keys")
    print("2. Sign Message")
    print("3. Verify Signature")
    print("4. Demonstrate Tampering")
    print("5. Simulate Alice-Bob Email")
    print("6. Exit")
    print("===============================================")
    choice = input("Enter choice (1-6): ").strip()
    if choice == "1": generate_keys()
    elif choice == "2": sign_message()
    elif choice == "3": verify_message()
    elif choice == "4": tamper_demo()
    elif choice == "5": email_simulation()
    elif choice == "6": 
        print("Exiting...")
        break
    else: 
        print("Invalid choice. Enter 1-6.")