def primes(limit):
    prime_numbers = []
    marked_numbers = []
    multiplier = 2
    for i in range(2,limit + 1):
        while i * multiplier <= limit:
            marked = i * multiplier
            marked_numbers.append(marked)
            multiplier += 1
        multiplier = 2
    for i in range(2, limit + 1):
        if i not in marked_numbers:
            prime_numbers.append(i)
    return prime_numbers
