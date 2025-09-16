def decode(string):
    result = ''
    numbers = '0123456789'
    temp_multiplier = ''
    for char in string:
        if char in numbers:
            temp_multiplier += char
        else:
            if temp_multiplier == '':
                result += 1 * char
            else:
                result += int(temp_multiplier) * char
            temp_multiplier = ''
    return result


def encode(string):   
    n = 0 
    i = 0
    result = ''
    temp_string = ''

    if string:
        while len(string) > i:
            if string[i] in string[n]:
                temp_string += string[i]
                i += 1
            else:
                i = 0
                if len(temp_string) == 1:
                    result += string[i]
                else:
                    result += str(len(temp_string)) + string[i]
                string = string[len(temp_string):]
                temp_string = ''
        if len(temp_string) == 1:
            result += string[0]
        else:
            result += str(len(temp_string)) + string[0]
    return result

        