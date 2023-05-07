import random

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

try:
    # Get prime numbers from the user
    p = int(input("Enter a prime number: "))
    if not is_prime(p):
        raise ValueError("Value entered is not a prime number.")
    q = int(input("Enter another prime number: "))
    if not is_prime(q):
        raise ValueError("Value entered is not a prime number.")
except ValueError as err:
    print(err)
    exit()

# Generate two secret large random numbers
secret_key_a = random.randint(0, 1000)
secret_key_b = random.randint(0, 1000)

# Make sure the secret keys are not equal
if secret_key_a == secret_key_b:
    secret_key_b = random.randint(0, 1000)

# Calculate R and S
R = (q ** secret_key_a) % p
S = (q ** secret_key_b) % p

# Calculate the secret keys of sender and receiver
secret_key_sender = (S ** secret_key_a) % p
secret_key_receiver = (R ** secret_key_b) % p

# Print the results
print("\n\n*** Value of prime numbers ***\n")
print(f"Value of p is {p} and Value of q is {q} ")

print("\n\n*** Secret large random numbers ***\n")
print(f"Secret key of sender: {secret_key_a} Secret key of receiver: {secret_key_b}")

print("\n\n*** Value of R and S (keys) ***\n")
print(f"R -> q^a mod p = {q} ^ {secret_key_a} mod {p} = {R}\nS -> q^b mod p = {q} ^ {secret_key_b} mod {p} = {S}")

print("\n\n*** Secret key of sender and receiver ***\n")
print(f"Secret key of sender -> S^a mod p = {S} ^ {secret_key_a} mod {p} = {secret_key_sender}\nSecret key of receiver -> R^b mod p = {R} ^ {secret_key_b} mod {p} = {secret_key_receiver}")
