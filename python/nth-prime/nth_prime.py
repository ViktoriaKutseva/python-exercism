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


def prime(n):
    if n == 0:
        raise ValueError("there is no zeroth prime")
    prime_list = []
    number = 2
    while n != len(prime_list):
        if is_prime(number):
            prime_list.append(number)
            number += 1
        else:
            number += 1
            while is_prime(number) is False:
                number +=1
    return prime_list[-1]

print(prime(10001))