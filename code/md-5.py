import hashlib

# Generate MD5 hash
text = input("Enter text: ")
md5_hash = hashlib.md5(text.encode()).hexdigest()

print("MD5 Hash:", md5_hash)
print("Length:", len(md5_hash))

# Verify message integrity
old_hash = input("Enter previous MD5 hash: ")
new_hash = hashlib.md5(text.encode()).hexdigest()

if old_hash.lower() == new_hash:
    print("Message is not modified")
else:
    print("Message is modified")

# Avalanche effect
text1 = input("Enter first string: ")
text2 = input("Enter similar string: ")

h1 = hashlib.md5(text1.encode()).hexdigest()
h2 = hashlib.md5(text2.encode()).hexdigest()

print("Hash 1:", h1)
print("Hash 2:", h2)

b1 = bin(int(h1, 16))[2:].zfill(128)
b2 = bin(int(h2, 16))[2:].zfill(128)

changed = sum(x != y for x, y in zip(b1, b2))
print("Bits changed:", changed, "/ 128")