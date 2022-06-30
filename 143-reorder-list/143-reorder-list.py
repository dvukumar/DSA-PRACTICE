# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow,fast = head,head.next
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = None
        slow.next = None
        #print(second)
        
        while(second):
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        second = prev
        first = head
        while(second):
            next_first = first.next
            next_second = second.next
            
            first.next = second
            second.next = next_first
            
            first = next_first
            second = next_second