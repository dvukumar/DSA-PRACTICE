"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return root
        queue = [root]
        res = []
        while(queue):
            arr = []
            n = len(queue)
            for i in range(n):
                a = queue.pop(0)
                arr.append(a.val)
                
                for c in a.children:
                    queue.append(c)
            res.append(arr)
        return res