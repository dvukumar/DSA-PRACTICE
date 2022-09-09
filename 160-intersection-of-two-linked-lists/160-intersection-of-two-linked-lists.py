# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    
        dict = {}
        
        currA = headA
        while(currA):
            dict[currA] = True
            currA = currA.next
        
        currB = headB
        while(currB):
            if currB in dict:
                return currB
            currB = currB.next
        
        return None