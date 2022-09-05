"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        queue = [root]
        if not root:
            return root
        
        while(queue):
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
                    node.left.next = node.right
                    if node.next:
                        node.right.next = node.next.left
        return root
                    