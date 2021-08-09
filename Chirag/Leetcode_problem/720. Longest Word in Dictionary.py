class TrieNode:
    def __init__(self):
        self.child={}
        self.isEnd=False
    def insert(self,word):
        cur=self
        for ch in word:
            if ch not in cur.child:
                cur.child[ch]=TrieNode()
            cur=cur.child[ch]
        cur.isEnd=True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.root=TrieNode()
        for word in words:
            self.root.insert(word)
        self.root.isEnd=True
        return self.longest(self.root,'')
    def longest(self,curr,res):
        if not curr.isEnd:
            return res[:-1]
        previous=res
        for letter in curr.child:
            new = self.longest(curr.child[letter],res+letter)
            if len(new)>len(previous):
                previous=new
            elif len(new)==len(previous):
                previous=min(new,previous)
        return previous

#another approach
    
'''
class Solution:
    def longestWord(self, words: List[str]) -> str:
        D={}
        L=[0]*31
        maxlen=0
        for word in words:
            l=len(word)
            maxlen=max(l,maxlen)
            if l not in D:
                D[l]=set()
            if L[l]==0:
                L[l]=[word]
                continue
            L[l].append(word)
        #print(D)
        #print(L)
        if L[1]==0:
            return ''
        D[1]=set(L[1])
        
        i=2
        while i<=maxlen:
            if L[i]==0:
                break
            for item in L[i]:
                if item[0:i-1] in D[i-1]:
                    D[i].add(item)
            
            i+=1
        while maxlen:
            if maxlen in D and D[maxlen]:
                return sorted(D[maxlen])[0]
            maxlen-=1
'''
