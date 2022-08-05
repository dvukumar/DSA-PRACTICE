# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(root,p,q):
            if not root:
                return
            if (p.val<root.val and q.val>root.val) or (p.val>root.val and q.val<root.val):
                return root
            elif p.val<root.val and q.val<root.val:
                return lca(root.left,p,q)
            elif p.val>root.val and q.val>root.val:
                return lca(root.right,p,q)
            elif p.val==root.val:
                return p
            elif q.val==root.val:
                return q
        return lca(root,p,q)
                