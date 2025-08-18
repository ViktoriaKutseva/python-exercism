def append(list1, list2):
    result = list1 + list2
    return result


def concat(lists):
    result = []
    for item in lists:
        if item:
            result += item
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result += [item]
    return result


def length(list):
    count = 0
    for _ in list: 
        count = count + 1
    return count


def map(function, list):
    result = []
    for item in list:
        item = function(item)
        result += [item]
    return result


def foldl(function, list, initial):
    if not list:
        return initial
    result = function(initial, list[0])

    for item in list[1:]:
        result = function(result, item)
    return result


def foldr(function, list, initial):
    if not list:
        return initial
    result = function(initial, list[-1])
    list = list[::-1]
    for item in list[1:]:
        result = function(result, item)
    return result


def reverse(list):
    result = list[::-1]
    return result
