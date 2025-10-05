def egg_count(display_value):
    result = []
    count = 0
    if display_value == 0:
        return 0
    while display_value > 2:
        n = display_value - (display_value//2)*2       
        display_value = display_value//2 
        result.append(n)
    for i in result:
        if i == 1:
            count +=1
        else:
            count += 0
    return count + 1
