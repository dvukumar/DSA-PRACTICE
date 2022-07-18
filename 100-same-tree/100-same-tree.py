# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def findSame(p,arr):
            if p is None:
                arr.append(False)
                return arr
            else:
                arr.append(p.val)
                left = findSame(p.left,arr)
                right = findSame(p.right,arr)
                return arr
        val1 = findSame(p,arr1)
        val2 = findSame(q,arr2)
        print(val1,val2)
        return val1==val2
                
            
            


            
        