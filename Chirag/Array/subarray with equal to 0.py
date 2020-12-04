def brute_force(A,n):
    for i in range(n):
        s=A[i]
        for j in range(i+1,n):
            if s==0:
                return 1
            s+=A[j]
    return 0
def optimal_solution(A,n):
    S=set()
    total=0
    for i in A:
        total+=i
        if total==0 or total in S:
            print(S)
            return 1
        S.add(total)
    return 0
if __name__=='__main__':
    A=[4,2,-3,1,6]
    
    n=5
    print("Yes" if brute_force(A,n) else "No")
    print("Yes" if optimal_solution(A,n) else "No")        
            
