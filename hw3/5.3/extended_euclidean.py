import math

def extended_euclidean(a,b):
    a_0 = a
    b_0 = b
    t_0 = 0
    t = 1
    s_0 = 1
    s = 0
    q = math.floor(a_0/b_0)
    r = a_0 - (q*b_0)
    while r > 0:
        temp = t_0 - (q*t)
        t_0 = t
        t = temp
        temp = s_0 - (q*s)
        s_0 = s
        s = temp
        a_0 = b_0
        b_0 = r
        q = math.floor(a_0/b_0)
        r = a_0 - (q*b_0)
    r = b_0
    return (r,s,t)

print("17^-1 mod 101:")
print(int(extended_euclidean(17, 101)[1]%101)) # s mod b = a^-1 mod b
print("357^-1 mod 1234:")
print(int(extended_euclidean(357, 1234)[1]%1234))
print("3125^-1 mod 9987:")
print(int(extended_euclidean(3125, 9987)[1]%9987))
