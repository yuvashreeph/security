def rail_fence_encrypt(text, rails):
    if rails <= 1 or rails >= len(text):
        return text, [text]

    fence = [[] for _ in range(rails)]
    row = 0
    direction = 1

    for ch in text:
        fence[row].append(ch)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    ciphertext = ""

    for rail in fence:
        ciphertext += ''.join(rail)

    return ciphertext, fence


def rail_fence_decrypt(ciphertext, rails):
    if rails <= 1 or rails >= len(ciphertext):
        return ciphertext

    pattern = []
    row = 0
    direction = 1

    for i in range(len(ciphertext)):
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    rail_lengths = []

    for i in range(rails):
        rail_lengths.append(pattern.count(i))

    fence = []
    index = 0

    for length in rail_lengths:
        fence.append(list(ciphertext[index:index + length]))
        index += length

    positions = [0] * rails
    plaintext = ""

    for r in pattern:
        plaintext += fence[r][positions[r]]
        positions[r] += 1

    return plaintext


def main():
    plaintext = input("Enter plaintext: ")
    rails = int(input("Enter number of rails: "))

    if rails < 2:
        print("Number of rails must be at least 2.")
        return

    ciphertext, fence = rail_fence_encrypt(plaintext, rails)

    print("\nArrangement of characters in each rail:")

    for i, rail in enumerate(fence, 1):
        print("Rail", i, ":", ''.join(rail))

    print("\nEncrypted Text:", ciphertext)

    decrypted = rail_fence_decrypt(ciphertext, rails)
    print("Decrypted Text:", decrypted)


if __name__ == "__main__":
    main()