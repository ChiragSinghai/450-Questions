import heapq
def longestDiverseString(a, b, c):
    if a<=2 and b<=2 and c<=2:
        return 'a'*a+'b'*b + 'c'*c
    res=''
    heap=[]
    if a:heapq.heappush(heap,(-a,'a'))
    if b:heapq.heappush(heap,(-b,'b'))
    if c:heapq.heappush(heap,(-c,'c'))
    while len(heap)>1:
        c1,l1=heapq.heappop(heap)
        c2,l2=heapq.heappop(heap)
        if c1==c2:
            res+=l1+l2
            c2+=1
            c1+=1
        else:
            res+=l1*2+l2
            c1+=2
            c2+=1
        if c1<0:
            heapq.heappush(heap,(c1,l1))
        if c2<0:
            heapq.heappush(heap,(c2,l2))
    if heap:
        c1,l1=heapq.heappop(heap)
        res+=l1*min(-c1,2)
    return res
print(longestDiverseString(1,3,5))
