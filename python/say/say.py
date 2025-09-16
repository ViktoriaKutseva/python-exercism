def is_int(n):
    numbers = '0123456789'

    return True if n in numbers else False

def say_block(n):
    number_dict = {
        '0': '',
        '1': "one",
        '2': "two",
        '3': "three",
        '4': "four",
        '5': "five",
        '6': "six",
        '7': "seven",
        '8': "eight",
        '9': "nine",
        '10': "ten",
        '11': "eleven",
        '12': "twelve",
        '13': "thirteen",
        '14': "fourteen",
        '15': "fifteen",
        '16': "sixteen",
        '17': "seventeen",
        '18': "eighteen",
        '19': "nineteen",
        '20': "twenty",
        '30': "thirty",
        '40': "forty",
        '50': "fifty",
        '60': "sixty",
        '70': "seventy",
        '80': "eighty",
        '90': "ninety",
        '100': "hundred",
    }    
    temp_number = ''
    result = ''
    n = int(n)
    while n != 0:
        if n > 99:
            result += number_dict[str(n)[0]] + ' '
            result += number_dict['100'] + ' '
            n = int(str(n)[1:])
        if n > 19:
            temp_number += (str(n)[0]) + '0'
            result += number_dict[temp_number]
            if str(n)[1] != '0':
                result += '-' + number_dict[str(n)[1]]
            else:
                result += ''
                # result += number_dict[str(n)]
            n -= n
        elif n < 20:
            result += number_dict[str(n)]    
            n -= n
    return result


def say(number):
    if not is_int(number):
        raise ValueError('nahui idi')
    divisions_dict = {0: '', 1: 'thousand', 2: 'million', 3: 'billion'}
    result = ''
    list_of_hundreds = []
    if number < 0 or number > 999999999999:
        raise ValueError('input out of range')
    elif number == 0:
        return 'zero'
    elif number < 1000:
        result += say_block(number)
    elif number > 999:
        while len(str(number)) > 3:
            list_of_hundreds.append(str(number)[-3:])
            number = int(str(number)[:-3])
        list_of_hundreds.append(str(number))
        list_of_hundreds.reverse()
        print(list_of_hundreds)
        

    count = len(list_of_hundreds) - 1
    for i in range(len(list_of_hundreds)):
        result += say_block(((list_of_hundreds))[i])+ ' '
        if list_of_hundreds[i] == '000':
            result += ''
        else: 
            result +=  divisions_dict[count] + ' '
        count -= 1
    result = result.lstrip().rstrip()
    return result

print(say(100000000))
