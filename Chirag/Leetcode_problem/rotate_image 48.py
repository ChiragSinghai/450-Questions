def printmat(mat):
    for row in mat:
        print(row)
    print('=======================')
        
def rotate(mat):
    l,r=0,len(mat)-1
    while l<r:
        t=l
        b=r
        for i in range(r-l):
            temp=mat[t][l+i]
            print(temp)
            mat[t][l+i] = mat[b-i][l]
            mat[b-i][l] = mat[b][r-i]
            mat[b][r-i] = mat[t+i][r]
            mat[t+i][r] = temp
            
        l+=1
        r-=1
    printmat(mat)
    


image=[[1,2,3],[4,5,6],[7,8,9]]
rotate(image)
