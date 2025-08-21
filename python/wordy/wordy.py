import operator
def answer(question):
    question = question.replace('by', '').replace('?', '')
    operation_dict = {'plus' : operator.add, 'minus': operator.sub, 'multiplied' : operator.mul, 'divided' : operator.truediv}
    numbers = []
    ops = []
    block_list = question.split()
    block_list = block_list[2:]
    result = 0
    
    for block in block_list[::2]:
        try:
            numbers.append(int(block))
        except ValueError: 
            raise ValueError("syntax error")

    for block in block_list[1::2]:
        if block not in operation_dict:
            if block.isdigit(): 
                raise ValueError("syntax error")            
            raise ValueError("unknown operation")
        ops.append(operation_dict[block])

    if len(numbers) - len(ops) != 1:
        raise ValueError("syntax error")
    
    result = numbers[0]
    for op, number in zip(ops, numbers[1:]):
        print(op,number)
        result = op(result, number)
    return result
