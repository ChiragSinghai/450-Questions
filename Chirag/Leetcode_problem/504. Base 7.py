def convertToBase7(num) :
    if num == 0:
        return "0"
    
    stack = []
    flag = 0
    
    if num < 0:
        flag = 1
        num = abs(num)
    
    while num > 0:
        stack.append(str(num % 7))
        num //= 7
        
    if flag == 1:
        stack.append('-')
        
    return ''.join(stack[::-1])
print(convertToBase7(100))
