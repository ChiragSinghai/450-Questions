class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(root1,root2):
            if not root1 or not root2:
                return not root1 and not root2
            if root1.val!=root2.val:
                return False
            return ((helper(root1.left,root2.left) and helper(root1.right,root2.right))
             or (helper(root1.left,root2.right) and helper(root1.right,root2.left)))
        return helper(root1,root2)
