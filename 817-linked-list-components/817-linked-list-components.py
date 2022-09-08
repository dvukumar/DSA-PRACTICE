# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        curr = head
        flag = True
        res = 0
        while(curr):
            val = curr.val
            curr = curr.next
            
            if val in nums:
                nums.remove(val)
                if flag:
                    res+=1
                    flag = False
            else:
                flag = True
        return res
        