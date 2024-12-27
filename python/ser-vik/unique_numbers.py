list_1 = [1, 4, 6 ,345, 678, 234]
list_2 = [1, 4, 678, 234, 33, 234, 1212]

def find_unique_values(list_1: list, list_2: list) -> list:
    unique_list = []
    for value in list_1:
        if value not in unique_list:
            unique_list.append(value)
    for value_2 in list_2:
        if value_2 not in unique_list:
            unique_list.append(value_2)
    return unique_list
print(find_unique_values(list_1, list_2))
list_1.extend(list_2)
unique_list = list(set(list_1))
print(unique_list)
