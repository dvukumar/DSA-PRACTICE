# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    
        temp1 = headA
        temp2 = headB
        count1 = 0
        count2 = 0
        while(True):
            if not temp1:
                if count1==0:
                    temp1 = headB
                    count1+=1
                else:
                    return None
            if not temp2:
                if count2==0:
                    temp2 = headA
                    count2+=1
                else:
                    return None
            if temp1==temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next