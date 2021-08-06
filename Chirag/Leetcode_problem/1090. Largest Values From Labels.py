### brute
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        def fun(x):
            return -x[0]
        z=list(zip(values,labels))
        z=sorted(z,key=fun)
        d={}
        n=0
        used=0
        result=0
        for i in labels:
            if i not in d:
                d[i]=0
        #print(z)
        while used<num_wanted and n<len(values):
            if d[z[n][1]]<use_limit:
                result+=z[n][0]
                d[z[n][1]]+=1
                used+=1
            n+=1
            #print(d)
        return result

##another approach using dictionary
    
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        D={}
        S=[]
        for i,x in enumerate(labels):
            if x in D:
                D[x].append(values[i])
            else:
                D[x]=[values[i]]
        for l,vals in D.items():
            vals.sort(reverse=True)
            if len(vals)<use_limit:
                S.extend(vals[:])
            else:
                S.extend(vals[:use_limit])
            #print(S)
        S.sort(reverse=True)
        return sum(S[:num_wanted])
