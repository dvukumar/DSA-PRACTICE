# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        duplicate = ListNode()
        dummy = duplicate
        prev = None
        while(curr):
            
            dummy.val = curr.val
            curr = curr.next
            dummy.next = ListNode()
            prev = dummy
            dummy = dummy.next
        prev.next = None
        
        curr = duplicate
        prev = None
        
        while(curr):
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        
        curr1 = head
        curr2 = prev
        
        while(curr1 and curr2):
            if curr1.val!=curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        
        return True
        
        
            
        