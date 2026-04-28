def tick(matrix: list[list]):
    new_matrix = []
    matrix_len = len(matrix) - 1
    if matrix:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                count_cell = 0
                if i > 0 and j > 0 and matrix[i -1][j - 1] == 1:
                    count_cell+= 1
                if i > 0 and matrix[i -1][j] == 1:
                    count_cell += 1
                if i > 0 and j < matrix_len and matrix[i -1][j + 1] == 1:
                    count_cell += 1
                if j > 0 and matrix[i][j - 1] == 1:
                    count_cell += 1
                if j < matrix_len and matrix[i][j+1] == 1:
                    count_cell += 1
                if i < matrix_len and j > 0 and matrix[i +1][j - 1] == 1:
                    count_cell += 1
                if i < matrix_len and matrix[i + 1][j] == 1:
                    count_cell += 1
                if i < matrix_len and j < matrix_len and matrix[i + 1][j + 1] and matrix[i + 1][j + 1] == 1:
                    count_cell += 1      
                if (count_cell == 2 and matrix[i][j] == 1) or (count_cell == 3):
                    new_matrix.append(1)
                else: 
                    new_matrix.append(0) 
        final_matrix = [new_matrix[i:i + len(matrix)] for i in range(0, len(new_matrix), len(matrix))]

        return final_matrix
    else:
        return matrix