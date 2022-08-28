# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        dict = defaultdict(list)
        def dfs(root,level,x,y):
            if not root:
                return
            if root.left:
                if root.left.val==x or root.left.val==y:
                    
                    left = [root.val,root.left.val]
                    dict[level+1].append(left)
            if root.right:
                if root.right.val==x or root.right.val==y:
                    right = [root.val,root.right.val]
                    dict[level+1].append(right)
            dfs(root.left,level+1,x,y)
            dfs(root.right,level+1,x,y)
        
        dfs(root,0,x,y)
        keys = list(dict.keys())
        print(dict)
        
        if len(keys)==1:
            key = keys[0]
            arr = dict[key]
            if len(arr)>1:
                if arr[0][0]!=arr[1][0]:
                    return True
        return False
            
            