def totalNQueens(n):
    count=0
        ldiag=set()
        rdiag=set()
        col=set()
        def back(r):
            nonlocal count
            if r==n:
                count+=1
            for c in range(n):
                if c in col or r-c in ldiag or r+c in rdiag:
                    continue
                else:
                    ldiag.add(r-c)
                    rdiag.add(r+c)
                    col.add(c)
                    back(r+1)
                    ldiag.remove(r-c)
                    rdiag.remove(r+c)
                    col.remove(c)
        back(0)
        return count

    '''
    if n==1:
        return 1

    if n==2 or n==3:return 0
    if n==4:return 2
    if n==5:return 10
    if n==6:return 4
    if n==7:return 40
    if n==8: return 92
    if n==9:return 352
    '''
    
    '''
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
    return len(ans)
        '''

print(totalNQueens(4))
