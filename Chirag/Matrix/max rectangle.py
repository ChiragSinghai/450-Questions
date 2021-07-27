def maxArea(row,n):
    hstack=[]
    pstack=[]
    maxarea=0
    row.append(0)
    n=n+1
    for i in range(n):
        lastwidth=n*n
        while hstack and hstack[-1]>row[i]:
            lastwidth = pstack[-1]
            maxarea=max(maxarea,(i-pstack.pop())*hstack.pop())
        if not hstack or hstack[-1]<row[i]:
            hstack.append(row[i])
            pstack.append(min(lastwidth,i))
    return maxarea

def getmax(mat):
    n=len(mat)
    m=len(mat[0])
    area=0
    for i in range(n):
        for j in range(m):
            if i != 0:
                pass
                
        
        


if __name__=='__main__':
    A=[[1,0,1,0,0],
       [1,0,1,1,1],
       [1,1,1,1,1],
       [1,0,0,1,0]]
    print(maxArea(A[2]))
