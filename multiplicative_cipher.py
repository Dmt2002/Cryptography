def multiplicative_encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        if letter.isalpha():
            shifted = (ord(letter.upper()) - 65) * key % 26 + 65
            ciphertext += chr(shifted)
        else:
            ciphertext += letter
    return ciphertext

def multiplicative_decrypt(ciphertext, key):
    plaintext = ""
    # Finding the multiplicative inverse of the key
    inverse_key = 0
    for i in range(26):
        if (i * key) % 26 == 1:
            inverse_key = i
            break
    
    for letter in ciphertext:
        if letter.isalpha():
            shifted = (ord(letter.upper()) - 65) * inverse_key % 26 + 65
            plaintext += chr(shifted)
        else:
            plaintext += letter
    return plaintext

# Example usage
plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key: "))

# Encryption
ciphertext = multiplicative_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext} \n Formula used for encryption : (E(x) = ({key} * x) mod 26)")

# Ask for the ciphertext to decrypt
decrypt_input = input("Enter the ciphertext to decrypt: ")

# Decryption
decrypted_text = multiplicative_decrypt(decrypt_input, key)
print(f"Decrypted text: {decrypted_text}  (D(x) = ({pow(key, 24, 26)} * x) mod 26)")
