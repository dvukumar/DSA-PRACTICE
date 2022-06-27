# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        curr = head
        
        n = 0
        while(curr):
            curr = curr.next
            n+=1
        k = k%n
        curr = head
        next = curr.next
        while(k):
            temp = curr.val
            while(next):
                
                next_val = next.val
                
                next.val = temp
                temp  =next_val
                
                next = next.next
            curr.val = temp
            curr = head
            next = curr.next
            k-=1
        
        return curr
                