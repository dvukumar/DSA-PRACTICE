# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        arr = []
        curr = head
        
        while curr:
            val = curr.val
            arr.append(val)
            curr = curr.next
        
        n = len(arr)
        flag = True
        for i in range(len(arr)):
            val1 = arr[i]
            val2 = arr[n-i-1]
            if val1==val2:
                flag = True
            else:
                flag = False
                break
        return flag