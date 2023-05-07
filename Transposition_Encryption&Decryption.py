def encrypt(plaintext):
    plaintext = plaintext.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    plaintext += "_" * (9 - (len(plaintext) % 9))  # Pad the text with _ to make it a multiple of 9
    matrix = [list(plaintext[i:i+3]) for i in range(0, len(plaintext), 3)]  # Create a matrix
    transpose_matrix = [list(row) for row in zip(*matrix)]  # Transpose the matrix
    ciphertext = "".join([element for row in transpose_matrix for element in row])  # Flatten the matrix
    return ciphertext


def decrypt(ciphertext):
    ciphertext = ciphertext.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    matrix = [list(ciphertext[i:i+3]) for i in range(0, len(ciphertext), 3)]  # Create a matrix
    transpose_matrix = [list(row) for row in zip(*matrix)]  # Transpose the matrix
    plaintext = "".join([element for row in transpose_matrix for element in row])  # Flatten the matrix
    plaintext = plaintext.replace("_", "")  # Remove padding _ characters
    return plaintext


# Take user input
plaintext = input("Enter the text to be encrypted: ")

# Encrypt the input text
ciphertext = encrypt(plaintext)

# Display the input and output as 3x3 matrices
print("Input:")
for row in [list(plaintext[i:i+3]) for i in range(0, len(plaintext), 3)]:
    print(row)
print(f"Input = {plaintext}")
    
print("Output:")
for row in [list(ciphertext[i:i+3]) for i in range(0, len(ciphertext), 3)]:
    print(row)
print(f"Ciphertext = {ciphertext}")

# Take user input for decryption
ciphertext = input("Enter the ciphertext to be decrypted: ")

# Decrypt the input text
plaintext = decrypt(ciphertext)

# Display the input and output as 3x3 matrices
print("Input:")
for row in [list(ciphertext[i:i+3]) for i in range(0, len(ciphertext), 3)]:
    print(row)
print(f"Ciphertext = {ciphertext}")

print("Output:")
for row in [list(plaintext[i:i+3]) for i in range(0, len(plaintext), 3)]:
    print(row)
print(f"Plaintext = {plaintext}")
