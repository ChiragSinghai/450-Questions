def circularPermutation(n, start):
    tab=[0]
    x=0
    while x<n:
        l=1<<x
        for i in range(l-1,-1,-1):
            tab.append(l|tab[i])
        x+=1
    count=0
    while tab[count]!=start:
        count+=1
    return tab[count:]+tab[0:count]
    
print(circularPermutation(5,6))
