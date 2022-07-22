# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        curr = head
        curr1 = head
        listMin = ListNode()
        currMin = listMin
        prevMin = None
        listMax = ListNode()
        currMax = listMax
        prevMax = None
        while curr:
            val = curr.val
            if val<x:
                currMin.val = val
                currMin.next = ListNode()
                prevMin = currMin
                currMin = currMin.next
                
            else:
                currMax.val = val
                currMax.next = ListNode()
                prevMax = currMax
                currMax = currMax.next
            curr = curr.next
        
        if prevMin:   
            if prevMax:
                prevMin.next = listMax
            else:
                prevMin.next = None
        
            
        if prevMax:
            prevMax.next = None
        
        if not prevMin:
            return listMax
        return listMin