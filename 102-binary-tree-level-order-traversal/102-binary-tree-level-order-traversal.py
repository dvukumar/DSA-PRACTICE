# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dict = defaultdict(list)
        
        def lot(root,level):
            if not root:
                return
            dict[level].append(root.val)
            lot(root.left,level+1)
            lot(root.right,level+1)
        
        lot(root,0)
        ans = list(dict.values())
        return ans