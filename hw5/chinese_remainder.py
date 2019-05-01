from functools import reduce
import math

def multiplicative_inverse(a,p):
    a_0 = p
    b_0 = a
    t_0 = 0
    t = 1
    q = math.floor(a_0/b_0)
    r = a_0 - (q * b_0)
    while r > 0:
        temp = (t_0 - (q * t)) % p
        t_0 = t
        t = temp
        a_0 = b_0
        b_0 = r
        q = math.floor(a_0/b_0)
        r = a_0 - (q * b_0)
    return t

def chinese_remainder(number_values, mod_values=None):
    if (mod_values is None):
        if (type(number_values[0])==tuple):
            mod_values=[number_values[i][1] for i in range(len(number_values))]
            number_values=[number_values[i][0] for i in range(len(number_values))]
        elif (type(number_values[0])==list):
            if len(number_values[0])>2:
                mod_values=[number_values[1][i] for i in range(len(number_values[0]))]
                number_values=[number_values[0][i] for i in range(len(number_values[0]))]
            else:
                mod_values=[number_values[i][1] for i in range(len(number_values))]
                number_values=[number_values[i][0] for i in range(len(number_values))]
    M = reduce((lambda x, y: x * y), mod_values)
    m_subs = list(map((lambda x: M/x), mod_values))
    y_subs = []
    for i in range(len(m_subs)):
        y_subs.append(int(multiplicative_inverse(m_subs[i], mod_values[i])))
    x = 0
    x_calc_string = 'x=mod('
    for i in range(len(number_values)):
        x += number_values[i]*m_subs[i]*y_subs[i]
        x_calc_string += str(number_values[i]) + '*' + str(m_subs[i]) + '*' + str(y_subs[i]) + ' + '
    x = int(x%M)
    return x
p = 26981
q = 62549
num_1 = chinese_remainder([p-1, q-1], [p,q])
num_2 = chinese_remainder([1, q-1], [p,q])
num_3 = chinese_remainder([1,1], [p,q])
num_4 = chinese_remainder([p-1,1], [p,q])
print('result of pair one: a = ' + str(num_1))
print('result of pair two: a = ' + str(num_2))
print('result of pair three: a = ' + str(num_3))
print('result of pair four: a = ' + str(num_4))