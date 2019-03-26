import random

def feistel(left, right, keys, rounds):
    for i in range(rounds):
        f = xor(right, keys[i])
        temp_right = right
        right = xor(left, f)
        left = temp_right
    temp_right = right
    right = left
    left = temp_right
    return [left,right]

def xor(binary_1, binary_2):
    #print(binary_1, binary_2)
    return format((int(binary_1,2) ^ int(binary_2,2)), '#06b')

user_input = input('Enter the number of rounds: ')
rounds = int(user_input)
keys = []
for i in range(rounds):
    keys.append(format(random.randint(1,16), '#06b'))
plain_text_binary = ['0b0111','0b0010']
print('Original Plain Text Binary:')
print(plain_text_binary[0][2:]+plain_text_binary[1][2:])
cipher_text_binary = feistel(plain_text_binary[0], plain_text_binary[1], keys, rounds)
print('Cipher Text Binry: ')
print(cipher_text_binary[0][2:] + cipher_text_binary[1][2:])
keys.reverse()
plain_text_binary = feistel(cipher_text_binary[0], cipher_text_binary[1], keys, rounds)
print('Plain Text Binary Found Using Cipher Text Binary with Reversed Keys: ')
print(plain_text_binary[0][2:]+plain_text_binary[1][2:])