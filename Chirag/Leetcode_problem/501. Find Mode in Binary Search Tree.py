class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        self.count=0
        self.c=0
        self.prev=None
        def inorder(head):
            #self.prev=head.val
            if head.left:
                inorder(head.left)
            if head.val==self.prev:
                self.count+=1
            else:
                self.count=1
                self.prev=head.val
            
            if self.count==self.c:
                self.ans.append(head.val)
            if self.count>self.c:
                self.ans=[head.val]
                self.c=self.count
            #self.prev=head.val    
            if head.right:
                inorder(head.right)
        inorder(root)
        print(self.c)
        return self.ans
