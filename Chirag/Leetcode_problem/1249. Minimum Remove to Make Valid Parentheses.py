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
def minRemoveToMakeValid1(s):
    op_count=0
    total=0
    for i in range(len(s)):
        if s[i]=='(':
            op_count+=1
            total+=1
        elif s[i]==')':
            if not op_count:
                s=s[:i]+'#'+s[i+1:]
            else:
                op_count-=1
    opening=total-op_count
    res=''
    for i in range(len(s)):
        if s[i]=='#':
            continue
        elif s[i]=='(':
            if opening:
                opening-=1
                res+=s[i]
        else:
            res+=s[i]
    return res
print(minRemoveToMakeValid('abcd(((efg)h)))'))
print(minRemoveToMakeValid1('abcd(((efg)h)))'))
