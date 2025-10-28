def _convert_to_patterns(input_grid):
    patterns = []
    for col in range(0, len(input_grid[0]), 3):
        for row in range(len(input_grid)):
            patterns.append(input_grid[row][col:col+3])
    return patterns

def convert(input_grid):
    patterns = {
        (" _ ","| |","|_|", "   "): "0",
        ("   ","  |","  |", "   "): "1",
        (" _ "," _|","|_ ", "   "): "2",
        (" _ "," _|"," _|", "   "): "3",
        ("   ","|_|","  |", "   "): "4",
        (" _ ","|_ "," _|", "   "): "5",
        (" _ ","|_ ","|_|", "   "): "6",
        (" _ ","  |","  |", "   "): "7",
        (" _ ","|_|","|_|", "   "): "8",
        (" _ ","|_|"," _|", "   "): "9",
    }
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")
    result = ''
    result_for_columns = ''
    input_grid_patterns =_convert_to_patterns(input_grid)
    for i in range(0, len(input_grid_patterns), 4):
        key = tuple(input_grid_patterns[i: i+4])
        result += patterns.get(key, '?')
    if len(input_grid) > 4:
        find_iterator_col = len(input_grid)//4
        find_iterator_row = len(input_grid[0])//3
        for n in range(find_iterator_col):
            for i in range(0, len(result), find_iterator_row):
                result_for_columns += result[n + i]  
            if n < find_iterator_col - 1:
                result_for_columns += ','      
            else:
                result_for_columns = result_for_columns
        result = result_for_columns
    return result
        

