def numIslands(grid):
    if not grid:
        return 0
    islands=0
    rows,cols=len(grid),len(grid[0])
    
    def bfs(row,col):
        directions=[[1,0],[-1,0],[0,-1],[0,1]]
        queue=[]
        queue.append((row,col))
       
        while queue:
            row,col = queue.pop(0)
            for x,y in directions:
                x=row+x
                y=col+y
                if 0<=x<rows  and 0<=y<cols:
                    if grid[x][y]=="1":
                        grid[x][y]="0"
                        queue.append((x,y))
        
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]=="1":
                bfs(i,j)
                islands+=1
    return islands

A=[["1","1","1","1","0"],
   ["1","1","0","1","0"],
   ["1","1","0","0","0"],
   ["0","0","0","0","1"]]
print(numIslands(A))
