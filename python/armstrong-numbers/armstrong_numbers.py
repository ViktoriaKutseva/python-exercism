def is_armstrong_number(number):
    number_length = len(str(number))
    number = str(number)
    final_number = 0
    
    for digit in range(number_length):
        armstrong_number = (int(number[digit])) ** number_length
        final_number +=armstrong_number  
    
    if int(number) == final_number:
        return True
    return False