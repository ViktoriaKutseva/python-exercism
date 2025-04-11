def square_root(number):
    n = 1
    result = 1
    while result != number:
       n += 1
       result = n * n
    return n 

print(square_root(9))
print(square_root(65025))
print(square_root(1))