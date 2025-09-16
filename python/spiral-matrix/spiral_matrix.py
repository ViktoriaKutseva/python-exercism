def spiral_matrix(size):
    result = []
    amount = size*size
    for i in range(amount):
        result.append(i+1)
    return result
    

print(spiral_matrix(2))