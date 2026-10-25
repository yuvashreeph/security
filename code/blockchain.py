import hashlib


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.mine()

    def calculate_hash(self):
        text = (
            str(self.index)
            + self.data
            + self.previous_hash
            + str(self.nonce)
        )

        return hashlib.sha256(text.encode()).hexdigest()

    def mine(self):
        while True:
            h = self.calculate_hash()

            if h.startswith("0000"):
                return h

            self.nonce += 1


# Create blockchain
b1 = Block(0, "Genesis", "0")
b2 = Block(1, "Alice pays Bob", b1.hash)
b3 = Block(2, "Bob pays Sam", b2.hash)

blockchain = [b1, b2, b3]

# Display blockchain
for b in blockchain:
    print("\nBlock:", b.index)
    print("Data:", b.data)
    print("Previous Hash:", b.previous_hash)
    print("Nonce:", b.nonce)
    print("Hash:", b.hash)

# Validate blockchain
valid = True

for i in range(1, len(blockchain)):
    if blockchain[i].hash != blockchain[i].calculate_hash():
        valid = False

    if blockchain[i].previous_hash != blockchain[i - 1].hash:
        valid = False

print("\nBlockchain VALID" if valid else "Blockchain INVALID")

# Modify a block
b2.data = "Alice pays 100 Bob"

# Check again
valid = True

for i in range(1, len(blockchain)):
    if blockchain[i].hash != blockchain[i].calculate_hash():
        valid = False

    if blockchain[i].previous_hash != blockchain[i - 1].hash:
        valid = False

print(
    "After modification:",
    "Blockchain VALID" if valid else "Blockchain INVALID"
)