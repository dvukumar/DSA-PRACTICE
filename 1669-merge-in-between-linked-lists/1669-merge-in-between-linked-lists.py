# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        head1 = list1
        head2 = list2
        
        prev = None
        curr = head2
        while(curr):
            prev = curr
            curr = curr.next
        rightMost = prev
        
        curr = head1
        n = 1
        while(curr):
            if n==a:
                left = curr
            elif n==b+2:
                right = curr
                break
            curr = curr.next
            n+=1
            
        left.next = head2
        rightMost.next = right
        return head1