# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        curr_o = head
        curr_e = head.next
        start_e = curr_e
        start_o = curr_o
        while(curr_o and curr_e):
            
            prev_o = curr_o
            temp_o = curr_e.next
            curr_o.next = temp_o
            curr_o = temp_o
            if temp_o:
                temp_e = temp_o.next
                curr_e.next = temp_e
                curr_e = temp_e
        curr = prev_o
        while(curr):
            prev_o = curr
            curr = curr.next
        prev_o.next = start_e
        return start_o
            