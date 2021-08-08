import math
def numPrimeArrangements(n):
    def getPrime(n):
        prime=0
        for i in range(2,n+1):
            flag=True
            for j in range(2,int(math.sqrt(n))+1):
                if i%j==0 and i!=j:
                    flag = False
            if flag:
                prime+=1
        return prime,n-prime
    def fact(n):
        if n<=1:
            return 1
        return n*fact(n-1)
    a,b=getPrime(n)
    return (fact(a)*fact(b))%(10**9+7)
print(numPrimeArrangements(10))
