def spiral(L):
    r=len(L)
    if r==0:
        return 0
    c=len(L[0])
    row=column=0
    while row<r and column<c:
        for i in range(column,c):
            print(L[row][i],end=' ')
        row+=1
        for i in range(row,r):
            print(L[i][c-1],end=' ')
        c-=1
        if row<r:
            for i in range(c-1,column-1,-1):
                print(L[r-1][i],end=' ')
            r-=1
        if column<c:
            for i in range(r-1,row-1,-1):
                print(L[i][column],end=' ')
            column+=1
            
if __name__=='__main__':
    L=[[1,2,3,4,5],
       [14,15,16,17,6],
       [13,20,19,18,7]]
       #[12,11,10,9,8]]
       
    spiral(L)
