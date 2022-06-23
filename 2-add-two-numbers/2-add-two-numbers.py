# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = 0
        num2 = 0
        
        temp1 = l1
        i1 = 0
        while(temp1):
            val = temp1.val
            num1 = num1+(10**i1)*val
            temp1 = temp1.next
            i1+=1
        
        temp2 = l2
        i2 = 0
        while(temp2):
            val = temp2.val
            num2 = num2+(10**i2)*val
            temp2 = temp2.next
            i2+=1
        
        num = num1+num2
        
        l = ListNode()
        l.val = None
        curr = l
        s = str(num)
        n = len(s)
        while(n):
            val = num%10
            curr.val = val
            num = num//10
            n-=1
            if n>0:
                next = ListNode()
                next.val = None
                curr.next = next
                curr = curr.next
        return l
            