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
    var=0
    while mi<mx:
        mid=(ma-mi)//2
        for i in range(r):
            j=bisect(M[i],mid)
            var=var+j
        if var<target:
            mi=mid+1
        else:
            mx=mid
    print(mi)



        
            
