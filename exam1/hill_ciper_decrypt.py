import sys
import math
from itertools import count
import numpy as np
from string import ascii_uppercase

def main():
    inverse_key = [[8,18,19],[7,23,22],[11,2,13]]
    cipher_text = '''ciphertext here'''
    cipher_text = cipher_text.replace(' ', '')
    cipher_text = cipher_text.replace('\n', '')
    letters_to_numbers = dict(zip(ascii_uppercase, count(0)))
    numbers_to_letters = dict(zip(count(0), ascii_uppercase))
    cipher_text = [letters_to_numbers[letter] for letter in cipher_text]
    cipher_text_matrix = make_matrix_from_text(cipher_text)
    plain_text = np.matmul(inverse_key,cipher_text_matrix)
    plain_text = [[int(number % 26) for number in row]for row in plain_text]
    plain_text = [[numbers_to_letters[number] for number in row] for row in plain_text]
    print_plain_text(plain_text)

def print_plain_text(matrix):
    plain_text = ''
    for i in range(len(matrix[0])):
        plain_text = plain_text + str(matrix[0][i]) + str(matrix[1][i]) + str(matrix[2][i])
    print(plain_text)

def make_matrix_from_text(text):
    a=0
    b=1
    c=2
    row_1 = []
    row_2 = []
    row_3 = []
    while c < len(text):
        row_1.append(text[a])
        row_2.append(text[b])
        row_3.append(text[c])
        a = a+3
        b = b+3
        c = c+3
    matrix = [row_1,row_2,row_3]
    return matrix

if __name__ == '__main__':
    main()