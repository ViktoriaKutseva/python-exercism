def find(search_list: list, value):
    search_list = sorted(search_list)
    list_length = len(search_list)
    if value not in search_list:
        raise ValueError("value not in array")

    if list_length % 2 == 0:
        digit = list_length // 2 - 1
    else:
        digit = list_length // 2

    for _ in search_list:
        if search_list[digit] == value:
            return digit
        elif search_list[digit] > value:
            digit -= digit // 2 + 1
        elif search_list[digit] < value:
            digit += digit // 2
