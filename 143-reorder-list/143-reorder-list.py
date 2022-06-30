# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        
        temp = head
        n = 0
        while(temp):
            val = temp.val
            arr.append(val)
            n+=1
            temp = temp.next
        
        i = 0
        while(i<n):
            if i%2==1:
                end_val = arr.pop()
                arr.insert(i,end_val)
            i+=1
        
        curr = head
        i = 0
        while(curr):
            curr.val = arr[i]
            i+=1
            curr = curr.next
        return head
        