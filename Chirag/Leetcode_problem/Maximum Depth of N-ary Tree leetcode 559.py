"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(head):
            if not head:
                return 0
            depth=0
            for child in head.children:
                depth=max(depth,dfs(child))
            return 1+depth
        return dfs(root)
        '''
        if not root:
            return 0
        queue=[[root,1]]
        maxdepth=0
        while queue:
            head,depth=queue.pop(0)
            for child in head.children:
                queue.append([child,depth+1])
            maxdepth=max(depth,maxdepth)
        return maxdepth
        '''
