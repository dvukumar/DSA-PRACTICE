# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        n1 = 0
        n2 = 0
        
        currA = headA
        currB = headB
        
        while(currA or currB):
            if currA:
                n1+=1
                currA = currA.next
            if currB:
                n2+=1
                currB = currB.next
        
        currA = headA
        currB = headB
        
        if n2>n1:
            while(n2>n1):
                currB = currB.next
                n2-=1
        else:
            while(n1>n2):
                currA = currA.next
                n1-=1
        
        while(currA and currB):
            if currA==currB:
                return currA
            
            currA = currA.next
            currB = currB.next
        
        return None