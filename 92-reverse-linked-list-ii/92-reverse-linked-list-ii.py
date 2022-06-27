# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        count = 1
        n = right - left
        if n%2==0:
            n = (right - left)//2
        else:
            n = (right - left)//2 + 1
        arr = []
        temp = head
        
        while temp:
            val = temp.val
            arr.append(val)
            temp = temp.next
        
        for i in range(n):
            arr[left-1],arr[right-1] = arr[right-1],arr[left-1]
            left = left+1
            right = right - 1
        
        i = 0
        temp = head
        while temp:
            temp.val = arr[i]
            temp = temp.next
            i+=1
        return head