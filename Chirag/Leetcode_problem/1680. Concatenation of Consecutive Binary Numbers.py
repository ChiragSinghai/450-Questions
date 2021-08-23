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
        print(num)
        ans=ans<<num
        print(bin(ans))
        ans|=i
        ans%=modulo
    return ans

print(concatenatedBinary1(2))
