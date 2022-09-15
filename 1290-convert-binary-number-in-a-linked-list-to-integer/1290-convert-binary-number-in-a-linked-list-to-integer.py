# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        n = 0
        curr = head
        while(curr):
            n+=1
            curr = curr.next
        
        i = 1
        res = 0
        curr = head
        while(curr):
            val = curr.val
            res += val*2**(n-i)
            i+=1
            curr = curr.next
        
        return res
            