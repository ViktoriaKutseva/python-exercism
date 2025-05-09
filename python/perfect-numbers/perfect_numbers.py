def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    number_sum = 0
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    for digit in range(1,number):
        if number % digit == 0:
            number_sum += digit

    if number_sum == number:
        return 'perfect'
    if number_sum > number:
        return 'abundant'
    if number_sum < number:
        return 'deficient'
    