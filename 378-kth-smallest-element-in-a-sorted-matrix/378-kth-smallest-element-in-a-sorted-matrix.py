class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        arr = []
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                arr.append(val)
        
        arr.sort()
        return arr[k-1]