# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        order = [(root, -2147483649, 2147483648)]

        while order:
            node, left_bound, right_bound = order.pop()

            if node.right:
                if node.right.val <= node.val or node.right.val >= right_bound:
                    return False
                order.append((node.right, node.val, right_bound))

            if node.left:
                if node.left.val >= node.val or node.left.val <= left_bound:
                    return False
                order.append((node.left, left_bound, node.val))
        return True
            