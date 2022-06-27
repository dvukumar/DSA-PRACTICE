# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = head
        next = prev.next
        
        while(prev and next):
            prev_val = prev.val
            next_val = next.val
            
            prev.val = next_val
            next.val = prev_val
            
            prev = next.next
            if prev:
                next = prev.next
            
            #print(prev)
            #print(next)
        
        return head