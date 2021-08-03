def subset(A):
    result=[]
    subset=[]
    def dfs(i):
        if i>=len(A):
            result.append(subset[:])
            return
        
        subset.append(A[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)
    dfs(0)
    return result
A=[1,2,3]
print(subset(A))
