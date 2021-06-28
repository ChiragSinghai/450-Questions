def requiredPainters(A,mid):
    painter=1
    s=0
    for i in A:
        s+=i
        if s>mid:
            painter+=1
            s=i
    return painter
        
def minTime(A,m):
    totaltime=0
    k=0
    for i in A:
        k=max(k,i)
        totaltime+=i
    high=totaltime
    low=k
    while low<high:
        mid=(low+high)//2
        print(high,low,mid)

        painter=requiredPainters(A,mid)
        print(painter)
        if painter>m:
            low=mid+1
        else:
            high=mid
    
    print(low)
     
if __name__=='__main__':
    A=[10, 20, 60, 50, 30, 40 ]
    m=3
    minTime(A,m)
