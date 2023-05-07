def caesar_encrypt(plaintext, key=3):
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            shifted = (ord(letter.upper()) - 65 + key) % 26 + 65
            ciphertext += chr(shifted)
        else:
            ciphertext += letter
    return ciphertext

def caesar_decrypt(ciphertext, key=3):
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

# Encryption
ciphertext = caesar_encrypt(plaintext)
print(f"Ciphertext: {ciphertext} \n Formula used for encryption : (E(x) = (x + 3) mod 26)")

# Decryption
encrypted_text = input("Enter the encrypted text: ")
decrypted_text = caesar_decrypt(encrypted_text)
print(f"Decrypted text: {decrypted_text} \n Formula used for decryption : (D(x) = (x - 3) mod 26)")
