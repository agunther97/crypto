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
    return format((int(binary_1,2) ^ int(binary_2,2)), '#06b')

def complement(number):
    new_num = '0b'
    for entry in number:
        if entry == '0':
            new_num = new_num + '1'
        else:
            new_num = new_num + '0'
    return new_num

rounds = 15
keys = []
for i in range(rounds):
    keys.append(format(random.randint(0,15), '#06b'))
plain_text_binary_left = '0b'
plain_text_binary_right = '0b'
for i in range(4):
    plain_text_binary_left = plain_text_binary_left + str(random.randint(0,1))
    plain_text_binary_right = plain_text_binary_right + str(random.randint(0,1))
plain_text_binary = [plain_text_binary_left, plain_text_binary_right]
print('Original Plain Text Binary (x):')
print(plain_text_binary[0][2:]+plain_text_binary[1][2:])
cipher_text_binary = feistel(plain_text_binary[0], plain_text_binary[1], keys, rounds)
print('Original Cipher Text Binary (y):')
print(cipher_text_binary[0][2:] + cipher_text_binary[1][2:])
print('Bitwise Complement of Cipher Text (c(y)):')
print(complement(cipher_text_binary[0][2:]+cipher_text_binary[1][2:])[2:])
bitwise_keys = [complement(key[2:]) for key in keys]
found_bitwise_complement = feistel(complement(plain_text_binary[0][2:]), complement(plain_text_binary[1][2:]), bitwise_keys, rounds)
print('Found Bitwise Complement of Cipher Text (y\'):')
print(found_bitwise_complement[0][2:] + found_bitwise_complement[1][2:])