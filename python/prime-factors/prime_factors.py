import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
    
def factors(value):
    result = []
    number = 2
    if value == 1:
        return result
    while is_prime(value) is False:
        if value % number == 0:
            result.append(number)
            value = value//number
        else:
            number += 1
            while is_prime(number) is False:
                number +=1
    result.append(value)
    return result

