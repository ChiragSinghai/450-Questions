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

def checkMove1(board, rMove, cMove, color):
        directions=[[1,0],[-1,0],
                    [0,1],[0,-1],
                    [-1,-1],[1,1],
                    [-1,1],[1,-1]]
        board[rMove][cMove]=color
        def check(i,j,c,d):
            dr,dc=d
            row,col=i+dr,j+dc
            length=1
            while (0<=row<8) and 0<=col<8:
                length+=1
                if board[row][col]=='.':return False
                elif board[row][col]==c:return length>=3
                row+=dr
                col+=dc
            return False
        for d in directions:
            if check(rMove,cMove,color,d):
                return True
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
        
