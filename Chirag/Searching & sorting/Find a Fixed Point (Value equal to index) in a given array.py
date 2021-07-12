'''
Input: 
N = 5
Arr[] = {15, 2, 45, 12, 7}
Output: 2
Explanation: Only Arr[2] = 2 exists here.
'''
def getindex(A):
    n=len(A)
    L=[]
    for i in range(n):
        if A[i]==i+1:
            L.append(A[i])
    return L

if __name__=='__main__':
    A=[15, 2, 45, 12, 7]
    print(*getindex(A))
    
