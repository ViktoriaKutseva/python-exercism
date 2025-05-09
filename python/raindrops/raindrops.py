def convert(number):
    result = ''
    if number  % 3 == 0:
        result += 'Pling'
    if number % 5 == 0:
        result += 'Plang'
    if number % 7 == 0:
        result += 'Plong'    
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        result += str(number)     
    return result
    
print(convert(28))
print(convert(30))
print(convert(34))
print(convert(7))
print(convert(35))