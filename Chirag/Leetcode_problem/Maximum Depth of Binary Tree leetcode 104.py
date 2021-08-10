class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(head):
            if not head:
                return 0
            left = dfs(head.left)
            right = dfs(head.right)
            return 1+max(left,right)
        return dfs(root)
