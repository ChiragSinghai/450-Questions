class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
    def insert(self,word):
        temp=self
        for w in word:
            if w not in temp.children:
                temp.children[w]=TrieNode()
            temp=temp.children[w]
        temp.isEnd=True

class Solution:
    def findWords(self, board,words) :
        self.m=len(board)
        self.n=len(board[0])
        visit=set()
        res=set()
        root=TrieNode()
        for w in words:
            root.insert(w)
        def dfs(i,j,node,temp):
            
            if i<0 or j<0 or i==self.m or j==self.n or (i,j) in visit or board[i][j] not in node.children:
                return 
            visit.add((i,j))
            node=node.children[board[i][j]]
            temp+=board[i][j]
            if node.isEnd:
                res.add(temp)
            dfs(i+1,j,node,temp)
            dfs(i-1,j,node,temp)
            dfs(i,j+1,node,temp)
            dfs(i,j-1,node,temp)
                
            visit.remove((i,j))
            
        for i in range(self.m):
            for j in range(self.n):
                dfs(i,j,root,'')
                
        return res
                
