def findNthDigit(n):
    if n < 10:
        return n
    # find the digit of n
    digit = 0
    tmp = 0
    pre = 0
    while tmp < n:
        pre = tmp
        digit += 1
        tmp += (9*(10**(digit-1)))*digit
    # find where it belongs
    n -= pre
    num = 10**(digit-1) + ((n-1)//digit)
    # find the index
    index = (n-1)%digit
    return num//(10**(digit-index-1))%10
print(findNthDigit(190))
