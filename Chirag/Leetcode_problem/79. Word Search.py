class Solution:
    
    def exist(self,board, word):
        self.board=board
        self.word=word
        self.m=len(board)
        self.n=len(board[0])
        self.l=len(word)
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j]==self.word[0] and self.dfs(i,j,0):
                    return True
        return False
    def dfs(self,i,j,count):
        
        
        if count==self.l:
            return True
        if not 0<=i<self.m or not 0<=j<self.n or self.word[count]!= self.board[i][j]:
            return False
        #temp=board[i][j]
        self.board[i][j]="-1"
        check = (self.dfs(i+1,j,count+1) or self.dfs(i-1,j,count+1)
                    or self.dfs(i,j+1,count+1) or self.dfs(i,j-1,count+1))
        self.board[i][j]=self.word[count]
        return check
A=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
obj=Solution()
print(obj.exist(A,"ABCCSC"))

