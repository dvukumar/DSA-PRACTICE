# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        res = []
        a = root.val
        res.append(a)
        queue = [root]
        while(queue):
            
            count = 0
            n = len(queue)
            count = 0
            sum = 0
            for i in range(n):
                q = queue.pop(0)
                if q.left and q.right:
                    queue.append(q.left)
                    queue.append(q.right)
                    sum+=q.left.val+q.right.val
                    count+=2
                elif q.left:
                    queue.append(q.left)
                    sum+=q.left.val
                    count+=1
                elif q.right:
                    queue.append(q.right)
                    sum+=q.right.val
                    count+=1
            
            if count>0:
                ans = sum/count
                
                res.append(ans)
        return res
                
        