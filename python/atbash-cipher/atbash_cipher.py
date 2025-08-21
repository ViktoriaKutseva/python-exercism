
plain_alphabet = 'abcdefghijklmnopqrstuvwxyz'
reversed_alphabet = 'zyxwvutsrqponmlkjihgfedcba'
numbers = '1234567890'

def encode(plain_text):
    result_no_spaces = ''
    result = ''
    plain_text = plain_text.lower().replace(' ', '')
    temp_text = ''
    for char in plain_text:
        if char in plain_alphabet or char in numbers:
            temp_text += char
        else:
            temp_text += ''
    for char in temp_text:
        if char in plain_alphabet:
            found_index = plain_alphabet.index(char)
            result_no_spaces += reversed_alphabet[found_index]
        else:
            result_no_spaces += char
    if len(result_no_spaces) > 5:
        for i in range(len(result_no_spaces)):
            if i % 5 == 0 and i != 0: 
                result += ' '
                result += result_no_spaces[i]
            else:
                result += result_no_spaces[i]
    else:
        result = result_no_spaces
    return result

def decode(ciphered_text):
    ciphered_text = ciphered_text.lower().replace(' ', '')
    temp_text = ''
    for char in ciphered_text:
        if char in plain_alphabet or char in numbers:
            temp_text += char
        else:
            temp_text += ''    
    result = ''
    for char in temp_text:
        if char in plain_alphabet:
            found_index = reversed_alphabet.index(char)
            result += plain_alphabet[found_index]
        else:
            result += char   
    return result

