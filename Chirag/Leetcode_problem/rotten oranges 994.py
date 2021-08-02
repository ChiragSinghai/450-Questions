
def orangesRotting(grid):
    queue=[]
    m=len(grid)
    n=len(grid[0])
    counter = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==2:
                queue.append([i,j,0])
            elif grid[i][j]==0:
                counter+=1

    maxtime=0
    if counter==m*n:
        return maxtime
    if not queue:
        return -1
    while queue:
        i,j,t = queue.pop(0)
        maxtime = max(maxtime,t)
        if i+1<m and grid[i+1][j] == 1:
            grid[i+1][j] = 2
            queue.append([i+1,j,t+1])
        if i-1>=0 and grid[i-1][j] == 1:
            grid[i-1][j] = 2
            queue.append([i-1,j,t+1])
        if j+1<n and grid[i][j+1] == 1:
            grid[i][j+1] = 2
            queue.append([i,j+1,t+1])
        if j-1>=0 and grid[i][j-1] == 1:
            grid[i][j-1] = 2
            queue.append([i,j-1,t+1])
            
    for i in range(m):
        if 1 in grid[i]:
            return -1
    return maxtime

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
                        
