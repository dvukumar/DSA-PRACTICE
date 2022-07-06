# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        if not head.next:
            return head
        
        head.val,head.next.val = head.next.val,head.val
        
        if head.next.next:
            Solution.swapPairs(self,head.next.next)
        
        return head