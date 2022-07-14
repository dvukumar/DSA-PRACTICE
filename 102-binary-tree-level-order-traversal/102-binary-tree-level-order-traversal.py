# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dict = defaultdict(list)
        
        def Lot(root,level):
            if not root:
                return None
            
            dict[level].append(root.val)
            Lot(root.left,level+1)
            Lot(root.right,level+1)
            
        Lot(root,0)
        return dict.values()
            