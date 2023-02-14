import random

try:
    p = int(input("Enter the value of sender : "))
    q = int(input("Enter the value of receiver : "))
except ValueError as err:
    print(err)
    


# 2 secret large random number

a = random.randint(0,1000)
b = random.randint(0,1000)

if a == b:
    b = random.randint(0,1000)


r = (q**a)%p
s = (q**b)%p

r1 = (s**a)%p
s1 = (r**b)%p

print("\n\n***** Value of large prime numbers *****\n")
print(f'Value of sender is {p} and Value of receiver is {q} ')
print("\n\n***** Secret large random number *****\n")
print(f'Value1 : {a} Value2 : {b}')
print("\n\n***** Value of sender & receiver (key) *****\n")
print(f'R -> q^a mod p = {q} ^ {a} mod {p} = {r}     &     S -> q^b mod p = {q} ^ {b} mod {p} = {s}')
print("\n\n***** Secret key of sender & receiver *****\n")
print(f'Rk -> s^a mod p = {s} ^ {a} mod {p} = {r1}     &     Sk -> r^b mod p = {r} ^ {b} mod {p} = {s1}')

