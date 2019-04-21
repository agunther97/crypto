from itertools import count
from string import ascii_lowercase

numbers_to_letters = dict(zip(count(0), ascii_lowercase))
n=18721
b=25
decoded_numbers = []
decoded_count = 0
cipher = [365,0,4845,14930,2608,2608,0]
while decoded_count != 7:
    for i in range(0,25):
        if pow(i,b,n) == cipher[decoded_count]:
            decoded_numbers.append(i)
            decoded_count = decoded_count+1
            if decoded_count == 7:
                break
decoded_letters = [numbers_to_letters[num] for num in decoded_numbers]
print(decoded_letters)
    