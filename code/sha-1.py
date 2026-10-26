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


'''
## Algorithm: SHA-1 Message Digest, Avalanche Effect, Message Comparison, and Preprocessing

1. Start the program and import the `hashlib` module.
2. Define a function to generate the SHA-1 digest of a message.
3. Display the menu with options to generate a digest, demonstrate the avalanche effect, compare messages, perform preprocessing, or exit.
4. Read the user's choice.
5. If option 1 is selected, read a message, calculate its SHA-1 digest, and display it.
6. If option 2 is selected, read a message and the position to modify, change the character, and calculate both SHA-1 digests.
7. Convert both digests into 160-bit binary values and count the number of bits that differ.
8. If option 3 is selected, read two messages, calculate their SHA-1 digests, and compare the hashes to determine whether the messages are identical or different.
9. If option 4 is selected, convert the sentence into binary form and calculate its original length in bits.
10. Append a `1` bit, add `0` bits until the length is 448 modulo 512, and append the original length as a 64-bit value.
11. Divide the padded message into 512-bit blocks and display each block and the SHA-1 digest.
12. If option 5 is selected, exit the program.
13. If an invalid choice is entered, display an error message.
14. Repeat the menu until the user chooses to exit.
15. Stop the program.
'''
