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
        
    def search(self,curr,change,i,word):
        if i==len(word):
            return change==1 and curr.isEnd
        elif change>1:
            return False
        ans=False
        for w in curr.child:
            ans= ans or self.search(curr.child[w],change+int(word[i]!=w),i+1,word)
        return ans
        
        
class MagicDictionary:
    def __init__(self):
        self.root=TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.root.insert(word)
    def search(self, searchWord: str) -> bool:
        return self.root.search(self.root,0,0,searchWord)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
