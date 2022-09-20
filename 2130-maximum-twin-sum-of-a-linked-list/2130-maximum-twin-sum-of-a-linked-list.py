# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        curr1 = head
        slow,fast = head,head.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        curr2 = slow.next
        slow.next = None
        
        prev = None
        while(curr2):
            temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = temp
        
        curr2 = prev
        
        maxRes = 0
        while(curr1 and curr2):
            res = curr1.val + curr2.val
            maxRes = max(maxRes,res)
            curr1 = curr1.next
            curr2 = curr2.next
        
        return maxRes
            
        