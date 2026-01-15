class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.naked_data = self.matrix_string.split()
        self.column_count = self.matrix_string.count("\n") + 1
        self.row_count = len(self.naked_data) // self.column_count
        self.split_matrix = self.matrix_string.splitlines()


    def row(self, index):
        result = []
        string_row = self.split_matrix[index - 1].split()
        for i in range(len(string_row)):
            result.append(int(string_row[i]))
        return result
        
    def column(self, index):
        result = []
        string_column = self.naked_data[index - 1::self.row_count]
        for i in range(len(string_column)):
          result.append(int(string_column[i]))
        return result