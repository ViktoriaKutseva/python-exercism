def sum_of_multiples(limit, multiples):
    set_of_numbers = []
    set_of_unique = []
    for number in multiples:
        n = number
        if limit < number or number == 0:
            set_of_numbers.append(0)
            continue
        while number < limit:
            set_of_numbers.append(number)
            number += n
        set_of_numbers = sorted(set_of_numbers)
    for unique in set_of_numbers:
        if unique not in set_of_unique:
            set_of_unique.append(unique)
    result = sum(set_of_unique)
    return result

