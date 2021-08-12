def minRemoveToMakeValid(s):
    counter=0
    op_count=0
    stack=[]
    res=''
    for i in range(len(s)):
        if s[i]==')':
            if op_count:
                res+=s[i]
                op_count-=1
                stack.pop(0)
            else:
                counter+=1
        elif s[i]=='(':
            op_count+=1
            res+=s[i]
            stack.append(i-counter)
        else:
            res+=s[i]
    #print(res,op_count)
    counter=0
    while op_count:
        index=stack.pop(0)
        print(index)
        res=res[:index-counter]+res[index+1-counter:]
        op_count-=1
        counter+=1
    return res
print(minRemoveToMakeValid('abcd(((efg)h)))'))
