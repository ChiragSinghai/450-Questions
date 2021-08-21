class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.A=[]
        def inorder(head):
            if head.left:
                inorder(head.left)
            self.A.append(head.val)
            if head.right:
                inorder(head.right)
        inorder(root)
        return self.A
