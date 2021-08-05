# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result=[]
        count = -1
        while queue:
            count+=1
            tmp=[]
            for _ in range(len(queue)):
                head=queue.pop(0)
                tmp.append(head.val)
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
            if count%2==1:
                tmp.reverse()
            result.append(tmp)
        return result     
