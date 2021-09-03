def maxProfit(prices):
    lsf=prices[0]
    maxProfit=0
    for price in prices:
        if lsf>price:
            lsf=price
        maxProfit=max(maxProfit,price-lsf)
    return maxProfit
print(maxProfit([1,3,6,4,5,2,9]))
