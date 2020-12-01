def bruteforceApproach(A,n,s):
    count=0
    for i in range(n):
        j=i+1
        while j<n:
            if A[i]+A[j]==s:
                count+=1
            j+=1
    print(count)
#i dont understand this solution but because I found array of 1000 digits for
#small arrays is quite non optimal
def optimalSolution(A,n,s):
    B=[0]*1000
    for i in A:
        B[i]+=1
    count=0
    for i in A:
        count+=B[s-i]
        if (s - i ==i):
            twice_count-=1
        
    print(count//2)
if __name__=='__main__':
    N=int(input())
    A=list(map(int,input().split()))
    S=int(input())
    bruteforceApproach(A,N,S)
    optimalSolution(A,N,S)
        
