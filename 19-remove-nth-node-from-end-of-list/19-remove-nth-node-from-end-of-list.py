# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        t = 1
        temp = head
        while(temp.next):
            t+=1
            temp = temp.next
        
        prev = None
        curr = head
        nxt = curr.next
        
        count =t-n
        if count==0:
            return head.next
        #print(count)
        while(count):
            prev = curr
            curr = nxt
            nxt = nxt.next
            count-=1
            #print(nxt)
        prev.next = nxt
        
        return head
        