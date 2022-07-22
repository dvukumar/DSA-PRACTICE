"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hash = {}
        
        def dfs(node):
            if node is None:
                return None
            if node in hash:
                return hash[node]
            
            copyNode = Node(node.val)
            hash[node] = copyNode
            
            for neighbor in node.neighbors:
                copyNeighbor  = dfs(neighbor)
                copyNode.neighbors.append(copyNeighbor)
            return copyNode
        print(hash)
        return dfs(node)
            