class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head and head.val==val:
            head=head.next
        if not head:
            return head
        prev=head
        nex=prev.next
        
        while nex:
            if nex.val==val:
                prev.next=nex.next
            else:
                prev=prev.next
            nex=nex.next
            
        return head
