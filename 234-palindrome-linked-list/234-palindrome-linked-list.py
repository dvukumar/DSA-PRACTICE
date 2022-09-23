# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        def reverse(curr):
            prev = None
            while(curr):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        slow,fast = head,head
        
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        
        slow.next = reverse(slow.next)
        slow = slow.next
        fast = head
        while(slow):
            if fast.val!=slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True