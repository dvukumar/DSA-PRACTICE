class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        for i in edges[0]:
            count = 0
            for edge in edges:
                if i in edge:
                    count+=1
            if count==n:
                return i
            
                