# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def Tree(left,right):
            if left>right:
                return
            index = (left+right)//2
            tree = TreeNode(nums[index])
            tree.left = Tree(left,index-1)
            tree.right = Tree(index+1,right)
            return tree
        return Tree(0,len(nums)-1)