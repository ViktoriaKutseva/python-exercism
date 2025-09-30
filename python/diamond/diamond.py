def rows(letter):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    get_index = alphabet.index(letter)        
    temp_string = ''
    result = []
    count = get_index
    odd_numbers = 1
    if get_index == 0:
        result = ['A']
        return result
    for i in range(get_index):
        if i <= get_index:
            if i == 0:
                temp_string += ' ' * count + alphabet[i] + ' '* count
                # result.append(temp_string)
                count -= 1
            else:
                temp_string += '\n' + ' ' * count + alphabet[i] + ' '*odd_numbers + alphabet[i] +  ' ' * count
                # result.append(temp_string)
                odd_numbers += 2
                count -= 1
    reversed_string = '\n' + "".join(reversed(temp_string))
    temp_string += '\n' + ' ' * count + letter + ' '*odd_numbers + letter +  ' ' * count
    temp_string += reversed_string
    result = temp_string.split('\n')
    return result

