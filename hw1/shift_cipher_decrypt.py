from itertools import count
from string import ascii_lowercase

cipher_text = 'beeakfydjxuqyhyjiqryhtyjiqfbqduyjiikfuhcqd'
results_file = open('results.txt', 'w')
letters_to_numbers = dict(zip(ascii_lowercase, count(0)))
numbers_to_letters = dict(zip(count(0), ascii_lowercase))
cipher_text_numbers = [letters_to_numbers[letter] for letter in cipher_text]
for i in range(1,26):
    shifted_cipher = [(num - i)%26 for num in cipher_text_numbers] 
    plain_text = [numbers_to_letters[num] for num in shifted_cipher]
    results_file.write('\n')
    results_file.write('Shift Amount: ' + str(i))
    results_file.write('\n')
    results_file.write(''.join(plain_text))
