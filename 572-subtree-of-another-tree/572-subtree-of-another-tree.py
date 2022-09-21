# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare(root1,root2):
            queue1 = [root1]
            queue2 = [root2]
            
            while(queue1 and queue2):
                node1 = queue1.pop(0)
                node2 = queue2.pop(0)
                
                if node1.val!=node2.val:
                    return False
                if node1.left and node2.left:
                    
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                
                elif node1.left:
                    return False
                elif node2.left:
                    return False
                
                if node1.right and node2.right:
                    
                    queue1.append(node1.right)
                    queue2.append(node2.right)
                
                elif node1.right:
                    return False
                elif node2.right:
                    return False
            if queue1:
                return False
            elif queue2:
                return False
            else:
                return True
        res = []  
        def dfs(root,subRoot):
            
            if not root:
                return 
            flag =  compare(root,subRoot)
            res.append(flag)
            dfs(root.left,subRoot)
            dfs(root.right,subRoot)
        dfs(root,subRoot)
        return True in res