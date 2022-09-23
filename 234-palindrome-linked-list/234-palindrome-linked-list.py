# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        dummy = ListNode()
        temp = dummy
        curr = head
        while(curr):
            
            temp.next = ListNode(curr.val)
            temp = temp.next
            curr = curr.next
        
        prev = None
        curr = dummy.next
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev
        
        curr1 = head
        curr2 = head2
        #print(curr1,curr2)
        while(curr1 and curr2):
            if curr1.val!=curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
      
        return True
        