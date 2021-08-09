class Solution:
    def reorganizeString(self,s):
        D={}
        for i in s:
            if i not in D:
                D[i]=0
            D[i]+=1
        heap=[]
        for i,j in D.items():
            heappush(heap,(-j,i))
        
        res = ""
        prev_freq, prev_ch = heapq.heappop(heap)
        res += prev_ch
        while heap:
            curr_freq, curr_ch = heapq.heappop(heap)
            res += curr_ch
            if prev_freq < -1: 
                heapq.heappush(heap, (prev_freq + 1, prev_ch))
            prev_freq, prev_ch = curr_freq, curr_ch
            
        if len(s) != len(res):
            return ""
        return res
                
