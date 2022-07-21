# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        
            
        n = 0
        if left>1:
            flag = True
        else:
            flag = False
        temp = head
        while(temp):
            n+=1
            temp = temp.next
        
        
        prevNode = None
        curr = head
        
        while(left-1):
            prevNode = curr
            curr = curr.next
            left-=1
        
        leftNode = curr
        
        rightNode = head
        
        while(right-1):
            rightNode = rightNode.next
            right-=1
            
        nextNode = rightNode.next
        if flag:
            prevNode.next = rightNode
        
        rightNode.next = None
        
        curr = leftNode
        prev = nextNode
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        if flag:
            return head
        return rightNode
        
        