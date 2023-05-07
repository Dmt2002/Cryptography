def shift_encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            shifted = (ord(letter.upper()) - 65 + key) % 26 + 65
            ciphertext += chr(shifted)
        else:
            ciphertext += letter
    return ciphertext

def shift_decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            shifted = (ord(letter.upper()) - 65 - key) % 26 + 65
            plaintext += chr(shifted)
        else:
            plaintext += letter
    return plaintext

# Example usage
plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key: "))

# Encryption
ciphertext = shift_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext} \n Formula used for encryption : (E(x) = (x + {key}) mod 26)")

# Ask for the ciphertext to decrypt
decrypt_input = input("Enter the ciphertext to decrypt: ")

# Decryption
decrypted_text = shift_decrypt(decrypt_input, key)
print(f"Decrypted text: {decrypted_text} \n Formula used for decryption : (D(x) = (x - {key}) mod 26)")
