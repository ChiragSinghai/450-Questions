def getString(S):
    stack=[]
    i=len(S)
    for i in S:
        stack.append(i)
        if i ==']':
            stack.pop()
            s=''
            while stack:
                if stack[-1] == '[':
                    stack.pop()
                    break
                s=stack.pop()+s
            print(s)
            d=''
            while stack and stack[-1].isdigit():
                k=stack.pop()
                d=k+d
            stack.append(s*int(d))
        print(stack)
    return stack.pop()
                    
if __name__=='__main__':
    S='3[a2[b2[cd]]]'
    print(getString(S))
