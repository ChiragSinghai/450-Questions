import heapq
def solution(A):
    l=[-i for i in A]
    heapq.heapify(l)
    while len(l)>1:
        first=heapq.heappop(l)
        second=heapq.heappop(l)
        if second>first:
            heapq.heappush(l,first-second)
    l.append(0)
    return abs(l[0])
if __name__=='__main__':
    A=[2,7,4,1,8,1]
    print(solution(A))
