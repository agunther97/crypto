from itertools import count
from string import ascii_lowercase
import math

def find_factor(n):
    start = math.floor(math.sqrt(n))
    if start % 2 == 0:
        start = start - 1
    ans = 1
    while ans != 0:
        ans = n % start
        if ans == 0:
            break
        start = start + 2
    return start

def multiplicative_inverse(a,b):
    a_0 = a
    b_0 = b
    t_0 = 0
    t = 1
    q = math.floor(a_0/b_0)
    r = a_0 - (q * b_0)
    while r > 0:
        temp = (t_0 - (q * t)) % a
        t_0 = t
        t = temp
        a_0 = b_0
        b_0 = r
        q = math.floor(a_0/b_0)
        r = a_0 - (q * b_0)
    return t

def sam(x, c, n):
    c = int(c)
    c = '{0:b}'.format(c) #to binary
    z = 1
    l = len(c)
    for i in range(l):
        z = (math.pow(z, 2)) % n
        if(c[i] == "1"):
            z = (z*x) % n
    return z

def decrypt_numbers(cipher):
    first = math.floor((cipher/(26*26))) % 26
    second = math.floor((cipher/26)) % 26
    third = math.floor(cipher) % 26
    return numbers_to_letters[first] + numbers_to_letters[second] + numbers_to_letters[third]    

numbers_to_letters = dict(zip(count(0), ascii_lowercase))
n = 18721
b = 25
cipher_text = [14456, 8031, 2159, 15155, 12168, 4109]

p = find_factor(n)
q = math.floor(n/p)

phi_n = (p-1) * (q-1)
a = multiplicative_inverse(phi_n, b)
plain_text_numbers = [sam(c, a, n) for c in cipher_text]
plain_text = [decrypt_numbers(c) for c in plain_text_numbers]
print (plain_text)