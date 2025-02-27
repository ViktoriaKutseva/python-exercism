def square(number):
    if number > 64 or number <= 0:
        raise ValueError("square must be between 1 and 64")
    else:
        result = 2 ** (number - 1)
    return result

def total():
    total_grains = 0 
    for grain in range(1, 65):
        total_grains += 2 ** (grain - 1)
    return int(total_grains)

# print(square(5)) 
# print(total())

