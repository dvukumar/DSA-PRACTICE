# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        arr = []
        
        def dfs(root,target,temp):
            nonlocal arr
            if not root:
                return
            # if target<0:
            #     temp.pop()
            #     return
            
            temp.append(root.val)
            #print(temp)
            if root.val==target and not root.left and not root.right:
                arr.append(list(temp))
            left = dfs(root.left,target-root.val,temp)
         
            right = dfs(root.right,target-root.val,temp)
            temp.pop(-1)
            #print(target,temp)
            
            
        dfs(root,targetSum,[])
        return arr
            