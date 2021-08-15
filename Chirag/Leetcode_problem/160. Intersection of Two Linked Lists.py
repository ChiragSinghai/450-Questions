# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getlength(head):
            l=0
            while head:
                l+=1
                head=head.next
            return l
        A=getlength(headA)
        B=getlength(headB)
        while headB and A<B:
            headB=headB.next
            B-=1
        while headA and A>B:
            headA=headA.next
            A-=1
        while headA and headB and headA!=headB:
            headA=headA.next
            headB=headB.next
        return headA
        
            
        
