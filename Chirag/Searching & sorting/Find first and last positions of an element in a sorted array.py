'''
Input:
n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  2 5
Explanation: First occurrence of 5 is at index 2 and last
             occurrence of 5 is at index 5. 
'''
def find(A,n,x):
    first_index=last_index=-1
    for i in range(n):
        if A[i]==x:
            if first_index==-1:
                first_index=i
            last_index=i
    print(first_index,last_index)            
                
    
if __name__=='__main__':
    n=9
    x=7
    A=[1, 3, 5, 5, 5, 5, 7, 123, 125]
    find(A,n,x)
