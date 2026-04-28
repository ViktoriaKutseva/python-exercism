def gamestate(board):
    # return board[2][1]
    x_count = 0
    o_count = 0
    for row in range(3):
        for column in range(3):
            if board[row][column] == 'X':
                x_count += 1
            if board[row][column] == 'O':
                o_count += 1
            else:
                continue
    uninterrupted = 0 
    win_count = 0
    if (x_count >= o_count) or (o_count == (x_count - 1)):
        for row in range(3):
            for column in range(3):
                first_value = board[row][0]   
                if first_value == board[row][column] and (board[row][column] == 'X' or board[row][column] == 'O'):
                    uninterrupted += 1
            if uninterrupted == 3:
                win_count += 1
                uninterrupted = 0
            else:
                uninterrupted = 0
        for column in range(3):
            for row in range(3):
                first_value = board[0][column] 
                if first_value == board[row][column] and (board[row][column] == 'X' or board[row][column] == 'O'):
                    uninterrupted += 1
            if uninterrupted == 3:
                win_count += 1
                uninterrupted = 0
            else:
                uninterrupted = 0
        for row in range(3):
            first_value = board[0][0] 
            if first_value == board[row][row] and (board[row][row] == 'X' or board[row][row] == 'O'):
                uninterrupted += 1
        if uninterrupted == 3:
            win_count += 1
            uninterrupted = 0
        else:
            uninterrupted = 0
        diagonal = [2, 1, 0]
        for row, column in enumerate(diagonal):
            first_value = board[0][2] 
            if first_value == board[row][column] and (board[row][column] == 'X' or board[row][column] == 'O'):
                uninterrupted += 1
        if uninterrupted == 3:
            win_count += 1
            uninterrupted = 0
        else:
            uninterrupted = 0
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    if x_count != o_count and o_count != (x_count -1):
        raise ValueError("Wrong turn order: X went twice")
    if win_count == 2 and x_count == o_count:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if win_count == 1:
        return ("win")
    if win_count == 2 and x_count == o_count + 1:
        return ("win")
    if win_count == 0:
        return ("ongoing")
    if win_count == 0 and x_count == o_count + 1:
        return('draw')


