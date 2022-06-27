# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        prev = None
        curr = head
        next = head.next
        flag = False
        while(next):
            
            if next.val==curr.val:
                next = next.next
                curr = curr.next
                
                flag = True
            elif next.val!=curr.val and flag==True:
                next = next.next
                curr = curr.next
                flag = False
                if prev!=None:
                    
                    prev.next = curr
                    
                else:
                    head = curr
                    
            else:
                prev = curr
                curr = next
                next = next.next
        if flag==True:
            if prev==None:
                return None
            else:
                prev.next = None
        return head