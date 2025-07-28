def commands(binary_str):

    list_of_commands = ['wink', 'double blink', 'close your eyes', 'jump']
    result = []
    n = -1

    for digit in range(4):
        if binary_str[n] == '1':
            result.append(list_of_commands[digit])
        n -= 1

    if binary_str[0] == '1':
        result.reverse()
        return result
    return result
