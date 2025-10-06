def _find_highest_coordinates (matrix):
    highest_coordinates = []
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][col] == max(matrix[row]):
                highest_coordinates.append([row + 1, col + 1])
            else:
                continue
    return highest_coordinates

def _find_lowest_coordinates(matrix):
    col_list = []
    col_line = []
    for col in range(len(matrix[0])) :
        col_line = []
        for row in range(len(matrix)):
            s = matrix
            col_line.append(s[row][col])
        col_list.append(col_line)
    lowest_coordinates = []
    for col in range(len(col_list[0])):
        for row in range(len(col_list)):
            if col_list[row][col] == min(col_list[row]):
                lowest_coordinates.append([col + 1, row + 1])
            else:
                continue
    return lowest_coordinates

def saddle_points(matrix):
    coordinates = []
    if matrix:
        row_lenght = len(matrix[0])
        for row in matrix:
            if len(row) == row_lenght:
                continue
            else:
                raise ValueError("irregular matrix")
        high = _find_highest_coordinates(matrix)
        low = _find_lowest_coordinates(matrix)
        for i in high:
            if i in low:
                dict_coordinate = {'row': i[0], 'column': i[1]}
                coordinates.append(dict_coordinate)
            else:
                coordinates = coordinates
    return coordinates
