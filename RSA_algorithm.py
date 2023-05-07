import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = inverse(e, phi)
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

# Example usage
p = 61
q = 53
public, private = generate_keypair(p, q)
message = "44"
cipher_text = encrypt(public, message)
print(cipher_text)
plain_text = decrypt(private, cipher_text)
print(plain_text)
