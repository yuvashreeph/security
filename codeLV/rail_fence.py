def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1  # 1 means moving down, -1 means moving up
    for char in text:
        fence[rail].append(char)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    ciphertext = "".join("".join(r) for r in fence)
    return ciphertext, fence

def rail_fence_decrypt(ciphertext, rails):
    fence = [['\n' for _ in range(len(ciphertext))] for _ in range(rails)]
    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        fence[rail][i] = '*'
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction  
    idx = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if fence[r][c] == '*' and idx < len(ciphertext):
                fence[r][c] = ciphertext[idx]
                idx += 1      
    plaintext = []
    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        plaintext.append(fence[rail][i])
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    return "".join(plaintext)

def display_rail_fence(text, rails):
    grid = [['.' for _ in range(len(text))] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for i, char in enumerate(text):
        grid[rail][i] = char
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    for row in grid:
        print(" ".join(row))

text = ''.join(c for c in input("Enter plaintext: ").upper() if c.isalnum())
rails = int(input("Enter number of rails (depth): "))

print("\n--- Rail Fence Zig-Zag Pattern ---")
display_rail_fence(text, rails)

cipher, matrix = rail_fence_encrypt(text, rails)
decrypted = rail_fence_decrypt(cipher, rails)

print("\n--- Results ---")
print("Plaintext  :", text)
print("Ciphertext :", cipher)
print("Decrypted  :", decrypted)