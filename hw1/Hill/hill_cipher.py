import sys
import math
from itertools import count
import numpy as np
from string import ascii_lowercase

def main():
    user_input = input('Enter d to decrypt or e to encrypt: ')
    while True:
        if user_input == 'd':
            decrypt()
        elif user_input == 'e':
            encrypt()
        elif user_input == 'q':
            break
        else:
            print('Enter a valid option')

def encrypt():
    letters_to_numbers = dict(zip(ascii_lowercase, count(0)))
    numbers_to_letters = dict(zip(count(0), ascii_lowercase))
    plain_text = input('Enter your plain text: ')
    key = enter_hill_cipher_key()
    if len(plain_text) < len(key):
        plain_text = plain_text + 'q'
    chunk_size = int(len(plain_text)/len(key)) if len(plain_text) % len(key) == 0 else math.ceil(len(plain_text)/len(key))
    plain_text_chunks = add_padding_to_chunks(list(chunkstring(plain_text, chunk_size)), chunk_size)
    plain_text_matrix = [[letters_to_numbers[letter] for letter in chunk] for chunk in plain_text_chunks]
    print('Plain Text Matrix: ')
    print('\n'.join(str(entry) for entry in plain_text_matrix))
    encrypted_matrix = [[numbers_to_letters[num] for num in row] for row in [entry % 26 for entry in np.matmul(key, plain_text_matrix)]]
    print('Encrypted Matrix: ')
    print('\n'.join([str(entry) for entry in encrypted_matrix]))
    # print('Decrypyed Matrix: ')
    # encrypted_numbers = [[letters_to_numbers[num] for num in entry] for entry in encrypted_matrix]
    # inverted_key = np.linalg.inv(key)
    # inverted_key = np.matmul(inverted_key, np.linalg.det(key))
    # inverted_key = np.matmul(inverted_key, np.mu)
    # inverted_key = [[num for num in entry] for entry in inverted_key]
    # print('\n'.join([str(entry) for entry in inverted_key]))
    # decrypted_matrix = np.matmul(inverted_key, encrypted_numbers)
    # decrypted_matrix = [[int(num % 26) for num in entry] for entry in decrypted_matrix]
    # decrypted_matrix = [[numbers_to_letters[letter] for letter in entry] for entry in decrypted_matrix]
    # print('\n'.join([str(entry) for entry in decrypted_matrix]))


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def add_padding_to_chunks(text_chunks, key_size):
    for i in range(len(text_chunks)):
        while len(text_chunks[i].strip()) < key_size:
            text_chunks[i] = text_chunks[i] + 'q'
    return text_chunks

def decrypt():
    print('no')

def enter_hill_cipher_key():
    while True:
        key_size = input('Enter your key size: ')
        try:
            key_size = int(key_size)
            break
        except:
            print('Not a valid number for key\n')
    rows = list()
    while True:
        row = input('Enter the row with commas (,) between entries: ')
        row_entires = row.split(',')
        try:
            row_entires = [int(number) for number in row_entires]
        except:
            print('Row entries must be numbers!\n')
        if len(row_entires) > key_size or len(row_entires) < key_size:
            print('Invalid amount of entries in the row!\n')
        else:
            rows.append(row_entires)
            if len(rows) == key_size:
                try:
                    rows = [[num % 26 for num in entry] for entry in rows]
                    np.linalg.inv(rows)
                    break
                except:
                    print('key not invertable!')
                    rows.clear()
    return rows
        
if __name__ == '__main__':
    main()
