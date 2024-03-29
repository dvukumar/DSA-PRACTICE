# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            
            if root.left and root.right:
                return 1+min(dfs(root.left),dfs(root.right))
            if root.left:
                return 1+dfs(root.left)
            if root.right:
                return 1+dfs(root.right)
            else:
                return 1
        
        res = dfs(root)
        return res if root else 0