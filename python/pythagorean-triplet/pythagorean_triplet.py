def triplets_with_sum(number):
    all_possible_sets = []
    single_set = []
    for i in range(1,number//3 + 1):
        j = (number * (number - 2 * i)) // (2 * (number - i))
        if j < i:
            continue
        k = number - i - j 
        if pow(i, 2) + pow(j, 2) == pow(k, 2) and i + j + k == number and i < j < k:
            single_set.append(i)
            single_set.append(j)
            single_set.append(k)
            all_possible_sets.append(single_set)
        single_set = []
    return all_possible_sets
