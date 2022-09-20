# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dict = {}
        curr = head
        n = 1
        while(curr):
            dict[n] = curr.val
            curr = curr.next
            n+=1
        
        size = n-1
        curr = head
        n = 1
        while(curr):
            if n==k:
                curr.val = dict[size-k+1]
            elif n==size-k+1:
                curr.val = dict[k]
            curr = curr.next
            n+=1
        #print(dict)
        return head
                