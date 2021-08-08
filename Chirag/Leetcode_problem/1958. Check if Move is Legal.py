def checkMove(board, r, c, color):
    for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1):
        i, j = r + dr, c + dc
        size = 2
        while 8 > i >= 0 <= j < 8:
            if board[i][j] == '.'or size < 3 and board[i][j] == color:
                break 
            if board[i][j] == color:
                return True    
            i += dr
            j += dc
            size += 1
    return False


board = [[".",".",".",".",".",".",".","."],
         [".","B",".",".","W",".",".","."],
         [".",".","W",".",".",".",".","."],
         [".",".",".","W","B",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".","B","W",".","."],
         [".",".",".",".",".",".","W","."],
         [".",".",".",".",".",".",".","B"]]
rMove = 4
cMove = 4
color = "W"
print(checkMove(board,rMove,cMove,color))
        
