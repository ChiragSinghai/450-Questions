for _ in range(int(input())):
    n=int(input())
    c=list(map(int,input().split()))
    s=int(input())
    c.sort()
    mi=c[-1]
    i=0
    j=s-1
    while j<n:
        mi=min(mi,c[j]-c[i])
        i+=1
        j+=1
    print(mi)
    
