#the code at the official site is implemented wrong
#
def fun(prices):
    mi=ma=prices[0]
    maximum=0
    for i in prices:
        if mi>i:
            maximum=max(maximum,ma-mi)
            mi=ma=i
        if ma<i:
            ma=i
    print(maximum)

if __name__=='__main__':
    #A=[7,1,5,3,6,4]
    arr=list(map(int,input().split()))
    fun(arr)
