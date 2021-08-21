def minWindow(s, t):
        res=float("infinity")
        D={}
        window={}
        for i in t:
            D[i]=D.get(i,0)+1
        #print(D)
        string=[-1,-1]
        have=0
        need=len(D)
        l=0
        for r in range(len(s)):
            char=s[r]
            window[char]=window.get(char,0)+1
            if char in D and D[char]==window[char]:
                have+=1
            while have==need:
                if r-l+1<res:
                    string=[l,r]
                    res=r-l+1
                window[s[l]]-=1
                if s[l] in D and window[s[l]]<D[s[l]]:
                    have-=1
                l+=1
        l,r=string
        return s[l:r+1] if res!=float("infinity") else ""
print(minWindow("ABDAEBCNANBC","ABC"))
    
