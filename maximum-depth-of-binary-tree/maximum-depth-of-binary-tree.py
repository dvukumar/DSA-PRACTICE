# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def findmax(root):
            if not root:
                return 0
            left = findmax(root.left)
            right = findmax(root.right)
            return 1+max(left,right)
        res = findmax(root)
        return res