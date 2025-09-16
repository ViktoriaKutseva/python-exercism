def decode(string):
    pass
def encode(string):
    current_char = string[0]
    number = 0
    result = ''
    for char in string:
        if current_char != char:
            result += str(number) + current_char if number > 1 else current_char
            current_char = char
            number = 1
        else:
            number +=1
    result += str(number) + current_char if number > 1 else current_char
    return result
    
        
print(decode("XYZ"))
print(encode("WWBddd"))