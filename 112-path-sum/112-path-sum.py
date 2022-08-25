# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def path(root,s,target,flag):
            if flag==True:
                return flag
            
            if not root.left and not root.right and s==target:
                flag = True
                return flag
            
            if root.left:
                flag = path(root.left,s+root.left.val,target,flag)
            if root.right:
                flag = path(root.right,s+root.right.val,target,flag)
            return flag
        
        if not root:
            return False
        return path(root,root.val,targetSum,False)