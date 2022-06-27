# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        prev = head
        curr = head.next
        
        while(curr):
            
            if curr.val==val:
                curr = curr.next
                prev.next = curr
                
            else:
                curr = curr.next
                prev = prev.next
        if head.val == val:
            return head.next
        else:
            return head
        
        