# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        curr = head.next
        currRes = res
        sum = 0
        prev = None
        while(curr):
            if curr.val!=0:
                val = curr.val
                sum+=val
            else:
                currRes.val = sum
                prev = currRes
                currRes.next = ListNode()
                currRes = currRes.next
                sum = 0
            #print(res)
            curr = curr.next
        prev.next = None
        
        return res
        
        