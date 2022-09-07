# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        level = 1
        queue = [[root,0]]
        max_ = 0
        while(queue):
            start = queue[0][1]
            end = queue[-1][1]
            max_ = max(max_,end-start+1)
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                idx = node[1]
                if node[0].left:
                    queue.append([node[0].left,2*idx+1])
                if node[0].right:
                    queue.append([node[0].right,2*idx+2])
            
            
        return max_
                
               
                
            