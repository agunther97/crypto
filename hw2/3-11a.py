def swap_bit_position(binary_string):
    return '0b' + binary_string[3] + binary_string[2] + binary_string[5] + binary_string[4]

def xor(binary_1, binary_2):
    return '{1:0{0}b}'.format(6, int(binary_1,2) ^ int(binary_2,2))

rows = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

binary_rows = [[format(number, '#06b')  for number in row] for row in rows]
binary_rows_with_swaped_bits = [[swap_bit_position(bin_string) for bin_string in row] for row in binary_rows]
binary_rows_xored = [[xor(bin_string, '0b0110') for bin_string in row] for row in binary_rows_with_swaped_bits]
results = [[int(bin_string, 2) for bin_string in row] for row in binary_rows_xored]
print('Original row 2')
print(rows[1])
print('Row 1 mutated to Row 2')
print(results[0])