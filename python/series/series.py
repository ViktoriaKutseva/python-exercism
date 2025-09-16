def slices(series, length):
    if series == '':
        raise ValueError( "series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")    
    if length == 0:
        raise ValueError ("slice length cannot be zero")      
    if length < 0:
        raise ValueError("slice length cannot be negative")

    result = []
    while len(series) != length or len(series) > length:
        result.append(series[:length])
        series = series[1:]
    result.append(series)
    return result

# print(slices("", 5))