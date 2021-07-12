'''Input :
N = 9
Output:
2
Explanation:
1 and 4 are the only Perfect Squares
less than 9. So, the Output is 2.'''
import math
def fun(N):
    n=int(math.sqrt(N))
    if n*n==N:
        return n-1
    return n

if __name__=='__main__':
    N=81
    print(fun(N))
