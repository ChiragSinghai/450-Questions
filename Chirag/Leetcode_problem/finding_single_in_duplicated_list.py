def find(A):
    xor_value=0
    for i in A:
        xor_value=xor_value^i
    print(xor_value)
        
        
    
if __name__=='__main__':
    A=[2,3,4,5,6,25,6,5,4,3,2]
    find(A)
