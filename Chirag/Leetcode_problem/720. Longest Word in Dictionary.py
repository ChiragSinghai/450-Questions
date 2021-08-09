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
