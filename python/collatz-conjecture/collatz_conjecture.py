def steps(number):
    count = 0
        
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number != 1: 
            count += 1
            if number % 2 == 0:
                number = number / 2 
            else:
                number = number * 3 + 1
        return count

print(steps(12))