def proverb(*input_data, qualifier=None):
    result = []
    count = 0
    for word in range(len(input_data)):
        if word + 1 != len(input_data):
            result.append(f'For want of a {input_data[count]} the {input_data[count + 1]} was lost.')
            count += 1
        else:
            result.append(f"And all for the want of a {(qualifier + ' ' + input_data[0] if qualifier is not None else input_data[0])}.")
    return result


