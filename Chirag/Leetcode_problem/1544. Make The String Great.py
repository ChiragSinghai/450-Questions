def makeGood(s):
    List=list(s)
    l=0
    r=len(s)-1
    while l<=r:
        if List[l].isupper():
            if l and List[l-1]==List[l].lower():
                List.pop(l)
                List.pop(l-1)
                r-=2
                l-=1
            elif l<r and List[l+1]==List[l].lower():
                List.pop(l+1)
                List.pop(l)
                r-=2
            else:
                l+=1
        elif List[l].islower():
            if l and List[l-1]==List[l].upper():
                List.pop(l)
                List.pop(l-1)
                r-=2
                l-=1
            elif l<r and List[l+1]==List[l].upper():
                List.pop(l+1)
                List.pop(l)
                r-=2

            else:
                l+=1
    
        else:
            l+=1
        #print(l,List)
    return ''.join(List)
def makeGood1(s):
    s=list(s)   
    ans=[s.pop()]
    
    while s:
        a= s.pop()
        
        if len(ans)>0:
            
            if (a).lower()==ans[-1].lower() and a!=ans[-1]:
                ans.pop()
            else:
                ans.append(a)
        else:
            ans.append(a)
    
    return ''.join(ans[::-1])
print(makeGood1("WpubBUPwG"))
        
