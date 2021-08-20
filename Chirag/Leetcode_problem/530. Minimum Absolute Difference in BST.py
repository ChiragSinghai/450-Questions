class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.A=[]
        def preorder(head):
            if head:
                preorder(head.left)
                self.A.append(head.val)
                preorder(head.right)
        preorder(root)
        res=float("inf")
        for i in range(1,len(self.A)):
            res=min(res,self.A[i]-self.A[i-1])
        return res
#faster solution
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        
        self.res=10**5+1
        self.last_value=-10**5+1
        def preorder(head):
            if head.left:
                preorder(head.left)
            
            self.res=min(self.res,head.val-self.last_value)
            self.last_value=head.val
            if head.right:
                preorder(head.right)    
        preorder(root)
        #for i in range(1,self.count):
            #res=min(res,A[i]-A[i-1])
        return self.res
