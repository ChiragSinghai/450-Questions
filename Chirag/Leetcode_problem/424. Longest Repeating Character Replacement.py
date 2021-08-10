def characterReplacement(s, k) :
    D={}
    l=0
    res=0
    maxf=0
    for r in range(len(s)):
        D[s[r]]=1+D.get(s[r],0)
        maxf=max(maxf,D[s[r]])
        if (r-l+1)-maxf>k:
            D[s[l]]-=1
            l+=1
        res=max(res,r-l+1)
    return res

def characterReplacement1(s, k) :
    D={}
    l=0
    res=0
    for r in range(len(s)):
        D[s[r]]=1+D.get(s[r],0)
        
        if (r-l+1)-max(D.values())>k:
            D[s[l]]-=1
            l+=1
        res=max(res,r-l+1)
    return res
print(characterReplacement('ABABAAA',2))
print(characterReplacement1('ABABAAA',2))
