import hashlib

def generate_sha1():
    text = input("\nEnter text message: ")
    digest = hashlib.sha1(text.encode()).hexdigest()
    print("Original Message:", text)
    print("SHA-1 Digest (40-char hex):", digest)

def avalanche_effect():
    text1 = input("\nEnter original text: ")
    if text1:
        text2 = text1[:-1] + chr(ord(text1[-1]) + 1)
    else:
        text2 = "A"
    d1 = hashlib.sha1(text1.encode()).hexdigest()
    d2 = hashlib.sha1(text2.encode()).hexdigest()
    print(f"String 1: '{text1}' -> SHA-1: {d1}")
    print(f"String 2: '{text2}' -> SHA-1: {d2}")
    print("1-character change completely alters the hash output!")

def compare_messages():
    print("\n--- Compare Two Messages ---")
    m1 = input("Enter message 1: ")
    m2 = input("Enter message 2: ")
    h1 = hashlib.sha1(m1.encode()).hexdigest()
    h2 = hashlib.sha1(m2.encode()).hexdigest()
    print("Hash 1:", h1)
    print("Hash 2:", h2)
    if h1 == h2:
        print("Result: Messages are IDENTICAL.")
    else:
        print("Result: Messages are DIFFERENT.")

def sha1_preprocessing():
    print("\n--- SHA-1 Preprocessing Stage Demonstration ---")
    msg = input("Enter a sentence: ")
    data = msg.encode('utf-8')
    orig_bit_len = len(data) * 8
    # 1. Convert to binary representation
    binary_msg = ''.join(format(b, '08b') for b in data)
    print(f"\n1. Original message binary length: {orig_bit_len} bits")
    print(f"   Binary preview: {binary_msg[:32]}...")
    # 2. Padding: Append '1' bit (0x80) and '0' bits until length ≡ 448 mod 512 (56 bytes mod 64)
    padded = bytearray(data)
    padded.append(0x80) 
    while len(padded) % 64 != 56:
        padded.append(0x00)
    # 3. Append 64-bit big-endian representation of original message length
    padded += orig_bit_len.to_bytes(8, byteorder='big')
    padded_binary = ''.join(format(b, '08b') for b in padded)
    print(f"\n2. Padding complete! Total padded length: {len(padded_binary)} bits (Multiple of 512 bits)")
    print(f"   Padded binary preview: {padded_binary[:64]}... (truncated)")
    # 4. Division into 512-bit (64-byte) blocks
    print(f"\n3. Division into 512-bit blocks (Total blocks: {len(padded) // 64}):")
    for i in range(0, len(padded), 64):
        block = padded[i:i+64]
        print(f"   Block {i//64 + 1}: {block.hex()[:32]}... (64 bytes / 512 bits)")
    # 5. Final Hash Generation
    digest = hashlib.sha1(data).hexdigest()
    print(f"\n4. Final SHA-1 Message Digest: {digest}")

while True:
    print("\n--- SHA-1 MENU ---")
    print("1. Generate SHA-1 Digest")
    print("2. Demonstrate Avalanche Effect")
    print("3. Compare Two Messages via Hashes")
    print("4. Demonstrate SHA-1 Preprocessing & Padding")
    print("5. Exit")
    choice = input("Choice (1-5): ").strip()
    if choice == "1": generate_sha1()
    elif choice == "2": avalanche_effect()
    elif choice == "3": compare_messages()
    elif choice == "4": sha1_preprocessing()
    elif choice == "5": break
    else: print("Invalid choice. Try again.")