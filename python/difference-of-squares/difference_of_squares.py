def square_of_sum(number):
    res = 0
    for i in range(number + 1):
        res += i
    return res**2
    
def sum_of_squares(number):
    res = 0
    for i in range(number + 1):
        res += i**2
    return res

def difference_of_squares(number):   
    x = square_of_sum(number)
    y = sum_of_squares(number)
    res = x - y
    return res
