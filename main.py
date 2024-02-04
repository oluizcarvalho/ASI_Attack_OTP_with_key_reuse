def read_and_split_by_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            full_text = file.read()
            lines = full_text.split('\n')
            return lines
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


def validate_and_print_ascii(hex_value):
    ascii_char = chr(int(hex_value, 16))
    print(f"ASCII character for {hex_value}: {ascii_char}")

    if ascii_char.isalnum():
        print(f"{ascii_char} is a valid character.")
        return True
    else:
        print(f"{ascii_char} is not a valid character.")
        return False


file_path = 'text_encoded.txt'
lines_from_file = read_and_split_by_lines(file_path)

if lines_from_file:
    print(lines_from_file)
    index_of_position = 0  # Change this to the desired index
    selected_position = lines_from_file[index_of_position]
    length_of_position = len(selected_position)
    pairs_length = length_of_position // 2
    print(f"Length of position {index_of_position + 1}: {length_of_position}: {pairs_length} pairs")

if lines_from_file:
    pairs_array = [[position[i:i + 2] for i in range(0, len(position), 2)] for position in lines_from_file]
    print("Pairs of characters from each position:")
    print(pairs_array)
    result = []
    # for i in range(0, len(pairs_array) - 1, 2):
    count_pairs = 0
    possible_spaces = []
    posicao_atual = pairs_array[5]
    proxima_posicao = pairs_array[6]
    # print(f"Comparando {i + 1} e {i + 2}")
    first_position_array1 = posicao_atual
    first_position_array2 = proxima_posicao

    hex_values_alpha = []
    for pair1, pair2 in zip(first_position_array1, first_position_array2):
        # Extract the first two digits from each pair
        first_two_digits1 = pair1[:2]
        first_two_digits2 = pair2[:2]
        # Convert to binary
        binary1 = bin(int(first_two_digits1[0], 16))[2:].zfill(4)
        binary2 = bin(int(first_two_digits2[0], 16))[2:].zfill(4)

        # print(f"Binary representation of {first_two_digits1[0]}: {binary1}")
        # print(f"Binary representation of {first_two_digits2[0]}: {binary2}")

        result_xor = bin(int(binary1, 2) ^ int(binary2, 2))[2:].zfill(4)
        # print(f"XOR of {binary1} and {binary2}: {result_xor}")

        if result_xor.startswith("01"):
            binary12 = bin(int(first_two_digits1[1], 16))[2:].zfill(4)
            binary22 = bin(int(first_two_digits2[1], 16))[2:].zfill(4)
            binary_results = [bin(int(binary1, 2) ^ int('0010', 2))[2:].zfill(4),
                              bin(int(binary12, 2) ^ int('0000', 2))[2:].zfill(4),
                              bin(int(binary2, 2) ^ int('0010', 2))[2:].zfill(4),
                              bin(int(binary22, 2) ^ int('0000', 2))[2:].zfill(4)]
            print(binary_results)
            hex_values_test = [hex(int(binary_results[0] + binary_results[1], 2))[2:],
                               hex(int(binary_results[2] + binary_results[3], 2))[2:]]
            index = 0
            for hex_value in hex_values_test:
                if validate_and_print_ascii(hex_value):
                    x = (first_two_digits1 if index == 0 else first_two_digits2)
                    y = (first_two_digits2 if index == 0 else first_two_digits1)
                    hex_values_alpha.append([hex_value, x, y, count_pairs + 1, chr(int(hex_value, 16))])
                    result.append(hex_values_alpha)
                index += 1
        else:
            print("The new binary does not start with '01'")
        count_pairs += 1

    print("Possible hex_values:", hex_values_alpha)
    print("Result", result)

else:
    print("Array doesn't have enough positions for comparison.")
