def solveNQueens(n):
    #self.n=n
    directions=[[-1,-1],
                     [1,1],
                     [1,-1],
                     [-1,1],
                     [1,0],
                     [0,1],
                     [-1,0],
                     [0,-1]]
    ans=[]
    empty_board=[['.']*n for i in range(n)]
    def isValid(board,i,j):
        #checking diagonally:
        nonlocal empty_board,directions
        for dirs in directions:
            x,y=i+dirs[0],j+dirs[1]
            while 0<=x<n and 0<=y<n:
                if board[x][y]=='Q':
                    return False
                x+=dirs[0]
                y+=dirs[1]
        return True
    def add(board):
        nonlocal ans
        a=[]
        for row in board:
            a.append(''.join(row))
        ans.append(a)
        
    def backtrack(curr_row):
        nonlocal empty_board
        if curr_row>=n:
            return True
        for j in range(n):
            
            if isValid(empty_board,curr_row,j):
                empty_board[curr_row][j]='Q'
                if backtrack(curr_row+1):
                    if curr_row==n-1:
                        add(empty_board)
                        #self.empty_board=[['.']*n for i in range(n)]
                empty_board[curr_row][j]='.'
        return False
        
    backtrack(0)
    return ans

def solveNQueens1(n):
    
    xysum, yxdiff, boardset = set(), set(), set()
    board, ans = [], []
            
    def dfs():
        
        nonlocal board, ans
        
        if len(board) == n:
            ans += [board[::][::]]
            return
        
        r = len(board)
        left = ''
        for c in range(n):
            if c not in boardset and r+c not in xysum and c-r not in yxdiff:
                xysum.add(r+c)
                yxdiff.add(c-r)
                boardset.add(c)
                board += [left + 'Q'+'.'*(n-len(left)-1)]
                dfs()
                board.pop()
                xysum.remove(r+c)
                yxdiff.remove(c-r)
                boardset.remove(c)
            left += '.'
    dfs()
    return ans

print(solveNQueens1(5))
