def flatten(iterable):
    # result = []
    # iterable = str(iterable)    
    # iterable = iterable.replace('[', '').replace(']','').replace('None', '')
    # iterable = iterable.split(',')
    # iterable = [line.strip() for line in iterable if line.strip()]

    # for i in iterable:
    #     i = int(i)
    #     result.append(i)
    # return result


    result = []
    for item in iterable:
        if isinstance(item, list):
            result.extend(flatten(item))  # recursion for nested lists
        elif item is not None:
            result.append(item)
    return result