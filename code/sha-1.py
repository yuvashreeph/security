import hashlib

def sha1(msg):
    return hashlib.sha1(msg.encode()).hexdigest()

def generate():
    m = input("Enter message: ")
    print("Original Message:", m)
    print("SHA-1 Digest:", sha1(m))

def avalanche():
    m = input("Enter message: ")
    pos = int(input(f"Position to modify (0-{len(m)-1}): "))

    new = chr(ord(m[pos]) + 1)
    m2 = m[:pos] + new + m[pos+1:]

    h1, h2 = sha1(m), sha1(m2)

    print("Original:", m, "->", h1)
    print("Modified:", m2, "->", h2)

    b1 = bin(int(h1, 16))[2:].zfill(160)
    b2 = bin(int(h2, 16))[2:].zfill(160)

    print("Bits changed:", sum(x != y for x, y in zip(b1, b2)), "/ 160")


def compare():
    m1 = input("Message 1: ")
    m2 = input("Message 2: ")

    h1, h2 = sha1(m1), sha1(m2)

    print(h1, "\n" + h2)
    print("Messages are IDENTICAL" if h1 == h2 else "Messages are DIFFERENT")


def preprocessing():
    m = input("Enter sentence: ")

    bits = "".join(format(b, "08b") for b in m.encode())
    L = len(bits)

    bits += "1"

    while len(bits) % 512 != 448:
        bits += "0"

    bits += format(L, "064b")

    print("Original length (bits):", L)
    print("Padded message length:", len(bits))
    print("Padded message:\n", bits)

    blocks = [bits[i:i+512] for i in range(0, len(bits), 512)]

    for i, b in enumerate(blocks, 1):
        print(f"Block {i} (512 bits):", b)

    print("SHA-1 Digest:", sha1(m))


def main():
    while True:
        print("\n===== SHA-1 MESSAGE DIGEST =====")
        print("1. Generate SHA-1 Message Digest")
        print("2. Demonstrate Avalanche Effect")
        print("3. Compare Two Messages")
        print("4. Demonstrate SHA-1 Preprocessing")
        print("5. Exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            generate()
        elif ch == "2":
            avalanche()
        elif ch == "3":
            compare()
        elif ch == "4":
            preprocessing()
        elif ch == "5":
            break
        else:
            print("Invalid choice")

main()