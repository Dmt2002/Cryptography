#encrypt
def substitution_cipher_encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            idx = (alphabet.index(char) + key) % 26
            ciphertext += alphabet[idx]
        else:
            ciphertext += char
    return ciphertext

key = 3
plaintext = input("Enter the plaintext to be encrypted: ")
ciphertext = substitution_cipher_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
#decryptkhoor wfhw
def substitution_cipher_decrypt(ciphertext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = ""
    for char in ciphertext:
        if char in alphabet:
            idx = (alphabet.index(char) - key + 26) % 26
            plaintext += alphabet[idx]
        else:
            plaintext += char
    return plaintext

key = 3
ciphertext = input("Enter the ciphertext to be decrypted: ")
plaintext = substitution_cipher_decrypt(ciphertext, key)
print("Plaintext:", plaintext)
