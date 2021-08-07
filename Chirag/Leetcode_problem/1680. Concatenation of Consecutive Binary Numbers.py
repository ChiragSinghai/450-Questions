def concatenatedBinary(n) :
    modulo=10**9+7
    s=''
    for i in range(1,n+1):
        s+=bin(i)[2:]
    return int(s,2)%modulo
print(concatenatedBinary(45))
