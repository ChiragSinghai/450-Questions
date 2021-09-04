
def mostVisited(n, rounds):
    ans=[]
    if rounds[0]<rounds[-1]:
        for i in range(rounds[0],rounds[-1]+1):
            ans.append(i)
    elif rounds[0]>rounds[-1]: 
        for i in range(1,rounds[-1]+1):
            ans.append(i)
        for i in range(rounds[0],n+1):
            ans.append(i)
    else:
        return [rounds[-1]]
        
    return ans
        
