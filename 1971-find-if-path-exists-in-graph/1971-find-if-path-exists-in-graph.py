class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj = [[] for _ in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False]*n
        queue = [source]
        while(queue):
            curr = queue.pop(0)
            visited[curr] = True
            
            for node in adj[curr]:
                if visited[node] is False:
                    queue.append(node)
        return visited[destination]
            
        
        
            