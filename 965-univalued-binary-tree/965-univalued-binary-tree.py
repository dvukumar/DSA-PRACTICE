# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root,val,flag):
            if not root:
                return flag
            if root.val!=val:
                flag = False
                return flag
            flag = dfs(root.left,val,flag) and dfs(root.right,val,flag)
            return flag
        
        flag = dfs(root,root.val,True)
        return flag
        
            