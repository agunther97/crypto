from itertools import count
from string import ascii_lowercase

plain_text = 'july'
results_file = open('results.txt', 'w')
letters_to_numbers = dict(zip(ascii_lowercase, count(0)))
numbers_to_letters = dict(zip(count(0), ascii_lowercase))
plain_text_numbers = [letters_to_numbers[letter] for letter in plain_text]
for i in range(0, 26):
    #encrypt the plain text by shifting by some number
    cipher_numbers = [(num + i)%26 for num in plain_text_numbers]
    #try to decrypt the plain text by shifting forward by the same number (encrypt function = decrypt function)
    decrypted_cipher_numbers = [(num + i)%26 for num in cipher_numbers]
    attempted_plain_text = [numbers_to_letters[num] for num in decrypted_cipher_numbers]
    
    if ''.join(attempted_plain_text) == plain_text: #if we decrypt print which key values work
        print('At shift = ' + str(i) + ':')
        print('Plain text: ' + plain_text)
        print('Attempted Plain Text Decrypt: ' + ''.join(attempted_plain_text))