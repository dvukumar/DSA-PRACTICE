# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        arr = []
        flag = True
        def HeightOfTree(root):
            nonlocal flag
            
            if root is None:
                return 0
            else:
                leftNode = HeightOfTree(root.left)
                rightNode = HeightOfTree(root.right)
                diff = abs(leftNode - rightNode)
                if diff>1:
                    flag = False
                    # arr.append(flag)
                
                
                return 1+max(leftNode,rightNode)
        res = HeightOfTree(root)
        return flag