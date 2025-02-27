def rows(letter):
    n = ord(letter) - ord('A') + 1  # Position of the letter, 'A' is 1, 'B' is 2, etc.
    
    result = []
    
    for i in range(n):
        spaces = '·' * (n - i - 1)
        
        letter_part = chr(ord('A') + i)
        
        if i == 0:
            result.append(spaces + letter_part + spaces)
        else:
            middle_spaces = '·' * (2 * i - 1)
            result.append(spaces + letter_part + middle_spaces + letter_part + spaces)
    
    result += result[:-1][::-1]
    
    for line in result:
        print(line)
    return result
        
print(rows('D'))