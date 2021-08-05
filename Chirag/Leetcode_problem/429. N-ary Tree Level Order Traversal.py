"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue=[[root,1]]
        prevdepth=1
        temp=[]
        while queue:
            head,depth=queue.pop(0)
            if prevdepth<depth:
                result.append(temp[:])
                temp.clear()
                prevdepth=depth
            temp.append(head.val)
            
            for child in head.children:
                queue.append([child,1+depth])
        result.append(temp[:])
        return result
        
