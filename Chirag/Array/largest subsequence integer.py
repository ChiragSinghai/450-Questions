def findSub(A,n):
    A.sort()
    l=[]
    count=1
    ans=0
    for i in range(1,n):
        if A[i]==A[i-1]-1 or A[i]==A[i-1]:
            count+=1
        else:
            count=1
        ans = max(ans, count)
    print(count)
if __name__=='__main__':
    findSub([6,2,7,3,4,5,31,31,5]
