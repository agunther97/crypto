from itertools import count
from string import ascii_lowercase
import math

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

def encrypt_numbers(letters):
    first = math.floor(letters_to_numbers[letters[0]]*26*26)
    second = math.floor(letters_to_numbers[letters[1]]*26)
    third = math.floor(letters_to_numbers[letters[2]])
    return first+second+third 

def encrypt_rsa(plain_text, n, b):
    plain_text = [int(encrypt_numbers(entry)) for entry in plain_text]
    cipher_text = [int(sam(p, b, n)) for p in plain_text]
    return cipher_text

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

numbers_to_letters = dict(zip(count(0), ascii_lowercase))
letters_to_numbers = dict(zip(ascii_lowercase, count(0)))
n = 18721
b = 25
print(multiplicative_inverse(n, 365))
plain_text = [
    "hel", "lom", "yna", "mei", "saa", "ron" #hello my name is aaron
]
cipher_text1 = encrypt_rsa(plain_text, n, b)
cipher_text2 = [365,0,4845,14930,2608,2608,0]