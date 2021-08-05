# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not k or not head or not head.next:
            return head
        
        temp=head
        totalNode=1
        while temp.next:
            totalNode+=1
            temp=temp.next
        if k>totalNode:
            k=k%totalNode
        if k==totalNode or not k:
            return head
        
        totalNode = totalNode-k-1
        temp=head
        for _ in range(totalNode):
            temp=temp.next
        newhead=temp.next
        temp.next=None
        temp = newhead
        for _ in range(k-1):
            temp=temp.next
        temp.next=head
        
        return newhead
    
            
            
        
