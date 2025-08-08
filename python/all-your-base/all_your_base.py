def rebase(input_base, digits: list, output_base):

    if input_base < 2:
        raise ValueError('input base must be >= 2')
    
    if output_base < 2:
        raise ValueError('output base must be >= 2')    
    
    for i in range(len(digits)):
        print(digits[i])
        if not input_base > digits[i] >= 0:
            raise ValueError('all digits must satisfy 0 <= d < input base')
    
    len_of_number = len(digits)
    result_in_10_base = 0
    for i in range(len_of_number):
        print(digits[i])
        result_in_10_base += digits[i] * input_base ** (len_of_number - 1)
        len_of_number = len_of_number - 1 
    result = []
    n = 0

    while result_in_10_base >= output_base:
        n =result_in_10_base - (result_in_10_base//output_base)*output_base
        print(n)
        result.append(n)
        result_in_10_base = result_in_10_base//output_base
    result.append(result_in_10_base)
    result.reverse()
    return result


