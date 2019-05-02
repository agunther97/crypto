import math

def find_s_and_t(n):
    s = 0
    t = 0
    for possible_t in range(math.ceil(math.sqrt(n)), n):
        if math.sqrt((pow(possible_t, 2) - n)) == math.ceil(math.sqrt((pow(possible_t, 2) - n))):
            t = possible_t
            s_squared = pow(t, 2) - n
            s = math.floor(math.sqrt(s_squared))
            return (s, t)

result = find_s_and_t(310485170747)

p = result[0] + result[1]
q = result[1] - result[0]

print("p = ", p)
print("q = ", q)