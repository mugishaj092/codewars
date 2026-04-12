def is_solved(board):
    for i in range(len(board)):
        if board[i][0] != 0 and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return board[i][0]
        
        if board[0][i] != 0 and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i]
        
    if board[0][0] != 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
​
    if board[0][2] != 0 and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
​
    for row in board:
        if 0 in row:
            return -1
        
    return 0