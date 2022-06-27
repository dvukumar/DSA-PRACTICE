# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        curr = head
        next = curr.next
        
        while(next):
            curr_val = curr.val
            next_val = next.val
            
            if curr_val==next_val:
                next = next.next
                curr.next = next
            else:
                curr = curr.next
                next = next.next
            
        return head