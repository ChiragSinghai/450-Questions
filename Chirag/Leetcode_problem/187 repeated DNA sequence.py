def findRepeatedDnaSequences(s) :
    D={}
    i=0
    
    while i+10<=len(s):
        D[s[i:i+10]]=1+D.get(s[i:i+10],0)
        
        i+=1
    for k in list(D.keys()):
        if D[k]<=1:
            D.pop(k)
    return list(D.keys())
print(findRepeatedDnaSequences("AAAAAAAAAAA"))
