# def roman(number):
#     roman_number_dict = {1: 'I', 4: 'IV', 5: 'V', 
#                          9: 'IX', 10: 'X', 40: 'XL',
#                          50: 'L', 90: 'XC', 100: 'C', 
#                          400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
#     division_numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     result = ''
#     count = 0
#     while number != 0: 
#         while number >= division_numbers[count]:
#             result += roman_number_dict[division_numbers[count]] 
#             number -= division_numbers[count]     
#         count += 1    
#     return result

def roman(number):
    roman_number_dict = {1: 'I', 4: 'IV', 5: 'V', 
                         9: 'IX', 10: 'X', 40: 'XL',
                         50: 'L', 90: 'XC', 100: 'C', 
                         400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    result = ''
    for value in sorted(roman_number_dict.keys(), reverse=True):
        while number >= value:
            result += roman_number_dict[value]
            number -= value
    return result

