# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        arr = []
        root_val = root.val
        s = ""
        
        def treepath(root,s):
            if root is None:
                return False
            
            val = root.val
            if s:
                s = s + "->" + str(val)
            else:
                s+=str(val)
            left = treepath(root.left,s)
            right = treepath(root.right,s)
            print(left,right,s)
            if left==False and right==False:
                arr.append(str(s))
            s = s[:-3]
        treepath(root,s)
        return arr

                