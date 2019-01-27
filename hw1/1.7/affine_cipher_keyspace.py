from math import gcd

results_file = open('results.txt', 'w')
user_input = input('Enter the m value: ')
while user_input != 'q':
    m = int(user_input)
    results_file.write('Enter the m value: ' + str(m) + '\n')
    keys = 0
    for i in range(1,m):
        if gcd(i, m) == 1:
            keys = keys + 1
    keys = keys * m
    results_file.write(str(keys) + '\n')
    user_input = input('Enter the m value: ')