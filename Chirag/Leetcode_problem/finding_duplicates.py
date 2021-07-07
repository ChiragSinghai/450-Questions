def find(A):
    xor_value=0
    for i in A:
        xor_value=xor_value^i
    print(bin(xor_value))
    i=0
    while True:
        bit=1<<i
        if bit&xor_value:
            break
        i+=1
    ans=[0,0]
    
    for n in A:
        if bit & n :
            ans[1]^=n
        else:
            ans[0]^=n
    print(ans)
        
        
    
if __name__=='__main__':
    A=[2,3,4,5,6,25,6,5,4,3,2,7]
    find(A)
