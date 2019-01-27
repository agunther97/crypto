from itertools import count
from string import ascii_lowercase

# cipher_text = open('shift_cipher_text.txt', 'r')
cipher_text = 'beeakfydjxuqyhyjiqryhtyjiqfbqduyjiikfuhcqd' # ddurq
letters = dict(zip(ascii_lowercase, count(0)))
numbers = dict(zip(count(0), ascii_lowercase))
cipher_text_numbers = [letters[letter] for letter in cipher_text]
for i in range(1,26):
    shifted_cipher = [(num - i)%26 for num in cipher_text_numbers] 
    plain_text = [numbers[num] for num in shifted_cipher]
    print('Shift Amount: ' + str(i) + ':')
    print(''.join(plain_text))
