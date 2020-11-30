def bruteforceApproach(A,n,s):
    count=0
    for i in range(n):
        j=i+1
        while j<n:
            if A[i]+A[j]==s:
                count+=1
            j+=1
    print(count)

if __name__=='__main__':
    N=int(input())
    A=list(map(int,input().split()))
    S=int(input())
    bruteforceApproach(A,N,S)
        
