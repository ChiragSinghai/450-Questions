def partition5(A,n,k):
    start=0
    end=n-1
    count=0
    index=-1
    subcount=0
    for i in A:
        if i<=k:
            count+=1
            subcount+=1
        else:
            count=0
        index=max(index,count)
    print(subcount-count)
        
            
    
    

if __name__=='__main__':
    n=int(input())
    A=list(map(int,input().split()))
    k=int(input())
    partition5(A,n,k)
