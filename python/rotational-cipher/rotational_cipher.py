def rotate(text, key_chifer):

    alphabet_dict = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f',
        7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
        13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r',
        19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x',
        25: 'y', 26: 'z'
    }
    # Step 1: reverse the dictionary
    letter_to_number = {}
    for key, value in alphabet_dict.items():
        letter_to_number[value] = key

    # Step 2: loop through the text and convert to numbers
    result = ''
    for char in text:
        if char in letter_to_number:
            num = letter_to_number[char]
            rotated_num = (num + key_chifer - 1) % 26 + 1  # Wrap around 1-26
            result += alphabet_dict[rotated_num]
            # preserve original case
            result += rotated_char.upper() if char.isupper() else rotated_char
        else:
            result += char  # preserve spaces and punctuation
    return result

print(rotate("O M G", 5))