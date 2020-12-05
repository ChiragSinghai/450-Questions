def findSub(A,n):
    A.sort()
    l=[]
    count=1
    ans=0
    print(A)
    for i in range(1,n):
        if A[i]==A[i-1]+1 or A[i]==A[i-1]:
            if A[i]==A[i-1]:
                count-=1
            count+=1
        else:
            count=1
        print(count)
        ans = max(ans, count)
    print(ans)
if __name__=='__main__':
    findSub([6,2,7,3,3,4,4,4,4,4,5,31,31,5],14)
