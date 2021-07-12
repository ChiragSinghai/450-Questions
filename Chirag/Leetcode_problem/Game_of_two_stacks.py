def score(S1,S2,X):
    total=i=j=0
    while i<len(S1) and total+S1[i]<=X:
        total+=S1[i]
        i+=1
    ans=i
    print(total,ans)
    for item in S2:
        total+=item
        j+=1
        while total>X and i>0:
            i-=1
            total-=S1[i]
            
        if total-X<=0:
            ans=max(ans,i+j)
    return ans


if __name__=='__main__':
    g = int(input().strip())
    for a0 in range(g):
        n,m,x = input().split()
        n,m,x = [int(n),int(m),int(x)]
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        #stack1=[4,2,4,6,1]
        #stack2=[2,1,8,5]
        print(score(a,b,x))
    
