# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        arr = []
        def tree(root,flag,res):
            if root is None:
                return
            
            tree(root.left,True,res)
            tree(root.right,False,res)
            #print(root.val,flag)
            if flag:
                if not root.left and not root.right:
                    arr.append(root.val)
         
        res = 0
        tree(root,False,res)
    

        return sum(arr)