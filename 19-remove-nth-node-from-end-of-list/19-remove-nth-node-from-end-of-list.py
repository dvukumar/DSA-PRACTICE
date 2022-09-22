# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        start = head
        slow = head
        fast = head
        
        i = 0
        while(i<n-1):
            fast = fast.next
            i+=1
        prev = ListNode(-1)
        while(fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next
        if prev.val!=-1:
            prev.next = slow.next
            return start
        return start.next