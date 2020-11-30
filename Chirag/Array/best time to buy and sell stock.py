def fun(prices):
    mi=ma=prices[0]
    for i in prices:
        if mi>i:
            mi=i
        else:
            if i>ma:
                ma=i
    print(ma-mi if ma-mi>0 else 0)
if __name__=='__main__':
    fun([7,1,5,3,6,4])
