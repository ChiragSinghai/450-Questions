
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(head,left,right):
            if not left<head.val<right:
                return False
            if head.left:
                if not helper(head.left,left,head.val):
                    return False
            if head.right:
                if not helper(head.right,head.val,right):
                    return False
            return True
        return helper(root,-2**31-1,2**31+1)
    
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(head,left,right):
            if not head:
                return True
            if not left<head.val<right:
                return False
            return (helper(head.left,left,head.val) and
                    helper(head.right,head.val,right))
                    
        return helper(root,-2**31-1,2**31+1)        
