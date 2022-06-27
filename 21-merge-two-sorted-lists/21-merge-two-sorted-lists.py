# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        elif list1==None and list2!=None:
            return list2
        elif list1!=None and list2==None:
            return list1
        
        p = ListNode()
        head = p
        count = 0
        
        while list1!=None and list2!=None:
            
            if count>0:
                p.next = ListNode()
                p = p.next
                
            if list1.val>list2.val:
                p.val = list2.val
                list2 = list2.next
            else:
                p.val = list1.val
                list1 = list1.next
            count+=1
        
        if list1!=None:
            p.next = list1
        elif list2!=None:
            p.next = list2
        return head