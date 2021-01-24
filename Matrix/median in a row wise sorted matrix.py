from bisect import bisect
def solution(M,r,c):
    mi=M[0][0]
    ma=0
    for i in range(r):
        if mi>M[i][0]:
            mi=M[i][0]
        else:
            if ma<M[i][c-1]:
                ma=M[i][c-1]

    target=(r*c+1)//2
    
    while mi<ma:
        mid=mi+(ma-mi)//2
        var=0
        print('mid=',mid)
        for i in range(r):
            j=bisect(M[i],mid)
            print(j)
            var=var+j
            
        if var<target:
            mi=mid+1
        else:
            ma=mid
    print(mi)

if __name__=='__main__':
    M=[[5,6,8],
       [2,3,4],
       [0,1,7]]
    r,c=3,3
    solution(M,r,c)



        
            
