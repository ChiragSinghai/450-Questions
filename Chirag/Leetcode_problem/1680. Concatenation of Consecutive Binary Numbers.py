import math
def concatenatedBinary(n) :
    modulo=10**9+7
    s=''
    for i in range(1,n+1):
        s+=bin(i)[2:]
    return int(s,2)%modulo

def concatenatedBinary1(n) :
    modulo=10**9+7
    ans = 1 
    #calculate bits
    for i in range(2,n+1):
        num=int(math.log(i)/math.log(2)+1)
        ans=ans<<num
        ans|=i
        ans%=modulo
    return ans
def concatenatedBinary2(n):
    mem = list(accumulate(range(100001), lambda s, i: (s << i.bit_length() | i) % 1000000007))
    return mem[n]
print(concatenatedBinary1(45))
